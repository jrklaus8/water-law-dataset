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
    "study_id": "S671",
    "citation": "Drew G, Deepika MG, Jyotishi A, Suripeddi S (2021). Water insecurity and patchwork adaptability in Bangalore's low-income neighbourhoods. Water International 46:900-918.",
    "doi": "10.1080/02508060.2021.1963031",
    "publication_year": "2021",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "south-eastern Bangalore (Sector Sixty, Water Tower Panchayat, Meadow Enclave)",
    "legal_system": "common law (India)",
    "urban_rural": "urban (peri-urban unplanned settlements)",
    "service_provider": "Bangalore Water Supply and Sewerage Board (BWSSB); private tanker suppliers; private borewell owners; panchayat (village council) lineman",
    "regulatory_model": "unplanned settlements located outside the municipal piped-water grid, water supply 'largely unregulated by a state entity'; BWSSB per-m2 property connection fee (US$1340-2680) as a formal-connection barrier",
    "population": "low-income residents of three unplanned-settlement neighbourhood enclaves in south-eastern Bangalore",
    "sample_size": "30-household questionnaires plus door-knocking/semi-structured interviews and focus groups across 3 of 5 sample neighbourhoods (Sector Sixty ~30 households, Water Tower Panchayat ~300 homes, Meadow Enclave), fieldwork January-August 2018",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "30-household questionnaires; semi-structured interviews and focus groups (e.g. 5-woman focus group, July 2018) across 3 neighbourhood enclaves",
    "model_type": "qualitative ethnographic analysis with primary interview/questionnaire data",
    "study_design": "qualitative case study (site visits, door-knocking questionnaires, semi-structured interviews, focus groups)",
    "risk_of_bias_tool": "CASP",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: the municipality's resource-governance failure and the real exclusion of unplanned peri-urban settlements from Bangalore's formal piped-water grid (BWSSB), including a documented per-m2 connection fee of US$1340-2680 as a formal-connection barrier, are documented against real primary household-level fieldwork (30-household questionnaires plus interviews/focus groups across three neighbourhoods) showing time-intensive, costly informal coping strategies (tanker water, borewells, bottled water) substituting for formal connection.",
    "source_document": "Drew, Deepika, Jyotishi & Suripeddi 2021, Water International 46:900-918 (retrieved via Google Drive inbox)",
    "page": "900-918",
    "figure": "Figure 1 (study area map); Figure 2-4 (site photographs)",
    "section": "Water insecurity in Bangalore's low-income neighbourhoods; Patchwork adaptability in Sector Sixty; Social divisions and resource inequities in Water Tower Panchayat; Tanker supplier dependence in Meadow Enclave",
    "exact_location": "Sections documenting exclusion from the municipal piped grid and household coping strategies",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative ethnographic case study of household water insecurity documenting municipal governance failure and unplanned-settlement exclusion from the formal piped-water grid, with real primary household-level fieldwork. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative ethnographic design, no regression-based causal estimate. Extracted for record_id R8C898DA2D09A.",
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
