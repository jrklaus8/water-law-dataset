#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RE3D6C0549F37",  # Bhattarai et al 2021 - gender inequality urban water governance, Nepal
    "RE290B71E882F",  # Wait et al 2020 - well water outreach disparities, North Carolina
    "RE27DBC552685",  # Lloyd Owen 2013 - Glas Cymru not-for-profit PPP, Wales
    "RE26DB8683A1F",  # Montgomery & Dacin - Detroit water wars, institutional renewal
    "RE080CB357B2C",  # Marques, Simoes & Berg 2013 - Cape Verde water sector regulation
    "RDF291C6CC5DD",  # Grimes 2011 - right to water, South Africa
    "RDE788100646E",  # Krasznai Kovacs et al 2019 - political ecology, lower Himalayas
]

EXCLUDES = {
    "RE122123AF5EF": ("E05", "Nallathiga (2011), 'Urban water supply sector in India: setting the reform agenda for improving service delivery.' A normative policy-reform-agenda review article drawing on secondary published statistics and comparative tables, not an original empirical study with primary data collection."),
    "RE0841B3F072D": ("E01", "Ruet, Gambiez & Lacour (2007), 'Private appropriation of resource: Impact of peri-urban farmers selling water to Chennai Metropolitan Water Board.' Core focus is upstream bulk-water-sourcing property-rights conflict and changing agricultural practices among peri-urban/rural farmers supplying the metropolitan utility, not a household/domestic last-mile water-access barrier mechanism for urban residents."),
    "RDFA05DD5B85A": ("E06", "Mulas, Corona, Haimi, Sundell, Heinonen & Vahala (2011), 'Estimating nitrate concentration in the post-denitrification unit of a municipal wastewater treatment plant.' Pure engineering/statistical soft-sensor design study for wastewater treatment plant process control, no legal/institutional water-access-barrier mechanism analyzed."),
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

print(f"Batch 157 recorded: {n_inc} includes, {n_exc} excludes.")
