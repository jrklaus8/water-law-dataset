#!/usr/bin/env python3
"""Outcome coding for Dutch (Rechtspraak.nl) decisions: FUTURE_WORK.md Priority 1.

Standard library only. Resumable: results are appended to a JSONL checkpoint, one line per ECLI.

What it does
  1. Fetches the full XML of an ECLI from data.rechtspraak.nl (public Open Data, about 10 requests per second allowed).
  2. Extracts the dispositive part (the paragraphs after the last "Beslissing" heading, or after the last
     "De Afdeling/De rechtbank ... :" operative lead-in when no heading exists).
  3. Applies rule-based classification to the ordered operative clauses and records WHICH rule fired.
  4. Anything the rules do not resolve is labelled UNCLASSIFIED for LLM or human review (never guessed).

Labels (perspective: the party whose challenge the court decided, i.e. the appellant or applicant at the
instance that produced this decision; see the `multi_step` flag for chains that overturn and re-decide):
  WIN, LOSS, PARTIAL, INADMISSIBLE, REMAND, INTERIM (tussenuitspraak, no final outcome yet), NO_MERITS_RULING
  (withdrawn, costs-only), UNCLASSIFIED, NO_TEXT, FETCH_FAILED.

Known limits (also written to the output so nobody forgets them)
  * "WIN" means the challenge was upheld, not that the appellant was an individual or that water access improved.
    Appellant identity is NOT coded here (see FUTURE_WORK.md, optional extension).
  * Where an appeal court upholds the hoger beroep, annuls, and then itself decides the original beroep, the
    label follows the FINAL merits clause on the original proceeding and `multi_step` is set to 1.
  * Rule precision is unmeasured until a manual sample is coded; use validation/ for that.

Usage
  python utils/nl_outcome_coding.py fetch  --ids ids.txt --out outcomes.jsonl [--rate 8]
  python utils/nl_outcome_coding.py classify-text "verklaart het beroep gegrond"
"""
import argparse
import json
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE = "https://data.rechtspraak.nl/uitspraken/content?id="
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")

# Operative clause patterns. Order within a clause list is by position in the text, not by this table.
# Each entry: (compiled regex, kind). "kind" is later mapped to a label.
CLAUSES = [
    (re.compile(r"verklaart\s+(?:het|de|zowel\s+het)\s+(?:\w+\s+){0,3}?(?:beroep|beroepen|bezwaar|bezwaren|verzet|hoger beroep|verzoek)\b[^;:]{0,160}?gedeeltelijk\s+gegrond"), "partial"),
    (re.compile(r"verklaart\s+(?:het|de|zowel\s+het)\s+(?:\w+\s+){0,3}?(?:beroep|beroepen|bezwaar|bezwaren|verzet|hoger beroep|verzoek)\b[^;:]{0,160}?(?:niet[- ]ontvankelijk)"), "inadmissible"),
    (re.compile(r"verklaart\s+(?:het|de|zowel\s+het)\s+(?:\w+\s+){0,3}?(?:beroep|beroepen|bezwaar|bezwaren|verzet|hoger beroep|verzoek)\b[^;:]{0,160}?ongegrond"), "dismissed"),
    (re.compile(r"verklaart\s+(?:het|de|zowel\s+het)\s+(?:\w+\s+){0,3}?(?:beroep|beroepen|bezwaar|bezwaren|verzet|hoger beroep|verzoek)\b[^;:]{0,160}?gegrond"), "upheld"),
    (re.compile(r"verklaart\s+(?:het|de)\s+(?:\w+\s+){0,3}?(?:beroep|beroepen|bezwaar|hoger beroep)\s+(?:\w+\s+){0,6}?kennelijk\s+ongegrond"), "dismissed"),
    (re.compile(r"verklaart\s+zich\s+onbevoegd|onbevoegd\s+is\s+om\s+kennis\s+te\s+nemen|niet[- ]ontvankelijk"), "inadmissible"),
    (re.compile(r"bevestigt\s+de\s+(?:aangevallen|bestreden)\s+uitspraak|bekrachtigt\s+de\s+(?:aangevallen|bestreden)\s+uitspraak"), "dismissed"),
    (re.compile(r"wijst\s+(?:het|de)\s+(?:\w+\s+){0,3}?verzoek(?:en)?\s+(?:\w+\s+){0,4}?af\b|wijst\s+het\s+verzoek\s+om\s+voorlopige\s+voorziening\s+af|wijst\s+af\b"), "dismissed"),
    (re.compile(r"wijst\s+(?:het|de)\s+(?:\w+\s+){0,3}?verzoek(?:en)?\s+(?:\w+\s+){0,4}?toe\b|treft\s+(?:de\s+)?voorlopige\s+voorziening|schorst\s+(?:het\s+)?(?:\w+\s+)?besluit"), "upheld"),
    (re.compile(r"verwijst\s+de\s+zaak\s+(?:terug|naar)|draagt\s+(?:de\s+)?(?:\w+\s+){0,3}?op\s+een\s+nieuw\s+besluit|opnieuw\s+(?:te\s+)?beslissen|doet\s+de\s+zaak\s+zelf\s+af\s+niet"), "remand"),
    (re.compile(r"verklaart\s+(?:het\s+)?(?:hoger\s+)?beroep\s+(?:\w+\s+){0,3}?(?:ingetrokken|vervallen)|doet\s+aantekening\s+van\s+(?:de\s+)?intrekking|beroep\s+is\s+ingetrokken"), "procedural"),
    (re.compile(r"veroordeelt\s+(?:het\s+)?(?:college|de\s+\w+|\w+)\s+tot\s+(?:vergoeding\s+van\s+)?(?:de\s+)?proceskosten|wijst\s+af\b"), "costs"),
    (re.compile(r"vernietigt\s+(?:het|de)\s+(?:bestreden\s+)?(?:besluit|uitspraak|beschikking)"), "annul"),
    (re.compile(r"herroept\s+(?:het|de)|vernietigt\b"), "annul"),
]

HEADING = re.compile(r"^\s*(?:\d+\.\s*)?Beslissing\s*$", re.I)
LEADIN = re.compile(r"(?:De\s+Afdeling[^:]{0,120}|De\s+(?:voorzieningenrechter|rechtbank|enkelvoudige\s+kamer|meervoudige\s+kamer|Centrale\s+Raad[^:]{0,60}|Raad[^:]{0,60}|rechter)[^:]{0,120}|Het\s+College[^:]{0,120}|Het\s+Hof[^:]{0,120}|Hoge\s+Raad[^:]{0,60}):\s*$", re.I)


def _norm(t):
    return t.replace("\u2011", "-").replace("\u2010", "-").replace("\u00a0", " ")


def paragraphs(xml_text):
    """Return the uitspraak paragraphs as plain-text strings (tags removed, whitespace collapsed)."""
    start = xml_text.find("<uitspraak")
    body = xml_text[start:] if start >= 0 else xml_text
    paras = re.findall(r"<(?:para|title|nr)\b[^>]*>(.*?)</(?:para|title|nr)>", body, flags=re.S)
    out = []
    for p in paras:
        t = WS.sub(" ", _norm(TAG.sub(" ", p))).strip()
        if t:
            out.append(t)
    return out


def dispositive(paras):
    """Text of the operative part. Prefer the last 'Beslissing' heading; else the last court lead-in ending in ':'."""
    idx = None
    for i, p in enumerate(paras):
        if HEADING.match(p):
            idx = i + 1
    if idx is None:
        for i, p in enumerate(paras):
            if LEADIN.match(p) and len(p) < 240:
                idx = i + 1
    if idx is None:
        # Fallback: the last paragraphs before the signing block (decisions with neither a heading nor a lead-in).
        sign = None
        for i, p in enumerate(paras):
            if re.match(r"^(Aldus|Dit vonnis|Deze uitspraak is gedaan|Uitgesproken|w\.g\.)", p, re.I):
                sign = i
                break
        end = sign if sign is not None else len(paras)
        window = paras[max(0, end - 14):end]
        text = " ".join(window)[-3000:]
        return ("[fallback window] " + text) if re.search(r"verklaart|bevestigt|vernietigt|herroept|wijst|schorst|bepaalt", text, re.I) else ""
    tail = paras[idx:]
    # Stop at the signing block ("Aldus vastgesteld/gedaan/gewezen ...").
    keep = []
    for p in tail:
        if re.match(r"^(Aldus|Dit vonnis|Deze uitspraak|Uitgesproken|Aldus gewezen|Aldus gedaan|w\.g\.)", p, re.I):
            break
        keep.append(p)
    return " ".join(keep)[:4000]


def find_clauses(text):
    """Ordered list of (position, kind) for every operative clause found. Overlapping matches keep the first pattern."""
    hits = []
    taken = []
    for rx, kind in CLAUSES:
        for m in rx.finditer(text):
            s, e = m.span()
            if any(not (e <= a or s >= b) for a, b in taken):
                continue
            taken.append((s, e))
            hits.append((s, kind, m.group(0)))
    hits.sort()
    return hits


def classify(dispo):
    """Return (label, rule, multi_step). `rule` names the evidence so a reviewer can audit it."""
    if not dispo.strip():
        return "NO_TEXT", "no dispositive part found", 0
    hits = find_clauses(dispo.lower())
    if not hits:
        if re.search(r"tussenuitspraak|bestuurlijke\s+lus|heropent\s+het\s+onderzoek|draagt\s+[^.;]{0,80}\s+op\s+om", dispo.lower()):
            return "INTERIM", "interim ruling (tussenuitspraak, bestuurlijke lus or order to cure)", 0
        return "UNCLASSIFIED", "no operative clause recognised", 0
    kinds = [k for _, k, _ in hits]
    merits = [k for k in kinds if k in ("upheld", "dismissed", "partial", "inadmissible")]
    multi = int(("annul" in kinds or "upheld" in kinds) and "dismissed" in kinds and kinds.index("dismissed") > 0
                and any(k in ("upheld", "annul") for k in kinds[: kinds.index("dismissed")]))
    low = dispo.lower()
    interim = re.search(r"tussenuitspraak|bestuurlijke\s+lus|heropent\s+het\s+onderzoek|houdt\s+de\s+behandeling\s+aan|draagt\s+[^.;]{0,80}\s+op\s+om", low)
    if interim and not merits:
        return "INTERIM", "interim ruling (tussenuitspraak, bestuurlijke lus or order to cure)", 0
    if "remand" in kinds and not merits:
        return "REMAND", "remand clause only", 0
    if merits:
        last = merits[-1]
        mp = {"upheld": "WIN", "dismissed": "LOSS", "partial": "PARTIAL", "inadmissible": "INADMISSIBLE"}
        label = mp[last]
        rule = "final merits clause: " + last + "; clauses=" + ",".join(kinds)
        if "remand" in kinds and label == "WIN":
            return "WIN", rule + " (with remand)", multi
        if label == "WIN" and "partial" in kinds:
            return "PARTIAL", rule, multi
        if label == "WIN" and re.search(r"rechtsgevolgen[^.;]{0,80}in\s+stand", low):
            return "PARTIAL", rule + "; annulled but legal effects maintained", multi
        return label, rule, multi
    if "annul" in kinds:
        return "WIN", "annulment only; clauses=" + ",".join(kinds), 0
    if "procedural" in kinds:
        return "NO_MERITS_RULING", "withdrawn or lapsed", 0
    if "costs" in kinds or "proceskosten" in low:
        return "NO_MERITS_RULING", "costs or procedural order only", 0
    return "UNCLASSIFIED", "unmapped clauses=" + ",".join(kinds), 0


def classify_xml(xml_text):
    d = dispositive(paragraphs(xml_text))
    label, rule, multi = classify(d)
    return {"outcome": label, "rule": rule, "multi_step": multi, "dispositive": d[:2000]}


class Throttle:
    def __init__(self, rate):
        self.gap = 1.0 / rate
        self.lock = threading.Lock()
        self.next = 0.0

    def wait(self):
        with self.lock:
            now = time.monotonic()
            t = max(now, self.next)
            self.next = t + self.gap
        if t > now:
            time.sleep(t - now)


def fetch(ecli, throttle, retries=4):
    url = BASE + urllib.request.quote(ecli, safe=":")
    for attempt in range(retries):
        throttle.wait()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "water-law-dataset-research/0.3 (academic)"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", errors="replace"), None
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return None, "http_%d" % e.code
            err = "http_%d" % e.code
        except Exception as e:  # noqa: BLE001
            err = type(e).__name__
        time.sleep(1.5 * (attempt + 1))
    return None, err


def cmd_fetch(args):
    ids = [l.strip() for l in Path(args.ids).read_text().splitlines() if l.strip()]
    out = Path(args.out)
    done = set()
    if out.exists():
        for line in out.read_text(encoding="utf-8").splitlines():
            try:
                done.add(json.loads(line)["ecli"])
            except Exception:  # noqa: BLE001
                pass
    todo = [i for i in ids if i not in done]
    print("to fetch: %d (already done: %d)" % (len(todo), len(done)), flush=True)
    th = Throttle(args.rate)
    lock = threading.Lock()
    n = [0]

    def work(ecli):
        xml, err = fetch(ecli, th)
        rec = {"ecli": ecli}
        if xml is None:
            rec.update({"outcome": "FETCH_FAILED", "rule": err, "multi_step": 0, "dispositive": ""})
        else:
            rec.update(classify_xml(xml))
        with lock:
            with out.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n[0] += 1
            if n[0] % 200 == 0:
                print("  %d done" % n[0], flush=True)

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(work, todo))
    print("finished", flush=True)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch")
    f.add_argument("--ids", required=True)
    f.add_argument("--out", required=True)
    f.add_argument("--rate", type=float, default=8.0)
    f.add_argument("--workers", type=int, default=6)
    c = sub.add_parser("classify-text")
    c.add_argument("text")
    a = ap.parse_args(argv)
    if a.cmd == "fetch":
        cmd_fetch(a)
    else:
        print(classify(a.text))


if __name__ == "__main__":
    main()
