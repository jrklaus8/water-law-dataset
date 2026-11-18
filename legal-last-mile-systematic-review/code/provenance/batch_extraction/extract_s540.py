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
    "study_id": "S540",
    "citation": 'Silva-Novoa Sanchez LM, Bossenbroek L, Schilling J, Berger C (2022). "Governance and Sustainability Challenges in the Water Policy of Morocco 1995-2020." Water, 14(18), 2932.',
    "doi": "10.3390/w14182932",
    "publication_year": "2022",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Morocco",
    "subnational_unit": "Sais plain (Meknes region), and Souss-Massa region case studies",
    "legal_system": "civil law (with customary/tribal land tenure institutions)",
    "urban_rural": "rural and peri-urban (smallholder and commercial irrigated agriculture; unconnected rural households)",
    "service_provider": "ORMVA (Regional Agricultural Development Offices), ABH (river basin agencies), Ministry of Interior (caidat/local administration), and ONEE (national water/electricity utility) for drinking water",
    "regulatory_model": "1995 Water Law (Law 10-95) and its 2016 successor (Law 36-15) establishing permit-based groundwater/well abstraction rights, river-basin agencies (ABH), and a fragmented multi-ministry governance structure (Ministry of Agriculture, Ministry of Interior, Ministry of Water)",
    "population": "Smallholder and commercial farmers, tribal land users, and rural households in the Sais plain and Souss-Massa region",
    "sample_size": "37 semi-structured interviews with farmers, local officials, and water administrators, plus document/content analysis of policy texts",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "tribal/collective land tenure (soulaliyate) alongside private/melk land tenure",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "TRUE",
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "TRUE",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "37",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative content analysis of water policy documents (1995-2020) combined with 37 semi-structured interviews with farmers, local officials, and water administrators in the Sais plain and Souss-Massa region",
    "risk_of_bias_tool": "CASP Qualitative Studies Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "",
    "outcome_measurement_quality": "",
    "mechanism_certainty": "3",
    "source_document": "Silva-Novoa Sanchez et al 2022, Water 14(18):2932",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Results; Discussion",
    "exact_location": "Section 3 (well-digging permits and illegal drilling); Section 4 (drip-irrigation subsidy eligibility and land tenure documentation circularity); Section 5 (institutional fragmentation between Agriculture/Water/Interior ministries)",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Documents legal-administrative access mechanisms: well-digging permits requiring bribery to obtain, drip-irrigation subsidy eligibility contingent on tribal land-use certificates that themselves require a digging permit (chicken-and-egg exclusion of tenure-insecure farmers), institutional fragmentation between Ministry of Agriculture (subsidies), Ministry of Water (permits), and Ministry of Interior/caidat (land certification), unequal Kharouba water-rights share allocation among farmers (1/8, 1/4 shares), and unconnected/intermittent rural drinking-water households. record_id R9FFEBB4E1EFA.",
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
