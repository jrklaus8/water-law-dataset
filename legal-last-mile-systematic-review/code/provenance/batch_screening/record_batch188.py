#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R6727B5865609",  # Nelson-Nunez, Walters & Charpentier - Chile rural water services, Law No. 20.998
    "R662825EA0EAA",  # O'Reilly & Dhanju - Rajasthan caste public taps/private connections
    "R6D53C0A6E3A4",  # Ennis-McMillan - Suffering from Water, Mexico
    "R61C9559AE0A2",  # Rammelt et al - Toxic injustice Bangladesh arsenic
    "R5DEA9225B1BF",  # De & Nag - Local self-governance, ethnic division, Kolkata slums
]

EXCLUDES = {
    "R653C938D77F9": ("E06", "Reddy & Batchelor (2012), 'Cost of providing sustainable water, sanitation and hygiene (WASH) services: an initial assessment of a life-cycle cost approach (LCCA) in rural Andhra Pradesh, India.' Financial-costing/budgeting methodology paper (life-cycle cost approach) for WASH service planning; a technical/financial planning-tool paper, not an institutional/legal-mechanism empirical study."),
    "R646F7032970F": ("E01", "O'Connell & Devine (2015), 'Who is likely to own a latrine in rural areas? Findings from formative research studies.' Behavior-change (SaniFOAM) framework study of social/behavioral determinants (norms, affordability perceptions, motivational drivers) of household latrine ownership across Tanzania, Indonesia, and India; behavioral/social-norm determinants study, not an institutional/legal access-mechanism study, consistent with the Kefeni & Yallew Addis Ababa exclusion precedent."),
    "R62C43D95536A": ("E05", "Ray & Shaw (2016), 'Water Stress in the Megacity of Kolkata, India, and Its Implications for Urban Resilience.' Desk-based application of an existing urban-water-resilience conceptual framework using secondary survey/census data (Asia Development Bank, Census of India); no original fieldwork, interviews, or primary data collection -- a conceptual/framework-application chapter."),
    "R61B13B02B733": ("E07", "Baruah (2010), 'Energy services for the urban poor: NGO participation in slum electrification in India.' Study of NGO-facilitated electricity/energy-service delivery to urban informal settlements in Ahmedabad, India; the service examined is electrification/energy, not water or sanitation."),
    "R6C5EA80EC864": ("E01", "Mitra & Pool (2000), 'Why women stay poor: An examination of urban poverty in India.' Broad gender/urban-poverty analysis examining education, health care, labour-force participation, and basic services (water, sanitation, drainage, roads) as one of three general components of urban poverty; water/sanitation is one of several minor topics in a broader gender-poverty study, not the dedicated focus."),
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

print(f"Batch 188 recorded: {n_inc} includes, {n_exc} excludes.")
