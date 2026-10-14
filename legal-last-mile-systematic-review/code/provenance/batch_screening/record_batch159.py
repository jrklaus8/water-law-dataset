#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RD6FBE5C6BF3B",  # Mulwafu & Msosa - IWRM and poverty reduction, Malawi
    "RD601DD13E14F",  # Roy, Akshintala & Sharma - Water Governance and Supply, Delhi/JNNURM
    "RD460C6C5BA82",  # Lewis - public infrastructure, municipal economic development, Kenya
    "RD1C3B399E90B",  # Townsend & Eyles - potable water regulation, Tijuana Mexico
    "RD17D28844F71",  # Brady & Gray - water pricing, Ireland
    "RD0D63BD0DF34",  # Vasquez - municipal water services, Guatemala official perceptions
]

EXCLUDES = {
    "RD24CFA69A828": ("E05", "Khan (1988), 'Institutional Aspects of Water Supply and Sanitation in Asia.' A normative policy-synthesis review drawing on secondary published national statistics across multiple Asian countries, not an original empirical study with primary data collection -- matches the Nallathiga (2011) and Ezeudu (2019) precedent."),
    "RD1DE793F1296": ("E01", "Otis, Gilbertson, McCarthy & Barnett (2004), 'Performance management and inventory system for onsite/cluster wastewater treatment facilities.' A technical description of a GIS/database software tool for permit-tracking and regulatory administration in rural Minnesota, not an empirical study of a legal/institutional water-access-barrier mechanism -- matches the tool/methodology-development exclusion precedent."),
    "RD135735976C0": ("E06", "Bes-Pia, Cuartas-Uribe, Mendoza-Roca & Alcaina-Miranda (2010), 'Study of the behaviour of different NF membranes for the reclamation of a secondary textile effluent in rinsing processes.' Pure membrane-technology engineering study for industrial wastewater reuse, no legal/institutional water-access-barrier mechanism analyzed."),
    "RCFA60F99F5A8": ("E06", "Cain, Irias & Pratt (2009), 'Seismic Safety of Water Lifelines: An Ongoing Process.' Pure engineering paper on seismic retrofitting design standards for a California water utility's infrastructure, no legal/institutional water-access-barrier mechanism analyzed."),
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

print(f"Batch 159 recorded: {n_inc} includes, {n_exc} excludes.")
