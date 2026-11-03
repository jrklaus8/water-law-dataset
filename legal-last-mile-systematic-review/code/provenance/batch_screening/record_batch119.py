import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"

INCLUDES = {
    "RFDCD6A65E245": "Book chapter synthesizing 12 primary Hydroconseil/pS-Eau field case studies (Mali, Burkina Faso, Senegal, Niger, Uganda) documenting institutional/financing mechanisms (household-subsidy schemes, sanitation-surcharge fee mechanisms, decentralization of sanitation responsibility to local authorities without corresponding financial transfer, land-tenure/title-document barriers preventing informal-settlement residents from demanding service) against real tracked household-level outcome data: ~900,000-1 million people gaining sanitation access via a targeted subsidy scheme over 14-15 years in Ouagadougou/Bobo-Dioulasso, and Senegal's PAQPUD program interruption leaving 56% of registered household requests unfulfilled. Extracted as S657.",
}

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

found = {r["record_id"]: r for r in rows if r["record_id"] in INCLUDES}
missing = set(INCLUDES) - set(found)
assert not missing, f"Missing record_ids: {missing}"

for rid, r in found.items():
    assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided: {r}"

for rid in INCLUDES:
    r = found[rid]
    r["full_text_decision"] = "include"
    r["final_decision"] = "include"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["notes"] = INCLUDES[rid]

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"Updated {len(found)} records in full_text_screening_database.csv")
