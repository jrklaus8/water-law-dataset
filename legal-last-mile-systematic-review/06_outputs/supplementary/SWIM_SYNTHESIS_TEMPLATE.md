# Structured Synthesis Without Meta-Analysis (SWiM) — Template (Phase 13)

For every candidate synthesis family (`PROJECT_SPEC.md` §8) that
`ANALYSIS_PLAN.md` §2's decision tree routes to "structured quantitative
synthesis" rather than meta-analysis — either because comparability
fails, there aren't enough independent studies, or substantive
heterogeneity is unacceptable. This is not a fallback for a failed
meta-analysis; PROTOCOL.md and `README.md`'s governing rule are explicit
that systematic review does not require meta-analysis, and a
well-reported structured synthesis is a first-class output here, not a
consolation prize.

**This template does not reproduce SWiM's own reporting-guideline
checklist items verbatim** — `SOURCES.md` §7 cites the guideline
(Campbell et al. 2020, BMJ) but this project has not independently
re-verified its exact item wording against the publisher (the same
access-blocked situation as the risk-of-bias tools in `SOURCES.md`
§9–13). **Check the actual SWiM reporting guideline directly before
finalizing any manuscript section based on this template** — what
follows is a structural starting point organized around SWiM's
well-known general approach (grouping studies, a standardized metric,
tabulation, vote-counting or a harvest plot, and an explicit certainty
judgment), not a certified reproduction of its checklist.

Copy this template once per family that lands here; save as
`06_outputs/supplementary/<family>_swim_synthesis.md`.

```
# SWiM Synthesis — Family [A/B/C/...] — [date]

## Why this family did not proceed to meta-analysis
[Cite the specific ANALYSIS_PLAN.md S2 decision-tree branch that routed
here -- e.g. "insufficient independent studies (k=4)" or "substantive
heterogeneity in institutional context judged unacceptable despite
statistical poolability." Be as specific as the tree itself is -- this
is a methodological finding, not an apology for missing data.]

## Studies included in this synthesis
[Table: study_id, citation, country, study_design_class, outcome
measured, direction of effect (positive/negative/null/mixed), and
whether the effect estimate is statistically significant where
reported. Pull from extraction_database.csv and evidence_map.csv --
do not re-extract.]

## Standardized metric used for comparison
[SWiM calls for reporting studies on a common, if informal, metric even
without pooling -- e.g. direction and statistical significance of effect,
or a common descriptive statistic where genuinely comparable across
studies. State explicitly what that metric is here and why it's
comparable enough for this purpose even though a pooled estimate isn't
defensible (ANALYSIS_PLAN.md S3's critical pooling rule still applies:
do not manufacture comparability just because this is now a narrative
synthesis rather than a formal meta-analysis).]

## Grouping and ordering of studies for the synthesis
[How studies are grouped for presentation -- e.g. by jurisdiction, by
mechanism family, by direction of effect. State the rationale; SWiM
requires this be principled, not just alphabetical or by publication
date.]

## Results
[Vote-counting table or harvest plot: how many studies found a positive/
negative/null effect on the outcome, broken out by the grouping above.
A picture (harvest plot) is often clearer here than prose -- see
ANALYSIS_PLAN.md's R tooling (08_code/R/) for how a meta-analysis
family reports results, and produce an analogous visual summary for
this family if it aids interpretation.]

## Robustness of the synthesis
[What would change this synthesis's conclusion -- e.g. if one influential
study were excluded, or if a borderline-eligible study were included
instead of excluded. This is the SWiM analog of the leave-one-out check
in 08_code/R/02_sensitivity_analysis.R for a pooled family.]

## Certainty in this body of evidence
[Reference RISK_OF_BIAS.md S3's cross-cutting evidence-limitations
narrative and 04_quality/risk_of_bias/EVIDENCE_LIMITATIONS_TEMPLATE.md --
do not present a narrative synthesis's conclusions with more confidence
than the underlying studies' quality and consistency actually support.]

## Limitations of this synthesis approach itself
[SWiM syntheses lack meta-analysis's formal handling of heterogeneity
and precision-weighting -- name that limitation plainly rather than
letting a confident-sounding narrative imply more rigor than a
vote-count or harvest plot actually provides.]
```
