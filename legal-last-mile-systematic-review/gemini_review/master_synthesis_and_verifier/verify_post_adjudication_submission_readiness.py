#!/usr/bin/env python3
"""Post-Adjudication & Pre-Submission Readiness Verifier (`Item 1B.3`).
Run from `legal-last-mile-systematic-review/` AFTER merging Gemini PRs and applying Claude repairs:
    python gemini_review/master_synthesis_and_verifier/verify_post_adjudication_submission_readiness.py

Exits 0 with `--strict` once all pre-submission blockers are resolved; in default `--report` mode, prints
the complete pass/open scorecard and writes `SUBMISSION_READINESS_SCORECARD.csv`.
"""
import argparse
import csv
import json
import re
import sys
import zipfile
from pathlib import Path

csv.field_size_limit(2**31 - 1)


def run_checks(review_root: Path) -> list[dict]:
    checks = []

    def add(cid: str, severity: str, pr_ref: str, desc: str, passed: bool, detail: str) -> None:
        checks.append({
            "check_id": cid,
            "severity": severity,
            "source_pr": pr_ref,
            "status": "PASS" if passed else "OPEN_NEEDS_PI_OR_CLAUDE",
            "description": desc,
            "detail": detail,
        })

    # 1. OSF preregistration draft L80 vs L66 effect_sizes count contradiction (PR #29)
    osf = (review_root / "00_admin/preregistration/osf_preregistration_draft.md").read_text(encoding="utf-8")
    eff_n = sum(1 for _ in csv.DictReader((review_root / "05_analysis/effect_sizes/effect_sizes.csv").open(encoding="utf-8")))
    has_stale_58 = ("| Effect-size rows | **58**" in osf or "Family A 16, Family B 5, Family C 16" in osf) and eff_n != 58
    add("SUB-01", "CRITICAL_PRE_OSF", "PR #29", "OSF draft L80 effect_sizes row count matches live effect_sizes.csv", not has_stale_58, f"live effect_sizes.csv={eff_n}; L80_stale_58_A16_B5_C16={has_stale_58}")

    # 2. OSF identifier filled in PROTOCOL.md & MANUSCRIPT_DRAFT (Open Item A7 / A8)
    ms = (review_root / "07_manuscript/draft/MANUSCRIPT_DRAFT_2026-10-04.md").read_text(encoding="utf-8")
    has_placeholder = bool(re.search(r"\[OSF|TBD|not yet registered|awaiting upload|to be added|identifier pending|unregistered", ms, re.I))
    add("SUB-02", "HIGH_PRE_SUBMIT", "PR #16/#29", "OSF registration uploaded & identifier populated in manuscript draft", not has_placeholder, f"unregistered_or_placeholder={has_placeholder}")

    # 3. PRELIMINARY_RESULTS_REPORT_2026-09-29.docx synced with .md (PR #29)
    docx_p = review_root / "06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.docx"
    docx_stale = False
    if docx_p.exists():
        with zipfile.ZipFile(docx_p) as zf:
            xml = zf.read("word/document.xml").decode("utf-8", errors="replace")
            txt = re.sub(r"<[^>]+>", "", xml)
            docx_stale = ("1,159" in txt or "1159" in txt)
    add("SUB-03", "HIGH_OUTPUT_SYNC", "PR #29", "PRELIMINARY_RESULTS_REPORT .docx regenerated (no frozen 1,159 count)", not docx_stale, f"docx_contains_1159={docx_stale}")

    # 4. deduplicate.py DOI backfill & NFKD Unicode normalization + Windows csv limit (PR #24 & PR #35)
    dedup_src = (review_root / "code/search/deduplicate.py").read_text(encoding="utf-8")
    has_win_crash = "csv.field_size_limit(sys.maxsize)" in dedup_src
    has_nfkd = "NFKD" in dedup_src
    has_doi_backfill = bool(re.search(r'kept\[match_idx\]\["doi"\]', dedup_src))
    add("SUB-04", "MEDIUM_CODE", "PR #24/#35", "deduplicate.py Windows 64-bit csv.field_size_limit portability", not has_win_crash, f"uses_sys_maxsize_unwrapped={has_win_crash}")
    add("SUB-05", "HIGH_PIPELINE", "PR #35", "deduplicate.py backfills dropped DOI & normalizes NFKD diacritics", (has_nfkd and has_doi_backfill), f"NFKD={has_nfkd}, doi_backfill={has_doi_backfill}")

    # 5. E10 ('Inaccessible full text') rows carrying full_text_status == 'retrieved' (PR #30)
    ft_rows = list(csv.DictReader((review_root / "02_screening/full_text/full_text_screening_database.csv").open(encoding="utf-8")))
    e10_ret = sum(1 for r in ft_rows if r["full_text_decision"] == "exclude" and r["exclusion_reason"] == "E10" and r["full_text_status"] == "retrieved")
    add("SUB-06", "HIGH_PRISMA", "PR #30", "Zero E10 ('Inaccessible full text') exclusions carrying full_text_status='retrieved'", e10_ret == 0, f"e10_with_retrieved_status={e10_ret}")

    # 6. 08_code/R/02_sensitivity_analysis.R quasi-experimental regex bug (PR #37)
    r02 = (review_root / "08_code/R/02_sensitivity_analysis.R").read_text(encoding="utf-8")
    r02_bug = 'grepl("experiment|randomi", study_design' in r02 and "!grepl(\"quasi\"" not in r02
    add("SUB-07", "HIGH_R_CODE", "PR #37", "02_sensitivity_analysis.R excludes 'quasi-experimental' from experimental_only", not r02_bug, f"quasi_matched_as_experimental={r02_bug}")

    # 7. Criterion 10 multilingual translation logging or DEVIATIONS_REGISTER disclosure (PR #37)
    ex_rows = list(csv.DictReader((review_root / "03_extraction/extracted_data/extraction_database.csv").open(encoding="utf-8")))
    dev_txt = (review_root / "00_admin/DEVIATIONS_REGISTER.csv").read_text(encoding="utf-8")
    c10_unlogged = 0
    for r in ex_rows:
        lang = (r.get("language") or "").strip().lower()
        if not lang or lang in ("english", "en") or "portuguese" in lang or "dutch" in lang or ("english" in lang and "abstract" not in lang and "translated" not in lang):
            continue
        if not re.search(r"translat(?:ed|ion|or)", r.get("extraction_note") or "", re.I):
            c10_unlogged += 1
    c10_disclosed = "Criterion 10" in dev_txt or "translation" in dev_txt.lower()
    add("SUB-08", "HIGH_PROTOCOL", "PR #37/#38", "Criterion 10 non-EN/PT/NL translation method logged per study or disclosed in DEVIATIONS_REGISTER", (c10_unlogged == 0 or c10_disclosed), f"unlogged_studies={c10_unlogged}, in_deviations_register={c10_disclosed}")

    # 8. 6 Publication-year discrepancies resolved (PR #27: S1085, S571, S1148, S425, S959, S972)
    ex_by_sid = {r["study_id"]: r for r in ex_rows}
    expected_yrs = {"S1085": "2013", "S571": "2026", "S1148": "2020", "S425": "2015", "S959": "2013", "S972": "2019"}
    yr_mismatches = {s: ex_by_sid[s]["publication_year"] for s, y in expected_yrs.items() if s in ex_by_sid and ex_by_sid[s]["publication_year"].strip() != y}
    add("SUB-09", "MEDIUM_DATA", "PR #27", "6 verified publication_year discrepancies reconciled against PDFs", len(yr_mismatches) == 0, f"remaining_mismatches={yr_mismatches}")

    # 9. S926 MBA teaching case not rated ROBINS-I quasi-experimental causal study (PR #26)
    s926_robins = "ROBINS-I" in ex_by_sid.get("S926", {}).get("risk_of_bias_tool", "")
    add("SUB-10", "HIGH_CAUSAL", "PR #26", "S926 (Harvard/Yale MBA teaching case) removed from ROBINS-I causal backbone", not s926_robins, f"S926_still_ROBINS_I={s926_robins}")

    # 10. Open Item A30 human direction verification on 31 SWiM studies
    swim_tbl = list(csv.DictReader((review_root / "05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv").open(encoding="utf-8")))
    ck_cols = [c for c in (swim_tbl[0].keys() if swim_tbl else []) if c.startswith("ck_")]
    ck_filled = sum(1 for r in swim_tbl if any((r.get(c) or "").strip() for c in ck_cols))
    add("SUB-11", "CRITICAL_HUMAN_PI", "Open Item A30 / PR #11/#31", "PI (CK) human verification recorded on all 31 SWiM core studies", ck_filled == len(swim_tbl) and len(swim_tbl) > 0, f"ck_verified_swim_rows={ck_filled}/{len(swim_tbl)}")

    # 11. AI_USE_LEDGER includes Gemini 4 Carbon second-model audit runs
    ledger_txt = (review_root / "00_admin/AI_USE_LEDGER.csv").read_text(encoding="utf-8")
    has_gemini4 = "gemini-4-carbon" in ledger_txt.lower()
    add("SUB-12", "MEDIUM_PROVENANCE", "PRs #10-#42", "AI_USE_LEDGER updated by Claude with Gemini second-model runs (0 human-checked)", has_gemini4, f"gemini_4_carbon_logged={has_gemini4}")

    return checks


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--review-root", type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument("--out-csv", type=Path, default=None)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    checks = run_checks(args.review_root)
    passed = sum(1 for c in checks if c["status"] == "PASS")
    print(f"Post-Adjudication Submission Readiness: {passed}/{len(checks)} checks PASS ({len(checks)-passed} awaiting PI/Claude merge actions)")
    for c in checks:
        print(f"  [{c['status']:24s}] {c['check_id']} ({c['severity']}, {c['source_pr']}): {c['description']} -> {c['detail']}")
    if args.out_csv:
        args.out_csv.parent.mkdir(parents=True, exist_ok=True)
        with args.out_csv.open("w", encoding="utf-8", newline="\n") as fh:
            w = csv.DictWriter(fh, fieldnames=list(checks[0].keys()), lineterminator="\n")
            w.writeheader()
            w.writerows(checks)
    return 1 if (args.strict and passed < len(checks)) else 0


if __name__ == "__main__":
    sys.exit(main())
