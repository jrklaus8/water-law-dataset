#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"
TODAY = date.today().isoformat()

RID = "R8F394022B0DC"
CODE = "E01"
DETAIL = ("Roncoli, Dowd-Uribe, Orlove, West & Sanon (2016), 'Who counts, what counts: representation and "
          "accountability in water governance in the Upper Comoe sub-basin, Burkina Faso.' On closer reading, "
          "the local water user committee (Comite Local de l'Eau) studied is a basin-scale IWRM water-resource "
          "ALLOCATION institution whose core function is developing an annual irrigation water-allocation plan "
          "partitioning basin water supplies among agro-industrial users (SN-SOSUCO sugar company, UCEPAK) and "
          "riparian farmers; the national water utility (ONEA) appears only as one of several allocation "
          "stakeholders, not as the focus of analysis. This is basin/catchment-scale water-resources allocation "
          "governance, not a household water/sanitation access study, consistent with the van Steenbergen "
          "Balochistan and Tapela Zimbabwe (this same batch) basin-scale exclusion precedent.")

with open(SCREEN, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

found = False
for row in rows:
    if row["record_id"] == RID:
        assert row["full_text_decision"] == "include", f"unexpected prior state: {row['full_text_decision']}"
        row["full_text_status"] = "excluded"
        row["full_text_decision"] = "exclude"
        row["final_decision"] = "exclude"
        row["exclusion_reason"] = CODE
        row["exclusion_reason_detail"] = DETAIL
        row["notes"] = f"[{TODAY}] Corrected from initial include to exclude ({CODE}) after closer full-text reading confirmed basin-scale irrigation/industrial water-allocation focus rather than household water access; see exclusion_reason_detail."
        found = True
assert found

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(SCREEN))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, SCREEN)

# fetch metadata for exclusion log
meta = {}
with open(SCREEN, newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        meta[row["record_id"]] = row

with open(EXCLOG, newline="") as f:
    r = csv.DictReader(f)
    ex_fieldnames = r.fieldnames
    ex_rows = list(r)

existing_ids = {row["record_id"] for row in ex_rows}
assert RID not in existing_ids

m = meta[RID]
ex_rows.append({
    "record_id": RID,
    "title": m["title"],
    "authors": m["authors"],
    "year": m["year"],
    "stage": "full_text",
    "exclusion_code": CODE,
    "exclusion_reason_detail": DETAIL,
    "reviewer": "Claude",
    "date": TODAY,
})

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXCLOG))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ex_fieldnames)
    w.writeheader()
    for row in ex_rows:
        w.writerow(row)
os.replace(tmp, EXCLOG)

print("Corrected R8F394022B0DC to exclude E01 and added to exclusion log.")
