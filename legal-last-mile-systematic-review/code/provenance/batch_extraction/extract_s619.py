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

    # S619: Robina Ramirez, De Clercq & Jackson 2019, Human Water Governance South Africa
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S619",
        "citation": "Robina Ramirez R, De Clercq W, Jackson MN (2019). Human Water Governance: A Social Innovation Model to Reduce the Inequalities of Water Services in South African Informal Settlements. In: Cagica Carvalho L et al. (eds), New Paths of Entrepreneurship Development, Studies on Entrepreneurship, Structural Change and Industrial Dynamics, Springer, pp. 231-252.",
        "doi": "10.1007/978-3-319-96032-6_12",
        "publication_year": "2019",
        "publication_type": "book chapter",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "South Africa",
        "subnational_unit": "Kayamandi and Enkanini informal settlements, Stellenbosch Municipality, Western Cape Province",
        "legal_system": "mixed (Roman-Dutch common law tradition with post-1994 constitutional/statutory water-rights framework)",
        "urban_rural": "urban (informal settlements)",
        "service_provider": "Stellenbosch Municipality (public water utility)",
        "regulatory_model": "Municipal by-law-based application/approval system for individual connections (Credit Control and Debt Collection By-laws), combined with free communal standpipe/on-site sanitation provision for non-qualifying households; governed by the National Water Act (36 of 1998), Water Services Act (1997), and Municipal Systems Act/Municipal Structures Act community-participation requirements",
        "population": "124 randomly-selected informal dwellers in Kayamandi and Enkanini informal settlements",
        "sample_size": "124",
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
        "documentation": "",
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
        "hardship_exception": "TRUE",
        "administrative_review": "",
        "complaint": "TRUE",
        "judicial_review": "TRUE",
        "disconnection": "",
        "reconnection": "",
        "sanction": "",
        "participation": "TRUE",
        "institutional_fragmentation": "",
        "political_coordination": "TRUE",
        "bureaucratic_assistance": "TRUE",
        "formal_connection": "TRUE",
        "water_access": "TRUE",
        "sanitation_access": "TRUE",
        "service_coverage": "TRUE",
        "service_reliability": "TRUE",
        "service_quantity": "TRUE",
        "service_quality": "TRUE",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "TRUE",
        "refusal": "",
        "delay_outcome": "TRUE",
        "effect_measure": "PLS-SEM standardized path coefficients (beta) with t-statistics and p-values",
        "effect_estimate": "Principles of Water Governance (PWG) -> Human Water Management (HWM) outcome construct: beta=0.265, t=3.523, p<0.001. Human Water Principles (HWP) -> HWM: beta=0.322, t=3.747, p<0.001. Water Principles (WP) -> HWM: beta=0.450, t=4.488, p<0.001. Model explains 55.4% of variance in HWM (R2=0.554). HWM composite construct includes items on eliminating communal taps, receiving equal water/wastewater sanitation service parity with formal neighbourhoods, and being assisted with water saving/conservation.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "<0.001 (H1-H3); <0.01 (H4-H5)",
        "extraction_sample_size": "124",
        "adjusted_or_unadjusted": "not applicable (PLS-SEM structural path model, not covariate-adjusted regression)",
        "covariates": "",
        "model_type": "Partial Least Squares Structural Equation Modeling (PLS-SEM)",
        "study_design": "cross-sectional survey with PLS-SEM hypothesis testing",
        "risk_of_bias_tool": "MMAT",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "2",
        "outcome_measurement_quality": "2",
        "mechanism_certainty": "Moderate: tests a defined institutional-governance construct (Principles of Water Governance, including legally-mandated participation, tariff transparency, Indigent Policy awareness) against a household-outcome construct (Human Water Management) using PLS-SEM path coefficients with statistical significance; however, both exposure and outcome are multi-item composite latent constructs rather than single well-defined legal-mechanism and access-outcome variables, and the small non-probability-adjacent sample (n=124 from an estimated 20,000-plus-dweller population) limits generalizability, as the authors themselves note in their effect-size discussion.",
        "source_document": "Robina Ramirez, De Clercq & Jackson 2019, New Paths of Entrepreneurship Development (Springer), pp. 231-252 (retrieved via Google Drive inbox)",
        "page": "231-252",
        "table": "Table 4 (path coefficients and statistical significance)",
        "figure": "Fig. 1 (Human Water Management model); Fig. 2 (final structural model with path coefficients)",
        "section": "3 A Case Study: Methodology; 4 Results; 5 Conclusions",
        "exact_location": "Section 3.1 (application-based connection requirement, By-laws quote); Section 2.1 (National Water Act/Water Services Act minimum free basic water); Section 2.2.2 (Municipal Systems Act/Municipal Structures Act community-participation legal requirement); Table 4 (path coefficients)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). PLS-SEM survey of 124 informal dwellers in Kayamandi/Enkanini, Stellenbosch, South Africa, documenting municipal by-law application-based connection requirements, statutory free-basic-water entitlements, legally-required community participation, and Enkanini's contested illegal-settlement status, against household-level water/sanitation access, service-parity, and affordability outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: exposure and outcome are multi-item composite SEM latent constructs rather than a single identifiable legal/institutional exposure tested against a single identifiable access/outcome measure. Extracted for record_id RAFC08D21DB57.",
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
