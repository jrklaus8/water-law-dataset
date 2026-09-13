# Scopus search string

Field: `TITLE-ABS-KEY`. Boolean: `AND` / `OR`. Phrase: `"..."`. Truncation: `*`.

```
TITLE-ABS-KEY(
  sanitation OR
  wastewater OR
  sewerage OR
  "sewer connection*" OR
  "water supply" OR
  "piped water" OR
  "municipal water" OR
  "water connection*" OR
  "water service*" OR
  "sanitation service*" OR
  WASH
)
AND
TITLE-ABS-KEY(
  "administrative burden" OR
  "administrative barrier*" OR
  "administrative law" OR
  "legal barrier*" OR
  eligibility OR
  "legal status" OR
  "legal recognition" OR
  "land tenure" OR
  "property title" OR
  documentation OR
  "building permit*" OR
  zoning OR
  formalization OR
  formalisation OR
  regularization OR
  regularisation OR
  "service area*" OR
  "administrative discretion" OR
  accommodation OR
  enforcement OR
  regulation OR
  "regulatory governance" OR
  governance OR
  institutional* OR
  bureaucratic
)
AND
TITLE-ABS-KEY(
  access OR
  connection OR
  coverage OR
  reliability OR
  affordability OR
  exclusion OR
  inclusion OR
  inequality OR
  inequity OR
  "service delivery"
)
```

## Notes

- This is the pilot string (`SEARCH_PROTOCOL.md` §5.1) — refine against the
  four preliminary source papers in `SOURCES.md` before running in earnest.
- Consider `DOCTYPE(ar OR re OR cp)` and a language limit
  (`LANGUAGE(english OR portuguese OR dutch)`) as filters, logged separately
  in the `filters` field of the search log — do not bake filters into the
  string itself so that the unfiltered result count is also recoverable.
- No date range is imposed by default; if one is applied (e.g. matching the
  judicial dataset's 2016–2026 window for comparability), record the
  rationale in `notes`.
- Status: **not yet executed.**
