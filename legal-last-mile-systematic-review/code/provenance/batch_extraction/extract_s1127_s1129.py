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

# S1127 -- Gulyani, Talukdar & Kariuki 2005
r = blank_row(fieldnames)
r.update({
    "study_id": "S1127",
    "citation": "Gulyani S, Talukdar D, Kariuki RM (2005). Universal (Non)service? Water Markets, Household Demand and the Poor in Urban Kenya. Urban Studies 42(8):1247-1274.",
    "doi": "10.1080/00420980500150557",
    "publication_year": "2005",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Kenya",
    "subnational_unit": "3 Kenyan towns",
    "legal_system": "common law (Kenya)",
    "urban_rural": "urban",
    "service_provider": "public utilities; private water vendors; kiosks",
    "regulatory_model": "demand-driven/water-markets institutional model (full-cost pricing)",
    "population": "poor and non-poor households, 3 Kenyan towns",
    "sample_size": "674 households",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
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
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Survey-based analysis of water use and unit costs finds the standard 'poor "
        "pay more, use less' narrative does not hold cleanly: water use behavior and "
        "unit costs do not divide simply along poor/non-poor lines, and willingness "
        "to pay among the unconnected for piped water or improved kiosk service is "
        "tested directly, with findings indicating that pricing/market-based reforms "
        "alone (without attention to service-delivery mechanisms) are insufficient to "
        "improve access for the poor; kiosks are found not always to be a good "
        "solution."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "674 households, 3 Kenyan towns",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "quantitative household-survey study",
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
        "Moderate-high: rigorous household-survey-based empirical test of the "
        "demand-driven/water-markets institutional prescription (full-cost pricing, "
        "willingness-to-pay), directly documenting how this institutional model "
        "performs for poor vs. non-poor urban households in Kenya."
    ),
    "source_document": "Gulyani, Talukdar & Kariuki 2005 (retrieved via Google Drive)",
    "page": "1247-1274",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous empirical institutional-"
        "mechanism study of the market-based water-service model's performance for "
        "the urban poor. No regression-based effect size directly isolating a legal/"
        "institutional mechanism; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1128 -- Ballestero 2015
r = blank_row(fieldnames)
r.update({
    "study_id": "S1128",
    "citation": "Ballestero A (2015). The Ethics of a Formula: Calculating a Financial-Humanitarian Price for Water. American Ethnologist 42(2):262-278.",
    "doi": "10.1111/amet.12129",
    "publication_year": "2015",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Costa Rica",
    "subnational_unit": "national (ARESEP, Autoridad Reguladora de los Servicios Publicos)",
    "legal_system": "civil law (Costa Rica); constitutional right to water (early 2000s constitutional court recognition)",
    "urban_rural": "mixed",
    "service_provider": "AyA (Costa Rica's largest water utility); state/municipal water entities",
    "regulatory_model": "ARESEP water-tariff regulatory formula, including the 'R' development-yield variable",
    "population": "water consumers, Costa Rica",
    "sample_size": "32 interviews; ethnographic fieldwork (ARESEP)",
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
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "TRUE",
    "complaint": "",
    "judicial_review": "TRUE",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
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
        "Ethnographic documentation of ARESEP's regulatory price-setting formula, "
        "including the R (development yield/surplus) variable, and how it is used to "
        "assess and rule on water-utility rate-increase petitions (e.g., a documented "
        "case of AyA petitioning for a 40% price increase) in a manner intended to "
        "operationalize the constitutionally recognized human right to water while "
        "precluding profit-making by water providers."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "32 interviews",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "ethnographic institutional/legal case study",
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
        "Moderate-high: rigorous ethnographic documentation of how a legal/"
        "regulatory tariff-setting formula (ARESEP's price-regulation mechanism) "
        "operationalizes the constitutional human right to water into concrete "
        "affordability outcomes for Costa Rican water consumers."
    ),
    "source_document": "Ballestero 2015 (retrieved via Google Drive)",
    "page": "262-278",
    "table": "",
    "figure": "Figure 2 (ARESEP pricing formula)",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-mechanism "
        "ethnography of a water-tariff regulatory formula operationalizing the human "
        "right to water. No regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1129 -- Pastore 2015
r = blank_row(fieldnames)
r.update({
    "study_id": "S1129",
    "citation": "Pastore MC (2015). Reworking the relation between sanitation and the city in Dar es Salaam, Tanzania. Environment and Urbanization 27(2):473-488.",
    "doi": "10.1177/0956247815592285",
    "publication_year": "2015",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Tanzania",
    "subnational_unit": "Dar es Salaam (3 case-study areas)",
    "legal_system": "civil law (Tanzania); colonial-era infrastructure planning legacy",
    "urban_rural": "urban",
    "service_provider": "local government; decentralized on-site systems (boreholes, wells, on-site latrines)",
    "regulatory_model": "colonial-era centralized 'piped paradigm' vs. decentralized on-site sanitation systems",
    "population": "urban residents of Dar es Salaam, by settlement type",
    "sample_size": "3 case-study areas",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "TRUE",
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
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
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
    "institutional_fragmentation": "TRUE",
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
        "The colonial-era 'piped paradigm' (centralized off-site water/sanitation "
        "infrastructure) was imported to serve only elite neighborhoods; today, "
        "formal planning for infrastructure still follows the centralized model "
        "while the majority of urban Africans (in sub-Saharan Africa generally: 40% "
        "piped water, 25% public standposts, 24% wells/boreholes, 8% "
        "lakes/ponds/springs; sanitation predominantly on-site: boreholes, wells, "
        "on-site latrines) rely on decentralized, informally evolved systems outside "
        "the formal planning model."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "3 case-study areas, Dar es Salaam",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "institutional/planning-history case study",
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
        "Moderate-high: documents how a colonial-era infrastructure-planning "
        "institutional design (the centralized 'piped paradigm,' historically "
        "reaching only elite neighborhoods) continues to structure differential "
        "sanitation access by settlement type in present-day Dar es Salaam."
    ),
    "source_document": "Pastore 2015 (retrieved via Google Drive)",
    "page": "473-488",
    "table": "",
    "figure": "",
    "section": "Introduction; case study areas",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/planning-history "
        "case study of colonial-legacy infrastructure design as a mechanism of "
        "differential sanitation access. No regression-based effect size; not added "
        "to effect_sizes.csv."
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
