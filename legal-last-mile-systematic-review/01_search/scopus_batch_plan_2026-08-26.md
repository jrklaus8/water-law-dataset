# Scopus Batch Export Plan (2026-08-26)

Purpose: get the remaining ~4,944 of the ~5,444 total matching records
(500 already captured in `SEARCH_018`), split into batches small enough to
actually clear whatever export ceiling Scopus enforced last time (the one
real export we've seen stopped at exactly 500, so every batch below
targets comfortably under that). Built from the real year-by-year
breakdown in `01_search/raw_exports/native/SEARCH_018_SCOPUS_2026-08-26_analyze-by-year.csv`
— not a guess.

**For every batch: follow `EXECUTION_CHECKLIST.md`'s Scopus section exactly
— Advanced Search, export all results as CSV, and this time tick
Abstract in the field picker.** Log the actual result count Scopus shows
before export; if it doesn't match the `n~` estimate below, note that too
— the estimates are from a raw hit count, not a guarantee.

## Base string (identical in every batch — only the PUBYEAR clause changes)

```
TITLE-ABS-KEY(
  sanitation OR wastewater OR sewerage OR "sewer connection*" OR
  "water supply" OR "piped water" OR "municipal water" OR
  "water connection*" OR "water service*" OR "sanitation service*" OR WASH
)
AND
TITLE-ABS-KEY(
  "administrative burden" OR "administrative barrier*" OR
  "administrative law" OR "legal barrier*" OR eligibility OR
  "legal status" OR "legal recognition" OR "land tenure" OR
  "property title" OR documentation OR "building permit*" OR zoning OR
  formalization OR formalisation OR regularization OR regularisation OR
  "service area*" OR "administrative discretion" OR accommodation OR
  enforcement OR regulation OR "regulatory governance" OR governance OR
  institutional* OR bureaucratic
)
AND
TITLE-ABS-KEY(
  access OR connection OR coverage OR reliability OR affordability OR
  exclusion OR inclusion OR inequality OR inequity OR "service delivery"
)
```

## Batches

Paste the base string above, **AND**ed with the year clause shown, into
Scopus Advanced Search. Save each export as
`SEARCH_0NN_SCOPUS_2026-08-26.csv` using the search_id shown.

| search_id | Years | Est. n | Year clause to AND onto the base string |
|---|---|---|---|
| SEARCH_019 | 2027 | ~1 | `PUBYEAR = 2027` |
| SEARCH_020a | 2026, articles+reviews only | ~? | `PUBYEAR = 2026 AND DOCTYPE(ar OR re)` — see note below |
| SEARCH_020b | 2026, everything else | ~? | `PUBYEAR = 2026 AND NOT DOCTYPE(ar OR re)` |
| SEARCH_021a | 2025, articles+reviews only | ~? | `PUBYEAR = 2025 AND DOCTYPE(ar OR re)` |
| SEARCH_021b | 2025, everything else | ~? | `PUBYEAR = 2025 AND NOT DOCTYPE(ar OR re)` |
| SEARCH_022 | 2024 | ~391 | `PUBYEAR = 2024` |
| SEARCH_023 | 2023 | ~337 | `PUBYEAR = 2023` |
| SEARCH_024 | 2022 | ~326 | `PUBYEAR = 2022` |
| SEARCH_025 | 2021 | ~324 | `PUBYEAR = 2021` |
| SEARCH_026 | 2020 | ~273 | `PUBYEAR = 2020` |
| SEARCH_027 | 2019 | ~254 | `PUBYEAR = 2019` |
| SEARCH_028 | 2018 | ~241 | `PUBYEAR = 2018` |
| SEARCH_029 | 2016–2017 | ~375 | `PUBYEAR > 2015 AND PUBYEAR < 2018` |
| SEARCH_030 | 2014–2015 | ~315 | `PUBYEAR > 2013 AND PUBYEAR < 2016` |
| SEARCH_031 | 2012–2013 | ~293 | `PUBYEAR > 2011 AND PUBYEAR < 2014` |
| SEARCH_032 | 2009–2011 | ~367 | `PUBYEAR > 2008 AND PUBYEAR < 2012` |
| SEARCH_033 | 2003–2008 | ~388 | `PUBYEAR > 2002 AND PUBYEAR < 2009` |
| SEARCH_034 | 1928–2002 (everything older) | ~357 | `PUBYEAR > 1927 AND PUBYEAR < 2003` |

**Note on 2026 and 2025 (`SEARCH_020`/`SEARCH_021`):** these two years
alone (619 and 583 records) exceed the 500-record ceiling even as single
years, so each needs a further split. `DOCTYPE(ar OR re)` (articles and
reviews only) vs. its negation is one reasonable way to split without
losing anything — check the result count for each half before exporting;
if either half is *still* over ~450, split it again the same way using a
different `DOCTYPE` boundary (e.g. isolate `cp` conference papers, `ch`
book chapters, or `no` notes into their own batch) rather than truncating.

## After each export

Send the resulting file back. For each one Claude will:

1. Run it through `code/search/adapters/scopus_adapter.py` (already
   validated against a real Scopus export).
2. Preserve the untouched original in
   `01_search/raw_exports/native/` alongside the normalized version in
   `01_search/raw_exports/`.
3. Log it as its own row in `01_search/search_logs/search_log.csv`.
4. Re-run `code/search/deduplicate.py` across everything accumulated so
   far (catches duplicates both within Scopus and against the earlier
   WebSearch-pilot records).
5. Re-run `code/screening/init_screening_db.py` to merge new unique
   records into the screening database.

Once abstracts are present for the first time, real title/abstract
screening against `INCLUSION_EXCLUSION.md` becomes possible — that's the
actual milestone this batch plan is working toward, not just a bigger
number of unscreened records.

## Status

Not yet executed. `SEARCH_018` (the first 500, no abstracts) remains the
only Scopus data actually in the pipeline as of 2026-08-26.
