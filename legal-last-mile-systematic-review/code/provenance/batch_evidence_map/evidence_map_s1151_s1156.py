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
        "study_id": "S1151",
        "study_design_class": "qualitative institutional/administrative case study with survey-based access comparisons",
        "evidence_level": "moderate",
        "mechanism_family": "burden, tenure, property, planning, zoning, service_area, fees, political_coordination, formal_connection (historical racial housing-type allocation and municipal service-delivery strategy)",
        "outcome_family": "water_access, sanitation_access, service_coverage, service_reliability, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "post-apartheid municipal governance and historical racial housing-type allocation",
        "institutional_context": "Greater Johannesburg Metropolitan Council, Johannesburg, South Africa",
    },
    {
        "study_id": "S1152",
        "study_design_class": "qualitative gender-focused policy-analysis case study",
        "evidence_level": "moderate",
        "mechanism_family": "burden, planning, fees, participation, affordability (water-policy decentralization/privatization/user-pays reform)",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "water-sector decentralization/privatization/user-pays policy reform since the mid-1990s",
        "institutional_context": "national water-supply system, Malawi",
    },
    {
        "study_id": "S1153",
        "study_design_class": "quantitative survey-based logistic regression (participation outcome, not access outcome)",
        "evidence_level": "moderate",
        "mechanism_family": "burden, planning, participation (mandatory community-participation program design)",
        "outcome_family": "water_access, sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "community-managed water-supply program design (mandatory participation/labor contribution)",
        "institutional_context": "community-managed water-supply projects, three cities in central India",
    },
    {
        "study_id": "S1154",
        "study_design_class": "qualitative mixed-methods governance case study",
        "evidence_level": "moderate",
        "mechanism_family": "planning, service_area, discretion, institutional_fragmentation, political_coordination (constitutional devolution of local-government service functions)",
        "outcome_family": "water_access, service_coverage, service_reliability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "2013 Constitution of Zimbabwe, devolution provisions",
        "institutional_context": "urban local councils, four urban areas, Zimbabwe",
    },
    {
        "study_id": "S1155",
        "study_design_class": "qualitative historical-institutional case study",
        "evidence_level": "low-moderate",
        "mechanism_family": "planning, service_area, institutional_fragmentation, political_coordination (absence of coherent water policy/water law)",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "historically absent/underdeveloped national water policy and water law",
        "institutional_context": "national water-management institutions, Cameroon",
    },
    {
        "study_id": "S1156",
        "study_design_class": "qualitative political-economy case study with documented national incidence figures",
        "evidence_level": "moderate",
        "mechanism_family": "burden, enforcement, fees, disconnection, reconnection, political_coordination, affordability, service_continuity (World Bank-driven global water-privatization policy diffusion)",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "World Bank/transnational-policy-network-driven global 'Water for All' privatization/cost-recovery paradigm",
        "institutional_context": "private water concessionaires under World Bank-promoted privatization, South Africa",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
