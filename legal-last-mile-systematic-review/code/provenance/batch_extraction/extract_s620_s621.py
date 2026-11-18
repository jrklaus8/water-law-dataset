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

    # S620: Poonia & Punia 2019, drinking water supply determinants India
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S620",
        "citation": "Poonia A, Punia M (2019). Associates and determinants of drinking water supply: a case study along urban-rural continuum of semi-arid cities in India. Urban Water Journal 16(10):749-755.",
        "doi": "10.1080/1573062X.2020.1729387",
        "publication_year": "2019",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "India",
        "subnational_unit": "Jaipur (large city) and Pilani (small city), Rajasthan",
        "legal_system": "common law (India)",
        "urban_rural": "mixed (urban-rural continuum: city core, outskirts, peripheral villages)",
        "service_provider": "municipal/institutional water supply (urban and rural local bodies) alongside private water suppliers and individual tube wells",
        "regulatory_model": "institutional (municipal) piped water supply governed by urban and rural local bodies under the 73rd and 74th Indian Constitutional amendments, alongside informal private-supplier and self-supply (tube well) arrangements",
        "population": "households along the urban-rural continuum of two semi-arid Rajasthan cities",
        "sample_size": "280",
        "household_level": "TRUE",
        "community_level": "TRUE",
        "income_group": "TRUE",
        "tenure_status": "",
        "legal_status": "",
        "indigenous_population": "TRUE",
        "migrant_population": "",
        "eligibility": "",
        "burden": "TRUE",
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
        "political_coordination": "",
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
        "effect_measure": "binary logistic regression odds ratios (OR) with 95% CI; chi-square test of association",
        "effect_estimate": "Payment per month for water (institutional-supply proxy): 54-180 Rs OR=7.355 (95% CI 2.787-19.413, p<0.01) vs. <54 Rs reference; 180-300 Rs OR=2.494 (95% CI 1.057-5.885, p<0.05); >300 Rs (private-supplier proxy) OR=0.211 (95% CI 0.060-0.744, p<0.05). Location: outskirts of city OR=4.071 (95% CI 1.151-14.398, p<0.05); core of city OR=3.652 (95% CI 1.085-12.287, p<0.05) vs. village reference. Model Nagelkerke R2=0.515.",
        "lower_CI": "0.060 (lowest bound, >300Rs payment category)",
        "upper_CI": "19.413 (highest bound, 54-180Rs payment category)",
        "standard_error": "",
        "p_value": "<0.01 to <0.10 across predictors (see effect_estimate)",
        "extraction_sample_size": "280",
        "adjusted_or_unadjusted": "adjusted (seven-predictor multivariable logistic regression: social group, male education, female education, occupation, income, payment for water, location)",
        "covariates": "social group (caste), male education, female education, occupation, income group",
        "model_type": "binary logistic regression",
        "study_design": "cross-sectional household survey",
        "risk_of_bias_tool": "JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "2",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate: payment-per-month-for-water is explicitly interpreted by the authors as a proxy for institutional (municipal) vs. private water-supply arrangement and shows the strongest association (highest chi-square value among tested indicators) with the dichotomous good-drinking-water-supply outcome in a properly-specified multivariable logistic regression with real odds ratios and 95% CI; however, it is an indirect proxy rather than a directly-coded institutional-arrangement variable, and is estimated jointly with several socioeconomic covariates (caste, education, occupation, income) rather than as an isolated legal/institutional exposure.",
        "source_document": "Poonia & Punia 2019, Urban Water Journal 16(10):749-755 (retrieved via Google Drive inbox)",
        "page": "749-755",
        "table": "Table 3 (chi-square associations); Table 4 (logistic regression odds ratios and 95% CI)",
        "figure": "",
        "section": "Database and methodology; Analysis and results; Discussion; Conclusion",
        "exact_location": "Table 4 (payment per month for water and location odds ratios); Discussion section (institutional factor interpretation of payment variable)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). 280-household survey with seven-predictor logistic regression along the urban-rural continuum of two Rajasthan cities, documenting payment-for-water (institutional-supply proxy) and location (differential municipal coverage) as significant determinants of household drinking-water access. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: institutional-arrangement variable is an indirect payment-amount proxy embedded among socioeconomic covariates, not a directly-coded single legal/institutional exposure in the Family A/B/C sense. Extracted for record_id RD7BE4A2810FC.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })
    new_rows.append(r)

    # S621: Reddy 2018, Techno-institutional models Andhra Pradesh
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S621",
        "citation": "Reddy VR (2018). Techno-institutional models for managing water quality in rural areas: case studies from Andhra Pradesh, India. International Journal of Water Resources Development 34(1):97-115.",
        "doi": "10.1080/07900627.2016.1218755",
        "publication_year": "2018",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "India",
        "subnational_unit": "8 villages across 4 districts (coastal and Telangana regions), united Andhra Pradesh",
        "legal_system": "common law (India)",
        "urban_rural": "rural",
        "service_provider": "mixed: gram panchayat (village council), private/NGO foundations (Byrraju Foundation, Naandi Foundation, Sai Oral Health Foundation), and government Rural Water Supply and Sanitation Department (RWSSD)",
        "regulatory_model": "public-private-community partnership models for water treatment plant governance: panchayat-private(NGO) partnership, public-panchayat-private partnership, community/panchayat self-management, and government-department handover-to-panchayat model; formalized via panchayat resolutions and tripartite agreements",
        "population": "rural households in 8 villages using or eligible to use community water treatment plants",
        "sample_size": "240 households (30 per village across 8 villages)",
        "household_level": "TRUE",
        "community_level": "TRUE",
        "income_group": "TRUE",
        "tenure_status": "",
        "legal_status": "",
        "indigenous_population": "TRUE",
        "migrant_population": "TRUE",
        "eligibility": "TRUE",
        "burden": "TRUE",
        "discretion_accommodation": "TRUE",
        "enforcement": "",
        "documentation": "",
        "tenure": "",
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
        "bureaucratic_assistance": "TRUE",
        "formal_connection": "",
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
        "effect_measure": "descriptive coverage percentages by socioeconomic group; net present value and benefit-cost ratio financial-viability metrics",
        "effect_estimate": "Household coverage of treated water by land-ownership group across 8 villages: large farmers 18%, medium 35%, small/marginal 43%, landless 37% (overall 38%). Coverage in surface-water-source villages ranged 23-66%. RO/UV plants meet only ~10% of total household domestic water demand (drinking/cooking), while microfilter technology can meet full domestic demand (~40+ L/capita/day). Benefit-cost ratios ranged from 0.34 (Bomminampadu, unviable) to 3.75 (Dandu Malkapur, panchayat-managed, most viable) across the 8 sample plants.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "240",
        "adjusted_or_unadjusted": "not applicable (descriptive comparative case-study statistics, not a regression model)",
        "covariates": "",
        "model_type": "descriptive comparative case-study analysis; cost-benefit financial analysis (NPV, BCR)",
        "study_design": "mixed-methods multi-site comparative case study (FGDs, village transect walks, structured household survey)",
        "risk_of_bias_tool": "MMAT",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "2",
        "outcome_measurement_quality": "2",
        "mechanism_certainty": "Moderate: documents four distinct institutional governance models (panchayat-private partnership, public-private-community partnership, community self-management, government-department handover) for water treatment service delivery, with real tracked coverage-by-socioeconomic-group and financial-viability outcome data across 8 villages; however, the comparison is descriptive/case-study in nature (no regression isolating institutional-model effects on access net of confounding village-level factors like contamination severity and water source type), and coverage differences are also driven by contamination type and technology choice, not institutional arrangement alone.",
        "source_document": "Reddy 2018, International Journal of Water Resources Development 34(1):97-115 (retrieved via Google Drive inbox)",
        "page": "97-115",
        "table": "Table 1 (sample villages); Table 4 (cash flow/NPV/BCR); Table 5-7 (institutional mechanisms and links); coverage-by-landholding table",
        "figure": "Fig. 1 (perceptions of panchayat management capability)",
        "section": "Approach and methodology; Institutional dynamics; Provision of treated water in rural areas: public versus private; Concluding remarks and policy implications",
        "exact_location": "Institutional dynamics section (Tables 5-7, panchayat/foundation institutional models); coverage-by-landholding table (public versus private section); Table 4 (NPV/BCR financial viability)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Mixed-methods comparative case study of 8 villages in Andhra Pradesh, India, examining public-private-community institutional partnership models (panchayat resolutions, tripartite agreements, village development councils) for water treatment plant governance against household-level coverage, quantity, affordability, and inclusiveness outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9 (goes beyond water-quality-only framing to examine institutional governance of service delivery). Not effect_sizes eligible: descriptive comparative case-study design across 8 villages, no regression isolating institutional-arrangement effects on access. Extracted for record_id RBF205A6C9F47."
        ,
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
