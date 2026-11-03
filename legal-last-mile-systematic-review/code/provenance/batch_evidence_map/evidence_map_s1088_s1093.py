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
        "study_id": "S1088",
        "study_design_class": "qualitative interview study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, enforcement (labour-law coverage by occupation sector)",
        "outcome_family": "sanitation_access, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Factories Act (1948); Building and Other Construction Workers Act (1996)",
        "institutional_context": "employers across four occupation sectors, Bangalore, India",
    },
    {
        "study_id": "S1089",
        "study_design_class": "mixed institutional analysis and household survey",
        "evidence_level": "moderate",
        "mechanism_family": "institutional_fragmentation, bureaucratic_assistance (decentralized governance, NGO-utility partnership)",
        "outcome_family": "water_access, sanitation_access, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Local Government Ordinance 2001 / Local Government Act (provincial)",
        "institutional_context": "WASA and NGO partnership (Badar Colony), Lahore and Peshawar, Pakistan",
    },
    {
        "study_id": "S1090",
        "study_design_class": "legal-historical case study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, fees (legal connection-eligibility barriers, discriminatory tariffs)",
        "outcome_family": "water_access, formal_connection, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Water Resources Law No. 7/2004; judicial review of tariff increases",
        "institutional_context": "PAM Jaya and private concessionaires, Jakarta, Indonesia",
    },
    {
        "study_id": "S1091",
        "study_design_class": "programme-evaluation case study",
        "evidence_level": "moderate",
        "mechanism_family": "institutional_fragmentation, fees (enabling-environment policy/financing dimensions)",
        "outcome_family": "sanitation_access, service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Total Sanitation and Sanitation Marketing (TSSM) enabling-environment framework",
        "institutional_context": "national/district governments, India, Indonesia, Tanzania",
    },
    {
        "study_id": "S1092",
        "study_design_class": "policy-analysis study",
        "evidence_level": "high",
        "mechanism_family": "fees, eligibility (connection charges, tariff/subsidy design)",
        "outcome_family": "water_access, formal_connection, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "municipal water tariff and connection-charge policy",
        "institutional_context": "urban local bodies (ULBs), India",
    },
    {
        "study_id": "S1093",
        "study_design_class": "critical political-ecology case study",
        "evidence_level": "high",
        "mechanism_family": "fees, enforcement (infrastructure/connection charges, regulatory capture)",
        "outcome_family": "water_access, sanitation_access, formal_connection, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "1993 water/sanitation privatization concession; ETOSS regulatory agency",
        "institutional_context": "Aguas Argentinas, Buenos Aires, Argentina",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
