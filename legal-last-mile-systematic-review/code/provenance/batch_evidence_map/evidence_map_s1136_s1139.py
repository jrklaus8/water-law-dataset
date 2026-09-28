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
        "study_id": "S1136",
        "study_design_class": "quantitative regression-based institutional-mechanism study",
        "evidence_level": "high",
        "mechanism_family": "discretion_accommodation, enforcement, discretion, institutional_fragmentation, political_coordination, bureaucratic_assistance (political capture of constitutionally mandated local-government sanitation function)",
        "outcome_family": "sanitation_access, service_coverage, service_quality",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "73rd Constitutional Amendment; Panchayati Raj Institutions Act sanitation mandate",
        "institutional_context": "4 South Indian states (Andhra Pradesh, Karnataka, Kerala, Tamil Nadu)",
    },
    {
        "study_id": "S1137",
        "study_design_class": "multi-jurisdiction qualitative institutional comparative case study",
        "evidence_level": "moderate",
        "mechanism_family": "burden, discretion_accommodation, enforcement, planning, service_area, fees, discretion, complaint, participation, institutional_fragmentation, political_coordination, bureaucratic_assistance, formal_connection (governance-reform/outsourcing/PPP institutional models)",
        "outcome_family": "water_access, sanitation_access, service_coverage, service_reliability, service_quality",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "74th Constitutional Amendment; JNNURM/RUIDP central urban-renewal schemes",
        "institutional_context": "12 paired cities, 6 Indian states",
    },
    {
        "study_id": "S1138",
        "study_design_class": "qualitative institutional/administrative-mechanism case study",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, burden, discretion_accommodation, documentation, planning, service_area, procedural_steps, delay, discretion, administrative_review, institutional_fragmentation, political_coordination, bureaucratic_assistance, formal_connection, application_success, refusal, delay_outcome (competitive earmarked-fund allocation mechanism)",
        "outcome_family": "water_access, service_coverage, service_reliability, service_quantity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "central-local administrative fiscal transfer system ('project mechanism')",
        "institutional_context": "2 counties, Yunnan province, China",
    },
    {
        "study_id": "S1139",
        "study_design_class": "mixed-methods institutional/legal sustainability assessment",
        "evidence_level": "moderate",
        "mechanism_family": "burden, enforcement, documentation, planning, service_area, fees, institutional_fragmentation, political_coordination, formal_connection (absence of enforceable sanitation law; institutional-framework gaps)",
        "outcome_family": "sanitation_access, service_coverage, service_reliability, service_quality, affordability, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "absence of national sanitation law (under formulation); National Sanitation Policy and Strategies",
        "institutional_context": "Kigali, Rwanda",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
