#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R7B052D90C3BF",  # Guidi Gutierrez, Gonzalez Gomez & Guardiola - Sucre Bolivia governance deficit
    "R7891B393A14B",  # Smith - Citizens' Voice in the Regulation of Water Services, South Africa
    "R756C4F77C0A7",  # Rama Mohan - Rural Water Supply in India, institutionalizing people's participation
    "R73872693EBDD",  # Hellberg - Water, life and politics: eThekwini municipality governmentality
    "R82B3655E82D0",  # Blase, Green & Matson - Public Water Supply Districts impacts, Missouri
    "R721DC414A085",  # de Carvalho, Costa, Marques & Netto - household connection to wastewater, Brazil RIA
]

EXCLUDES = {
    "R7B043D18F36C": ("E05", "Hirano (2016), 'Public participation in the global regulatory governance of water services: Global administrative law perspective on the Inspection Panel of the World Bank and amicus curiae in investment arbitration.' Doctrinal/conceptual legal analysis applying a global-administrative-law theoretical framework to World Bank Inspection Panel and investment-arbitration participation procedures; no case study, no household-level or connection-rate empirical data, and no original data collection -- a conceptual/theoretical legal-framework paper consistent with the established E05 precedent (Grimes UWAF)."),
    "R7A4DACA8AA5D": ("E01", "Lawanson & Fadare (2013), 'Neighbourhood differentials and environmental health interface in Lagos metropolis, Nigeria.' Comparative household survey (452 households, 3 neighborhoods) of general socioeconomic/environmental-health disparities; water access is one of several environmental-health indicators (alongside toilet type, waste disposal, drainage, cooking fuel, healthcare access) in a broader multi-indicator disparity study, not a dedicated institutional/legal water-access-mechanism study."),
    "R777E7407DCD6": ("E06", "Rowles, Whittaker, Ward, Araiza, Kirisits, Lawler & Saleh (2021), 'A Structural Equation Model to Decipher Relationships among Water, Sanitation, and Health in Colonias-Type Unincorporated Communities.' Structural equation modeling of household survey and water-quality microbial-testing data examining perceived vs. actual water quality and health outcomes in unincorporated Texas colonias; a technical/statistical water-quality-and-health measurement study, not an institutional/legal access-mechanism study."),
    "R73487CC7FF84": ("E06", "Fuller, Goldstick, Bartram & Eisenberg (2016), 'Tracking progress towards global drinking water and sanitation targets: A within and among country analysis.' Statistical/methodological paper comparing generalized additive models against linear regression for JMP global drinking-water/sanitation monitoring-trend estimation; a technical monitoring-methodology paper, not an empirical institutional/legal-mechanism study."),
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

print(f"Batch 185 recorded: {n_inc} includes, {n_exc} excludes.")
