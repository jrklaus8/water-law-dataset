# Release 0.2.0-interim (2026-10-14)

Tag `v0.2.0-interim` marks the commit that carries this file, i.e. the **complete state after open items A13, A14 and A8 were closed** (the full commit hash is in the tag message and is printed by `git rev-parse 'v0.2.0-interim^{commit}'`). An earlier local tag on `a23f63e`, made before those three items were closed, is superseded and was never pushed. The tag was created locally; pushing it is left to the PI because the git relay refused a tag push with HTTP 403 and was not bypassed. Version and date are in `CITATION.cff`. This replaces `0.1.0-interim` (2026-09-12), which described a state of the project that no longer exists (screening and extraction were then live; appraisal and synthesis had not started).
It is still an **interim, AI-assisted** deposit: nothing in it has been independently verified by a human beyond the items listed under "What is verified", and the protocol was not registered before the work was done.

## What the release contains (figures as of the release date; the live values are in `00_admin/CURRENT_FIGURES.md`)

| Item | Figure |
|---|---|
| Search | 34,594 raw records, 27,481 after deduplication; closed 2026-09-11 |
| Title/abstract screening | 3,659 include / 6 exclude |
| Full-text screening | closed 2026-09-28 by researcher decision; 2,277 of 3,659 assessed: **1,078 include / 1,199 exclude**; 1,382 never assessed |
| Included studies | **1,078 reports, representing 1,076 distinct studies** on the definite same-data links (1,074 counting the partial-overlap links); the 5 RoB 2 report rows are 4 trials |
| Appraisal | every included study has a design-matched tool and a rule-based rating: RoB 2 5, ROBINS-I 57, JBI 129, MMAT 195, CASP 248, AMSTAR 2 18, Legal Institutional Evidence Appraisal Framework 426 (non-validated, project-specific) |
| Effect sizes | 58 rows (Family A 16, B 6, C 17, and 19 reasoned non-fits, S331 among them); **none pooled** (Phase 11 verdict); three structured (SWiM) syntheses, Family A k = 16, B k = 6, C k = 17, each study coded for the raw sign of its estimate and its substantive direction for households, with a sensitivity analysis |
| Controlled vocabularies | `mechanism_family` (nine families plus `multiple`), `outcome_family` (four plus `multiple`) and `study_design_class` (eight values plus `other`) adopted 2026-10-14; original labels preserved |

## What changed since 0.1.0-interim (see `CHANGELOG.md`)

Full-text screening completed and closed; extraction of every included report; corpus-wide appraisal; the quantitative-feasibility judgment and three SWiM syntheses; re-extraction of abstract-level rows from full texts in the researcher's Drive; verification of all effect-size rows against full texts; the PI's scope rulings of 2026-10-13 and 14 (the narrow, rule-type reading of criterion 2, disclosed in `INCLUSION_EXCLUSION.md`), which reversed 86 includes to excludes and 3 excludes to includes and settled every ledger item from A1 to A27 except those listed below (A26 moved S358, S590 and S606 to the reasoned non-fits and excluded S1121 and S1143); a deterministic, hash-seed-independent generator pipeline and a 188-check repository verifier.

## What is verified, and what is not

- **Verified by the repository checks:** internal consistency (counts, one-to-one maps between screening, exclusion log, extraction and evidence map, controlled vocabularies, generated files fresh). Run `bash code/analysis/regenerate_all.sh`.
- **Verified by the PI:** 197 full-text includes (S001–S200 less three the PI later excluded) and 270 further full-text decisions ruled on in the adjudication passes, in A6 tier 1 and in the A26 SWiM core confirmations (166 excludes and 104 includes, each with a recorded ruling), 467 of 2,277 decisions (20.5%) in all. A6 tier 1 (73 rows) is complete.
- **Not verified by a human:** extracted values (no second extractor), risk-of-bias ratings, the direction coding in the SWiM tables (except the 20 studies whose inclusion and both codings the author confirmed on 2026-10-14; ten others were flagged and await a ruling, A28), the mechanism and outcome vocabulary mapping, and the remaining AI full-text decisions. The `reviewer_1` label of 73 early decisions was inferred, not recorded.

## Still open (long-term, `00_admin/DECISIONS_AND_OPEN_ITEMS.md`)

A6 human second-review sampling (the reviewer-2 queue) and the independent second-extractor sample; A28 (ten SWiM core studies flagged on the narrow-scope and outcome check, awaiting the author's ruling); A7 OSF registration (prepared 2026-10-14 as a transparent retrospective registration frozen at this release; the researcher uploads it after pushing the tag); the ten included studies whose full text is a landing page or absent (S256, S280, S284, S290, S300, S301, S314, S317, S365, S380; flagged `landing_page_only` / `abstract_only` under the closed item A14) and the other papers still to fetch; manuscript revision by a human author (`07_manuscript/draft/`) with the methods disclosure of the narrow criterion-2 ruling.

## Closed in the same release (2026-10-14, later)

Before the freeze the PI closed A13 (S331's adjusted OR 4.27 added as a reasoned non-fit: 60 effect rows, 16 non-fits, Families A 18 / B 6 / C 20 unchanged), A14 (new `full_text_status` values `landing_page_only` and `abstract_only` on ten included studies; no count moved) and A8 (every disclosure statement, the 14 standard CRediT roles and the AI-tool provenance entered). The figures above are those of this state.
