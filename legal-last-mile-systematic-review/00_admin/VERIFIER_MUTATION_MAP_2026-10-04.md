# Verifier mutation map (2026-10-04)

Produced by `python3 code/analysis/check_verifier_mutations.py --write`: one deliberate defect at a time is applied to a scratch copy of the project and `verify_repository.py` is run on it. "Failing" is the number of failed checks; "first message" is the check that said so. An UNCAUGHT row is a mistake the verifier would let through.

| Defect | What was done | Result | Failing | First message |
|---|---|---|---|---|
| `drop_extraction_row` | the last extraction row is deleted | CAUGHT (crash) | 18 | extraction/evidence_map study_id sets differ: ['S1164'] |
| `drop_evidence_map_row` | the last evidence-map row is deleted | CAUGHT (crash) | 4 | extraction/evidence_map study_id sets differ: ['S1164'] |
| `map_wrong_record` | two studies swap their screening record ids in the extraction database | CAUGHT | 1 | extraction_database.record_id disagrees with study_record_map |
| `flip_include_to_exclude` | one full-text include is switched to exclude | CAUGHT | 18 | study_record_map is not a bijection with the full-text includes |
| `drop_exclusion_log_row` | the last exclusion-log row is deleted | CAUGHT | 7 | exclusion_log does not match full-text excludes one-to-one |
| `exclude_without_code` | a full-text exclude loses its exclusion code | CAUGHT | 1 | a full-text exclude lacks an exclusion_reason code |
| `es_study_not_extracted` | an effect-size row points to a study that is not extracted | CAUGHT (crash) | 2 | effect_sizes has study_ids not extracted: ['S9999'] |
| `es_value_changed` | an effect estimate is changed to 999 (derived tables become stale) | CAUGHT | 1 | 03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-10-04.csv is stale: run `python3 code/analysis/build_second_extractor_sampl |
| `duplicate_doi` | two extraction rows get the same DOI | CAUGHT | 1 | the same DOI appears on two extraction rows (a double-counted paper?) |
| `bad_year` | a publication year becomes 302 | CAUGHT | 5 | 06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md is stale: run `python3 code/analysis/build_preliminary_report.py` |
| `invalid_design_class` | an evidence-map design class outside the enumeration | CAUGHT | 5 | 06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md is stale: run `python3 code/analysis/build_preliminary_report.py` |
| `invalid_boolean_field` | a yes/no extraction field is set to "maybe" | CAUGHT | 1 | boolean fields hold non-TRUE/FALSE/blank values: [('S004', 'household_level', 'maybe')] |
| `drop_map_row` | the last study_record_map row is deleted | CAUGHT | 1 | study_record_map gaps in the S-number sequence differ from the two documented ones (S227, S399, retired 2026-09-16 before the map existed):  |
| `country_changed` | a study's country is changed to a non-country | CAUGHT | 3 | 00_admin/current_figures.json is stale: run `python3 code/analysis/current_figures.py --write` |
| `appraisal_tool_changed` | a JBI study is relabelled RoB 2 without any appraisal | CAUGHT | 16 | 00_admin/current_figures.json is stale: run `python3 code/analysis/current_figures.py --write` |
| `blank_citation` | a study loses its citation text | CAUGHT | 1 | extraction rows with a blank citation, record_id or study_design: [('S008', 'citation')] |
| `stale_generated_file` | a generated audit file is edited by hand | CAUGHT | 1 | 05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.md is stale: run `python3 code/analysis/audit_exclusion_basis.py` |
| `tamper_readme_figure` | the README extraction figure is changed | CAUGHT | 1 | README.md: expected to contain '1,159 studies extracted' (extraction row) |
| `remove_ai_disclosure_title` | the "AI-Assisted" marker is removed from the README title | CAUGHT | 1 | README.md: H1 no longer carries "AI-Assisted" |
| `remove_ai_use_statement` | AI_USE_STATEMENT.md is deleted | CAUGHT | 1 | AI_USE_STATEMENT.md is missing |
| `unlisted_test_file` | a new test file that regenerate_all.sh does not run | CAUGHT | 1 | unit-test files not run by code/analysis/regenerate_all.sh: ['test_zz_unlisted'] |

21 of 21 defects caught.
