#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RAE228938C27E",  # Mwihaki - Decentralisation as a tool in improving water governance in Kenya
    "RC373C4B7C2DE",  # Lenneiye - Testing Community Empowerment Strategies in Zimbabwe (water supply/sanitation programme)
    "R1CEF7787CF8F",  # Mbanaso - Urban service delivery system and federal government bureaucracy, Lagos Festac
    "R7FA19A7B8819",  # Silvestre, Marques, Dollery & Correia - Regional consortia and transaction costs for sanitation services, Brazil
    "RFFE28947EC31",  # Cleaver - Problems in the Planning of Rural Water Supply Projects, Nkayi District, Zimbabwe
    "RF2447F982F89",  # Ogle - Water supply, waste disposal, and the culture of privatism, mid-19th c. American city
    "REED4B1701A21",  # Prieto - Practicing costumbres and the decommodification of nature, Chilean water markets/Atacameno
]

EXCLUDES = {
    "R9FEFA8CF8F20": ("E06", "Penn, Loring & Schnabel (2017), 'Diagnosing water security in the rural North with an environmental security framework.' An ethnographic-synthesis diagnostic study applying a four-dimensional (availability/access/utility/stability) water-security framework to rural Alaska; the substantive analysis centers on infrastructure engineering suitability for Arctic conditions, energy/operating costs, and water-Utility operational capacity, not a documented legal/institutional access-mechanism causally analyzed -- consistent with the established E06 engineering/infrastructure-focused exclusion precedent (Berg & Mugisha; Heath/Parker/Weatherhead)."),
    "R2587238E5574": ("E03", "Marara, Palamuleni & Ebenso (2011), 'Access to Potable Drinking Water in the Wonderfonteinspruit Catchment.' A survey study whose central focus and contribution (suitability index, municipal-effectiveness index) concerns water-QUALITY/contamination risk from acid-mine-drainage radionuclide pollution and community perceptions thereof, with settlement-type water-source-access data used as secondary context rather than a documented legal/institutional access mechanism being isolated -- consistent with the established E03 water-quality/contamination-focus exclusion precedent (Peres et al. fluoridation; Driedger et al. Walkerton)."),
    "RFBB1B55A8D79": ("E05", "Huby (2001), 'The Sustainable Use of Resources on a Global Scale.' A theoretical/policy-comparative essay on reconciling social-welfare and environmental-sustainability goals for domestic water and energy, drawing entirely on secondary cross-national statistics (World Bank tables); no original empirical data collection or analysis of a specific documented legal/institutional water-access mechanism -- consistent with the established E05 theoretical-essay/secondary-source-synthesis exclusion precedent (Olutayo et al.; Pawar)."),
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

print(f"Batch 172 recorded: {n_inc} includes, {n_exc} excludes.")
