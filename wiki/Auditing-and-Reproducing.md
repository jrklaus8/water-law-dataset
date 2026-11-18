# Auditing and Reproducing the Systematic Review

> The aim of this project is to be as open as possible about what was done, how far it can be checked, and where it is weak, so that other researchers can find the weak points and do better research. This page is the map. Files named here are in the review folder `legal-last-mile-systematic-review/`, on the branch [`claude/legal-last-mile-review-spec-8ri0zs`](https://github.com/jrklaus8/water-law-dataset/tree/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review) until it is merged into `main`.

## Start here

[`START_HERE.md`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/START_HERE.md) is the whole project on one page (what it is, what was done and by whom, what to trust, three reading paths). [`GLOSSARY.md`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/GLOSSARY.md) explains every label (`A28`, `CK`, "AI-checked"). Every numbered folder has its own `README.md`.

## The transparency files

Each has a CSV for filtering and joining. The first four are generated from the databases and checked by the repository verifier on every run, so they cannot go stale.

| Question | File |
|---|---|
| What are the weak points, and how do I test or break each? | [`00_admin/WEAKNESSES.md`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/00_admin/WEAKNESSES.md) (data: `WEAKNESS_REGISTER.csv`) |
| For one study, what has a human actually checked? | [`00_admin/STUDY_AUDIT_TRAIL.csv`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/00_admin/STUDY_AUDIT_TRAIL.md), one row per included study |
| Which AI did what at each stage, and what is not archived? | [`00_admin/AI_USE_LEDGER.md`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/00_admin/AI_USE_LEDGER.md) |
| Where did the project depart from its plan, and which errors did it find in itself? | [`00_admin/DEVIATIONS_AND_ERRORS.md`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/00_admin/DEVIATIONS_AND_ERRORS.md) (hand-maintained data) |
| How far can it be reproduced, and how? | [`10_reproducibility/REPRODUCE.md`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/10_reproducibility/REPRODUCE.md) |
| Are the files I hold the files that were analysed? | [`10_reproducibility/DATA_MANIFEST.csv`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/10_reproducibility/DATA_MANIFEST.csv) (SHA-256 of every data file) |

## How far it can be reproduced

| Level | What | Needs |
|---|---|---|
| 0. Read | Everything the project reports | A browser |
| 1. Verify | That the databases, documents and registers agree with each other and with the manifest | Python 3 standard library, about 30 seconds |
| 2. Regenerate | Every derived table, register, report and figure from the stored decisions | + `openpyxl`, `python-docx`, `matplotlib`; about 90 seconds |
| 3. Re-derive from the sources | Whether extracted numbers match the papers | The papers (not in the repository) |
| 4. Redo the judgments | Screening, extraction, appraisal, direction coding | A human or an AI; **not** reproducible by re-running, because AI decisions are not deterministic and most prompts and model versions were not recorded |
| 5. Redo the search | The records | Institutional database access; results will differ as databases change |

A recorded fresh-clone run passed levels 1 and 2: apart from seven rendered files (five SVG figures, the report HTML that embeds them, and the Word executive summary, which differ only in drawing details), every output was byte-identical. It was made by the AI that wrote the code, so it is not an independent reproduction; one is wanted.

**A passing reproduction shows that the pipeline faithfully reports the stored decisions. It does not show that the decisions are right.**

## The weaknesses the AI would attack first

These are the AI's own ratings (not an independent reviewer's); the register has the evidence and a test for each.

- **W01** Planned databases were not searched or not exported (SSRN, Westlaw/Lexis, most of HeinOnline and JSTOR).
- **W05** Over a third of the candidates that reached the full-text stage were never assessed.
- **W06** Every title/abstract exclusion was made by the AI; none was checked by a human beyond a 120-record spot-check.
- **W08, W09** Most full-text exclusions and inclusions are AI-only. The one measured false-exclusion rate (3 of 62, 4.8%) is not small.
- **W11** The same AI family made the screening, extraction, appraisal and classification decisions, so its errors can be correlated.
- **W12** Every extraction was made by one AI; no second extractor has checked any; the error rate is unmeasured.
- **W16** Most risk-of-bias ratings are rule-based batch ratings, not readings of each paper.
- **W19, W20** The syntheses are vote counts on very few studies, and the author has confirmed none of the direction codings.
- **W21** Scope rulings on synthesis studies were made after the effect rows and direction counts were visible.
- **W28** The prompts, model versions and settings behind the main AI work are not archived.

## Report what you find

Use the [audit report form](https://github.com/jrklaus8/water-law-dataset/issues/new?template=audit-report.yml) (available once the review is merged), quoting the weakness, error or study ID. A failed test is as useful as a passed one. See also [[Systematic Review]], [[AI Disclosure]] and [[Contributing]].
