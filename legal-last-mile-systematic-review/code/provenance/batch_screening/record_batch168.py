#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R4EF71E7E284E",  # Swyngedouw - Contradictions of Urban Water Provision, Guayaquil Ecuador
    "R85BDB2AE39E0",  # Kooy & Walter - Packaged Drinking Water Supply, Jakarta
    "R8DBAA192D598",  # Hordijk, Sara & Sutherland - comparative water governance, 4 southern cities
    "RBD155EDBD079",  # Romero Lankao & Gunther - Neoliberal modernization, Mexico City/Buenos Aires
    "R8A2445A92C67",  # Ducrot, Bueno, Barban & Reydon - land tenure gaming approach, Sao Paulo periphery
    "RB279F6DED9CF",  # Hill - E-Governance: Silencing Vulnerable Populations, Cape Town
    "R8D4D5CF53A02",  # Hanrahan - Water (in)security in Canada, Indigenous exclusion
    "R96660AABF429",  # Ayalew, Chenoweth, Malcolm, Mulugetta, Okotto & Pedley - small independent water providers, Kenya/Ethiopia
]

EXCLUDES = {
    "RC61650B037D2": ("E12", "Hutchings et al. (2015), 'A systematic review of success factors in the community management of rural water supplies over the past 30 years.' A secondary systematic review/meta-analysis synthesizing 174 published case studies; not itself a primary empirical study, and including it as primary evidence in this review's own synthesis would risk double-counting the underlying primary studies."),
    "R8DC43EB66951": ("E04", "Shandra, Shandra & London (2011), 'World Bank Structural Adjustment, Water, and Sanitation: A Cross-National Analysis of Child Mortality in Sub-Saharan Africa.' A cross-national two-way fixed-effects panel regression (31 nations, 4 time points) whose sole dependent variable is child mortality rate; access to improved water/sanitation is included only as an independent/control variable, not as the outcome being isolated."),
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

print(f"Batch 168 recorded: {n_inc} includes, {n_exc} excludes.")
