#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EM = f"{BASE}/05_analysis/descriptive/evidence_map.csv"

with open(EM, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

def add(sid, **kwargs):
    assert sid not in existing_ids, f"{sid} already exists"
    row = {fn: "" for fn in fieldnames}
    row["study_id"] = sid
    row.update(kwargs)
    rows.append(row)

add("S928",
    study_design_class="comparative ethnographic fieldwork (two-district, cross-country)",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="decentralization and public-private-partnership legal frameworks, Rwanda and Uganda",
    institutional_context="district/sector local governments, private contractors, community structures",
    )

add("S929",
    study_design_class="qualitative investigative study with primary and secondary data",
    evidence_level="moderate",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Nigeria rural water-sector policy and institutional framework",
    institutional_context="community-based service providers; government water-supply agencies",
    )

add("S930",
    study_design_class="quasi-experimental propensity-score-matched difference-in-differences, municipal panel 1990-2010",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="sanitation_access",
    quantitative_synthesis_eligible="TRUE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="1995 Oaxaca constitutional reform granting legal standing to usos y costumbres traditional governance, Mexico",
    institutional_context="indigenous municipalities (usos y costumbres) vs. party-governed municipalities",
    )

add("S931",
    study_design_class="participatory action-research project case documentation with field observation",
    evidence_level="moderate",
    mechanism_family="bureaucratic_assistance",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Bangladesh national water policy framework",
    institutional_context="local government institutions; development agencies; community mobilization",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
