# Westlaw and Lexis search strategies

Legal-research platforms use connector syntax rather than plain
AND/OR/parentheses, and the two platforms differ from each other.

## Westlaw (Terms and Connectors)

`&` = AND, blank space between quoted phrases = OR (or explicit `OR`),
`/s` = same sentence, `/p` = same paragraph, `!` = truncation, `"..."` = phrase.

```
(sanitation "sewer connection!" "water supply" "piped water" "municipal
water" "water connection!" "water service!" WASH)
/p
("administrative burden" "administrative barrier!" "administrative law"
"legal barrier!" eligibility "legal recognition" "land tenure" "property
title" documentation "building permit!" zoning formaliz! formalis!
regulariz! regularis! "administrative discretion" enforcement "regulatory
governance" bureaucratic)
/p
(access! connection coverage reliability affordability exclusion inclusion
"service delivery")
```

## Lexis+ (Lexis Advance connectors)

`AND` / `OR` supported directly; `W/n` for proximity (e.g. `W/25`); `!` for
truncation; `"..."` for phrase.

```
(sanitation OR "sewer connection!" OR "water supply" OR "piped water" OR
"municipal water" OR "water connection!" OR "water service!" OR WASH)
AND
("administrative burden" OR "administrative barrier!" OR "administrative
law" OR "legal barrier!" OR eligibility OR "legal recognition" OR "land
tenure" OR "property title" OR documentation OR "building permit!" OR
zoning OR formaliz! OR formalis! OR regulariz! OR regularis! OR
"administrative discretion" OR enforcement OR "regulatory governance" OR
bureaucratic)
AND
(access! OR connection OR coverage OR reliability OR affordability OR
exclusion OR inclusion OR "service delivery")
```

## Notes

- These platforms index primary law (statutes, regulations, case law) and
  secondary sources (law reviews, treatises) together — restrict to
  Secondary Sources / Law Reviews & Journals for the systematic review's
  scholarship search, and treat any primary-law hits (statutes, regulations)
  as candidate legal authorities for the doctrinal side of the dissertation
  rather than as systematic-review "studies."
- The `/p` (same paragraph) connector on Westlaw is a coarser proximity
  filter than Boolean AND across an entire document — if it returns too few
  results, fall back to `/s` "document contains all three clause sets"
  behavior via the platform's full-text AND, and log which connector was
  actually used.
- Status: **not yet executed.**
