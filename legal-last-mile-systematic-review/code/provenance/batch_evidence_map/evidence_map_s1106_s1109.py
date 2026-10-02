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
        "study_id": "S1106",
        "study_design_class": "political ecology case study (multiple case studies)",
        "evidence_level": "high",
        "mechanism_family": "institutional_fragmentation, political_coordination, service_area (colonial jurisdictional exclusion)",
        "outcome_family": "water_access, sanitation_access, service_coverage, service_quality",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Indian Act reservation system; federal fiduciary/constitutional responsibility for on-reserve water",
        "institutional_context": "First Nation communities, Canadian Prairie region",
    },
    {
        "study_id": "S1107",
        "study_design_class": "qualitative institutional case study (key informant interviews)",
        "evidence_level": "moderate",
        "mechanism_family": "discretion_accommodation, enforcement, political_coordination, bureaucratic_assistance (formal/informal institutional complementarity)",
        "outcome_family": "water_access, service_coverage, service_reliability, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "National Water Policy decentralization framework; Community Owned Water Supply Organizations (COWSOs)",
        "institutional_context": "Hai and Siha districts, Tanzania",
    },
    {
        "study_id": "S1108",
        "study_design_class": "institutional/legal case study (community-based planning)",
        "evidence_level": "high",
        "mechanism_family": "institutional_fragmentation, political_coordination, service_area, participation (federal/provincial jurisdictional fragmentation)",
        "outcome_family": "water_access, service_coverage, service_quality",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Indian Act 1876; Constitution Act 1982",
        "institutional_context": "Muskowekwan First Nation, Treaty 4, Saskatchewan, Canada",
    },
    {
        "study_id": "S1109",
        "study_design_class": "qualitative institutional case study (thematic analysis of interviews)",
        "evidence_level": "high",
        "mechanism_family": "institutional_fragmentation, political_coordination, fees, burden (overlapping agency mandates, PPP concession pricing)",
        "outcome_family": "water_access, service_coverage, service_quality, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "PPP concession arrangement (PSAWEN-NUWACO); Natural Water Resources Law 1984",
        "institutional_context": "Garowe, Puntland, Somalia",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
