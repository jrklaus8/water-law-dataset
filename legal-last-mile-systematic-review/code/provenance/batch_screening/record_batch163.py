#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R49BC05123474",  # Whittington, Lauria & Mu - water vending WTP, Onitsha Nigeria
    "R3BE9653C9842",  # Nolan, Bloom & Subbaraman - legal status/deprivation, India slums
    "R2D16CA4C51A0",  # Alvez Marin - constitutional Indigenous water rights, Chile
    "R003523574784",  # Cook & Wei - rainwater harvesting government programme, China
    "R7B1FE35F1E88",  # Perumal - Mazibuko v City of Johannesburg feminist legal analysis
]

EXCLUDES = {
    "R457A96841C7E": ("E06", "Parkinson & Tayler (2003), 'Decentralized wastewater management in peri-urban areas in low-income countries.' A technical/policy review of decentralized wastewater treatment technology options and a proposed capacity-building framework, drawing on secondary case examples rather than original empirical data collection."),
    "R323554A8B2B1": ("E01", "Bah (1992), 'Community Participation and Rural Water Supply Development in Sierra Leone.' A case study of an NGO (Plan International) rural-development project's community self-help well-construction model and its failure/success factors; concerns NGO project design and community motivation, not a legal/institutional government water-access-barrier mechanism."),
    "R2EDB83537DF8": ("E01", "Frumkin (2005), 'Health, Equity, and the Built Environment' (guest editorial). A general environmental-justice/built-environment opinion editorial covering housing, transportation, food deserts, parks, and neighborhood disorder; contains no water/sanitation-access content and is not empirical research."),
    "R1360D12AADAC": ("E01", "Moller & Radloff (2010), 'Monitoring Perceptions of Social Progress and Pride of Place in a South African Community.' A broad quality-of-life/social-indicators household survey (n=1020) covering housing, electricity, employment, and civic pride, with water access as one minor descriptive indicator among many; not a dedicated legal/institutional water-access-mechanism study."),
    "R04002DCC0AAF": ("E05", "Bartlett (2003), 'Water, sanitation and urban children: the need to go beyond improved provision.' A literature-review synthesis of secondary research on child health effects of inadequate water/sanitation provision, no original empirical data collection or institutional/legal mechanism analysis."),
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

print(f"Batch 163 recorded: {n_inc} includes, {n_exc} excludes.")
