#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "REA98E915A1CD",  # Tynan 2013 - 19th century London water supply, regulation history
    "RE992755C7ABF",  # Pizzi 2020 - Ethnicity and government provision of drinking water, China
    "RE8EDE45DF049",  # Crawford & Bell 2012 - urban livelihoods and water infrastructure, Cusco Peru
    "RE57362A779FA",  # Pierce & Gmoser-Daskalakis 2021 - intra-city water system arrangements, California
    "RE54EF28A4406",  # Pezon 2017 - price-cap regulation, Burkina Faso
]

EXCLUDES = {
    "RE9FD407645E2": ("E05", "Ezeudu (2019), 'Urban sanitation in Nigeria: the past, current and future status of access, policies and institutions.' A literature review synthesising secondary sources (academic articles, agency reports, gray literature) rather than an original empirical study with primary data collection."),
    "RE8E407F925B3": ("E01", "Takeda & Putthividhya (2015), 'Perspectives on Dry-Season Water Allocation Characteristics and Resilience to Climate Change Impacts in the Chao-Phraya River Basin, Thailand.' Core focus is inter-sectoral (agriculture/municipal/environmental) irrigation-water allocation governance and climate-change resilience at river-basin scale, not a household/domestic legal-institutional water-access barrier mechanism."),
    "RE8CF1FD19CE7": ("E03", "Rowles et al. (2020), 'Seasonal contamination of well-water in flood-prone colonias and other unincorporated U.S. communities.' Core empirical analysis is water-quality chemistry/microbiology (arsenic and E. coli seasonal contamination testing); the informal/unincorporated legal status of colonias is background context, not the object of empirical analysis."),
    "RE5FCC85D5EF2": ("E06", "Ouellet-Plamondon, Davis, Watts & Savoie (2009), 'Audit, need analysis and design of vehicle washdown facilities for biosecurity in Queensland, Australia.' Pure engineering audit/design study for agricultural biosecurity vehicle-washdown infrastructure, no legal/institutional water-access-barrier mechanism analyzed."),
    "RE3EE606AB539": ("E06", "Asay (2007), 'Water suppliers and plumbers share backflow prevention responsibility.' Pure technical/engineering trade-journal article on backflow-prevention and cross-connection-control plumbing practice, not an empirical study of a legal/institutional water-access-barrier mechanism."),
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

print(f"Batch 156 recorded: {n_inc} includes, {n_exc} excludes.")
