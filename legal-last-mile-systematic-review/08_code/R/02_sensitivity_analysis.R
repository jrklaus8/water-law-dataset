# 02_sensitivity_analysis.R -- Phase 14 (sensitivity analysis)
#
# STATUS: template, not yet run against real data -- see ../README.md's
# "Status" section. Run 01_meta_analysis.R first; this script re-derives
# its own pooled dataset the same way rather than depending on 01's saved
# .rds files, so it can be re-run independently.
#
# ANALYSIS_PLAN.md S10 is explicit that each sensitivity analysis must
# answer a specific methodological question -- this script runs exactly
# the five it names, no more, and never "reflexively." If a family's data
# doesn't support one of the five (e.g. no risk_of_bias_rating recorded),
# that check is skipped and reported as skipped, not silently omitted.
#
# Input:  05_analysis/effect_sizes/effect_sizes.csv,
#         03_extraction/extracted_data/extraction_database.csv
# Output: 05_analysis/sensitivity/<family>_sensitivity.csv

library(metafor)
library(dplyr)

effect_sizes <- read.csv("05_analysis/effect_sizes/effect_sizes.csv", stringsAsFactors = FALSE)
extraction <- read.csv("03_extraction/extracted_data/extraction_database.csv", stringsAsFactors = FALSE)

effect_sizes <- effect_sizes %>%
  left_join(extraction %>% select(study_id, risk_of_bias_rating, country, study_design),
            by = "study_id")

pooled <- effect_sizes %>% filter(included_in_pooled_estimate == TRUE)

if (nrow(pooled) == 0) {
  stop("No pooled effects yet -- nothing to run sensitivity analysis on.")
}

fit_and_summarize <- function(data, label) {
  if (nrow(data) < 2) {
    return(data.frame(check = label, k = nrow(data), estimate = NA, ci_lb = NA, ci_ub = NA,
                       note = "fewer than 2 studies remain -- cannot fit"))
  }
  m <- tryCatch(rma(yi = data$effect_estimate, sei = data$standard_error, method = "REML"),
                error = function(e) NULL)
  if (is.null(m)) {
    return(data.frame(check = label, k = nrow(data), estimate = NA, ci_lb = NA, ci_ub = NA,
                       note = "model failed to fit"))
  }
  data.frame(check = label, k = m$k, estimate = m$b[1], ci_lb = m$ci.lb, ci_ub = m$ci.ub, note = "")
}

for (fam in unique(pooled$synthesis_family)) {

  fam_data <- pooled %>% filter(synthesis_family == fam)
  results <- list()

  results[["full_sample"]] <- fit_and_summarize(fam_data, "full sample (baseline)")

  # 1. Risk of bias: exclude high-risk studies -- does the finding depend
  #    on weaker studies?
  if ("risk_of_bias_rating" %in% names(fam_data) && any(!is.na(fam_data$risk_of_bias_rating))) {
    # NOTE: "high risk" spans different labels across tools (RoB 2: "high";
    # ROBINS-I: "serious"/"critical"; JBI/CASP/MMAT: their own vocabulary --
    # RISK_OF_BIAS.md S1 deliberately does not use one universal scale).
    # This pattern-matches common high-risk labels across tools rather
    # than assuming one vocabulary; verify it actually caught every
    # high-risk study in this family before trusting the result.
    high_risk_pattern <- "high|serious|critical"
    low_risk_only <- fam_data %>%
      filter(!grepl(high_risk_pattern, risk_of_bias_rating, ignore.case = TRUE))
    results[["exclude_high_risk"]] <- fit_and_summarize(low_risk_only, "excluding high-risk-of-bias studies")
  } else {
    results[["exclude_high_risk"]] <- data.frame(
      check = "excluding high-risk-of-bias studies", k = NA, estimate = NA, ci_lb = NA, ci_ub = NA,
      note = "skipped: no risk_of_bias_rating recorded for this family yet")
  }

  # 2. Leave-one-out: is one study driving the result?
  loo_rows <- list()
  for (i in seq_len(nrow(fam_data))) {
    loo_data <- fam_data[-i, ]
    loo_result <- fit_and_summarize(loo_data, sprintf("leave-one-out: excluding %s", fam_data$study_id[i]))
    loo_rows[[i]] <- loo_result
  }
  results[["leave_one_out"]] <- do.call(rbind, loo_rows)

  # 3. Jurisdiction sensitivity: remove one major geographic group -- is
  #    the result dependent on one institutional context?
  if ("country" %in% names(fam_data)) {
    for (grp in unique(na.omit(fam_data$country))) {
      excl_data <- fam_data %>% filter(country != grp)
      results[[paste0("exclude_country_", grp)]] <-
        fit_and_summarize(excl_data, sprintf("excluding country=%s", grp))
    }
  }

  # 4. Study design: compare observational-only vs.
  #    observational+quasi-experimental vs. experimental evidence
  #    separately -- ANALYSIS_PLAN.md S10 asks for these as separate
  #    comparisons, not a single pooled re-fit with design as a covariate
  #    (that's meta-regression, already covered in 01_meta_analysis.R S8).
  if ("study_design" %in% names(fam_data)) {
    obs_only <- fam_data %>% filter(grepl("observ", study_design, ignore.case = TRUE))
    results[["observational_only"]] <- fit_and_summarize(obs_only, "observational-only subset")

    exp_only <- fam_data %>% filter(grepl("experiment|randomi", study_design, ignore.case = TRUE))
    results[["experimental_only"]] <- fit_and_summarize(exp_only, "experimental-only subset")
  }

  # 5. Alternative effect measures: only where substantively and
  #    mathematically defensible (ANALYSIS_PLAN.md S10) -- this script
  #    deliberately does NOT attempt an automatic measure conversion here.
  #    A blanket odds-ratio conversion is exactly what ANALYSIS_PLAN.md S4
  #    warns against ("do not automatically convert every measure").
  #    Decide case by case whether an alternative-measure comparison is
  #    defensible for this family, and if so, add it explicitly rather
  #    than through a generic loop.
  cat(sprintf(
    "Family %s: alternative-effect-measure sensitivity check NOT automated -- ",
    "ANALYSIS_PLAN.md S4/S10 require a case-by-case defensibility judgment, ",
    "add manually if applicable for this family.\n", fam))

  fam_results <- do.call(rbind, results)
  dir.create("05_analysis/sensitivity", showWarnings = FALSE, recursive = TRUE)
  write.csv(fam_results, sprintf("05_analysis/sensitivity/%s_sensitivity.csv", fam), row.names = FALSE)
  cat(sprintf("Wrote %d sensitivity check row(s) for family %s.\n", nrow(fam_results), fam))
}
