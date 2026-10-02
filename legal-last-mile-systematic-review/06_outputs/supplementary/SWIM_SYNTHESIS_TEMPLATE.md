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
checklist items verbatim, and still doesn't — but its structure is now
cross-checked, not just "well-known general approach."** `SOURCES.md` §7
cites the guideline (Campbell et al. 2020, BMJ); as of 2026-09-28, a
`WebSearch` (not `WebFetch` — every publisher/repository/guideline-registry
domain tested, including doi.org, the EQUATOR Network, and the guideline's
own official site, returned `EGRESS_BLOCKED`; only search-result snippets
were reachable) confirmed SWiM's real structure is a **9-item checklist**:
(1) grouping studies for synthesis, (2) standardised metric and
transformation methods, (3) synthesis methods, (4) criteria used to
prioritise results for summary and synthesis, (5) investigation of
heterogeneity in reported effects, (6) certainty of evidence, (7) data
presentation methods, (8) reporting results, (9) limitations of the
synthesis. This template's existing sections map onto 8 of the 9 (below);
**item 4 — criteria for prioritizing results — was genuinely missing until
this update**, added as its own section rather than left implicit. Full
item *wording* (as opposed to the item topics themselves) remains
unconfirmed, since no full-text or PDF fetch succeeded — **check the
actual guideline directly before finalizing any manuscript section**, per
the original caveat.

| SWiM item (confirmed 2026-09-28) | This template's section |
|---|---|
| 1. Grouping studies for synthesis | "Grouping and ordering of studies for the synthesis" |
| 2. Standardised metric / transformation | "Standardized metric used for comparison" |
| 3. Synthesis methods | "Standardized metric" + "Results" together (no single dedicated section — a real, minor structural gap; consider adding one if a future revision has room) |
| 4. Criteria for prioritizing results | **"Criteria used to prioritize results" — new, see below** |
| 5. Heterogeneity investigation | "Robustness of the synthesis" (adapted as a leave-one-out-style analog, not identical framing) |
| 6. Certainty of evidence | "Certainty in this body of evidence" |
| 7. Data presentation | "Results" (table/harvest plot) |
| 8. Reporting results | "Results" |
| 9. Limitations of the synthesis | "Limitations of this synthesis approach itself" |

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

## Criteria used to prioritize results
[SWiM item 4, added 2026-09-28. Not "which studies were included" (that's
Phase 6 screening) but "given that each study may report multiple possible
results, which one was selected to represent it here, and why." For this
project, the answer is usually mechanical, not a new judgment call for
this section to invent: `CODEBOOK.md` §12's one-prespecified-effect-per-
study default means each study's `effect_sizes.csv` row already reports
the single result its own `provenance_note` designates as primary
(typically because it's the most direct legal/institutional mechanism
estimate, or explicitly labeled the paper's own main result) -- cite that
provenance_note's stated reason here rather than re-deriving it. Only
write something new in this section if a study in this specific family
was a genuine exception to the mechanical default.]

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
