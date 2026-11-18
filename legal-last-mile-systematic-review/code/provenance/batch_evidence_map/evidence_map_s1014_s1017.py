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
        "study_id": "S1014",
        "study_design_class": "doctrinal/policy analysis (statutory law, regulations, case law, government data)",
        "evidence_level": "high",
        "mechanism_family": "enforcement",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "1996 Constitution Sec. 27; National Water Act 1998; Water Services Act 1997; Free Basic Water Policy 2001",
        "institutional_context": "municipalities/water services authorities, Johannesburg Water (Pty) Ltd, Department of Water Affairs and Forestry",
    },
    {
        "study_id": "S1015",
        "study_design_class": "comparative case study (two community self-help water projects)",
        "evidence_level": "high",
        "mechanism_family": "eligibility",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "collective/community self-help service model; formalized connection-fee eligibility structure",
        "institutional_context": "Mpundu Village Traditional Council; Bonadikombo Village Council/management committee",
    },
    {
        "study_id": "S1016",
        "study_design_class": "policy-evaluation study (national coverage statistics, documented sub-case)",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Water Services Act 1997; Free Basic Water Policy 2001; pre-payment/payment-for-operations tariff mechanisms",
        "institutional_context": "Department of Water Affairs and Forestry, local government water services authorities",
    },
    {
        "study_id": "S1017",
        "study_design_class": "ethnographic case study (interviews, participant observation, documentary analysis)",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "1992 National Water Law (Ley de Aguas Nacionales) differential subsidy structure",
        "institutional_context": "Comision Estatal de Servicios Publicos de Ensenada (CESPE), Comision Nacional del Agua (CNA)",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
