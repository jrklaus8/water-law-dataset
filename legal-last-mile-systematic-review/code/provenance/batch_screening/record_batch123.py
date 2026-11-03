import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

EXCLUDES = {
    "RA54757489129": {
        "title": "Adapting to climate change: Public water supply in England and Wales",
        "authors": "Arnell N.W.; Delaney E.K.",
        "year": "2006",
        "code": "E01",
        "detail": "Utility-level supply-side climate-adaptation study examining privatized water companies' organizational adaptation strategy and Ofwat's regulatory investment-review process in response to climate-change-driven supply-reliability risk; no household-level access, connection, affordability, or exclusion outcome data -- same rationale as the utility-level-benchmarking exclusion precedent.",
    },
}

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

found = {r["record_id"]: r for r in rows if r["record_id"] in EXCLUDES}
missing = set(EXCLUDES) - set(found)
assert not missing, f"Missing record_ids: {missing}"

for rid, r in found.items():
    assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided: {r}"

for rid, info in EXCLUDES.items():
    r = found[rid]
    r["full_text_decision"] = "exclude"
    r["final_decision"] = "exclude"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["exclusion_reason"] = info["code"]
    r["exclusion_reason_detail"] = info["detail"]

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"Updated {len(found)} records in full_text_screening_database.csv")

with open(EXCLOG, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    exc_fieldnames = reader.fieldnames
    exc_rows = list(reader)

for rid, info in EXCLUDES.items():
    exc_rows.append({
        "record_id": rid,
        "title": info["title"],
        "authors": info["authors"],
        "year": info["year"],
        "stage": "full_text",
        "exclusion_code": info["code"],
        "exclusion_reason_detail": info["detail"],
        "reviewer": REVIEWER,
        "date": DATE,
    })

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EXCLOG))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=exc_fieldnames)
    writer.writeheader()
    writer.writerows(exc_rows)
os.replace(tmppath, EXCLOG)
print(f"Appended {len(EXCLUDES)} rows to exclusion_log.csv. New total: {len(exc_rows)}")
