import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

rid = "RC85926098F35"
reviewer = "Claude-AI-fulltext-2026-09-21"
changed = 0
for r in rows:
    if r["record_id"] == rid:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", "already decided"
        r["full_text_decision"] = "include"
        r["final_decision"] = "include"
        r["reviewer_1"] = reviewer
        r["notes"] = "Extracted as S545. Qualitative case study (27 semi-structured interviews, 35 individuals) of small low-income community participation in California's SGMA groundwater-governance regime. Documents real legal-administrative mechanisms: institutional exclusion of privately-owned water systems and domestic-well communities from formal Groundwater Sustainability Agency (GSA) representation, financial cost of voting representation, transparency/notification failures, and 'voice but not vote' disenfranchisement, with drinking-water needs largely absent from Groundwater Sustainability Plans. CASP (qualitative)."
        changed += 1

assert changed == 1

fd, tmp = tempfile.mkstemp(dir="02_screening/full_text")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, db_path)

print("done, db changed", changed)
