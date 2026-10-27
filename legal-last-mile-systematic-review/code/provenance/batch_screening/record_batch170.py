#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RFEE77DC1C510",  # Razavi - 'Social control' and public participation in water remunicipalization, Cochabamba
    "RB57945A09D4B",  # Kumasi & Agbemor - Tracking user satisfaction of rural water services, northern Ghana
    "R9432B4531BC0",  # Spencer, Meng, Nguyen & Guzinsky - Innovations in Local Governance, Southeast Asia
    "R960A96145969",  # Akpabio - Water and People: Perception and Management Practices, Akwa Ibom Nigeria
    "R706C98313920",  # Cleaver & Toner - The evolution of community water governance in Uchira, Tanzania
]

EXCLUDES = {
    "RCA5C1A9910CA": ("E01", "Grafton, Garrick, Manero & Do (2019), 'The water governance reform framework: Overview and applications to Australia, Mexico, Tanzania, U.S.A and Vietnam.' A macro-scale, basin-level water-RESOURCE governance reform framework applied to the Murray-Darling, Rufiji, and Colorado river basins; concerns water-scarcity/allocation governance at the basin level, not household-level 'last mile' drinking-water access."),
    "R5BBEEFE4A138": ("E01", "Sigler, Mahmoudi & Graham (2015), 'Analysis of behavioral change techniques in community-led total sanitation programs.' A public-health behavior-change intervention methodology review/survey of CLTS program implementers (triggering, transect walks, shame/disgust techniques); no legal/institutional water-access-barrier mechanism content."),
    "R94BF90B2AED5": ("E12", "Magee (2013), 'The politics of water in rural China: a review of English-language scholarship.' Explicitly titled and structured as a secondary literature review of existing scholarship; not itself a primary empirical study."),
    "R9575AD9F87A8": ("E05", "Pawar (2013), 'Water Insecurity: A Case for Social Policy Action by Social Workers.' The abstract states the paper draws on 'secondary data analysis' to build a conceptual social-policy-action framework for social workers; no original empirical data collection."),
    "R96CC88EE0933": ("E04", "Wutich & Ragsdale (2008), 'Water insecurity and emotional distress: Coping with supply, access, and seasonal variability of water in a Bolivian squatter settlement.' A 72-household survey whose outcome variable is emotional distress/mental health, with water-access dimensions used only as independent/exposure variables; the studied outcome is not a water-access outcome."),
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

print(f"Batch 170 recorded: {n_inc} includes, {n_exc} excludes.")
