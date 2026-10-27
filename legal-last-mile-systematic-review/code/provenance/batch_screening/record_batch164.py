#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R7D0B0BE35E0D",  # Anand - PoliTechnics of Water Supply, Mumbai
    "R7ECF02CF6B42",  # Schnegg & Kiaka - economic value of water, Namibia CBM
    "R7FBDF527DD60",  # dos Santos et al - WatSan inclusive development policies, Brazil
    "R7F994C395052",  # Wutich et al - cross-cultural justice in water institutions
]

EXCLUDES = {
    "R7952A5F79DF3": ("E05", "Basnet, book review of Cahill-Ripley, 'The Human Right to Water and Its Application in the Occupied Palestinian Territories' (Asian Journal of International Law). A book review, not original empirical research or legal analysis by the document's own author."),
    "R7A71F4BE9DFF": ("E01", "Ferreyra, de Loe & Kreutzwiser (2008), 'Imagined communities, contested watersheds: Challenges to integrated water resources management in agricultural areas.' A policy-network governance study of agricultural water-QUALITY protection and watershed-based collaborative governance in Ontario, Canada, concerning drinking-water-source contamination protection, not household water-access barriers."),
    "R7C907BED6D11": ("E05", "Fontana & Elson (2014), 'Public policies on water provision and early childhood education and care (ECEC): do they reduce and redistribute unpaid work?' A policy-advocacy synthesis drawing on secondary statistics (UNICEF/WHO, existing time-use studies) to argue for public investment in water/ECEC; no original empirical data collection."),
    "R7F3951051E8D": ("E01", "Hecker, Watzold & Markwardt (2020), 'Spotlight on Spatial Spillovers: An Econometric Analysis of Wastewater Treatment in Mexican Municipalities.' A spatial-econometrics study of policy-diffusion/spillover effects in municipal wastewater-treatment-facility adoption between neighboring Mexican municipalities; concerns environmental-policy adoption patterns, not household water/sanitation-access-barrier mechanisms."),
    "R7E8BD25A85A4": ("E01", "Young & Keil (2005), 'Urinetown or Morainetown? Debates on the Reregulation of the Urban Water Regime in Toronto.' A political-ecology analysis of Toronto's water-privatization debate, urban sprawl, and watershed/moraine conservation politics; concerns municipal water-governance political economy and environmental protection, not household water-access-barrier mechanisms."),
    "R7D58C754450F": ("E05", "Book review of Shannon & De Meulder (eds.), 'Water Urbanisms 2 - East' (Urban Studies). A book review of a design/architecture volume on water-urbanism projects across Asia, not original empirical research."),
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

print(f"Batch 164 recorded: {n_inc} includes, {n_exc} excludes.")
