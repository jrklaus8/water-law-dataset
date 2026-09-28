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
        "study_id": "S1158",
        "study_design_class": "systematic scoping review",
        "evidence_level": "moderate",
        "mechanism_family": "burden, planning, service_area, institutional_fragmentation, political_coordination (institutional/political barriers in protracted displacement)",
        "outcome_family": "water_access, sanitation_access, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "humanitarian/institutional response frameworks in protracted displacement",
        "institutional_context": "varies by displacement setting, global scoping review",
    },
    {
        "study_id": "S1159",
        "study_design_class": "qualitative expert-elicitation study (Nominal Group Technique)",
        "evidence_level": "moderate",
        "mechanism_family": "discretion_accommodation, planning, service_area, fees, discretion, political_coordination, participation, affordability (ESG/fiscal-governance strategy for sanitation utility)",
        "outcome_family": "sanitation_access, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "ESG/fiscal-governance framework for a public sanitation utility under budgetary constraint",
        "institutional_context": "public sanitation utility, Maceio, Brazil",
    },
    {
        "study_id": "S1160",
        "study_design_class": "quantitative survey-based logistic regression plus qualitative FGDs (participation outcome, not access outcome)",
        "evidence_level": "moderate",
        "mechanism_family": "burden, complaint, participation, bureaucratic_assistance (community-participation program in NGO-sponsored water schemes)",
        "outcome_family": "water_access, sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "NGO-sponsored community water-scheme governance",
        "institutional_context": "Sustainable Aid in Africa International water schemes, Kisumu, Kenya",
    },
    {
        "study_id": "S1161",
        "study_design_class": "qualitative institutional/regulatory-mechanism case study",
        "evidence_level": "moderate",
        "mechanism_family": "enforcement, planning, service_area, participation, institutional_fragmentation, political_coordination (disaster-governance institutional failure)",
        "outcome_family": "sanitation_access, service_coverage, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Brazilian environmental/sanitation regulatory framework, disaster response",
        "institutional_context": "CASAN, Civil Defense, environmental regulators, Florianopolis, Brazil",
    },
    {
        "study_id": "S1162",
        "study_design_class": "quantitative multilevel (hierarchical) linear regression",
        "evidence_level": "high",
        "mechanism_family": "planning, service_area, institutional_fragmentation, political_coordination, bureaucratic_assistance, formal_connection (local-government administrative category)",
        "outcome_family": "water_access, service_coverage",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "Indian municipal-governance category system (municipal corporation / municipality / town panchayat)",
        "institutional_context": "3,547 urban local governments, 21 states, India",
    },
    {
        "study_id": "S1163",
        "study_design_class": "quantitative multilevel mixed-effects logistic regression",
        "evidence_level": "high",
        "mechanism_family": "service_area, participation, bureaucratic_assistance, formal_connection (external WaSH-program funding/support; PTA governance)",
        "outcome_family": "water_access, sanitation_access, service_reliability, service_continuity",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "external WaSH-program funding/support; parent-teacher-association governance",
        "institutional_context": "rural schools, 14 low- and middle-income countries",
    },
    {
        "study_id": "S1164",
        "study_design_class": "qualitative comparative case-study collection (edited volume)",
        "evidence_level": "moderate",
        "mechanism_family": "planning, zoning, service_area, institutional_fragmentation, political_coordination (peri-urban water/sanitation governance arrangements)",
        "outcome_family": "water_access, sanitation_access, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "peri-urban water/sanitation governance arrangements, multi-country comparative",
        "institutional_context": "varies by case study; Africa, Asia, South America, Netherlands",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
