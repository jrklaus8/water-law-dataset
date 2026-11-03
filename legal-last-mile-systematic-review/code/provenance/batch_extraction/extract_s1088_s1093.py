#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


def blank_row(fieldnames):
    return {fn: "" for fn in fieldnames}


with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
new_rows = []

# S1088 -- Rajaraman, Travasso & Heymann 2013
r = blank_row(fieldnames)
r.update({
    "study_id": "S1088",
    "citation": "Rajaraman D, Travasso SM, Heymann SJ (2013). A qualitative study of access to sanitation amongst low-income working women in Bangalore, India. Journal of Water, Sanitation and Hygiene for Development 3(3):432-441.",
    "doi": "10.2166/washdev.2013.114",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Bangalore, Karnataka",
    "legal_system": "common law (India)",
    "urban_rural": "urban",
    "service_provider": "employers (construction sites, private homes, markets, factories)",
    "regulatory_model": "Factories Act (1948); Building and Other Construction Workers Act (1996)",
    "population": "low-income working women, four occupation groups",
    "sample_size": "48 women (12 per occupation group)",
    "household_level": "TRUE",
    "community_level": "",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "TRUE",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "descriptive frequency comparison by occupation group",
    "effect_estimate": "Access to a toilet at work: 0/12 construction workers, 2/12 domestic workers (despite 7/12 reporting nominal access), 8/12 street vendors (paid, 1-4 rupees per use), 9/12 factory workers (free). 23/48 women overall lacked workplace toilet access.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "48 women",
    "adjusted_or_unadjusted": "",
    "covariates": "occupation group (construction, domestic, street vending, factory)",
    "model_type": "",
    "study_design": "qualitative interview study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "High: documents that domestic workers have no legal protection requiring "
        "employer provision of sanitation access (no binding legislation covering "
        "domestic work), while the Factories Act (1948) and Building and Other "
        "Construction Workers Act (1996) legally mandate toilet provision for factory "
        "and construction employers respectively -- yet implementation is high in "
        "factories (9/12 with free access) and effectively non-existent on construction "
        "sites (0/12 with access), demonstrating that legal coverage alone does not "
        "guarantee access absent enforcement, while its complete absence (domestic work) "
        "produces near-total exclusion."
    ),
    "source_document": "Rajaraman, Travasso & Heymann 2013 (retrieved via Google Drive)",
    "page": "432-441",
    "table": "Table 1-2",
    "figure": "",
    "section": "Results: Access to sanitation at the workplace",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal mechanism study "
        "documenting how presence or absence of labour-law coverage produces differential "
        "workplace sanitation access by occupation/employment-sector. Qualitative "
        "interview study, descriptive frequencies only; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1089 -- Javed & Farhan 2020
r = blank_row(fieldnames)
r.update({
    "study_id": "S1089",
    "citation": "Javed N, Farhan K (2020). Access to urban services for political and social inclusion in Pakistan. In: Urban Book Series, Springer, Ch. 10.",
    "doi": "10.1007/978-981-15-2973-3_10",
    "publication_year": "2020",
    "publication_type": "book chapter",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Pakistan",
    "subnational_unit": "Lahore (Punjab), Peshawar (Khyber Pakhtunkhwa)",
    "legal_system": "common law (Pakistan)",
    "urban_rural": "urban",
    "service_provider": "provincial/local government water and sanitation agencies (e.g., WASA); NGOs",
    "regulatory_model": "Local Government Ordinance 2001 / Local Government Act (provincial), decentralized governance",
    "population": "low-income slum/squatter settlement residents",
    "sample_size": "household survey, two low-income settlements (Kotli Ghazi, Lahore; Ganj Bazar, Peshawar)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "descriptive survey percentages",
    "effect_estimate": "52% of surveyed low-income households had access to safe drinking water, 42% to community-level sanitation/waste disposal. Service delivery ranged 62.5-87.5% across services in Lahore vs. 22.5-65.0% in Peshawar. Badar Colony case: NGO contributed 38% of capital investment to extend water/sewerage to ~3,000 households, achieving 98% billing compliance after 8 years.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "household survey, two low-income settlements",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "mixed institutional analysis and household survey",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: documents institutional fragmentation between provincial and local "
        "government under Pakistan's decentralization framework limiting municipal "
        "capacity to extend water/sanitation services, alongside the Badar Colony case in "
        "which an NGO formed by residents contributed 38% of capital investment and "
        "entered a bulk-purchase/distribution agreement with the city utility (WASA) "
        "after the utility had no funds for service extension to the area -- an "
        "institutional partnership model directly substituting for formal utility "
        "extension."
    ),
    "source_document": "Javed & Farhan 2020 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Household survey findings; Badar Colony case study",
    "exact_location": "Sections 2-3",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal mechanism study "
        "of decentralized governance structure and NGO-utility partnership models "
        "directly affecting water-service access. NOT added to effect_sizes.csv: "
        "descriptive survey percentages only, water access bundled with several other "
        "urban services, no regression-based effect size."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1090 -- Colbran 2017
r = blank_row(fieldnames)
r.update({
    "study_id": "S1090",
    "citation": "Colbran N (2017). Piped Water in Jakarta: A Political, Economic or Social Good? In: Human Rights, Human Dignity, and Cormorant Autonomous Conduct, Cambridge University Press, Ch. 14.",
    "doi": "10.1017/9780511862601.016",
    "publication_year": "2017",
    "publication_type": "book chapter",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Indonesia",
    "subnational_unit": "Jakarta",
    "legal_system": "civil law (Indonesia)",
    "urban_rural": "urban",
    "service_provider": "PAM Jaya; private concessionaires (Palyja, Aetra/TPJ)",
    "regulatory_model": "Water Resources Law No. 7/2004; Jakarta Water Supply Regulatory Body (JWSRB/ETOSS-equivalent)",
    "population": "low-income and informal-settlement residents, Jakarta",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "TRUE",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "TRUE",
    "complaint": "TRUE",
    "judicial_review": "TRUE",
    "disconnection": "TRUE",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "TRUE",
    "effect_measure": "",
    "effect_estimate": "Less than one-third of Jakarta's ~12 million residents have in-home piped water access; only ~25% when informal households are included. Water tariffs for low-income households rose 63% in 2005 vs. under 11% for upper-income/commercial. 2004 Central Jakarta District Court suspended a 40% tariff increase pending service improvements.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "legal-historical case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "High: documents that 'the government has put in place legal obstacles that mean "
        "many of the city's lowest income residents do not qualify for household water "
        "supply services,' motivated by a political goal of discouraging migration to "
        "Jakarta and removing informal settlements; combined with a per-connection "
        "payment structure that incentivizes concessionaires to prioritize wealthier "
        "neighborhoods, disproportionate tariff increases for low-income customer groups "
        "(63% vs. under 11%), and changing/tightening eligibility criteria for the "
        "lower-tariff customer group (e.g., building-size threshold lowered without "
        "notifying customers)."
    ),
    "source_document": "Colbran 2017 (retrieved via Google Drive)",
    "page": "503-",
    "table": "",
    "figure": "",
    "section": "Sections 2-4",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous legal/institutional mechanism study "
        "directly documenting formal eligibility barriers and discriminatory tariff "
        "structures excluding the urban poor from formal water-service access. Legal-"
        "historical case study, no regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1091 -- Mukherjee, Kumar, Cardosi & Singh 2009
r = blank_row(fieldnames)
r.update({
    "study_id": "S1091",
    "citation": "Mukherjee N, Kumar A, Cardosi J, Singh U (2009). What does it take to scale up and sustain rural sanitation beyond projects? Waterlines 28(4):293-310.",
    "doi": "10.3362/1756-3488.2009.030",
    "publication_year": "2009",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India, Indonesia, Tanzania",
    "subnational_unit": "Himachal Pradesh, Madhya Pradesh (India); East Java (Indonesia); 10 districts (Tanzania)",
    "legal_system": "mixed (multi-country)",
    "urban_rural": "rural",
    "service_provider": "national/district governments; Water and Sanitation Program (WSP)",
    "regulatory_model": "Total Sanitation and Sanitation Marketing (TSSM) 'enabling environment' framework",
    "population": "rural households, three countries",
    "sample_size": "4.45 million people targeted for access by 2010 across project sites",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "TSSM project targeted 4.45 million additional people gaining sanitation access by 2010, with 37.7 million more envisaged by 2015 across three countries. Indonesia's 21 TSSM districts increased sanitation budgets 20-500% over pre-TSSM (2006) levels.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "programme-evaluation case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: documents an eight-dimension 'enabling environment' framework (policy, "
        "institutional arrangements, programme methodology, implementation capacity, "
        "product/tool availability, financing, cost-effective implementation, monitoring) "
        "used to track institutional and policy determinants of sustainable rural "
        "sanitation scale-up, including Indonesia's 2008 national strategy that "
        "explicitly forbids household sanitation subsidies, and measurable increases in "
        "district-level sanitation budget allocations following institutional reform."
    ),
    "source_document": "Mukherjee et al. 2009 (retrieved via Google Drive)",
    "page": "293-310",
    "table": "Table 1",
    "figure": "Figures 1-3",
    "section": "The Total Sanitation and Sanitation Marketing (TSSM) Project; Lessons",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/policy mechanism study "
        "directly examining the policy and financing environment enabling or constraining "
        "rural sanitation-access scale-up. Programme-evaluation case study, no regression-"
        "based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1092 -- Singh, Upadhyay & Mittal 2005
r = blank_row(fieldnames)
r.update({
    "study_id": "S1092",
    "citation": "Singh MR, Upadhyay V, Mittal AK (2005). Water Tariff Structure and Reform Needs for Socio-Economic Sustainability in India. ASCE EWRI 2005 Impacts of Global Climate Change.",
    "doi": "",
    "publication_year": "2005",
    "publication_type": "conference paper",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "national (multiple cities: Mumbai, Bangalore, Chennai, Hyderabad, Delhi, Guntur)",
    "legal_system": "common law (India)",
    "urban_rural": "urban",
    "service_provider": "urban local bodies (ULBs), municipal water utilities",
    "regulatory_model": "municipal water tariff structures, connection-charge policy",
    "population": "urban households, India, particularly unconnected poor",
    "sample_size": "NIUA survey of 260 urban centers",
    "household_level": "TRUE",
    "community_level": "",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "TRUE",
    "tenure": "",
    "property": "TRUE",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
    "hardship_exception": "TRUE",
    "administrative_review": "",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "TRUE",
    "reconnection": "",
    "sanction": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "Connection charges range up to Rs. 12,000 (domestic) and Rs. 42,000 (commercial) in Guntur, Andhra Pradesh. ~50% of the Indian poor population remains unconnected to the piped water system, spending 5-10% of monthly income on water from other sources, paying more than 10x per cubic metre relative to connected households via private vendors. Only 3% of overall water-sector costs are covered by user charges.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "260 urban centers (NIUA survey)",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "policy-analysis study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "High: documents that connection charges are 'a major obstacle for the poor "
        "households in getting connection to water supply systems,' with substantial "
        "variation across cities and no clear or transparent basis, and that "
        "unconnected poor households -- roughly half of India's poor population -- pay "
        "far more per unit of water from informal vendors than connected households pay "
        "through subsidized tariffs, meaning existing subsidy schemes systematically "
        "bypass the very population they are intended to help."
    ),
    "source_document": "Singh, Upadhyay & Mittal 2005 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Subsidies and Problems; Reform Needs",
    "exact_location": "Sections 2.5, 3.3",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal mechanism study "
        "directly examining connection-fee and tariff-structure barriers to formal water-"
        "service access for the poor in India. Policy-analysis paper citing survey "
        "statistics, no original regression; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1093 -- Loftus & McDonald 2001
r = blank_row(fieldnames)
r.update({
    "study_id": "S1093",
    "citation": "Loftus AJ, McDonald DA (2001). Of Liquid Dreams: A Political Ecology of Water Privatization in Buenos Aires. Environment and Urbanization 13(2):179-199.",
    "doi": "",
    "publication_year": "2001",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Argentina",
    "subnational_unit": "Buenos Aires (federal capital and 17 surrounding municipalities)",
    "legal_system": "civil law (Argentina)",
    "urban_rural": "urban",
    "service_provider": "Aguas Argentinas (private concessionaire)",
    "regulatory_model": "1993 water/sanitation privatization concession; ETOSS regulatory agency",
    "population": "low-income newly-connecting households, Buenos Aires",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "",
    "property": "TRUE",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "TRUE",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "TRUE",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "TRUE",
    "effect_measure": "",
    "effect_estimate": "Water coverage rose from 70% (1993) to 82.4% (1999); sewerage coverage from 58% to 61%, missing the contracted 64% target. Infrastructure charge for newly-connected households: US$43-600 (water), up to US$1,000 (sewerage). 1998 tariff dispute: company sought 11.7%, regulator ETOSS proposed 1.6%, national government imposed 4.6%. Further 15% increase granted for 2001-2003.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "critical political-ecology case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "High: documents a regressive 'infrastructure charge' (US$43-600 for water, up to "
        "US$1,000 for sewerage) levied specifically on newly-connecting households -- "
        "disproportionately the poor, who were more likely to lack a prior connection -- "
        "plus an additional 'OPCT' connection-acceleration charge that in practice "
        "delayed connections until paid (described by a public hearing submitter as a "
        "'subversive' infrastructure charge), documented disconnections of poor "
        "households in payment arrears, and repeated national-government intervention "
        "overriding the independent regulator (ETOSS) to grant the concessionaire tariff "
        "increases beyond what the regulator itself approved."
    ),
    "source_document": "Loftus & McDonald 2001 (retrieved via Google Drive)",
    "page": "179-199",
    "table": "Table 2-3",
    "figure": "",
    "section": "The crisis of the infrastructure charge; Disconnections",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/regulatory mechanism "
        "study directly documenting connection-fee and regulatory-capture barriers to "
        "affordable formal water-service access for the urban poor. Critical political-"
        "ecology case study, no regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
