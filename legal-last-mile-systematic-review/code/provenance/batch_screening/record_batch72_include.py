import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

rid = "R08C74B34D928"
reviewer = "Claude-AI-fulltext-2026-09-21"
changed = 0
for r in rows:
    if r["record_id"] == rid:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", "already decided"
        r["full_text_decision"] = "include"
        r["final_decision"] = "include"
        r["reviewer_1"] = reviewer
        r["notes"] = "Extracted as S541. Multi-country (Afghanistan/Pakistan/India/Nepal/China/Bhutan) narrative synthesis of urban water governance across 8 HKH cities; documents unenforced groundwater abstraction bye-laws, illegal borewell proliferation, absence of metering/differential pricing, informal tanker markets, and inequitable 'zero day' distribution. Legal Institutional Evidence Appraisal Framework (doctrinal/policy-audit synthesis, no systematic-review search methodology)."
        changed += 1

assert changed == 1

fd, tmp = tempfile.mkstemp(dir="02_screening/full_text")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, db_path)

print("done, db changed", changed)
