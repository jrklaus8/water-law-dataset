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

    # S633: Kasri, Wirutomo, Kusnoputranto & Moersidik 2017, Pamsimas citizen engagement Indonesia
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S633",
        "citation": "Kasri RY, Wirutomo P, Kusnoputranto H, Moersidik SS (2017). Citizen engagement to sustaining community-based rural water supply in Indonesia. International Journal of Development Issues 16(3):276-288.",
        "doi": "10.1108/IJDI-03-2017-0031",
        "publication_year": "2017",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Indonesia",
        "subnational_unit": "4 villages: Desa Sukalaksana and Desa Cisarua (Garut district, West Java); Silayang Jorong VI Parit Panjang and Jorong Gumarang I (Agam district, West Sumatera)",
        "legal_system": "civil law (Indonesia); decentralized governance since 2001 (34 provinces, 514 cities/districts, ~74,000 villages)",
        "urban_rural": "rural",
        "service_provider": "BPSPAMS (Badan Pengelola Sarana Penyediaan Air Minum dan Sanitasi) -- village-level community-based water management bodies established under the Pamsimas national rural water program",
        "regulatory_model": "Community-Demand-Driven (CDD) national program (Pamsimas, Program Penyediaan Air Minum dan Sanitasi Berbasis Masyarakat) mandated under Presidential Decree No. 185/2014, implemented via village-level community organizations (BPSPAMS) whose legal status, tariff-setting, and budget-support arrangements are established through village decrees and require citizen-government collaboration across program sub-cycles (strategic planning, financing, construction, O&M, sustaining services)",
        "population": "rural households in 4 Pamsimas program villages, Indonesia",
        "sample_size": "4 villages (qualitative case study; in-depth interviews and focus group discussions, Feb-Apr 2016)",
        "household_level": "TRUE",
        "community_level": "TRUE",
        "income_group": "TRUE",
        "tenure_status": "",
        "legal_status": "TRUE",
        "indigenous_population": "",
        "migrant_population": "",
        "eligibility": "TRUE",
        "burden": "TRUE",
        "discretion_accommodation": "TRUE",
        "enforcement": "",
        "documentation": "TRUE",
        "tenure": "",
        "property": "",
        "planning": "TRUE",
        "zoning": "",
        "building_permit": "",
        "service_area": "TRUE",
        "fees": "TRUE",
        "procedural_steps": "TRUE",
        "delay": "TRUE",
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
        "formal_connection": "TRUE",
        "water_access": "TRUE",
        "sanitation_access": "TRUE",
        "service_coverage": "TRUE",
        "service_reliability": "TRUE",
        "service_quantity": "",
        "service_quality": "TRUE",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "qualitative multi-case comparison (2 higher-performing vs 2 lower-performing villages), village-level tracked access counts",
        "effect_estimate": "Desa Sukalaksana (good performance): entire targeted population (village decree on tariff, active BPSPAMS with published financial reports, village-budget support for major repairs) reached full access to improved water/sanitation by 2015, up from 30-min-walk dug-well/spring access and 15% improved-latrine coverage pre-program. Desa Cisarua (poor performance): BPSPAMS established without legal status, no water meter or tariff enacted; piped access stopped in 2011 after only 1 of 2 targeted hamlets was reached; by 2016 only ~40 of 1,170 targeted households had functioning Pamsimas access. Silayang Jorong VI (good performance): tariff and BPSPAMS operations legalized via village decree, village budget allocated for expansion; received district-level best-village award (2015). Jorong Gumarang I (poor performance): budget transferred directly to a program-created group (KKM) bypassing the village leader, no village decree resolved an inter-village pipe-tapping dispute; as of 2016, no functioning Pamsimas piped water existed in the village at all.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "4 villages",
        "adjusted_or_unadjusted": "not applicable (qualitative comparative case study, not a regression model)",
        "covariates": "",
        "model_type": "qualitative comparative case study (in-depth interviews, focus group discussions, document review)",
        "study_design": "qualitative multi-case comparison",
        "risk_of_bias_tool": "CASP",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate: documents concrete institutional/legal factors -- village-government decrees legalizing tariffs and BPSPAMS operations, formal legal status (or its explicit absence) of the community water-management body, and village-level budget-allocation decisions -- against real, village-tracked access outcomes (population/household counts reaching functioning water access) across 4 comparably-situated villages with contrasting sustainability performance; however, this is a qualitative multi-case comparison without a statistical exposure-outcome contrast, and citizen-engagement/social-structure factors (trust in village leadership, communal culture) are analyzed alongside the legal/institutional ones as co-determinants.",
        "source_document": "Kasri, Wirutomo, Kusnoputranto & Moersidik 2017, International Journal of Development Issues 16(3):276-288 (retrieved via Google Drive inbox)",
        "page": "276-288",
        "table": "Table I; Table II; Table III",
        "figure": "Figure 1",
        "section": "Discussion and findings; Citizen engagement in delivering and sustaining rural water supply in four villages; Synthesis from the four villages",
        "exact_location": "Village case-study subsections (Desa Sukalaksana, Desa Cisarua, Silayang Jorong VI, Jorong Gumarang I) and the Synthesis subsection",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative comparative case study of 4 Indonesian Pamsimas rural water-supply villages, documenting village-government policy/decrees, BPSPAMS community-body legal status, and program governance as institutional determinants of service-delivery sustainability, against real village-level tracked access outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative multi-case comparison, no quantitative exposure-outcome effect estimate. Extracted for record_id RC0FCB69ED597.",
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
