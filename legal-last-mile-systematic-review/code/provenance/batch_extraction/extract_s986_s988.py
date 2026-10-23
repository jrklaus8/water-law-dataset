#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

def blank_row(fieldnames):
    return {k: "" for k in fieldnames}

def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
new_rows = []

# S986 - R3D9E303C9EB3 - Lovei & Whittington 1993 - Jakarta rent-extraction
r = blank_row(fieldnames)
r.update({
    "study_id": "S986",
    "citation": "Lovei L, Whittington D (1993). Rent-extracting behavior by multiple agents in the provision of municipal water supply: A study of Jakarta, Indonesia. Water Resources Research.",
    "doi": "10.1029/92WR02998",
    "publication_year": "1993",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Indonesia",
    "subnational_unit": "Jakarta",
    "legal_system": "civil law",
    "urban_rural": "urban",
    "service_provider": "municipal water utility (city-owned), public tap operators, distributing vendors, tanker trucks",
    "regulatory_model": "municipal government tariff-setting (City Council of Jakarta), sales-permit licensing for retail water outlets, informal rent-extracting behavior by government officials/utility staff/neighborhood leaders",
    "population": "Jakarta households, particularly the 54% relying on private wells and 32% buying from vendors, versus the 14% with direct municipal connections",
    "sample_size": "city-wide institutional/economic analysis with numerical modeling calibrated to Jakarta data",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "discretion": "TRUE",
    "documentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "descriptive/modeled monopoly-rent allocation percentages",
    "study_design": "economic/institutional framework analysis with numerical modeling",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original institutional-economic analysis directly linking informal rent-extracting "
        "behavior by government officials, water utility staff, and licensed public-tap operators/vendors to "
        "restricted house-connection supply, limited public-tap numbers, and dramatically higher effective prices "
        "(up to 50x the municipal tariff) for unconnected households relying on vendors."),
    "source_document": "Lovei & Whittington 1993, Water Resources Research (retrieved via Google Drive)",
    "section": "Examination of Possible Rent-Extracting Behavior; Numerical Examples",
    "exact_location": "Table 2 (actors/objectives/strategies), Figures 2-4 (rent allocation)",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: original institutional-economic framework and numerical "
        "modeling demonstrating how informal rent-seeking behavior by government officials, water utility staff, and "
        "licensed public-tap operators (via restricted connections, capped public-tap numbers, and off-budget "
        "payments) generates monopoly rents and directly determines the terms of household water access in Jakarta "
        "-- households relying on vendors paying up to 50x the price of municipally connected households. Strong "
        "Family C match (institutional/administrative barriers/access inequality). NOT effect_sizes eligible: "
        "theoretical/numerical modeling framework calibrated to approximate Jakarta conditions, not a regression-"
        "based estimate from primary household data. Extracted for record_id R3D9E303C9EB3."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S987 - R3AE23244EFDE - Ducrot 2017 - Mozambique water committees
r = blank_row(fieldnames)
r.update({
    "study_id": "S987",
    "citation": "Ducrot R (2017). When good practices by water committees are not relevant: Sustainability of small water infrastructures in semi-arid Mozambique. Physics and Chemistry of the Earth.",
    "doi": "10.1016/j.pce.2016.08.004",
    "publication_year": "2017",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Mozambique",
    "subnational_unit": "semi-arid district, Limpopo Basin",
    "legal_system": "civil law",
    "urban_rural": "rural",
    "service_provider": "community-based water committees under the National Rural Water Supply and Sanitation Program",
    "regulatory_model": "community-based management (CBM) combined with demand-responsive-approach (DRA) institutional design; water-committee governance and leadership structure",
    "population": "rural villages served by community-managed boreholes in a semi-arid district",
    "sample_size": "village-level case study fieldwork across multiple communities",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "eligibility": "TRUE",
    "discretion_accommodation": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_continuity": "TRUE",
    "study_design": "qualitative/mixed-methods case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original field research directly linking water-committee leadership quality and "
        "village governance -- rather than normative committee functioning alone -- to borehole sustainability and "
        "continued water access, with explicit attention to how unequitable access to intervention benefits "
        "undermines community collective-action capacity."),
    "source_document": "Ducrot 2017, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    "section": "Results on committee leadership, village governance and infrastructure sustainability",
    "exact_location": "Throughout results sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: field study of the Mozambique National Rural Water "
        "Supply and Sanitation Program's community-based management institutional design, finding that coordinated "
        "committee leadership and village governance quality -- not normative committee functioning -- determine "
        "borehole sustainability, and that unequitable access to intervention benefits weakens community collective "
        "action. Strong Family A/B match. NOT effect_sizes eligible: qualitative case-study fieldwork, no regression-"
        "based estimate. Extracted for record_id R3AE23244EFDE."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S988 - R39C8535D837B - Rout 2014 - India Odisha DRA institutional variations
r = blank_row(fieldnames)
r.update({
    "study_id": "S988",
    "citation": "Rout S (2014). Institutional variations in practice of demand responsive approach: evidence from rural water supply in India. Water Policy.",
    "doi": "10.2166/wp.2014.155",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Odisha state (12 villages)",
    "legal_system": "common law",
    "urban_rural": "rural",
    "service_provider": "Gram Panchayat (local government) in seven villages; community-based Village Water and Sanitation Committee in five villages",
    "regulatory_model": "Demand Responsive Approach (DRA) reform under India's Sector Reforms Pilot Project (1999), state/district/village-level decentralized institutional structure",
    "population": "rural households in 12 villages, Odisha",
    "sample_size": "12 village communities (5 community-managed, 7 Gram-Panchayat-managed)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "extraction_sample_size": "12",
    "study_design": "comparative qualitative case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original comparative field study directly linking two distinct institutional "
        "arrangements (local-government Gram Panchayat vs. community-based Village Water and Sanitation Committee) "
        "implementing the Demand Responsive Approach reform to differential household water-supply outcomes, "
        "explicitly finding that DRA reinforced and extended existing social inequality in access to rural drinking "
        "water rather than addressing it."),
    "source_document": "Rout 2014, Water Policy (retrieved via Google Drive)",
    "section": "Findings on institutional variation and water access equity",
    "exact_location": "Throughout results/discussion sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: comparative field study (12 villages, Odisha) of two "
        "institutional arrangements (Gram Panchayat local government vs. community-based Village Water and "
        "Sanitation Committee) implementing India's Demand Responsive Approach water-sector reform, finding that DRA "
        "reinforced and extended existing social inequality in rural drinking-water access rather than addressing "
        "it. Strong Family A/C match. NOT effect_sizes eligible: qualitative comparative case study, no regression-"
        "based estimate. Extracted for record_id R39C8535D837B."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
