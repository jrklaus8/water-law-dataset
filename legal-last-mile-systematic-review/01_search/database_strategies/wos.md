# Web of Science search string

Field: `TS=` (Topic: title, abstract, author keywords, Keywords Plus).
Boolean: `AND` / `OR` (must be explicit and capitalized). Phrase: `"..."`.
Truncation: `*`.

```
TS=(
  sanitation OR wastewater OR sewerage OR "sewer connection*" OR
  "water supply" OR "piped water" OR "municipal water" OR
  "water connection*" OR "water service*" OR "sanitation service*" OR WASH
)
AND
TS=(
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
TS=(
  access OR connection OR coverage OR reliability OR affordability OR
  exclusion OR inclusion OR inequality OR inequity OR "service delivery"
)
```

## Notes

- Direct field-syntax port of `scopus.md`; WoS `TS=` is broader than Scopus
  `TITLE-ABS-KEY` (it includes Keywords Plus), so expect a higher raw hit
  count for an equivalent search — do not treat the two counts as directly
  comparable without checking for this.
- Restrict to Web of Science Core Collection indexes (SCI-EXPANDED,
  SSCI, A&HCI, ESCI) explicitly and record which in the search log `filters`
  field — different index combinations return different results.
- Status: **executed 2026-09-11 (`SEARCH_035`)** — 4,058 records across 5
  export batches (WoS's native 1,000-record export cap), all with
  abstracts. Core Collection index selection actually used was not
  reported back to the pipeline — flagged in `search_log.csv`'s `filters`
  field as unconfirmed rather than guessed; worth double-checking with
  whoever ran it. `code/search/adapters/wos_adapter.py` is now
  **validated against this real export** (it wasn't when first written —
  found and fixed two real bugs in the process: no tab-delimited support
  initially, and a quote-escaping parsing bug that was silently
  corrupting ~1-2% of records before the fix; see `CHANGELOG.md`
  2026-09-11 (later)). This batch's include/unsure rate after screening
  (~13%) came in well below the ~25-30% seen in Scopus batches — expected,
  since `TS=` is broader than Scopus's `TITLE-ABS-KEY` and this batch is
  only the WoS-unique residue after cross-database dedup against Scopus
  removed the overlap.
