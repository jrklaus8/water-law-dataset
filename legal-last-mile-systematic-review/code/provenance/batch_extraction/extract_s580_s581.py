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

    existing_ids = {r["study_id"] for r in rows}
    assert "S580" not in existing_ids and "S581" not in existing_ids

    new_rows = []

    # S580 -- Craps et al. 2004, Andes indigenous/professional community negotiation
    s580 = blank_row(fieldnames)
    s580.update({
        "study_id": "S580",
        "citation": "Craps M, Dewulf A, Mancero M, Santos E, Bouwen R (2004). Constructing Common Ground and Re-Creating Differences Between Professional and Indigenous Communities in the Andes. Journal of Community & Applied Social Psychology 14(5):378-393.",
        "doi": "10.1002/casp.796",
        "publication_year": "2004",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Ecuador",
        "subnational_unit": "Chambo river subbasin, Chimborazo province, central Andean highlands",
        "legal_system": "civil law",
        "urban_rural": "rural",
        "service_provider": "Indigenous irrigation-water-user organizations/communities; provincial development professionals and NGOs facilitating the Interinstitutional Consortium for the Sustainable Development of the Chambo River Subbasin",
        "regulatory_model": "Formation of a new legal 'consortium' (Interinstitutional Consortium) as an institutional mechanism to formalize water/land-use governance across indigenous communities and professional/state institutions; use of indigenous communities' legal land titles and a judicial workshop process in negotiating water-related resource governance",
        "population": "Indigenous highland communities and development professionals negotiating water and natural-resource governance in the Chambo river subbasin",
        "sample_size": "Qualitative case study; participant observation and interviews with indigenous community members and development professionals across multiple negotiation/workshop events (exact respondent count not separately tabulated)",
        "household_level": "",
        "community_level": "TRUE",
        "income_group": "",
        "tenure_status": "TRUE",
        "legal_status": "TRUE",
        "indigenous_population": "TRUE",
        "migrant_population": "",
        "eligibility": "",
        "burden": "",
        "discretion_accommodation": "TRUE",
        "enforcement": "",
        "documentation": "TRUE",
        "tenure": "TRUE",
        "property": "TRUE",
        "planning": "TRUE",
        "zoning": "",
        "building_permit": "",
        "service_area": "TRUE",
        "fees": "",
        "procedural_steps": "TRUE",
        "delay": "",
        "discretion": "TRUE",
        "hardship_exception": "",
        "administrative_review": "",
        "complaint": "",
        "judicial_review": "TRUE",
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
        "service_coverage": "",
        "service_reliability": "",
        "service_quantity": "",
        "service_quality": "",
        "affordability": "",
        "service_continuity": "",
        "application_success": "",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "qualitative case narrative (no quantitative effect estimate)",
        "effect_estimate": "",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "",
        "adjusted_or_unadjusted": "",
        "covariates": "",
        "model_type": "qualitative case study; process/discourse analysis of negotiation events",
        "study_design": "qualitative case study of an intergroup negotiation process over resource governance",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "2",
        "outcome_measurement_quality": "2",
        "mechanism_certainty": "Moderate: documents concrete legal-institutional artefacts (indigenous land titles, a judicial workshop, formation of a new interinstitutional legal consortium) shaping water/resource governance negotiations between indigenous communities and professionals, but as a qualitative process case study without a quantified access outcome.",
        "source_document": "Craps et al. 2004, Journal of Community & Applied Social Psychology 14(5):378-393 (retrieved via Google Drive inbox)",
        "page": "",
        "table": "",
        "figure": "",
        "section": "Case description; Discussion",
        "exact_location": "Case narrative sections describing land-title recognition, the judicial workshop, and consortium formation",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Genuine legal-institutional content: indigenous communities' legal land titles, a judicial workshop process, and the creation of a new legal 'consortium' structure to govern subbasin water/natural-resource issues between indigenous communities and professional/state institutions. record_id R7D3F1DFC2F82.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })
    new_rows.append(s580)

    # S581 -- Hess et al. 2016, Drought Risk Institutional Politics American Southwest
    s581 = blank_row(fieldnames)
    s581.update({
        "study_id": "S581",
        "citation": "Hess DJ, Wold CA, Hunter E, Nay J, Worland S, Gilligan J, Hornberger GM (2016). Drought, Risk, and Institutional Politics in the American Southwest. Sociological Forum 31(S1):807-827.",
        "doi": "10.1111/socf.12274",
        "publication_year": "2016",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "United States",
        "subnational_unit": "22 largest metropolitan statistical areas (MSAs) in the extended American Southwest (AZ, CA, CO, NV, NM, OK, TX, UT)",
        "legal_system": "common law",
        "urban_rural": "urban",
        "service_provider": "City water departments/utilities of the 22 largest MSAs in the extended American Southwest",
        "regulatory_model": "Municipal water-supply-strategy regime (supply-increase vs demand-reduction) analyzed via institutional logics (development, preservation, environmental, consumer); Vanderbilt Water Conservation Index (VWCIb), a 117-metric count of city water-conservation ordinances/pricing policies/mandates/incentives",
        "population": "Central cities of the 22 largest MSAs in the American Southwest and their water-supply/conservation policy regimes",
        "sample_size": "22 cities (qualitative conflict-coding of media reports; VWCIb index constructed from public documents/ordinances for all 22 cities; quantitative decision-tree/random-forest regression, n=22)",
        "household_level": "",
        "community_level": "TRUE",
        "income_group": "",
        "tenure_status": "",
        "legal_status": "",
        "indigenous_population": "TRUE",
        "migrant_population": "",
        "eligibility": "",
        "burden": "TRUE",
        "discretion_accommodation": "TRUE",
        "enforcement": "TRUE",
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
        "judicial_review": "TRUE",
        "disconnection": "",
        "reconnection": "",
        "sanction": "TRUE",
        "participation": "TRUE",
        "institutional_fragmentation": "TRUE",
        "political_coordination": "TRUE",
        "bureaucratic_assistance": "",
        "formal_connection": "",
        "water_access": "TRUE",
        "sanitation_access": "",
        "service_coverage": "",
        "service_reliability": "TRUE",
        "service_quantity": "TRUE",
        "service_quality": "",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "decision-tree regression and random-forest variable-importance ranking (VWCIb score as dependent variable)",
        "effect_estimate": "Decision-tree model: lowest VWCIb scores (14) predicted for MSAs with negative (more Republican) Partisan Voting Index (PVI < -1.3) and precipitation >90cm/yr (n=2: Tulsa, Houston); highest VWCIb scores (48) predicted for MSAs with positive PVI (>1.3) and regional price parity >105 (n=6: Los Angeles, Oxnard-Ventura, Riverside-San Bernardino, San Diego, San Francisco, San Jose). Random-forest variable-importance analysis: PVI is by far the most important predictor of VWCIb (removing PVI increases prediction error by ~20%), followed by regional price parity and precipitation; removing the drought variable decreases prediction error by ~5%. Paired-city qualitative contrasts: Austin (VWCIb 46, PVI 8.25) vs Dallas-Fort Worth (VWCIb 28, PVI -3.61); Albuquerque (VWCIb 43, PVI 10.80) vs Phoenix (VWCIb 20, PVI -3.14) -- more Democratic-leaning MSAs have substantially higher water-conservation-policy index scores.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "22 MSAs",
        "adjusted_or_unadjusted": "adjusted (random-forest model considers multiple sociopolitical and hydrological predictors simultaneously: population, population growth, regional price parity, PVI, temperature, precipitation, surface-water dependence, drought duration)",
        "covariates": "Population, population growth, regional price parity, Partisan Voting Index, mean annual temperature, mean annual precipitation, percent surface-water supply, longest drought duration (Palmer Hydrological Drought Index)",
        "model_type": "Mixed-methods: qualitative institutional-logics conflict coding of media reports (Table III) plus quantitative decision-tree and random-forest regression (VWCIb as dependent variable)",
        "study_design": "Mixed-methods cross-sectional comparative study of 22 MSAs (qualitative document/media analysis plus quantitative decision-tree/random-forest modeling)",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "Low (all 22 largest Southwest MSAs included, not a sample)",
        "measurement_bias": "Moderate (VWCIb constructed by the research team from public ordinances/documents; cross-validated against AWWA survey data, r=0.7)",
        "confounding": "Moderate; addressed via multivariate random-forest modeling of sociopolitical and hydrological predictors jointly",
        "attrition": "",
        "reporting_bias": "Low (small-n caveats explicitly discussed; mixed/contradictory qualitative conflict cases reported transparently)",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate-high: documents genuine legal/institutional water-supply governance content (litigation over water rights, reservoir/pipeline permitting conflicts, tiered-pricing ordinances, conservation mandates and enforcement, tribal water-rights litigation) with both a systematic qualitative institutional-logics conflict analysis and a quantitative model of political/regulatory predictors of conservation-policy adoption, though the dependent variable (VWCIb) is a policy-adoption index rather than a directly measured household access/affordability outcome.",
        "source_document": "Hess et al. 2016, Sociological Forum 31(S1):807-827 (retrieved via Google Drive inbox)",
        "page": "807-827",
        "table": "Table I (supply-increase strategies); Table II (VWCIb scores); Table III (political conflicts by institutional logic)",
        "figure": "Figure 1 (regression tree and variable-importance plot)",
        "section": "Results: Research Question 1 (qualitative); Results: Research Question 2 (quantitative); Discussion",
        "exact_location": "Table III (political-conflict cases by institutional logic, e.g., Choctaw/Chickasaw Nations litigation over Sardis Lake, San Antonio Vista Ridge ratepayer opposition, Tucson pricing/mandate conflicts); Figure 1 and accompanying text (decision-tree and random-forest PVI results)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Documents genuine institutional/regulatory water-supply-policy content at the municipal/regulatory unit of analysis: litigation over water rights (e.g., Choctaw/Chickasaw Nations v. Oklahoma City Water Utilities Trust), tiered-pricing and conservation-mandate ordinances, ratepayer/consumer-logic opposition to infrastructure cost pass-through, and a quantitative model identifying political/regulatory predictors (Partisan Voting Index) of water-conservation-policy adoption across 22 municipalities. record_id R1F5F1AA03B4D.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })
    new_rows.append(s581)

    for row in new_rows:
        extra = set(row.keys()) - set(fieldnames)
        assert not extra, f"unexpected fields in {row['study_id']}: {extra}"
        missing = set(fieldnames) - set(row.keys())
        assert not missing, f"missing fields in {row['study_id']}: {missing}"

    rows.extend(new_rows)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    print(f"done, extraction rows now {len(rows)}")

if __name__ == "__main__":
    main()
