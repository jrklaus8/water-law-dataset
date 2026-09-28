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
assert by_id["RA2C47DBF8584"]["full_text_decision"] == ""
assert by_id["RA2C47DBF8584"]["final_decision"] == ""

r = by_id["RA2C47DBF8584"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "exclude"
r["final_decision"] = "exclude"
r["exclusion_reason"] = "E05"
r["exclusion_reason_detail"] = ("Narrative literature review synthesizing ~30 secondary published studies on "
                                  "gender, time-use, and water-collection drudgery in low-income urban areas; "
                                  "no original primary data collection and no documented systematic-review "
                                  "search methodology (the authors explicitly disclaim comprehensiveness: "
                                  "'We have not undertaken a comprehensive review of the literature on women's "
                                  "organizing over water'). Institutional/legal themes (illegal settler status, "
                                  "water cartels) appear only incidentally within a broader gender/time-use "
                                  "synthesis, not as the paper's object of study. Extends the established "
                                  "narrative-synthesis exclusion precedent (cf. Foster & Gathu 2024).")
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"

with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

ex_rows.append({
    "record_id": "RA2C47DBF8584",
    "title": "How the Drudgery of Getting Water Shapes Women's Lives in Low-income Urban Communities",
    "authors": "Crow, Ben; McPike, Jamie",
    "year": "2009",
    "stage": "full_text",
    "exclusion_code": "E05",
    "exclusion_reason_detail": ("Narrative literature review with no original primary data collection and no "
                                  "documented systematic-review search methodology; institutional/legal themes "
                                  "appear only incidentally - fails inclusion criterion 3."),
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

print("Batch 136 recorded: 0 includes, 1 exclude.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
