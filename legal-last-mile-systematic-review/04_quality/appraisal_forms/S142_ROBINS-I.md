# ROBINS-I Appraisal (partial/pilot) -- S142

**Citation:** Allaire MC, Brusco B, Bakchan A, Elliott MA, Jordan MA, Maxcy-Brown J, White KD (2024). Water and wastewater infrastructure inequity in unincorporated communities. npj Clean Water 7:125.

**Date appraised:** 2026-09-16  
**Appraiser:** Claude-AI-appraisal-2026-09-16

## Source of tool structure

Tool structure obtained via WebSearch (WebFetch to every publisher/repository domain tried -- bristol.ac.uk, riskofbias.info, cochrane.org, corates.org, pmc.ncbi.nlm.nih.gov -- returned EGRESS_BLOCKED in this environment; see CHANGELOG.md 2026-09-16). Only the Confounding domain (Domain 1) is assessed below, using signalling-question concepts recovered with reasonable confidence from multiple WebSearch results ('Is there potential for confounding of the effect of intervention in this study?'; whether an appropriate analysis method controlled for important confounding domains). The other six domains (selection of participants, classification of interventions, deviations from intended interventions, missing data, measurement of outcomes, selection of the reported result) could not be recovered as specific signalling questions in this environment, so per researcher decision 2026-09-16 they are marked 'not assessable -- incomplete tool text obtained in this environment' rather than guessed. This is a partial, flagged appraisal, not a complete ROBINS-I application -- confounding is described in the methodological literature as typically the dominant source of bias in non-randomized studies, which is why it is the one domain assessed here, but the overall rating below is a lower bound, not a full ROBINS-I overall judgement.

## Domain-level judgements

| Domain | Judgement | Basis |
|---|---|---|
| 1. Bias due to confounding | Moderate | Adjusted multivariate negative binomial regression explicitly controlling for poverty rate, proximity to municipal boundary, and regional/state indicators (extraction_database.csv covariates field) -- genuine confounder adjustment, but still an observational cross-sectional design that cannot rule out unmeasured confounders (e.g. historical infrastructure-investment patterns). |
| 2. Bias due to selection of participants into the study | Not assessable -- incomplete tool text obtained in this environment | See 'Source of tool structure' above. |
| 3. Bias in classification of interventions | Not assessable -- incomplete tool text obtained in this environment | See 'Source of tool structure' above. |
| 4. Bias due to deviations from intended interventions | Not assessable -- incomplete tool text obtained in this environment | See 'Source of tool structure' above. |
| 5. Bias due to missing data | Not assessable -- incomplete tool text obtained in this environment | See 'Source of tool structure' above. |
| 6. Bias in measurement of outcomes | Not assessable -- incomplete tool text obtained in this environment | See 'Source of tool structure' above. |
| 7. Bias in selection of the reported result | Not assessable -- incomplete tool text obtained in this environment | See 'Source of tool structure' above. |

## Overall judgement: at least Moderate (partial; lower bound only)

ROBINS-I's own combination rule sets the overall judgement to the most severe domain-level judgement (with possible escalation). Since 6 of 7 domains are not assessable here, this is a lower bound from the Confounding domain alone, not a complete ROBINS-I overall judgement -- the true overall judgement could be worse (e.g. 'Critical') but cannot be better than what is shown here.
