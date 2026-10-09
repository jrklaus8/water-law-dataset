import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

rid = "R05E6A40917AB"
reviewer = "Claude-AI-fulltext-2026-09-21"
changed = 0
for r in rows:
    if r["record_id"] == rid:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", "already decided"
        r["full_text_decision"] = "include"
        r["final_decision"] = "include"
        r["reviewer_1"] = reviewer
        r["notes"] = "Extracted as S544. Qualitative case study (30 in-depth interviews, WV mineral/surface owners and concerned citizens) of household groundwater security around hydraulic fracturing. Documents real legal-administrative mechanisms: WV code 22-6A-18 'presumed liability' statute requiring industry-controlled baseline/post-drill water testing within a 1500-foot setback, delayed/incomplete test results, non-disclosure agreements, exemption of oil/gas wastewater from the Safe Drinking Water Act ('Halliburton Loophole'), and WVDEP's documented failure to enforce Underground Injection Control requirements. CASP (qualitative)."
        changed += 1

assert changed == 1

fd, tmp = tempfile.mkstemp(dir="02_screening/full_text")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, db_path)

print("done, db changed", changed)
