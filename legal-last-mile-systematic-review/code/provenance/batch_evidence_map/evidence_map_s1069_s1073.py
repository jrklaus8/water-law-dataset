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
        "study_id": "S1069",
        "study_design_class": "political-historical case study",
        "evidence_level": "high",
        "mechanism_family": "Free Basic Water policy, tariff design, and disconnection enforcement",
        "outcome_family": "affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Free Basic Water policy; prepaid metering; convex-block tariff structure",
        "institutional_context": "Johannesburg Water, South Africa",
    },
    {
        "study_id": "S1070",
        "study_design_class": "qualitative case study",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "pro-poor equity strategy in rural water-program design",
        "institutional_context": "rural water and sanitation programme, semi-arid Mozambique",
    },
    {
        "study_id": "S1071",
        "study_design_class": "theoretical/game-theoretic model with empirical evidence",
        "evidence_level": "moderate",
        "mechanism_family": "water-sector legal reform and regulatory-body establishment (tariff-setting, resource-management, consumer protection)",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Chilean Water Code tradable water-rights market",
        "institutional_context": "national water-rights market, Chile",
    },
    {
        "study_id": "S1072",
        "study_design_class": "quantitative cross-national panel regression study",
        "evidence_level": "moderate",
        "mechanism_family": "IMF structural adjustment conditionality",
        "outcome_family": "service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "IMF structural adjustment programs",
        "institutional_context": "30 Sub-Saharan African national governments",
    },
    {
        "study_id": "S1073",
        "study_design_class": "political-ecological mixed-methods case study",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "full-cost-recovery tariff reform",
        "institutional_context": "Jaipur public water-supply utility, Rajasthan, India",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
