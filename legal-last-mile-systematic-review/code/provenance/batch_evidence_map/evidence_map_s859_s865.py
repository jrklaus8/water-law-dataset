#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EMAP = f"{BASE}/05_analysis/descriptive/evidence_map.csv"

with open(EMAP, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

def add(sid, study_design_class, evidence_level, mechanism_family, outcome_family,
        quant_eligible, qual_eligible, legal_context, institutional_context):
    assert sid not in existing_ids, f"{sid} already in evidence_map"
    rows.append({
        "study_id": sid,
        "study_design_class": study_design_class,
        "evidence_level": evidence_level,
        "mechanism_family": mechanism_family,
        "outcome_family": outcome_family,
        "quantitative_synthesis_eligible": quant_eligible,
        "qualitative_synthesis_eligible": qual_eligible,
        "legal_context": legal_context,
        "institutional_context": institutional_context,
    })

add("S859", "mixed-methods comparative study", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "water-sector decentralization reform, Tanzania",
    "village water-management committees, district governance")

add("S860", "citywide poverty-mapping survey", "high", "documentation",
    "water_access", "FALSE", "TRUE",
    "slum notification status and service eligibility, India",
    "municipal corporations, ADB/UN-HABITAT Water for Asian Cities Programme")

add("S861", "mixed-methods ethnographic/survey case study", "high", "bureaucratic_assistance",
    "water_access", "FALSE", "TRUE",
    "local political leadership navigating law and bureaucracy, India",
    "Delhi Jal Board, municipal bureaucracy")

add("S862", "documentary institutional analysis", "high", "enforcement",
    "water_access", "FALSE", "TRUE",
    "regulatory state capture, Department of Water and Sanitation, South Africa",
    "DWS, municipal Water Services Authorities")

add("S863", "historical institutional case study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "divided treaty-port municipal governance, China",
    "British/Japanese Settlement Municipal Councils, Old City administration")

add("S864", "ethnographic case study with original interview data", "high", "fees",
    "water_access", "FALSE", "TRUE",
    "bulk-water contract mechanism, Philippines",
    "MWCI, community Peoples' Organizations")

add("S865", "legal/policy review with government survey statistics", "moderate-high", "documentation",
    "water_access", "FALSE", "TRUE",
    "Water Services Act 1997, National Water Act 1998, Free Basic Services Policy, South Africa",
    "Commission for Gender Equality, DWA/DWAF")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
