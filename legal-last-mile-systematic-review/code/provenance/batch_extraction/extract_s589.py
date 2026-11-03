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

    assert "S589" not in {r["study_id"] for r in rows}

    s589 = blank_row(fieldnames)
    s589.update({
        "study_id": "S589",
        "citation": "World Bank; Inter-American Development Bank (2004). Ecuador: Creating Fiscal Space for Poverty Reduction -- A Fiscal Management and Public Expenditure Review, Volume I: Main Report. Report No. 28911-EC.",
        "doi": "",
        "publication_year": "2004",
        "publication_type": "report",
        "language": "English",
        "peer_reviewed": "FALSE",
        "country": "Ecuador",
        "subnational_unit": "National fiscal analysis; household case study of Machala, El Oro province",
        "legal_system": "civil law",
        "urban_rural": "mixed (national fiscal analysis, with an urban case study)",
        "service_provider": "Decentralized municipal water/sanitation providers; Ministerio de Desarrollo Urbano y Vivienda (MIDUVI, national transfers for municipal investment)",
        "regulatory_model": "Water and sanitation services are fully decentralized to municipal governments, with the Central Government's role limited to quality/efficiency oversight and coverage guarantees; no integrated national system for managing water resources; incomplete regulatory and institutional frameworks (in contrast to the electricity sector); MIDUVI transfers for municipal water investment cut from US$52 million (2001) to US$5 million (2002)",
        "population": "Ecuadorian households by income quintile (national subsidy-incidence analysis); households with versus without a formal water connection in Machala, El Oro province (illustrative case study)",
        "sample_size": "National quintile-level subsidy-incidence analysis (Table 3.4, based on 1990s household income distribution/LSMS 1994 data); household case comparison in Machala (Box 3.2, sourced from Yepes, Gomez and Carvajal 2002 and Sotomayor 2004)",
        "household_level": "TRUE",
        "community_level": "TRUE",
        "income_group": "mixed (quintile-disaggregated; explicit poorest-vs-richest comparison)",
        "tenure_status": "",
        "legal_status": "",
        "indigenous_population": "",
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
        "political_coordination": "TRUE",
        "bureaucratic_assistance": "",
        "formal_connection": "TRUE",
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
        "effect_measure": "descriptive quintile-based subsidy-incidence analysis; illustrative case-comparison table (connected vs. unconnected household expenditure)",
        "effect_estimate": "Water subsidy incidence, 2003 (Table 3.4): US$5.3M (7.9%) to poorest quintile vs. US$28.0M (41.3%) to richest quintile, of US$67.5M total -- top two quintiles capture about two-thirds of water subsidies. Machala case (Box 3.2): connected households consume ~15 m3/month for ~US$1.20 (0.4% of monthly family income); unconnected households served by tankers consume ~4-5 m3/month for ~US$29.00 (9.0% of monthly family income) -- roughly 22.5x higher per-unit cost and 3x lower consumption for unconnected households.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "",
        "adjusted_or_unadjusted": "unadjusted (descriptive quintile/case comparison, not a regression-adjusted estimate)",
        "covariates": "",
        "model_type": "Descriptive fiscal subsidy-incidence analysis (World Bank staff estimate) plus an illustrative secondary-sourced household case comparison",
        "study_design": "Government/multilateral fiscal-policy review with an embedded quantitative subsidy-incidence analysis and household case illustration",
        "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "Moderate -- the Machala household comparison (Box 3.2) is drawn from another secondary source (Yepes, Gomez and Carvajal 2002) rather than this report's own primary data collection",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "2",
        "outcome_measurement_quality": "2",
        "mechanism_certainty": "Moderate: water/sanitation is a minor sub-topic of a much larger multi-sector (electricity, telecom, education, health, pensions, oil) national fiscal-management report, covered in only about 3 of the document's many pages, but within that sub-section the report presents its own original quantile-based subsidy-incidence estimate for water specifically and a concrete household-level illustration (connection status directly associated with a roughly 22-fold difference in per-unit water cost and a 3-fold difference in consumption) tied to decentralized, under-resourced municipal water governance institutions.",
        "source_document": "World Bank/IDB 2004, Report No. 28911-EC, Volume I (retrieved via Google Drive inbox, Antigravity retrieval)",
        "page": "vii, 45-48",
        "table": "Table 3.4 (Basic Services Subsidies by Expenditure Quintile, 2003)",
        "figure": "",
        "section": "Chapter 3, Subsidies in Basic Infrastructure Services; Box 3.2, Household Expenditures on Water: The Case of Machala, El Oro",
        "exact_location": "Paragraphs 3.15-3.18 and Table 3.4 (water subsidy incidence by quintile); Box 3.2 (Machala connected vs. unconnected household water expenditure comparison)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Water/sanitation is one of several sectors covered in this multi-sector national fiscal review; only the water/sanitation-relevant subsection was extracted. Documents genuine institutional/regulatory content (full decentralization of water/sanitation provision to municipalities, incomplete regulatory/institutional frameworks, declining MIDUVI transfers) alongside an original World-Bank-staff quantitative subsidy-incidence estimate specific to water and a household-level affordability comparison by connection status in Machala. record_id R98669D9A19CA.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })

    extra = set(s589.keys()) - set(fieldnames)
    assert not extra, f"unexpected fields: {extra}"
    missing = set(fieldnames) - set(s589.keys())
    assert not missing, f"missing fields: {missing}"

    rows.append(s589)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    print(f"done, extraction rows now {len(rows)}")

if __name__ == "__main__":
    main()
