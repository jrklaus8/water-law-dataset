import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}

assert by_id["RD76AC7C9D711"]["full_text_decision"] == ""
assert by_id["RD76AC7C9D711"]["final_decision"] == ""

r = by_id["RD76AC7C9D711"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "exclude"
r["final_decision"] = "exclude"
r["exclusion_reason"] = "E01"
r["exclusion_reason_detail"] = ("Social-capital measurement-instrument methodology paper (position-generator "
                                  "survey tool development/validation for slum research); water-connection "
                                  "access appears only as a brief illustrative validation vignette (~half a "
                                  "page) demonstrating the instrument's real-life relevance, not as the "
                                  "paper's object of study - no legal, administrative, institutional, "
                                  "regulatory or governance factor is itself examined - fails inclusion "
                                  "criterion 2. Extends the established methodological-contribution "
                                  "precedent (cf. Silva Rodriguez de San Miguel et al. 2019).")
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"

with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

ex_rows.append({
    "record_id": "RD76AC7C9D711",
    "title": "Measuring Social Capital in a Philippine Slum",
    "authors": "Matous, Petr; Ozawa, Kazumasa",
    "year": "2010",
    "stage": "full_text",
    "exclusion_code": "E01",
    "exclusion_reason_detail": ("Social-capital measurement-instrument methodology paper; water-connection "
                                  "access is a brief illustrative validation vignette, not the paper's object "
                                  "of study - fails inclusion criterion 2."),
    "reviewer": "Claude-AI-fulltext-2026-09-21",
    "date": "2026-09-23",
})

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ex_fieldnames)
    w.writeheader()
    w.writerows(ex_rows)
os.replace(tmp, EXLOG)

print("Batch 134 recorded: 0 includes, 1 exclude.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
