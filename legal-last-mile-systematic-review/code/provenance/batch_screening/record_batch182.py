#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R8DF8439BABC3",  # Martinez-Espineira, Garcia-Valinas & Gonzalez-Gomez - Spanish water pricing inequality
    "R8C6C4D410F39",  # Peal, Evans, Blackett, Hawkins & Heymans - FSM comparative analysis 12 cities
    "R9502CE771F1E",  # Barde - What Determines Access to Piped Water in Rural Areas, Brazil
    "R94E2C2B0C8C2",  # Biddle & Baehler - Breaking bad, polycentricity NYC vs Flint
    "R88AA43E1DE4C",  # Rachwal - 30 Years UK water sector, Thames Water privatisation
]

EXCLUDES = {
    "R8B31849A5CDA": ("E06", "Wride, Chen & Johnstone (2004), 'Characterizing the Spatial Variability of Rainfall Across a Large Metropolitan Area.' Hydrological/engineering rainfall-measurement-methodology study for sewer-system model calibration, Cincinnati; a purely technical study, not an institutional/legal water-access mechanism."),
    "R8A914A23E59B": ("E01", "Humphries, Kindness, Ellery, Hughes, Bond & Barnes (2011), 'Vegetation influences on groundwater salinity and chemical heterogeneity in a freshwater, recharge floodplain wetland, South Africa.' Pure ecohydrology/geochemistry study of tree-groundwater interactions in a wetland ecosystem; zero human water-access content, a corpus-inclusion error."),
    "R8A823907105A": ("E05", "Grimes (2012), 'Integrating human rights into water governance.' A conceptual framework paper proposing a Unified Water Assessment Framework (UWAF) integrating human-rights and water-governance concepts, with a brief desk-based illustrative application to South Africa's known constitutional/legislative reforms rather than original empirical data collection; a conceptual/framework-development paper, consistent with the established E05 exclusion precedent."),
    "R89AB91CFAF11": ("E12", "Obani (2017), 'Inclusiveness in humanitarian action -- access to water, sanitation & hygiene in focus.' Confirmed via full-text read to be explicitly self-described as 'This review of the scholarly literature,' with a stated database search methodology (Science Direct, Scopus, Google Scholar) synthesizing prior published legal/policy literature on WASH in humanitarian crises; a secondary literature review, not original empirical research."),
    "R89525A02FCDE": ("E06", "Harvey (2007), 'Cost determination and sustainable financing for rural water services in sub-Saharan Africa.' Presents a systematic cost-calculation/tariff-hierarchy planning tool and methodology for rural water utility financing; a technical/financial-planning methodology paper, not an empirical institutional/legal-mechanism study."),
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

assert n_inc == len(INCLUDES), f"expected {len(INCLUDES)} includes, matched {n_inc}"
assert n_exc == len(EXCLUDES), f"expected {len(EXCLUDES)} excludes, matched {n_exc}"

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

print(f"Batch 182 recorded: {n_inc} includes, {n_exc} excludes.")
