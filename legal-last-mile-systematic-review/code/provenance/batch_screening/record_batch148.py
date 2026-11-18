#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RE2092C0B2608", "RE1E71A927835", "RE1B2A5D017D1", "RE0FFA253B377", "RDF9D6AE68D61", "RDECE6D5D99AE", "RDE53A2FE1BAD"]

EXCLUDES = {
    "RE26903A758D8": ("E01", "Life-cycle costs approach (LCCA) methodology paper examining government WASH capital-expenditure allocation patterns causing service 'slippage' in rural Andhra Pradesh, India. A public-finance/costing-methodology study; no specific legal/administrative eligibility, documentation, or tenure mechanism creating differential household access is analyzed."),
    "RE17576EC9085": ("E01", "Ethnographic study of gender, technology and household water-collection practices in Kankan, Guinea, framed through modernity/tradition and gender-technology theory. Documents SEG utility rationing practices as incidental context, but the paper's object of study is gendered technology use and cultural meaning of water, not a legal/administrative access-barrier mechanism."),
    "RDEE9E6CB3035": ("E01", "Sound-studies/cultural-anthropology ethnography analyzing 'soundscapes' of water collection in Govindpuri slums, Delhi, as a cultural system. Analytical framework is sound/listening politics, not a legal/institutional access-barrier mechanism; water scarcity is contextual background, not the object of legal-mechanism analysis."),
}

def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow(row)
    os.replace(tmp, path)

with open(SCREEN, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

n_inc = n_exc = 0
for row in rows:
    rid = row["record_id"]
    if rid in INCLUDES:
        row["full_text_status"] = "included"
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["reviewer_1"] = "Claude"
        n_inc += 1
    elif rid in EXCLUDES:
        code, detail = EXCLUDES[rid]
        row["full_text_status"] = "excluded"
        row["full_text_decision"] = "exclude"
        row["final_decision"] = "exclude"
        row["exclusion_reason"] = code
        row["exclusion_reason_detail"] = detail
        row["reviewer_1"] = "Claude"
        n_exc += 1

atomic_write(SCREEN, fieldnames, rows)

meta = {}
with open(SCREEN, newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        meta[row["record_id"]] = row

with open(EXCLOG, newline="") as f:
    r = csv.DictReader(f)
    ex_fieldnames = r.fieldnames
    ex_rows = list(r)

for rid, (code, detail) in EXCLUDES.items():
    m = meta[rid]
    ex_rows.append({
        "record_id": rid,
        "title": m["title"],
        "authors": m["authors"],
        "year": m["year"],
        "stage": "full_text",
        "exclusion_code": code,
        "exclusion_reason_detail": detail,
        "reviewer": "Claude",
        "date": TODAY,
    })

atomic_write(EXCLOG, ex_fieldnames, ex_rows)

print(f"Batch 148 recorded: {n_inc} includes, {n_exc} excludes.")
