import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
sid = "S657"
assert sid not in existing_ids

rows.append({
    "study_id": sid,
    "study_design_class": "narrative synthesis of primary case-study field data",
    "evidence_level": "moderate-high",
    "mechanism_family": "sanitation-financing institutional mechanisms (household subsidies vs. micro-finance, sanitation-surcharge fees, decentralization without financial transfer, land-tenure barriers)",
    "outcome_family": "household sanitation access/coverage",
    "quantitative_synthesis_eligible": "FALSE",
    "qualitative_synthesis_eligible": "TRUE",
    "legal_context": "Sub-Saharan Africa: decentralization of sanitation responsibility to local authorities; sanitation-surcharge legislation (Burkina Faso, Senegal, Tunisia)",
    "institutional_context": "Hydroconseil/pS-Eau field research consortium; national water/sanitation utilities and NGOs across 5 countries",
})

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"New total: {len(rows)}")
