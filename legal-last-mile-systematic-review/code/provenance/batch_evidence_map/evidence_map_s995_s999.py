#!/usr/bin/env python3
import csv
import tempfile
import os

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
        "study_id": "S995",
        "study_design_class": "ethnographic survey with qualitative narrative analysis",
        "evidence_level": "moderate",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "water supply privatization contract/policy",
        "institutional_context": "Belize Water Supply Limited (BWSL)",
    },
    {
        "study_id": "S996",
        "study_design_class": "cross-sectional household survey with qualitative analysis",
        "evidence_level": "moderate",
        "mechanism_family": "tenure",
        "outcome_family": "sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "de facto vs. de jure tenure security regimes",
        "institutional_context": "self-managed household on-site sanitation, urban Dakar low-income areas",
    },
    {
        "study_id": "S997",
        "study_design_class": "project case study/policy analysis",
        "evidence_level": "moderate",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "flexible vs. mandated O&M cost-recovery tariff-collection policy",
        "institutional_context": "Tamil Nadu rural water supply program, government engineers, community",
    },
    {
        "study_id": "S998",
        "study_design_class": "qualitative case study with interviews and participant observation",
        "evidence_level": "high",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "2004 National Water Initiative, Native Title Act 1993, Strategic Indigenous Reserve",
        "institutional_context": "Northern Territory water-allocation planning authority, Water Advisory Committee, Northern Land Council",
    },
    {
        "study_id": "S999",
        "study_design_class": "legal/policy case analysis with descriptive epidemiological data",
        "evidence_level": "high",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "notified/non-notified slum status, 2014 Bombay High Court PIL ruling, Article 21 constitutional right to water",
        "institutional_context": "Mumbai municipal government, Pani Haq Samiti (advocacy group), Bombay High Court",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
