import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"
log_path = "02_screening/exclusion_log/exclusion_log.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

rid = "R81549C4709FC"
found = False
for r in rows:
    if r["record_id"] == rid:
        assert r["full_text_decision"] == "exclude" and r["final_decision"] == "exclude", "unexpected state, aborting"
        r["full_text_decision"] = ""
        r["final_decision"] = ""
        r["reviewer_1"] = ""
        r["exclusion_reason"] = ""
        r["exclusion_reason_detail"] = ""
        r["notes"] = (
            r["notes"].rstrip()
            + " Fourth retrieval attempt (2026-09-21, Google Drive inbox 'Check drive now' batch): again delivered "
            "the wrong file -- this time chs.19-20 of the same edited volume (Sherpa, 'Climate Change in Nepal "
            "through an Indigenous Environmental Justice Lens,' DOI 10.4324/9781003371175-25; and Awale, 'Women, "
            "Water, and Weather: Kavre Villages Adapt to the Increasing Impacts of the Climate Crisis,' DOI "
            "10.4324/9781003371175-26), confirmed via full-text read -- neither 'Singh' nor 'Political Capabilities' "
            "appears anywhere in the delivered PDF. An initial pass mistakenly recorded this record as excluded "
            "(E01) based on the wrong delivered file's content without first checking this record's prior "
            "full_text_status/notes history; that erroneous decision was caught and reverted the same session "
            "(see CHANGELOG.md). wrong_file_retrieved flag remains in place; record still open pending correct "
            "retrieval of Singh & Singh ch.18 (DOI 10.4324/9781003371175-24)."
        )
        found = True
        break

assert found, f"{rid} not found"

fd, tmp = tempfile.mkstemp(dir="02_screening/full_text")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, db_path)

with open(log_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    log_fieldnames = reader.fieldnames
    log_rows = list(reader)

before = len(log_rows)
log_rows = [r for r in log_rows if r["record_id"] != rid]
after = len(log_rows)
assert before - after == 1, f"expected to remove exactly 1 row, removed {before-after}"

fd, tmp = tempfile.mkstemp(dir="02_screening/exclusion_log")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=log_fieldnames)
    writer.writeheader()
    writer.writerows(log_rows)
os.replace(tmp, log_path)

print("done. db reverted, exclusion_log rows now", after, "(was", before, ")")
