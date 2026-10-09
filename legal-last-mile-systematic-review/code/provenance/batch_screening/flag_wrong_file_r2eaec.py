import csv, tempfile, os

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
DB = os.path.join(REPO, "02_screening/full_text/full_text_screening_database.csv")

with open(DB, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

target = "R2EAEC279B644"
found = False
for r in rows:
    if r['record_id'] == target:
        found = True
        assert r['full_text_decision'] == '' and r['final_decision'] == '', "record not open"
        r['full_text_status'] = 'wrong_file_retrieved'
        r['full_text_location'] = ''
        r['notes'] = (
            "wrong_file_retrieved: target is Koros, Juuti, Juuti, Hukka & Asokan (2024) "
            "'Leaving No One Behind: Prospects for User-Owned Urban Water Utilities in Kenya', "
            "DOI 10.1177/1087724X231181076. Delivered PDF is an entirely different document: "
            "Werchota & Nordmann (Nov 2015), 'Using the Water Kiosk to Increase Access to Water "
            "for the Urban Poor in Kenya' (GIZ/BMZ Water Sector Reform Programme case study, "
            "Global Delivery Initiative / World Bank series, on the Water Services Trust Fund and "
            "water kiosks). Same country/topic area but not the target publication -- no shared "
            "authors, no shared title, no shared DOI. full_text_decision left blank; not screened; "
            "file not moved from inbox pending correct retrieval."
        )
        break

assert found, "record_id not found"

fd, tmppath = tempfile.mkstemp(dir=REPO)
with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print("R2EAEC279B644 flagged wrong_file_retrieved.")
