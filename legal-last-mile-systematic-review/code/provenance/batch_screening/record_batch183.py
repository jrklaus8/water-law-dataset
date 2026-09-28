#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R8821F07922AB",  # Reynaud - PSP, regulation, social policies in water supply in France
    "R86051205DAED",  # Furlong - Good water governance without good urban governance?
    "R8F394022B0DC",  # Roncoli et al - Who counts, what counts (Burkina Faso)
    "R83CC2CDECA38",  # Zaato & Ohemeng - Building Resilient Organizations (Ghana Water Company)
    "R8132FFEC58AA",  # Vijay & Ghosh - Sabar Shouchagar Project
    "R8CC9DED5F88A",  # Roth - Constructing community health and safety
]

EXCLUDES = {
    "R87F24B4E11DF": ("E12", "Shah & Narain (2019), 'Re-framing India's water crisis: An institutions and entitlements perspective.' Self-labeled Geoforum 'Review' section piece synthesizing an institutions-and-entitlements conceptual argument entirely from secondary literature; no original empirical data collection of its own."),
    "R86E29439A5B6": ("E01", "Bazoglu (2011), 'Measuring and coping with urban growth in developing countries.' Book chapter analyzing UN-HABITAT Global City Sample urban-growth/governance typology across 52-119 cities; piped-water access is one of several infrastructure indicators (alongside sewer, electricity, telephones, mortality, literacy) in a broader multi-sector urban-governance analysis, not a dedicated water-access institutional-mechanism study."),
    "R860770E07485": ("E01", "Tapela (2002), 'The challenge of integration in the implementation of Zimbabwe's new water policy: case study of the catchment level institutions surrounding the Pungwe-Mutare water supply project.' Basin/catchment-scale water-resources allocation and governance study (Catchment Councils, Sub-Catchment Councils, interstate Joint Water Commission water-sharing arrangements); content is entirely about basin-level water-resource allocation institutions among farmers, mines, and municipalities, not household water/sanitation access outcomes, consistent with the van Steenbergen Balochistan basin-scale exclusion precedent."),
    "R81BEA2E1C8CE": ("E01", "Dinpanah & Lashgarara (2008), 'Designing an optimum model for protection and improvement of sustainability of natural resources and environment in Iran.' General agricultural/natural-resource and environmental-sustainability conceptual model paper; water is mentioned only as one of several natural resources (alongside soil, land), not the focus of the paper."),
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

print(f"Batch 183 recorded: {n_inc} includes, {n_exc} excludes.")
