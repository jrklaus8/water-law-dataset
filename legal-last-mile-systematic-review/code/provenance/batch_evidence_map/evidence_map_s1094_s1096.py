#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"


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

new_rows = [
    {
        "study_id": "S1094",
        "study_design_class": "anthropological fieldwork case study",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, fees, institutional_fragmentation (co-production governance modes)",
        "outcome_family": "water_access, sanitation_access, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "co-production/co-delivery of public goods via multiple modes of local governance",
        "institutional_context": "state water technicians, communes, development-partner projects, three urban sites, Niger",
    },
    {
        "study_id": "S1095",
        "study_design_class": "mixed-methods case study",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, tenure, fees (community-public partnership governance)",
        "outcome_family": "water_access, formal_connection, service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "community-based natural resource management (CBNRM); business-based Water User Association model",
        "institutional_context": "Water User Associations, peri-urban Malawi",
    },
    {
        "study_id": "S1096",
        "study_design_class": "institutional/policy analysis",
        "evidence_level": "high",
        "mechanism_family": "fees, institutional_fragmentation (subsidy allocation, connection-cost burden)",
        "outcome_family": "water_access, sanitation_access, formal_connection, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "federal subsidy allocation (CONAGUA operating rules); Article 115 municipal responsibility",
        "institutional_context": "municipal water utilities, Mexico",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
