import csv, tempfile, os

EXTR = '/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv'

with open(EXTR) as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

def blank_row():
    return {k: "" for k in fieldnames}

r = blank_row()
r.update({
    'study_id': 'S539',
    'citation': 'Zhang X, Gonzalez Rivas M, Grant M, Warner ME (2022). "Water pricing and affordability in the US: public vs. private ownership." Water Policy, 24(3), 500-516.',
    'doi': '10.2166/wp.2022.283',
    'publication_year': '2022',
    'publication_type': 'journal article',
    'language': 'English',
    'peer_reviewed': 'TRUE',
    'country': 'United States',
    'subnational_unit': '48 states and the District of Columbia (500 largest community water systems)',
    'legal_system': 'common law',
    'urban_rural': 'urban (500 largest community water systems, serving ~140 million people, 44% of US population)',
    'service_provider': 'government-owned (321), cooperative (121), and investor-owned/private (58) community water systems',
    'regulatory_model': 'State Public Utility Commissions (PUCs) financially regulate all 58 private systems in the sample plus public systems in 6 states; "fair value" legislation (e.g., NJ Water Infrastructure Protection Act, PA Act 11 of 2012) allows private purchase of municipal systems at inflated valuations without public referendum and recovery of acquisition/wastewater costs through drinking-water rate increases; Distribution System Improvement Charges (DSIC) pass capital-improvement costs directly to ratepayers between formal rate cases.',
    'population': 'Households served by the 500 largest US community water systems, with focus on lowest-income-quintile households',
    'sample_size': '500 water systems (321 government-owned, 121 cooperative, 58 investor-owned), 321 counties',
    'household_level': 'TRUE',
    'community_level': 'TRUE',
    'income_group': 'lowest quintile of household income (focus of affordability outcome)',
    'tenure_status': '',
    'legal_status': '',
    'indigenous_population': '',
    'migrant_population': '',
    'eligibility': '',
    'burden': 'TRUE',
    'discretion_accommodation': 'TRUE',
    'enforcement': 'TRUE',
    'documentation': '',
    'tenure': '',
    'property': 'TRUE',
    'planning': '',
    'zoning': '',
    'building_permit': '',
    'service_area': 'TRUE',
    'fees': 'TRUE',
    'procedural_steps': '',
    'delay': '',
    'discretion': 'TRUE',
    'hardship_exception': 'TRUE',
    'administrative_review': 'TRUE',
    'complaint': '',
    'judicial_review': '',
    'disconnection': 'TRUE',
    'reconnection': '',
    'sanction': '',
    'participation': '',
    'institutional_fragmentation': 'TRUE',
    'political_coordination': 'TRUE',
    'bureaucratic_assistance': '',
    'formal_connection': '',
    'water_access': 'TRUE',
    'sanitation_access': '',
    'service_coverage': '',
    'service_reliability': '',
    'service_quantity': '',
    'service_quality': '',
    'affordability': 'TRUE',
    'service_continuity': 'TRUE',
    'application_success': '',
    'refusal': '',
    'delay_outcome': '',
    'effect_measure': 'OLS regression coefficient',
    'effect_estimate': 'Private ownership associated with a $144.04 higher annual water bill (std. coeff 0.35, p<0.01) and 1.55 percentage-point higher share of lowest-quintile household income spent on water (std. coeff 0.26, p<0.01), controlling for regulation, water supply, and community demographics. State regulation favorable to private providers (NJ/PA fair-value legislation and DSIC surcharges) associated with an additional $88.64 higher annual bill (p<0.01). PUC regulation of public utilities showed no significant effect on price or affordability. Poverty rate significantly associated with higher affordability burden (0.14, p<0.01) independent of ownership.',
    'lower_CI': '', 'upper_CI': '', 'standard_error': '', 'p_value': '<0.01 (private ownership effects); <0.01 (favorable private regulation effect)',
    'extraction_sample_size': '500',
    'adjusted_or_unadjusted': 'adjusted (PUC regulation of public utilities, favorable private regulation, service population, age of infrastructure, groundwater source, severe drought, Gini, poverty rate, percent minority, population density, population growth)',
    'covariates': 'PUC regulation of public utilities; favorable private regulation (NJ/PA); percent occupied houses built before 1940; groundwater source; severe drought %; Gini; poverty rate; percent minority; population density; population growth; service population',
    'model_type': 'OLS multiple regression (two models: annual water bill; percent of lowest-quintile income spent on water)',
    'study_design': 'cross-sectional observational study (500 largest US community water systems, 2015 data)',
    'risk_of_bias_tool': 'JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies',
    'risk_of_bias_rating': '',
    'selection_bias': '', 'measurement_bias': '', 'confounding': '', 'attrition': '', 'reporting_bias': '',
    'legal_measurement_quality': '', 'outcome_measurement_quality': '',
    'mechanism_certainty': '2',
    'source_document': 'Zhang et al 2022, Water Policy 24(3):500-516',
    'page': '', 'table': 'Table 2', 'figure': '', 'section': 'Results; Discussion',
    'exact_location': 'Table 2 (Regression results: differences in public and private water rates); Table 3 (state comparison)',
    'extraction_note': 'Extracted from full-text PDF (retrieved via Google Drive inbox). record_id RA0FB2C52085F.',
    'researcher': 'Claude-AI-fulltext-2026-09-21',
    'date_extracted': '2026-09-21',
    'evidence_status': 'OBSERVED',
})
rows.append(r)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, EXTR)
print('done, total rows now', len(rows))
