# Report: Master Synthesis, One-Stop Adjudication Pack & Automated Pre-Submission Readiness Verifier (`Items 1A & 1B.3`)

*AI-generated second-model output. Not human verification.*

## 1. What This PR Delivers on GitHub

1. **`GEMINI_29_PR_MASTER_AUDIT_SYNTHESIS_2026-11-20.md`:** Commits the full 29-PR (`#10–#38`) master synthesis directly into the repository so it lives permanently on GitHub alongside the review data.
2. **One-Stop Master CSVs for PI (`CK`) & Claude Post-Merge Execution:**
   - `MASTER_RESCUED_STUDIES_ACROSS_ALL_PRS_2026-11-21.csv` (**`9` narrow-C2 eligible studies** rescued across `Tier-2`, `Phase-6 unassessed`, `E10`, and `non-queue` exclusion audits).
   - `MASTER_11_OMITTED_SWIM_CANDIDATES_2026-11-21.csv` (**`0` omitted SWiM-eligible studies** surfaced across `100%` [`71/71`] of unmined Cat A + B quantitative studies).
   - `MASTER_UNSCORED_SECOND_EXTRACTION_SHEETS_INDEX_2026-11-21.csv` (indexing **`277` blind study extractions / `2,493` field rows** across `PRs #14, #20, #23, #26, #31, #38, #40` ready for `code/analysis/score_second_extractor_sheet.py`).
3. **Executable Post-Adjudication Pre-Submission Verifier (`verify_post_adjudication_submission_readiness.py` + `BASELINE_SUBMISSION_READINESS_SCORECARD_2026-11-21.csv`):**
   - Automates Item `1B.3` ("Final pre-submission verification pass") as a deterministic 12-check Python gate (`SUB-01`..`SUB-12`) that you and Claude can execute with `--strict` immediately after merging PRs and applying repairs:
   ```text
Post-Adjudication Submission Readiness: 1/12 checks PASS (11 awaiting PI/Claude merge actions)
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-01 (CRITICAL_PRE_OSF, PR #29): OSF draft L80 effect_sizes row count matches live effect_sizes.csv -> live effect_sizes.csv=52; L80_stale_58_A16_B5_C16=True
  [PASS                    ] SUB-02 (HIGH_PRE_SUBMIT, PR #16/#29): OSF registration uploaded & identifier populated in manuscript draft -> unregistered_or_placeholder=False
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-03 (HIGH_OUTPUT_SYNC, PR #29): PRELIMINARY_RESULTS_REPORT .docx regenerated (no frozen 1,159 count) -> docx_contains_1159=True
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-04 (MEDIUM_CODE, PR #24/#35): deduplicate.py Windows 64-bit csv.field_size_limit portability -> uses_sys_maxsize_unwrapped=True
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-05 (HIGH_PIPELINE, PR #35): deduplicate.py backfills dropped DOI & normalizes NFKD diacritics -> NFKD=False, doi_backfill=False
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-06 (HIGH_PRISMA, PR #30): Zero E10 ('Inaccessible full text') exclusions carrying full_text_status='retrieved' -> e10_with_retrieved_status=121
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-07 (HIGH_R_CODE, PR #37): 02_sensitivity_analysis.R excludes 'quasi-experimental' from experimental_only -> quasi_matched_as_experimental=True
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-08 (HIGH_PROTOCOL, PR #37/#38): Criterion 10 non-EN/PT/NL translation method logged per study or disclosed in DEVIATIONS_REGISTER -> unlogged_studies=37, in_deviations_register=False
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-09 (MEDIUM_DATA, PR #27): 6 verified publication_year discrepancies reconciled against PDFs -> remaining_mismatches={'S1085': '', 'S571': '', 'S1148': '2018', 'S425': '2012', 'S959': '2011'}
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-10 (HIGH_CAUSAL, PR #26): S926 (Harvard/Yale MBA teaching case) removed from ROBINS-I causal backbone -> S926_still_ROBINS_I=True
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-11 (CRITICAL_HUMAN_PI, Open Item A30 / PR #11/#31): PI (CK) human verification recorded on all 31 SWiM core studies -> ck_verified_swim_rows=3/31
  [OPEN_NEEDS_PI_OR_CLAUDE ] SUB-12 (MEDIUM_PROVENANCE, PRs #10-#42): AI_USE_LEDGER updated by Claude with Gemini second-model runs (0 human-checked) -> gemini_4_carbon_logged=False
   ```
