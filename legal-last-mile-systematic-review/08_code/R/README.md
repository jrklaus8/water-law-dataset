# R Analysis Code (Phases 12, 14, 15)

`ANALYSIS_PLAN.md` §12 specifies R for the meta-analytic phases —
`metafor`/`meta` are the mature, standard tools for this, unlike the
stdlib-Python convention used for this repository's search/screening/
extraction pipeline scripts under `code/`. This is a deliberate,
already-made tooling choice, not an inconsistency.

## Status: templates, not yet run

**No R interpreter is available in the environment these templates were
written in, so none of this code has actually been executed.** Every
script below is a structurally complete skeleton written directly against
`ANALYSIS_PLAN.md`'s own specification, but per this project's
never-fabricate rule (`PROJECT_SPEC.md` §14), that is not the same claim
as "tested and working." **Before relying on any of it: run it against
either the real `effect_sizes.csv` once populated, or a small synthetic
one, and fix whatever doesn't run.** Treat a first real run as a normal
part of using this code, not a sign something was scaffolded carelessly.

## Required packages

Per `ANALYSIS_PLAN.md` §12: `metafor`, `meta` (primary); `tidyverse`,
`dplyr`, `readxl`, `openxlsx`, `janitor`, `ggplot2`, `robvis`
(supporting). Install only what a given script actually calls — don't
add packages beyond what `ANALYSIS_PLAN.md` names.

## Scripts, in run order

1. **`01_meta_analysis.R`** (Phase 12) — per candidate synthesis family
   (`PROJECT_SPEC.md` §8) that Phase 11 judged eligible
   (`evidence_map.csv`'s `quantitative_synthesis_eligible`,
   `effect_sizes.csv`'s `included_in_pooled_estimate`): fits a
   random-effects model (`ANALYSIS_PLAN.md` §5), reports heterogeneity
   (I², tau², Q, CI, **prediction interval** — §6), runs subgroup
   analysis only where a subgroup actually has enough independent
   studies (§7), and meta-regression only at the ~10-studies-per-moderator
   threshold (§8). Writes results to `05_analysis/meta_analysis/` and
   `05_analysis/heterogeneity/`.
2. **`02_sensitivity_analysis.R`** (Phase 14) — the five specific checks
   `ANALYSIS_PLAN.md` §10 names (risk-of-bias exclusion, leave-one-out,
   jurisdiction removal, study-design subsetting, alternative effect
   measures where defensible) — run against whatever family
   `01_meta_analysis.R` actually pooled. Writes to `05_analysis/sensitivity/`.
3. **`03_publication_bias.R`** (Phase 15) — funnel plot and
   Egger/Begg-type tests, gated behind `ANALYSIS_PLAN.md` §9's own
   ~10-studies-per-family threshold: **refuses to run below it** rather
   than producing a funnel plot too sparse to mean anything, the same
   "don't silently do something meaningless below N" discipline already
   used in `code/extraction/select_pilot_sample.py`.

## What's NOT templated here, and why

Phase 13 (structured synthesis of unpoolable evidence, SWiM) is
**not** an R script — it's a narrative/tabular reporting exercise for
families that fail `ANALYSIS_PLAN.md` §2's decision tree, not a
statistical procedure with a fittable model. See
`06_outputs/supplementary/SWIM_SYNTHESIS_TEMPLATE.md` instead.
