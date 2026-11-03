import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
sid = "S658"
assert sid not in existing_ids

rows.append({
    "study_id": sid,
    "study_design_class": "historical-archival/legal institutional case study",
    "evidence_level": "high",
    "mechanism_family": "water-district territorial exclusion denying voting rights and political standing over service-provision decisions",
    "outcome_family": "household water/sanitation service access and connection",
    "quantitative_synthesis_eligible": "FALSE",
    "qualitative_synthesis_eligible": "TRUE",
    "legal_context": "United States (Texas): 1971 Texas statute (Article 8280-3.2); Jimenez v. Hidalgo WCID 2; Fonseca v. Hidalgo WCID 2 (1972-1976)",
    "institutional_context": "farmer-controlled Water Control and Improvement Districts (WCIDs)",
})

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"New total: {len(rows)}")
