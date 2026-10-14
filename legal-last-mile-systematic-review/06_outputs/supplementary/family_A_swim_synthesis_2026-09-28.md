# SWiM Synthesis — Family A (Legal status, tenure, recognition and governance-arrangement mechanisms) — 2026-09-28

> **Update 2026-10-14 (k 13, after the author's A28 rulings: S1020, S1042 and S1057 left).** Under open item A28 the author ruled, from the verbatim PDF passages, that S1020 (Hope 2007: the intervention is physical watershed engineering, with no legal or regulatory term in the paper; E03), S1042 (Kvartiuk 2016: the dependent variable is the mayors' subjective 1 to 4 valuation of municipal water access, not a household access outcome; E04) and S1057 (Isham & Kähkönen 2001: a demand-responsive community design and O&M participation study with no legal or administrative access rule tested; E03) fall outside the review, and kept S920 (Bardé 2017: the municipality transfers responsibility for water supply to the user association through a formal concession contract, so its specific mechanism is `regulatory_model_ownership` (municipal concession transfer) alongside participatory management). Their effect rows are archived in `11_archive/effect_sizes_removed_2026-10-13.csv`. Every count below was recomputed on the 13 remaining studies; the 16-study version is in the git history. The earlier updates follow.
>
> **Update 2026-10-14 (k 16, after the author's A26 rulings: S358 and S1121 left).** S358 (Williams et al. 2025, Arizona) moved to the reasoned non-fits in `effect_sizes.csv`: its outcome is groundwater decline and contamination risk at the level of 1,881 service areas, not household access. S1121 (Hanak 2008, California) was excluded under E04 and its row archived: its only dependent variable is the log of residential building permits, and the one other regression explains household water use under rate structures, a conservation outcome. Every count below was recomputed on the 16 remaining studies, and two direction tables (raw sign and substantive direction) replace the single sign table; the 18-study version is in the git history. The author also confirmed the inclusion and both direction codings of S404, S765, S780, S882, S930 and S1122 on 2026-10-14; S920, S1020, S1042 and S1057 were flagged on the narrow-scope check and await a ruling (open item A28), so they are not counted as confirmed.
>
> **Update 2026-10-14 (k 18, after S969 and S589 left).** A second change on 2026-10-14 closed open item A1: S589's `effect_sizes.csv` row (World Bank / IDB 2004, Machala, Ecuador; an unadjusted descriptive city-level comparison in a study not flagged quantitative-synthesis-eligible) was removed (archived in `11_archive/effect_sizes_removed_2026-10-13.csv`), so every count below was recomputed again on 18 studies. The study stays in the review; only its quantitative row left. The text of the first update follows.
>
> **Earlier update 2026-10-14 (k 20 to 19).** The PI's narrow-scope ruling excluded S969 (Njoh & Akiwumi 2011, colonial-era governance duration and access in 43 African countries; E03, no legal or administrative rule tested) and its `effect_sizes.csv` row was removed (archived in `11_archive/effect_sizes_removed_2026-10-13.csv`). Every count below was recomputed on the remaining 19 studies; the sign-based and concordance tables are otherwise unchanged. The 20-study version of 2026-09-28 is in the git history. Counts of countries and mechanism types were recounted from the named countries in the table, so they are lower than the earlier rounder figures.

> **What the family label means (added 2026-10-14 under the A21 ruling 2026-10-14, open item A21).** Family A groups studies whose exposure is a legal status, tenure, recognition or governance arrangement (slum notification, municipal incorporation, regulatory primacy, zoning, water-user-association membership, land titling, customary governance, participation arrangements). The protocol heading, 'Legal recognition and access', was narrower than what was synthesised. Families A, B and C are **thematic mechanism groupings used to organise the structured vote count (SWiM)**, not homogeneous exposure–outcome pairs. Their member studies share a broad theme, not a comparable exposure, comparator and outcome measure; that is why Phase 11 rejected pooling (`phase11_quantitative_feasibility_judgment.md`; `ANALYSIS_PLAN.md` §2). The `synthesis_family` codes in `effect_sizes.csv` and every study assignment are unchanged; only the descriptive heading changed. The pre-evidence wording of the families stays in `PROJECT_SPEC.md` §8 (see the dated note there).
> The keyword audit that prompted this is `05_analysis/effect_sizes/FAMILY_FIT_AUDIT_2026-10-04.md`.

## Why this family did not proceed to meta-analysis

`ANALYSIS_PLAN.md` §2's decision tree fails at its central fork for Family A: **no two of
the 13 studies share a substantively comparable exposure–comparator–outcome estimand.**
`06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md` §3 documents this in
full — the 13 studies span 11 countries and 9 genuinely distinct legal/institutional exposures (slum-notification status, municipal incorporation, zoning designation, water-user-association legal membership, land titling, ethnic-autonomous-county status, formal connection fees, municipal concession transfer to a participatory user association, customary governance), each measured on its own outcome scale (adjusted % differences, ORs, hazard
ratios, DiD coefficients, PSM ATTs, minutes saved, incidence-rate ratios). `ANALYSIS_PLAN.md`
§4's own rule — "a linear-probability coefficient should **not** simply be treated as an odds
ratio" — rules out silently converting these onto one scale to force a pool. This is a
methodological finding about the state of the evidence base, not a gap in this review's
execution: **k = 13 is a real number of studies on this general topic; the number that share
a genuinely poolable estimand is zero.**

## Studies included in this synthesis

| Study | Country | Design | Direction (as extracted) | RoB tool / rating |
|---|---|---|---|---|
| S037 | United States | Cross-sectional comparative | Null — no significant difference | ROBINS-I — Moderate |
| S057 | Cambodia | Cluster-RCT | Positive — subsidy eligibility increases purchase | RoB 2 (cluster) — Some concerns |
| S084 | India | Cross-sectional survey | Negative — unrecognized status → lower access | JBI Cross-Sectional — Some concern |
| S104 | Zambia | Quantitative cross-sectional | Positive — home ownership → higher odds of interruption (counter-intuitive; see note) | JBI — Low concern |
| S142 | United States | Quantitative cross-sectional (large admin. data) | Negative — unincorporated status → reduced access | ROBINS-I — Moderate |
| S398 | Brazil | Quasi-experimental panel DiD | Positive — ZEIS zoning designation → increased access | ROBINS-I — Moderate |
| S404 | Kenya | Quasi-experimental cross-sectional | Positive — WRUA membership reduces water poverty | ROBINS-I — Moderate |
| S765 | Peru | Quasi-experimental phased-rollout DiD | Positive — land titling → significant gain | ROBINS-I — Moderate |
| S780 | China | County-level quantitative regression | Null — no significant effect | JBI Cross-Sectional — Low concern |
| S882 | Philippines | Mixed-methods survey + regression | Positive — own connection → all four water-security outcomes | MMAT |
| S920 | Brazil | DiD + kernel PSM (national admin. data) | Positive — participatory management → higher piped-access rates | ROBINS-I — Moderate |
| S930 | Mexico | Quasi-experimental PSM-DiD | Positive — usos y costumbres → greater sewerage-access gains | ROBINS-I — Moderate |
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
effect-per-study default means each of these 13 studies already contributes exactly one result
to `effect_sizes.csv`, selected at extraction time as the paper's own primary or most directly
mechanism-isolating estimate — see each row's own `provenance_note` for the study-specific
reason where one is recorded (several Family C studies document an explicit choice among
multiple reported results in their `provenance_note`; none of this family's 13 provenance notes
happen to document that same kind of explicit multi-result selection, which is itself
informative — it suggests these 13 papers more often reported a single clear headline
legal-recognition estimate rather than several competing candidates). No study in this family
required a new prioritization decision beyond the existing one-effect-per-study default.

## Grouping and ordering of studies for the synthesis

Grouped by the **type of legal/institutional mechanism** tested, following
`phase11_quantitative_feasibility_judgment.md` §3's own identification of the closest
conceptual pairs, extended to cover all 13 studies:

1. **Settlement/tenure/jurisdictional recognition status** (S084, S142, S1122) — whether
   a household's settlement, jurisdiction, or connection-eligibility status is formally
   recognized.
2. **Land and resource-rights formalization** (S765) — individual or collective legal
   title/registration as the exposure.
3. **Governance-model and participatory-management arrangement choice** (S404, S920, S930) — which institutional model manages the resource, including customary governance and S920's municipal concession transfer to a user association (`regulatory_model_ownership`).
4. **Long-run institutional legacy** (S780) — historical
   institutional-origin variables (S969, the colonial-era governance study, left this family on 2026-10-14).
5. **Regulatory eligibility and formal-connection mechanisms** (S057, S398) — a
   household's or applicant's formal eligibility/connection status.
6. **Water-rights and production-side regulatory exposure** (S037) — legal authority over
   water allocation rather than household-facing service law (S358, Tribal oversight of groundwater, left this family on 2026-10-14).
7. **Household-level resource/ownership status** (S104, S882) — a household's own asset or connection status, closest to an individual-level
   (rather than jurisdiction-level) legal/institutional exposure.

This is a presentation grouping, not a pooling decision — `ANALYSIS_PLAN.md` §7's subgroup
framing.

## Results

Two tables follow because the raw sign of a coefficient and its meaning for households are different things (SWiM, Campbell et al. 2020). Until 2026-10-14 this section held one "sign" table whose categories were assigned from each study's full `direction` text, and that table mixed the two readings: S358 and S404 sat under Positive although both coefficients are negative, and S1020 sat under Negative although its coefficient is positive (the earlier table read 11 positive, 5 negative, 2 null, 0 mixed). Both tables below come from `05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv`, which records for each study (i) the raw sign of the reported estimate, (ii) whether a higher value of the outcome is better or worse for households, and (iii) the pole of the exposure the estimate refers to. The substantive direction is computed from those three fields and never typed. Both codings are the AI's; the author has not yet confirmed either coding for any of the 13 studies (`05_analysis/effect_sizes/SWIM_AI_SCOPE_CHECKS_2026-10-14.csv` records the AI's scope check; worksheet `SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv`; open item A30).

### (a) Raw coefficient sign

The sign of the reported estimate for the contrast it reports (a ratio above 1 is positive, below 1 negative); Null means the paper reports no significant difference.

| Direction | k | Studies |
|---|---|---|
| Positive (+) | 7 | S057, S104, S398, S765, S882, S920, S930 |
| Negative (-) | 4 | S084, S142, S404, S1122 |
| Null | 2 | S037, S780 |
| Mixed | 0 | — |

### (b) Substantive direction for household access

Favourable means that the exposure, with the recognised or formal arrangement as the exposure, goes with better access, affordability or service on the paper's own outcome measure; Unfavourable means worse; Null means no significant difference. It describes the association in each paper and is not a judgment that the exposure is desirable.

| Direction | k | Studies |
|---|---|---|
| Favourable | 10 (76.9%) | S057, S084, S142, S398, S404, S765, S882, S920, S930, S1122 |
| Unfavourable | 1 (7.7%) | S104 |
| Null | 2 (15.4%) | S037, S780 |
| Mixed | 0 (0%) | — |

### Where the two readings come apart

| Study | Reported estimate | Raw sign | Substantive | Why |
|---|---|---|---|---|
| S084 | non-notified vs notified slums: 37.3% less water per capita | negative | Favourable | the reported exposure is the deprived pole; restated to notified vs non-notified, recognition goes with more water |
| S142 | unincorporated vs incorporated: significantly reduced centralised access | negative | Favourable | the same restatement of a non-recognised status |
| S1122 | non-zoned vs zoned residence: hazard ratio 0.14 for first piped-water access | negative | Favourable | the same restatement; a lower hazard means slower access |
| S104 | home ownership: OR 1.31 for a piped-water interruption | positive | Unfavourable | an interruption is an adverse outcome, and the tenure-security hypothesis predicts fewer |
| S404 | WRUA membership: ATT -14% to -32% on a water-poverty index | negative | Favourable | water poverty is an adverse outcome |

By raw sign 7 of 13 (53.8%) are positive, 4 (30.8%) negative and 2 (15.4%) null. By substantive direction **10 of 13 (76.9%) are Favourable, 1 (7.7%) Unfavourable and 2 (15.4%) Null.** The two cannot be read as one count: adding the positive and negative rows of table (a) says nothing about whether recognition helps access. An earlier draft of this document did exactly that ("18 of 20, 90%") and was corrected on 2026-09-28 by the repository audit.

So the honest summary is that **10 of 13 studies (77%) are consistent with legal/institutional recognition of a settlement, tenure claim, or governance arrangement being associated with better water/sanitation access**, across 11 countries and the 7 mechanism groups above, and one legitimate, adjusted finding (S104, rated "Low" concern) runs against it and is not an outlier to be explained away. This coding is itself a judgment call: S404's reading depends on the polarity of its outcome (see Robustness below). It is disclosed, not hidden, and both tables are kept so a reader can recompute either version. Before the A26 rulings of 2026-10-14 the family had 18 studies (13 Favourable, 3 Unfavourable, 2 Null); S358 and S1121 left it for the reasons given in the update note at the top, which left 16 studies (12 Favourable, 2 Unfavourable, 2 Null); the author's A28 rulings then removed S1020 (Unfavourable), S1042 and S1057 (both Favourable), leaving 13.

**S589 (resolved 2026-10-14).** S589's `effect_sizes.csv` row recorded a *descriptive, unadjusted*
group comparison (connected vs. unconnected household consumption and cost share), not a
regression estimate, in a study that `evidence_map.csv` does not flag
`quantitative_synthesis_eligible`. It was the only `effect_sizes.csv` row in that position and was
left in place from the 2026-09-28 audit until the PI removed it on 2026-10-14 (open item A1). Every
count above excludes it; it was one of the concordant (negative-sign) studies.

A harvest-plot-style visual summary is not produced here — with only 13 studies split across 7
thematic groups and a simple 4-category direction code, the table above already conveys the
same information a harvest plot would, without adding a chart for its own sake.

## Robustness of the synthesis

**Corrected 2026-09-28 (audit); recomputed 2026-10-14 for the two-table coding and again after the A26 rulings.** An earlier draft here said the "90% 'recognition helps access'
figure" was sensitive to how S358 and S404 are coded and quoted a drop to 10/18 (56%). Both
numbers mixed two different measures (the discarded sign-sum "90%" and the positive-sign-only
share) and overstated the sensitivity. S358 has since left the family (A26), and on the substantive count (10 of 13 Favourable, 77%) S404 is the one remaining
judgment call: its "reduces poverty" result is Favourable only because a lower value of an adverse outcome (the water-poverty index) is read as better, which is a judgment about outcome polarity; if it were dropped,
the Favourable share would be 9 of 12 (75%). Further scenarios were added on 2026-10-14
(`05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`): keeping only the studies for which a positive sign means Favourable and a negative sign Unfavourable, that is dropping every study whose
inverted-outcome or restated-pole coding was needed (S084, S104, S142, S404 and S1122 here; S4d), leaves 6 of 8 (75%); the scenarios that recode S471 or S879 (both in Family C; S4c, S4e) leave this family unchanged at 10 of 13 (77%), as the retired scenario S4b (which dropped S1140 and S1136, in Families B and C, before the A29 ruling moved both out of the families) also did; and all the others together (S5) leave 9 of 12 (75%). (Before S589's row was removed a further
scenario, dropping it as an unadjusted descriptive comparison, was also tested.) The
Favourable share therefore stays between 75% and 77% across every scenario tried —
the family-level pattern is *not* fragile to them; it is thin for the different
reason that no more than 10 studies carry it, as the certainty section below says. The two null results (S037, S780) both test institutional exposures
that are one step removed from the household (state/tribal water-rights authority; county-level
administrative allocation) rather than a household-facing recognition status directly, which
may explain why they diverge from the pattern — a hypothesis this synthesis notes but does not
test, since testing it would require exactly the kind of forced comparability this document has
argued against throughout.

## Certainty in this body of evidence

**Low-to-moderate confidence**, per `04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`'s
"Overall confidence" section: of the ROBINS-I-rated studies underlying much of this family (8 of the 13 studies above), the corpus-wide pattern is 44 of 53 total ROBINS-I ratings landing at "Moderate" confounding risk and 9 at "Serious" — meaning even this family's strongest-designed
quasi-experimental studies (S398, S404, S765, S920, S930, S1122, S142, S037) carry real, undocumented confounding risk by this project's own conservative reading. The
JBI Cross-Sectional-rated studies (S084, S104, S780), the MMAT-rated S882, and the RoB 2 cluster-trial study (S057, "Some concerns") add further heterogeneity in appraisal depth rather than
resolving it. **This review can document that legal/institutional recognition and improved
access co-occur in most of this family's studies (10 of 13 on the corrected concordance count); it cannot currently certify that this
association is causal in the majority of these 13 individual cases** — see
`RISK_OF_BIAS.md` §3 for the full corpus-wide account.

## Limitations of this synthesis approach itself

A vote count by direction is the bluntest tool SWiM offers: it discards effect magnitude,
statistical power, and sample size entirely, and treats a large, well-powered study (e.g. S142's
large administrative dataset) the same as a small one in the tally. It also cannot detect or
correct for publication bias, since no formal small-study-effects test is possible without a
common effect-size scale (`08_code/R/03_publication_bias.R`'s templates require exactly the
pooled data this family does not have). The 7/4/2 raw split and the 10/1/2 substantive split reported above should be read as "a
directionally consistent pattern across a heterogeneous evidence base," not as an estimate of a
true effect size or its precision — a genuinely different and weaker claim than what a
meta-analysis, had one been possible, would support.
