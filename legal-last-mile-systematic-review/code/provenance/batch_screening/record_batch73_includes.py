import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

decisions = {
    "RB432D9F6004C": "Extracted as S542. Companion narrative review to S541 (Water Policy 22 special issue on HKH), across Bangladesh, India, Nepal, Pakistan; documents own supply-demand data (Table 9, 13 cities) and legal-administrative mechanisms (departmental mandate limitation blocking spring recharge, institutional coordination failures delaying/escalating water-augmentation projects, tanker pricing burden restricting poor households' water use). Legal Institutional Evidence Appraisal Framework (narrative synthesis, no systematic-review search protocol).",
    "R0312B751BEAE": "Extracted as S543. Mixed-methods study (26 semi-structured interviews across 4 Ghanaian cities + secondary data + GIS mapping) of water privatization and access inequality in urban Ghana. Documents genuine legal-administrative mechanisms: informal-settlement residents barred from formal pipe connections for lack of legal documentation, weak regulatory environment enabling private-vendor price gouging, borehole certification/licensing requirement (Water Resources Commission), and GWCL water-rationing schedule producing unequal service outcomes. MMAT (mixed methods).",
}

reviewer = "Claude-AI-fulltext-2026-09-21"
changed = 0
for r in rows:
    rid = r["record_id"]
    if rid in decisions:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided"
        r["full_text_decision"] = "include"
        r["final_decision"] = "include"
        r["reviewer_1"] = reviewer
        r["notes"] = decisions[rid]
        changed += 1

assert changed == len(decisions), f"expected {len(decisions)}, got {changed}"

fd, tmp = tempfile.mkstemp(dir="02_screening/full_text")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, db_path)

print("done, db changed", changed)
