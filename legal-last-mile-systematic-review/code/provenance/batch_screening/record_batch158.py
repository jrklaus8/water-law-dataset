#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RDE1EDA735C46",  # Fuente & Bartram - pro-poor governance, GLAAS surveys
    "RDCFFEDDA5CAF",  # Swatuk & Kgomotso - Botswana Ngamiland government policy evaluation
    "RDC175D72AFE5",  # Beisheim et al - transnational PPPs, areas of limited statehood
    "RDB3CF0A8AAED",  # Vasquez - WTP/WTW municipal vs community-managed, Guatemala
    "RDAD1B5F3B10E",  # Hailu, Osorio & Tsukada - Bolivia privatization/renationalization
    "RD93C9D05E8F4",  # Bradlow - embeddedness and cohesion, Sao Paulo
    "RD864FBEE0D54",  # Britto, Maiello & Quintslr - Rio de Janeiro water supply
]

EXCLUDES = {
    "RDDEE18CE92AF": ("E01", "Guppy (2014), 'The Water Poverty Index in rural Cambodia and Viet Nam: A holistic snapshot to improve water management planning.' A composite-index methodology-validation study comparing the Water Poverty Index against conventional coverage measures, not an empirical study of a legal/institutional water-access-barrier mechanism -- matches established precedent excluding methodology-development/validation papers."),
    "RDAD34E024169": ("E05", "Lee (1995), 'Financing investments in water supply and sanitation.' A regional policy-analysis paper drawing on secondary published national statistics (ECLAC studies) to model tariff-based self-financing scenarios across Latin American countries, not an original empirical study with primary data collection -- matches the Nigam & Ghosh (1995) precedent."),
    "RD88D7BDC6553": ("E05", "Ako, Shimada, Eyong & Fantong (2010), 'Access to potable water and sanitation in Cameroon within the context of Millennium Development Goals (MDGs).' A descriptive MDG-progress-tracking synthesis of secondary national survey/government statistics, not an original empirical study of a specific legal/institutional water-access-barrier mechanism."),
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

print(f"Batch 158 recorded: {n_inc} includes, {n_exc} excludes.")
