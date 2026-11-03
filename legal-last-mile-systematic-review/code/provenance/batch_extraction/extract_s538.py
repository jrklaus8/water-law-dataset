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
    'study_id': 'S538',
    'citation': 'Dallasheh L (2022). "Would the United States Come to Nazareth\'s Aid? Local and International Contests over the City\'s Water." Journal of Palestine Studies, 51(4), 24-44.',
    'doi': '10.1080/0377919X.2022.2131458',
    'publication_year': '2022',
    'publication_type': 'journal article',
    'language': 'English',
    'peer_reviewed': 'TRUE',
    'country': 'Israel',
    'subnational_unit': 'Nazareth, Galilee',
    'legal_system': 'common law (mixed, Mandate-era ordinance carried into Israeli military-rule administrative structure)',
    'urban_rural': 'urban',
    'service_provider': 'Nazareth Municipality (contested) vs. Mekorot (Israeli national/quasi-official water utility)',
    'regulatory_model': 'Water infrastructure decision-making formally vested in the Nazareth municipal council under the Mandate-era Municipal Corporations Ordinance of 1934, but subordinated in practice to Israeli military-government authorization requirements (1948-1966 martial law) for every plan, budget, equipment import, and foreign-currency allocation; Mekorot, a quasi-official national water utility, ultimately gained control of the municipality-owned well as a precondition of connecting the city to the national grid (1955), and later used a 1966 debt-collection water-supply cutoff as political leverage against the elected mayor.',
    'population': 'Palestinian residents of Nazareth (Arab citizens of Israel post-1948)',
    'sample_size': '',
    'household_level': 'TRUE',
    'community_level': 'TRUE',
    'income_group': '',
    'tenure_status': '',
    'legal_status': 'TRUE',
    'indigenous_population': 'TRUE',
    'migrant_population': '',
    'eligibility': '',
    'burden': 'TRUE',
    'discretion_accommodation': 'TRUE',
    'enforcement': 'TRUE',
    'documentation': '',
    'tenure': '',
    'property': 'TRUE',
    'planning': 'TRUE',
    'zoning': '',
    'building_permit': '',
    'service_area': 'TRUE',
    'fees': 'TRUE',
    'procedural_steps': 'TRUE',
    'delay': 'TRUE',
    'discretion': 'TRUE',
    'hardship_exception': '',
    'administrative_review': '',
    'complaint': '',
    'judicial_review': '',
    'disconnection': 'TRUE',
    'reconnection': '',
    'sanction': 'TRUE',
    'participation': 'TRUE',
    'institutional_fragmentation': 'TRUE',
    'political_coordination': 'TRUE',
    'bureaucratic_assistance': '',
    'formal_connection': 'TRUE',
    'water_access': 'TRUE',
    'sanitation_access': '',
    'service_coverage': 'TRUE',
    'service_reliability': 'TRUE',
    'service_quantity': 'TRUE',
    'service_quality': 'TRUE',
    'affordability': 'TRUE',
    'service_continuity': 'TRUE',
    'application_success': '',
    'refusal': 'TRUE',
    'delay_outcome': 'TRUE',
    'effect_measure': 'Archival historical case-study narrative (no statistical contrast)',
    'effect_estimate': 'Under Israeli military rule (1948-1966), Nazareth\'s elected municipal council needed official authorization for every water-infrastructure decision -- funding, equipment import, and foreign-currency allocation -- despite formally retaining Mandate-era Municipal Corporations Ordinance authority over its own water supply. The city suffered chronic water shortages (water trickling only a few days per month in crisis periods), forcing residents to rely on costly tanker deliveries and contested access at Mary\'s Well. The municipality\'s 7-year campaign (1948-1955) to retain ownership of its independently drilled well, including an appeal to the US Point Four aid program, ultimately failed: in 1955 Mekorot secured control of the well as a precondition of connection to the national grid. In 1966, Mekorot cut off Nazareth\'s entire water supply over an unpaid municipal water debt, used explicitly as a political tool to force the resignation of an elected mayor backed by a Communist-Mapam coalition.',
    'lower_CI': '', 'upper_CI': '', 'standard_error': '', 'p_value': '',
    'extraction_sample_size': '',
    'adjusted_or_unadjusted': '',
    'covariates': '',
    'model_type': 'historical archival case study',
    'study_design': 'historical archival case study (primary-source archival research: Israeli State Archives, Nazareth Municipal Archives, US National Archives, Knesset records, contemporary press)',
    'risk_of_bias_tool': 'Legal Institutional Evidence Appraisal Framework',
    'risk_of_bias_rating': '',
    'selection_bias': '', 'measurement_bias': '', 'confounding': '', 'attrition': '', 'reporting_bias': '',
    'legal_measurement_quality': '', 'outcome_measurement_quality': '',
    'mechanism_certainty': '2',
    'source_document': 'Dallasheh 2022, Journal of Palestine Studies 51(4):24-44',
    'page': '', 'table': '', 'figure': '', 'section': '',
    'exact_location': '"Water Infrastructure, Water Troubles" and "Might the United States Be Able to Help?" sections; epilogue on the 1966 Mekorot cutoff',
    'extraction_note': 'Extracted from full-text PDF (retrieved via Google Drive inbox). record_id R0482B6E724C6.',
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
