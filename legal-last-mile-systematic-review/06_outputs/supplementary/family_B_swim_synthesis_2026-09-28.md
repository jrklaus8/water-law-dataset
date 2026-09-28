# SWiM Synthesis — Family B (Administrative assistance and access) — 2026-09-28

## Why this family did not proceed to meta-analysis

`ANALYSIS_PLAN.md` §2's decision tree routes Family B to structured synthesis primarily on the
**"too few independent studies" branch**, not a failed comparability test — `PROJECT_SPEC.md`
§8 itself anticipated this outcome for Family B ("study count may be too small to pool — use
structured quantitative synthesis if so"). Six studies test six distinct mechanisms:
bureaucratic assistance × political coordination (S085, RCT); community WASH institutional
strengthening (S294, RCT); capital-cost contribution/meeting attendance (S1102, PSM); network
capital in funding applications (S1140, logit); NGO/CBO trust (S1144, logit); external WaSH
programme funding (S1163, multilevel logistic). Even the three studies with a genuinely shared
model family (S1140, S1144, S1163 — all logit/logistic) test different exposure constructs
(network capital, organizational trust, external funding), so **k = 6 never reaches the point
where the comparability question in §2 would even need to be asked** — see
`06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md` §4.

## Studies included in this synthesis

| Study | Country | Design | Direction (as extracted) | RoB tool / rating |
|---|---|---|---|---|
| S085 | India | Cluster-RCT (2×2 factorial) | Positive — bureaucratic assistance increases formalization, conditional on political coordination | RoB 2 (cluster) — Some concerns |
| S294 | DR Congo | Cluster-RCT | Mixed — null on health outcomes, positive on institutional-strengthening outcome | RoB 2 (cluster) — Some concerns |
| S1102 | India | Quasi-experimental (PSM) | Positive — participation + capital-cost contribution → improved access outcomes | ROBINS-I — Moderate |
| S1140 | Nepal | Quantitative regression (logit) | Positive — greater network capital → higher probability of securing collaborative programme access | JBI Cross-Sectional — Low concern |
| S1144 | Uganda | Quantitative regression (logit) | Positive — higher NGO/CBO trust → higher probability of accessing that organization's service | JBI Cross-Sectional — Low concern |
| S1163 | 14 LMICs | Cross-sectional multilevel regression | Positive — external WaSH-programme funding → higher odds of the outcome | ROBINS-I — Moderate |

Pulled from `effect_sizes.csv` and `extraction_database.csv`; not re-extracted. RoB ratings as
of the 2026-09-28 corpus-wide pass — `RISK_OF_BIAS.md` §4.

## Standardized metric used for comparison

Direction and statistical significance of effect, as reported by each study — the same
informal common ground used for Family A, and for the same reason: no shared effect-size scale
exists across an RCT risk difference (S085, S294), a PSM coefficient (S1102), and three logit
odds ratios on three different exposure constructs (S1140, S1144, S1163).

## Criteria used to prioritize results

Mechanical, not a new judgment call for this synthesis: `CODEBOOK.md` §12's one-prespecified-
effect-per-study default means each of these 6 studies already contributes exactly one result to
`effect_sizes.csv`. None of this family's 6 `provenance_note` entries document an explicit
choice among several competing reported results (unlike some Family C studies do — see that
family's synthesis) — each of these 6 papers' selected result was its own clear primary finding,
not one picked over rival candidates. No study in this family required a new prioritization
decision beyond the existing default.

## Grouping and ordering of studies for the synthesis

Two natural groups, both noted in `phase11_quantitative_feasibility_judgment.md` §4:

1. **Direct provider-side assistance mechanisms tested experimentally** (S085, S294) — both
   cluster-RCTs where the intervention *is* a form of administrative/bureaucratic assistance or
   institutional strengthening delivered to communities. These are this family's strongest
   designs by construction (randomized), and its only two studies not rated via an
   observational risk-of-bias instrument.
2. **Administrative/institutional-trust mechanisms measured via regression** (S1102, S1140,
   S1144, S1163) — observational studies where an institutional-trust, network-capital, or
   funding-relationship variable predicts a formalization or access outcome. Worth presenting
   as a group because three of the four (S1140, S1144, S1163) share a logit/logistic modeling
   choice even though their exposure constructs remain distinct — a presentation convenience,
   not a claim of comparability (`ANALYSIS_PLAN.md` §7).

## Results

Direction categories were assigned from each study's full `direction` text in `effect_sizes.csv`,
not its first word — the one case where that mattered is S294 (extracted direction is a mixed
null-on-health / positive-on-institutional-strengthening finding, coded Mixed). Sign and
valence coincide for all six studies here (every positive sign is a beneficial result for
access), unlike Families A and C.

| Direction | k | Studies |
|---|---|---|
| Positive | 5 | S085, S1102, S1140, S1144, S1163 |
| Mixed | 1 | S294 (null on its health-outcome arm, positive on its institutional-strengthening arm) |
| Negative | 0 | — |
| Null | 0 | — |

**Every one of the 6 studies in Family B reports a positive association between some form of
administrative assistance, institutional trust, or bureaucratic facilitation and improved
formal access or service outcomes, with the sole partial exception of S294's health-outcome
arm** (its institutional-strengthening arm is itself positive). This is the most directionally
consistent of the three families — but with k = 6, "consistent" and "well-established" are not
the same claim; see Robustness below. No harvest plot is produced: with only 6 studies and a
5-positive/1-mixed split, a table conveys this fully.

## Robustness of the synthesis

**This is the family where a single study could most plausibly flip the headline finding.**
Removing either RCT (S085 or S294) leaves the "consistent positive association" claim resting
entirely on 4 observational studies. Removing S294 specifically (this family's one mixed
result) would make the vote count a unanimous 5/5 positive — a leave-one-out sensitivity worth
stating explicitly rather than letting the unanimous framing stand unexamined. `PROJECT_SPEC.md`
§8's own anticipation that this family might be "too small to pool" should be read alongside
this: k = 6 is also arguably too small to draw a confident *directional* conclusion from, even
without attempting a pooled estimate.

## Certainty in this body of evidence

**Low confidence on sample-size grounds, independent of the individual studies' own
reasonably solid appraisals** — per
`04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`'s "Overall confidence" section
(corrected here: that document's Family B paragraph names "S085 and S879" as this family's
two RoB 2 cluster-trial studies, but S879 is a Family C study — S085's actual Family B RoB 2
co-study is **S294**; both were appraised in the same batch, which is the likely source of the
mix-up. Both statements below are correct for S085/S294; `2026-09-28_evidence_limitations.md`
has been corrected to match). S085 and S294 carry this project's richest appraisal forms in
the whole corpus — genuine pre-registration evidence, individual full domain-by-domain RoB 2
cluster-trial appraisal — and both land at "Some concerns," not "High risk." The four
observational studies (S1102 "Moderate," S1140/S1144 "Low concern," S1163 "Moderate") are
individually reasonably appraised as well. **The limiting factor for this family's confidence
is not appraisal quality — it is that six studies, six different mechanisms, is not enough
independent evidence to generalize from**, exactly the caveat `PROJECT_SPEC.md` §8 flagged
before any of this appraisal work began.

## Limitations of this synthesis approach itself

With k = 6, even a vote count risks looking more authoritative than the underlying evidence
supports — a 5/6 positive split reads as a strong pattern, but is statistically indistinguishable
from chance at this sample size without a formal test this synthesis deliberately does not run
(no pooled estimate exists to test). This synthesis should be read as "the small number of
studies that exist on this topic mostly point the same way," not as "administrative assistance
has been shown to improve access" — the latter claim would need either more independent studies
or a formal meta-analysis this family cannot yet support.
