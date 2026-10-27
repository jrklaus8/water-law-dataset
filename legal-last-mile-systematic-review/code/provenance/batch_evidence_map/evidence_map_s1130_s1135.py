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
        "study_id": "S1130",
        "study_design_class": "governmentality/institutional-sociology policy-process case study",
        "evidence_level": "moderate",
        "mechanism_family": "fees, discretion, participation, institutional_fragmentation, political_coordination (accounting/tariff mechanisms in privatization debate)",
        "outcome_family": "water_access, service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "proposed public-private-partnership/lease privatization; full-cost-recovery tariff mechanism",
        "institutional_context": "Ghana Water Company, Ghana",
    },
    {
        "study_id": "S1131",
        "study_design_class": "qualitative policy-document analysis and embedded institutional case study",
        "evidence_level": "moderate",
        "mechanism_family": "legal_status, property, participation, political_coordination (community self-governance vs. state/private commodification)",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "National Water Policy 1987/2002; community-owned water-parliament governance",
        "institutional_context": "Tarun Bharat Sangh (TBS), Rajasthan, India",
    },
    {
        "study_id": "S1132",
        "study_design_class": "matched comparative case study with household survey",
        "evidence_level": "high",
        "mechanism_family": "eligibility, discretion_accommodation, planning, service_area, fees, procedural_steps, hardship_exception, complaint, participation, bureaucratic_assistance (participatory-governance institutional mechanism)",
        "outcome_family": "water_access, sanitation_access, service_reliability, service_quality, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Ward Water Committees (WWCs), community-participation institutional design",
        "institutional_context": "Kerala Water Authority, Kerala, India",
    },
    {
        "study_id": "S1133",
        "study_design_class": "ethnographic institutional/legal case study",
        "evidence_level": "high",
        "mechanism_family": "tenure_status, legal_status, eligibility, burden, discretion_accommodation, enforcement, documentation, tenure, service_area, fees, procedural_steps, delay, discretion, disconnection, reconnection, sanction, political_coordination (notified/non-notified slum legal status; residency-cutoff eligibility)",
        "outcome_family": "water_access, sanitation_access, service_coverage, service_reliability, affordability, service_continuity, refusal, delay_outcome",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Maharashtra Slum Areas (Improvement, Clearance and Redevelopment) Act 1971; pre-1995 residency cutoff",
        "institutional_context": "Rafinagar and Khotwadi informal settlements, Mumbai, India",
    },
    {
        "study_id": "S1134",
        "study_design_class": "comparative institutional case study with household survey",
        "evidence_level": "high",
        "mechanism_family": "tenure_status, legal_status, eligibility, burden, discretion_accommodation, documentation, tenure, service_area, fees, procedural_steps, delay, participation, institutional_fragmentation, political_coordination, bureaucratic_assistance (notified-slum eligibility; cost-recovery/user-committee model)",
        "outcome_family": "water_access, sanitation_access, service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Community Managed Sewerage Scheme; notified-slum eligibility requirement",
        "institutional_context": "Gwalior and Indore, Madhya Pradesh, India",
    },
    {
        "study_id": "S1135",
        "study_design_class": "ethnographic panel-survey institutional case study",
        "evidence_level": "high",
        "mechanism_family": "tenure_status, legal_status, eligibility, burden, discretion_accommodation, enforcement, documentation, tenure, property, fees, procedural_steps, discretion, hardship_exception, sanction, participation, refusal (community-membership eligibility institution)",
        "outcome_family": "water_access, service_reliability, service_quantity, affordability, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "informal community-membership eligibility rules (landowner/proxy-member vs. renter status)",
        "institutional_context": "Villa Israel squatter settlement, Cochabamba, Bolivia",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
