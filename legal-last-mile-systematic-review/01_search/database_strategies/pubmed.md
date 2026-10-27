# PubMed / Global Health (Ovid) search strings

## PubMed

Field tag `[tiab]` (title/abstract); MeSH terms are supplementary, not
required, since this is a governance/legal topic rather than a clinical one.
Truncation `*`. Boolean must be capitalized.

```
(sanitation[tiab] OR wastewater[tiab] OR sewerage[tiab] OR "sewer
connection"[tiab] OR "water supply"[tiab] OR "piped water"[tiab] OR
"municipal water"[tiab] OR "water connection"[tiab] OR "water
service"[tiab] OR "sanitation service"[tiab] OR WASH[tiab])
AND
("administrative burden"[tiab] OR "administrative barrier"[tiab] OR
"administrative law"[tiab] OR "legal barrier"[tiab] OR eligibility[tiab] OR
"legal status"[tiab] OR "legal recognition"[tiab] OR "land tenure"[tiab] OR
"property title"[tiab] OR documentation[tiab] OR "building permit"[tiab] OR
zoning[tiab] OR formalization[tiab] OR formalisation[tiab] OR
regularization[tiab] OR regularisation[tiab] OR "service area"[tiab] OR
"administrative discretion"[tiab] OR accommodation[tiab] OR
enforcement[tiab] OR regulation[tiab] OR "regulatory governance"[tiab] OR
governance[tiab] OR institutional*[tiab] OR bureaucratic[tiab])
AND
(access[tiab] OR connection[tiab] OR coverage[tiab] OR reliability[tiab] OR
affordability[tiab] OR exclusion[tiab] OR inclusion[tiab] OR
inequality[tiab] OR inequity[tiab] OR "service delivery"[tiab])
```

PubMed does not support truncation inside phrase quotes and applies
automatic term mapping unless `[tiab]` is specified on every term — hence
every term above is explicitly tagged rather than left bare.

## Global Health (Ovid)

Ovid syntax uses `.ti,ab.` field suffixes and `adj`/`.mp.` operators; port
the same three concept blocks using:

```
(sanitation or wastewater or sewerage or "sewer connection$" or "water
supply" or "piped water" or "municipal water" or "water connection$" or
"water service$" or "sanitation service$" or WASH).ti,ab.
AND
("administrative burden" or "administrative barrier$" or "administrative
law" or "legal barrier$" or eligibility or "legal status" or "legal
recognition" or "land tenure" or "property title" or documentation or
"building permit$" or zoning or formalization or formalisation or
regularization or regularisation or "service area$" or "administrative
discretion" or accommodation or enforcement or regulation or "regulatory
governance" or governance or institutional$ or bureaucratic).ti,ab.
AND
(access or connection or coverage or reliability or affordability or
exclusion or inclusion or inequality or inequity or "service
delivery").ti,ab.
```

(Ovid uses `$` for truncation rather than `*`.)

## Notes

- Expect low yield relative to Scopus/WoS — PubMed/Global Health are
  included because WASH (water, sanitation, hygiene) has a public-health
  literature that sometimes reports legal/administrative eligibility factors
  as a covariate rather than a primary exposure; screen accordingly.
- Status: **not yet executed.**
