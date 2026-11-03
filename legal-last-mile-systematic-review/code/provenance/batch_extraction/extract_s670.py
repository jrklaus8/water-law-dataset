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


r = blank_row(fieldnames)
r.update({
    "study_id": "S670",
    "citation": "Dosu B, Hanrahan C, Johnston T, Spaling H (2022). Assessing the capacity gaps of decentralized rural water management: qualitative evidence from Ghana. Water International 47:1267-1286.",
    "doi": "10.1080/02508060.2022.2098454",
    "publication_year": "2022",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "Esereso, Wabrease, Wioso (Sunyani West and Sekyere Kumawu districts)",
    "legal_system": "common law (Ghana)",
    "urban_rural": "rural",
    "service_provider": "community-based Water and Sanitation Committees (WATSANs); Community Water and Sanitation Agency (CWSA); metropolitan/municipal/district assemblies",
    "regulatory_model": "National Community Water and Sanitation Programme (1994); CWSA standards/guidelines (design/coverage standards: 20 litres/person/day, max 500m travel, max 300 users/borehole, Ghana Standards Board water-quality parameters); district assemblies as legal owners of communal infrastructure; WATSAN committee formation/reformation rules (four-year reconstitution, no political/chieftaincy interference)",
    "population": "three rural communities in Ghana (Esereso pop. 457, Wabrease pop. 420, Wioso pop. 551) and water management agencies at national, district and community levels",
    "sample_size": "household and informant interviews plus focus group discussions across 3 rural communities and multi-level water management agencies (CWSA, district assembly officials)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "institutional_fragmentation": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "fees": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "household/informant interviews and FGDs across 3 rural communities (populations 420-551) plus national/district-level agency officials",
    "model_type": "qualitative thematic analysis with primary interview and focus-group data",
    "study_design": "qualitative case study (household interviews, key-informant interviews, focus group discussions)",
    "risk_of_bias_tool": "CASP",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: Ghana's real regulatory/institutional framework for decentralized rural water management (National Community Water and Sanitation Programme, CWSA design/coverage standards, district-assembly legal ownership of infrastructure, WATSAN committee formation rules) is documented against real primary household, informant, and focus-group data across three rural communities, identifying institutional, financial, human-resource, technical and social capacity gaps affecting rural water supply and management outcomes.",
    "source_document": "Dosu, Hanrahan, Johnston & Spaling 2022, Water International 47:1267-1286 (retrieved via Google Drive inbox)",
    "page": "1267-1286",
    "figure": "Figure 1 (institutional framework for rural water management in Ghana); Figure 2 (study communities)",
    "section": "Background to decentralized rural water management in Ghana; Selection of the study communities and participants; Results",
    "exact_location": "Sections on the CWSA regulatory framework and the community-level capacity-gap findings",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative institutional case study of decentralized rural water management capacity gaps in Ghana, with real primary household/informant/FGD data documenting the CWSA/district-assembly regulatory framework tied to real community-level water access outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative thematic-analysis design, no regression-based causal estimate. Extracted for record_id RFAAFF404B38C.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})

assert r["study_id"] not in existing_ids
rows.append(r)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

print(f"Added 1 row. New total: {len(rows)}")
