# HeinOnline search strategy

HeinOnline's search (Law Journal Library, core full-text search) supports
`AND`/`OR`/`NOT`, phrase quotes, and `*` truncation, but does **not** support
the same nested-parenthesis Boolean depth as Scopus/WoS well in its basic
search bar — use the Advanced Search fielded form (Title / Full Text /
Author) instead of a single mega-string, and run each concept block as a
separate fielded clause combined with AND.

Recommended approach: three sequential Full-Text searches, ANDed via the
Advanced Search builder:

**Clause 1 (service):**
```
sanitation OR wastewater OR sewerage OR "sewer connection" OR "water
supply" OR "piped water" OR "municipal water" OR "water connection" OR
"water service" OR "sanitation service"
```

**Clause 2 (mechanism):**
```
"administrative burden" OR "administrative barrier" OR "administrative
law" OR "legal barrier" OR eligibility OR "legal recognition" OR "land
tenure" OR "property title" OR documentation OR "building permit" OR
zoning OR formalization OR formalisation OR regularization OR
regularisation OR "administrative discretion" OR enforcement OR
"regulatory governance" OR bureaucratic
```

**Clause 3 (outcome):**
```
access OR connection OR coverage OR reliability OR affordability OR
exclusion OR inclusion OR "service delivery"
```

## Notes

- HeinOnline is a full-text law-journal archive: expect many false
  positives from incidental co-occurrence of common words like "access" and
  "regulation" in unrelated articles — title/abstract screening precision
  will be lower here than for Scopus/WoS. Budget accordingly.
- Also run a targeted secondary search restricted to Title, using only the
  narrower legal-mechanism terms ("administrative burden", "legal
  recognition", "regularização fundiária", "aansluitplicht") combined with
  "water" OR "sanitation", to surface doctrinal/legal-scholarship pieces
  that a full-text search would bury.
- Status: **not yet executed.**
