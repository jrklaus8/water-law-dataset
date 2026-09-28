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

# S672 - Gondo & Kolawole 2020, Okavango Delta Botswana customary/statutory water institutions
r = blank_row(fieldnames)
r.update({
    "study_id": "S672",
    "citation": "Gondo R, Kolawole OD (2020). Institutional factors engendering dissonance between customary and statutory institutions in water access in the Okavango Delta, Botswana. Sustainable Water Resources Management 6:99.",
    "doi": "10.1007/s40899-020-00458-9",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Botswana",
    "subnational_unit": "Shakawe, Tubu and Shorobe villages, Okavango Delta",
    "legal_system": "mixed (common law and customary law, Botswana)",
    "urban_rural": "rural",
    "service_provider": "Water Utilities Corporation (WUC); District Councils (DCs); Department of Water Affairs (DWA); customary/traditional water-governance institutions",
    "regulatory_model": "Water Utilities Corporation Act (1970); 2008 Botswana water-sector reform delineating DWA (planning) and WUC (reticulation) responsibilities; government policy shift from free/subsidized access to cost-recovery tariffs; customary institutions (taboos, norms, spirit mediums) operating in dissonance with statutory water legislation",
    "population": "households in three rural villages in the Okavango Delta, Botswana",
    "sample_size": "455 household heads, 44 community elders, and 17 government officials sampled via expert and homogeneous purposive sampling across 3 rural villages",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "documentation": "TRUE",
    "enforcement": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "455 household heads, 44 community elders, 17 government officials; key informant interviews, FGDs, household interview schedules",
    "model_type": "mixed-methods analysis (descriptive/inferential statistics plus content analysis)",
    "study_design": "cross-sectional mixed-methods case study (household interview schedules, key-informant interviews, FGDs, Kruskal-Wallis/Mann-Whitney U tests, qualitative content analysis)",
    "risk_of_bias_tool": "MMAT",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: Botswana's real statutory water-governance framework (WUC Act 1970, 2008 water-sector reform, cost-recovery tariff policy) is documented as being in dissonance with customary water institutions, against a large-N primary household/elder/official sample (455/44/17) across three rural villages combining quantitative inferential statistics and qualitative content analysis of water-access conflict.",
    "source_document": "Gondo & Kolawole 2020, Sustainable Water Resources Management 6:99 (retrieved via Google Drive inbox)",
    "page": "1-13",
    "table": "Table 5 (water bill for 45 kilolitres/month)",
    "section": "Methodology; Water access issues",
    "exact_location": "Sections documenting the WUC Act, 2008 reform, and customary/statutory institutional dissonance",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Mixed-methods institutional case study of customary/statutory water-institution dissonance in the Okavango Delta, with a large-N primary household/elder/official sample tied to real water-access and cost-recovery-tariff outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: reported inferential statistics are demographic/distance correlations (e.g. household size vs. distance), not a regression-based estimate isolating the institutional/legal mechanism. Extracted for record_id R0C5195EA94D6.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S673 - Tantoh, Simatele, Ebhuoma, Donkor & McKay 2021, Northwest Cameroon CBWSM
r = blank_row(fieldnames)
r.update({
    "study_id": "S673",
    "citation": "Tantoh HKB, Simatele DM, Ebhuoma E, Donkor K, McKay TJM (2021). Towards a pro-community-based water resource management system in Northwest Cameroon: practical evidence and lessons of best practices. GeoJournal 86:943-961.",
    "doi": "10.1007/s10708-019-10085-3",
    "publication_year": "2021",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Cameroon",
    "subnational_unit": "six rural villages, Northwest Cameroon",
    "legal_system": "mixed (civil law and customary/traditional authority, Cameroon)",
    "urban_rural": "rural",
    "service_provider": "community-based water management committees; village traditional authorities (Chiefs); public authorities and donors",
    "regulatory_model": "Cameroon decentralization policy; ministerial decree Articles 3(11) and 3(16) governing central-government retention of control over natural resources; traditional-authority/village-Chief customary governance structures",
    "population": "households in six rural communities in Northwest Cameroon",
    "sample_size": "156 household questionnaires (26 per village across 6 villages, systematic equal-probability sampling) plus key-informant interviews with water users and management-committee actors",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "institutional_fragmentation": "TRUE",
    "participation": "TRUE",
    "political_coordination": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "156 household questionnaires (26 per village, 6 villages) plus key-informant interviews",
    "model_type": "mixed-methods analysis with primary and secondary data",
    "study_design": "cross-sectional mixed-methods case study (systematic-sample household questionnaires, key-informant interviews, participatory research methods)",
    "risk_of_bias_tool": "MMAT",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate: Cameroon's decentralization policy and its practical limits (ministerial decree Articles 3(11)/3(16) retaining central-government control) alongside traditional-authority/village-Chief customary governance structures are documented against real primary household-level data (156-household systematic survey across 6 villages) on community-based water-project success/failure and sustainability outcomes, though the causal mechanism linking institutional arrangement to outcome is documented descriptively/qualitatively rather than through a formal regression.",
    "source_document": "Tantoh, Simatele, Ebhuoma, Donkor & McKay 2021, GeoJournal 86:943-961 (retrieved via Google Drive inbox)",
    "page": "943-961",
    "section": "Methodology; Community-based natural resource management in the Cameroonian context",
    "exact_location": "Sections on decentralization ministerial-decree constraints and community water-project outcomes",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Mixed-methods institutional case study of community-based water resource management sustainability in Northwest Cameroon, with real primary household-level survey data across six villages tied to decentralization-policy and traditional-authority institutional arrangements. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive/qualitative mixed-methods design, no regression-based causal estimate isolating the institutional/legal mechanism. Extracted for record_id RBFA4A3198454.",
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
