# Resolution of the 9 never-evaluated blank-`synthesis_family` rows — 2026-09-28

Closes the item Phase 11 §6 and §8 explicitly left open: "9 rows carry no family-fit
discussion at all... this document does not resolve [them]." Phase 11
(`06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md`) found that 9 of the
18 originally-blank `effect_sizes.csv` rows — S434, S435, S445, S448, S470, S471, S483, S489,
S491 — had apparently been added to the corpus without ever being checked against
`PROJECT_SPEC.md` §8's Family A/B/C definitions, unlike their 9 blank siblings (S149, S178,
S312, S353, S388, S636, S649, S795, S869), each of which already carried a genuine, reasoned
non-fit judgment.

## Method

The same side-by-side comparison Phase 11 gave the other 52 rows, applied here to these 9:
read each row's `exposure_definition`, `comparator_definition`, and `outcome_family` against
`PROJECT_SPEC.md` §8's three family definitions, and — critically — against the *already
established precedent* of how structurally similar exposures were judged elsewhere in the
corpus, rather than deciding each in isolation. Four precedent categories did almost all of
the work:

- **Fiscal-transfer/grant-mechanism exposures don't map to Family A/B/C** — established by
  S636 (Indonesia's Water Hibah performance-grant program) and S649 (Mexico's federal
  intergovernmental transfers), both already excluded on this basis.
- **Intermunicipal-cooperation-arrangement exposures don't map to Family A/B/C** —
  established by S869 (Brazilian sanitation consortium).
- **Jurisdiction/institution-level policy-adoption outcomes aren't household-level access
  outcomes** — established by S312 (state/city moratorium-adoption).
- **Governance/regulatory-structure exposures tested against a price/affordability outcome
  *do* fit Family C** — established by S1038 (state-vs-local economic regulation of
  municipal utilities), which already carries the `C` tag Phase 11 left standing.

## Result: 2 corrected to Family C, 7 confirmed as reasoned non-fits

| Study | Verdict | Precedent applied |
|---|---|---|
| S434 | Non-fit (blank) | Exposure (mine-site proximity) is economic/geographic, not legal or administrative at all |
| S435 | Non-fit (blank) | Outcome is institution-level policy adoption, not household access — same as S312 |
| S445 | Non-fit (blank) | Exposure is a school-funding-formula proxy — same category as S636/S649; also school-, not household-, level |
| S448 | Non-fit (blank) | Exposure is an intermunicipal cooperation arrangement — same category as S869 |
| **S470** | **→ Family C** | Regulatory enforcement of an eligibility-based social tariff → affordability-program enrollment — an eligibility-restriction mechanism + affordability outcome, the same kind of pairing already accepted for S1038 |
| **S471** | **→ Family C** | Municipal-government-form (mayor-led vs. manager/council-led) → water-price outcome — a regulatory-structure/affordability pairing, directly parallel to S1038 |
| S483 | Non-fit (blank) | Exposure is income-based residential classification, not a legal/administrative mechanism (tenure security is discussed narratively but not tested) |
| S489 | Non-fit (blank) | Exposure is a household perception/attitude variable (perceived cost), not an institutional mechanism |
| S491 | Non-fit (blank) | The moratorium is a genuine legal mechanism, but the tested exposure is a household payment-history characteristic that both groups experience the moratorium equally under — the legal mechanism itself is not the exposure-comparator being estimated |

Full reasoning for each row is recorded in `effect_sizes.csv`'s `exclusion_from_pooling_reason`
field, following the same convention Phase 11 used for S749's correction — not summarized away
here.

## Effect on the corpus-level family counts

| `synthesis_family` | Before this pass | After |
|---|---|---|
| A | 20 | 20 |
| B | 6 | 6 |
| C | 17 | **19** |
| *(blank, reasoned non-fit)* | 18 | 16 |
| **Total** | **61** | **61** |

S470 and S471 join S1038 as a small, presentation-worthy sub-grouping within Family C's SWiM
synthesis — "institutional/regulatory structure and affordability" — alongside, but distinct
from, the ownership/price cluster (S526, S539, S749) addressed separately in
`phase11_pooling_feasibility_S526_S539_S749.md`. **Neither correction changes Phase 11's
overall verdict**: Family C still does not clear `ANALYSIS_PLAN.md` §2's bar for
meta-analysis, and still routes to structured synthesis (SWiM) instead — see
`family_C_swim_synthesis_2026-09-28.md`.

## What this does not do

This resolves the 9 rows' family *classification* only. It does not change any row's
`effect_estimate`, `direction`, `adjusted`, or `evidence_status` — those remain exactly as
originally extracted. It also does not reopen the 9 already-reasoned non-fits from Phase 11
§6 (S149, S178, S312, S353, S388, S636, S649, S795, S869), which were not re-litigated here.
