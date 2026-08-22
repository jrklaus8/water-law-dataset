# Extraction Codebook

Governs `03_extraction/extracted_data/extraction_database.csv`. Piloted on
~10 studies before full extraction (`PRISMA_WORKFLOW.md` Phase 7). Every
field below maps to a column in that CSV — see `DATA_DICTIONARY.md` for
type/format detail per field.

## 1. Identification

`study_id` · `citation` · `doi` · `publication_year` · `publication_type` ·
`language` · `database_source` · `peer_reviewed`

## 2. Jurisdiction

`country` · `subnational_unit` · `legal_system` · `urban_rural` ·
`service_provider` · `regulatory_model`

## 3. Population

`population` · `sample_size` · `household_level` · `community_level` ·
`income_group` · `tenure_status` · `legal_status` · `indigenous_population` ·
`migrant_population`

State the unit of analysis explicitly (`PROJECT_SPEC.md` §2, §4) — this is
not optional metadata, it determines whether a study's effect estimate can
ever be pooled with another study's.

## 4. Legal mechanism

The four families used as the initial coding architecture (open to being
supported, modified, subdivided, or rejected by the evidence —
`PROJECT_SPEC.md` §2):

- `ELIGIBILITY`
- `BURDEN`
- `DISCRETION_ACCOMMODATION`
- `ENFORCEMENT`

Detailed codes (a study may carry more than one):

```
documentation · tenure · property · planning · zoning · building_permit ·
service_area · fees · procedural_steps · delay · discretion ·
hardship_exception · accommodation · administrative_review · complaint ·
judicial_review · disconnection · reconnection · sanction · participation ·
institutional_fragmentation · political_coordination · bureaucratic_assistance
```

Do not add codes merely to make the model more quantitative — a code earns
its place by describing a mechanism actually observed in the retrieved
literature.

## 5. Outcomes

```
formal_connection · water_access · sanitation_access · service_coverage ·
service_reliability · service_quantity · service_quality · affordability ·
service_continuity · application_success · refusal · delay
```

Map every outcome to the hierarchy in `PROJECT_SPEC.md` §7 (primary /
effective-access / economic-access / administrative). Never pool outcomes
across families simply because both are colloquially "access."

## 6. Mediators and moderators (contextual codes, not automatic statistical variables)

**Potential mediators:** administrative burden, learning costs, compliance
costs, psychological costs, application completion, administrative delay,
bureaucratic interaction, legal assistance, appeal capacity, accommodation.

**Potential moderators:** regulatory capacity, decentralization, service
provider ownership, urban vs. rural context, institutional fragmentation,
income, tenure status, legal recognition, administrative review, judicial
accessibility, service type, study design, study period.

Most moderators should remain contextual codes; only promote a moderator to
a formal meta-regression covariate under the minimum-study-count rule in
`ANALYSIS_PLAN.md` §"Meta-regression".

## 7. Statistical information

`effect_measure` · `effect_estimate` · `lower_CI` · `upper_CI` ·
`standard_error` · `p_value` · `sample_size` (extraction-specific, may
differ from population `sample_size` if the effect is on a subsample) ·
`adjusted_or_unadjusted` · `covariates` · `model_type`

## 8. Study quality

`study_design` · `risk_of_bias_tool` · `risk_of_bias_rating` ·
`selection_bias` · `measurement_bias` · `confounding` · `attrition` ·
`reporting_bias` · `legal_measurement_quality` · `outcome_measurement_quality`

See `RISK_OF_BIAS.md` for which tool applies to which design.

## 9. Mechanism certainty

`mechanism_certainty` — distinguishes *authors argue X* from *the study
directly demonstrated X*:

| Value | Meaning |
|---|---|
| 0 | Inferred only |
| 1 | Documented association |
| 2 | Mechanism directly observed |
| 3 | Quasi-experimental evidence |
| 4 | Experimental evidence |

## 10. Evidence status

`evidence_status` — one of `OBSERVED` / `CALCULATED` / `ASSUMED` /
`INTERPRETED` per `PROJECT_SPEC.md` §13. Apply this per extracted
statistic, not per study as a whole — a single study record may contain
both an OBSERVED effect size and an ASSUMED standard error reconstructed
from a reported confidence interval.

## 11. Provenance

`source_document` · `page` · `table` · `figure` · `section` ·
`exact_location` · `extraction_note` · `researcher` · `date_extracted`

Every extracted statistic must carry provenance — see `REPRODUCIBILITY.md`
§"Evidence provenance" for the full rationale and a worked example.

## 12. Dependent effect sizes

If a study reports several relevant effects, the first-paper default is one
prespecified effect per study and outcome family. Do not use multilevel/
robust-variance/multivariate dependence models merely because they are
available — only when the evidence base is large enough to warrant them
(`ANALYSIS_PLAN.md` §"Dependent effect sizes").
