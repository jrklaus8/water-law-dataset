#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R4818B7F566CE",  # Ponder & Omstedt - The violence of municipal debt, Detroit water crisis
    "R460B9BC74FA4",  # Danesi, Passarelli & Peruzzi - Water services reform in Italy (Galli Law)
    "R45FB2A780DA8",  # Kacker & Joshi - In the pipeline, governance of water supply to urban informal settlements, New Delhi
    "RA580E8237E5A",  # March & Sauri - The unintended consequences of ecological modernization, Barcelona water-cycle debt
]

EXCLUDES = {
    "R4CC41822C1CE": ("E12", "Ludwig (2000), book review of Marino & Boland (1999), 'An integrated approach to wastewater management, deciding where, when, and how much to invest', The World Bank. A 'Book reviews' section entry summarizing a 46-page World Bank policy brochure; not primary empirical research."),
    "R4B036EC5F939": ("E12", "Stoler (2017), 'From curiosity to commodity: a review of the evolution of sachet drinking water in West Africa.' Self-labeled WIREs Water 'Advanced Review' literature-synthesis article reviewing 2011-2016 sachet-water literature; not primary empirical research."),
    "RA40422CA051D": ("E01", "Taddei (2011), 'Watered-down democratization: modernization versus social participation in water management in Northeast Brazil.' Ethnographic study of basin-committee water-ALLOCATION meetings governing large reservoirs in the Jaguaribe Valley, Ceara, primarily allocating water among irrigation, municipal, and industrial users; a basin-scale water-resource-allocation governance study, not a household water-access study, consistent with the established Tapela/Mancilla Garcia precedent."),
    "R490B82E5ADFA": ("E06", "Xie, Li, Huang, Li & Chen (2011), 'An inexact chance-constrained programming model for water quality management in Binhai New Area of Tianjin, China.' Technical optimization-modeling study (interval linear programming/chance-constrained programming) for industrial wastewater-discharge and water-environmental-capacity planning; an engineering/operations-research methodology study with no legal/institutional access-mechanism content."),
    "RA3A338BE381A": ("E01", "Lockie, Momtaz & Taylor (1999), 'Meaning and the Construction of Social Impacts: Water infrastructure development in Australia's Gladstone/Calliope region.' Case study of the politics and methodology of Social Impact Assessment (SIA) around a proposed dam/bulk-water-supply infrastructure project for industrial/regional development; the object of study is SIA process legitimacy and social construction of impacts, not household water/sanitation access."),
    "RA592B6E9DD12": ("E01", "Kudebayeva (2010), 'Kazakhstan: Poverty And Social Exclusion In Rural Development.' Cross-sectional logit-regression study of general rural-poverty determinants (household composition, education, health, region) with water/sanitation infrastructure presence used as one of several household-amenity covariates predicting poverty status; wrong outcome direction and water is one of several indicators in a general poverty study, not an institutional/legal-mechanism study of water access."),
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
        assert row["full_text_decision"] in ("", None), f"{rid} already decided"
        row["full_text_status"] = "included"
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["reviewer_1"] = "Claude"
        n_inc += 1
    elif rid in EXCLUDES:
        assert row["full_text_decision"] in ("", None), f"{rid} already decided"
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

print(f"Batch 192 recorded: {n_inc} includes, {n_exc} excludes.")
