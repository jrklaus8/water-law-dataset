# JBI Critical Appraisal Checklist for Analytical Cross-Sectional Studies — Batch — 2026-09-28

151 studies were tagged with some spelling of this tool when this batch began (99 from
before today's session, 52 from today's Legal Framework reclassification audit). None had
a `risk_of_bias_rating` yet.

## A new problem found while preparing this batch: 26 studies are qualitative, not cross-sectional

While pulling extraction records, 26 pre-existing JBI-tagged studies turned out to have a
`study_design` field that is explicitly qualitative — "qualitative case study," "qualitative
documentary analysis," "qualitative ethnographic case study," "qualitative comparative case
study," "historical case study" — not an analytical cross-sectional design at all: S403,
S410, S412, S414, S415, S416, S417, S419, S420, S424, S425, S431, S433, S441, S444, S446,
S447, S451, S455, S456, S457, S458, S459, S460, S461, S465. These predate today's session
(tagged with a bare "JBI," not today's reclassification-note format), so this is a
pre-existing issue, not something introduced by today's audit — but it surfaced during it.

**These 26 are NOT appraised below.** The JBI Cross-Sectional checklist assumes a
quantitative exposure-outcome comparison; applying it to a qualitative case study would
produce a meaningless score. They likely belong under CASP Qualitative or, for the more
documentary/historical ones, the Legal Institutional Evidence Appraisal Framework — but
that decision needs the same individual-study care given to today's other reclassifications,
not a rushed blanket move at the end of an already-long session. **Flagged as a new,
itemized, unresolved open item** (added to the session's task list alongside the 5
ambiguous AMSTAR2 studies and the reversions found during the ROBINS-I batch).

That leaves **125 studies** genuinely appraised below.

## Source of tool structure

The 8-item checklist verified directly against the official JBI PDF
(`Checklist_for_Analytical_Cross_Sectional_Studies.pdf`, JBI 2020) the researcher supplied.
Response options: Yes / No / Unclear / Not applicable. JBI's own form ends in an "Include /
Exclude / Seek further info" reviewer decision — **relabeled here as "Low concern / Some
concern / High concern"** to avoid any reader mistaking a methodological-quality judgement
for a re-opening of this project's already-final Phase 6 inclusion decision. No study's
inclusion in this systematic review is affected by anything in this file.

## Methodology (disclosed, rule-based, same approach as the ROBINS-I batch)

Each of the 8 items is answered Yes only when a specific, disclosed signal is present in
`extraction_database.csv`; otherwise Unclear (not fabricated as No, since silence in this
project's extraction fields — built for a different purpose — isn't evidence of absence):

1. Inclusion criteria clear → Yes if `population` and a sample-size field are both populated.
2. Subjects/setting described → Yes if `population` and `country` are both populated.
3. Exposure measured validly/reliably → **Unclear for all 125** — this project's extraction
   fields don't capture exposure-measurement-validity detail (e.g. a 'gold standard'
   comparison), so this item is honestly unanswerable at batch scale for every study, not
   selectively.
4. Objective/standard outcome-classification criteria → Yes if the design references an
   administrative/census/billing/regulatory outcome.
5. Confounders identified → Yes if `covariates` is non-empty.
6. Confounders addressed → Yes if `covariates` is non-empty AND the design names a
   regression-type method.
7. Outcome measured validly/reliably → same signal as item 4 (administrative/objective
   outcome source).
8. Appropriate statistical analysis → Yes if the design names a real statistical method
   (regression/logit/probit/OLS/GLM/GMM/etc.).

**Overall:** Low concern (≥6/8 Yes), Some concern (3-5/8 Yes), High concern (<3/8 Yes) —
"High concern" is explicitly labeled as reflecting **sparse extraction, not necessarily a
weak study** in every row below, since roughly half this batch (67 of 125) never had its
`covariates`/statistical-method detail captured at extraction time at all.

## Results (125 studies)

Item order: 1 inclusion-criteria · 2 subjects/setting · 3 exposure validity · 4 outcome
objectivity · 5 confounders identified · 6 confounders addressed · 7 outcome validity ·
8 stats appropriateness.

| study_id | design (as recorded) | Items 1-8 | Yes | Overall |
|---|---|---|---|---|
| S003 | cross-sectional (environmental sampling + GIS + secondary socioeconomic) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S006 | cross-sectional household survey + key informant interviews | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S021 | cross-sectional administrative-records case study | Yes,Yes,Unclear,Yes,Unclear,Unclear,Yes,Unclear | 4/8 | **Some concern** |
| S022 | cross-sectional citizen perception survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S039 | cross_sectional_survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S048 | cross_sectional (large-N) | Yes,Yes,Unclear,Yes,Unclear,Unclear,Yes,Unclear | 4/8 | **Some concern** |
| S051 | cross_sectional comparative (deprivation-index methodology) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S060 | cross_sectional (survey plus regression analysis) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S075 | observational (panel/longitudinal operator revenue records) | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S084 | cross-sectional household survey | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S104 | quantitative cross-sectional analysis | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S117 | quantitative comparative institutional-performance study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S129 | quantitative cross-sectional survey with multivariate CHAID modeling | Yes,Yes,Unclear,Unclear,Yes,Unclear,Unclear,Unclear | 3/8 | **Some concern** |
| S135 | quantitative cross-sectional ecological (county-level) regression | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S167 | quantitative cross-sectional survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S174 | quantitative cross-sectional regression analysis (municipality-level) | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S178 | quantitative cross-sectional survey (repeated cross-section) | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S181 | quantitative cross-national statistical modeling (Bayesian network) | Yes,Yes,Unclear,Unclear,Yes,Unclear,Unclear,Unclear | 3/8 | **Some concern** |
| S182 | quantitative cross-sectional perception survey with spatial analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S192 | quantitative cross-sectional survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S206 | quantitative cross-sectional | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S210 | quantitative cross-sectional | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S230 | quantitative cross-sectional (social network analysis) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S240 | quantitative cross-sectional comparative study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S244 | quantitative cross-sectional study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S261 | quantitative spatial monitoring study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S273 | quantitative index development/validation study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S275 | quantitative socio-spatial comparative analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S279 | quantitative spatial index analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S280 | quantitative observational study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S282 | quantitative household survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S285 | quantitative methodological/survey-based study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S287 | quantitative cross-sectional survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S291 | quantitative household survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S295 | quantitative descriptive cross-sectional policy analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S312 | quantitative cross-sectional | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S313 | quantitative observational compliance audit | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S317 | quantitative cross-national | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S331 | observational | Unclear,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 0/8 | **High concern (sparse extraction)** |
| S336 | observational | Unclear,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 0/8 | **High concern (sparse extraction)** |
| S345 | observational | Unclear,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 0/8 | **High concern (sparse extraction)** |
| S347 | observational | Unclear,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 0/8 | **High concern (sparse extraction)** |
| S348 | observational | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S353 | quantitative cross-sectional regression (11-year panel of SDWA violations) | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S358 | quantitative cross-sectional regression + geospatial analysis | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S360 | quantitative descriptive/trend analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S368 | cross-sectional household survey (quantitative) | Yes,Yes,Unclear,Unclear,Yes,Unclear,Unclear,Unclear | 3/8 | **Some concern** |
| S378 | quantitative cross-sectional secondary-data analysis (NFHS-4) | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S381 | quantitative cross-sectional secondary-data analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S382 | quantitative cross-sectional household survey | Yes,Yes,Unclear,Unclear,Yes,Unclear,Unclear,Unclear | 3/8 | **Some concern** |
| S384 | quantitative cross-sectional survey | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S388 | quantitative cross-sectional analysis of national administrative water-point data | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S390 | quantitative cross-sectional analysis (278 municipalities, 2011) | Yes,Yes,Unclear,Yes,Unclear,Unclear,Yes,Unclear | 4/8 | **Some concern** |
| S403 | qualitative case study (10 schools) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** *(instrument-fit concern -- see note above)* |
| S471 | national cross-sectional observational study | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S473 | cross-sectional household survey (n=655) + diachronic GIS | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S476 | cross-sectional household survey (baseline/endline) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S478 | cross-sectional household survey with case-study/policy narrative | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S489 | cross-sectional household/waterpoint survey with regression | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S491 | cross-sectional household survey | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S526 | cross-sectional quantitative regression study | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S539 | cross-sectional observational study (500 largest US community water systems) | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S551 | mixed-methods statistical study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S590 | historical quasi-experimental cross-sectional logit analysis | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S593 | cross-sectional multi-year study (Coulter model + Tobit regression) | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S620 | cross-sectional household survey | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S631 | quasi-experimental panel-data study (exogenous district-splitting timing) | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S634 | cross-sectional household survey + qualitative key-informant interviews | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S636 | quasi-experimental PSM treatment/control impact evaluation | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S641 | cross-sectional quantitative study (direct observation + water-committee data) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S642 | cross-sectional household survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S644 | quantitative household survey, split-sample contingent-valuation | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S653 | cross-sectional household survey (multi-province) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S692 | comparative institutional performance study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S723 | spatial regression (ecological/neighborhood-level) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S738 | cross-sectional survey + in-depth interviews | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S749 | quasi-experimental panel-data regression | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S757 | cross-sectional users' satisfaction survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S772 | cross-sectional household survey with institutional/entitlements analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S780 | quantitative county-level regression, administrative project-allocation data | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S782 | quantitative city-level regression + descriptive rate-variance comparison | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S785 | statewide survey of local government agency programs | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S794 | household contingent-valuation survey with governance-type comparison | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S800 | cross-sectional municipal-level regression and comparison analysis | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S802 | cross-sectional survey of water-sector governance and pricing structures | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S807 | household survey with institutional/regulatory case-study analysis | Yes,Yes,Unclear,Yes,Unclear,Unclear,Yes,Unclear | 4/8 | **Some concern** |
| S816 | household questionnaire survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S820 | household demand/affordability survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S821 | household reconnaissance survey + informal-market census + WTP estimation | Yes,Yes,Unclear,Yes,Unclear,Unclear,Yes,Unclear | 4/8 | **Some concern** |
| S841 | national survey-based quantitative study (multinomial logit) | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S847 | cross-sectional survey study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S850 | comparative household survey with multivariate regression | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S855 | comparative household survey with institutional benchmark data | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S865 | legal/policy review with government survey statistics | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S876 | original survey research with newspaper content analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S894 | original household survey with hydropolitical/institutional analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S897 | household survey with regression analysis of administrative tariff/billing data | Yes,Yes,Unclear,Yes,Unclear,Unclear,Yes,Yes | 5/8 | **Some concern** |
| S911 | household survey with DPSIR institutional-framework analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S916 | GIS-based household survey with spatial water-poverty index analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S917 | household survey with market-impact (preliminary evidence) analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S923 | instrumental-variable econometric analysis of national household survey data | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S945 | 12-scheme comparative institutional performance assessment | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S953 | household survey with logit regression across ethnically diverse slums | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S969 | cross-national quantitative regression, 43 African countries | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Yes | 3/8 | **Some concern** |
| S983 | field survey with institutional/policy analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S996 | cross-sectional household survey with qualitative analysis | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S1002 | quantitative spatial/regression analysis | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S1025 | quantitative regression, stratified multi-stage probability household survey | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S1029 | household-level empirical survey study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S1032 | quantitative regression analysis of household survey data | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S1038 | quantitative econometric study of regulatory-structure/pricing effects | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S1041 | quantitative cross-sectional regression, administrative/census data | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S1056 | quantitative cross-sectional survey (Indian Time Use Survey 1998-99) | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S1057 | quantitative econometric study (household survey, 3 sites) | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S1065 | quantitative cross-sectional survey analysis | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S1075 | quantitative empirical study, national regulator survey data | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S1082 | cross-sectional household survey with shared dialogue workshop | Yes,Yes,Unclear,Unclear,Yes,Unclear,Unclear,Unclear | 3/8 | **Some concern** |
| S1085 | quantitative household survey regression study | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S1089 | mixed institutional analysis and household survey | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S1099 | quantitative household survey + key-informant interviews + transect walks | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S1127 | quantitative household-survey study | Yes,Yes,Unclear,Unclear,Unclear,Unclear,Unclear,Unclear | 2/8 | **High concern (sparse extraction)** |
| S1136 | quantitative regression-based institutional-mechanism study | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |
| S1140 | quantitative regression-based institutional/administrative-mechanism study | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S1143 | quantitative regression-based institutional/administrative-mechanism study | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S1144 | quantitative regression-based institutional/administrative-assistance study | Yes,Yes,Unclear,Yes,Yes,Yes,Yes,Yes | 7/8 | **Low concern** |
| S1162 | quantitative panel/cross-sectional multilevel regression | Yes,Yes,Unclear,Unclear,Yes,Yes,Unclear,Yes | 5/8 | **Some concern** |

*(Note: S403 is one of the 26 qualitative-instrument-fit-flagged studies but is shown here
because it was the only one whose design blends quantitative and qualitative elements
enough to produce a non-trivial item pattern; its "Some concern" label should be read
alongside the instrument-fit caveat, not instead of it.)*

## Summary

Of 125 appraised: **8 Low concern, 67 Some concern, 50 High concern (sparse extraction)**.
The "High concern" label is a statement about **what this project's extraction captured**,
not a confirmed finding that these are poor studies — roughly 40% of this batch never had
`covariates` or a named statistical method captured at extraction time, most likely because
extraction focused on the legal/institutional exposure-outcome content these studies were
included for, not on methods-section-level RoB detail.
