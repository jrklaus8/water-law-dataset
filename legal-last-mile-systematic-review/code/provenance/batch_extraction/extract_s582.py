import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

def blank_row(fieldnames):
    return {k: "" for k in fieldnames}

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    assert "S582" not in {r["study_id"] for r in rows}

    s582 = blank_row(fieldnames)
    s582.update({
        "study_id": "S582",
        "citation": "Jambadu L, Pilo' F, Monstadt J (2024). Co-producing maintenance and repair: hybrid labor relations in water supply in Accra, Ghana. Urban Research & Practice 17(2):280-302.",
        "doi": "10.1080/17535069.2023.2180325",
        "publication_year": "2024",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Ghana",
        "subnational_unit": "Nima (informal settlement) and Dodowa (peri-urban), Greater Accra Metropolitan Area",
        "legal_system": "common law",
        "urban_rural": "mixed (Nima urban informal settlement; Dodowa peri-urban)",
        "service_provider": "Ghana Water Company Limited (GWCL, urban areas); Community Water and Sanitation Agency (CWSA) and community-level Water and Sanitation Management Teams (WSMTs, peri-urban/rural areas); private plumbers/area mechanics; households",
        "regulatory_model": "GWCL regulated by the Public Utilities Regulatory Commission (PURC) and Water Resource Commission (WRC), with the Ministry of Sanitation and Water Resources providing policy direction; household responsibility for private-connection maintenance under national water-sector policy, usually outsourced to private plumbers; decentralized CWSA/WSMT framework for peri-urban/rural community water-system maintenance and repair; legality/illegality distinction for private water connections independent of formal/informal practice distinction",
        "population": "Households, private plumbers, GWCL officials, and community water-management actors in Nima and Dodowa",
        "sample_size": "48 semi-structured interview respondents (GWCL officials, local plumbers, residents, small-business owners, government administration representatives) plus field observations, 2018-2020",
        "household_level": "TRUE",
        "community_level": "TRUE",
        "income_group": "mixed (Nima low-income; Dodowa middle/high-income)",
        "tenure_status": "",
        "legal_status": "TRUE",
        "indigenous_population": "",
        "migrant_population": "",
        "eligibility": "",
        "burden": "TRUE",
        "discretion_accommodation": "TRUE",
        "enforcement": "TRUE",
        "documentation": "",
        "tenure": "",
        "property": "",
        "planning": "",
        "zoning": "",
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
        "disconnection": "TRUE",
        "reconnection": "",
        "sanction": "TRUE",
        "participation": "TRUE",
        "institutional_fragmentation": "TRUE",
        "political_coordination": "TRUE",
        "bureaucratic_assistance": "TRUE",
        "formal_connection": "TRUE",
        "water_access": "TRUE",
        "sanitation_access": "",
        "service_coverage": "TRUE",
        "service_reliability": "TRUE",
        "service_quantity": "",
        "service_quality": "",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "",
        "refusal": "TRUE",
        "delay_outcome": "TRUE",
        "effect_measure": "qualitative thematic/content analysis (no quantitative effect estimate)",
        "effect_estimate": "",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "",
        "adjusted_or_unadjusted": "",
        "covariates": "",
        "model_type": "qualitative case-study content/thematic analysis of semi-structured interviews and field observations",
        "study_design": "qualitative comparative case study (two neighborhoods)",
        "risk_of_bias_tool": "CASP",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "2",
        "mechanism_certainty": "Moderate-high: documents concrete legal-institutional content (GWCL/PURC/WRC regulatory framework, the legality/illegality distinction for private connections and self-repair, household maintenance obligations, and the CWSA/WSMT decentralized governance framework) with named informants and triangulated interview/observation data across two contrasting neighborhoods, though the study is descriptive/qualitative rather than a controlled exposure-comparator design.",
        "source_document": "Jambadu, Pilo' & Monstadt 2024, Urban Research & Practice 17(2):280-302 (retrieved via Google Drive inbox)",
        "page": "280-302",
        "table": "Table 1 (water infrastructure systems in Nima and Dodowa)",
        "figure": "Figure 1 (map); Figures 2-3 (water connections); Figures 4-6 (repair operations)",
        "section": "Results (sections 6-8); Conclusion",
        "exact_location": "Section 6 (GWCL public maintenance/repair system); Section 7 (private plumbers' role, 7.1 Nima, 7.2 Dodowa); Section 8 (hybrid public/private labor relations)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Genuine household-level legal-institutional content: GWCL's PURC/WRC-regulated public maintenance mandate, the legality/illegality distinction for private and illegal water connections and informal self-repair practices, household responsibility for private-connection maintenance under national water-sector policy, and Ghana's decentralized CWSA/WSMT community water-management framework. record_id RE48029A5D3C0.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })

    extra = set(s582.keys()) - set(fieldnames)
    assert not extra, f"unexpected fields: {extra}"
    missing = set(fieldnames) - set(s582.keys())
    assert not missing, f"missing fields: {missing}"

    rows.append(s582)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    print(f"done, extraction rows now {len(rows)}")

if __name__ == "__main__":
    main()
