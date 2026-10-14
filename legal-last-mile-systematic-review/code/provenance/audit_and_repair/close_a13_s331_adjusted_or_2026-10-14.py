"""2026-10-14 (open item A13, PI ruling under reviewer CK): S331 (Sarfo 2025, PhD dissertation, Kent State University; record RFFE690159838).

The full PDF in the researcher's Drive was read again for the adjusted model (Table 4, p. 64, and the adjusted-results text, pp. 63-65): point-of-sale (POS) versus non-POS onsite-sewage-system inspection,
odds of correcting a failed system within the 120-day notice-of-violation deadline, multivariable logistic regression, n = 938: adjusted OR 4.27 (95% CI 3.07-5.93, p < 0.0001); unadjusted OR 7.225
(5.389-9.686, Table 3). Covariates: type of new OWTS (alternative, sewer, versus traditional), repair versus replacement, correction cost per $1,000, age of the faulty system in 10-year units.

Changes (all idempotent, each guarded by a marker):
1. extraction_database.csv, S331: effect_estimate, lower_CI, upper_CI, p_value, extraction_sample_size, adjusted_or_unadjusted, page, table, exact_location, section, confounding, risk_of_bias_rating (item 6 re-answered
   from Yes to Unclear, 7/8 Yes, still Low concern under the project's >= 6/8 rule) and extraction_note (the unadjusted OR stays in the note).
2. effect_sizes.csv: one new row, S331, synthesis_family BLANK = reasoned non-fit. ANALYSIS_PLAN.md section 2: the estimand is a regulatory-compliance outcome (does an owner correct a failed onsite sewage system within
   a notice deadline), not household access; PROJECT_SPEC.md section 8 Family C is about barriers and access inequality, connection probability and service quality or reliability. The same ruling was applied to the
   regulatory-compliance outcomes of S178 (Water Safety Plan compliance) and S353 (SDWA violations). Row count 59 to 60; Families A 18, B 6, C 20 unchanged; non-fits 15 to 16. No SWiM family table changes.
3. FULLTEXT_VERIFICATION_2026-10-04.csv: one row for S331 (verified against the full text).
4. evidence_map.csv, S331: quantitative_synthesis_eligible FALSE to TRUE (every effect row must come from an eligible study; the flag was FALSE only because no effect row existed) and evidence_level refreshed.

Run from legal-last-mile-systematic-review/."""
import csv
import os
import sys
import tempfile

csv.field_size_limit(sys.maxsize)

ED = '03_extraction/extracted_data/extraction_database.csv'
ES = '05_analysis/effect_sizes/effect_sizes.csv'
VF = '05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
MARK = 'A13 2026-10-14'


def load(p):
    raw = open(p, newline='', encoding='utf-8').read()
    crlf = '\r\n' in raw[:20000]
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), crlf


def save(p, fields, rows, crlf):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n')
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, p)


# ---- 1. extraction row -------------------------------------------------------------------------------------------------------------------------------------------------------------------
fields, rows, crlf = load(ED)
n0 = len(rows)
r = next(x for x in rows if x['study_id'] == 'S331')
if MARK in r['extraction_note']:
    print('extraction row already updated')
else:
    assert r['record_id'] == 'RFFE690159838' and r['lower_CI'] == '5.389' and r['upper_CI'] == '9.686'
    r['effect_estimate'] = ('Adjusted OR 4.27 (95% CI 3.07-5.93, p < 0.0001; Table 4, multivariable logistic regression, n = 938): failed onsite sewage systems found at a point-of-sale (POS) inspection were '
                            '4.27 times as likely to be corrected within the 120-day notice-of-violation deadline as those found at a non-POS inspection. The covariates are type of new system, repair versus '
                            'replacement, correction cost per $1,000 and age of the system.')
    r['lower_CI'], r['upper_CI'], r['p_value'] = '3.07', '5.93', '<0.0001'
    r['extraction_sample_size'] = '938 (complete cases in the adjusted logistic model)'
    r['adjusted_or_unadjusted'] = ('adjusted OR entered (Table 4, 2026-10-14); the unadjusted OR 7.225 (95% CI 5.389-9.686, p < 0.0001, Table 3) is kept in extraction_note')
    r['table'] = 'Table 4 (adjusted logistic model, p. 64); Table 3 (unadjusted logistic models, p. 58-59)'
    r['page'] = '8, 30-31, 40-49, 54-65'
    r['exact_location'] = ('Research question p8; Methods p30-31; sample flow p40-41 (Figure 4); variables and model equations p44-49; results p54-59 (unadjusted OR p59); adjusted model p63-65 (Table 4 p64)')
    r['section'] = 'Full text (dissertation, Ch.1-4): Research Question and Hypothesis; Methods and variables; Descriptive, unadjusted and adjusted logistic results'
    r['confounding'] = ('Moderate (four covariates modelled: type of new system, repair versus replacement, correction cost, system age; the odds ratio fell from 7.2 to 4.27 on adjustment, so confounding matters here; '
                        'these covariates describe the correction that follows the inspection and are partly post-exposure, owner, property and area characteristics were not modelled, and POS is a self-selected pathway)')
    old_rating = r['risk_of_bias_rating']
    assert old_rating.startswith('Low concern (appraised 2026-10-04 on the full text, partly read;') and 'Yes,Yes,Yes,Yes,Yes,Yes,Yes,Yes; 8/8 Yes' in old_rating
    r['risk_of_bias_rating'] = (
        'Low concern (re-appraised 2026-10-14 on the full text, adjusted model read; supersedes the 2026-10-04 appraisal made before the adjusted results were seen; '
        'JBI Cross Sectional items 1-8: Yes,Yes,Yes,Yes,Yes,Unclear,Yes,Yes; 7/8 Yes, still Low concern under the project\'s >= 6/8 rule). '
        'Basis: inclusion criteria by date, complete data and failed-system status; setting described (county health district); POS vs non-POS context recorded in the district database; objective 120-day NOV deadline; '
        'four named confounders identified and modelled (Table 4); logistic regression with ORs and CIs. Item 6 is now Unclear rather than Yes: the modelled covariates (type of new system, repair versus replacement, cost, system age) '
        'describe the correction that follows the inspection and are partly post-exposure, so they do not deal with confounding of the POS contrast by owner, property or area characteristics. '
        'Caveats: single county, administrative records, POS is a self-selected pathway (sales trigger the inspection), the odds ratio fell from 7.2 to 4.27 on adjustment, and the dissertation reports no sensitivity analysis.')
    r['extraction_note'] = (
        f'{MARK} (PI ruling, reviewer CK): the adjusted model was read in the full PDF (Table 4 and the adjusted-results text, pp. 63-65) and entered above. The unadjusted OR 7.225 (95% CI 5.389-9.686, p < 0.0001; Table 3) is kept here for the record. '
        'The row was added to effect_sizes.csv as a reasoned non-fit (the outcome is compliance with a notice deadline, not household access; the same reading as S178 and S353) and quantitative_synthesis_eligible was set TRUE in evidence_map.csv. '
        'Earlier note: re-extracted 2026-10-04 from the full-text PDF in the researcher\'s Drive (PhD dissertation, Kent State University, 2025; about 135,000 characters read at the time; the Drive reader had not returned the adjusted results); '
        'supersedes the abstract-only extraction. Flags not removed; flags added only where the text supports them. record_id RFFE690159838.')
    r['researcher'] = r['researcher'] + '; adjusted model entered 2026-10-14 (A13)'
    print('extraction row S331 updated')
assert len(rows) == n0
save(ED, fields, rows, crlf)

# ---- 2. effect_sizes row ---------------------------------------------------------------------------------------------------------------------------------------------------------------
fields, rows, crlf = load(ES)
if any(x['study_id'] == 'S331' for x in rows):
    print('effect row already present')
else:
    rows.append({
        'study_id': 'S331', 'outcome_family': 'administrative_outcome', 'synthesis_family': '',
        'exposure_definition': ('Onsite wastewater treatment system (OWTS) inspection carried out as a point-of-sale (POS) inspection tied to a property transfer (Portage County Health District, Ohio; a county '
                                'point-of-sale inspection requirement), against a failed system found at a non-POS inspection.'),
        'comparator_definition': ('Failed OWTS found at non-POS inspections (annual evaluations, nuisance complaints, newly installed systems and stormwater illicit-discharge inspections), '
                                  'with type of new OWTS, repair versus replacement, correction cost and system age held constant.'),
        'effect_measure': 'Odds ratio (multivariable logistic regression, Table 4)', 'effect_estimate': '4.27', 'lower_CI': '3.07', 'upper_CI': '5.93', 'standard_error': '',
        'sample_size': '938 complete cases (1,021 failed systems analysed descriptively: 487 POS, 534 non-POS); Portage County, Ohio, inspections January 2015 to June 2023',
        'direction': 'positive (failed systems found at a POS inspection are more likely to be corrected within the 120-day notice period)',
        'adjusted': 'adjusted (type of new OWTS, repair versus replacement, correction cost per $1,000, system age in 10-year units)',
        'evidence_status': 'OBSERVED',
        'provenance_note': ('extraction_database.csv S331; source Sarfo 2025, PhD dissertation, Kent State University, Table 4 (p. 64; the text gives OR = 4.269, 95% CI 3.073-5.931). Added 2026-10-14 by the PI\'s ruling on open item A13. '
                            'The unadjusted OR 7.225 (95% CI 5.389-9.686) is in extraction_note, not here. The outcome is compliance with a regulatory deadline after a notice of violation, a result of enforcement, not household access.'),
        'included_in_pooled_estimate': 'FALSE',
        'exclusion_from_pooling_reason': ('ANALYSIS_PLAN.md section 2 decision tree and PROJECT_SPEC.md section 8: reasoned non-fit, no family assigned. The estimand is whether an owner corrects a failed onsite sewage system within a notice '
                                          'deadline (a regulatory-compliance outcome), not household connection, access or service quality, so it does not match Family A, B or C; the same reading was applied to S178 (Water Safety Plan compliance) '
                                          'and S353 (Safe Drinking Water Act violations). It is a single study with this exposure (a point-of-sale inspection trigger) and this outcome, so pooling is not possible.')})
    print('effect row S331 added')
save(ES, fields, rows, crlf)

# ---- 3. verification row ---------------------------------------------------------------------------------------------------------------------------------------------------------------
fields, rows, crlf = load(VF)
if any(x['study_id'] == 'S331' for x in rows):
    print('verification row already present')
else:
    rows.append({'study_id': 'S331', 'synthesis_family': '', 'numbers_in_row': '6', 'numbers_found_in_text': '6', 'numbers_not_found': '',
                 'source_text': 'Drive full text (2026-10-14; Table 4 p. 64 and the adjusted-results text pp. 63-65)', 'verdict': 'verified',
                 'note': ('Table 4: POS inspection OR 4.27 (95% CI 3.07-5.93), p < 0.0001, n = 938; the text states OR = 4.269 (3.073-5.931) and the 120-day deadline; the unadjusted OR 7.225 (5.389-9.686) is Table 3; '
                          'direction (POS more likely to comply) consistent; covariates are type of new OWTS, repair versus replacement, cost per $1,000 and age in 10-year units')})
    print('verification row added')
save(VF, fields, rows, crlf)

# ---- 4. evidence map -------------------------------------------------------------------------------------------------------------------------------------------------------------------
fields, rows, crlf = load(EM)
r = next(x for x in rows if x['study_id'] == 'S331')
if r['quantitative_synthesis_eligible'] == 'TRUE':
    print('evidence map already updated')
else:
    assert r['quantitative_synthesis_eligible'] == 'FALSE'
    r['quantitative_synthesis_eligible'] = 'TRUE'
    r['evidence_level'] = ('Single-study evidence: a retrospective cross-sectional analysis (PhD dissertation) of Portage County, Ohio, inspection records, read in full text on 2026-10-04 and again for the adjusted model on 2026-10-14. '
                           'A point-of-sale inspection triggered by a real-estate transfer is associated with higher odds of correcting a failed onsite sewage system within the 120-day notice (adjusted OR 4.27, 95% CI 3.07-5.93, n = 938; '
                           'unadjusted OR 7.2, CI 5.4-9.7). A single county, administrative data, a self-selected pathway; a compliance outcome, so a reasoned non-fit for Families A to C.')
    print('evidence map S331 updated')
save(EM, fields, rows, crlf)
