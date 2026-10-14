#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RD78BE4E7A173", "RD6ACC482E5FD", "RD69D09F09A2C", "RD60E8645D88B", "RD57B43C5CE2C"]

EXCLUDES = {
    "RD888853DBB5B": ("E01", "Earle (2007), 'The role of governance in countering corruption: an African case study.' Legal-doctrinal case study of the Lesotho Highlands Water Project bribery prosecutions (jurisdiction, definition of bribery), a bulk transboundary water-transfer megaproject. Concerns anti-corruption legal doctrine in large-scale infrastructure financing/procurement, not a household/community last-mile legal-access-barrier mechanism."),
    "RD6CFBE19B1AC": ("E01", "Schwartz & McConnell (2009), 'Do crises help remedy regulatory failure? A comparative study of the Walkerton water and Jerusalem banquet hall disasters.' Comparative public-policy analysis of whether disaster crises catalyze regulatory reform, using the Walkerton E. coli drinking-water contamination and an unrelated Israeli structural-collapse disaster. Concerns general regulatory-failure/reform theory, not a legal/institutional mechanism producing differential household water access for the poor."),
    "RD6C57C9AE28E": ("E01", "Madon & Sahay (2002), 'An Information-Based Model of NGO Mediation for the Empowerment of Slum Dwellers in Bangalore.' Case study of an NGO's information/communication mediation model (audiotapes, newspapers, right-to-information advocacy) between slum dwellers and government. Water is one of several generic basic-amenity comparisons in a slum profile; the analytical object is an information/communication NGO-mediation model, not a water-specific legal-access mechanism."),
    "RD6B9F237B30D": ("E01", "Zwarteveen (1997), 'Water: From Basic Need to Commodity: A Discussion on Gender and Water Rights in the Context of Irrigation.' Conceptual/theoretical discussion of gendered water-rights allocation in irrigation systems (productive agricultural water use), not domestic/household water or sanitation access; matches established precedent excluding irrigation/agricultural-water-allocation papers as out of scope."),
    "RD673D5E33933": ("E01", "Quaghebeur, Masschelein & Nguyen (2004), 'Paradox of Participation: Giving or Taking Part?' Foucauldian governmentality critique of participatory methodology in a Vietnamese-Belgian water-management development project. Analytical object is the theory/politics of 'participation' itself, not a legal/institutional mechanism producing differential household water access."),
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

print(f"Batch 150 recorded: {n_inc} includes, {n_exc} excludes.")
