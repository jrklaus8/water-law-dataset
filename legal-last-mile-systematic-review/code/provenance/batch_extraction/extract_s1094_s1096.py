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

# S1094 -- de Sardan 2011
r = blank_row(fieldnames)
r.update({
    "study_id": "S1094",
    "citation": "de Sardan JPO (2011). Local Powers and the Co-delivery of Public Goods in Niger. IDS Bulletin 42(2):32-42.",
    "doi": "10.1111/j.1759-5436.2011.00209.x",
    "publication_year": "2011",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Niger",
    "subnational_unit": "Balleyara, Say, Guidan Roumdji",
    "legal_system": "civil law with customary law (Niger)",
    "urban_rural": "urban",
    "service_provider": "state water technicians; communes; development-partner projects; associational structures (water-user committees)",
    "regulatory_model": "co-production/co-delivery via multiple modes of local governance",
    "population": "urban residents, three Niger sites",
    "sample_size": "anthropological fieldwork, three urban sites, 2009",
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
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
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
    "effect_estimate": "Water technicians in departmental services are limited to a single agent with no vehicle or office. Development-project water-well drilling is uncoordinated ('each of them put their wells where they like'). Traders may declare themselves 'mere hawkers' to access socially subsidized water sources not intended for their commercial use.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "anthropological fieldwork case study",
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
        "Moderate: documents multiple institutional 'modes of governance' co-delivering "
        "water and sanitation (bureaucratic, project-based, associational, municipal, "
        "chiefly, merchant), including development-project-imposed 'social counterpart'/"
        "quota financial contributions as a condition of infrastructure investment, and an "
        "eligibility-circumvention practice in which traders misrepresent their occupation "
        "to access water sources subsidized for a different, non-commercial population, "
        "alongside severe under-resourcing of the formal state water-technician service."
    ),
    "source_document": "de Sardan 2011 (retrieved via Google Drive)",
    "page": "32-42",
    "table": "",
    "figure": "",
    "section": "Provision of the four public goods by modes of local governance",
    "exact_location": "Section 3, subsections 3.1-3.6",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/governance mechanism "
        "study directly examining formal and informal eligibility, contribution, and "
        "coordination mechanisms affecting water-service co-delivery to the poor. "
        "Qualitative fieldwork case study, no regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1095 -- Adams & Zulu 2015
r = blank_row(fieldnames)
r.update({
    "study_id": "S1095",
    "citation": "Adams EA, Zulu LC (2015). Participants or customers in water governance? Community-public partnerships for peri-urban water supply. Geoforum 65:112-124.",
    "doi": "",
    "publication_year": "2015",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Malawi",
    "subnational_unit": "peri-urban neighborhoods, two major Malawian cities",
    "legal_system": "common law (Malawi)",
    "urban_rural": "peri-urban",
    "service_provider": "Water User Associations (WUAs)",
    "regulatory_model": "community-based natural resource management (CBNRM); business-based WUA model",
    "population": "poor urban and peri-urban residents, Malawi",
    "sample_size": "preliminary survey, key-informant interviews, focus groups",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "TRUE",
    "property": "",
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
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "mixed-methods case study",
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
        "Moderate: examines Water User Associations (WUAs) as a business-based "
        "community-public partnership model for peri-urban water supply, finding that "
        "insecure/uncertain land tenure, poor municipal capacity, and power relations "
        "between WUAs and residents produce tradeoffs between expanding water-supply "
        "coverage and participatory/ownership goals, effectively repositioning residents "
        "as 'customers' rather than 'participants' in water governance."
    ),
    "source_document": "Adams & Zulu 2015 (retrieved via Google Drive)",
    "page": "112-124",
    "table": "",
    "figure": "",
    "section": "Results and Discussion",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/governance mechanism "
        "study directly examining community-public partnership models and land-tenure "
        "barriers affecting peri-urban water access for the poor. Mixed-methods case "
        "study, no regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1096 -- Sandoval-Minero 2019
r = blank_row(fieldnames)
r.update({
    "study_id": "S1096",
    "citation": "Sandoval-Minero R (2019). Water Utilities: Is Their Sustained Financial Efficiency Achievable? -- The Mexican Case. In: Springer book chapter, Ch. 6.",
    "doi": "",
    "publication_year": "2019",
    "publication_type": "book chapter",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Mexico",
    "subnational_unit": "national (federal, state, municipal water institutions)",
    "legal_system": "civil law (Mexico)",
    "urban_rural": "urban",
    "service_provider": "municipal water utilities; CONAGUA (National Water Commission)",
    "regulatory_model": "federal subsidy allocation via CONAGUA operating rules; Article 115 municipal responsibility",
    "population": "urban households, Mexico, particularly low-income/impoverished neighborhoods",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
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
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "95.7% of urban households have access to water supply infrastructure, but only 80% have service inside the house, 75% report daily service, 62.1% report constant supply, and only 25.3% believe tap water is drinkable without risk. Federal subsidies (CONAGUA) covered ~50% of the total water/sanitation capital budget 2007-2011 but were reduced by over 70% between 2015-2017.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "institutional/policy analysis",
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
        "High: documents that federal subsidies for Mexican municipal water utilities are "
        "allocated via centralized CONAGUA 'operating rules' without linkage to "
        "performance-improvement commitments or ex post assessment, that most municipal "
        "utilities lack any formal economic/tariff regulation, and that 'many new "
        "connections are financed by the users themselves directly through connection "
        "rights,' shifting the cost of infrastructure expansion onto households -- with "
        "the paper explicitly noting that impoverished neighborhoods 'wouldn't afford much "
        "higher tariffs' even in otherwise well-performing utility service areas."
    ),
    "source_document": "Sandoval-Minero 2019 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Financing capital investments in urban water and sanitation sector",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal mechanism study "
        "directly examining subsidy-allocation and connection-cost-burden barriers to "
        "affordable formal water-service access in Mexico. Institutional/policy analysis "
        "chapter citing survey statistics, no original regression; not added to "
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
