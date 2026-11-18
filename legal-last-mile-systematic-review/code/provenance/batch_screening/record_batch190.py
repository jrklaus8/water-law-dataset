#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R566E192D76F6",  # Narzetti & Marques - Isomorphic mimicry and the effectiveness of water-sector reforms in Brazil
    "R5597D1B7A139",  # Kachenje - Strengths/weaknesses of community-based water supply scheme, Dar es Salaam, Tanzania
    "R5088AD87DF7C",  # Rusca, Alda-Vidal & Kooy - Sanitation justice, Kawempe District, Kampala, Uganda
    "R5207E9C3B055",  # Nastar & Ramasar - Transition in South African water governance, power analysis, Johannesburg
    "R4DBC86E42AB3",  # Laurie & Crespo - Deconstructing the best case scenario, La Paz-El Alto water politics, Bolivia
]

EXCLUDES = {
    "R550AF41D1041": ("E06", "Walkinshaw, Hecht, Patel & Podrabsky (2019), 'Training High School Student Citizen Scientists to Document School Water Access: A Feasibility Study.' Feasibility study of a photo-evidence citizen-science protocol for measuring physical condition (wear, cleanliness, flow) of school drinking-water fountains; a data-collection methodology/measurement study with zero discussion of legal or institutional access mechanisms."),
    "R50095132981A": ("E12", "Parker, Kirkpatrick & Figueira-Theodorakopoulou (2008), 'Infrastructure regulation and poverty reduction in developing countries: A review of the evidence and a research agenda.' Self-described literature review of published evidence on infrastructure regulation and poverty across multiple sectors (water, electricity, telecoms, transport), concluding with a proposed future research agenda; a review/synthesis article, not water-specific primary empirical research."),
    "R4FB92115E802": ("E06", "Naghibi-Beidokhti & Lence (2005), 'Management Alternatives for River-Alluvial Groundwater Supply Systems.' Engineering/hydrogeology optimization study of manganese/iron removal and reliability-based withdrawal-treatment modeling for the Fredericton, New Brunswick groundwater supply; a technical water-treatment engineering study with no legal or institutional access-mechanism content."),
    "R4EE7C202AE99": ("E01", "Robinson, Angehr, Robinson, Petit, Petit & Brawn (2004), 'Distribution of Bird Diversity in a Vulnerable Neotropical Landscape.' Conservation-biology study of forest bird-species distribution in the Panama Canal corridor; mentions the forests' function as the canal's water supply only in passing, with zero content on household/institutional water access. Corpus-inclusion error analogous to prior batches' off-topic exclusions (e.g., Vivekanandan nanotechnology, Humphries wetland ecohydrology)."),
    "R4D7CD4E75E33": ("E04", "Vasquez (2013), 'An economic valuation of water connections under different approaches of service governance.' Hedonic-price analysis of stated rental values to estimate households' implicit willingness-to-pay for in-house/yard water connections under municipal, private and community-managed governance in Guatemala; the outcome measured is economic valuation/willingness-to-pay, not an actual access, connection, or reliability outcome. Wrong outcome, consistent with the Salman et al. (Jordan demand elasticity) precedent."),
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
        assert row["full_text_decision"] in ("", None), f"{rid} already decided"
        row["full_text_status"] = "included"
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["reviewer_1"] = "Claude"
        n_inc += 1
    elif rid in EXCLUDES:
        assert row["full_text_decision"] in ("", None), f"{rid} already decided"
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

print(f"Batch 190 recorded: {n_inc} includes, {n_exc} excludes.")
