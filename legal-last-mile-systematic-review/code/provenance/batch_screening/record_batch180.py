#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RA6A6B0425E70",  # Nizkorodov - Southern California water PPP risk allocation
    "R9E1C92EFDCBB",  # Saleth & Sastry - Karnataka water/sanitation sector status/subsidy/reform
    "RA2C6963F84B8",  # Alzahrani - Three Essays on Water Economics (SDWA, BWNs, Source Water Protection Act)
    "R9ACCC3D2E6C2",  # Adams, Braune, Cobbing, Fourie & Riemann - South Africa 20yr groundwater/Water Act 1998
    "R999C3CB53A0C",  # Kundu - Urban Development Programmes in India: A Critique of JnNURM
    "R9926E6BB7498",  # Hazarika & Nitivattananon - Guwahati groundwater rights/land rights DPSIR
]

EXCLUDES = {
    "RA86C18416D33": ("E07", "O'Toole (1989), 'Goal Multiplicity in the Implementation Setting: Subtle Impacts and the Case of Wastewater Treatment Privatization.' Confirmed via full-text read to be a public-administration implementation-theory study (top-down/bottom-up synthesis) using EPA-funded municipal wastewater TREATMENT PLANT construction-grant privatization as its empirical case; concerns industrial/municipal treatment infrastructure financing policy, not household water/sanitation service access."),
    "R9D43BF928F12": ("E06", "Jimenez & Perez-Foguet (2011), 'The relationship between technology and functionality of rural water points: evidence from Tanzania.' Water Point Mapping technical analysis of functionality-decay curves by pump technology type (handpumps, gravity-fed, motorised); an engineering/technical durability study, not a legal/institutional access-mechanism study."),
    "R9D37CC49998B": ("E06", "Guragai, Takizawa, Hashimoto & Oguma (2017), 'Effects of inequality of supply hours on consumers' coping strategies and perceptions of intermittent water supply in Kathmandu Valley, Nepal.' Household survey and on-site water-quality testing examining intermittent-supply reliability, contamination levels and coping strategies; an engineering/water-quality reliability study, not a legal/institutional access-mechanism study."),
    "R9E388863E256": ("E01", "Salmoral, Zegarra, Vazquez-Rowe et al. (2020), 'Water-related challenges in nexus governance for sustainable development: Insights from the city of Arequipa, Peru.' Stakeholder-interview/workshop study of water-food-energy-land NEXUS governance and natural-resource competition (urban/agricultural/environmental); basin/resource-scale nexus governance distinct from household water-access institutional mechanisms, consistent with the established Kabogo WUA exclusion precedent."),
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

print(f"Batch 180 recorded: {n_inc} includes, {n_exc} excludes.")
