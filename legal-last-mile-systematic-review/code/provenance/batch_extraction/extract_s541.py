import csv, tempfile, os

path = "03_extraction/extracted_data/extraction_database.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

def blank_row():
    return {k: "" for k in fieldnames}

row = blank_row()
row.update({
    "study_id": "S541",
    "citation": 'Singh V, Pandey A (2020). "Urban water resilience in Hindu Kush Himalaya: issues, challenges and way forward." Water Policy, 22(S1), 33-45.',
    "doi": "10.2166/wp.2019.329",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Multi-country: Afghanistan, Pakistan, India, Nepal, China, Bhutan",
    "subnational_unit": "Hindu Kush Himalaya (HKH) region; 8 named urban centres: Kabul, Quetta, Shimla, Mussoorie, Nainital, Kathmandu, Xining, Thimphu, plus additional Indian Himalayan towns (Almora, Dharamshala, Gangtok, Srinagar, Leh, Manali, Palampur)",
    "legal_system": "mixed (civil law and common law across the 6 countries; municipal bye-laws and groundwater abstraction regulations discussed generically, not jurisdiction-specific statutory citation)",
    "urban_rural": "urban (mountain/hill towns and cities)",
    "service_provider": "Municipal/city water utilities and water supply agencies (e.g., Nepal Drinking Water Corporation for Pokhara, Afghanistan Urban Water Supply and Sewerage Company for Kabul, Water and Sanitation Agency for Quetta), supplemented by informal tanker operators",
    "regulatory_model": "Groundwater abstraction policies exist in municipal bye-laws in multiple HKH towns (cited: Quetta, Kabul, Dehradun, Haldwani) but are described as seldom enforced due to the political influence of informal water-tanker operators ('tanker mafia'); artificial low water pricing and absence of metering/differential pricing across most towns; institutional fragmentation across multiple departments/agencies responsible for water supply, management, and infrastructure maintenance, operating in silos with limited coordination.",
    "population": "Urban residents of HKH towns and cities, with explicit attention to socio-economically weaker/poor households who cannot afford premium-priced tanker water",
    "sample_size": "8 cities with quantitative supply/demand data (Table 1); additional qualitative case discussion of ~10 further Indian Himalayan towns",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
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
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "TRUE",
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
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "Descriptive comparative synthesis (secondary-data compilation across 8 cities, no statistical contrast)",
    "effect_estimate": "Groundwater abstraction bye-laws exist in multiple towns (Quetta, Kabul, Dehradun, Haldwani) but are 'seldom followed,' with illegal/unregulated borewell proliferation attributed to weak enforcement and the political influence of informal tanker operators. Supply-demand gaps documented across 8 cities (Table 1): Kabul supplies only ~20% of population (15 Lpcd); Quetta has a 50% deficit (106 MLD supply vs. 170 MLD demand); Kathmandu Valley faces a 210 MLD shortfall (~70% gap); Shimla meets 84.2% of demand. Only the affluent can afford premium-priced tanker water (Kabul residents pay $0.36/unit for tanker deliveries); poor/socio-economically weaker areas experience recurring 'zero day' water cutoffs even where aggregate scarcity is not severe, reflecting inequitable distribution rather than pure physical scarcity. Absence of water metering and differential pricing across most towns is linked to inefficient use and poor demand management.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "8",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "narrative policy synthesis (secondary-data/literature compilation plus author field observations from the HI-AWARE research consortium; no systematic-review search protocol)",
    "study_design": "narrative synthesis / policy-review case-study compilation across 8 Hindu Kush Himalaya cities, drawing on secondary literature, project reports, and author field observations",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "",
    "outcome_measurement_quality": "",
    "mechanism_certainty": "3",
    "source_document": "Singh & Pandey 2020, Water Policy 22(S1):33-45",
    "page": "",
    "table": "Table 1",
    "figure": "Figure 2",
    "section": "Development of urban centres and water crises in major cities of HKH; Key issues and challenges for urban water resilience in HKH; Recommendations",
    "exact_location": "Table 1 (demand/supply and major issues in 8 selected cities); Figure 2 (challenges and issues related to urban water management in HKH, including 'Poor Governance', 'Lack of institutional reforms', 'Exclusive decision making', 'Selective water distribution')",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Documents legal-administrative/governance mechanisms across 8 HKH cities: groundwater abstraction bye-laws that exist but are seldom enforced (Quetta, Kabul, Dehradun, Haldwani), attributed partly to the political influence of informal tanker-water operators; absence of metering and differential pricing; institutional fragmentation across water-supply/management departments operating in silos; inequitable 'zero day' distribution disproportionately affecting socio-economically weaker areas; and unaffordable tanker-water pricing as the de facto supply mechanism where formal municipal supply is deficient. Not a systematic review (no described search protocol), so appraised with the project's Legal Institutional Evidence Appraisal Framework rather than AMSTAR 2. record_id R08C74B34D928.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-21",
    "evidence_status": "OBSERVED",
})

rows.append(row)

fd, tmp = tempfile.mkstemp(dir="03_extraction/extracted_data")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, path)

print("done, extraction rows now", len(rows))
