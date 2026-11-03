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

existing = {r["study_id"] for r in rows}

new_rows = [
    {
        "study_id": "S1027",
        "study_design_class": "policy analysis (government/Auditor General documentary data, focus groups)",
        "evidence_level": "high",
        "mechanism_family": "institutional_fragmentation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "federal jurisdiction over reserve lands (Constitution Act s.35); fragmented departmental responsibility",
        "institutional_context": "AANDC, Health Canada, Environment Canada, band councils",
    },
    {
        "study_id": "S1028",
        "study_design_class": "case study (formal Public Inquiry analysis)",
        "evidence_level": "high",
        "mechanism_family": "enforcement",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "neo-liberal deregulation of water-safety oversight",
        "institutional_context": "Walkerton Public Utilities Commission, Ontario Ministry of the Environment",
    },
    {
        "study_id": "S1029",
        "study_design_class": "household-level empirical survey study",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "IMF-linked public-sector reform driving water-supply privatisation",
        "institutional_context": "privatized water-supply concessionaire, Pathumthani province",
    },
    {
        "study_id": "S1030",
        "study_design_class": "ethnographic case study (observation, interviews, focus groups)",
        "evidence_level": "high",
        "mechanism_family": "enforcement",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Prevention of Damages to Public Property Act; differentiated institutional water-allocation quota",
        "institutional_context": "Brihanmumbai Municipal Corporation (BMC)",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
