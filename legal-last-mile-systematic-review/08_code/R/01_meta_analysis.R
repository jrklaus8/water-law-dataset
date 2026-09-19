# 01_meta_analysis.R -- Phase 12 (meta-analysis where justified)
#
# STATUS: template, not yet run against real data -- no R interpreter was
# available in the environment this was written in. See ../README.md's
# "Status" section before relying on this. Structurally complete against
# ANALYSIS_PLAN.md SS4-8, but verify it actually runs once effect_sizes.csv
# has real rows.
#
# Fits one random-effects model per candidate synthesis family
# (PROJECT_SPEC.md S8) that has already cleared two upstream judgment
# calls this script does NOT make: Phase 11's quantitative-synthesis
# decision tree (ANALYSIS_PLAN.md S2, applied per family) and, per study,
# effect_sizes.csv's own included_in_pooled_estimate flag
# (DATA_DICTIONARY.md -- set only for effects "actually judged eligible
# for quantitative synthesis"). This script trusts those flags; it never
# re-derives eligibility itself.
#
# Input:  05_analysis/effect_sizes/effect_sizes.csv
# Output: 05_analysis/meta_analysis/<family>_model.rds (fitted model object)
#         05_analysis/meta_analysis/<family>_forest.png
#         05_analysis/heterogeneity/<family>_heterogeneity.csv

library(metafor)
library(dplyr)
library(ggplot2)

MIN_STUDIES_FOR_SUBGROUP <- 3   # ANALYSIS_PLAN.md S7: "sufficient independent
                                 # studies" is not numerically pinned down
                                 # there -- 3 is this script's own
                                 # conservative floor below which a subgroup
                                 # estimate is not reported at all; revise
                                 # if the researcher sets an explicit
                                 # threshold in ANALYSIS_PLAN.md.
MIN_STUDIES_PER_MODERATOR <- 10 # ANALYSIS_PLAN.md S8, explicit.

effect_sizes <- read.csv("05_analysis/effect_sizes/effect_sizes.csv", stringsAsFactors = FALSE)
extraction <- read.csv("03_extraction/extracted_data/extraction_database.csv", stringsAsFactors = FALSE)

# effect_sizes.csv itself has no jurisdiction/context columns (see its
# schema in DATA_DICTIONARY.md) -- moderator and subgroup candidates live
# in extraction_database.csv instead, joined in here by study_id.
# ANALYSIS_PLAN.md SS7-8 name candidate moderators/subgroups colloquially
# ("jurisdiction", "decentralization", "regulatory_structure") that do
# NOT map 1:1 onto extraction_database.csv's actual column names
# (CODEBOOK.md S2: country, subnational_unit, legal_system,
# regulatory_model). This script does not invent that mapping --
# `jurisdiction` below is approximated as `country` (the closest existing
# column), and "legal_remedy"/"service_type" have no direct
# extraction_database.csv equivalent at all as of this schema version.
# Resolve the real mapping deliberately in ANALYSIS_PLAN.md or here before
# trusting any subgroup/moderator result -- do not assume this
# approximation is correct without checking it against what the
# extracted studies actually recorded.
effect_sizes <- effect_sizes %>%
  left_join(extraction %>% select(study_id, jurisdiction = country, study_design,
                                    regulatory_model, legal_system),
            by = "study_id")

pooled <- effect_sizes %>% filter(included_in_pooled_estimate == TRUE)

if (nrow(pooled) == 0) {
  stop("No rows in effect_sizes.csv have included_in_pooled_estimate == TRUE yet -- ",
       "nothing to pool. This is expected until Phase 11 has actually judged ",
       "some family eligible; do not force a run before that.")
}

families <- unique(pooled$synthesis_family)

for (fam in families) {

  fam_data <- pooled %>% filter(synthesis_family == fam)
  cat(sprintf("\n=== Synthesis family: %s (%d effect(s)) ===\n", fam, nrow(fam_data)))

  # ANALYSIS_PLAN.md S11 / CODEBOOK.md S12: one prespecified effect per
  # study and outcome family is the first-paper default. Flag rather than
  # silently allow if a study contributes more than one row to this
  # family -- that's exactly the dependence CODEBOOK.md S12 says needs a
  # deliberate multilevel/RVE/multivariate decision, not an accident.
  dupe_studies <- fam_data %>% count(study_id) %>% filter(n > 1)
  if (nrow(dupe_studies) > 0) {
    warning(sprintf(
      "Family %s: %d study/studies contribute more than one pooled effect (%s). ",
      fam, nrow(dupe_studies), paste(dupe_studies$study_id, collapse = ", ")),
      "ANALYSIS_PLAN.md S11 requires a deliberate dependence-modeling decision ",
      "(multilevel / robust-variance / multivariate) before pooling these as if ",
      "independent -- this script does NOT make that decision for you. Resolve ",
      "before trusting the model fit below.")
  }

  # ANALYSIS_PLAN.md S5: random effects, because studies are expected to
  # differ in population/institutional context/legal system/service
  # system/operationalization -- not a license to pool studies that
  # failed the S2 comparability test upstream.
  model <- rma(
    yi = fam_data$effect_estimate,
    sei = fam_data$standard_error,
    method = "REML",
    slab = fam_data$study_id
  )

  print(summary(model))

  dir.create("05_analysis/meta_analysis", showWarnings = FALSE, recursive = TRUE)
  dir.create("05_analysis/heterogeneity", showWarnings = FALSE, recursive = TRUE)

  saveRDS(model, sprintf("05_analysis/meta_analysis/%s_model.rds", fam))

  # ANALYSIS_PLAN.md S6: I^2, tau^2, Q, CI, and the prediction interval --
  # the prediction interval especially, since it speaks directly to how
  # much the effect might vary across a future comparable jurisdiction,
  # which matters given this review's explicitly cross-jurisdictional
  # design.
  pred <- predict(model)
  heterogeneity <- data.frame(
    synthesis_family = fam,
    k = model$k,
    pooled_estimate = model$b[1],
    ci_lb = model$ci.lb,
    ci_ub = model$ci.ub,
    I2 = model$I2,
    tau2 = model$tau2,
    Q = model$QE,
    Q_p = model$QEp,
    pred_lb = pred$pi.lb,
    pred_ub = pred$pi.ub
  )
  write.csv(heterogeneity,
            sprintf("05_analysis/heterogeneity/%s_heterogeneity.csv", fam),
            row.names = FALSE)

  # Substantive heterogeneity is itself potentially reportable even
  # without a pooled estimate (ANALYSIS_PLAN.md S6) -- a high I^2 here is
  # a finding to discuss, not a bug to suppress by switching models.
  if (!is.na(model$I2) && model$I2 > 75) {
    cat(sprintf(
      "NOTE: family %s shows I^2 = %.1f%% -- high heterogeneity. Per ANALYSIS_PLAN.md ",
      "S6, treat this as a substantive/institutional question (legal system, ",
      "centralization, provider model, population, mechanism, outcome, design), ",
      "not merely a statistical nuisance to explain away.\n", fam, model$I2))
  }

  png(sprintf("05_analysis/meta_analysis/%s_forest.png", fam), width = 1000, height = 800)
  forest(model, main = sprintf("Family %s (random effects, k=%d)", fam, model$k))
  dev.off()

  # ANALYSIS_PLAN.md S7: subgroup analysis only where a subgroup actually
  # has enough independent studies -- never run reflexively just because
  # a grouping column exists.
  if ("jurisdiction" %in% names(fam_data)) {
    subgroup_counts <- fam_data %>% count(jurisdiction)
    eligible_subgroups <- subgroup_counts %>% filter(n >= MIN_STUDIES_FOR_SUBGROUP)
    if (nrow(eligible_subgroups) >= 2) {
      cat(sprintf("Subgroup analysis by jurisdiction (%d group(s) with >= %d studies):\n",
                   nrow(eligible_subgroups), MIN_STUDIES_FOR_SUBGROUP))
      for (grp in eligible_subgroups$jurisdiction) {
        grp_data <- fam_data %>% filter(jurisdiction == grp)
        grp_model <- rma(yi = grp_data$effect_estimate, sei = grp_data$standard_error, method = "REML")
        cat(sprintf("  %s (k=%d): estimate=%.3f [%.3f, %.3f]\n",
                     grp, grp_model$k, grp_model$b[1], grp_model$ci.lb, grp_model$ci.ub))
      }
    } else {
      cat("Subgroup analysis skipped: no jurisdiction has >= ", MIN_STUDIES_FOR_SUBGROUP,
          " independent studies yet.\n")
    }
  }

  # ANALYSIS_PLAN.md S8: meta-regression is not a primary analysis, and
  # never below ~10 studies per moderator -- this loop only ATTEMPTS a
  # moderator if there's any chance of clearing that bar; it does not
  # lower the bar to fit something anyway.
  # Only the columns actually joined in above (or present natively in
  # effect_sizes.csv) are attempted -- see the mapping caveat where
  # extraction_database.csv was joined in, above.
  candidate_moderators <- intersect(
    c("jurisdiction", "regulatory_model", "legal_system", "study_design"),
    names(fam_data)
  )
  for (mod in candidate_moderators) {
    if (nrow(fam_data) >= MIN_STUDIES_PER_MODERATOR) {
      cat(sprintf("Fitting meta-regression on moderator '%s' (k=%d >= %d threshold)...\n",
                   mod, nrow(fam_data), MIN_STUDIES_PER_MODERATOR))
      mod_formula <- as.formula(paste("~", mod))
      mod_model <- tryCatch(
        rma(yi = fam_data$effect_estimate, sei = fam_data$standard_error,
            mods = mod_formula, method = "REML", data = fam_data),
        error = function(e) {
          cat(sprintf("  Meta-regression on '%s' failed to fit: %s\n", mod, conditionMessage(e)))
          NULL
        }
      )
      if (!is.null(mod_model)) print(summary(mod_model))
    } else {
      cat(sprintf("Meta-regression on '%s' skipped: k=%d below the %d-study threshold.\n",
                   mod, nrow(fam_data), MIN_STUDIES_PER_MODERATOR))
    }
  }
}
