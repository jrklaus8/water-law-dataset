#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RD4DC2325ECF4", "RD4C7B154BD46", "RD4A74FAB9801", "RD3F146BB7AEA", "RD3A71388F324", "RD0BCF1B1B012", "RCFBDF8C62619"]

EXCLUDES = {
    "RD506C8166A35": ("E01", "Chitonge (2014), 'Cities Beyond Networks: The Status of Water Services for the Urban Poor in African Cities.' A broad continent-level review/synthesis of water-infrastructure financing and investment-climate factors (private-investor risk aversion, donor funding trends, political sensitivity of tariffs) across many African cities, drawing on aggregate secondary statistics. Not a focused case study of a specific legal/institutional access-barrier mechanism with primary evidence."),
    "RD3A6C6EA4781": ("E01", "Capone (2013), 'The Assemblies of the City of Naples: A Long Battle to Defend the Landscape and Environment.' A narrative history of a Naples civic movement's fight against real-estate speculation and, primarily, the Campania toxic-waste-trafficking scandal and incinerator-subsidy lobbying. The 2011 water-privatization referendum is mentioned only once in passing as one item in a chronology; the substantive analysis throughout concerns solid-waste management, not a water-access legal/institutional mechanism."),
    "RD00CC5C728CA": ("E01", "Ballestero (2012), 'Transparency Short-Circuited: Laughter and Numbers in Costa Rican Water Politics.' Anthropological study of an NGO/aid-agency project's internal audit-indicator design process for a 'human right to water' initiative, focused on the role of laughter and numeric indicators as political devices in transparency-creation. Analytical object is NGO project audit culture/transparency theory, not a legal/institutional mechanism producing differential household water access."),
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

print(f"Batch 151 recorded: {n_inc} includes, {n_exc} excludes.")
