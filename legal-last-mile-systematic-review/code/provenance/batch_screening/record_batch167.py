#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R85E320C718A8",  # Derman - Cultures of Development and Indigenous Knowledge, Zimbabwe water reform
    "R8609FE411A88",  # Odeku & Konanani - Poor Water Service Delivery, Phiri/Mazibuko case analysis, South Africa
    "R513E53E45833",  # Grant - Urban and Suburban Nashville, metropolitan water-district fragmentation
    "R899DB35753C8",  # Addai & Pokimica - Trust and Material Hardship in Ghana, institutional trust/water deprivation
]

EXCLUDES = {
    "R87C35161C630": ("E01", "Safransky (2014), 'Greening the urban frontier: Race, property, and resettlement in Detroit.' Analyzes settler-colonial/racial dimensions of Detroit's green-infrastructure/austerity planning; water is mentioned only in passing as one of several public services (water, streetlights, transportation, garbage) facing withdrawal, with no dedicated institutional/legal water-access-mechanism analysis."),
    "R87FBB9180C15": ("E05", "Punjabi (2016), 'Debate on Karen Bakker's Privatizing Water.' An IJURR 'Author Meets the Critics' debate/book-review forum compiling four scholars' commentaries on Bakker's book with no original empirical data collection, matching the established book-review exclusion precedent."),
    "R77749A581F7E": ("E05", "Dukhovny & Ziganshina (2011), 'Ways to improve water governance.' A normative/advocacy policy essay on global and transboundary water governance (IWRM, 'hydro-solidarity') with no empirical data collection, household-level content, or case-study methodology."),
    "R87654C2FD7AA": ("E06", "Heath, Parker & Weatherhead (2012), 'Testing a rapid climate change adaptation assessment for water and sanitation providers in informal settlements in three cities in sub-Saharan Africa.' A technical climate-adaptation assessment methodology for water/sanitation infrastructure providers; an engineering/technical methodology-testing study, not an institutional/legal-mechanism analysis."),
    "R87132C51E802": ("E01", "Gonzalez Rivas (2014), 'Ethnolinguistic Divisions and Access to Clean Water in Mexico.' A political-economy regression study of ethnic fragmentation and indigenous/non-indigenous water-access disparities at the municipal and individual level; examines demographic/ethnic-fragmentation correlates of public-goods provision without identifying or testing any specific legal/institutional access mechanism (no tenure, documentation, eligibility rule, or formal-recognition barrier)."),
    "R889D34F0A0C2": ("E01", "Nyong & Kanaroglou (1999), 'Domestic Water Use in Rural Semiarid Africa: A Case Study of Katarko Village in Northeastern Nigeria.' A hydrological/behavioral household-survey study of water-collection and use patterns in a village relying entirely on natural water sources (rainfall, wells, streams) with no formal water utility, service provider, or legal/institutional access framework at all."),
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

print(f"Batch 167 recorded: {n_inc} includes, {n_exc} excludes.")
