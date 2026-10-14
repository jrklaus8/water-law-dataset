# R Analysis Code (Phases 12, 14, 15)

`ANALYSIS_PLAN.md` §12 specifies R for the meta-analytic phases —
`metafor`/`meta` are the mature, standard tools for this, unlike the
stdlib-Python convention used for this repository's search/screening/
extraction pipeline scripts under `code/`. This is a deliberate,
already-made tooling choice, not an inconsistency.

## Status: validated 2026-09-28, ready to use once a family is poolable

> **Correction, 2026-10-04.** The 2026-09-28 validation did not cover the column types of the real `effect_sizes.csv`: its free text in non-pooled rows made R read `effect_estimate` and `standard_error` as character, so `rma()` would have failed ("'yi' is not numeric") the first time any row was flagged for pooling. All three scripts now coerce the pooled rows to numeric and stop with a clear message if a pooled row has no numeric estimate or SE. `code/tests/test_r_templates.py` (run by `regenerate_all.sh`) exercises all three scripts with synthetic pooled rows in the real layout.

**Updated 2026-09-28: an R interpreter became available in this environment (installed via
`apt-get install r-base-core`, plus `r-cran-metafor`/`r-cran-dplyr`/`r-cran-ggplot2` — the only
three packages any of these three scripts actually `library()`-load; `meta`/`readxl`/
`openxlsx`/`janitor`/`robvis` below are unused by the code as written and were never installed
or needed). All three scripts were run against the real `effect_sizes.csv` (currently 62 rows,
all `included_in_pooled_estimate = FALSE` per Phase 11's verdict) and against several synthetic
datasets built specifically to exercise every branch the real data doesn't currently reach.**

Against real data, all three scripts correctly and immediately `stop()` with an informative
message rather than running -- exactly the intended behavior given nothing is poolable yet, not
a bug. Against synthetic data (crafted to include enough pooled rows, enough per-jurisdiction
studies, enough per-moderator studies, and, in one dataset, deliberately high heterogeneity),
**4 real bugs were found and fixed, all the same class of error**: a multi-line `sprintf()` call
where the message was split across several string arguments intended to read as one continuous
sentence, but R does not auto-concatenate adjacent string literals the way some other languages
do -- each fragment was instead being passed as a separate *value* argument to fill a `%s`/`%d`
placeholder that didn't exist for it, either silently dropping the real substitution values
(`02_sensitivity_analysis.R`, produced a warning and garbled text but didn't crash) or throwing
a hard, unrecoverable `Error` (`01_meta_analysis.R`'s I²>75% heterogeneity note; both of
`03_publication_bias.R`'s user-facing messages -- one of which fires on *every* run, since its
two branches, below- and at-or-above the 10-study threshold, are exhaustive). **This meant
`03_publication_bias.R` would have crashed on its very first real invocation, whichever branch
it took.** Fixed by wrapping each split message in `paste0()` before passing it to `sprintf()`,
so the fragments concatenate into one format string as originally intended. See
`CHANGELOG.md`'s 2026-09-28 "R templates validated" entry for the full account of what was
tested and how.

**What this validation does and does not establish**: every branch of all three scripts now
runs cleanly against synthetic data structurally equivalent to what a real poolable family
would look like (multiple studies, several jurisdictions, high and low heterogeneity, k above
and below each script's own threshold). It does **not** mean these scripts have been run
against a real poolable family, because none currently exists (Phase 11's verdict). Treat the
first real run against genuine pooled data as still worth double-checking output plausibility
against expectations, the same discipline as any first real-data run of validated code -- but
not as a search for further bugs, since the code paths themselves are now exercised and clean.

## Required packages

Per `ANALYSIS_PLAN.md` §12: `metafor`, `meta` (primary); `tidyverse`,
`dplyr`, `readxl`, `openxlsx`, `janitor`, `ggplot2`, `robvis`
(supporting). Install only what a given script actually calls — don't
add packages beyond what `ANALYSIS_PLAN.md` names. **Confirmed 2026-09-28**:
the three scripts below only actually `library()`-load `metafor`, `dplyr`,
and `ggplot2` as written — `meta`, `readxl`, `openxlsx`, `janitor`, and
`robvis` are part of `ANALYSIS_PLAN.md` §12's broader named toolkit but
are not called by any code that currently exists here. Install them only
if a future addition to these scripts actually needs one.

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
