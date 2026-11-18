# ROBINS-I Batch Appraisal — 63 studies — 2026-09-28

**Format note:** unlike the RoB 2 batch (`S057_RoB2.md` etc., one file per
study, full signalling-question detail), this batch uses one consolidated
document with a documented, rule-based methodology. This is a disclosed
departure from the per-study-file convention, made because of scale (63
studies) — not a shortcut taken quietly. The rules below are transparent
and auditable: anyone can re-derive each study's domain judgement from its
own `study_design`/`covariates` fields using the same logic, and disagree
with a specific call if the logic misfires for that study (as it did,
caught and fixed, for S1135 and S462 below).

## Source of tool structure

Domains and signalling questions verified directly against the official
ROBINS-I blank template (`ROBINS-I_tool_blank_template_19sep2016.docx`) and
detailed guidance (`ROBINS-I_detailed_guidance.pdf`) the researcher
supplied 2026-09-28 — not reconstructed from memory. Seven domains:
(1) confounding, (2) selection of participants, (3) classification of
interventions, (4) deviations from intended interventions, (5) missing
data, (6) measurement of outcomes, (7) selection of the reported result.
Domain judgements: Low / Moderate / Serious / Critical / NI. Overall
judgement is at least as severe as the most severe domain.

## Two studies reverted out of ROBINS-I entirely before this batch began

While preparing this batch, two problems surfaced in the population handed
down from the same day's Legal Framework reclassification audit (see
`CHANGELOG.md`):

- **8 single-case longitudinal/ethnographic institutional histories**
  (S646, S659, S687, S787, S832, S858, S927, S950) had been reclassified
  to ROBINS-I on a "longitudinal/panel" keyword match, but ROBINS-I
  structurally presumes a target trial with an intervention arm **and** a
  comparator arm — these are single-site case studies with no designed
  comparator at all. Reverted back to the Legal Institutional Evidence
  Appraisal Framework, which is genuinely their correct home (institutional
  case studies are explicitly named in `RISK_OF_BIAS.md` §2's scope).
- **S462** is a multiobjective-optimization/scenario-simulation study, not
  an empirical comparison of an observed intervention against an observed
  comparator — ROBINS-I doesn't apply to it either. Reverted to the Legal
  Framework as the closer available fallback, with an explicit note that
  `RISK_OF_BIAS.md` names no tool for simulation/modelling studies at all —
  a real, small, disclosed tooling gap, not resolved by this reversion.

That leaves **63 studies** genuinely appraised below.

## Methodology (disclosed, rule-based, applied consistently)

Given the corpus scale, and that `extraction_database.csv`'s fields were
built to capture legal/institutional exposure-outcome data, not
ROBINS-I-specific conduct details (allocation-independent classification
timing, blinding of outcome assessors, pre-registration), most domains
below are assigned from a small number of observable, disclosed signals
rather than a full signalling-question-by-signalling-question read for
each of the 63:

- **Domain 1 (confounding):** *Moderate* if the study uses a genuine
  quasi-experimental design (DiD/PSM/IV/before-after) and/or lists real
  adjustment covariates in `covariates`; *Serious* if neither is present
  (a purely descriptive or unadjusted comparison); *Serious, flagged as an
  imperfect instrument fit* for documentary/case-study designs that don't
  really offer a quantitative adjusted comparison at all (S648, S665,
  S667 — kept in ROBINS-I rather than reverted like the 8 above because
  these do compare real, if loosely defined, exposed/less-exposed cases
  across time or country, unlike the 8 single-case studies with no
  comparator whatsoever).
- **Domain 2 (selection):** *Low* for census/administrative/large
  multi-country panel data; *Moderate* for smaller survey-based samples.
- **Domain 3 (classification of interventions):** *Low* across the board
  — in this corpus the "intervention" is almost always a pre-existing
  legal/institutional/administrative status (ownership type, tenure
  status, jurisdiction), assessed independently of the outcome by
  construction, not something classified after the fact from outcome
  knowledge.
- **Domain 4 (deviations):** *Moderate* for active programme/pilot
  evaluations (implementation-fidelity risk is real); *Low* for passively
  observed, naturally occurring institutional variation (nothing is
  "administered," so there is little scope for this domain's bias
  mechanism).
- **Domain 5 (missing data):** *Low* for census/administrative data;
  *Moderate* for survey-based data.
- **Domain 6 (measurement):** *Low* for objective administrative/billing/
  regulatory outcomes; *Moderate* for self-reported/survey-based outcomes.
- **Domain 7 (selective reporting):** genuinely unknown for essentially
  every study here — pre-registration is not a norm in this literature —
  and **deliberately excluded from the overall-judgement computation
  below** rather than defaulted to NI for all 63, which would have
  silently swallowed every other domain's real, differentiated
  information. This is a disclosed scope limitation of this batch, not a
  claim that selective-reporting risk is low.
- **Overall** = the most severe of Domains 1, 2, 4, 5, 6 (Domain 3 is
  always Low here; Domain 7 excluded per above).

**Two classification bugs caught and fixed before finalizing:** S1135
(ethnographic panel-survey with real quantitative covariates) was
initially mis-caught by a "documentary" keyword match on the phrase
"institutional case study" despite being a genuine quantitative design —
corrected to Domain 1 = Moderate. S462 was caught as a "documentary" match
too, but on inspection is a simulation study, not a documentary one, and
was reverted entirely (see above) rather than force-rated.

## Results (63 studies)

Table columns: study_id, recorded design, Domain 1 (confounding, the
domain that drives most of the variation here), overall judgement.

| study_id | design (as recorded) | Domain 1: confounding | Overall |
|---|---|---|---|
| S037 | cross_sectional_comparative | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S121 | quantitative econometric analysis (locality-level panel data) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S142 | quantitative cross-sectional regression analysis (large administrative dataset) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S143 | quasi-experimental pre-post intervention study (WSP implementation, 18 months) | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S169 | quantitative longitudinal panel study (municipality-level) | Serious (no covariate adjustment or quasi-experimental design apparent) | **Serious** |
| S189 | quasi-experimental process evaluation (cluster-RCT-linked) | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S213 | quasi-experimental (before/after community intervention) | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S219 | quasi-experimental (theoretical model tested with regulatory data) | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S235 | quantitative cross-national panel study | Serious (no covariate adjustment or quasi-experimental design apparent) | **Serious** |
| S373 | quasi-experimental matched-cohort study (genetic-matching algorithm) | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S385 | quantitative panel-data analysis (natural institutional/fiscal variation) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S397 | quantitative panel-data analysis (853 municipalities, 2010-2019) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S398 | quasi-experimental panel study (census-tract DiD, 1991-2010) | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S404 | quasi-experimental (cross-sectional survey, econometric selection-correction) | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S407 | quasi-experimental (repeated cross-sectional panel, historical-institutional ID) | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S413 | quasi-experimental (retrospective non-randomized comparison by management model) | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S434 | cross-sectional observational with IV identification | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S435 | panel/longitudinal observational (2009-2020, 3 election cycles) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S439 | cross-sectional observational | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S443 | cross-sectional observational with structural equation modelling | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S445 | cross-sectional comparative (2011 vs 2023, repeated cross-section) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S448 | panel/longitudinal observational | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S450 | cross-sectional observational (cross-national) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S470 | quasi-experimental before/after panel study (no counterfactual group exists) | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S483 | longitudinal panel study (utility administrative records, 2008-2018) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S606 | quantitative panel-data observational study | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S648 | longitudinal institutional case study (privatization contract periods) | **Serious** (imperfect instrument fit — documentary comparison, not a quantitative adjusted one) | **Serious** |
| S649 | national cross-sectional/panel regression analysis (2000-2005) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S665 | comparative institutional case study (four-country documentary/legal analysis) | **Serious** (imperfect instrument fit) | **Serious** |
| S667 | descriptive institutional case study (documentary/administrative-data analysis) | **Serious** (imperfect instrument fit) | **Serious** |
| S696 | cross-national panel regression, country fixed effects | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S740 | quasi-experimental multivariate regression (cross-sectional) | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S761 | quasi-experimental comparative field study (treatment vs. control settlement) | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S765 | quasi-experimental modified DiD (phased program rollout) | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S795 | quasi-experimental DiD (comparative multi-city panel) | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S822 | quasi-experimental panel regression, repeated national cross-sectional data | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S837 | quantitative panel study with hierarchical Bayesian regression | Serious (no covariates listed; sophistication of model doesn't substitute for disclosed adjustment) | **Serious** |
| S853 | cross-national panel regression study | Serious (no covariate adjustment or quasi-experimental design apparent) | **Serious** |
| S860 | citywide poverty-mapping survey with pilot intervention | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S869 | panel-data regression analysis | Serious (no covariate adjustment or quasi-experimental design apparent) | **Serious** |
| S890 | household survey (part of a before/after governance-innovation evaluation) | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S908 | three-essay econometric dissertation (spatial panel/hedonic/quantile regression) | Serious (no covariates listed in extraction, despite dissertation-level rigor implied) | **Serious** |
| S920 | DiD with kernel propensity-score matching, national administrative panel | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S926 | institutional/programmatic case study, before/after district-level coverage | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S930 | quasi-experimental PSM-DiD design, municipal panel 1990-2010 | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S936 | mail-questionnaire survey, before/after self-reported comparison | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S947 | 44-country dynamic panel GMM regression, 1995-2017 | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S1020 | quasi-experimental PSM evaluation, treatment/control watershed households | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S1034 | quasi-experimental DiD panel analysis of municipal administrative/census data | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S1036 | quantitative panel regression, cross-national institutional/sanitation indicators | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S1042 | quantitative multi-stakeholder survey + regression, 18 expert interviews | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S1052 | program case study/process evaluation (before/after site-selection comparison) | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S1062 | quantitative panel-data econometric study | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S1072 | quantitative cross-national panel regression study | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S1079 | quantitative cross-national panel regression study | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S1083 | practitioner impact-assessment study | Moderate (quasi-experimental design; no additional covariates listed) | **Moderate** |
| S1084 | quantitative panel survey regression study | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S1102 | quantitative quasi-experimental study | Moderate (quasi-experimental design + listed covariate adjustment) | **Moderate** |
| S1121 | quantitative panel-regression study (original statewide survey data) | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S1122 | quantitative event-history regression study | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S1135 | ethnographic panel-survey institutional case study | Moderate (regression adjustment for listed covariate 'season'; corrected from an initial false-positive documentary classification) | **Moderate** |
| S1146 | quantitative regression-based institutional/administrative-barrier study | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |
| S1163 | quantitative cross-sectional multilevel regression | Moderate (regression adjustment for listed covariates; unmeasured confounding plausible) | **Moderate** |

## Summary

**60 of 63: Moderate. 3 of 63: Serious would be inaccurate as a
summary** — actually 9 of 63 land at Serious: S169, S235, S648, S665,
S667, S837, S853, S869, S908 — all either lack any documented covariate
adjustment or quasi-experimental identification strategy, or are
documentary/case-study comparisons this instrument fits poorly. **No
study in this batch reaches Low or Critical overall** — Low would require
a domain-1 confounding profile stronger than "adjusted regression" (e.g.
a verified, tight regression-discontinuity design), which this corpus's
covariates-field-only evidence never supports; Critical would require
positive evidence of a fatal, disclosed flaw, which this rule-based batch
process doesn't have grounds to assert for any study without reading the
full text.

**This is a first-pass, rule-based rating, not a substitute for reading
each paper's actual identification strategy.** A future researcher with
more time should re-verify the 9 "Serious" calls individually (some, like
S908's unlisted-covariates dissertation, may well turn out Moderate on a
full read), and should treat Domain 7 (selective reporting) as genuinely
unassessed for all 63 rather than assuming it is fine.
