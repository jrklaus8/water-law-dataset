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
        "study_id": "S981",
        "study_design_class": "policy/institutional review with national statistics",
        "evidence_level": "moderate",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Law 382 (General Law of Sanitation Services, 1988), Law 70 (General Law of Tariffs, 1988), Law 18,778 (subsidy law, 1989)",
        "institutional_context": "Superintendencia de Servicios Sanitarios (SISS), fully private and concessionary water companies",
    },
    {
        "study_id": "S982",
        "study_design_class": "cross-sectional mixed-methods household survey",
        "evidence_level": "moderate",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Tanzania Water Resources Management Act 2009, National Water Policy 2002, municipal building-permit bylaws",
        "institutional_context": "Ministry of Water, district/municipal authorities, DAWASCO",
    },
    {
        "study_id": "S983",
        "study_design_class": "field survey with institutional/policy analysis",
        "evidence_level": "high",
        "mechanism_family": "institutional_fragmentation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "World Bank/JBIC loan-conditioned institutional reform, demand-responsive-approach community ownership",
        "institutional_context": "Kerala Water Authority (KWA), Kerala Rural Water Supply and Sanitation Agency (KRWSA)",
    },
    {
        "study_id": "S984",
        "study_design_class": "qualitative case study with semi-structured interviews",
        "evidence_level": "high",
        "mechanism_family": "tenure",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Egypt's 1984 Irrigation and Drainage Law, Islamic waqf charitable-endowment institution, property rights regimes",
        "institutional_context": "charitable water wells (sobol), local NGO (Charitable Association), village youth group",
    },
    {
        "study_id": "S985",
        "study_design_class": "exploratory/descriptive case study with semi-structured interviews",
        "evidence_level": "moderate",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Namibia Water Resources Management Act 2004 (proposed Water Regulatory Board, not implemented)",
        "institutional_context": "NamWater (bulk supplier), City of Windhoek, Ministry of Agriculture Water and Forestry",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
