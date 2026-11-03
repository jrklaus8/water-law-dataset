import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}
r = by_id["R5571A513905A"]
assert r["full_text_decision"] == ""
assert r["final_decision"] == ""

r["full_text_status"] = "wrong_file_retrieved"
r["full_text_location"] = ""
r["notes"] = ("Title/author nominally match a record for Truelove Y. (2021), 'Gendered infrastructure and "
              "liminal space in Delhi's unauthorized colonies,' Environment and Planning D: Society and Space, "
              "DOI 10.1177/02637758211055483. However, the delivered PDF is an entirely different publication: "
              "a 2019 multi-author digital magazine/workshop output ('Urban Infrastructures', produced from the "
              "'Labouring Urban Infrastructures' workshop, Durham UK, June 2019, edited by Ruszczyk/Stokes/De "
              "Coss), running to 16 short essays across many research locations. It does contain a differently-"
              "titled short magazine essay by the same author ('The Body as Infrastructure: Gender and the "
              "Everyday Practices and Labour of Water's Urban Circulation,' Delhi, India, Yaffa Truelove, "
              "pp.27-29) on a related but distinct theme -- but this is not the target 2021 peer-reviewed "
              "journal article and cannot substitute for it. Left open pending a correct re-retrieval of the "
              "actual target article. Not moved from the inbox per the wrong_file_retrieved convention "
              "(see R33E4CEE682AC/R58E83E4193E6 precedent).")

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

print("R5571A513905A flagged wrong_file_retrieved.")
