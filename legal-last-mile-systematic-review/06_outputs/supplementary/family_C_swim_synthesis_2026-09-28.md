# SWiM Synthesis — Family C (Administrative/legal barriers and access inequality) — 2026-09-28

## Why this family did not proceed to meta-analysis

`ANALYSIS_PLAN.md` §2's decision tree fails at the comparability fork, as it does for Family
A, but Family C is the family `PROJECT_SPEC.md` §8 itself flagged in advance as "conceptually
attractive but potentially too heterogeneous; treat as secondary synthesis unless evidence is
unusually consistent." That prediction holds: of the 20 studies (17 originally, plus S470 and
S471 corrected in from blank on 2026-09-28 — see
`phase11_blank_family_resolution_2026-09-28.md` — and S348, a genuine new addition found by a
re-mining pass the same day, see `effect_sizes_remining_2026-09-28.md`), only one genuine 3-study sub-cluster (§"The
ownership/price cluster" below) shares even a family-resemblance estimand, and even that
cluster cannot be pooled — see
`phase11_pooling_feasibility_S526_S539_S749.md`'s dedicated methods note, which concludes no
defensible common-metric transformation exists for it. The other 16 studies each test a
distinct administrative/legal-barrier mechanism in a distinct national context — see
`phase11_quantitative_feasibility_judgment.md` §5.2's list. **This is the least internally
consistent of the three families, exactly as `PROJECT_SPEC.md` anticipated before any evidence
was gathered.**

## Studies included in this synthesis

| Study | Country | Design | Direction (as extracted) | RoB tool / rating |
|---|---|---|---|---|
| S174 | Brazil | Cross-sectional regression | Positive — higher institutional capacity → better sanitation indicators | JBI Cross-Sectional — Some concern |
| S470 | Brazil | Quasi-experimental before/after panel | Positive — regulatory enforcement → higher social-tariff enrollment | ROBINS-I — Moderate |
| S471 | United States | Cross-sectional (national, 2,119 municipalities) | Negative — mayor-led government → lower water cost | JBI Cross-Sectional — Low concern |
| S526 | United States | Cross-sectional regression | Negative — private ownership → more regressive pricing | JBI Cross-Sectional — Some concern |
| S539 | United States | Cross-sectional (500 utilities) | Positive — private ownership/pro-private regulation → higher price, lower affordability | JBI Cross-Sectional — Some concern |
| S590 | Germany (historical) | Historical quasi-experimental logit | Positive — concentrated local political power (wealthy taxpayers) → outcome | JBI Cross-Sectional — Some concern |
| S593 | South Korea | Cross-sectional, multi-year | Mixed — administrative classification/tax burden associated with greater [effect varies by measure] | JBI Cross-Sectional — Some concern |
| S606 | China | Panel-data observational | Negative — unregistered temporary-resident share → lower per-capita provision | ROBINS-I — Moderate |
| S631 | Indonesia | Quasi-experimental panel (exogenous admin. timing) | Negative — local government proliferation → lower access | JBI Cross-Sectional — Low concern |
| S749 | Brazil | Quasi-experimental panel | Positive — private ownership → higher tariffs (lower affordability) | JBI Cross-Sectional — Some concern |
| S879 | Kenya | Cluster-RCT | Mixed — positive for payment compliance, null for water access/connection | RoB 2 (cluster) — Some concerns |
| S947 | 44 African countries | Dynamic panel GMM | Positive — higher institutional/regulatory quality → greater access | ROBINS-I — Moderate |
| S1032 | India | Quantitative regression | Negative — redress-seeking contact → reduced odds of complaint resolution | JBI Cross-Sectional — Some concern |
| S1038 | United States | Econometric (1965 cross-section) | Negative — state-level regulation → lower excess pricing (better affordability) | JBI Cross-Sectional — Low concern |
| S1062 | 22 Sub-Saharan African countries | Panel econometric | Mixed — positive up to a threshold, then negative (curvilinear) | ROBINS-I — Moderate |
| S1136 | India | Regression-based institutional-mechanism study | Positive — political proximity → more infrastructure; SC/ST residence → less | JBI Cross-Sectional — Some concern |
| S1143 | United States | Regression-based institutional-mechanism study | Mixed — weight rule favors better-off areas; supplementary rule favors equity | JBI Cross-Sectional — Low concern |
| S1146 | Multi-country Africa (Afrobarometer) | Regression-based | Negative — higher corruption → lower likelihood of adequate service | ROBINS-I — Moderate |
| S1162 | India | Panel/cross-sectional multilevel regression | Negative — lower admin. capacity/category → lower access | JBI Cross-Sectional — Some concern |
| S348 | Ghana | Fuzzy c-means clustering + hierarchical multivariate regression | Negative — weak governance quality (independent of poverty) → substantially reduced access | JBI Cross-Sectional — Some concern |

Pulled from `effect_sizes.csv` and `extraction_database.csv`; not re-extracted. RoB ratings as
of the 2026-09-28 corpus-wide pass — `RISK_OF_BIAS.md` §4. **S348 was appraised as part of that
same corpus-wide pass** (it was already an extracted study, just not yet an `effect_sizes.csv`
row at the time) — added to `effect_sizes.csv` later the same day by a separate re-mining pass
(`effect_sizes_remining_2026-09-28.md`), but its risk-of-bias rating predates and is unaffected
by that addition.

## The ownership/regulatory-structure-and-price cluster (S526, S539, S749, and related S471, S1038)

This is the sub-grouping Phase 11 §5.1 identified as "the single strongest candidate
sub-cluster in the entire corpus," and the one this project subsequently wrote a dedicated
methods note about (`phase11_pooling_feasibility_S526_S539_S749.md`). Presented here as its own
group because it is genuinely different from the rest of Family C in kind, not just degree:

| Study | Exposure | Outcome metric | Effect |
|---|---|---|---|
| S526 | Private vs. government ownership | Unit-price ratio (progressivity) | −0.167, more regressive (p<0.001) |
| S539 | Private vs. public/cooperative ownership | Annual bill (USD); % of lowest-quintile income | +$144.04/yr (p<0.01); +1.55 pp (p<0.01) |
| S749 | Private vs. public/mixed-capital ownership | Tariff level (R$/m³) | +0.3456 R$/m³ (significant) |
| S471 | Mayor-led vs. manager/council-led government form | Monthly cost (6,000 gal) | −$1.58 (p<0.05, attenuates to non-significant with full covariates) |
| S1038 | State vs. local economic regulation | Monopoly welfare loss (% of bill) | −4.6 pp under state regulation (p<0.01) |

**All three ownership-type studies (S526, S539, S749) agree in substance**: private ownership is
associated with a worse affordability/progressivity outcome for the household, across three
different countries (US ×2, Brazil) and three non-convertible metrics.
`phase11_pooling_feasibility_S526_S539_S749.md` concludes this cannot be pooled — the
dimensionless UPR (S526) measures rate-*structure* progressivity, a different construct from
the price-*level* measures in S539/S749, and converting S539↔S749 would require assumed
household consumption volumes, a currency-conversion reference year, and an inflation
adjustment that neither source paper's own extracted data supports. S471 and S1038 share the
broader "governance/regulatory-structure → affordability" theme but test a different exposure
(government form; regulatory jurisdiction, not ownership type) and are presented alongside, not
folded into, the three-study ownership cluster.

**Vote count for this 5-study grouping**: 3 of 5 (S539, S749, and — read as "lower cost is the
favorable direction" — S471) point toward the state/public/regulated-structure comparator being
more favorable for affordability; S526 agrees in substance (private → more regressive) even
though its raw sign is "negative"; S1038 agrees as well (state regulation → lower excess
pricing). **All 5 of 5 studies in this grouping point the same substantive direction**: more
public, more regulated, or more accountable governance structures are associated with better
household affordability outcomes than less regulated/private alternatives. This is the
strongest directionally consistent finding in Family C, precisely because it is also the most
mechanistically coherent sub-group.

## The remaining 15 studies

The other 15 studies (S174, S590, S593, S606, S631, S879, S947, S1032, S1062, S1136, S1143,
S1146, S1162, S348, and S470 — S470 groups more naturally here than with the ownership/price
cluster, since it concerns eligibility-based tariff *enrollment*, not ownership structure;
S348, added later the same day by the re-mining pass, tests its own distinct
governance-quality-classification exposure with no comparable study yet in this group) each test a
distinct administrative/legal-barrier mechanism: institutional-capacity indices, historical
franchise/political-power structure, fiscal-autonomy classification, household-registration
(hukou) status, jurisdiction-splitting/proliferation, contract-enforcement RCTs, national
regulatory-quality indices, redress-seeking behavior, cost-recovery/regulatory-enforcement
policy, political proximity/capture, service-delivery-rule design, corruption incidence, and
local-government administrative category. **None shares a comparable estimand with another
study in this set.** `PROJECT_SPEC.md` §8's prediction that this family would prove "too
heterogeneous" for anything beyond individual narrative treatment holds for this remainder.

## Standardized metric used for comparison

Direction and statistical significance, as for Families A and B, with the ownership/price
cluster additionally organized around its shared *substantive theme* (governance structure →
affordability) even though its members' *metrics* remain non-convertible — a distinction this
synthesis is careful to keep explicit throughout, per `ANALYSIS_PLAN.md` §3.

## Criteria used to prioritize results

Mechanical for 19 of 20 studies, per `CODEBOOK.md` §12's one-prespecified-effect-per-study
default — each already contributes exactly one result to `effect_sizes.csv`, selected at
extraction time as the paper's clearest primary finding. **One study in this family did require
an explicit selection among competing results, recorded in its own `provenance_note`**: S471's
form-of-government coefficient was chosen over two other reported institutional/fiscal
coefficients from the same combined regression model (purchased-water dependence,
+2.86/SE 0.91/p<0.05; water utility expenditures per capita, +0.0055/SE 0.0008/p<0.01) because
it is "the clearest formal institutional/governance-structure exposure-comparator among the
variables studied" — i.e. the one that actually tests this family's mechanism, not merely the
statistically strongest or most convenient of the three. No other study in this family required
a new prioritization decision beyond the existing default.

## Grouping and ordering of studies for the synthesis

Two-tier grouping: (1) the ownership/regulatory-structure-and-affordability cluster (5 studies,
above), presented first as this family's most coherent finding; (2) the remaining 14
studies, grouped loosely by barrier type (fiscal/regulatory-capacity mechanisms; political/
administrative-structure mechanisms; identity- or registration-based exclusion mechanisms;
service-delivery-rule design) for readability, without claiming comparability across those
loose groups.

## Results

Vote count across all 20 studies, as extracted (S348 added 2026-09-28, direction negative):

| Direction | k | Studies |
|---|---|---|
| Positive | 7 | S174, S470, S539, S590, S749, S947, S1136 |
| Negative | 9 | S348, S471, S526, S606, S631, S1032, S1038, S1146, S1162 |
| Mixed | 4 | S593, S879, S1062, S1143 |
| Null | 0 | — |

Unlike Family A (60% positive) or Family B (83% positive), **Family C shows no dominant
direction across its full 20-study set** — 7 positive, 9 negative, 4 mixed, a genuinely
heterogeneous pattern that mirrors the heterogeneity of the mechanisms themselves. This is not
a synthesis failure; it is the accurate representation of what `PROJECT_SPEC.md` §8 predicted
before this review began. **The one place a real pattern emerges is the 5-study
ownership/regulatory-structure sub-grouping above, where all 5 point the same way** — that
finding should not be diluted by averaging it into the full 20-study vote count, and is
reported separately for that reason.

## Robustness of the synthesis

The full-family 7/9/4 split is not meaningfully robust to any single exclusion — it is already
close to an even three-way split, so removing or reclassifying any one or two studies could flip
which direction is nominally "most common" without changing the substantive conclusion (there is
no dominant direction). The 5-study ownership/regulatory-structure finding is more robust:
losing any single study out of the five still leaves 4/4 in the same direction. The most
influential single study in that sub-group is S526, since it is the only one testing a
dimensionless progressivity metric rather than a price level — removing it would leave a
4-study, price-level-only sub-group that is arguably even more internally consistent, at the
cost of one fewer country represented.

## Certainty in this body of evidence

**Low-to-moderate confidence**, per
`04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`'s "Overall confidence" section,
which identifies Family C's ownership/price sub-cluster (S526, S539 — both JBI "Some concern")
as this family's strongest internal candidate without changing the overall family verdict. The
15 non-ownership studies (including S348, JBI "Some concern") span ROBINS-I ("Moderate," the
large majority), JBI Cross-Sectional ("Some concern" or "Low concern"), and one RoB 2
cluster-trial study (S879, "Some concerns") —
consistent appraisal depth with Families A and B, but spread across 15 unrelated mechanisms
rather than concentrated on one question, which limits how much any single rating can say about
the family's overall causal credibility.

## Limitations of this synthesis approach itself

Family C is where a vote-counting/SWiM approach is weakest as a tool: 20 studies testing 15+
distinct mechanisms cannot be meaningfully reduced to a single directional headline, and this
synthesis's own 7/9/4 split makes that explicit rather than papering over it with a false
"barriers generally worsen access" narrative the corpus does not actually support at the
full-family level. The one place this synthesis approach adds real value is the 5-study
ownership/regulatory-structure sub-grouping, where enough mechanistic similarity exists for a
vote count to mean something — and even there, it stops at "consistent direction across 5
studies," not a claim about effect size, which only a (currently unavailable) common metric
could support.
