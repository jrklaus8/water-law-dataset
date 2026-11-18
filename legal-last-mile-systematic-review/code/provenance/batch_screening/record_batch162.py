#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RBDEF2943A1C3",  # Hylton & Charles - Sao Paulo favelas water services regularization
    "RBDD2A9AC8690",  # Costa et al - Belo Horizonte municipal committees
    "RBB42A504E371",  # Bakker et al - Indigenous peoples water governance, Canada
    "RBA427862C34C",  # Kibassa - cost recovery/human right to water, Ileje Tanzania
    "RB932E7855B82",  # Wanda et al - WASH governance disaster risk, Karonga Malawi
    "RB894AA51801F",  # Wanda, Gulula & Phiri - public water supply, Mzuzu City Malawi
    "RB7A0171C272A",  # Donoso - urban water pricing, Chile
    "RB76C55D87C12",  # Komala, Nur & Septanisa - real demand survey, Padang Indonesia
]

EXCLUDES = {
    "RB937F6B14510": ("E01", "Kolb & Williamson (2012), 'Water and Sewer Infrastructure Challenges as a Barrier to Housing Development in the Marcellus Shale Region.' A case study of utility infrastructure-expansion capacity and cost constraints (driven by Clean Water Act enforcement and Chesapeake Bay TMDL compliance costs) limiting new housing development in a US natural-gas boom region; concerns aggregate housing-supply/rent effects and utility capacity, not household-level legal/institutional water-access exclusion mechanisms."),
    "RB8541E7A11B9": ("E01", "Alley, Barr & Mehta (2018), 'Infrastructure disarray in the clean Ganga and clean India campaigns.' An anthropological case study of wastewater/fecal-sludge management infrastructure governance and caste-based manual-scavenging labor practices in India; concerns the 'back end' sewage-treatment-chain infrastructure and sanitation labor rather than household-level water/sanitation access-barrier determination."),
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

print(f"Batch 162 recorded: {n_inc} includes, {n_exc} excludes.")
