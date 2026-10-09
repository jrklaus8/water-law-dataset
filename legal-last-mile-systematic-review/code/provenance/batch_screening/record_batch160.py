#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RCF31FA5B9CF9",  # Kalulu & Hoko - Blantyre Water Board performance, Malawi
    "RCF1AD58436DF",  # Begolli & Lajci - Kosova water sector reform
    "RCD44792548EF",  # Guimaraes, Malheiros & Marques - Inclusive governance, Brazil
    "RC8FC125A9F16",  # Gerlach & Franceys - Regulating water services for the poor, Amman
]

EXCLUDES = {
    "RCEF41B961251": ("E01", "Lagerwey (2009), 'In their own words: nurses' discourses of cleanliness from the Rehoboth Mission.' A historical discourse-analysis study of missionary nursing culture and cleanliness rhetoric at a Navajo mission hospital, 1903-1965 -- no legal/institutional water-access-barrier mechanism analyzed."),
    "RCEDB672130C6": ("E03", "Jimenez-Moleon & Gomez-Albores (2011), 'Waterborne diseases in the state of Mexico, Mexico (2000-2005).' A spatial-epidemiological GIS study correlating waterborne-disease incidence with water/sewer service coverage; the institutional/regulatory context is background only, matching the Rowles et al. (2020) Texas colonias precedent for water-quality/health-outcome-focused studies."),
    "RCD3248F027A6": ("E01", "Samwel & Gabizon (2009), 'Improving school sanitation in a sustainable way for a better health of school children in the EECCA and in the new EU member states.' A technical/engineering demonstration-project report on dry urine-diverting toilet installation and user-acceptance surveys at rural schools, not an empirical study of a legal/institutional household water-access-barrier mechanism."),
    "RCC7EA7EF993C": ("E01", "Nabulo & Cole, 'Uganda: Environmental Health Concerns' (encyclopedia entry). A broad country-profile encyclopedia article covering geography, demography, HIV/AIDS, malaria, industrial pollution, and food safety, with only a brief listing of water-sector legislation among many other environmental laws -- not a focused empirical study of a legal/institutional water-access-barrier mechanism."),
    "RCBA43CCC1A08": ("E05", "Rusca & Schwartz (2014), \"'Going with the grain': accommodating local institutions in water governance.\" An explicitly framed literature-review essay synthesizing institutional-governance theory (Good Governance Agenda critique, bricolage, elite capture); its one illustrative empirical example (Lilongwe Malawi water user associations) is drawn from a separate co-authored paper, not original data collected for this article -- matches the Nallathiga/Ezeudu review-paper precedent."),
    "RCB7A81AE9AD2": ("E05", "Neto & Tropp (2000), 'Water supply and sanitation services for all: global progress during the 1990s.' A global policy-synthesis paper reporting secondary UN coverage statistics (Table 1, regional water/sanitation coverage 1990-2000, sourced from United Nations 2000) and institutional/economic policy discussion, not an original empirical study with primary data collection -- matches the Nigam & Ghosh (1995) precedent."),
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

print(f"Batch 160 recorded: {n_inc} includes, {n_exc} excludes.")
