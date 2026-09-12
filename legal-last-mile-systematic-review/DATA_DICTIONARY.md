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
| url | string | source URL; required when doi is blank (grey literature and many non-indexed sources have no DOI) — added 2026-08-25, see `CHANGELOG.md` |
| abstract | text | optional — present only when the source export included it; blank for anything ingested before 2026-09-10. Real title/abstract screening (`INCLUSION_EXCLUSION.md`) is not possible on a record with a blank abstract — see `CHANGELOG.md` 2026-09-10 |
| duplicate | boolean | true if merged with another record_id (link in notes) |
| title_abstract_decision | enum | `include` / `exclude` / `unsure` |
| full_text_decision | enum | **unused/superseded 2026-09-12** — full-text screening is tracked in the separate `02_screening/full_text/full_text_screening_database.csv` instead; see that file's section below and `FULL_TEXT_README.md` for why |
| exclusion_reason | string | E01–E12, see `INCLUSION_EXCLUSION.md` (title/abstract stage only) |
| reviewer_1, reviewer_2 | string | reviewer IDs (title/abstract stage only — full-text has its own independent pair, see below) |
| conflict | boolean | true if reviewer_1 ≠ reviewer_2 on a record where reviewer_1 made a firm `include`/`exclude` call (see note below) |
| final_decision | enum | `include` / `exclude`, after conflict resolution (title/abstract stage) |

**How `conflict` treats `unsure`**: a `title_abstract_decision` of `unsure` from
reviewer_1 is not a firm decision to compare against, it's a request for
reviewer_2 to resolve the uncertainty — so an `unsure`-then-resolved record is
never marked `conflict = true` regardless of which way reviewer_2 resolves it,
and `final_decision` is simply set to reviewer_2's call. `conflict = true` is
reserved for the one case PROTOCOL.md's "conflicts resolved by discussion or a
third reviewer" actually describes: reviewer_1 said `include` (a firm call)
and reviewer_2 said `exclude` — a genuine disagreement, where `final_decision`
is left blank pending that resolution rather than picked automatically.

## `02_screening/full_text/full_text_screening_database.csv`

Seeded 2026-09-12 by `code/screening/init_full_text_db.py` (schema
generated there, not hand-declared — see that script's `SCHEMA` constant)
from every `screening_database.csv` record with `final_decision ==
"include"` (3,659 at seed time). See `FULL_TEXT_README.md` for the
workflow.

| Field | Type | Notes |
|---|---|---|
| record_id | string | matches `screening_database.csv` |
| title, authors, year, doi, url | — | bibliographic metadata, copied from `screening_database.csv` at seed time |
| full_text_status | enum | `` / `sought` / `retrieved` / `not_retrievable` |
| full_text_location | string | file path or URL where the retrieved full text can be found again |
| full_text_decision | enum | `` / `include` / `exclude` |
| exclusion_reason | string | E01–E12, see `INCLUSION_EXCLUSION.md`; blank if included or not yet decided |
| exclusion_reason_detail | text | unlike the title/abstract stage, can cite an exact page/section/passage now that the full text is available |
| reviewer_1, reviewer_2 | string | reviewer IDs for the full-text stage — **independent of and not shared with** `screening_database.csv`'s reviewer columns |
| conflict | boolean | same rule as `screening_database.csv`: true only when reviewer_1 made a firm `include`/`exclude` call that reviewer_2 then contradicted |
| final_decision | enum | `` / `include` / `exclude`, after conflict resolution |
| notes | text | free text |

**Relationship to `screening_database.csv`**: that file's own
`full_text_decision`/`reviewer_1`/`reviewer_2`/`conflict` columns predate
this file and are now **unused and superseded** — they were never
populated for the full-text stage and won't be going forward. This file is
the single source of truth for Phase 6, kept separate rather than reusing
those columns so the title/abstract stage's own audit trail is never
overwritten and so full-text-only fields (retrieval status, file location)
have somewhere to live. See `FULL_TEXT_README.md` for the full reasoning.

## `02_screening/full_text/full_text_retrieval_queue.csv`

Generated (repeatedly, on demand) by `code/screening/build_full_text_queue.py`
(schema generated there, not hand-declared) from `full_text_screening_database.csv`
joined against `screening_database.csv` for the `database` field — a
disposable working copy for the retrieval/screening loop, not authoritative
on its own. Contains only records with no `final_decision` yet, sorted by
`database` then `year` descending. Never write a decision into this file —
record it via `update_full_text_record.py` against
`full_text_screening_database.csv`, then regenerate this queue.

| Field | Type | Notes |
|---|---|---|
| record_id, title, authors, year, doi, url | — | as in `full_text_screening_database.csv` |
| database | string | source database, looked up from `screening_database.csv` |
| full_text_status, full_text_location, notes | — | current values from `full_text_screening_database.csv`, for context while working |

## `02_screening/title_abstract/ai_first_pass_rationale.csv`

Supplementary audit trail for Claude's `reviewer_1` first pass (added
2026-09-10) — not a schema field of `screening_database.csv` itself, and
not consulted by any script. One row per screened record, giving the
short (<25 word) rationale behind that record's `title_abstract_decision`
and `exclusion_reason`, so a human `reviewer_2` (or anyone auditing the
first pass) can see *why* without re-reading every abstract from scratch.

| Field | Type | Notes |
|---|---|---|
| record_id | string | matches `screening_database.csv` |
| title_abstract_decision | enum | `include` / `exclude` / `unsure`, must match `screening_database.csv` for this record_id |
| exclusion_reason | string | E01–E12 if excluded, blank otherwise |
| rationale | text | one short sentence, free text |

## `02_screening/title_abstract/reviewer_2_queue.csv` and `exclude_spotcheck_sample.csv`

Generated 2026-09-10 from `screening_database.csv` (see
`REVIEWER_2_README.md` for how to use them) — working copies for the human
`reviewer_2` pass, not authoritative on their own. `reviewer_2_queue.csv`
is every `include`/`unsure` record from the first pass (1,608 rows);
`exclude_spotcheck_sample.csv` is a random, fixed-seed (`20260910`) 100-row
sample of the 3,565 first-pass excludes, for false-negative QA rather than
full review. Both carry the same bibliographic fields as
`screening_database.csv` plus `ai_rationale` (from
`ai_first_pass_rationale.csv`) for context. Neither file's `reviewer_2`
input feeds back into these CSVs automatically — write the actual second
decision into `screening_database.csv`'s own `reviewer_2` column.

## `03_extraction/extraction_form/pilot_sample.csv`

Not yet generated as of this writing — will be created by
`code/extraction/select_pilot_sample.py` (schema in that script's own
`OUTPUT_FIELDS`, add to `validate_schemas.py`'s generated schemas once it
actually exists) once enough `full_text_screening_database.csv` records
carry `final_decision == "include"` to draw the ~10-study pilot required
by `PROTOCOL.md` §6. Disposable working list, not consulted downstream —
see `03_extraction/extraction_form/PILOT_EXTRACTION.md`.

| Field | Type | Notes |
|---|---|---|
| record_id, title, authors, year, doi, url | — | as in `screening_database.csv`/`full_text_screening_database.csv` |
| database | string | source database, looked up from `screening_database.csv` |

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
