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

    # S616: Reniko & Kolawole 2020, Karoi Zimbabwe prepaid water meters
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S616",
        "citation": "Reniko G, Kolawole OD (2020). 'They don't read metres, they only bring bills': Issues surrounding the installation of prepaid water metres in Karoi town, Zimbabwe. South African Geographical Journal 102(3):356-371.",
        "doi": "10.1080/03736245.2019.1691046",
        "publication_year": "2020",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Zimbabwe",
        "subnational_unit": "Karoi town, Mashonaland West Province (5 residential areas: Chiedza B, Chiedza D, Garikai, Claudia, Chikangwe)",
        "legal_system": "common law",
        "urban_rural": "urban",
        "service_provider": "Zimbabwe National Water Authority (ZINWA); Karoi Town Council (KTC, planned transferee)",
        "regulatory_model": "Zimbabwean Constitution (right to water); proposed prepaid water meter (PWM) policy replacing traditional post-paid block-tariff billing; Build-Operate-Transfer/privatization framework underlying ZINWA's establishment (1990s ESAP)",
        "population": "Residents of 5 high-density (predominantly low-income) residential areas in Karoi town",
        "sample_size": "35 residents (convenience-sampled: 10 Chiedza D, 10 Chiedza B, 5 each Garikai/Claudia/Chikangwe) via interviews, FGDs, and observations at water points; plus KTC clerk/secretary, ZINWA-Karoi manager, hospital nurses, and Ministry of Gender and Women Affairs staff interviews",
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
        "documentation": "TRUE",
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
        "hardship_exception": "TRUE",
        "administrative_review": "TRUE",
        "complaint": "TRUE",
        "judicial_review": "",
        "disconnection": "TRUE",
        "reconnection": "",
        "sanction": "TRUE",
        "participation": "TRUE",
        "institutional_fragmentation": "TRUE",
        "political_coordination": "TRUE",
        "bureaucratic_assistance": "",
        "formal_connection": "TRUE",
        "water_access": "TRUE",
        "sanitation_access": "",
        "service_coverage": "",
        "service_reliability": "TRUE",
        "service_quantity": "",
        "service_quality": "TRUE",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "Qualitative thematic/content analysis of interviews, FGDs, and documents; real revenue-collection data by residential area (descriptive), no regression",
        "effect_estimate": "Under the existing post-paid billing system, ZINWA collected only 8.2% of possible monthly revenue on average across the 5 residential areas in 2018 (ranging from 1.6% in Chikangwe to 26.8% in Garikai, Table 2); residents and officials framed the proposed prepaid water meter (PWM) policy as risking automatic disconnection of low-income households unable to pre-pay, in violation of the Zimbabwean Constitution's right to water and the UN ICESCR human right to water; literature cited within the study reports PWMs associated with reduced water demand by up to 65% and, elsewhere (Ngwelezane, South Africa), a cholera epidemic affecting 113,966 people following prepayment requirements.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "35 residents; KTC/ZINWA officials; 5 residential areas' revenue data",
        "adjusted_or_unadjusted": "not applicable (qualitative case study; descriptive revenue-collection statistics)",
        "covariates": "",
        "model_type": "Qualitative case study (document analysis, unstructured interviews, FGDs, observations)",
        "study_design": "Qualitative case study",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "2",
        "mechanism_certainty": "Moderate: documents a genuine constitutional/legal exposure (the proposed prepaid water meter policy versus the Zimbabwean Constitution's right to water) directly against household-level water access, affordability, and disconnection-risk concerns raised by 35 resident interviewees and municipal/utility officials, corroborated by real revenue-collection data under the current post-paid system; however, the PWM policy had not yet been implemented at the time of study, so the analysis captures pre-implementation stakeholder perceptions rather than an observed exposure-outcome relationship.",
        "source_document": "Reniko & Kolawole 2020, South African Geographical Journal 102(3):356-371 (retrieved via Google Drive inbox)",
        "page": "356-371",
        "table": "Table 1 (gender of respondents); Table 2 (average monthly water revenue collection by residential area, 2018)",
        "figure": "",
        "section": "Popular viewpoints on the introduction of PWMs in Karoi; Average monthly water revenue collection for 2018 in Karoi town; Impact of water shortage in Karoi",
        "exact_location": "Table 2 (revenue-collection data); Popular viewpoints section (constitutional right-to-water framing, disconnection risk)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative case study of a proposed prepaid water meter policy in Karoi, Zimbabwe, documenting a genuine constitutional/legal exposure (right to water vs. automatic-disconnection PWM policy) against household-level water access, affordability, and disconnection-risk outcomes, corroborated by real revenue-collection data under the existing post-paid system. Not effect_sizes eligible: PWMs not yet implemented at time of study, no exposure-comparator outcome regression. Extracted for record_id R7DF720007123.",
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
