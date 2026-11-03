# SWiM Synthesis — Family B (Assistance, participation, trust and external-support mechanisms) — 2026-09-28

> **Update 2026-10-14 (k 5 to 3, after the author's A28 rulings).** Under open item A28 the author ruled, from the verbatim PDF passages, that S1144 (Tukahirwa 2011: the exposure is sociological social-proximity trust in neighbours and NGOs, not a legal or administrative rule; E03) and S1163 (Cronk et al. 2021: the exposure is whether a school had any WASH programme sponsored by an external organisation, that is donor or NGO sponsorship; E03) fall outside the review, and kept S1102 (Prokopy 2009: a mandatory project rule requires capital-cost contributions in cash, labour or materials and attendance at project meetings; n = 1,523 households in 45 villages) and the DRC trial of Quattrochi et al. The full text on file for that trial is the 2021 BMJ Global Health report, catalogued as S366, so the Family B effect row moved from S294 (the 2025 companion report, which stays as the linked report with no effect row) to S366 and is anchored to its verified improved-water-source estimate (+33 percentage points, 95% CI 22 to 45; 1,312 households in 121 clusters). Their rows are archived in `11_archive/`. The family now has 3 studies: S085, S366 and S1102. The earlier update follows.
>
> **Update 2026-10-14 (k 6 to 5, after the author's A29 ruling).** S1140 left Family B for the reasoned non-fits on the author's A29 ruling (its outcome, a village community's success in securing programme funding, is not a household water or sanitation access outcome, so the primary count follows criterion 4; the author had kept it under A26, and the sensitivity scenario that dropped it, S4b, is retired). The family now has 5 studies. S294, S1102, S1144 and S1163 were flagged on the AI's narrow-scope and outcome check (programme delivery, participation, an attitude measure, and for S294 health outcomes) and await a ruling (open item A28), so they are not counted as confirmed; S085 was confirmed earlier (inclusion only).
>
> **What the family label means (added 2026-10-14 under the A21 ruling 2026-10-14, open item A21).** Family B groups studies of assistance, participation, trust and external support (bureaucratic assistance with political coordination, community institutional strengthening, capital-cost contribution, network capital, NGO/CBO trust, external programme funding). Only S085 tests bureaucratic assistance in the protocol's sense; the protocol heading, 'Administrative assistance and access', was narrower than what was synthesised. Families A, B and C are **thematic mechanism groupings used to organise the structured vote count (SWiM)**, not homogeneous exposure–outcome pairs. Their member studies share a broad theme, not a comparable exposure, comparator and outcome measure; that is why Phase 11 rejected pooling (`phase11_quantitative_feasibility_judgment.md`; `ANALYSIS_PLAN.md` §2). The `synthesis_family` codes in `effect_sizes.csv` and every study assignment are unchanged; only the descriptive heading changed. The pre-evidence wording of the families stays in `PROJECT_SPEC.md` §8 (see the dated note there).
> The keyword audit that prompted this is `05_analysis/effect_sizes/FAMILY_FIT_AUDIT_2026-10-04.md`.

## Why this family did not proceed to meta-analysis

`ANALYSIS_PLAN.md` §2's decision tree routes Family B to structured synthesis primarily on the
**"too few independent studies" branch**, not a failed comparability test — `PROJECT_SPEC.md`
§8 itself anticipated this outcome for Family B ("study count may be too small to pool — use
structured quantitative synthesis if so"). Three studies test three distinct mechanisms: bureaucratic assistance × political coordination (S085, RCT); a community-driven WASH programme working through village WASH committees (S366, RCT; the 2021 report of the DRC trial whose 2025 companion report is S294); capital-cost contribution/meeting attendance (S1102, PSM). The designs and outcome constructs differ (formal land and connection status, an improved primary water source, a water-improvements index), so **k = 3 never reaches the point where the comparability question in §2 would even need to be asked** — see
`06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md` §4.

## Studies included in this synthesis

| Study | Country | Design | Direction (as extracted) | RoB tool / rating |
|---|---|---|---|---|
| S085 | India | Cluster-RCT (2×2 factorial) | Positive — bureaucratic assistance increases formalization, conditional on political coordination | RoB 2 (cluster) — Some concerns |
| S366 | DR Congo | Cluster-RCT | Positive — a community-driven WASH programme raises the share of households with an improved primary water source (+33 pp) | RoB 2 (cluster) — Some concerns |
| S1102 | India | Quasi-experimental (PSM) | Positive — participation + capital-cost contribution → improved access outcomes | ROBINS-I — Moderate |

S1140 (Shrestha 2013, Nepal; network capital and success in securing programme funding) was in this table until the A29 ruling of 2026-10-14 and is now a reasoned non-fit (`effect_sizes.csv`).

The DRC trial has two published reports in the corpus (`linked_reports_2026-09-28.csv`, LR01): S366 (Quattrochi et al. 2021, *BMJ Global Health*; infrastructure, access, behaviour and governance outcomes) and S294 (the 2025 companion report; health, child-growth and institutions-index outcomes). The full text on file is the 2021 report, so under the author's A28 ruling the Family B row sits on S366, anchored to its verified improved-water-source estimate (Table 2: 83% against 43%, adjusted difference +33 pp, 95% CI 22 to 45). S294 is kept as the linked report with no `effect_sizes.csv` row, because its numbers (diarrhoea and child growth null; +0.40 on a community WASH-institutions index) could not be checked against a full text; its old row is archived in `11_archive/effect_sizes_removed_2026-10-13.csv`. The two reports are one trial and count as one study here.

Pulled from `effect_sizes.csv` and `extraction_database.csv`; not re-extracted. RoB ratings as
of the 2026-09-28 corpus-wide pass — `RISK_OF_BIAS.md` §4.

## Standardized metric used for comparison

Direction and statistical significance of effect, as reported by each study — the same
informal common ground used for Family A, and for the same reason: no shared effect-size scale
exists across an RCT interaction coefficient (S085), an RCT adjusted difference in proportions (S366) and a PSM mean difference (S1102).

## Criteria used to prioritize results

Mechanical, not a new judgment call for this synthesis: `CODEBOOK.md` §12's one-prespecified-
effect-per-study default means each of these 3 studies already contributes exactly one result to `effect_sizes.csv`. Only S366's `provenance_note` records an explicit choice among several reported results (the trial's prespecified primary access outcome, the improved water source, was entered; its sanitation, water-collection-time and quantity results are not), and the choice follows the paper's own primary outcome; S085 and S1102 each reported one clear headline result. No study in this family required a new prioritization
decision beyond the existing default.

## Grouping and ordering of studies for the synthesis

Two natural groups, both noted in `phase11_quantitative_feasibility_judgment.md` §4:

1. **Direct provider-side assistance mechanisms tested experimentally** (S085, S366) — both cluster-RCTs where the intervention *is* a form of administrative/bureaucratic assistance or community institutional strengthening delivered to communities. These are this family's strongest designs by construction (randomized), and its only two studies not rated via an observational risk-of-bias instrument.
2. **A participation rule measured via matched comparison** (S1102) — an observational study where a mandatory project rule (capital-cost contribution) and meeting attendance predict a water-improvements index, the one study here that tests a rule rather than a delivered intervention (`ANALYSIS_PLAN.md` §7).

## Results

Two tables follow, derived from `05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv` (the AI's coding; for 0 of the 3 studies has the author confirmed the direction coding: S1102 and S366 were ruled in under A28 and S085 was confirmed earlier, all for inclusion only, with the direction coding not yet checked; worksheet `SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv`): the raw sign of each reported estimate, and its substantive direction for household access, formal access or service (Favourable, Unfavourable, Null or Mixed). The two readings coincide for all three studies here: every positive coefficient is a beneficial result, unlike Families A and C. The one case where the extracted `direction` text mattered was S294 (null on its health arm, positive on its institutional-strengthening arm, coded Mixed in both tables); the A28 ruling replaced it with the S366 row, which is positive. Until 2026-10-14 only one table, headed "Direction", was shown; its counts are unchanged.

### (a) Raw coefficient sign

| Direction | k | Studies |
|---|---|---|
| Positive (+) | 3 | S085, S366, S1102 |
| Mixed | 0 | — |
| Negative (-) | 0 | — |
| Null | 0 | — |

### (b) Substantive direction for household access

| Direction | k | Studies |
|---|---|---|
| Favourable | 3 (100%) | S085, S366, S1102 |
| Mixed | 0 (0%) | — |
| Unfavourable | 0 (0%) | — |
| Null | 0 (0%) | — |

S1140 is no longer in this table: its outcome is success in securing programme funding (an application outcome), not a household access measure, so the author's A29 ruling moved it to the reasoned non-fits. Before that ruling the family had 6 studies (5 Favourable, 1 Mixed on both readings) and the sensitivity scenario S4b dropped S1140; the primary count now follows that scenario. The A28 rulings then removed S1144 and S1163 (E03) and replaced S294 with S366, which left 3 studies, all Favourable on both readings (the 5-study version had 4 Favourable and 1 Mixed).

**Every one of the 3 studies in Family B reports a positive association between some form of administrative assistance, a participation rule, or community institutional strengthening and improved formal access or service outcomes.** This is the most directionally consistent of the three families — but with k = 3, "consistent" and "well-established" are not the same claim; see Robustness below. No harvest plot is produced: with only 3 studies and a 3-positive split, a table conveys this fully.

## Robustness of the synthesis

**This is the family where a single study could most plausibly flip the headline finding.**
Removing either RCT (S085 or S366) leaves the "consistent positive association" claim resting on two studies, one of them observational. The vote count is unanimous (3 of 3 Favourable), so no leave-one-out can change its direction, but any single removal takes away half or a third of the evidence. The unanimity also partly reflects the narrower scope after the author's A28 rulings: the 5-study version had one Mixed study (S294's health-and-institutions row, since replaced by S366's access estimate) and two studies of NGO trust and external programme funding that the author excluded for scope. `PROJECT_SPEC.md` §8's own anticipation that this family might be "too small to pool" should be read alongside this: k = 3 is also too small to draw a confident *directional* conclusion from, even without attempting a pooled estimate.

## Certainty in this body of evidence

**Low confidence on sample-size grounds, independent of the individual studies' own
reasonably solid appraisals** — per
`04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`'s "Overall confidence" section
(corrected here: that document's Family B paragraph names "S085 and S879" as this family's
two RoB 2 cluster-trial studies, but S879 is a Family C study — S085's actual Family B RoB 2 co-study is **S366** (the report of the DRC trial that carries the effect row; its companion report is S294); both were appraised in the same batch, which is the likely source of the
mix-up. Both statements below are correct for S085/S366; `2026-09-28_evidence_limitations.md`
has been corrected to match). S085 and S366 carry this project's richest appraisal forms in
the whole corpus — genuine pre-registration evidence, individual full domain-by-domain RoB 2
cluster-trial appraisal — and both land at "Some concerns," not "High risk." The one observational study (S1102, "Moderate") is individually reasonably appraised as well. **The limiting factor for this family's confidence
is not appraisal quality — it is that three studies, three different mechanisms, is not enough independent evidence to generalize from**, exactly the caveat `PROJECT_SPEC.md` §8 flagged
before any of this appraisal work began.

## Limitations of this synthesis approach itself

With k = 3, even a vote count risks looking more authoritative than the underlying evidence supports — a 3/3 positive split reads as a strong pattern, but is statistically indistinguishable
from chance at this sample size without a formal test this synthesis deliberately does not run
(no pooled estimate exists to test). This synthesis should be read as "the small number of
studies that exist on this topic mostly point the same way," not as "administrative assistance
has been shown to improve access" — the latter claim would need either more independent studies
or a formal meta-analysis this family cannot yet support.
