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

    # S645: Mugambe, Tumwesigye & Larkan 2013, PLWHA WASH barriers Uganda
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S645",
        "citation": "Mugambe RK, Tumwesigye NM, Larkan F (2013). Barriers to accessing water, sanitation and hygiene among people living with HIV/AIDS in Gomba and Mpigi districts in Uganda: a qualitative study. Journal of Public Health 21:29-37.",
        "doi": "10.1007/s10389-012-0515-x",
        "publication_year": "2013",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Uganda",
        "subnational_unit": "Gomba and Mpigi districts",
        "legal_system": "common law (Uganda)",
        "urban_rural": "rural (with some peri-urban)",
        "service_provider": "local water/sanitation infrastructure (boreholes, springs, public latrines); water vendors",
        "regulatory_model": "public-latrine and water-source pricing follows a flat fee-per-use rate applied uniformly regardless of vulnerability status, with no pro-poor or PLWHA-sensitive pricing consideration; water-user-committee/facility-management-committee structures nominally govern public water/sanitation facilities but PLWHA reported exclusion from committee participation and some facility management committees were reported non-functional; explicit institutional avoidance of PLWHA-targeted WASH arrangements was reported by a district official out of concern this would appear discriminatory toward other groups",
        "population": "people living with HIV/AIDS (PLWHA) receiving antiretroviral therapy at Maddu Health Centre IV (Gomba) and Mpigi Health Centre IV (Mpigi)",
        "sample_size": "6 focus group discussions (49 participants: 3 male, 3 female groups); 12 key-informant interviews (water officers, environmental health officers, medical officers, HIV/AIDS care givers)",
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
        "judicial_review": "",
        "disconnection": "",
        "reconnection": "",
        "sanction": "",
        "participation": "TRUE",
        "institutional_fragmentation": "TRUE",
        "political_coordination": "",
        "bureaucratic_assistance": "",
        "formal_connection": "",
        "water_access": "TRUE",
        "sanitation_access": "TRUE",
        "service_coverage": "TRUE",
        "service_reliability": "",
        "service_quantity": "TRUE",
        "service_quality": "TRUE",
        "affordability": "TRUE",
        "service_continuity": "",
        "application_success": "",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "qualitative content analysis (latent/summative) of FGD and KII transcripts",
        "effect_estimate": "Safe water coverage in Mpigi district was 33% in 2009 (below the 55% national average); latrine coverage 57.6% (below 63% national average); functionality rate of safe water sources declined from 95% (2006) to 79% (2009). PLWHA reported paying 0.04 USD per 20-L jerrycan at improved sources versus 0.4-0.6 USD from water vendors during shortages, with no pro-poor/vulnerability-sensitive pricing at public facilities despite calls for it. Major qualitative themes: financial, attitudinal, knowledge, social, physical, and institutional/sustainability barriers, plus limited improved water sources -- institutional barriers specifically included flat-rate public-facility fee structures lacking a pro-poor perspective, exclusion of PLWHA from water-user-committee participation, and non-functional facility management committees. A district official explicitly declined to establish PLWHA-targeted WASH arrangements, citing concern about appearing discriminatory toward other vulnerable groups.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "49 FGD participants; 12 key informants",
        "adjusted_or_unadjusted": "not applicable (qualitative content analysis, not a regression model)",
        "covariates": "",
        "model_type": "qualitative content analysis (focus groups and key-informant interviews)",
        "study_design": "qualitative descriptive study",
        "risk_of_bias_tool": "CASP",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "2",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate: documents a genuine institutional/administrative barrier (uniform flat-rate facility-fee structures with no vulnerability-sensitive accommodation, and exclusion of PLWHA from water-user-committee governance) against real qualitative FGD/KII evidence of WASH access and utilization barriers for a specific vulnerable population; the institutional dimension is one of several barrier types (financial, social, physical, attitudinal, knowledge) documented, and the study does not isolate the institutional mechanism's independent effect via a quantitative comparison.",
        "source_document": "Mugambe, Tumwesigye & Larkan 2013, Journal of Public Health 21:29-37 (retrieved via Google Drive inbox)",
        "page": "29-37",
        "table": "Table 1",
        "figure": "",
        "section": "Institutional and sustainability barriers; Results",
        "exact_location": "Institutional and sustainability barriers subsection (flat-rate fee structures, water-user-committee exclusion) and Table 1 (major themes)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative study of WASH access barriers among people living with HIV/AIDS in Gomba and Mpigi districts, Uganda, documenting institutional/administrative barriers (flat-rate fee structures, exclusion from water-committee governance) alongside financial/social/physical barriers. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative FGD/KII study. Extracted for record_id R221EA3C5B171.",
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
