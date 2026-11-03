# Reproducibility

## 1. What another researcher must be able to reproduce

1. Every database search.
2. Every deduplication decision.
3. Every screening decision.
4. Every exclusion decision.
5. Every extracted value.
6. Every effect-size calculation.
7. Every risk-of-bias judgment.
8. Every meta-analytic result.
9. Every figure.
10. Every table.

## 2. Raw vs. processed data

Raw data is never overwritten. `data/raw/` holds untouched exports (search
results, extraction-form exports); `data/processed/` holds derived/cleaned
versions produced by scripts in `code/`; `data/metadata/` holds
schema/codebook snapshots. The canonical machine-readable format is CSV;
XLSX is permitted for human review copies only, regenerated from the CSV,
never hand-edited independently of it.

Search-export naming convention (`SEARCH_PROTOCOL.md` §6):
`SEARCH_{NNN}_{DATABASE}_{YYYY-MM-DD}.csv` in `01_search/raw_exports/`.

## 3. Evidence provenance

Every extracted statistic carries provenance fields (`CODEBOOK.md` §11):
`source_document`, `page`, `table`, `figure`, `section`, `exact_location`,
`extraction_note`, `researcher`, `date_extracted`.

Worked example:

```
study_id = S001
source_document = article.pdf
page = 12
table = Table 3
measure = OR
value = <extracted value>
note = adjusted model
```

This is essential for publication review and for anyone auditing a pooled
estimate back to its source.

## 4. Observed / calculated / assumed / interpreted

See `PROJECT_SPEC.md` §13 and `CODEBOOK.md` §10. Never blur these
categories — an `ASSUMED` standard error must never be silently presented in
a table alongside `OBSERVED` values without the distinction being visible.

## 5. Missing data policy

Never silently impute a missing effect size. If one is unavailable: (1)
search supplementary material, (2) search the repository/dataset version of
the paper, (3) search the author-manuscript version, (4) search a
dissertation or working-paper version, (5) contact authors where
appropriate, (6) record the missingness explicitly (leave the field blank
with a note, not a zero or an inferred value). Do not infer a statistic
without a transparent calculation and documented assumptions logged in
`09_data_dictionary/transformations/`.

## 6. Duplicate publication policy

Identify: conference abstract + journal article; working paper + journal
article; preprint + published article; multiple reports from the same
dataset; multiple papers from the same intervention. Where multiple reports
describe the same underlying study, **treat the underlying study as one
study** — select the most complete report for primary extraction, retain
linked reports for supplementary information, and cross-reference their
`study_id`s.

(Watch for this specifically in the SSRN/working-paper search results —
`01_search/database_strategies/jstor_google_scholar_ssrn.md` — and around
the Gaikwad/Thomas field-experiment literature, which appears to have an
earlier working-paper title, "Bureaucratic Hurdles, Political Resistance,
and Public Service Access," distinct from the 2026 AJPS publication title —
verify at full-text stage whether these are the same underlying study
before extracting both.)

## 7. Computational stack

R packages, when analysis code is written (not before there is data to
analyze): `metafor`, `meta` (primary); `tidyverse`, `dplyr`, `readxl`,
`openxlsx`, `janitor`, `ggplot2`, `robvis` (supporting). Python where useful
for search/screening/extraction tooling. Reporting via Quarto. Do not add a
package the analysis does not actually require.

Record the actual computational environment (language/package versions) in
`10_reproducibility/computational_environment/` once analysis code exists —
currently empty, since no analysis has been run.

## 8. Version history

Log substantive methodological changes (not routine documentation fixes) in
`10_reproducibility/version_history/` and in the root `CHANGELOG.md`,
including any amendment to the registered protocol per `PROTOCOL.md` §12.
