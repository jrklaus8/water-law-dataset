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
| country, legal_system | free text | **Not controlled vocabularies.** `country` holds single names, multi-country lists (`;`, `/`, `,`) and free-text regions (122 of 1,159 studies name several countries or a region; `Democratic Republic of Congo` and `... of the Congo` both occur); `legal_system` has hundreds of distinct strings. Any tabulation needs an explicit bucketing rule — the ones the project uses are in `code/analysis/current_figures.py` |
| peer_reviewed | boolean | |
| household_level, community_level, indigenous_population, migrant_population | boolean | |
| eligibility, burden, discretion_accommodation, enforcement | boolean | top-level mechanism families |
| documentation ... bureaucratic_assistance | boolean | detailed mechanism codes, `CODEBOOK.md` §4 |
| formal_connection ... delay_outcome | boolean | outcome codes, `CODEBOOK.md` §5 (note `delay_outcome`, not `delay`, to avoid a duplicate header with the mechanism-code `delay`) |
| effect_measure | enum (as originally specified) | `OR` / `RR` / `RD` / `MD` / `SMD` / `r` / `beta` / `log_OR` / `other` (specify in extraction_note). **In `extraction_database.csv` itself this short code is often followed by descriptive text in the same field** (e.g. `OR`, but also longer strings naming the exact model); **`effect_sizes.csv`'s own `effect_measure` column abandons the short-code convention entirely** — all 62 rows there use a full descriptive phrase instead (e.g. "multilevel logistic regression, adjusted odds ratio (OR)"), which is more informative for a review that deliberately does not force effect measures onto one common scale (`ANALYSIS_PLAN.md` §4) — see that file's own column for real examples rather than the short-code list here. |
| effect_estimate, lower_CI, upper_CI, standard_error, p_value | numeric | leave blank, not zero, if not reported/calculable |
| adjusted_or_unadjusted | enum | `adjusted` / `unadjusted`. **`effect_sizes.csv`'s equivalent column is named `adjusted`, not `adjusted_or_unadjusted`, and was not separately documented here until 2026-09-28** — see that file's own section below. |
| model_type | string | e.g. `logistic regression`, `OLS`, `difference-in-differences` |
| risk_of_bias_rating | string | tool-specific rating vocabulary (RoB 2: low/some concerns/high; ROBINS-I: low/moderate/serious/critical/no information; JBI/CASP/MMAT: per that tool's own scale) — record the tool alongside the rating so the scale is unambiguous |
| mechanism_certainty | integer 0–4 | `CODEBOOK.md` §9 |
| evidence_status | enum | `OBSERVED` / `CALCULATED` / `ASSUMED` / `INTERPRETED`, `PROJECT_SPEC.md` §13 |
| record_id | string | **Added 2026-09-28 (93rd column, after the 92 codebook fields).** The `record_id` of this study's row in `full_text_screening_database.csv`; a full-text include. Unique per row. Filled from `study_record_map.csv`, which keeps the `link_method` provenance. |

## `03_extraction/extracted_data/study_record_map.csv` and `linked_reports_2026-09-28.csv`

Two index files added by the 2026-09-28 repository audit; neither is a validated-schema file and neither is
read by any script.

**`study_record_map.csv`** — `study_id, record_id, link_method, status, note`. One row per extracted study
(1,159 `active`), plus the three retired rows (`retired_duplicate` for S233 and S299; `retired_excluded` for S356, excluded E05 on full text). It links each
extraction row to its `full_text_screening_database.csv` `record_id`; since 2026-09-28 the same value is also the
extraction database's own last column, and the map is kept for its `link_method` provenance and the retired rows. `link_method`: `extraction_note` (a record_id stated in the row's own note; 992),
`doi` (122), `title in citation` (41), or `manual` (5, accent/spelling variants verified by hand). The map is
a bijection with the 1,159 full-text includes. S227 and S399 (retired earlier) are not listed: their record
IDs are not recoverable from the repository.

**`linked_reports_2026-09-28.csv`** — `link_id, study_id_a, study_id_b, relationship, same_underlying_data,
basis, source_of_link, in_effect_sizes, confidence, status`. Candidate groups of reports of one underlying
study, per `REPRODUCIBILITY.md` §6. `source_of_link` is `extractor_note` (the extractor already stated the
relationship) or `audit_inferred` (the audit's inference from extracted fields, unverified). `same_underlying_data`
is `yes` / `partial` / `possible` / `probable` / `no`. `status` is always "proposed": no link has been applied to
any count. New links should get the next `LRnn` id.

## `05_analysis/descriptive/evidence_map.csv`

| Field | Type | Notes |
|---|---|---|
| study_design_class | enum | `experimental` / `quasi_experimental` / `observational` / `qualitative` / `doctrinal` / `jurimetric` / `systematic_review_secondary` / `mixed_methods`. **Status, 2026-09-28**: normalized for the 707 studies whose `risk_of_bias_tool` unambiguously implies one of the first 6 values (`code/analysis/build_evidence_map.py`'s `derive_study_design_class`); the 455 studies tagged with the project's own Legal Institutional Evidence Appraisal Framework or `NONE` remain free text, since their real methodological diversity (ethnographic/historical-institutional/comparative-institutional/documentary case studies, per `RISK_OF_BIAS.md` §2) doesn't reduce to just `doctrinal`/`jurimetric` without inventing a false binary — see `05_analysis/descriptive/study_design_class_normalization_2026-09-28.md`. A future extension of this enum (e.g. a `qualitative_institutional_case_study` value) would let that remainder be normalized too. |
| evidence_level | string | narrative tier, not a numeric score (this project does not use a single universal evidence-hierarchy number — see `RISK_OF_BIAS.md` §1 on design-matched appraisal) |
| mechanism_family | enum (as originally specified) | `ELIGIBILITY` / `BURDEN` / `DISCRETION_ACCOMMODATION` / `ENFORCEMENT` / `MULTIPLE`. **In practice, this enum has been superseded, not followed.** A large share of `evidence_map.csv` rows instead carry a specific, synthesized lowercase thematic label describing the study's actual substantive mechanism (e.g. `institutional_fragmentation`, `landlord_tenant_exclusion`, `corruption_favouritism_distribution`, `tariff_subsidy_design`) — richer and more analytically useful than the 5-value enum, but an undocumented departure from it, not a documented alternative. This is a genuine, unresolved schema question, not a data error: a future researcher should decide whether to (a) formally adopt the richer scheme as the documented standard and normalize the remaining `ELIGIBILITY`/`BURDEN`/.../`MULTIPLE`-style rows up to it, or (b) enforce the narrow enum and lose the richer labels' specificity. Neither direction should be taken mechanically — see `04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`'s "Mechanism-family coverage" section. |
| outcome_family | enum (as originally specified) | per `PROJECT_SPEC.md` §7 (`primary_connection` / `effective_access` / `economic_access` / `administrative_outcome`). **In practice, `effect_sizes.csv`'s `outcome_family` column uses a wider set** — `water_access`, `sanitation_access`, `service_coverage`, `affordability`, `formal_connection` also appear, alongside the four documented values. Not corrected here for the same reason as `mechanism_family` above: these look like a deliberate refinement (splitting `effective_access` into water- and sanitation-specific variants, for instance), not noise, and forcing them back into the 4-value list would lose that distinction without a considered decision to do so. |
| quantitative_synthesis_eligible, qualitative_synthesis_eligible | boolean | |
| legal_context | string | e.g. `civil_law`, `common_law` |
| institutional_context | string | e.g. `centralized`, `decentralized`, `fragmented` |

## `05_analysis/effect_sizes/effect_sizes.csv`

Records only the effects actually judged eligible for quantitative synthesis
(a subset of `extraction_database.csv`, one row per pooled or
pooling-candidate effect):

**Status, 2026-09-28**: this section originally documented only 3 of `effect_sizes.csv`'s 17
actual columns. Filled in below to match the live file, none of it retroactive invention — every
row added to this file across the project (61 at original extraction, S348 added 2026-09-28)
already used these fields; this just catches the dictionary up.

| Field | Type | Notes |
|---|---|---|
| outcome_family | enum (as originally specified, see `evidence_map.csv` section above) | which outcome construct this effect targets — see that section's note on the enum's actual, wider usage in this file specifically |
| synthesis_family | string | `A` / `B` / `C` per `PROJECT_SPEC.md` §8, or a newly identified family — record the family's own definition in `05_analysis/meta_analysis/` if a new one is created |
| exposure_definition | string | full prose description of the exposure and how it was operationalized in the source study — not a short code, since `ANALYSIS_PLAN.md` §3's critical pooling rule requires enough detail to judge comparability, not just a label |
| comparator_definition | string | full prose description of the reference/comparison group, same reasoning as `exposure_definition` |
| effect_measure | string | see this file's `effect_measure` note above — in practice a full descriptive phrase, not the short enum code |
| effect_estimate | string | the reported point estimate, narrated in the study's own terms when a single clean numeric value isn't recoverable from this project's extraction (a real, disclosed limit — not invented precision) |
| lower_CI, upper_CI, standard_error | numeric or blank | leave blank, not zero, if not reported/calculable — same rule as `extraction_database.csv` |
| sample_size | string | the study's own reported N, in whatever unit is appropriate to its design (households, utilities, country-years, etc.) |
| direction | string | `positive` / `negative` / `null` / `mixed`, with a short parenthetical stating what that direction means substantively for this specific exposure-outcome pair (raw regression sign alone is not informative across differently-coded reference categories) |
| adjusted | string | **not the same enum as `adjusted_or_unadjusted` above** — in practice, a descriptive phrase naming the actual covariates/matching/fixed-effects used, not a bare `adjusted`/`unadjusted` flag (a bare `TRUE` here is a data-entry artifact, not a valid value — see `CHANGELOG.md`'s 2026-09-28 "adjusted field" fix entry for the 19 rows this was corrected in) |
| evidence_status | enum | `OBSERVED` / `CALCULATED` / `ASSUMED` / `INTERPRETED`, `PROJECT_SPEC.md` §13 — same enum as `extraction_database.csv`'s field of the same name |
| provenance_note | string | cites the source `extraction_database.csv` study_id, citation, and — for any row added or corrected after original extraction — the specific audit/pass responsible, so this file's own history stays traceable without needing `CHANGELOG.md` open at the same time |
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

**This section originally said "No data exists yet in any of the CSVs above beyond headers,"
written when this dictionary was drafted ahead of extraction so the schema would be fixed
before data entry began, per `REPRODUCIBILITY.md`. That was true then and has been badly wrong
for a long time — updated here 2026-09-28 rather than left to keep misleading a reader.**

As of 2026-09-28: `screening_database.csv` holds all 27,481 deduplicated records, fully
screened at title/abstract; `full_text_screening_database.csv` holds 3,659 seeded records,
2,276 assessed (Phase 6 formally closed by researcher decision); `extraction_database.csv`
holds all 1,159 included studies (1,162 before two duplicates were merged and S356 excluded on 2026-09-28), fully extracted against every field this dictionary
documents; `evidence_map.csv` and `effect_sizes.csv` are populated and current as described in
their own sections above (both were updated the same day this Status section was corrected).
See `README.md`'s "Current project status" table for exact live figures — this dictionary
describes the *schema*, and that table is the authoritative source for *how much of it is
filled in* at any given time; the two will drift apart again if only one is kept current, so
check both rather than assuming this section's date makes it permanently reliable.
