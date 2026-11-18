#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R916889165AD5",  # Aiga & Umenai - Impact of water supply improvement, Manila (ZIP legalization program)
    "R8EF694ACCE60",  # Post - Home Court Advantage, investor type/contract resilience, Argentina
    "R92E20B0729D7",  # Narsiah & Ahmed - Neoliberalization of Water and Energy Sectors, South Africa/India
    "R6EA0A0277A0E",  # Gomez, Perdiguero & Sanz - Socioeconomic factors affecting rural water access
]

EXCLUDES = {
    "R91DDD83ED473": ("E01", "Blanchard-Boehm, Earl, Wachter & Hanford (2008), 'Communicating future water needs to an at-risk population... Applewhite Dam and Reservoir Project, San Antonio, Texas.' A risk-communication case study of a defeated bulk-water-supply infrastructure referendum; concerns macro-scale regional water-resource planning and public communication, not household-level water-access-barrier mechanisms."),
    "R8F2B41CC1A57": ("E01", "Gonzalez-Gomez & Guardiola (2009), 'A Duration Model for the Estimation of the Contracting Out of Urban Water Management in Southern Spain.' A duration-model regression of 744 municipalities' decisions to contract out water management; examines determinants of a municipal privatization DECISION itself (complexity, economies of scale, financial restrictions, government stability), with no water-access, coverage, or connection outcome content whatsoever."),
    "R8E2E7578F722": ("E05", "Bond (2004), 'Water Commodification and Decommodification Narratives: Pricing and Policy Debates from Johannesburg to Kyoto to Cancun and Back.' An explicitly labeled polemical/theoretical Essay synthesizing global water-pricing policy debates via secondary sources; no original empirical data collection."),
    "R917E4BA2FDDC": ("E05", "Castro (2008), 'Water Struggles, Citizenship and Governance in Latin America.' A short 'Dialogue' opinion/commentary piece broadly synthesizing water-struggle literature across Latin America; no original empirical data collection or case-study methodology."),
    "R8F3A862DA6B1": ("E05", "Olutayo, Omobowale & Amzat (2009), 'Privatization and the Social Value of Water in Africa.' A policy-advocacy essay drawing entirely on secondary statistics and press/NGO sources (Public Citizen, SAMWU) to critique water privatization in South Africa and Ghana; no original empirical data collection or fieldwork methodology."),
    "R550D015C22B6": ("E01", "Adida & Girod (2011), 'Do migrants improve their hometowns? Remittances and access to public services in Mexico, 1995-2000.' A political-economy panel regression (2,438 municipalities) examining migrant remittances (a private household financial flow) as a substitute for government utility provision; the exposure is a private economic transfer, not a legal/institutional access mechanism."),
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

print(f"Batch 169 recorded: {n_inc} includes, {n_exc} excludes.")
