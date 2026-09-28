#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["REB79407B1F91", "RE875C1FD167C", "RE7568F6E701C", "RE6EEC29886F0", "RE63BCE294E12", "RE3D6525404B1"]

EXCLUDES = {
    "REA39654B750D": ("E01", "NGO/practitioner methods paper on strengthening Community-Led Total Sanitation (CLTS) programmes in Asia (welfare mapping, community monitoring, capacity building). Describes participatory NGO-facilitation techniques, not a government legal/administrative access-barrier mechanism; no statute, eligibility, or documentation framework analyzed."),
    "RE9F82B212206": ("E01", "Methodological development paper presenting a participatory risk-scoring framework to assess sanitation-related health risks in Maputo, Mozambique. A technical/methodological risk-assessment tool validation study; no legal/institutional access-barrier mechanism examined."),
    "RE78B9B796A4A": ("E01", "Composite-index development study (the SIPE approach: Socio-economic, Institutional, Physiochemical, Environmental) measuring a 'safe water adaptability index' across upazilas in southwest Bangladesh. The institutional dimension refers to which government departments are involved in managing salinity/arsenic/drought risk, not a specific legal/administrative mechanism creating differential household access; a composite vulnerability index, not a legal-mechanism analysis."),
    "RE4EEC48EC1E1": ("E01", "Study of a market-based social enterprise (Sanergy) providing sanitation services in Nairobi and Kampala informal settlements, comparing user practices and small-scale providers. Focus is on market-based service-delivery innovation and business scaling challenges, not a specific government legal/administrative access-barrier mechanism."),
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

print(f"Batch 147 recorded: {n_inc} includes, {n_exc} excludes.")
