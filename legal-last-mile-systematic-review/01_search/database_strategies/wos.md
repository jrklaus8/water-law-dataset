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
- Status: **not yet executed.**
