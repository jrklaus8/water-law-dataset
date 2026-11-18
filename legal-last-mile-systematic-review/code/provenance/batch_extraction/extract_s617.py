#!/usr/bin/env python3
import csv, os, tempfile

DB = "03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"


def blank_row(fieldnames):
    return {f: "" for f in fieldnames}


def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    new_rows = []

    # S617: Shuaib & Rana 2020, Rajshahi Bangladesh
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S617",
        "citation": "Shuaib ASM, Rana MMP (2020). Assessing water supply for the urban poor in Rajshahi City, Bangladesh. Management of Environmental Quality: An International Journal 31(1):75-88.",
        "doi": "10.1108/MEQ-06-2019-0138",
        "publication_year": "2020",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Bangladesh",
        "subnational_unit": "Rajshahi city (10 slums across inner, middle, and outer zones: Ramchandrapur, Shekerchak, Baganpara, Bahorampur, Bhadra, Daspukur, Jamalpur, Khojapur, Buthpara, RU Station)",
        "legal_system": "common law",
        "urban_rural": "urban",
        "service_provider": "Water and Sewerage Authority; Rajshahi City Corporation; informal/illegal pipeline connections",
        "regulatory_model": "Formal water-connection application process requiring legal recognition of residence status; informal/tolerated illegal connections in unrecognized slum communities; sporadic authority monitoring for illegal watermain connections",
        "population": "Slum-dwelling households in Rajshahi city (minimum 10-year residency)",
        "sample_size": "100 heads of household (questionnaire survey, 2016), 10 slums across 3 zones (inner: 30, middle: 38, outer: 32)",
        "household_level": "TRUE",
        "community_level": "TRUE",
        "income_group": "TRUE",
        "tenure_status": "TRUE",
        "legal_status": "TRUE",
        "indigenous_population": "",
        "migrant_population": "",
        "eligibility": "TRUE",
        "burden": "TRUE",
        "discretion_accommodation": "TRUE",
        "enforcement": "TRUE",
        "documentation": "TRUE",
        "tenure": "TRUE",
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
        "administrative_review": "TRUE",
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
        "service_reliability": "TRUE",
        "service_quantity": "TRUE",
        "service_quality": "TRUE",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "TRUE",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "Composite weighted-average performance index (0-1 scale) per dimension and slum, derived from standardized questionnaire indicators (Akbar et al. 2007 framework); descriptive, no regression",
        "effect_estimate": "Slum residents in 'unrecognized' communities lack the legal right to apply for formal water connections; most access is informal/illegal pipeline connection, tolerated but only occasionally monitored (4 of 10 slums reported monitored for illegal connections vs 6 never monitored); institutional corruption reported in connection installation (BDT 2000-3000 bribes paid to Water and Sewerage Authority fieldworkers for tubewell/connection placement favoring certain residents); 61% of households receive only 10-20 L/person/day (below WHO minimum), 79% receive water only 4-8 hours/day, and a majority report water charges as unaffordably high; overall water-supply performance is 'moderate' but varies significantly by slum location, with institutional-dimension performance rated 'low' in the inner-zone Ramchandrapur slum.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "100 households (10 slums, 3 zones)",
        "adjusted_or_unadjusted": "not applicable (descriptive composite performance indices)",
        "covariates": "",
        "model_type": "Questionnaire-survey case study with a 6-dimension weighted-average performance-assessment framework",
        "study_design": "Cross-sectional questionnaire survey (case study)",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate: documents a genuine legal/institutional mechanism (slum residents' lack of legal right to apply for formal water connections due to unrecognized settlement status, resulting informal/illegal connections, sporadic monitoring, and documented bribery in connection installation) directly against household-level water access, quantity, reliability, and affordability outcomes measured via a 100-household survey across 10 slums; however, the relationship is documented through a descriptive composite performance index rather than a regression linking the legal exposure to the outcome.",
        "source_document": "Shuaib & Rana 2020, Management of Environmental Quality 31(1):75-88 (retrieved via Google Drive inbox)",
        "page": "75-88",
        "table": "Table I (selected slums and households); Table II (dimensions/indicators); Table III (performance levels by dimension and slum); Table IV (slum categories by overall performance)",
        "figure": "Fig. 1 (study slum locations); Fig. 2 (performance-level categories)",
        "section": "3.2.4 Institutional dimension of water supply; 3.2.5 Economic dimension of water supply; 3.1 Overall performance of water supply",
        "exact_location": "Section 3.2.4 (legal access, monitoring, corruption); Table III (institutional-dimension performance by slum)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Questionnaire-survey case study of water supply for the urban poor in Rajshahi, Bangladesh, documenting a genuine legal/institutional exposure (unrecognized-settlement status barring legal connection applications, informal/illegal connections, sporadic monitoring, and connection-installation bribery) against household-level water access, quantity, reliability, and affordability outcomes. Not effect_sizes eligible: descriptive composite performance indices, no regression. Extracted for record_id RE06ED02A63C7.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })
    new_rows.append(r)

    for r in new_rows:
        assert r["study_id"] not in existing_ids, f"{r['study_id']} already exists"

    rows.extend(new_rows)

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended", len(new_rows), "rows:", [r["study_id"] for r in new_rows])


if __name__ == "__main__":
    main()
