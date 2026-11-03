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

add("S912",
    study_design_class="ethnographic case study",
    evidence_level="moderate-high",
    mechanism_family="discretion",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="formal utility non-recognition of informal settlements, Dhaka",
    institutional_context="DWASA, DESCO, local association negotiators",
    )

add("S913",
    study_design_class="comparative case study (2 municipalities, successful vs. non-successful sewerage investment)",
    evidence_level="moderate-high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="multi-stakeholder governance arrangements, Chennai, India",
    institutional_context="Resident Welfare Associations, municipal government",
    )

add("S914",
    study_design_class="documentary/legal analysis with illustrative case examples",
    evidence_level="moderate-high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="constitutional right to water; Water Services Act 108 of 1997, South Africa",
    institutional_context="local government municipalities",
    )

add("S915",
    study_design_class="qualitative case study (single PPP pilot project)",
    evidence_level="moderate-high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="water-supply public-private-partnership pilot, Bengaluru",
    institutional_context="PPP marketization intervention, informal-settlement counter-experimentation",
    )

add("S916",
    study_design_class="GIS-based household survey with spatial water-poverty index analysis",
    evidence_level="high",
    mechanism_family="fees",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="1995 Senegalese water-sector reform",
    institutional_context="Senegalese Waters (SDE)",
    )

add("S917",
    study_design_class="household survey with market-impact (preliminary evidence) analysis",
    evidence_level="moderate-high",
    mechanism_family="eligibility",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="April 1990 water-resale deregulation measure, Jakarta",
    institutional_context="Perusahaan Air Minum Jaya",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
