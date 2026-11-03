import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}


def blank_row(fieldnames):
    return {f: "" for f in fieldnames}


new_rows = []

# S668 - Dakyaga, Ahmed & Sillim 2021, Dar es Salaam informal-settlement water governance
r = blank_row(fieldnames)
r.update({
    "study_id": "S668",
    "citation": "Dakyaga F, Ahmed A, Sillim ML (2021). Governing Ourselves for Sustainability: Everyday Ingenuities in the Governance of Water Infrastructure in the Informal Settlements of Dar es Salaam. Urban Forum 32:111-129.",
    "doi": "10.1007/s12132-020-09412-6",
    "publication_year": "2021",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Tanzania",
    "subnational_unit": "Goba-Chaurembo, Goba-Kibululu, Goba-Kunguru (Ubungo municipality, Dar es Salaam)",
    "legal_system": "common law (Tanzania)",
    "urban_rural": "urban (informal settlements)",
    "service_provider": "non-state water service providers (mechanised boreholes, water kiosks, wells, standpipes, tanker trucks, pushcarts); Dar es Salaam Water and Sewerage Authority (DAWASA)",
    "regulatory_model": "informal/unwritten rules and mechanisms governing non-state water provision, operating alongside and through relations with DAWASA (the statutory water utility); planning regulations distinguishing formally recognised from unplanned settlements",
    "population": "residents of three informal settlements in Dar es Salaam (16,491 people, 3,965 households)",
    "sample_size": "35 non-state water service providers interviewed (structured/open-ended, plus reconnaissance observation to saturation); key-informant interviews with the municipal water engineer, 2 Mtaa ward leaders, and the ward health officer",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "institutional_fragmentation": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "35 non-state water service provider interviews; 4 key-informant interviews; settlement-level population/household/income data (Table 2)",
    "model_type": "qualitative thematic analysis with primary interview data",
    "study_design": "qualitative case study (interviews, reconnaissance observation, MAXQDA thematic coding)",
    "risk_of_bias_tool": "CASP",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: informal/unwritten institutional rules and clientelist relationships governing non-state water provision in Dar es Salaam's informal settlements, structured by and interacting with the statutory water utility DAWASA's limited service capacity, are documented against real primary interview data from 35 water service providers and settlement-level household/income data, showing monthly-billing-based networked water access excluding low-income residents who cannot afford connection costs.",
    "source_document": "Dakyaga, Ahmed & Sillim 2021, Urban Forum 32:111-129 (retrieved via Google Drive inbox)",
    "page": "111-129",
    "table": "Table 1 (governance for sustainability framework); Table 2 (settlement/household/provider sample data)",
    "section": "Results and Discussion; The Actors Involved and Their Roles in the Urban Water Provision",
    "exact_location": "Sections on non-state water provider governance rules and DAWASA interaction",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative institutional case study of informal/non-state water governance in Dar es Salaam informal settlements, with real primary provider-interview and settlement-level data, following the established Hackenbroch & Hossain (S652) informal-institutional-water-governance precedent. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative thematic-analysis design, no regression-based causal estimate. Extracted for record_id R512A2C899B40.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S669 - Brown-Luthango & Arendse 2023, Cape Town co-production
r = blank_row(fieldnames)
r.update({
    "study_id": "S669",
    "citation": "Brown-Luthango M, Arendse W (2023). Co-production to reframe state practices in informal settlements: Lessons from Malawi Kamp and Klipheuwel in Cape Town, South Africa. Development Southern Africa 40:541-559.",
    "doi": "10.1080/0376835X.2021.2024069",
    "publication_year": "2023",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Malawi Camp and Klipheuwel informal settlements, City of Cape Town",
    "legal_system": "common law (South Africa)",
    "urban_rural": "urban (informal settlements)",
    "service_provider": "City of Cape Town (CoCT) Water & Sanitation Department, Environmental Health, Solid Waste, and Social Development & Early Childhood Development Departments",
    "regulatory_model": "CoCT Inter-Departmental Task Team (established 2013); Memorandum of Understanding (MoU) formalising co-production commitments; official Water & Sanitation Department regulations governing communal-toilet siting (denial of relocation to individual yards) and community-managed 'Water Saving Ambassadors' arrangement",
    "population": "residents of Malawi Camp (1,000+ people, average 13-year residency) and Klipheuwel informal settlements",
    "sample_size": "two comparative case studies (qualitative institutional/documentary analysis of co-production process, 2013-2019 period)",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "discretion_accommodation": "TRUE",
    "participation": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_quality": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "two informal-settlement case studies; qualitative documentary/interview analysis of the co-production process and monthly joint meetings",
    "model_type": "qualitative comparative case study with institutional/documentary analysis",
    "study_design": "qualitative case study (comparative, institutional/documentary analysis of co-production process)",
    "risk_of_bias_tool": "CASP",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": "Moderate: a real municipal Water & Sanitation Department regulation barring the relocation of communal toilets/taps to individual yards is documented against a real negotiated institutional workaround (community-managed 'Water Saving Ambassadors', proactive toilet-repair scheduling) and settlement-level water/sanitation infrastructure outcomes in two named Cape Town informal settlements, though the study is a qualitative comparative case study without individual household-level outcome data.",
    "source_document": "Brown-Luthango & Arendse 2023, Development Southern Africa 40:541-559 (retrieved via Google Drive inbox)",
    "page": "541-559",
    "section": "Findings; Discussion",
    "exact_location": "Sections on Water & Sanitation Department regulations and the Water Saving Ambassadors arrangement",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative comparative case study of municipal water/sanitation regulatory constraints and negotiated institutional co-production outcomes in South African informal settlements. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative comparative case-study design, no regression-based causal estimate. Extracted for record_id R84E44162269B.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
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

print(f"Added {len(new_rows)} rows. New total: {len(rows)}")
