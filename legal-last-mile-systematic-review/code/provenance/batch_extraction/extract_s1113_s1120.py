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

# S1113 -- Narzetti & Marques 2021
r = blank_row(fieldnames)
r.update({
    "study_id": "S1113",
    "citation": "Narzetti DA, Marques RC (2021). Access to Water and Sanitation Services in Brazilian Vulnerable Areas: The Role of Regulation and Recent Institutional Reform. Water 13(6):787.",
    "doi": "10.3390/w13060787",
    "publication_year": "2021",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Brazil",
    "subnational_unit": "national (multiple vulnerable/slum areas)",
    "legal_system": "civil law (Brazil); Lei 14.026/2020 (new legal sanitation framework)",
    "urban_rural": "mixed",
    "service_provider": "municipal/state water and sanitation utilities under regulatory contracts",
    "regulatory_model": "recent institutional/regulatory reform (2020) of Brazil's water/sanitation sector",
    "population": "poor/vulnerable populations and informal settlements, Brazil",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "TRUE",
    "property": "",
    "planning": "",
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
    "participation": "",
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
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Slums and other informal settlements are typically excluded from urban-area "
        "statistics on water/sanitation coverage ('nobody's land'); public authorities "
        "have not proactively addressed regulation of service provision to vulnerable "
        "areas. Regulatory/institutional reform is identified as necessary for "
        "universalization of access under Brazil's 2020 sanitation legal framework."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "institutional/regulatory case study",
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
        "Moderate-high: documents that formal urban-area statistics and regulatory "
        "coverage systematically exclude informal settlements from water/sanitation "
        "service assessment and provision planning, and that Brazil's 2020 institutional "
        "reform requires a more proactive regulatory role to achieve universalization for "
        "vulnerable areas."
    ),
    "source_document": "Narzetti & Marques 2021 (retrieved via Google Drive)",
    "page": "1-14",
    "table": "",
    "figure": "",
    "section": "Introduction; Discussion",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/regulatory-mechanism "
        "case study documenting regulatory-framework effects on vulnerable-area water/"
        "sanitation access. No regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1114 -- Safari et al 2019
r = blank_row(fieldnames)
r.update({
    "study_id": "S1114",
    "citation": "Safari J, Mohamed H, Dimoso P, Akyoo W, Odhiambo F, Mpete R, Massa K, Mwakitalima A (2019). Lessons learned from the national sanitation campaign in Njombe district council, Tanzania. Journal of Water, Sanitation and Hygiene for Development.",
    "doi": "10.2166/washdev.2019.274",
    "publication_year": "2019",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Tanzania",
    "subnational_unit": "Njombe District Council",
    "legal_system": "civil law (Tanzania); local government WASH by-laws",
    "urban_rural": "rural",
    "service_provider": "local government (village/district councils)",
    "regulatory_model": "Community-Led Total Sanitation (CLTS) with local WASH by-law enforcement",
    "population": "rural households, Njombe District Council, Tanzania",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "",
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
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Household improved-latrine coverage increased from 7.5% before intervention "
        "(2011) to 99.8% by September 2018; functional handwashing facilities increased "
        "from 5.1% to 94% over the same period. Attributed to village WASH by-laws "
        "enacted by local government and 'SMART enforcement' (graduated mix of warnings, "
        "fines, and prosecutions), with fine proceeds used to fund latrine construction "
        "for the fined household."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative case study (document review, key informant interviews)",
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
        "High: directly documents that a specific local legal-enforcement mechanism "
        "(village WASH by-laws, graduated SMART enforcement with fines/prosecutions) "
        "drove a large increase in sanitation coverage over a 7-year period, with a "
        "restorative-justice feature (fine proceeds funding the fined household's "
        "latrine)."
    ),
    "source_document": "Safari et al. 2019 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Abstract; Results",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-enforcement-"
        "mechanism case study documenting large sanitation-coverage gains attributable "
        "to village by-law enforcement. Before/after percentages are descriptive, not "
        "regression-based; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1115 -- Danert et al 2003
r = blank_row(fieldnames)
r.update({
    "study_id": "S1115",
    "citation": "Danert K, Carter RC, Rwamwanja R, Ssebalu J, Carr G, Kane D (2003). The Private Sector in Rural Water and Sanitation Services in Uganda: Understanding the Context and Developing Support Strategies. Journal of International Development 15(8):1099-1114.",
    "doi": "10.1002/jid.1053",
    "publication_year": "2003",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Uganda",
    "subnational_unit": "8 of Uganda's 56 districts",
    "legal_system": "common law (Uganda); decentralization and privatization policy framework",
    "urban_rural": "rural",
    "service_provider": "small private water sector enterprises",
    "regulatory_model": "decentralization and privatization policy, enhanced by debt-relief-funded sector financing",
    "population": "rural water/sanitation users, 8 districts, Uganda",
    "sample_size": "extensive interviews with major stakeholders, 8 districts",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Thematic findings from extensive stakeholder interviews across 8 districts under "
        "8 headings (corruption; community participation; role of NGOs; private sector "
        "support services; networks and associations; local government procurement "
        "procedures; construction quality; business viability), identifying two sets of "
        "root causes limiting effective private-sector rural water/sanitation delivery."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "8 districts, extensive stakeholder interviews",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative institutional case study (multi-district stakeholder interviews)",
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
        "Moderate-high: rigorous multi-district stakeholder-interview analysis of how "
        "decentralization/privatization policy and local-government procurement "
        "procedures shape private-sector rural water/sanitation service delivery in "
        "Uganda."
    ),
    "source_document": "Danert et al. 2003 (retrieved via Google Drive)",
    "page": "1099-1114",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous multi-district institutional case "
        "study of private-sector rural water/sanitation delivery. No regression-based "
        "effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1116 -- Mottelson 2020
r = blank_row(fieldnames)
r.update({
    "study_id": "S1116",
    "citation": "Mottelson J (2020). A New Hypothesis on Informal Land Supply, Livelihood, and Urban Form in Sub-Saharan African Cities. Land 9(11):435.",
    "doi": "10.3390/land9110435",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multiple (East Africa)",
    "subnational_unit": "four major East African cities (case study areas)",
    "legal_system": "civil/common law (East Africa, mixed); informal-settlement/land-use enforcement policy",
    "urban_rural": "urban",
    "service_provider": "informal land market actors; municipal governments",
    "regulatory_model": "government repression vs. acceptance of informal urban land development",
    "population": "urban informal-settlement residents financially excluded from formal housing markets, East Africa",
    "sample_size": "4 cities, case study areas in each",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "TRUE",
    "building_permit": "",
    "service_area": "",
    "fees": "",
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
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Comparative finding across 4 East African cities: cities/areas with more "
        "government repression of informal urban development show a more compact urban "
        "form, higher levels of tenancy and overcrowding, and lower levels of access to "
        "water and sanitation, attributed to decreased informal land supply, increased "
        "informal-land-market competition, and higher accommodation costs leaving fewer "
        "household resources for infrastructure investment."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "4 cities",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "comparative case study (urban land-use analysis)",
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
        "High: directly compares government repression vs. acceptance of informal urban "
        "development across 4 cities and links repression to reduced informal land "
        "supply, higher accommodation costs, and lower water/sanitation access -- a "
        "legal/administrative land-use enforcement mechanism with a documented "
        "differential access outcome."
    ),
    "source_document": "Mottelson 2020 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Abstract; Results",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-mechanism "
        "comparative case study. No regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1117 -- Amaechina et al 2020
r = blank_row(fieldnames)
r.update({
    "study_id": "S1117",
    "citation": "Amaechina E, Amoah A, Amuakwa-Mensah F, Amuakwa-Mensah S, Bbaale E, Bonilla JA, Bruhl J, Cook J, Chukwuone N, Fuente D, Madrigal-Ballestero R, Marin R, Nam PK, Otieno J, Ponce R, Saldarriaga CA, Vasquez Lavin F, Viguera B, Visser M (2020). Policy Note: Policy Responses to Ensure Access to Water and Sanitation Services during COVID-19: Snapshots from the Environment for Development (EfD) Network. Water Economics and Policy 6(4):2071002.",
    "doi": "10.1142/S2382624X20710022",
    "publication_year": "2020",
    "publication_type": "journal article (policy note)",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Costa Rica; El Salvador; Guatemala; Honduras; Nicaragua; Chile; Colombia; Ghana; Kenya; Nigeria; Panama; South Africa; Uganda; Vietnam",
    "subnational_unit": "national (14 countries)",
    "legal_system": "mixed (civil/common law, 14 countries)",
    "urban_rural": "mixed",
    "service_provider": "national/municipal water utilities (multiple, by country)",
    "regulatory_model": "emergency COVID-19 disconnection moratoriums, subsidy programs, reconnection policies",
    "population": "connected and unconnected/informal-settlement households, 14 Global South countries",
    "sample_size": "14 countries",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "TRUE",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "TRUE",
    "disconnection": "TRUE",
    "reconnection": "TRUE",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
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
    "effect_estimate": (
        "Costa Rica Decree 076-S: disconnection moratorium and mandatory reconnection "
        "throughout the pandemic emergency. Colombia: 250,000+ households previously "
        "disconnected for non-payment reconnected, reconnection cost waived; installment "
        "payment plans; national program rejected by constitutional court after 4 months "
        "(cost ~USD 15 million/month). Chile: existing decile-based subsidy program "
        "covering 15-85% of first 15 m3/month cost extended; USD 6 million rural subsidy "
        "reaching 700,000 rural households. Cape Town, South Africa: indigent program "
        "(qualifying threshold R300,000 property value or <R6,000/month household income) "
        "provides 10.5 m3/month free; households not qualifying could arrange payment "
        "plans; water/sanitation tariffs nonetheless increased 4.5-9.9% across major "
        "cities during the pandemic. Ghana: government paid full water bills for all "
        "domestic customers (~USD 16.4 million/month to GWCL) for April-September 2020. "
        "Uganda NWSC: suspended disconnections; installed emergency water points/tanks in "
        "informal settlements. Across all countries, connected households with regular "
        "billing received more relief than unconnected/informal households."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "14 countries",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "multi-country comparative documentation (EfD network country-team snapshots)",
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
        "High: documents specific, dated, quantified legal/institutional water-access "
        "mechanisms (disconnection moratoriums, reconnection programs, income/property-"
        "value-based subsidy eligibility criteria) across 14 countries, with a consistent "
        "finding that these mechanisms disproportionately benefit already-connected, "
        "regularly-billed households over unconnected/informal-settlement households."
    ),
    "source_document": "Amaechina et al. 2020 (retrieved via Google Drive)",
    "page": "1-14",
    "table": "Table 1 (WASH indicators by country)",
    "figure": "",
    "section": "Government Water and Sanitation Policy Responses to COVID-19 (Section 2, by country)",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous multi-country comparative "
        "documentation of specific institutional/legal water-access mechanisms with "
        "differential effects on connected vs. unconnected households. No regression-"
        "based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1118 -- Mawani 2019
r = blank_row(fieldnames)
r.update({
    "study_id": "S1118",
    "citation": "Mawani V (2019). Unmapped Water Access: Locating the Role of Religion in Access to Municipal Water Supply in Ahmedabad. Water 11(6):1282.",
    "doi": "10.3390/w11061282",
    "publication_year": "2019",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Ahmedabad, Gujarat",
    "legal_system": "common law (India); town planning scheme (TPS) mechanism",
    "urban_rural": "urban",
    "service_provider": "Ahmedabad Municipal Corporation",
    "regulatory_model": "town planning scheme (TPS) implementation, premised on legal status (illegality) of constructions",
    "population": "Muslim-majority areas of Ahmedabad",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "TRUE",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Qualitative finding: poor access to municipal water in Ahmedabad's Muslim areas "
        "is tied to difficulties implementing the town planning scheme, itself premised "
        "on widespread illegal constructions; influential legal actors from both majority "
        "and minority communities exert pressures obstructing plan formulation/"
        "implementation, producing an unstable, contested 'unmapping and mapping' "
        "landscape of water access that is not reducible to a simple state-discrimination "
        "or illegality narrative."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative institutional/legal case study",
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
        "High: directly documents how a specific planning-law mechanism (town planning "
        "scheme), intersecting with legal-status (illegality) determinations and "
        "contested by influential legal actors from majority and minority communities, "
        "produces differential municipal water access along religious lines in "
        "Ahmedabad."
    ),
    "source_document": "Mawani 2019 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Abstract; throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous planning-law/legal-status "
        "mechanism case study. No regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1119 -- Silvestri et al 2018
r = blank_row(fieldnames)
r.update({
    "study_id": "S1119",
    "citation": "Silvestri G, Wittmayer JM, Schipper K, Kulabako R, Oduro-Kwarteng S, Nyenje P, Komakech H, van Raak R (2018). Transition Management for Improving the Sustainability of WASH Services in Informal Settlements in Sub-Saharan Africa -- An Exploration. Sustainability 10(11):4052.",
    "doi": "10.3390/su10114052",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Tanzania; Ghana; Uganda",
    "subnational_unit": "Arusha (Tanzania); Dodowa (Ghana); Kampala (Uganda)",
    "legal_system": "mixed (civil/common law, 3 countries)",
    "urban_rural": "urban (informal settlements)",
    "service_provider": "community water committees; Kampala Capital City Authority (KCCA); local government",
    "regulatory_model": "decentralization policies; governance capacities for WASH services",
    "population": "informal settlement residents, Arusha/Dodowa/Kampala",
    "sample_size": "57 interview summaries; 2 inter-/transdisciplinary workshops (2015-2018)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
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
    "discretion": "TRUE",
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
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Identifies five context dimensions accounting for WASH-service unsustainability "
        "in informal settlements: (a) multiplicity of WASH practices/structures/"
        "arrangements; (b) governance capacities; (c) landownership for sustainable "
        "access; (d) public participation in decision-making; (e) socio-economic "
        "inequalities governing access. Documents specific institutional exclusion: "
        "Kampala community leaders described how the Kampala Capital City Authority "
        "(KCCA) excluded part of the Kawaala informal settlement from access to a "
        "KCCA-built community water well; in Dodowa, landownership disputes result in "
        "some residents paying more for water than others."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "57 interviews; 2 workshops",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "mixed-methods case study (literature review plus interviews and workshops)",
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
        "Moderate-high: grounded in 57 original interviews and 2 workshops across 3 "
        "cities, directly documenting landownership and governance-capacity mechanisms "
        "(including a specific documented case of a municipal authority excluding part "
        "of an informal settlement from a community water source) shaping differential "
        "WASH access."
    ),
    "source_document": "Silvestri et al. 2018 (retrieved via Google Drive)",
    "page": "1-19",
    "table": "",
    "figure": "",
    "section": "Materials and Methods; Results (context dimensions)",
    "exact_location": "Throughout, esp. landownership and governance-capacity sections",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: mixed-methods institutional case study "
        "grounded in original interview/workshop data documenting land-tenure and "
        "governance-capacity mechanisms shaping WASH access. No regression-based effect "
        "size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1120 -- Yeboah 2006
r = blank_row(fieldnames)
r.update({
    "study_id": "S1120",
    "citation": "Yeboah I (2006). Subaltern strategies and development practice: urban water privatization in Ghana. Geographical Journal 172(1):50-65.",
    "doi": "10.1111/j.1475-4959.2006.00184.x",
    "publication_year": "2006",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "national (Accra-Tema Metropolitan Area and rural/small-town classification)",
    "legal_system": "common law (Ghana)",
    "urban_rural": "mixed",
    "service_provider": "Ghana Water Company Limited (GWCL, urban); Community Water and Sanitation Division (CWSD, rural/small-town)",
    "regulatory_model": "urban water privatization (lease/management-contract model), service-area reclassification by population/ability-to-pay",
    "population": "urban and rural/small-town water users, Ghana",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
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
    "effect_estimate": (
        "Service-area reclassification: 114 of GWSC's 210 urban systems transferred to "
        "the rural/small-town CWSD (towns up to 15,000 population), leaving only 96 as "
        "commercially-served urban systems; rationale explicitly stated as rural dwellers "
        "'do not have the ability to pay' (Halcrow Report 1995). CWSD communities required "
        "to provide at least 5% of total system cost, with the remainder from the state, "
        "NGOs and donors; urban dwellers had 93% access to safe water vs. 40% for rural "
        "dwellers at the time of the reform."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "institutional/political-economy case study (documentary analysis, consultant reports)",
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
        "High: directly documents an institutional service-area/eligibility "
        "classification mechanism -- reclassification of smaller towns from commercial "
        "urban service to a rural cost-sharing division on an explicit 'ability to pay' "
        "criterion -- producing differential water-access and cost-sharing-burden "
        "outcomes by geography and class."
    ),
    "source_document": "Yeboah 2006 (retrieved via Google Drive)",
    "page": "50-65",
    "table": "",
    "figure": "Figure 1 (privatization units)",
    "section": "Development practice and water privatization in Ghana; How was Ghana's water to be privatized?",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional-mechanism case study "
        "documenting service-area/eligibility classification by ability-to-pay criterion. "
        "No regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
