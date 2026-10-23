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

add("S943",
    study_design_class="multi-province qualitative interview study with case-study triangulation",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="South Africa post-1994 water-services legal framework",
    institutional_context="local municipal O&M institutional capacity",
    )

add("S944",
    study_design_class="single-town GIS-based case study with Census data and geo-coded public records",
    evidence_level="high",
    mechanism_family="zoning",
    outcome_family="sanitation_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="North Carolina Extraterritorial Jurisdiction (ETJ) law; annexation authority; Water Quality Critical Area zoning overlay",
    institutional_context="Town of Mebane municipal government",
    )

add("S945",
    study_design_class="12-scheme comparative institutional performance assessment with 850-household survey",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Maharashtra rural water-supply decentralization reforms, India",
    institutional_context="individual vs. regional piped water supply schemes",
    )

add("S946",
    study_design_class="18-city comparative institutional assessment framework across 6 countries",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="intergovernmental institutional structures, South and Southeast Asia",
    institutional_context="urban local governments",
    )

add("S947",
    study_design_class="44-country dynamic panel GMM regression, 1995-2017",
    evidence_level="high",
    mechanism_family="enforcement",
    outcome_family="water_access",
    quantitative_synthesis_eligible="TRUE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="regulation quality / institutional governance quality, 44 African countries",
    institutional_context="national governments; regulatory institutions",
    )

add("S948",
    study_design_class="mixed-methods comparative study across settlement legal-status categories",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="gazetted vs. ungazetted settlement legal recognition, Botswana",
    institutional_context="Ngamiland district water-supply institutions",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
