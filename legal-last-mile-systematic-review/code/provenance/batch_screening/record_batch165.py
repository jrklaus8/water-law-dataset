#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R812C5CF68631",  # Silva - Connectivity of Infrastructure Networks, Sao Paulo
    "R7FB3A3D76F81",  # Madrigal, Alpizar & Schluter - Community-Based Drinking Water Organizations, Costa Rica
    "R8277D5F60CD4",  # O'Reilly & Dhanju - Hybrid drinking water governance, Rajasthan
    "R850039CA750A",  # Aladuwaka & Momsen - Wanaraniya Water Project, Sri Lanka
]

EXCLUDES = {
    "R81F51DA7DB8A": ("E01", "Hasanov (2009), 'Social Capital, Civic Engagement and the Performance of Local Self-Government in Azerbaijan.' A broad social-capital/civic-engagement survey covering multiple municipal infrastructure categories (roads, parks, garbage collection, water supply, sewerage); water supply is one minor category among several, not a dedicated water-access institutional-mechanism study."),
    "R8044EE45423C": ("E01", "Rao & Purkayastha (2003), 'Common Property Resource Management: The Case of Chatla in Assam.' A common-property-resource-theory case study of fisheries management in a wetland; concerns fishing-rights institutions, not household drinking-water access."),
    "R80EFC63E1487": ("E01", "Karim, Emmelin, Resurreccion & Wamala (2012), 'Water Development Projects and Marital Violence: Experiences From Rural Bangladesh.' A study of a groundwater irrigation development project's gendered social/health consequences (domestic-water-shortage-linked marital violence); the studied outcome is intimate-partner violence, not a water-access-barrier mechanism or outcome."),
    "R838190F90528": ("E01", "Abers & Keck (2006), 'Muddy Waters: The Political Construction of Deliberative River Basin Governance in Brazil.' A political-institutional analysis of river-basin water-RESOURCE governance reform legislation (water pricing, federalism, executive-legislative relations) in Sao Paulo state and nationally; concerns basin-level water-resource management politics, not household water-access-barrier mechanisms."),
    "R54E45DD5DD8B": ("E01", "Earl & Czerniak (1996), 'Sunbelt Water War: The El Paso-New Mexico Water Conflict.' A legal/institutional analysis of an interstate bulk-water-supply conflict (federal reclamation law vs. New Mexico state law, commerce clause) resolved via a city-level water-source diversification strategy; concerns wholesale interstate water-rights allocation, not household-level water-access exclusion."),
    "RD8DF9CD532A4": ("E01", "Bartram et al. (2014), 'Global Monitoring of Water Supply and Sanitation: History, Methods and Future Challenges.' A methodology review of the WHO/UNICEF Joint Monitoring Programme's statistical methods (household-survey data, linear regression trend modeling); a monitoring-methodology review paper, not an empirical study of a specific legal/institutional water-access-barrier mechanism."),
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

print(f"Batch 165 recorded: {n_inc} includes, {n_exc} excludes.")
