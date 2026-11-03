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

    assert "S583" not in {r["study_id"] for r in rows}

    s583 = blank_row(fieldnames)
    s583.update({
        "study_id": "S583",
        "citation": "Hallstrom J (2005). Technology, social space and environmental justice in Swedish cities: water distribution to suburban Norrkoping and Linkoping, 1860-90. Urban History 32(3):413-433.",
        "doi": "10.1017/S0963926805003214",
        "publication_year": "2005",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Sweden",
        "subnational_unit": "Norrkoping and Linkoping (primary case cities); secondary material on Stockholm and Malmo suburbs",
        "legal_system": "civil law",
        "urban_rural": "mixed (working-class suburbs adjoining planned urban areas)",
        "service_provider": "Norrkoping Waterworks Board (municipal); Linkoping Water Company (part-municipal, 20% city-owned joint stock company)",
        "regulatory_model": "Swedish national urban building code, fire-protection law, and public-health law applied only within a city's formally designated 'planned area'; adjoining suburbs fell under separate rural-district administration and were exempt from these codes unless annexed or designated a municipalsamhalle; water-pipe extension decisions made at the discretion of the City Council/Waterworks Board (Norrkoping) or the part-municipal Water Company (Linkoping), financed via a '10 percent rule' requiring projected fee revenue to exceed 10% of construction cost within 10 years, and connection fees charged directly to building owners",
        "population": "Working-class suburban residents (Norrkoping's northern suburb; Linkoping's Ladugardsbacke suburb) seeking connection to municipal piped water systems, 1860-1890",
        "sample_size": "Historical case-comparative study of 2 primary cities (Norrkoping, Linkoping) plus secondary-source comparison with 2 further cities (Stockholm, Malmo); primary sources include City Council and Waterworks/Water Company meeting minutes and contemporary newspaper accounts",
        "household_level": "TRUE",
        "community_level": "TRUE",
        "income_group": "low-income (working-class suburbs)",
        "tenure_status": "TRUE",
        "legal_status": "TRUE",
        "indigenous_population": "",
        "migrant_population": "TRUE",
        "eligibility": "TRUE",
        "burden": "TRUE",
        "discretion_accommodation": "TRUE",
        "enforcement": "",
        "documentation": "",
        "tenure": "",
        "property": "TRUE",
        "planning": "TRUE",
        "zoning": "TRUE",
        "building_permit": "TRUE",
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
        "bureaucratic_assistance": "",
        "formal_connection": "TRUE",
        "water_access": "TRUE",
        "sanitation_access": "TRUE",
        "service_coverage": "TRUE",
        "service_reliability": "",
        "service_quantity": "",
        "service_quality": "",
        "affordability": "TRUE",
        "service_continuity": "",
        "application_success": "TRUE",
        "refusal": "TRUE",
        "delay_outcome": "TRUE",
        "effect_measure": "historical archival case-comparative analysis (no quantitative effect estimate)",
        "effect_estimate": "",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "",
        "adjusted_or_unadjusted": "",
        "covariates": "",
        "model_type": "historical case-comparative documentary analysis of primary archival sources (council minutes, water company records, newspaper accounts)",
        "study_design": "historical qualitative case-comparative study",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "2",
        "mechanism_certainty": "Moderate-high: documents a concrete, quotable legal-institutional mechanism (planned-area boundary determining applicability of building/health/fire codes; discretionary City Council/Waterworks Board/Water Company decisions on extension requests; the '10 percent rule' financing criterion) with primary archival sources (council minutes, contemporary newspaper transcripts of debates) directly recording the connection/refusal outcome for named suburbs, though the study is a qualitative historical case-comparison rather than a controlled exposure-comparator design.",
        "source_document": "Hallstrom 2005, Urban History 32(3):413-433 (retrieved via Google Drive inbox, Linkoping University postprint)",
        "page": "413-433",
        "table": "Table 1 (population growth); Tables 2-3 (city populations)",
        "figure": "Figure 3 (Norrkoping water system 1896); Figure 4 (Linkoping water system 1900)",
        "section": "City versus Suburb - the Extension of Water; Water Distribution to Workers' Suburbs in Other Swedish Cities; Cities, Working-Class Suburbs and Water Distribution in Perspective; Conclusions",
        "exact_location": "Norrkoping 1886 City Council/Waterworks Board debate over extending a water pipe to the northern suburb (eventually approved, 200-metre extension, fee-based); Linkoping 1881 City Council rejection of Ladugardsbacke's water-connection request (denied until 1921 despite 1911 annexation)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Genuine household/property-level legal-institutional content: the planned-area/rural-district administrative boundary determining applicability of national building, fire, and public-health codes; discretionary municipal water-authority decisions on extension requests from working-class suburbs; the '10 percent rule' extension-financing criterion; and fee-based connection charged to building owners, drawn from primary archival council-minute and newspaper sources. record_id R546EB2436B96.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })

    extra = set(s583.keys()) - set(fieldnames)
    assert not extra, f"unexpected fields: {extra}"
    missing = set(fieldnames) - set(s583.keys())
    assert not missing, f"missing fields: {missing}"

    rows.append(s583)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    print(f"done, extraction rows now {len(rows)}")

if __name__ == "__main__":
    main()
