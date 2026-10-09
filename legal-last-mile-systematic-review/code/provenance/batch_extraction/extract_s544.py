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
    "study_id": "S544",
    "citation": 'Turley B, Caretta MA (2020). "Household Water Security: An Analysis of Water Affect in the Context of Hydraulic Fracturing in West Virginia, Appalachia." Water, 12(1), 147.',
    "doi": "10.3390/w12010147",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "United States",
    "subnational_unit": "Northwestern West Virginia, Appalachia (Marshall, Doddridge, Harrison, Kanawha, Marion, Monongalia, Ritchie, Tyler, Upshur, Wetzel counties)",
    "legal_system": "common law",
    "urban_rural": "rural (low-population-density counties)",
    "service_provider": "Household private groundwater wells (approximately two-thirds of research participants), with oil and gas companies' hired third-party contractors conducting mandated water testing",
    "regulatory_model": "West Virginia code 22-6A-18 (2013 Natural Gas Horizontal Well Control Act) establishes 'presumed liability': oil and gas companies are presumed liable for water-quality changes if a pre-drill and post-drill test show impact, changes occur within 6 months, and the water well is within 1500 feet of the gas well head; companies' own hired contractors conduct the mandated baseline and post-drill testing; oil and gas extraction is exempt from the federal Safe Drinking Water Act ('the Halliburton Loophole'), so industry-generated water-quality data are not made public; WV mandates setback distances of 250 feet from an existing water well/spring and 625 feet from an occupied building, based on government compromise rather than public-health science; USEPA does not regulate private water wells; WVDEP manages Underground Injection Control permits but a Natural Resources Defense Council report found it failed to enforce Safe Drinking Water Act UIC requirements (wastewater injected under expired permits, over half of wells abandoned unplugged).",
    "population": "Mineral owners, surface owners, and concerned citizens in 8 northwestern West Virginia counties near Marcellus/Utica shale hydraulic-fracturing development",
    "sample_size": "30 semi-structured in-depth interviews (April-July 2018)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "TRUE",
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
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "TRUE",
    "judicial_review": "TRUE",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "TRUE",
    "effect_measure": "Qualitative thematic analysis (NVivo-coded, provisional coding) of 30 semi-structured interviews; no statistical contrast",
    "effect_estimate": "Residents' household groundwater security is undermined by uneven power relations built into the presumed-liability testing regime: water test results were frequently delayed by months, with residents in some cases learning only via FOIA requests that their water had already tested positive for contamination (e.g., E. coli, elevated arsenic and sodium) while continuing to drink it for months unknowingly. Presumed liability does not apply, and residents bear testing costs out-of-pocket, if the well is beyond the 1500-foot distance, if changes occur after 6 months, or if the company disputes causation (e.g., attributing arsenic to natural background levels). Non-disclosure agreements accompanying company buyouts or remediation suppress residents' ability to discuss confirmed contamination. Loss of usable water can render a home effectively unsellable, threatening residents' retirement savings and property value, while the company bears no equivalent financial risk. Residents report chronic anxiety, uncertainty, and mental stress that outweighs the economic benefits (jobs, tax revenue, mineral royalties) some also receive from extraction.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "30",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative case study (feminist epistemology, purposive snowball sampling, semi-structured interviews, member checking)",
    "study_design": "qualitative case study of household groundwater security and water affect around hydraulic fracturing, based on 30 in-depth semi-structured interviews with mineral owners, surface owners, and concerned citizens in northwestern West Virginia",
    "risk_of_bias_tool": "CASP Qualitative Studies Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "",
    "outcome_measurement_quality": "",
    "mechanism_certainty": "2",
    "source_document": "Turley & Caretta 2020, Water 12(1):147",
    "page": "",
    "table": "",
    "figure": "",
    "section": "5. Water Affect in the Marcellus Shale (5.1 Power; 5.2 Emotional and Mental Stress)",
    "exact_location": "Section 3 (WV code 22-6A-18 presumed liability, setback distances, Safe Drinking Water Act exemption); Section 5.1 (delayed/incomplete industry-controlled water testing, NDAs, presumed-liability distance/time limits); Section 5.2 (property-value loss, financial and mental-health burdens)",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Documents a genuine legal-administrative access regime governing household groundwater security: WV's presumed-liability statute conditions legal protection on distance (1500 ft) and time (6-month) thresholds set by government compromise rather than public-health science; industry (not an independent regulator) controls the mandated baseline/post-drill testing process, producing delayed and contested results; federal exemption of oil/gas wastewater from the Safe Drinking Water Act limits public data access; documented WVDEP non-enforcement of Underground Injection Control requirements. record_id R05E6A40917AB.",
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
