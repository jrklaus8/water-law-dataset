# SWiM Synthesis — Family C (Ownership, regulation, institutional-capacity and administrative-structure mechanisms) — 2026-09-28

> **Update 2026-10-14 (k 19 to 20, S1169 added).** The PI included Olmstead (2004, *Thirsty Colonias*, Land Economics 80(1):136–150) as S1169 after a full-text read of pages 2–15. Its one access-relevant estimate (probit on whether a Texas border-county colonia household is served, N = 781; price (rate) regulation of the provider, coefficient −1.1858, SE 0.4163, p = 0.004) is now a Family C row (`effect_sizes.csv`). Counts below were recomputed on the 20 studies: Negative 9 (was 8), Positive 7 and Mixed 4 unchanged. S1169 sits in the remaining group, not in the ownership/price cluster, because its outcome is service coverage, not affordability. The 19-study version is in the git history.
>
> **Earlier update 2026-10-14 (k 20 to 19).** The PI's narrow-scope ruling excluded S348 (Andrews, Beynon & Baafi 2025, Ghanaian district governance quality and access; E03, institutional context is background only) and its `effect_sizes.csv` row was removed (archived in `11_archive/effect_sizes_removed_2026-10-13.csv`). S348 was the study added by the 2026-09-28 re-mining pass, so the family is back to the 19 studies it had before that pass. Counts below were recomputed on the 19 studies; the ownership/price cluster is unchanged. The 20-study version of 2026-09-28 is in the git history.

> **What the family label means (added 2026-10-14 under the A21 ruling 2026-10-14, open item A21).** Family C groups studies of ownership, regulation, institutional capacity and administrative structure (private versus public ownership, price regulation, government form, political proximity, registration status, corruption, administrative category). The protocol heading, 'Administrative/legal barriers and access inequality', was broader in one respect and narrower in another than what was synthesised. Families A, B and C are **thematic mechanism groupings used to organise the structured vote count (SWiM)**, not homogeneous exposure–outcome pairs. Their member studies share a broad theme, not a comparable exposure, comparator and outcome measure; that is why Phase 11 rejected pooling (`phase11_quantitative_feasibility_judgment.md`; `ANALYSIS_PLAN.md` §2). The `synthesis_family` codes in `effect_sizes.csv` and every study assignment are unchanged; only the descriptive heading changed. The pre-evidence wording of the families stays in `PROJECT_SPEC.md` §8 (see the dated note there).
> The keyword audit that prompted this is `05_analysis/effect_sizes/FAMILY_FIT_AUDIT_2026-10-04.md`.

## Why this family did not proceed to meta-analysis

`ANALYSIS_PLAN.md` §2's decision tree fails at the comparability fork, as it does for Family
A, but Family C is the family `PROJECT_SPEC.md` §8 itself flagged in advance as "conceptually
attractive but potentially too heterogeneous; treat as secondary synthesis unless evidence is
unusually consistent." That prediction holds: of the 20 studies (17 originally, plus S470 and
S471 corrected in from blank on 2026-09-28 — see
`phase11_blank_family_resolution_2026-09-28.md`; S348, added by a re-mining pass the same day, see `effect_sizes_remining_2026-09-28.md`, was removed on 2026-10-14, and S1169 was added the same day), only one genuine 3-study sub-cluster (§"The
ownership/price cluster" below) shares even a family-resemblance estimand, and even that
cluster cannot be pooled — see
`phase11_pooling_feasibility_S526_S539_S749.md`'s dedicated methods note, which concludes no
defensible common-metric transformation exists for it. The other 17 studies each test a
distinct administrative/legal-barrier mechanism in a distinct national context — see
`phase11_quantitative_feasibility_judgment.md` §5.2's list. **This is the least internally
consistent of the three families, exactly as `PROJECT_SPEC.md` anticipated before any evidence
was gathered.**

## Studies included in this synthesis

| Study | Country | Design | Direction (as extracted) | RoB tool / rating |
|---|---|---|---|---|
| S174 | Brazil | Cross-sectional regression | Positive for financial, technical and operational capacity; the plan/policy (legal-compliance) component is negative for water coverage, null for sewerage, marginally positive for waste (full text read 2026-10-04; Minas Gerais, n = 391) | JBI Cross-Sectional — Some concern |
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
| S1169 | United States | Cross-sectional probit (781 Texas colonias) | Negative — price-regulated provider → lower probability of service | JBI Cross-Sectional — Some concern |

Pulled from `effect_sizes.csv` and `extraction_database.csv`; not re-extracted. RoB ratings as
of the 2026-09-28 corpus-wide pass — `RISK_OF_BIAS.md` §4.

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
associated with a worse affordability/progressivity outcome for the household, across **two**
countries (US ×2, Brazil; an earlier draft said "three different countries") and three
non-convertible metrics. **Independence caveat (added 2026-09-28, audit):** S526 (1,183–1,189 US
utilities serving 40,000+ people) and S539 (the 500 largest US community water systems) both draw on
large US utilities, so their samples very probably overlap substantially even though they are
separate papers by different author teams with different data collections — "three independent
studies" cannot be claimed for the ownership question. This is inferred from the two samples'
extracted descriptions, not verified against the source papers' data appendices; if it holds, the
ownership finding rests on two effectively independent samples (US and Brazil), both
cross-sectional and both appraised "Some concern".
`phase11_pooling_feasibility_S526_S539_S749.md` concludes this cannot be pooled — the
dimensionless UPR (S526) measures rate-*structure* progressivity, a different construct from
the price-*level* measures in S539/S749, and converting S539↔S749 would require assumed
household consumption volumes, a currency-conversion reference year, and an inflation
adjustment that neither source paper's own extracted data supports. S471 and S1038 share the
broader "governance/regulatory-structure → affordability" theme but test a different exposure
(government form; regulatory jurisdiction, not ownership type) and are presented alongside, not
folded into, the three-study ownership cluster.

**Vote count for this 5-study grouping** (the two tables under Results below, applied to these five studies): the three ownership-type studies are all **Unfavourable** for private ownership, with opposite raw signs because their outcomes point in opposite directions (S526: -0.167 on a progressivity ratio, where higher is better; S539: +$144 a year in the bill and +1.55 percentage points of the lowest-quintile income share, where higher is worse; S749: +0.3456 R$/m3 on the tariff, where higher is worse). The other two are **Favourable** for the more public or more regulated arrangement: S471 (raw sign negative on a cost, where lower is better; the association attenuates to non-significance once fiscal, community and environmental-risk covariates are added, so its fully adjusted direction is Null) and S1038 (state regulation, -4.6 percentage points of welfare loss). **All 5 of 5 studies in this grouping point the same way**: more
public, more regulated, or more accountable governance structures are associated with better
household affordability outcomes than less regulated/private alternatives. This is the most
directionally consistent sub-group in Family C and the most mechanistically coherent, but it is
small and thin: the *core* ownership question is 3 studies in 2 countries (two probably overlapping
US samples, above); S471 and S1038 test different exposures (government form; regulatory
jurisdiction) and S471's result is not robust to full covariate adjustment; whether "mayor-led" is
the more "accountable" structure is an interpretive reading, not something the extraction records;
and all five are observational cross-sectional or panel designs rated "Some concern" or "Low
concern" on the basis of limited extracted methodological detail.

## The remaining 15 studies

The other 15 studies (S174, S590, S593, S606, S631, S879, S947, S1032, S1062, S1136, S1143,
S1146, S1162, S1169, and S470 — S470 groups more naturally here than with the ownership/price
cluster, since it concerns eligibility-based tariff *enrollment*, not ownership structure; S1169 tests
price regulation of the provider, but its outcome is the probability of being served at all, not affordability) each test a
distinct administrative/legal-barrier mechanism: institutional-capacity indices, historical
franchise/political-power structure, fiscal-autonomy classification, household-registration
(hukou) status, jurisdiction-splitting/proliferation, contract-enforcement RCTs, national
regulatory-quality indices, redress-seeking behavior, cost-recovery/regulatory-enforcement
policy, political proximity/capture, service-delivery-rule design, corruption incidence, and
local-government administrative category, and price regulation of the provider against the probability of service in unserved border-county settlements. **None shares a comparable estimand with another
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
above), presented first as this family's most coherent finding; (2) the remaining 15
studies, grouped loosely by barrier type (fiscal/regulatory-capacity mechanisms; political/
administrative-structure mechanisms; identity- or registration-based exclusion mechanisms;
service-delivery-rule design) for readability, without claiming comparability across those
loose groups.

## Results

Vote count across all 20 studies, in two tables derived from `05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv` (the AI's coding, not yet human-verified; worksheet `SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv`). **They are counts of two different things.** Table (a) counts the raw sign of each study's reported estimate. Table (b) counts the substantive direction: whether the exposure, as the estimate reports it, goes with better (Favourable) or worse (Unfavourable) household access, affordability or equity on the paper's own outcome measure, once the polarity of the outcome is taken into account (a higher tariff, bill or complaint rate is worse; a higher progressivity ratio, coverage or access rate is better). Categories were assigned from each study's full `direction` and `effect_estimate` text, not its first word (S879 and S1062 are coded Mixed because their extracted directions combine a positive and a null or negative component).

Until 2026-10-14 this document declined to offer the second count, because deciding whether an exposure such as private ownership or mayor-led government is the adverse or the beneficial side of a comparison is a normative judgment the protocol does not fix. The substantive column does not make that judgment: it never restates a Family C exposure, and says only what the paper's own estimate implies for households. Raw sign and substantive direction diverge for S471 (negative on a cost, so Favourable), S539 and S749 (positive on a bill or tariff, so Unfavourable) and S1032 and S1038 (negative on complaints or on welfare loss, so Favourable), while S526 (negative on a progressivity ratio) is Unfavourable. Read the raw split as "7 positive, 9 negative", never as "7 beneficial, 9 adverse".

### (a) Raw coefficient sign

| Direction | k | Studies |
|---|---|---|
| Positive (+) | 7 | S174, S470, S539, S590, S749, S947, S1136 |
| Negative (-) | 9 | S471, S526, S606, S631, S1032, S1038, S1146, S1162, S1169 |
| Mixed | 4 | S593, S879, S1062, S1143 |
| Null | 0 | — |

### (b) Substantive direction for household access, affordability or equity

| Direction | k | Studies |
|---|---|---|
| Favourable | 8 (40%) | S174, S470, S471, S590, S947, S1032, S1038, S1136 |
| Unfavourable | 8 (40%) | S526, S539, S606, S631, S749, S1146, S1162, S1169 |
| Mixed | 4 (20%) | S593, S879, S1062, S1143 |
| Null | 0 (0%) | — |

Notes on individual rows. **S471** is coded on its primary estimate (-1.58, organisation-only model with state fixed effects, p < 0.05): negative in sign and Favourable, since a lower bill is better. Its fully adjusted estimate (-1.03) is not significant, so its adjusted direction is Null; a sensitivity scenario recodes it (S4c). **S1038**: the `exposure_definition` of its `effect_sizes.csv` row names local-only regulation as the exposure, but the reported difference (-4.6 percentage points of welfare loss) is state-regulated minus locally regulated, and it is coded on that contrast; the row should be confirmed. **S590** and **S1136** are coded Favourable on their own outcomes (a city's decision to build waterworks; road-level public sanitation infrastructure for politically connected villages, a favouritism finding), neither of which is a household access measure (checked 2026-10-14). **S879** is Mixed because payment compliance rose by 30 percentage points (a utility-side outcome) while water access did not change; a strict household-access reading would be Null.

Unlike Family A (13 of 18 Favourable) or Family B (5 of 6 Favourable), **Family C shows no dominant direction across its full 20-study set**, by either reading: 7 positive, 9 negative and 4 mixed by raw sign, and 8 Favourable, 8 Unfavourable and 4 Mixed by substantive direction. That is a genuinely heterogeneous pattern that mirrors the heterogeneity of the mechanisms themselves. This is not a synthesis failure; it is the accurate representation of what `PROJECT_SPEC.md` §8 predicted before this review began. **The one place a real pattern emerges is the 5-study ownership/regulatory-structure sub-grouping above**, where the three ownership studies are all Unfavourable for private ownership (S526, S539, S749 despite opposite raw signs), and the two governance-structure studies (S471, S1038) are Favourable for the more public or more regulated arrangement. That finding should not be diluted by averaging it into the full 20-study vote count, and is reported separately for that reason.

## Robustness of the synthesis

The full-family splits (7 positive, 9 negative, 4 mixed by raw sign; 8 Favourable, 8 Unfavourable, 4 Mixed by substantive direction) are not meaningfully robust to any single exclusion — no category holds a
majority (the largest, raw negative, is 9 of 20), so removing or reclassifying any one or two studies could change
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
15 non-ownership studies span ROBINS-I ("Moderate," the
large majority), JBI Cross-Sectional ("Some concern" or "Low concern"), and one RoB 2
cluster-trial study (S879, "Some concerns") —
consistent appraisal depth with Families A and B, but spread across 15 unrelated mechanisms
rather than concentrated on one question, which limits how much any single rating can say about
the family's overall causal credibility.

## Limitations of this synthesis approach itself

Family C is where a vote-counting/SWiM approach is weakest as a tool: 20 studies testing 15+
distinct mechanisms cannot be meaningfully reduced to a single directional headline, and this
synthesis's own 7/9/4 raw and 8/8/4 substantive splits make that explicit rather than papering over it with a false
"barriers generally worsen access" narrative the corpus does not actually support at the
full-family level. The one place this synthesis approach adds real value is the 5-study
ownership/regulatory-structure sub-grouping, where enough mechanistic similarity exists for a
vote count to mean something — and even there, it stops at "consistent direction across 5
studies," not a claim about effect size, which only a (currently unavailable) common metric
could support.
