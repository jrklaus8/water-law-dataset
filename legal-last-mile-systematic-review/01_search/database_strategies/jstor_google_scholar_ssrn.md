# JSTOR, Google Scholar, and SSRN search strategies

These three platforms either lack full nested-Boolean support or actively
penalize very long queries, so the three-block AND string used for Scopus/
WoS must be simplified for each.

## JSTOR

Advanced Search supports `AND`/`OR`/`NOT` across up to a handful of stacked
fields, plus phrase quotes; no wildcard truncation beyond `?` (single
character) in most interfaces — spell out variants instead of truncating.

```
((sanitation OR wastewater OR "water supply" OR "water connection" OR
"sewer connection") AND ("administrative burden" OR "administrative
barrier" OR "legal recognition" OR "land tenure" OR eligibility OR
"regulatory governance" OR bureaucratic) AND (access OR connection OR
exclusion OR inclusion OR "service delivery"))
```

## Google Scholar

No field tags, minimal reliable Boolean (`OR` works, `AND` is implicit via
space, `-` excludes, `"..."` for phrase, no true truncation). Long queries
are silently truncated by the interface — keep to short representative
phrases and run several narrower queries rather than one long one; record
each as a separate `search_id`.

```
"water connection" OR "sanitation access" "administrative burden" OR
"legal recognition" OR "administrative barrier"
```
```
"land tenure" "water access" eligibility OR "informal settlement"
```
```
"aansluitplicht" drinkwater OR riolering
```
```
"regularização fundiária" "abastecimento de água" OR saneamento
```

Google Scholar results are not exportable in bulk with full metadata by
default — plan to screen the first several hundred results by relevance
ranking and record the cutoff point and rationale in `notes`, since Google
Scholar does not guarantee a stable, fully reproducible result set the way
the Tier 1 databases do.

## SSRN

Basic keyword search with `AND`/`OR`, phrase quotes; primarily working
papers and preprints — expect substantial overlap with papers later
published in the Tier 1 databases (flag for duplicate-publication handling,
`REPRODUCIBILITY.md` §"Duplicate publication policy").

```
("water connection" OR "sanitation access" OR "water access") AND
("administrative burden" OR "legal recognition" OR "administrative
barrier" OR "regulatory governance" OR "land tenure")
```

## Notes

- All three are Tier 2 sources per `SEARCH_PROTOCOL.md` §1 — used to
  supplement, not replace, the Tier 1 database searches, and are
  particularly useful for grey/working-paper versions of studies later
  published in Tier 1 venues.
- Status: **not yet executed.**
