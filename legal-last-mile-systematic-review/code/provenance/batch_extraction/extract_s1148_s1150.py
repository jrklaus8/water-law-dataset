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

# S1148 -- Salazar Adams, Haro Velarde & Loera Burnes
r = blank_row(fieldnames)
r.update({
    "study_id": "S1148",
    "citation": "Salazar Adams A, Haro Velarde N, Loera Burnes E. Capacidad institucional de los organismos de agua de Saltillo y Hermosillo, Mexico [Institutional Capacity of the Water Utilities of Saltillo and Hermosillo, Mexico].",
    "doi": "",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "Spanish",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Mexico",
    "subnational_unit": "Saltillo, Coahuila; Hermosillo, Sonora",
    "legal_system": "civil law; Mexican municipal water-utility governance framework",
    "urban_rural": "urban",
    "service_provider": "Saltillo and Hermosillo municipal water utilities (organismos operadores de agua)",
    "regulatory_model": "comparative institutional-capacity framework: management autonomy, metering coverage, tariff indexation, staff training",
    "population": "residents served by two municipal water utilities, Mexico, 2001-2015",
    "sample_size": "comparative institutional case study, 2 Mexican municipal water utilities",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
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
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative/descriptive comparative institutional-capacity case study (no regression-based effect estimate)",
    "effect_estimate": (
        "Comparative institutional-capacity case study (2001-2015) of Saltillo and Hermosillo "
        "municipal water utilities in Mexico, evaluating political, administrative, and human-"
        "resource-management factors against management outcomes. Finds Saltillo's water utility "
        "has greater institutional capacity (management autonomy, metering coverage, tariff "
        "indexation, staff training) than Hermosillo's, and that this institutional-capacity "
        "difference corresponds to better service-delivery/management performance results."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "2 Mexican municipal water utilities, 2001-2015",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative comparative institutional-capacity case study",
    "study_design": "qualitative institutional-mechanism comparative case study",
    "risk_of_bias_tool": "CASP Qualitative Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: comparative institutional-capacity case study of two Mexican water utilities "
        "documenting a plausible institutional-mechanism/performance relationship, though "
        "descriptive/comparative rather than a designed causal-identification analysis."
    ),
    "source_document": "Salazar Adams, Haro Velarde & Loera Burnes (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine comparative institutional-mechanism case "
        "study of water-utility governance capacity affecting service performance. Qualitative "
        "only; no effect_sizes.csv entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1149 -- Martinez-Fernandez, Neto, Hernandez-Mora, Del Moral & La Roca 2020
r = blank_row(fieldnames)
r.update({
    "study_id": "S1149",
    "citation": "Martinez-Fernandez J, Neto S, Hernandez-Mora N, Del Moral L, La Roca F (2020). The role of the Water Framework Directive in the controversial transition of water policy paradigms in Spain and Portugal. Water Alternatives 13(3):556-581.",
    "doi": "",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Spain, Portugal",
    "subnational_unit": "national-level, Iberian Peninsula",
    "legal_system": "civil law; EU regulatory framework (Water Framework Directive)",
    "urban_rural": "mixed",
    "service_provider": "national water-governance authorities, Spain and Portugal",
    "regulatory_model": "EU Water Framework Directive-driven institutional transition from a 'hydraulic paradigm' to a new water-governance approach",
    "population": "national water-policy systems, Spain and Portugal",
    "sample_size": "comparative institutional/regulatory-history case study, 2 countries",
    "household_level": "",
    "community_level": "",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
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
    "effect_measure": "qualitative institutional/regulatory-reform case study (no regression-based effect estimate)",
    "effect_estimate": (
        "Qualitative institutional/regulatory-reform analysis documenting the EU Water Framework "
        "Directive's role as an institutional catalyst for shifting Spain's and Portugal's national "
        "water governance away from a dominant supply-side 'hydraulic paradigm' toward a new "
        "water-governance approach, examining the contested political and institutional process of "
        "this transition at the national level."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "national water-policy systems, Spain and Portugal",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative institutional/regulatory-reform case study",
    "study_design": "qualitative institutional/legal-mechanism case study",
    "risk_of_bias_tool": "CASP Qualitative Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: documented institutional/regulatory-reform case study of EU-level legal "
        "instrument driving national water-governance paradigm change, primarily descriptive/"
        "political-economy analysis rather than a designed comparison isolating a single "
        "mechanism's effect on a specific access outcome."
    ),
    "source_document": "Martinez-Fernandez et al. 2020 (retrieved via Google Drive)",
    "page": "556-581",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal-mechanism case study of "
        "EU regulatory reform's effect on national water-governance paradigms. Qualitative only; "
        "no effect_sizes.csv entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1150 -- World Bank & IADB 2018, Transforming Karachi
r = blank_row(fieldnames)
r.update({
    "study_id": "S1150",
    "citation": "World Bank & Inter-American Development Bank (2018). Transforming Karachi into a Livable and Competitive Megacity: A City Diagnostic and Transformation Strategy. Directions in Development: Infrastructure. Washington, DC: World Bank.",
    "doi": "",
    "publication_year": "2018",
    "publication_type": "report",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "FALSE",
    "country": "Pakistan",
    "subnational_unit": "Karachi",
    "legal_system": "common law; Pakistani federal/provincial/local administrative framework",
    "urban_rural": "urban",
    "service_provider": "Karachi Water & Sewerage Board (KWSB)",
    "regulatory_model": "highly fragmented multi-agency governance (~20 federal/provincial/local agencies with separate legal/administrative frameworks); KWSB Act 1996",
    "population": "Karachi residents, including over 50% living in informal settlements (katchi abadis)",
    "sample_size": "city-wide diagnostic, Karachi (population ~16 million)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "low-income",
    "tenure_status": "informal (katchi abadis) and formal settlement",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "TRUE",
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
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative/descriptive city-diagnostic case study (no regression-based effect estimate)",
    "effect_estimate": (
        "City diagnostic documenting Karachi's severe institutional/legal fragmentation across "
        "water/sanitation governance: approximately 20 federal, provincial, and local agencies "
        "with separate legal and administrative frameworks and minimal coordination; KWSB's own "
        "legal framework (KWSB Act 1996) specifying its functions, revenue collection, and service "
        "obligations; and the formal/informal-settlement status of the population (over 50% living "
        "in informal katchi abadis) as a structural determinant of water/sanitation access. Reports "
        "KWSB provides service through 1.13 million domestic connections against water needs "
        "estimated at more than double current supply (650 MGD supplied vs. 1,200 MGD needed per "
        "WHO per-capita standard), with informal settlements systematically underserved."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "Karachi, Pakistan (population ~16 million, >50% in informal settlements)",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative/descriptive city-diagnostic case study",
    "study_design": "qualitative institutional/legal-mechanism case study",
    "risk_of_bias_tool": "CASP Qualitative Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate-high: detailed institutional/legal diagnostic documenting multi-agency legal "
        "fragmentation and formal/informal-settlement status as structural mechanisms shaping "
        "differential water/sanitation service access in Karachi, with concrete service-coverage "
        "figures, though primarily descriptive rather than a designed causal-identification "
        "analysis."
    ),
    "source_document": "World Bank & IADB 2018 (retrieved via Google Drive)",
    "page": "book-length",
    "table": "",
    "figure": "",
    "section": "Water Supply and Sanitation chapter",
    "exact_location": "Water Supply and Sanitation chapter",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal-mechanism case study "
        "documenting multi-agency legal fragmentation and formal/informal-settlement status "
        "affecting water/sanitation access in Karachi. Qualitative only; no effect_sizes.csv entry."
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
