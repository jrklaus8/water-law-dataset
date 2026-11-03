#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R7A3F1A708032",  # Masanyiwa, Niehof & Termeer - Users' perspectives on decentralized rural water services, Tanzania
    "R9BEC06E5E577",  # Singh - Mapping Poverty to Reach the Urban Poor, Madhya Pradesh
    "R9F1FB9F1D75D",  # Das & Walton - Political Leadership and the Urban Poor: Local Histories, Delhi
    "R9D838E8FBB65",  # Galvin & Roux - Dam state capture: cascading effect on Department of Water and Sanitation, South Africa
    "R9CCA5D7854A6",  # Liu Haiyan - Water supply and the reconstruction of urban space, early 20th-century Tianjin
    "R9D4088D1FDFD",  # Chng - Privatization and Citizenship: Local politics of water in the Philippines
    "RA268D41C7EFC",  # Abrahams, Mhlongo & Napo - A gendered analysis of water and sanitation services policies, South Africa
]

EXCLUDES = {
    "R980187687E77": ("E01", "MacKillop & Boudreau (2008), 'Water and power networks and urban fragmentation in Los Angeles: Rethinking assumed mechanisms.' A macro-scale historical/political-economy analysis of LADWP network integration and city annexation politics; no household-level connection, eligibility, disconnection, or tariff content."),
    "R9D9CD0074631": ("E01", "Mahon & Fernandes (2010), 'Menstrual hygiene in South Asia: a neglected issue for WASH programmes.' A study of menstrual hygiene management practices, cultural taboos, and WASH-programme neglect of hygiene products/facilities; concerns gender-health and hygiene-product access, not a legal/institutional water-access-barrier mechanism."),
    "R9E976E52357D": ("E03", "Driedger, Mazur & Mistry (2014), 'The evolution of blame and trust: an examination of a Canadian drinking water contamination event.' A media/focus-group risk-perception study of public blame and trust following the Walkerton, Ontario E. coli water-quality contamination event; concerns water-quality-regulation trust/blame perceptions, not a household water-access-barrier mechanism."),
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

print(f"Batch 171 recorded: {n_inc} includes, {n_exc} excludes.")
