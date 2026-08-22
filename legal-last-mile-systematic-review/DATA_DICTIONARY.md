# Data Dictionary

Defines every field used across the project's CSV files. Field groupings
mirror `CODEBOOK.md`; this document adds type, allowed values, and
transformation notes where relevant. Update this file whenever a field is
added, renamed, or its allowed-value set changes — do not let it drift from
the actual CSV headers.

## `01_search/search_logs/search_log.csv`

| Field | Type | Notes |
|---|---|---|
| search_id | string | `SEARCH_NNN` zero-padded, sequential |
| database | string | e.g. `Scopus`, `Web of Science` |
| platform | string | vendor/interface, e.g. `Elsevier`, `Clarivate`, `Ovid` |
| date | date (YYYY-MM-DD) | date the search was executed |
| researcher | string | name or initials |
| exact_search_string | text | verbatim string as run, not a paraphrase |
| filters | text | e.g. document type, index, date range applied at the interface level |
| date_range | text | e.g. `2000-2026`, or `none` |
| language_filters | text | e.g. `English, Portuguese, Dutch`, or `none` |
| results_returned | integer | raw hit count before deduplication |
| export_filename | string | matches the file in `01_search/raw_exports/` |
| notes | text | anything relevant to reproducing the search |

## `02_screening/title_abstract/screening_database.csv`

| Field | Type | Notes |
|---|---|---|
| record_id | string | unique per deduplicated record |
| database | string | source database of this record |
| title, authors, year, doi | — | bibliographic metadata |
| duplicate | boolean | true if merged with another record_id (link in notes) |
| title_abstract_decision | enum | `include` / `exclude` / `unsure` |
| full_text_decision | enum | `include` / `exclude` / `not_applicable` |
| exclusion_reason | string | E01–E12, see `INCLUSION_EXCLUSION.md` |
| reviewer_1, reviewer_2 | string | reviewer IDs |
| conflict | boolean | true if reviewer_1 ≠ reviewer_2 decision |
| final_decision | enum | `include` / `exclude`, after conflict resolution |

## `03_extraction/extracted_data/extraction_database.csv`

All fields follow `CODEBOOK.md` §1–12 exactly, in the same order as the CSV
header. Key type/format notes not obvious from the field name alone:

| Field | Type | Notes |
|---|---|---|
| study_id | string | `S001`, `S002`, ... — stable once assigned, never reused |
| peer_reviewed | boolean | |
| household_level, community_level, indigenous_population, migrant_population | boolean | |
| eligibility, burden, discretion_accommodation, enforcement | boolean | top-level mechanism families |
| documentation ... bureaucratic_assistance | boolean | detailed mechanism codes, `CODEBOOK.md` §4 |
| formal_connection ... delay_outcome | boolean | outcome codes, `CODEBOOK.md` §5 (note `delay_outcome`, not `delay`, to avoid a duplicate header with the mechanism-code `delay`) |
| effect_measure | enum | `OR` / `RR` / `RD` / `MD` / `SMD` / `r` / `beta` / `log_OR` / `other` (specify in extraction_note) |
| effect_estimate, lower_CI, upper_CI, standard_error, p_value | numeric | leave blank, not zero, if not reported/calculable |
| adjusted_or_unadjusted | enum | `adjusted` / `unadjusted` |
| model_type | string | e.g. `logistic regression`, `OLS`, `difference-in-differences` |
| risk_of_bias_rating | string | tool-specific rating vocabulary (RoB 2: low/some concerns/high; ROBINS-I: low/moderate/serious/critical/no information; JBI/CASP/MMAT: per that tool's own scale) — record the tool alongside the rating so the scale is unambiguous |
| mechanism_certainty | integer 0–4 | `CODEBOOK.md` §9 |
| evidence_status | enum | `OBSERVED` / `CALCULATED` / `ASSUMED` / `INTERPRETED`, `PROJECT_SPEC.md` §13 |

## `05_analysis/descriptive/evidence_map.csv`

| Field | Type | Notes |
|---|---|---|
| study_design_class | enum | `experimental` / `quasi_experimental` / `observational` / `qualitative` / `doctrinal` / `jurimetric` / `systematic_review_secondary` / `mixed_methods` |
| evidence_level | string | narrative tier, not a numeric score (this project does not use a single universal evidence-hierarchy number — see `RISK_OF_BIAS.md` §1 on design-matched appraisal) |
| mechanism_family | enum | `ELIGIBILITY` / `BURDEN` / `DISCRETION_ACCOMMODATION` / `ENFORCEMENT` / `MULTIPLE` |
| outcome_family | enum | per `PROJECT_SPEC.md` §7 (`primary_connection` / `effective_access` / `economic_access` / `administrative_outcome`) |
| quantitative_synthesis_eligible, qualitative_synthesis_eligible | boolean | |
| legal_context | string | e.g. `civil_law`, `common_law` |
| institutional_context | string | e.g. `centralized`, `decentralized`, `fragmented` |

## `05_analysis/effect_sizes/effect_sizes.csv`

Records only the effects actually judged eligible for quantitative synthesis
(a subset of `extraction_database.csv`, one row per pooled or
pooling-candidate effect):

| Field | Type | Notes |
|---|---|---|
| synthesis_family | string | `A` / `B` / `C` per `PROJECT_SPEC.md` §8, or a newly identified family — record the family's own definition in `05_analysis/meta_analysis/` if a new one is created |
| included_in_pooled_estimate | boolean | |
| exclusion_from_pooling_reason | string | required if `included_in_pooled_estimate = false` — must cite the specific decision-tree branch from `ANALYSIS_PLAN.md` §2 that excluded it |

## Transformation log

Any transformation applied to a raw extracted value (e.g. a logistic
coefficient converted to an odds ratio, a linear-probability coefficient
explicitly *not* converted, a standard error reconstructed from a reported
CI) must be logged in `09_data_dictionary/transformations/` with: the
study_id, the source value, the transformation formula used, and the
resulting `evidence_status` (`CALCULATED` or `ASSUMED`). This is a per-value
audit trail, not a general methods description — general transformation
*rules* live in `ANALYSIS_PLAN.md` §4; this log records each specific
*application* of those rules.

## Status

No data exists yet in any of the CSVs above beyond headers. This dictionary
is written ahead of extraction so the schema is fixed before data entry
begins, per the reproducibility requirement in `REPRODUCIBILITY.md`.
