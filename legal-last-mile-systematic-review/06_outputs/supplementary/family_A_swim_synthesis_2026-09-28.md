# SWiM Synthesis — Family A (Legal recognition and access) — 2026-09-28

## Why this family did not proceed to meta-analysis

`ANALYSIS_PLAN.md` §2's decision tree fails at its central fork for Family A: **no two of
the 20 studies share a substantively comparable exposure–comparator–outcome estimand.**
`06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md` §3 documents this in
full — the 20 studies span at least 15 countries/jurisdictions and 14 genuinely distinct
legal/institutional exposures (slum-notification status, municipal incorporation, tribal vs.
state regulatory primacy, zoning designation, water-user-association legal membership, land
titling, ethnic-autonomous-county status, formal connection fees, participatory management,
customary governance, colonial-era governance duration, watershed-programme participation,
community-organization establishment, community design participation, growth-control
screening), each measured on its own outcome scale (adjusted % differences, ORs, hazard
ratios, DiD coefficients, PSM ATTs, minutes saved, incidence-rate ratios). `ANALYSIS_PLAN.md`
§4's own rule — "a linear-probability coefficient should **not** simply be treated as an odds
ratio" — rules out silently converting these onto one scale to force a pool. This is a
methodological finding about the state of the evidence base, not a gap in this review's
execution: **k = 20 is a real number of studies on this general topic; the number that share
a genuinely poolable estimand is zero.**

## Studies included in this synthesis

| Study | Country | Design | Direction (as extracted) | RoB tool / rating |
|---|---|---|---|---|
| S037 | United States | Cross-sectional comparative | Null — no significant difference | ROBINS-I — Moderate |
| S057 | Cambodia | Cluster-RCT | Positive — subsidy eligibility increases purchase | RoB 2 (cluster) — Some concerns |
| S084 | India | Cross-sectional survey | Negative — unrecognized status → lower access | JBI Cross-Sectional — Some concern |
| S104 | Zambia | Quantitative cross-sectional | Positive — home ownership → higher odds of interruption (counter-intuitive; see note) | JBI — Low concern |
| S142 | United States | Quantitative cross-sectional (large admin. data) | Negative — unincorporated status → reduced access | ROBINS-I — Moderate |
| S358 | United States | Cross-sectional + geospatial | Protective — Tribal oversight → lower odds of groundwater decline | JBI Cross-Sectional — Some concern |
| S398 | Brazil | Quasi-experimental panel DiD | Positive — ZEIS zoning designation → increased access | ROBINS-I — Moderate |
| S404 | Kenya | Quasi-experimental cross-sectional | Positive — WRUA membership reduces water poverty | ROBINS-I — Moderate |
| S589 | Ecuador | Multilateral policy review w/ embedded quantitative subsidy analysis | Negative — lack of formal connection → lower consumption, higher informal cost | Legal Institutional Evidence Appraisal Framework |
| S765 | Peru | Quasi-experimental phased-rollout DiD | Positive — land titling → significant gain | ROBINS-I — Moderate |
| S780 | China | County-level quantitative regression | Null — no significant effect | JBI Cross-Sectional — Low concern |
| S882 | Philippines | Mixed-methods survey + regression | Positive — own connection → all four water-security outcomes | MMAT |
| S920 | Brazil | DiD + kernel PSM (national admin. data) | Positive — participatory management → higher piped-access rates | ROBINS-I — Moderate |
| S930 | Mexico | Quasi-experimental PSM-DiD | Positive — usos y costumbres → greater sewerage-access gains | ROBINS-I — Moderate |
| S969 | 43 African countries | Cross-national quantitative regression | Positive — longer colonial-era governance → greater contemporary access | JBI Cross-Sectional — Some concern |
| S1020 | India | Quasi-experimental PSM (treatment/control) | Negative — watershed-development intervention → worsened outcome | ROBINS-I — Moderate |
| S1042 | Ukraine | Quantitative survey + regression | Positive — CBO establishment → improved system quality | ROBINS-I — Moderate |
| S1057 | Sri Lanka; India | Quantitative econometric (3 sites) | Positive — design participation → greater household outcome | JBI Cross-Sectional — Some concern |
| S1121 | United States | Panel regression (statewide survey) | Negative — water-adequacy screening → reduced connection permitting | ROBINS-I — Moderate |
| S1122 | Burkina Faso | Event-history regression | Negative — non-zoned/informal status → sharply reduced hazard of gaining access | ROBINS-I — Moderate |

Pulled from `effect_sizes.csv` and `03_extraction/extracted_data/extraction_database.csv`;
not re-extracted. RoB ratings as of the corpus-wide 2026-09-28 risk-of-bias pass — see
`RISK_OF_BIAS.md` §4 and `04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`.

## Standardized metric used for comparison

No common quantitative metric is used, deliberately — see "Why this family did not proceed to
meta-analysis" above. The comparison metric here is **direction and statistical significance
of effect, as reported by each study's own model**, the informal common ground SWiM permits
when a genuine common statistic is not defensible (`ANALYSIS_PLAN.md` §3's critical pooling
rule: do not manufacture comparability just because this is a narrative synthesis rather than
a meta-analysis). No attempt is made to convert, say, S765's DiD coefficient and S084's
adjusted odds ratio onto one effect-size scale.

## Criteria used to prioritize results

Mechanical, not a new judgment call for this synthesis: `CODEBOOK.md` §12's one-prespecified-
effect-per-study default means each of these 20 studies already contributes exactly one result
to `effect_sizes.csv`, selected at extraction time as the paper's own primary or most directly
mechanism-isolating estimate — see each row's own `provenance_note` for the study-specific
reason where one is recorded (several Family C studies document an explicit choice among
multiple reported results in their `provenance_note`; none of this family's 20 provenance notes
happen to document that same kind of explicit multi-result selection, which is itself
informative — it suggests these 20 papers more often reported a single clear headline
legal-recognition estimate rather than several competing candidates). No study in this family
required a new prioritization decision beyond the existing one-effect-per-study default.

## Grouping and ordering of studies for the synthesis

Grouped by the **type of legal/institutional mechanism** tested, following
`phase11_quantitative_feasibility_judgment.md` §3's own identification of the closest
conceptual pairs, extended to cover all 20 studies:

1. **Settlement/tenure/jurisdictional recognition status** (S084, S142, S1121, S1122) — whether
   a household's settlement, jurisdiction, or connection-eligibility status is formally
   recognized.
2. **Land and resource-rights formalization** (S765, S1042) — individual or collective legal
   title/registration as the exposure.
3. **Governance-model and participatory-management arrangement choice** (S404, S920, S930,
   S1057) — which institutional model manages the resource, including customary governance.
4. **Colonial-era and long-run institutional legacy** (S969, S780) — historical
   institutional-origin variables.
5. **Regulatory eligibility and formal-connection mechanisms** (S057, S398, S589) — a
   household's or applicant's formal eligibility/connection status.
6. **Water-rights and production-side regulatory exposure** (S037, S358) — legal authority over
   water allocation rather than household-facing service law.
7. **Household-level resource/ownership status and programme participation** (S104, S882,
   S1020) — a household's own asset or participation status, closest to an individual-level
   (rather than jurisdiction-level) legal/institutional exposure.

This is a presentation grouping, not a pooling decision — `ANALYSIS_PLAN.md` §7's subgroup
framing.

## Results

Vote count by **sign of the association as extracted** (see table above for per-study detail).
The Positive/Negative column headers below name the *usual* reading of each sign, but the
categories were assigned from each study's full `direction` text in `effect_sizes.csv`, not its
first word, and **sign and valence diverge for three studies** — see the concordance recount that
follows the table. Judgment calls in the coding: S358's extracted direction is "negative/protective"
(a *negative* coefficient on groundwater *decline*, i.e. beneficial) and was placed under Positive;
S404's is free text ("WRUA membership reduces water poverty") and was placed under Positive.

| Direction | k | Studies |
|---|---|---|
| Positive sign (usually: recognition/formalization associated with better access; S104 is the exception) | 12 | S057, S104, S358, S398, S404, S765, S882, S920, S930, S969, S1042, S1057 |
| Negative sign (usually: unrecognized/informal status associated with worse access; S1020 and S1121 are exceptions) | 6 | S084, S142, S589, S1020, S1121, S1122 |
| Null | 2 | S037, S780 |
| Mixed | 0 | — |

**By sign as extracted, 12 of 20 (60%) are Positive, 6 of 20 (30%) Negative, and 2 (10%) Null.**
For most studies the Positive sign means legal/institutional recognition associated with better
access, and the Negative sign means unrecognized/informal status associated with worse access —
directionally the same underlying claim stated from the opposite reference category — but that
mapping does not hold for three studies, so the sign counts should not be read as concordance
counts.

**Concordance recount (corrected 2026-09-28 by the repository audit).** An earlier draft of this
paragraph added the Positive and Negative rows together ("18 of 20, 90%") and called that the
share of studies finding recognition associated with better access. That was wrong: the sign of
the extracted coefficient is not the same as "recognition helps access", and three of those 18
studies run the other way. **S104** (home ownership associated with *higher* odds of water-supply
interruption) has a Positive sign but an adverse-for-access result; **S1020** (a
watershed-development intervention associated with *worsened*, i.e. longer, domestic water
collection time) and **S1121** (a water-adequacy screening policy associated with *reduced*
residential connection permitting) have Negative signs and are adverse results for exposures that
are not "unrecognized status" at all. Recounted by substance:

| Substantive reading | k | Studies |
|---|---|---|
| Consistent with "recognition/eligibility improves access" (11 positive-sign studies, plus the 4 negative-sign studies where unrecognized/informal status is the exposure) | 15 (75%) | S057, S358, S398, S404, S765, S882, S920, S930, S969, S1042, S1057; S084, S142, S589, S1122 |
| Counter-pattern (exposure associated with *worse* access) | 3 (15%) | S104, S1020, S1121 |
| Null | 2 (10%) | S037, S780 |

So the honest summary is that **15 of 20 studies (75%) are consistent with legal/institutional
recognition of a settlement, tenure claim, or governance arrangement being associated with better
water/sanitation access**, across 15 countries and 7 distinct mechanism types, and three
legitimate, adjusted findings — S104, S1020, S1121, rated "Low"/"Moderate" concern — run against
it and are not outliers to be explained away. This substantive coding is itself a judgment call
(S1020 and S1121 are arguably outside a strict "recognition" framing altogether); it is disclosed,
not hidden, and the sign-based vote table above is kept unchanged so a reader can recompute
either version.

**Eligibility caveat on S589.** S589's `effect_sizes.csv` row records a *descriptive, unadjusted*
group comparison (connected vs. unconnected household consumption and cost share), not a
regression estimate, and `evidence_map.csv` does not flag S589
`quantitative_synthesis_eligible`. It is the only one of the 62 `effect_sizes.csv` rows in that
position and is left in place pending the researcher's decision (`CHANGELOG.md`, 2026-09-28 audit
entry); see the robustness section for the effect on the counts above.

A harvest-plot-style visual summary is not produced here — with only 20 studies split across 7
thematic groups and a simple 4-category direction code, the table above already conveys the
same information a harvest plot would, without adding a chart for its own sake.

## Robustness of the synthesis

**Corrected 2026-09-28 (audit).** An earlier draft here said the "90% 'recognition helps access'
figure" was sensitive to how S358 and S404 are coded and quoted a drop to 10/18 (56%). Both
numbers mixed two different measures (the discarded sign-sum "90%" and the positive-sign-only
share) and overstated the sensitivity. On the corrected concordance count (15 of 20, 75%): S358
and S404 both report a "protective"/"reduces poverty" framing that required judgment to place as
concordant; if both were instead coded ambiguous and dropped, concordance would be 13 of 18 (72%).
If S589 is also dropped as an unadjusted descriptive comparison, it would be 12 of 17 (71%). The
concordant share therefore stays between 71% and 75% across all three coding/eligibility
decisions — the family-level pattern is *not* fragile to them; it is thin for the different
reason that no more than 15 studies carry it, as the certainty section below says. The two null results (S037, S780) both test institutional exposures
that are one step removed from the household (state/tribal water-rights authority; county-level
administrative allocation) rather than a household-facing recognition status directly, which
may explain why they diverge from the pattern — a hypothesis this synthesis notes but does not
test, since testing it would require exactly the kind of forced comparability this document has
argued against throughout.

## Certainty in this body of evidence

**Low-to-moderate confidence**, per `04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`'s
"Overall confidence" section: of the ROBINS-I-rated studies underlying much of this family (11
of the 20 studies above), the corpus-wide pattern is 54 of 63 total ROBINS-I ratings landing at
"Moderate" confounding risk and 9 at "Serious" — meaning even this family's strongest-designed
quasi-experimental studies (S398, S404, S765, S920, S930, S1020, S1042, S1121, S1122, S142,
S037) carry real, undocumented confounding risk by this project's own conservative reading. The
JBI Cross-Sectional-rated studies (S084, S104, S358, S780, S969, S1057), the MMAT-rated S882, the
Legal Framework-appraised S589, and the RoB 2 cluster-trial study (S057, "Some concerns") add further heterogeneity in appraisal depth rather than
resolving it. **This review can document that legal/institutional recognition and improved
access co-occur in most of this family's studies (15 of 20 on the corrected concordance count); it cannot currently certify that this
association is causal in the majority of these 20 individual cases** — see
`RISK_OF_BIAS.md` §3 for the full corpus-wide account.

## Limitations of this synthesis approach itself

A vote count by direction is the bluntest tool SWiM offers: it discards effect magnitude,
statistical power, and sample size entirely, and treats a large, well-powered study (e.g. S142's
large administrative dataset) the same as a small one in the tally. It also cannot detect or
correct for publication bias, since no formal small-study-effects test is possible without a
common effect-size scale (`08_code/R/03_publication_bias.R`'s templates require exactly the
pooled data this family does not have). The 60/30/10 split reported above should be read as "a
directionally consistent pattern across a heterogeneous evidence base," not as an estimate of a
true effect size or its precision — a genuinely different and weaker claim than what a
meta-analysis, had one been possible, would support.
