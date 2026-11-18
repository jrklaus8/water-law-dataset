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
        "study_id": "S1110",
        "study_design_class": "mixed-methods case study (transect walks, focus groups, desktop review)",
        "evidence_level": "high",
        "mechanism_family": "institutional_fragmentation, political_coordination, service_area (state-fragility/governance-failure)",
        "outcome_family": "water_access, sanitation_access, service_coverage, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "collapsed central-state statistical/regulatory capacity since 1991",
        "institutional_context": "Jariban district, Somalia",
    },
    {
        "study_id": "S1111",
        "study_design_class": "qualitative institutional case study (semi-structured interviews)",
        "evidence_level": "moderate",
        "mechanism_family": "discretion_accommodation, discretion, delay, bureaucratic_assistance, political_coordination (institutional legitimation/discretion)",
        "outcome_family": "water_access, sanitation_access, service_quality",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "German/EU asylum administrative framework, 2015-2016 refugee crisis",
        "institutional_context": "German government agencies and aid organizations",
    },
    {
        "study_id": "S1112",
        "study_design_class": "doctrinal/normative/economic comparative case study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, fees, enforcement, hardship_exception, judicial_review (constitutional minimum-water guarantee, cost-recovery charge)",
        "outcome_family": "water_access, service_quantity, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "2008 Ecuadorian Constitution; SENAGUA Ministerial Agreements 2017-1522/1523",
        "institutional_context": "Cuenca, Gualaceo, Suscal municipalities, Ecuador",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
