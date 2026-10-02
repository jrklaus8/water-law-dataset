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
        "study_id": "S1097",
        "study_design_class": "institutional/regulatory comparative case study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, service_area, enforcement (regulatory-jurisdiction fragmentation)",
        "outcome_family": "water_access, sanitation_access, formal_connection, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "AASA concession agreement (ETOSS) vs. ORAB regulatory tolerance; provincial decree 878/2003",
        "institutional_context": "AASA and independent municipal providers, Buenos Aires metropolitan region, Argentina",
    },
    {
        "study_id": "S1098",
        "study_design_class": "policy-reform analysis",
        "evidence_level": "high",
        "mechanism_family": "eligibility, fees (connection-cost subsidy, legalizing vending, exclusive-rights prohibition)",
        "outcome_family": "water_access, formal_connection, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "municipal water tariff and connection-policy reform agenda",
        "institutional_context": "municipal water utilities, South Asian cities",
    },
    {
        "study_id": "S1099",
        "study_design_class": "quantitative household survey with key-informant interviews",
        "evidence_level": "high",
        "mechanism_family": "legal_status, fees (illegal-settlement status, informal-purchase markup)",
        "outcome_family": "water_access, sanitation_access, formal_connection, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "informal/illegal settlement status; nationally-set block tariff structure",
        "institutional_context": "Ghana Water Company Limited, Kumasi, Ghana",
    },
    {
        "study_id": "S1100",
        "study_design_class": "institutional case study",
        "evidence_level": "high",
        "mechanism_family": "fees (full-cost-recovery tariff clause applied to collective bulk connection)",
        "outcome_family": "water_access, affordability, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "National Water Initiative Agreement, full-cost-recovery Clause 66(v)",
        "institutional_context": "SA Water and District Council of Ceduna, Yarilena Aboriginal homeland, Australia",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
