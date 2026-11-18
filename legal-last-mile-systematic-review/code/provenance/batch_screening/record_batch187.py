#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R6B6565EFE1C9",  # Cobbing et al - O&M and perceived unreliability of domestic groundwater, South Africa
    "R75F551BE4748",  # Johnson et al - Racial Apartheid in a Small North Carolina Town
    "R6A459D59A92A",  # Bassi & Kabir - Sustainability Versus Local Management, rural water India
    "R69C019A0A542",  # Boex et al - Political Economy of Urban Governance in Asian Cities
    "R7189977C3E95",  # Tadadjeu et al - natural resource dependence and access to water/sanitation, Africa
    "R6F22E1AE923A",  # Kujinga et al - household water security, Ngamiland Botswana
]

EXCLUDES = {
    "R696ECAB36A20": ("E12", "Jaffee (2018), 'Enclosing Water: Privatization, Commodification, and Access.' Book chapter synthesizing existing literature on global water-privatization/commodification trends (Bakker, Castro, Goldman, Zwarteveen & Boelens, etc.); no mention of fieldwork, interviews, or original data collection -- a secondary literature-synthesis chapter, not an original empirical study."),
    "R68475B3785B2": ("E04", "Harutyunyan (2014), 'Metering drinking water in Armenia: The process and impacts.' Study of water-metering's effects on household water consumption/demand elasticity and tariff-structure transition; the outcome is water consumption/demand quantity, not connection/access, consistent with the Salman Jordan wrong-outcome precedent (this same segment)."),
    "R6C487F03F147": ("E06", "Pailla (2011), 'Integration of Capacity Factors Analysis Risk Methodology and Ostrom's Social Ecological System Assessment Framework to Assess and Improve Domestic Water Infrastructure in Nalgonda District, Andhra Pradesh, India.' Engineering/technical decision-support-tool paper (Louis-Ostrom Comprehensive Capacity Assessment, LOCCA) for selecting appropriate water-supply technology; institutional factors are one of eight technical capacity-assessment inputs, not the object of an institutional/legal-mechanism empirical study."),
    "R67B4818D18B5": ("E01", "Roy, Sowgat, Islam & Anjum (2020), 'Sustainability Challenges for Sprawling Dhaka.' Broad urban-sprawl sustainability study (land-cover change detection, field observation/interviews in 19 areas) examining housing, drainage, accessibility, and sanitation as several dimensions of urban-sprawl governance; water/sanitation mentioned only 24/4 times in a 61,000-character paper, a minor topic within a broader sprawl-sustainability study."),
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

print(f"Batch 187 recorded: {n_inc} includes, {n_exc} excludes.")
