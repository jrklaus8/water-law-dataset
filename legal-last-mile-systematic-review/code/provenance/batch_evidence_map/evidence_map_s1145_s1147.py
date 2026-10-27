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
        "study_id": "S1145",
        "study_design_class": "qualitative comparative institutional/governance-reform case study",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, burden, discretion_accommodation, planning, service_area, fees, procedural_steps, discretion, complaint, participation, institutional_fragmentation, political_coordination, formal_connection (PPP-driven water-supply reform governance)",
        "outcome_family": "water_access, service_coverage, service_reliability, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "public-private-partnership-driven urban water-supply reform",
        "institutional_context": "Bangalore Water Supply and Sewerage Board, Chennai Metrowater, Kerala Water Authority, India",
    },
    {
        "study_id": "S1146",
        "study_design_class": "quantitative regression-based institutional/administrative-barrier study",
        "evidence_level": "high",
        "mechanism_family": "burden, enforcement, service_area, fees, discretion, formal_connection (utilities-sector corruption mechanism)",
        "outcome_family": "water_access, service_coverage, service_reliability, service_quantity, service_quality",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "utilities-sector corruption as an administrative barrier to water service access",
        "institutional_context": "national/regional water utilities, multi-country Africa (Afrobarometer round 7)",
    },
    {
        "study_id": "S1147",
        "study_design_class": "qualitative institutional/legal-history case study",
        "evidence_level": "moderate",
        "mechanism_family": "burden, enforcement, property, planning, service_area, fees, institutional_fragmentation, political_coordination, formal_connection (privatization/remunicipalisation regulatory-model shift)",
        "outcome_family": "water_access, sanitation_access, service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "public/private water-utility regulatory-model history (concession, INSFOPAL, decentralization)",
        "institutional_context": "multiple Colombian cities (Barranquilla, Bogota, Medellin, Cartagena, Pereira, Cali, EPM)",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
