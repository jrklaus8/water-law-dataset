#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RF6E405620386",  # Kumasi, Agbemor & Burr 2019 - rural water asset management, Ghana decentralised governance
    "RF6B313F45217",  # Nzengya 2015 - master operators/water kiosks DMM, Lake Victoria Kenya
    "RF69CDD7A3484",  # Helgegren et al 2021 - multiple regime analysis, Bolivia
    "RF611C2722057",  # Meeks 2018 - Property Rights and Water Access, Peru land titling (effect_sizes eligible)
    "RF564D516EE5E",  # Jones, Reed & Bevan 2003 - Water and sanitation for the disabled
    "RF2B2F583825D",  # Ravnborg & Jensen 2012 - water governance challenge, five countries
    "RF289721552FD",  # Smith 2004 - corporatization Cape Town
    "RF12971C35B2E",  # Adeoti & Fati 2020 - barriers to piped water extension, Ekiti State Nigeria
    "RF0C8946FC9E3",  # Novotny et al 2018 - social/political construction of latrines, Ethiopia
]

EXCLUDES = {
    "RF1E7023008C0": ("E01", "Onabolu, Jimoh, Igboro, Sridhar, Onyilo, Gege & Ilya (2011), 'Source to point of use drinking water changes and knowledge, attitude and practices in Katsina State, Northern Nigeria.' Core empirical contribution is a water-quality tracking study (bacteriological/physico-chemical deterioration from source to household storage) combined with a KAP survey on water handling/hygiene practices; institutional/legislative framework assessment is a background component (Part 1) supporting a water-quality monitoring system, not an analysis of a legal/institutional mechanism creating a last-mile water-access barrier."),
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

print(f"Batch 154 recorded: {n_inc} includes, {n_exc} excludes.")
