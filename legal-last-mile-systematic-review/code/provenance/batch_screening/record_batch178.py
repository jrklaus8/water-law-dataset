#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RAF4ED0F28A15",  # Kotsila & Saravanan - Biopolitics Gone to Shit? Mekong Delta Vietnam
    "RB1BD766758CF",  # Crow, Swallow & Asamba - Community Organized Household Water, Kenya
    "RB0D2ED9C835F",  # Whittington - Possible Adverse Effects of Increasing Block Water Tariffs
    "RB020C12A06CA",  # Monstadt & Schramm - Toward The Networked City, Dar es Salaam
    "RAD75F64031CA",  # Nyarko, Oduro-Kwarteng & Owusu-Antwi - Local authorities/PO partnerships, Ghana
    "RACB833F0F26E",  # Tiwale - Materiality matters, Lilongwe Malawi
]

EXCLUDES = {
    "RBFA34E702541": ("E01", "Van Vugt (2001), 'Community Identification Moderating the Impact of Financial Incentives in a Natural Social Dilemma: Water Conservation.' Social-psychology field/lab study of tariff-structure effects on household water CONSERVATION behavior in the UK; not a study of institutional/legal water-access mechanisms or access barriers."),
    "RB065139F8F17": ("E12", "Devkar, Mahalingam, Deep & Thillairajan (2013), 'Impact of Private Sector Participation on access and quality in provision of electricity, telecom and water services in developing countries.' Explicitly self-labeled 'A systematic review' in the abstract; secondary synthesis of existing studies across three infrastructure sectors, not original empirical research -- consistent with the established E12 secondary-review exclusion precedent."),
    "RAF8DEBF43A76": ("E06", "Arlosoroff et al. (1988), 'Executive Summary--Community Water Supply: The Handpump Option.' World Bank/UNDP engineering report on handpump technology selection, design criteria and maintenance logistics; purely technical/engineering content, not an institutional/legal access-mechanism study."),
    "RAED243630873": ("E01", "Nimoh, Poku, Ohene-Yankyera, Konradsen & Abaidoo (2014), 'Constraints and motivations to sanitation business in peri-urban communities in Ghana.' Case study of small-scale sanitation service providers' (masons, hardware suppliers, pit-emptiers) business profitability and constraints; supply-side business economics, not household sanitation-access barriers."),
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

print(f"Batch 178 recorded: {n_inc} includes, {n_exc} excludes.")
