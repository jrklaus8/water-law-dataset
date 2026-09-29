# Decisions and open items

The single place to see (A) what is still undecided and who decides, (B) the judgment calls already made and where each is
documented, (C) what has not been verified, and (D) a backlog of improvements. Update it, with a date, whenever an item
changes state; it does not replace `CHANGELOG.md`, it indexes it. Figures quoted here are as of 2026-09-28 and are
regenerated in `00_admin/CURRENT_FIGURES.md`.

## A. Open decisions for the researcher

| # | Decision | Why it matters | Recommendation | Detail |
|---|---|---|---|---|
| A1 | **S589's `effect_sizes.csv` row** — remove, or keep and flip its eligibility flag | It records an unadjusted descriptive comparison for a study `evidence_map.csv` does not flag eligible; the only such row of 62. Removing takes Family A from 20 to 19 | Remove the row (it fails the file's own inclusion standard) | Audit finding 5 |
| A2 | **73 decided full-text rows with no `reviewer_1`** — who screened them? | Provenance gap; none has a `reviewer_2`. Nothing back-filled, because a guessed value would be fabricated provenance | Route them to the reviewer_2 queue first | Audit finding 9 |
| A3 | **Linked reports** — collapse, keep-and-link, or leave | 2 links are the same underlying data (S294/S366 one trial; S097/S098 one interview sample), 2 overlap partly: 1,157 distinct studies (1,155 with the partial ones) instead of 1,159 rows; the 5 "RoB 2 studies" are 4 trials | Keep rows, treat linked reports as one study in any count or synthesis, decide before the manuscript | Audit finding 14; `03_extraction/extracted_data/linked_reports_2026-09-28.csv` |
| A4 | **Require a sensitivity analysis excluding the 67 abstract-only extractions (69 until S366 and S326 were re-extracted on 2026-09-29)** before publication? | They affect descriptive counts and ratings, not any effect-size row | Yes. **Script now exists and was run** (`code/analysis/sensitivity_analysis.py` → `05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`): no stated conclusion changes; the requirement itself is still your decision | Audit finding 7 |
| A5 | **`mechanism_family` / `outcome_family` taxonomy** | The fields hold 236 and 127 distinct values (uncontrolled labels), and 3 rows (S005, S041, S067) have a blank `mechanism_family`. A naive mechanical overwrite was deliberately not applied because it would destroy richer thematic labels | Choose a controlled vocabulary, then map. **A mechanical draft exists** (`05_analysis/descriptive/FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`, 45 studies flagged for review); nothing adopted, originals untouched | `05_analysis/descriptive/EVIDENCE_MAP_README.md` |
| A6 | **Human reviewer_2 pass** for full-text decisions | Only 100 of 1,159 includes (S001–S100) and 0 of 1,117 excludes are independently confirmed | Prioritise the 73 no-reviewer rows, then a random sample of excludes. **Queue and one-page checklist built** (`02_screening/full_text/REVIEWER_2_PRIORITY_QUEUE_README.md`, 226 rows); no human decisions recorded yet | `02_screening/full_text/REVIEWER_2_README.md` |
| A7 | **OSF preregistration** submission | Draft exists, not submitted | Submit and record the identifier in `PROTOCOL.md` | `00_admin/preregistration/` |
| A8 | **PRISMA 2020 items 25 (funding) and 26 (competing interests)** | No home in the repository yet | Add the disclosure text. **Prompt template created, content not filled** (`00_admin/disclosures/FUNDING_AND_COMPETING_INTERESTS_TEMPLATE.md`) | `06_outputs/prisma/PRISMA_2020_CHECKLIST.md` |
| A9 | **Verify checklist item wording** against the publishers' official texts (PRISMA 2020, AMSTAR 2, RoB 2, ROBINS-I, JBI, CASP, MMAT) | Verified only to search-snippet level; publisher sites were unreachable from the working environment | Needs someone with publisher access | `SOURCES.md` |
| A10 | **Release/versioning** — `CITATION.cff` still says version `0.1.0-interim`, released 2026-09-12 | Someone citing the dataset today would cite a state that no longer exists | Tag a release and update the version and date after A1–A4 | `CITATION.cff` |

## B. Judgment calls already made (all disclosed where they were made)

| Call | Where documented |
|---|---|
| Retrieval closed with 1,383 records never assessed (researcher decision) | README Known limitations 13; `02_screening/` |
| Non-validated Legal Institutional Evidence Appraisal Framework used for 447 studies | `RISK_OF_BIAS.md` §2; evidence-limitations note |
| Ratings are rule-based batch appraisals from extracted fields, not signalling-question reads | `RISK_OF_BIAS.md` §4; evidence-limitations note |
| Phase 11 verdict: no family clears the meta-analysis bar; all route to SWiM | `06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md` |
| Blank-family effect-size rows resolved as reasoned non-fits (16 rows) | `phase11_blank_family_resolution_2026-09-28.md` |
| S348 added to `effect_sizes.csv` after re-mining | `effect_sizes_remining_2026-09-28.md` |
| SWiM direction coding: S358, S404, S294, S879, S1062 read from full direction text; Family A concordance recount (S104, S1020, S1121 counter-pattern) | Family A/B/C synthesis documents |
| Exact duplicates merged, keeping the fuller full-text-based row (S233→S1008, S299→S392) | CHANGELOG 2026-09-28; audit finding 13 |
| S356 excluded E05 on its full text (non-systematic policy overview) | CHANGELOG 2026-09-28; audit finding 10 |
| Companion reports extracted as separate rows (precedent), now linked but not merged | Audit finding 14 |
| `mechanism_family` not mechanically overwritten | A5 above |

## C. Not verified

- **Extracted values against source papers.** The source PDFs are not in the repository and were not available to the audits;
  no second-extractor pass exists.
- **Risk-of-bias ratings** by any human.
- **Whether other same-paper duplicates exist** with different-language titles or a blank DOI: the check that found two covered the
  included studies only.
- **Overlap of samples between separate papers** (e.g. S526 and S539 both use large US utilities): inferred from extracted
  sample descriptions, not from the papers' data.

## D. Improvement backlog (no decision needed)

- ~~Add a `record_id` column to `extraction_database.csv`~~ — done 2026-09-28 (last column; verifier checks it against the map).
- Normalise `reviewer_1` labels (`Claude`, `claude`, `claude_sonnet_5`, date-stamped) with a documented mapping — decisions
  unchanged. Twelve decided rows also retain a stale `not_retrievable` status although they were decided.
- ~~Collapse the stale historical status rows in `PRISMA_WORKFLOW.md`~~ — done; old file archived verbatim at `11_archive/PRISMA_WORKFLOW_before_retirement_2026-09-28.md`.
- Extend `verify_repository.py` with any figure a future document quotes (boolean-field, freshness and queue checks added 2026-09-29).
- **New, from the S326 full-text reading (2026-09-29):** 13 included studies (S079, S320, S321, S322, S326, S429, S430, S436, S440, S466, S479, S480, S482) are self-described narrative or non-systematic reviews with tool `NONE`. Do they satisfy inclusion criterion 3 ("empirical evidence or a *systematic* empirical synthesis")? S356, a method-less policy overview with no primary data, was excluded E05 on 2026-09-28; these are narrative reviews *of* empirical studies. Options: keep as secondary context (not counted as evidence), exclude E05, or keep and report separately. Nothing applied.
- **New, from the S366 re-extraction (2026-09-29):** S366 now has full-text results (improved water source +33 pp, 95% CI 22 to 45). Decide whether to add an `effect_sizes.csv` row (it would count the same trial twice in Family B alongside S294 unless linked reports are collapsed — item A3), and whether LR01 should distinguish "same trial" from "same survey data" (S366: 1,312 households; S294: 3,283).
- **New, from the preliminary report:** (a) `AI_USE_STATEMENT.md` and `AUDITING_GUIDE.md` said title/abstract second review covered "all records"; the README says the human pass covered the 3,665 include-plus-unsure records, not the 22,557 AI excludes — **wording corrected 2026-09-29; researcher confirmed the README's narrower scope is correct**; (b) 12 of 24 AMSTAR 2 studies carry only a bare `systematic_review_secondary` label and 5 were extracted from abstracts (S319, S324, S325, S326, S344): confirm they are systematic reviews and decide whether AMSTAR 2 fits realist/scoping/mapping reviews; (c) confirm S879's randomisation unit and S189's parent trial (`06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md` §3.4).
