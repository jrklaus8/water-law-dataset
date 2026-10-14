# Release 0.2.0-interim (2026-10-14)

Tag `v0.2.0-interim` (on commit `a23f63e`, created locally; pushing it is left to the PI because the git relay refused the tag push with HTTP 403 and was not bypassed); version and date in `CITATION.cff`. This replaces `0.1.0-interim` (2026-09-12), which described a state of the project that no longer exists (screening and extraction were then live; appraisal and synthesis had not started).
It is still an **interim, AI-assisted** deposit: nothing in it has been independently verified by a human beyond the items listed under "What is verified", and the protocol was not registered before the work was done.

## What the release contains (figures as of the release date; the live values are in `00_admin/CURRENT_FIGURES.md`)

| Item | Figure |
|---|---|
| Search | 34,594 raw records, 27,481 after deduplication; closed 2026-09-11 |
| Title/abstract screening | 3,659 include / 6 exclude |
| Full-text screening | closed 2026-09-28 by researcher decision; 2,277 of 3,659 assessed: **1,080 include / 1,197 exclude**; 1,382 never assessed |
| Included studies | **1,080 reports, representing 1,078 distinct studies** on the definite same-data links (1,076 counting the partial-overlap links); the 5 RoB 2 report rows are 4 trials |
| Appraisal | every included study has a design-matched tool and a rule-based rating: RoB 2 5, ROBINS-I 58, JBI 130, MMAT 195, CASP 248, AMSTAR 2 18, Legal Institutional Evidence Appraisal Framework 426 (non-validated, project-specific) |
| Effect sizes | 59 rows; **none pooled** (Phase 11 verdict); three structured (SWiM) syntheses, Family A k = 18, B k = 6, C k = 20, with a sensitivity analysis |
| Controlled vocabularies | `mechanism_family` (nine families plus `multiple`), `outcome_family` (four plus `multiple`) and `study_design_class` (eight values plus `other`) adopted 2026-10-14; original labels preserved |

## What changed since 0.1.0-interim (see `CHANGELOG.md`)

Full-text screening completed and closed; extraction of every included report; corpus-wide appraisal; the quantitative-feasibility judgment and three SWiM syntheses; re-extraction of abstract-level rows from full texts in the researcher's Drive; verification of all effect-size rows against full texts; the PI's scope rulings of 2026-10-13 and 14 (the narrow, rule-type reading of criterion 2, disclosed in `INCLUSION_EXCLUSION.md`), which reversed 83 includes to excludes and 3 excludes to includes and settled every ledger item from A1 to A25 except those listed below; a deterministic, hash-seed-independent generator pipeline and a 177-check repository verifier.

## What is verified, and what is not

- **Verified by the repository checks:** internal consistency (counts, one-to-one maps between screening, exclusion log, extraction and evidence map, controlled vocabularies, generated files fresh). Run `bash code/analysis/regenerate_all.sh`.
- **Verified by the PI:** 197 full-text includes (S001–S200 less three the PI later excluded) and every adjudicated record listed in the ledger (137 excludes and 38 other includes carry a recorded ruling).
- **Not verified by a human:** extracted values (no second extractor), risk-of-bias ratings, the direction coding in the SWiM tables, the mechanism and outcome vocabulary mapping, and the remaining AI full-text decisions. The `reviewer_1` label of 73 early decisions was inferred, not recorded.

## Still open (long-term, `00_admin/DECISIONS_AND_OPEN_ITEMS.md`)

A6 human second-review sampling (the reviewer-2 queue) and the independent second-extractor sample; A7 OSF registration (prepared 2026-10-14 as a transparent retrospective registration frozen at this release; the researcher uploads it after pushing the tag); A8 final sign-off of the funding, competing-interest and affiliation statements entered 2026-10-14 (PRISMA items 25 and 26); A13 one effect-size candidate (S331: adjusted OR 4.27 found, PI approval needed) and A14 (ten included studies still rest on a landing page or no file: S256, S280, S284, S290, S300, S301, S314, S317, S365, S380); the papers still to fetch; manuscript revision by a human author (`07_manuscript/draft/`) with the methods disclosure of the narrow criterion-2 ruling.

## After the tagged snapshot (2026-10-14, later)

The tag marks commit `a23f63e`. Later the same day the PI closed A13 (S331's adjusted OR added as a reasoned non-fit: 60 effect rows, 16 non-fits; families unchanged), A14 (new `full_text_status` values `landing_page_only` and `abstract_only` on ten included studies; no count moves) and A8 (all disclosure statements entered). A7 (the OSF registration) is prepared and awaits upload. The figures in the table above are those of the tagged snapshot.
