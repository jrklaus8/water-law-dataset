import csv, tempfile, os

EM = '/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv'
ES = '/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv'

with open(EM) as f:
    reader = csv.DictReader(f)
    em_fieldnames = reader.fieldnames
    em_rows = list(reader)

em_row = {k: '' for k in em_fieldnames}
em_row.update({
    'study_id': 'S539',
    'study_design_class': 'observational',
    'evidence_level': 'Cross-sectional OLS regression across the 500 largest US community water systems (2015 data), controlling for regulatory, water-supply, and community-demographic confounders. JBI Analytical Cross Sectional rating deferred pending the official instrument; provisional confidence: high -- national near-census sample of large utilities, clear exposure/comparator definition, multiple robustness controls, consistent with prior literature.',
    'mechanism_family': 'MULTIPLE',
    'outcome_family': 'economic_access',
    'quantitative_synthesis_eligible': 'TRUE',
    'qualitative_synthesis_eligible': 'FALSE',
    'legal_context': 'common law',
    'institutional_context': 'State Public Utility Commissions regulate private water utility rates via cost-of-service ratemaking; "fair value" legislation (NJ Water Infrastructure Protection Act, PA Act 11 of 2012) enables private acquisition of municipal systems at inflated valuations recoverable through rates, and Distribution System Improvement Charge (DSIC) surcharges pass capital costs to ratepayers between formal rate cases -- both associated with significantly higher household water bills and reduced affordability for low-income households.',
})
em_rows.append(em_row)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=em_fieldnames)
    writer.writeheader()
    writer.writerows(em_rows)
os.replace(tmp, EM)

with open(ES) as f:
    reader = csv.DictReader(f)
    es_fieldnames = reader.fieldnames
    es_rows = list(reader)

es_row = {k: '' for k in es_fieldnames}
es_row.update({
    'study_id': 'S539',
    'outcome_family': 'economic_access',
    'synthesis_family': 'C',
    'exposure_definition': 'Investor-owned (private) community water utility, with rates set via state Public Utility Commission cost-of-service regulation and, in some states, "fair value" legislation and Distribution System Improvement Charge surcharges favorable to private capital recovery.',
    'comparator_definition': 'Government-owned or cooperative-owned community water utility (reference category), n=442 of 500 utilities.',
    'effect_measure': 'OLS regression coefficient',
    'effect_estimate': 'Private ownership associated with a $144.04 higher annual household water bill (std. coeff 0.35, p<0.01) and a 1.55 percentage-point higher share of lowest-quintile household income spent on water (std. coeff 0.26, p<0.01). Separately, state regulation favorable to private providers (NJ/PA fair-value legislation and DSIC surcharges) associated with an additional $88.64 higher annual bill (p<0.01), with no significant effect on the affordability-share outcome.',
    'lower_CI': '',
    'upper_CI': '',
    'standard_error': '',
    'sample_size': '500',
    'direction': 'positive (private ownership and pro-private regulation associated with higher price and lower affordability)',
    'adjusted': 'adjusted (PUC regulation of public utilities, favorable private regulation, age of infrastructure, groundwater source, severe drought, Gini, poverty rate, percent minority, population density, population growth, service population)',
    'evidence_status': 'OBSERVED',
    'provenance_note': 'extraction_database.csv S539; source Zhang, Gonzalez Rivas, Grant & Warner 2022, Water Policy 24(3):500-516, Table 2 (OLS regression results, annual water bill and percent-of-income models).',
    'included_in_pooled_estimate': 'FALSE',
    'exclusion_from_pooling_reason': 'ANALYSIS_PLAN.md S2 -- single study defining this exact private-vs-public-ownership/regulatory-favorability exposure and dollar-bill/income-share outcome operationalization; no other Family C study yet shares a convertible estimand, so pooling is not yet possible or meaningful.',
})
es_rows.append(es_row)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ES))
with os.fdopen(fd, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=es_fieldnames)
    writer.writeheader()
    writer.writerows(es_rows)
os.replace(tmp, ES)

print('evidence_map rows now', len(em_rows), 'effect_sizes rows now', len(es_rows))
