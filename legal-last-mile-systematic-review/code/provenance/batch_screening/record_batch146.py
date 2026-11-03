#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RED9BCBF3BA22", "RED145F94416F", "RED0408163645", "REBD3E8E26D01", "REB91A9D9447A"]

EXCLUDES = {
    "REE9E2CC218BA": ("E01", "Qualitative implementation-challenges study of Ethiopia's market-based sanitation (MBS) programme in Wolaita zone, examining demand/supply-side economic constraints and health-extension-worker workload. No specific legal/administrative access-barrier mechanism (eligibility, documentation, tenure) examined; 'legalization' references concern business/enterprise registration, not household access rights."),
    "REE56282C3DF9": ("E01", "Socio-technical transitions theory paper (multi-level perspective, Freeman & Perez innovation typology) using the historical shift from surface water to piped water in the Netherlands (1850-1930) as an illustrative case for technology-society co-evolution theory. Analytical focus is transitions theory, not a specific legal/institutional access-barrier mechanism or documented exclusion outcome."),
    "REDC07790866A": ("E01", "Survey-based study of farmer satisfaction with Community Water Project (CWP) irrigation systems on Mount Kenya, relating satisfaction to water quantity delivered. Concerns farmer perceptions of agricultural/household irrigation water quantity, not a legal/institutional access-barrier mechanism; wrong population/exposure per established precedent for agricultural water-economics and perception studies."),
    "RED78A982436F": ("E01", "Focus-group study of rural Australian seniors' attitudes toward water management policies and water price increases, framed through environmental gerontology. No specific legal/administrative access-barrier mechanism (statute, eligibility, disconnection) analyzed; outcome is subjective perception/identity, not a water-access/exclusion outcome."),
    "REC1AF8910410": ("E05", "Short opinion/synthesis essay (Peace Review) compiling third-party statistics and reports on women's global water burden. No original empirical research, case study, or specific legal-mechanism analysis; a commentary piece citing others' data rather than presenting new evidence."),
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

print(f"Batch 146 recorded: {n_inc} includes, {n_exc} excludes.")
