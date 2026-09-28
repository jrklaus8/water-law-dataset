import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updates = {
    "RDA537B7BBB17": (
        "Google Drive inbox delivery (2026-09-21) did not match this record: target is 'Fecal sludge management (FSM): "
        "Analytical tools for assessing FSM in cities', but the PDF delivered was Agbo, Jeffrey & Sule (2025), 'Evaluation "
        "of failings in urban water supply and sanitation systems in Sub-Saharan Africa: a systematic review to inform "
        "future planning', Journal of Water, Sanitation and Hygiene for Development 15(2):148-165, doi "
        "10.2166/washdev.2025.267 -- confirmed via full-text read. This is itself a systematic review (secondary), not "
        "the target FSM tools paper. full_text_status was 'not_retrievable' (CDN-blocked); now 'wrong_file_retrieved'. "
        "Record left open pending correct retrieval."
    ),
    "R22849E39FE23": (
        "Google Drive inbox delivery (2026-09-21) did not match this record: target is 'Community engagement and "
        "capacity building as determinants of rural water supply functionality: a case of traditional authority "
        "Mankhambira in Nkhata Bay District, Malawi', but the PDF delivered was Suleiman (2011), 'Civil society: a "
        "revived mantra in the development discourse', Water Policy 13:87-101, doi 10.2166/wp.2010.087 (Accra water "
        "utility privatisation governance case study) -- confirmed via full-text read. full_text_status was "
        "'not_retrievable' (CDN-blocked); now 'wrong_file_retrieved'. Record left open pending correct retrieval."
    ),
}

changed = 0
for r in rows:
    rid = r["record_id"]
    if rid in updates:
        r["full_text_status"] = "wrong_file_retrieved"
        r["notes"] = (r["notes"] + " " if r["notes"] else "") + updates[rid]
        changed += 1

assert changed == len(updates), f"expected {len(updates)}, got {changed}"

fd, tmp = tempfile.mkstemp(dir="02_screening/full_text")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, db_path)

print("done, updated", changed, "records")
