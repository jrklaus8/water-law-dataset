# Analysis Plan

Governs everything downstream of extraction: whether to pool at all, how to
pool if justified, and how to test the robustness of any pooled result. The
single rule that supersedes every technique below:

> **Do not manufacture comparability.** A mathematically convertible
> statistic is not automatically a substantively comparable effect
> (`PROJECT_SPEC.md` §3).

## 1. Quantitative-synthesis feasibility questions (answer before any pooling)

1. What constitutes a study?
2. What is the unit of analysis?
3. What is the exposure or intervention?
4. What is the comparator?
5. What is the outcome?
6. Can the exposure be coded consistently?
7. Can the outcome be coded consistently?
8. Can effect sizes be extracted?
9. Can effects be converted to a meaningful common estimand?
10. Are there enough independent studies?
11. Is pooling substantively defensible?
12. Is statistical heterogeneity acceptable?
13. Is institutional heterogeneity so large that pooling becomes misleading?

## 2. Quantitative-synthesis decision tree

```
Is there an empirical study?
        v
Is exposure clearly defined?
        v
Is outcome clearly defined?
        v
Are population/context sufficiently comparable?
        v
Is comparator meaningful?
        v
Is effect estimate available or defensibly calculable?
        v
Does the estimate represent a substantively comparable estimand?
        +---- NO ---> structured quantitative synthesis (SWiM-style)
        YES
        v
Are there enough independent studies?
        +---- NO ---> structured quantitative synthesis
        YES
        v
Is substantive heterogeneity acceptable?
        +---- NO ---> separate synthesis family
        YES
        v
META-ANALYSIS
```

Apply this tree **per candidate synthesis family** (`PROJECT_SPEC.md` §8),
not once globally — Family A, B, and C may land in different branches.

## 3. Critical pooling rule

Do not pool causal intervention effects with observational associations in
the same primary model, even when they nominally concern the same broad
topic (e.g. legal recognition associated with higher access vs. bureaucratic
assistance causing higher access — different estimands, separate synthesis
families).

## 4. Effect size strategy

- **Binary outcomes:** risk ratio, odds ratio, or risk difference. Do not
  automatically convert every measure to odds ratios — choose the measure
  the underlying studies most naturally support, and note when a conversion
  was necessary (`evidence_status = CALCULATED`).
- **Continuous outcomes:** mean difference only when scales are genuinely
  identical; standardized mean difference only when the underlying
  construct is genuinely comparable across different scales — not merely
  because both are numerical.
- **Correlations:** Fisher-transformed correlations, where appropriate.
- **Regression coefficients:** keep in original metric unless a defensible
  transformation exists. A logistic coefficient can yield a log odds ratio.
  A linear-probability coefficient should **not** simply be treated as an
  odds ratio.

## 5. Meta-analytic model (contingent)

If a restricted synthesis is justified for a given family: **random
effects**, because studies are expected to represent different populations,
institutional contexts, legal systems, service systems, and
operationalizations. Random effects is a modeling choice for expected
heterogeneity among genuinely comparable studies — it is **not** a license
to pool studies that fail the comparability test in §2.

## 6. Heterogeneity

Report, where a pooled estimate is produced: I², tau², Cochran's Q, the
confidence interval, and the **prediction interval** (particularly
important — it shows how much the effect might vary across future
comparable settings, which matters given the cross-jurisdictional design).

Treat heterogeneity as both a statistical and a substantive/institutional
question (`PROJECT_SPEC.md` §"substantive heterogeneity" sources: legal
system, institutional centralization/fragmentation, service-provider model,
population, mechanism, outcome, study design). Substantive heterogeneity may
itself be a major finding, reportable even without a pooled estimate.

## 7. Subgroup analysis

Candidate groups: jurisdiction (Brazil / Netherlands / Canada-Ontario /
region), mechanism (eligibility / burden / discretion / enforcement),
context (urban / rural / formal / informal).

The protocol does **not** promise jurisdictional subgroup meta-analyses in
advance. Protocol language:

> Jurisdiction will be coded as a potential moderator. Subgroup analysis
> will be conducted only where sufficient independent studies contribute to
> each subgroup.

## 8. Meta-regression

Not a primary analysis. Candidate moderators: jurisdiction, regulatory
structure, decentralization, institutional capacity, legal remedy, study
period, study design, service type.

Minimum: **approximately 10 studies per moderator**, more when moderators
are unevenly distributed. Do not fit large models to small evidence bases.

## 9. Publication bias and small-study effects

Funnel plot, Egger-type test, Begg-type test, or selection models — only
where appropriate, with a practical threshold of **approximately 10
studies** per family for meaningful funnel-asymmetry assessment. Do not run
these automatically below that threshold, and do not interpret funnel
asymmetry as proof of publication bias — heterogeneity, small-study effects,
selective reporting, and methodological differences are equally plausible
explanations.

## 10. Sensitivity analysis

Each sensitivity analysis must answer a specific methodological question —
do not run every possible one reflexively:

- **Risk of bias:** exclude high-risk studies — does the finding depend on weaker studies?
- **Leave-one-out:** is one study driving the result?
- **Jurisdiction sensitivity:** remove one major geographic group — is the result dependent on one institutional context?
- **Study design:** compare observational-only vs. observational+quasi-experimental vs. experimental evidence separately.
- **Alternative effect measures:** only where substantively and mathematically defensible.

## 11. Dependent effect sizes

First-paper default: one prespecified effect per study and outcome family
(`CODEBOOK.md` §12). If the evidence base grows large enough to warrant it:
multilevel meta-analysis, robust variance estimation, or multivariate
meta-analysis — used only when the evidence base actually requires them, not
by default.

## 12. Reproducibility of the analysis itself

R packages, when analysis code is written: `metafor`, `meta` (primary);
`tidyverse`, `dplyr`, `readxl`, `openxlsx`, `janitor`, `ggplot2`, `robvis`
(supporting); Quarto for reporting. Do not add packages the analysis does
not actually require. See `REPRODUCIBILITY.md`.

## 13. Status

**This section was stale for a long time — the text above described a
state (no extraction, Phase 6 not producing decisions) that stopped being
true many batches ago; it is rewritten here as of 2026-09-28 rather than
left to drift further.** Full-text retrieval (Phase 6) formally closed
2026-09-28; extraction (Phase 8) holds 1,159 studies (S001–S1164, with S227, S233, S299 and S399 retired duplicates and S356 retired after exclusion);
evidence classification (Phase 10) is populated for all of them; **Phase
11 — this document's own §2 decision tree, applied at the family level —
is now complete**, in
`06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md`.
Verdict: no family (A, B, or C) clears the bar for meta-analysis; all
three route to Phase 13's structured quantitative synthesis (SWiM)
instead — see that document for the full reasoning. **Update, 2026-09-28
(later the same day): Phase 13 is now also complete.** All three SWiM
write-ups exist —
`06_outputs/supplementary/family_A_swim_synthesis_2026-09-28.md`,
`family_B_swim_synthesis_2026-09-28.md`, `family_C_swim_synthesis_2026-09-28.md`
— each with a vote-counting table by direction of effect, thematic
subgroups, a robustness check, and a certainty judgment drawn from that
week's corpus-wide risk-of-bias ratings. Separately, the 9
`effect_sizes.csv` rows Phase 11 had flagged as never evaluated against
the family definitions were resolved
(`06_outputs/supplementary/phase11_blank_family_resolution_2026-09-28.md`),
and a dedicated methods note concluded no defensible common-metric
transformation exists for the Family C utility-ownership/price
sub-cluster (S526/S539/S749) with the data currently extracted
(`06_outputs/supplementary/phase11_pooling_feasibility_S526_S539_S749.md`)
— that sub-cluster is presented as a directionally-consistent
vote-counting group in the Family C SWiM synthesis instead of a pooled
estimate. `08_code/R/` (Phases 12/14/15) still holds only templates and
**none of that code has actually been run** — per Phase 11's verdict,
Phase 12 (meta-analysis) has nothing to run against, and nothing found
during Phase 13 changed that. See `08_code/R/README.md`'s "Status"
section and `README.md`'s "How to continue" for what remains (the DOI-
variant duplicate audit and the reviewer_2 human pass, primarily — not
this document's own synthesis work, which is now done).
