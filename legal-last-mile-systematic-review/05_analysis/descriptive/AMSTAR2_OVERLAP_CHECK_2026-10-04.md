# AMSTAR 2 reviews: do they share primary studies with the corpus? (2026-10-04)

*Produced by `code/provenance/audit_and_repair/check_amstar2_overlap_2026-10-04.py`. Read-only; changes no database. A hit means a corpus study is **cited anywhere** in a review's reference list (DOI or exact-title match), so it is an **upper bound** on the primary studies the review pooled (background citations count). Only 7 of the 23 AMSTAR 2 reviews could be checked (their PDFs were on this machine); the other 16 — including S697 and S438, which were read through Drive — are **unchecked**. Matching is by DOI or a title of at least 40 normalised characters, so it misses references with different wording or no DOI.*

| Review | Rating | Reference section found | DOIs in reference list | Corpus studies cited | Corpus AMSTAR 2 reviews cited |
|---|---|---|---|---|---|
| S052 | Critically Low | yes | 40 | 4 | — |
| S319 | Critically Low | yes | 49 | 21 | — |
| S324 | Critically Low | yes | 25 | 2 | S372 |
| S325 | Critically Low | yes | 39 | 19 | S697 |
| S327 | Low | yes | 38 | 1 | S372 |
| S344 | Critically Low | yes | 12 | 0 | — |
| S418 | Critically Low | yes | 1 | 2 | — |

## Corpus studies cited by two or more of the checked reviews

| Corpus study | Cited by | Title |
|---|---|---|
| S372 | S324, S327 | How community participation in water and sanitation interventions impacts human health, WA |

## What this does and does not show

- Across the 7 checked reviews, **48 distinct corpus studies** are cited at least once and **1** by two or more. Most hits, if any, are background citations rather than pooled primary studies.
- A review citing another corpus review is a different risk: that review's findings may already be counted through its own extraction. Column 6 lists those.
- The question the report asks — *would the same primary study be counted once as its own row and again inside a review?* — can only be settled from each review's included-studies list (appendix or table), which this check did not read.
- Nothing was changed: reviews stay secondary evidence and are never pooled as independent primary effects (RISK_OF_BIAS.md §1).
