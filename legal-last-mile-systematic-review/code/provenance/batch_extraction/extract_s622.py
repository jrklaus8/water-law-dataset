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

    # S622: Yadav 2018, CURE NOIDA market-based sanitation solution
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S622",
        "citation": "Yadav V (2018). A market-based solution to a sanitation issue in a marginalised area. Development in Practice 28(6):824-830.",
        "doi": "10.1080/09614524.2018.1476467",
        "publication_year": "2018",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "India",
        "subnational_unit": "Sectors 8-10 informal settlement, NOIDA, Uttar Pradesh (National Capital Region)",
        "legal_system": "common law (India)",
        "urban_rural": "urban (industrial township informal settlement)",
        "service_provider": "NOIDA Authority (state-appointed bureaucratic township authority); self-organized community/private bore wells and contractors, facilitated by NGO (Center for Urban and Regional Excellence, CURE)",
        "regulatory_model": "township authority refusal to extend formal water/sanitation service to settlements it classifies as illegal/unauthorized (land zoned industrial, occupied without formal tenure); community self-provision (private bore wells, illegally extended city water lines) and NGO-facilitated market-based/community-funded solutions (private drain-cleaning contractors) as a workaround",
        "population": "residents of an informal settlement (~11,300 households, 56,374 people) in NOIDA; project intervention area 3,925 households/18,840 individuals",
        "sample_size": "1,127 households (baseline survey, CURE 2015)",
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
        "documentation": "TRUE",
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
        "administrative_review": "",
        "complaint": "TRUE",
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
        "service_reliability": "TRUE",
        "service_quantity": "",
        "service_quality": "TRUE",
        "affordability": "TRUE",
        "service_continuity": "",
        "application_success": "TRUE",
        "refusal": "TRUE",
        "delay_outcome": "TRUE",
        "effect_measure": "descriptive baseline household survey percentages; program monitoring/tracking data",
        "effect_estimate": "85% of households depend on bottled/filtered water for consumption (formal piped supply denied/absent); 71% use private covered water sources for other purposes; 88% have private toilets (self-installed, not township-provided sewer connections); 11% rely solely on a poorly-built community toilet; 0.6% (11 households) report no access to sanitation facilities at all. Township refused to extend water infrastructure due to the settlement's illegal status; residents responded with self-installed private bore wells and illegal extensions of city water lines. Community-funded drain-cleaning contracts covered 165 households across 6 streets after CURE-facilitated negotiations; over 75 drain patches improved using community resources.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "1,127 households (baseline); 3,925 households (project intervention area)",
        "adjusted_or_unadjusted": "not applicable (descriptive baseline survey and program case study, not a regression model)",
        "covariates": "",
        "model_type": "descriptive case study / NGO program evaluation",
        "study_design": "qualitative/descriptive case study (participatory learning and action, baseline household survey, program monitoring)",
        "risk_of_bias_tool": "CASP",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "2",
        "mechanism_certainty": "Moderate-high: documents an explicit, directly-stated legal/administrative barrier -- the township Water Department's refusal to extend water/sanitation infrastructure to the settlement 'due to the illegal nature of housing in the colony' -- against real household-level baseline survey data on water/sanitation access (bottled-water dependence, private-toilet self-provision, community-toilet reliance) and real tracked project outcomes (community-funded drain improvements); however, the study is a descriptive case study/program report rather than a study isolating the legal-status exposure via a comparison group or regression.",
        "source_document": "Yadav 2018, Development in Practice 28(6):824-830 (retrieved via Google Drive inbox)",
        "page": "824-830",
        "table": "",
        "figure": "",
        "section": "Project area; Water and sanitation improvement project; Conclusion",
        "exact_location": "Project area section (illegal-settlement refusal of service, self-installed bore wells); Water and sanitation improvement project section (CURE 2015 baseline survey statistics, drain-improvement tracking)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Case study of an NGO (CURE) market-based water/sanitation improvement project in an informal settlement in NOIDA, India, documenting the township authority's explicit refusal to extend water/sanitation infrastructure due to the settlement's illegal status, against real household-level baseline survey data (bottled-water dependence, private-toilet self-provision, sanitation-access gaps) and real tracked community-driven service-improvement outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive case-study/NGO program evaluation with real survey percentages, no regression testing legal-status exposure against access outcome. Extracted for record_id R046A5EB2D8C0.",
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
