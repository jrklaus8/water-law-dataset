#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-28"
DATE = "2026-09-28"


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

# S1157 -- Samano Romero & Chavez-Mejia 2025, Water Access in Mexico City review
r = blank_row(fieldnames)
r.update({
    "study_id": "S1157",
    "citation": "Samano Romero G, Chavez-Mejia A (2025). Water Access in Mexico City: A Review of Local Research Approaches. Wiley Interdisciplinary Reviews: Water 12:e70046.",
    "doi": "10.1002/wat2.70046",
    "publication_year": "2025",
    "publication_type": "journal article (literature review)",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Mexico",
    "subnational_unit": "Mexico City",
    "legal_system": "civil law; Mexican municipal/national water-governance framework",
    "urban_rural": "urban",
    "service_provider": "Mexico City water-supply system (multiple agencies)",
    "regulatory_model": "large-scale hydraulic transfer/groundwater-extraction system; human-right-to-water framing",
    "population": "Mexico City residents",
    "sample_size": "narrative literature review/research synthesis (not a primary empirical study)",
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
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "narrative literature review/research synthesis (no regression-based effect estimate)",
    "effect_estimate": (
        "Reviews and synthesizes historical, sociospatial, and quantitative research domains "
        "on water access in Mexico City. Documents that despite a 98.8% official household "
        "water-connection rate (INEGI 2021), the practical access problem is water pressure, "
        "supply intermittency, and quality/trust concerns rather than absence of a domestic "
        "tap, with households bearing the cost of domestic storage systems and near-universal "
        "bottled-water purchase. Synthesizes literature on socially stratified and spatially "
        "differentiated water-access inequality across the city, tied to the historical "
        "development of a large-scale inter-basin hydraulic transfer and groundwater-"
        "extraction infrastructure system."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "narrative review of Mexico City water-access literature",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "narrative literature review/research synthesis",
    "study_design": "qualitative research synthesis / narrative literature review",
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
        "Moderate: a narrative (not systematic/PRISMA) review synthesizing a substantial body "
        "of existing empirical literature on water-access inequality and its institutional/"
        "infrastructural determinants in Mexico City; genuine secondary synthesis, not a "
        "designed primary causal-identification study."
    ),
    "source_document": "Samano Romero & Chavez-Mejia 2025 (retrieved via Google Drive; found mislabeled under a different record_id's fileId, R023B3A0D827A, in the Sep-26-2026 delivery -- see full_text_screening_database.csv notes for RC8E1C6959D2C and R023B3A0D827A)",
    "page": "1-11",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine literature-review synthesis of empirical "
        "water-access research covering governance, infrastructure, and affordability in "
        "Mexico City. Qualitative only; no effect_sizes.csv entry. Recorded under record_id "
        "RC8E1C6959D2C after a content-labeling correction -- see CHANGELOG.md, "
        "'Two-hundred-thirty-seventh full-text screening batch,' for the full account."
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
