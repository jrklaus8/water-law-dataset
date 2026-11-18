"""Compile results/*.json (Codex) and results_gemini/*.json (Gemini) into:
(a) a FILLED copy of the reviewer-2 priority queue restricted to tier 1-3 rows that were reviewed by
    at least one non-Claude model (Codex takes precedence as reviewer_2 of record when both exist;
    Gemini's independent verdict is recorded alongside for a three-way comparison),
(b) an agreement report (Markdown) covering decision agreement, tier breakdown, and all disagreements,
(c) a short summary of the second-extractor results (results_2ndextractor_*).
Never edits the BLANK queue, the screening database, or any extraction data.
"""
import csv, json, os, glob, datetime, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
QUEUE = os.path.join(ROOT, "02_screening/full_text/full_text_reviewer_2_priority_queue_2026-09-28.csv")
csv.field_size_limit(sys.maxsize)
rows = list(csv.DictReader(open(QUEUE, encoding="utf-8")))
header = list(rows[0].keys())


def load_results(dirpath):
    out = {}
    for f in glob.glob(os.path.join(dirpath, "*.json")):
        if f.endswith(".phase2.json") or f.endswith(".last.txt"):
            continue
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if d.get("parsed") is not None:
            out[d["record_id"]] = d
    return out


def load_phase2(dirpath):
    out = {}
    for f in glob.glob(os.path.join(dirpath, "*.phase2.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if d.get("parsed") is not None:
            out[d["record_id"]] = d
    return out


codex = load_results(os.path.join(HERE, "results"))
gemini = load_results(os.path.join(HERE, "results_gemini"))
codex_p2 = load_phase2(os.path.join(HERE, "results"))
gemini_p2 = load_phase2(os.path.join(HERE, "results_gemini"))

codex_label = next(iter(codex.values()))["label"] if codex else None
gemini_label = next(iter(gemini.values()))["label"] if gemini else None
today = datetime.date.today().isoformat()

K_DEC = "reviewer_2_decision (include/exclude/cannot_tell)"
K_CODE = "reviewer_2_exclusion_code (E01-E12)"
K_AGR = "reviewer_2_agrees_with_AI (Y/N)"
K_COM = "reviewer_2_comment"

filled, report_rows = [], []
all_ids = set(codex) | set(gemini)
for r in rows:
    rid = r["record_id"]
    if rid not in all_ids:
        continue
    cp = (codex.get(rid) or {}).get("parsed") or {}
    gp = (gemini.get(rid) or {}).get("parsed") or {}
    primary = cp if cp else gp
    primary_src = "codex" if cp else "gemini"
    dec = primary.get("decision", "")
    code = primary.get("exclusion_code", "") if dec == "exclude" else ""
    if dec in ("include", "exclude"):
        agrees = "Y" if (dec == r["ai_decision"] and (dec != "exclude" or code == r["ai_exclusion_code"])) else "N"
        decision_match = dec == r["ai_decision"]
    else:
        agrees, decision_match = "", None
    three_way = None
    if cp and gp:
        three_way = "agree" if cp.get("decision") == gp.get("decision") else "split"
    comment = "[%s; blind phase-1] %s" % (primary_src, primary.get("rationale", ""))
    if cp and gp and cp.get("decision") != gp.get("decision"):
        comment += " | SECOND MODEL DISAGREES (%s: %s %s)" % ("gemini" if primary_src == "codex" else "codex",
                                                                 gp.get("decision") if primary_src == "codex" else cp.get("decision"),
                                                                 gp.get("exclusion_code", "") if primary_src == "codex" else cp.get("exclusion_code", ""))
    p2 = codex_p2.get(rid) or gemini_p2.get(rid)
    if p2 and (p2.get("parsed") or {}).get("checks"):
        chk = p2["parsed"]["checks"]
        mism = [k for k, v in chk.items() if isinstance(v, dict) and v.get("agrees") == "N"]
        comment += " | extraction check: %d/%d agree; mismatches: %s" % (
            sum(1 for v in chk.values() if isinstance(v, dict) and v.get("agrees") == "Y"), len(chk),
            ", ".join(mism) or "none")
    nr = dict(r)
    nr[K_DEC] = dec
    nr[K_CODE] = code
    nr[K_AGR] = agrees
    nr[K_COM] = comment
    filled.append(nr)
    report_rows.append({"rank": r["priority_rank"], "rid": rid, "sid": r["study_id"], "tier": r["priority_tier"],
                        "ai_dec": r["ai_decision"], "ai_code": r["ai_exclusion_code"], "dec": dec, "code": code,
                        "agree": agrees, "match": decision_match, "three_way": three_way, "primary": primary_src,
                        "has_both": bool(cp and gp), "conf": primary.get("confidence", ""), "title": r["title"][:65]})

out_csv = os.path.join(HERE, "full_text_reviewer_2_FILLED_%s.csv" % today)
with open(out_csv, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader()
    w.writerows(filled)

out_md = os.path.join(HERE, "REVIEWER_2_AGREEMENT_%s.md" % today)
n = len(report_rows)
by_tier = Counter(x["tier"] for x in report_rows)
dm = Counter(x["match"] for x in report_rows)
full = Counter(x["agree"] for x in report_rows)
both_n = sum(1 for x in report_rows if x["has_both"])
three_way_split = [x for x in report_rows if x["three_way"] == "split"]
by_ai_tier = Counter((x["tier"], x["match"]) for x in report_rows)

lines = ["# Reviewer 2 (non-Claude models) — agreement report, %s" % today, "",
         "Models: Codex (`%s`), Gemini (`%s`). Both ran **blind**: phase 1 saw only `INCLUSION_EXCLUSION.md`, the "
         "checklist criteria and the PDF text — never `ai_decision` or `ai_reasoning`. Phase 2 (first-reviewer "
         "includes only) compared the paper against the extraction row's key fields." % (codex_label or "n/a", gemini_label or "n/a"), "",
         "Scope: %d of the 226 tier 1-3 rows reviewed (tier breakdown: tier 1 %d/73, tier 2 %d/103, tier 3 %d/50), "
         "limited to records whose PDF was available in the researcher's Drive folder. %d records were reviewed by "
         "**both** models independently (three-way comparison with the original AI possible)." % (
             n, by_tier.get("1", 0), by_tier.get("2", 0), by_tier.get("3", 0), both_n), "",
         "## Agreement (primary model vs. original AI reviewer)", "",
         "| Measure | Count |", "|---|---|",
         "| Same include/exclude decision | %d / %d |" % (dm.get(True, 0), n),
         "| Different decision | %d |" % dm.get(False, 0),
         "| Could not tell | %d |" % dm.get(None, 0),
         "| Same decision AND same exclusion code | %d |" % full.get("Y", 0),
         "", "## Three-way comparison (both Codex and Gemini reviewed the same record)", "",
         "%d records got both models' independent verdicts. %d of those **split** between Codex and Gemini "
         "(read these first, below) — the rest agree with each other." % (both_n, len(three_way_split)),
         "", "## By tier", "",
         "| Tier | Reviewed | Decision matches AI | Mismatches |", "|---|---|---|---|"]
for t in ("1", "2", "3"):
    lines.append("| %s | %d | %d | %d |" % (t, by_tier.get(t, 0), by_ai_tier.get((t, True), 0), by_ai_tier.get((t, False), 0)))
lines += ["", "## Row by row", "",
          "| Rank | Tier | Record | Study | AI | R2 (primary) | Primary model | Both ran? | 3-way | Title |",
          "|---|---|---|---|---|---|---|---|---|---|"]
for x in sorted(report_rows, key=lambda r: (int(r["tier"]), int(r["rank"]))):
    lines.append("| %s | %s | %s | %s | %s %s | %s %s | %s | %s | %s | %s |" % (
        x["rank"], x["tier"], x["rid"], x["sid"], x["ai_dec"], x["ai_code"], x["dec"], x["code"],
        x["primary"], "yes" if x["has_both"] else "no", x["three_way"] or "-", x["title"].replace("|", "/")))
lines += ["", "## Disagreements (primary model vs. original AI, or Codex vs. Gemini) — read first", ""]
for x in report_rows:
    if x["match"] is False or x["three_way"] == "split":
        rid = x["rid"]
        cp = (codex.get(rid) or {}).get("parsed") or {}
        gp = (gemini.get(rid) or {}).get("parsed") or {}
        lines.append("- **%s (%s, tier %s)** AI: %s %s -> Codex: %s %s | Gemini: %s %s" % (
            rid, x["sid"], x["tier"], x["ai_dec"], x["ai_code"],
            cp.get("decision", "n/a"), cp.get("exclusion_code", ""), gp.get("decision", "n/a"), gp.get("exclusion_code", "")))
        rationale = cp.get("rationale") or gp.get("rationale") or ""
        if rationale:
            lines.append("  - rationale: %s" % rationale)
lines += ["", "## Extraction-field mismatches (phase 2, includes only)", ""]
for rid, d in {**gemini_p2, **codex_p2}.items():
    chk = (d.get("parsed") or {}).get("checks") or {}
    for k, v in chk.items():
        if isinstance(v, dict) and v.get("agrees") == "N":
            lines.append("- %s field `%s`: paper says \"%s\" (%s)" % (rid, k, v.get("paper_says", "")[:200], v.get("where", "")))
lines += ["", "## How this was produced", "",
          "`_reviewer2_codex/run_codex_reviewer2.py` (both providers), compiled by `build_filled_queue.py`. Nothing in "
          "`full_text_screening_database.csv` or `extraction_database.csv` was changed by these scripts; recording "
          "confirmed decisions is a separate step with `code/screening/update_full_text_record.py`.",
          "", "Per the queue README, agreement on a partial sample is not a certified error rate; disagreements should widen the sample."]
open(out_md, "w", encoding="utf-8").write("\n".join(lines) + "\n")

print("rows:", n, "both-reviewed:", both_n, "3-way splits:", len(three_way_split))
print("decision agree:", dm.get(True, 0), "disagree:", dm.get(False, 0))
print("by tier:", dict(by_tier))
print("wrote", out_csv)
print("wrote", out_md)
