# 03_publication_bias.R -- Phase 15 (publication bias assessment)
#
# STATUS: template, not yet run against real data -- see ../README.md's
# "Status" section.
#
# ANALYSIS_PLAN.md S9: funnel plot, Egger-type test, Begg-type test, or
# selection models -- "only where appropriate, with a practical threshold
# of approximately 10 studies per family for meaningful funnel-asymmetry
# assessment. Do not run these automatically below that threshold, and do
# not interpret funnel asymmetry as proof of publication bias --
# heterogeneity, small-study effects, selective reporting, and
# methodological differences are equally plausible explanations."
# This script enforces the threshold as a hard refusal (matching the
# "don't silently do something meaningless below N" discipline already
# used in code/extraction/select_pilot_sample.py) and prints the
# multiple-explanations caveat alongside every result it does produce.
#
# Input:  05_analysis/effect_sizes/effect_sizes.csv
# Output: 05_analysis/publication_bias/<family>_funnel.png
#         05_analysis/publication_bias/<family>_tests.csv

library(metafor)
library(dplyr)

MIN_STUDIES_FOR_PUB_BIAS <- 10  # ANALYSIS_PLAN.md S9, explicit.

effect_sizes <- read.csv("05_analysis/effect_sizes/effect_sizes.csv", stringsAsFactors = FALSE)
pooled <- effect_sizes %>% filter(included_in_pooled_estimate == TRUE)

if (nrow(pooled) == 0) {
  stop("No pooled effects yet -- nothing to assess for publication bias.")
}

dir.create("05_analysis/publication_bias", showWarnings = FALSE, recursive = TRUE)

for (fam in unique(pooled$synthesis_family)) {

  fam_data <- pooled %>% filter(synthesis_family == fam)
  k <- nrow(fam_data)

  if (k < MIN_STUDIES_FOR_PUB_BIAS) {
    cat(sprintf(
      "Family %s: k=%d, below ANALYSIS_PLAN.md S9's %d-study threshold -- ",
      "REFUSING to run funnel/Egger/Begg for this family. A funnel plot with ",
      "this few points is not meaningfully interpretable for asymmetry; do not ",
      "force one just because the code can technically produce a plot.\n",
      fam, k, MIN_STUDIES_FOR_PUB_BIAS))
    next
  }

  model <- rma(yi = fam_data$effect_estimate, sei = fam_data$standard_error, method = "REML")

  png(sprintf("05_analysis/publication_bias/%s_funnel.png", fam), width = 800, height = 800)
  funnel(model, main = sprintf("Family %s (k=%d)", fam, k))
  dev.off()

  egger <- tryCatch(regtest(model, model = "lm"), error = function(e) NULL)
  begg <- tryCatch(ranktest(model), error = function(e) NULL)

  tests <- data.frame(
    synthesis_family = fam,
    k = k,
    egger_statistic = if (!is.null(egger)) egger$zval else NA,
    egger_p = if (!is.null(egger)) egger$pval else NA,
    begg_kendall_tau = if (!is.null(begg)) begg$tau else NA,
    begg_p = if (!is.null(begg)) begg$pval else NA
  )
  write.csv(tests, sprintf("05_analysis/publication_bias/%s_tests.csv", fam), row.names = FALSE)

  cat(sprintf(
    "Family %s (k=%d): Egger p=%.3f, Begg p=%.3f. REMINDER (ANALYSIS_PLAN.md S9): ",
    "do not interpret funnel asymmetry or a significant test here as PROOF of ",
    "publication bias on its own -- heterogeneity, genuine small-study effects, ",
    "selective outcome reporting, and methodological differences across studies ",
    "are equally plausible explanations. Report this alongside those alternatives, ",
    "not as a standalone verdict.\n",
    fam, k, tests$egger_p, tests$begg_p))
}
