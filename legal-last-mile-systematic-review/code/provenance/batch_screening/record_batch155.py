#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RF04979D5CC95",  # Hendry 2016 - Customer Forum, Scotland water regulation
    "REFCB6826A20A",  # Nagaraj & Namasivayam 2010 - institutions/entitlements Cuddalore Tamil Nadu
    "REF1851D5AE3F",  # Clifford-Holmes et al - modelling muddled middle, South Africa
    "RED1DDE4608AA",  # Abubakar 2016 - quality dimensions of public water services, Abuja
    "RED031F3340F7",  # Marson & van Dijk 2016 - Zambian water sector regulation pro-poor
    "REC9BE7729D00",  # Laryea-Adjei & van Dijk 2012 - Ghana decentralisation water governance
    "REC4A13B5CAD0",  # Sally et al 2014 - urbanization community-managed water, Buea Cameroon
    "REB42ED2971BB",  # Heller, Rezende & Cairncross 2014 - Brazil public-private pendulum
]

EXCLUDES = {
    "RF0679308DDFB": ("E01", "Weaver, O'Keeffe, Hamer & Palmer (2019), 'A civil society organisation response to water service delivery issues in South Africa drives transformative praxis. Part 1: Emergence and practice.' Core analytical lens is Wenger's Communities of Practice (CoP) theory applied to the emergence/internal practice of a single civil-society organisation (Water for Dignity), not an empirical study of a legal/institutional mechanism's effect on water access -- matches established precedent excluding participation/organisational-framework-development papers (cf. Das, Laishram & Jawed 2019)."),
    "RECB3D410CC43": ("E05", "Nigam & Ghosh (1995), 'A model of costs and resources for rural and peri-urban water supply and sanitation in the 1990s.' A global cost-estimation and financing-strategy model built from secondary WHO/World Bank statistics and normative policy recommendations, not an empirical study of a specific country's legal/institutional mechanism or original primary data collection."),
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

print(f"Batch 155 recorded: {n_inc} includes, {n_exc} excludes.")
