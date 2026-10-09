"""Independent (blind) second review of full-text decisions by a non-Claude model (Codex CLI or Gemini CLI).

Phase 1 (blind): the model sees INCLUSION_EXCLUSION.md, the reviewer-2 checklist criteria, and the paper text.
It never sees the first reviewer's decision or reasoning. It returns JSON.
Phase 2 (first-reviewer includes only, run after phase 1 is written): the model is shown the extraction row's
key fields and asked to flag mismatches against the paper (checklist step 5).

Usage:  python run_codex_reviewer2.py [--provider codex|gemini] [--tiers 1,2,3] [record_id ...]
Env:    R2_MODEL (codex: gpt-5.6-sol; gemini: gemini-2.5-pro), R2_EFFORT (codex reasoning effort, default high)
Outputs: results/<record_id>.json and results/<record_id>.phase2.json (codex) or results_gemini/... (gemini).
A FILLED copy of the priority queue is built by build_filled_queue.py.
"""
import csv, json, os, re, subprocess, sys, time, datetime, shutil, argparse
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
QUEUE = os.path.join(ROOT, "02_screening/full_text/full_text_reviewer_2_priority_queue_2026-09-28.csv")
EXTR = os.path.join(ROOT, "03_extraction/extracted_data/extraction_database.csv")
CRIT = open(os.path.join(ROOT, "INCLUSION_EXCLUSION.md"), encoding="utf-8").read()

ap = argparse.ArgumentParser()
ap.add_argument("--provider", choices=["codex", "gemini"], default="codex")
ap.add_argument("--tiers", default="1,2,3")
ap.add_argument("--workers", type=int, default=3)
ap.add_argument("records", nargs="*")
A = ap.parse_args()

PROVIDER = A.provider
if PROVIDER == "codex":
    MODEL = os.environ.get("R2_MODEL", "gpt-5.6-sol")
    EFFORT = os.environ.get("R2_EFFORT", "high")
    LABEL = "Codex-%s-reviewer2-fulltext-%s" % (MODEL, datetime.date.today().isoformat())
    RES = os.path.join(HERE, "results")
    EXE = shutil.which("codex") or "codex"
else:
    MODEL = os.environ.get("R2_MODEL", "gemini-2.5-pro")
    EFFORT = "n/a"
    LABEL = "Gemini-%s-reviewer2-fulltext-%s" % (MODEL, datetime.date.today().isoformat())
    RES = os.path.join(HERE, "results_gemini")
    EXE = shutil.which("gemini") or "gemini"
    if not os.environ.get("GEMINI_API_KEY"):
        try:
            k = subprocess.run(["powershell", "-NoProfile", "-Command", "(Get-ItemProperty HKCU:\\Environment).GEMINI_API_KEY"],
                               capture_output=True, text=True).stdout.strip()
            if k:
                os.environ["GEMINI_API_KEY"] = k
        except Exception:
            pass
    os.environ["GEMINI_CLI_TRUST_WORKSPACE"] = "true"
os.makedirs(RES, exist_ok=True)
MAX_CHARS = 160_000
TIERS = set(A.tiers.split(","))
ONLY = set(A.records)

csv.field_size_limit(sys.maxsize)
queue = [r for r in csv.DictReader(open(QUEUE, encoding="utf-8")) if r["priority_tier"] in TIERS]
extr = {r["study_id"]: r for r in csv.DictReader(open(EXTR, encoding="utf-8"))}
texts = {}
for f in os.listdir(os.path.join(HERE, "text")):
    m = re.match(r"(R[0-9A-F]{12})", f)
    if m and m.group(1) not in texts:
        texts[m.group(1)] = os.path.join(HERE, "text", f)

PHASE1 = """You are an independent second reviewer for a PRISMA 2020 systematic review titled "The Legal Last Mile"
(legal, administrative, institutional and governance factors in household water and sanitation service access).
You are reviewer_2 at the FULL-TEXT screening stage. You have NOT been shown the first reviewer's decision and you
must form your own judgment from the paper alone. Do not guess from the title or abstract when the body answers.

== INCLUSION / EXCLUSION CRITERIA (verbatim from the protocol) ==
{crit}

== CHECKLIST (apply all, in order) ==
1. Examines water or sanitation SERVICE ACCESS?
2. Examines a LEGAL, ADMINISTRATIVE, INSTITUTIONAL, REGULATORY or GOVERNANCE factor?
3. Contains EMPIRICAL evidence or a SYSTEMATIC empirical synthesis? (A policy overview, essay or commentary with
   no method and no primary data is NOT enough -> E05.)
4. Reports an OUTCOME relevant to access, connection, availability, reliability, quantity, affordability or exclusion?
5. Enough information to identify POPULATION, EXPOSURE and OUTCOME? Study DESIGN identifiable?
6. Language English, Portuguese or Dutch (others only if translation feasible)?
Qualitative socio-legal studies are never excluded merely because they cannot be pooled.
Decision: "include", "exclude" (with exactly one code E01-E12), or "cannot_tell" (e.g. text truncated/unreadable).

== PAPER (record {rid}; text extracted from the PDF, may contain layout noise) ==
{paper}
== END PAPER ==

Respond with ONLY a JSON object, no prose before or after, with these keys:
{{"record_id": "{rid}",
 "decision": "include|exclude|cannot_tell",
 "exclusion_code": "E01..E12 or empty string",
 "criteria": {{"c1_service_access": "yes|no|unclear", "c2_legal_admin_factor": "yes|no|unclear",
              "c3_empirical": "yes|no|unclear", "c4_access_outcome": "yes|no|unclear",
              "c5_pop_exposure_outcome_design": "yes|no|unclear", "c6_language": "yes|no"}},
 "study_design": "short label as reported in the paper",
 "country": "...", "population_and_sample": "...", "exposure": "...", "outcome": "...",
 "rationale": "2-4 sentences citing the page/section that decided it",
 "confidence": "high|medium|low"}}
"""

PHASE2 = """You are an independent second extractor for a systematic review. Below is the paper and the key fields that a first
extractor recorded for it. For EACH field say whether the paper supports it: "Y" (same substance; wording/rounding may
differ), "N" (a real difference), or "cannot_tell". Quote the page/section you relied on. Do not invent values.

== PAPER (record {rid}) ==
{paper}
== END PAPER ==

== FIRST EXTRACTOR'S VALUES ==
{fields}

Respond with ONLY a JSON object:
{{"record_id": "{rid}", "study_id": "{sid}",
 "checks": {{"<field>": {{"agrees": "Y|N|cannot_tell", "paper_says": "...", "where": "p./section"}}, ...}},
 "overall_comment": "one or two sentences"}}
"""

CHECK_FIELDS = ["country", "study_design", "population", "sample_size", "urban_rural", "service_provider",
                "regulatory_model", "effect_measure", "effect_estimate", "extraction_note"]


def run_model(prompt, out_path):
    tmp = out_path + ".last.txt"
    t0 = time.time()
    if PROVIDER == "codex":
        cmd = [EXE, "exec", "--skip-git-repo-check", "-s", "read-only", "-m", MODEL,
               "-c", 'model_reasoning_effort="%s"' % EFFORT, "-o", tmp, "-"]
        p = subprocess.run(cmd, input=prompt, text=True, encoding="utf-8", errors="replace",
                           capture_output=True, timeout=1500, cwd=HERE)
        last = open(tmp, encoding="utf-8", errors="replace").read() if os.path.exists(tmp) else ""
    else:
        cmd = [EXE, "-m", MODEL, "-p", "Follow the instructions in the input above and respond with ONLY the JSON object."]
        p = subprocess.run(cmd, input=prompt, text=True, encoding="utf-8", errors="replace",
                           capture_output=True, timeout=1500, cwd=HERE)
        last = p.stdout or ""
        open(tmp, "w", encoding="utf-8").write(last)
    dur = time.time() - t0
    m = re.search(r"\{.*\}", last, re.S)
    data = None
    if m:
        try:
            data = json.loads(m.group(0))
        except Exception:
            data = None
    return data, last, p.returncode, dur, (p.stderr or "")[-2000:]


def paper_text(rid):
    t = open(texts[rid], encoding="utf-8", errors="replace").read()
    return t[:MAX_CHARS] + ("\n[TRUNCATED]" if len(t) > MAX_CHARS else "")


def phase1(r):
    rid = r["record_id"]
    out = os.path.join(RES, rid + ".json")
    if os.path.exists(out):
        return rid, "cached"
    if len(open(texts[rid], encoding="utf-8", errors="replace").read().strip()) < 2000:
        rec = {"record_id": rid, "study_id": r["study_id"], "model": MODEL, "label": LABEL, "parsed": None,
               "skipped": "PDF text under 2000 chars (scan or empty); needs OCR"}
        json.dump(rec, open(out, "w", encoding="utf-8"), indent=1)
        return rid, "SKIP no text"
    data, raw, rc, dur, err = run_model(PHASE1.format(crit=CRIT, rid=rid, paper=paper_text(rid)), out)
    rec = {"record_id": rid, "study_id": r["study_id"], "priority_tier": r["priority_tier"], "provider": PROVIDER,
           "model": MODEL, "reasoning_effort": EFFORT, "label": LABEL,
           "run_at": datetime.datetime.now().isoformat(timespec="seconds"), "seconds": round(dur),
           "exit_code": rc, "parsed": data, "raw_last_message": raw, "stderr_tail": err}
    json.dump(rec, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return rid, (data or {}).get("decision", "PARSE_FAIL rc=%s" % rc)


def phase2(r):
    rid = r["record_id"]
    sid = r["study_id"]
    out = os.path.join(RES, rid + ".phase2.json")
    p1 = os.path.join(RES, rid + ".json")
    if os.path.exists(out) or r["ai_decision"] != "include" or sid not in extr:
        return rid, "skip"
    if os.path.exists(p1) and json.load(open(p1, encoding="utf-8")).get("skipped"):
        return rid, "skip (no text)"
    fields = "\n".join("- %s: %s" % (k, extr[sid].get(k, "")) for k in CHECK_FIELDS)
    data, raw, rc, dur, err = run_model(PHASE2.format(rid=rid, sid=sid, paper=paper_text(rid), fields=fields), out)
    rec = {"record_id": rid, "study_id": sid, "provider": PROVIDER, "model": MODEL, "label": LABEL, "seconds": round(dur),
           "exit_code": rc, "parsed": data, "raw_last_message": raw, "stderr_tail": err}
    json.dump(rec, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    checks = (data or {}).get("checks") or {}
    n = sum(1 for v in checks.values() if isinstance(v, dict) and v.get("agrees") == "N")
    return rid, "phase2 done, %d mismatches" % n


def log(msg):
    line = "[%s] %s" % (datetime.datetime.now().strftime("%H:%M:%S"), msg)
    print(line, flush=True)
    open(os.path.join(HERE, "run_%s.log" % PROVIDER), "a", encoding="utf-8").write(line + "\n")


if __name__ == "__main__":
    todo = [r for r in queue if r["record_id"] in texts and (not ONLY or r["record_id"] in ONLY)]
    log("provider=%s model=%s effort=%s label=%s tiers=%s records=%d" % (PROVIDER, MODEL, EFFORT, LABEL, A.tiers, len(todo)))
    with ThreadPoolExecutor(A.workers) as ex:
        for rid, res in ex.map(phase1, todo):
            log("phase1 %s: %s" % (rid, res))
    with ThreadPoolExecutor(A.workers) as ex:
        for rid, res in ex.map(phase2, todo):
            log("%s: %s" % (rid, res))
    log("ALL DONE")
