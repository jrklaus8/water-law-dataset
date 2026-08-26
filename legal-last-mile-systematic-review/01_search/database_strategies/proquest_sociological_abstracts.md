# ProQuest and Sociological Abstracts search string

Both run on the ProQuest platform. Field: `noft()` (anywhere except full
text) or `ti,ab` restriction via the Advanced Search field pickers; Boolean
`AND`/`OR`/`NOT`; phrase `"..."`; truncation `*`; wildcard `?`.

```
noft(sanitation OR wastewater OR sewerage OR "sewer connection*" OR "water
supply" OR "piped water" OR "municipal water" OR "water connection*" OR
"water service*" OR "sanitation service*" OR WASH)
AND
noft("administrative burden" OR "administrative barrier*" OR
"administrative law" OR "legal barrier*" OR eligibility OR "legal status"
OR "legal recognition" OR "land tenure" OR "property title" OR
documentation OR "building permit*" OR zoning OR formalization OR
formalisation OR regularization OR regularisation OR "service area*" OR
"administrative discretion" OR accommodation OR enforcement OR regulation
OR "regulatory governance" OR governance OR institutional* OR bureaucratic)
AND
noft(access OR connection OR coverage OR reliability OR affordability OR
exclusion OR inclusion OR inequality OR inequity OR "service delivery")
```

## Notes

- In the ProQuest UI, replace `noft(...)` with the "Anywhere except full
  text" field picker if searching interactively rather than pasting a raw
  command-line query; the parenthetical syntax above works in the Advanced
  Search command-line box.
- For **Sociological Abstracts** specifically, also run a narrower version
  restricted to the platform's own controlled-vocabulary thesaurus terms
  (e.g. "public utilities", "water resources", "bureaucracy",
  "administrative agencies") to catch records indexed on subject rather than
  keyword — log this as a second `search_id` in the search log rather than
  merging it into the main string.
- Status: **not yet executed.**
