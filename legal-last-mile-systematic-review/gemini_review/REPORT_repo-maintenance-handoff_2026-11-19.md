# Report: Workstream P — Ready-to-Apply Reproducibility Patches & Claude Task-B Handoff (`maintenance_handoff/`)

*AI-generated second-model output. Not human verification.*

> **Why Packaged Inside `gemini_review/maintenance_handoff/`:** Per `00_admin/GEMINI_HANDOFF_BRIEF_2026-11-17.md` §6 (`L187–196`) and §8 (`L245`), Gemini may create files **only** inside `legal-last-mile-systematic-review/gemini_review/`. Rather than touching protected code, `.gitignore`, or test files directly, this PR delivers **`git apply --check`–verified unified patches** plus a ready-to-run Claude helper script for **Task B** (`102` Tier-2 excludes) so the PI or Claude can apply them in one command.

---

## 1. Verified Unified Patches (`git apply --check` against `main` @ `2cd44e7`)

| Patch File | `git apply --check` Status |
|---|---|
| `01_windows_64bit_csv_field_size_limit.patch` | `PASS (exit 0)` |
| `02_gitattributes_lf_and_gitignore_gemini_json.patch` | `PASS (exit 0)` |
| `03_optional_matplotlib_test_guard.patch` | `PASS (exit 0)` |

### Patch Details
1. **`01_windows_64bit_csv_field_size_limit.patch`** — Fixes `OverflowError: Python int too large to convert to C long` on 64-bit Windows (`sys.maxsize == 2**63 - 1` vs C `long` `2**31 - 1`) across all `114` affected scripts:
  - `legal-last-mile-systematic-review/code/analysis/build_a16_adjudication_sheet.py`
  - `legal-last-mile-systematic-review/code/analysis/build_data_manifest.py`
  - `legal-last-mile-systematic-review/code/analysis/build_evidence_atlas.py`
  - `legal-last-mile-systematic-review/code/analysis/build_evidence_map.py`
  - `legal-last-mile-systematic-review/code/analysis/build_executive_summary.py`
  - `legal-last-mile-systematic-review/code/analysis/build_missing_fulltext_list.py`
  - `legal-last-mile-systematic-review/code/analysis/build_reclassification_proposal.py`
  - `legal-last-mile-systematic-review/code/analysis/build_second_extractor_passages.py`
  - `legal-last-mile-systematic-review/code/analysis/build_swim_source_dossier.py`
  - `legal-last-mile-systematic-review/code/analysis/check_verifier_mutations.py`
  - `legal-last-mile-systematic-review/code/analysis/current_figures.py`
  - `legal-last-mile-systematic-review/code/analysis/sheet_xlsx.py`
  - `legal-last-mile-systematic-review/code/analysis/validate_schemas.py`
  - `legal-last-mile-systematic-review/code/extraction/select_pilot_sample.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/_reextract_lib.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/add_record_id_column_2026-09-28.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/add_s1166_effect_row_2026-10-13.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/add_s1169_effect_row_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/add_s348.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/adopt_a5_a20_vocabularies_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/annotate_dup_notes.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/annotate_live_duplicates_2026-09-28.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a11_tool_moves_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a25_tool_moves_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a26_effect_row_rulings_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a26_swim_core_checks_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a28_effect_row_rulings_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a29_nonfit_s1140_s1136_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a31_relabel_ai_checked_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a6_tier1_batch2_ck_rulings_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a6_tier1_batches34_ck_rulings_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/apply_a6_tier1_ck_rulings_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/appraise_s052_s327_amstar2_2026-10-03.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/appraise_s328_amstar2_2026-10-04.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/appraise_s418_amstar2_2026-10-03.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/appraise_s697_s438_amstar2_2026-10-03.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/backfill_reviewer1_2026-09-16_batch_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/build_a6_tier1_batches_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/build_a6_tier1_ck_sheet_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/build_e05_recheck_sheet_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/build_effect_row_number_check_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/build_linked_reports_2026-09-28.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/build_pdf_retrieval_targets_2026-10-09.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/build_study_record_map_2026-09-28.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/build_swim_core_verification_table_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/build_swim_direction_coding_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/close_a13_s331_adjusted_or_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/close_a14_landing_page_status_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/correct_effect_rows_s312_s649_2026-10-04.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/doi_audit.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/enrich_s1163_ci_2026-10-04.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/enrich_s348_coefficients_2026-10-04.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/fill_a20_residue_adjudication_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/fill_a25_adjudication_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/fill_audit_excludes_adjudication_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/fix_adjusted_field.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/fix_stale_fulltext_status_batch_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/fix_stale_fulltext_status_s401_s391_s400_s390_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/fix_study_design_class.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/live_numbers.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/merge_live_duplicates_2026-09-28.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/normalise_conflict_case_2026-10-04.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/normalise_r803988411d3e_not_retrievable_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/normalize_mechanism_certainty_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/process_drive_inbox_2026-10-04.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/process_drive_inbox_2026-10-04b.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/process_drive_inbox_2026-10-04c.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/process_drive_inbox_2026-10-04d.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/process_drive_inbox_2026-10-04e.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/process_drive_inbox_2026-10-09.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/process_drive_inbox_2026-10-09b.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/record_a18_clarification_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/record_reviewer2_S101_S200_2026-10-02.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/reextract_2026-10-04/build_campaign_notes.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/reextract_amstar4_from_fulltext_2026-10-02.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/reextract_s277_from_fulltext_2026-09-29.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/reextract_s326_from_fulltext_2026-09-29.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/reextract_s366_from_fulltext_2026-09-29.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/refresh_evidence_map_deferred_text_2026-10-04.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/remove_s312_s435_effect_rows_2026-10-13.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/remove_s348_s969_effect_rows_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/remove_s589_effect_row_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/resolve_s324_rating_2026-10-04.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/resolve_s356_exclude_2026-09-28.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/resync_study_design_class.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/run_reextract_2026-10-04.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/set_group1_rule_flags_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/sync_design_class_after_a11_moves_2026-10-14.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/title_dup_audit.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/title_dup_classify.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/title_dup_final.py`
  - `legal-last-mile-systematic-review/code/provenance/audit_and_repair/title_dup_pass2_check.py`
  - `legal-last-mile-systematic-review/code/screening/apply_a16_adjudications.py`
  - `legal-last-mile-systematic-review/code/screening/build_full_text_queue.py`
  - `legal-last-mile-systematic-review/code/screening/build_full_text_reviewer2_queue.py`
  - `legal-last-mile-systematic-review/code/screening/bulk_import_full_text_results.py`
  - `legal-last-mile-systematic-review/code/screening/full_text_progress.py`
  - `legal-last-mile-systematic-review/code/screening/init_full_text_db.py`
  - `legal-last-mile-systematic-review/code/screening/init_screening_db.py`
  - `legal-last-mile-systematic-review/code/screening/resolve_a16_pending_reversals.py`
  - `legal-last-mile-systematic-review/code/screening/update_full_text_record.py`
  - `legal-last-mile-systematic-review/code/search/deduplicate.py`
  - `legal-last-mile-systematic-review/code/tests/test_a16_pipeline.py`
  - `legal-last-mile-systematic-review/code/tests/test_bulk_import_full_text.py`
  - `legal-last-mile-systematic-review/code/tests/test_current_figures_independent.py`
  - `legal-last-mile-systematic-review/code/tests/test_database_integrity.py`
  - `legal-last-mile-systematic-review/code/tests/test_deduplicate.py`
  - `legal-last-mile-systematic-review/code/tests/test_r_templates.py`
  - `legal-last-mile-systematic-review/code/tests/test_search_adapters.py`
  - `legal-last-mile-systematic-review/code/tests/test_search_reconciliation.py`
  - `legal-last-mile-systematic-review/code/tests/test_sensitivity_invariants.py`
  - `legal-last-mile-systematic-review/code/tests/test_swim_direction_coding.py`
  - `legal-last-mile-systematic-review/code/tests/test_swim_dossier.py`
  - `legal-last-mile-systematic-review/code/tests/test_update_full_text_record.py`
2. **`02_gitattributes_lf_and_gitignore_gemini_json.patch`** — Adds `.gitattributes` (`* text=auto eol=lf` + binary guards) so Windows clones pass all `DATA_MANIFEST.csv` SHA-256 checks out-of-the-box, and un-ignores `legal-last-mile-systematic-review/gemini_review/**/*.json` in root `.gitignore` (`*.json` on line 32 otherwise blocks `git add` without `-f`).
3. **`03_optional_matplotlib_test_guard.patch`** — Guards optional `matplotlib`-dependent test methods with `@unittest.skipUnless(_HAS_MPL, ...)` so the test suite passes cleanly in minimal Python environments:
  - `legal-last-mile-systematic-review/code/tests/test_executive_summary.py`

### One-Command Apply (for PI or Claude on `main`)
```bash
git apply legal-last-mile-systematic-review/gemini_review/maintenance_handoff/*.patch
```

---

## 2. Unblocking Task B (`102` Tier-2 Excludes): `build_tier2_mixed_blind_input_FOR_CLAUDE_ONLY.py`

Per `GEMINI_HANDOFF_BRIEF_2026-11-17.md` §3 (`L79`), Gemini must **not** construct the Tier-2 input file itself because filtering `priority_tier == 2` directly would reveal 100% set composition (`exclude`). Running `build_tier2_mixed_blind_input_FOR_CLAUDE_ONLY.py` as Claude/PI generates `02_screening/full_text/A6_TIER2_MIXED_BLIND_INPUT_FOR_SECOND_AI.csv` (`102` Tier-2 rows shuffled with `28` Tier-1 include decoys = `130` blind rows, with all tier/decision/code/study_id columns stripped), allowing Gemini to screen all `102` Tier-2 excludes with zero set-composition leakage.
