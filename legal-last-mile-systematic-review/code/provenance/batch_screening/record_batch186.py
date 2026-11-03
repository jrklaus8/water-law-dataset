#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R706085F2592E",  # Bontianti, Hungerford, Younsa & Noma - Niamey Niger fluid experiences
    "R700E3084D85D",  # Pierce & Gonzalez - California mobile home parks water access
    "R6DB58AA8E6EA",  # Muchadenyika - Harare Zimbabwe slum upgrading inclusive governance
    "R6C0CBAFA3F7A",  # Gutierrez - Malawi/Zambia pro-poor water/sanitation delivery
    "R6B7F134E71E2",  # Lele et al - south Indian small towns institutional water governance
]

EXCLUDES = {
    "R6F950F094963": ("E06", "Liu, Brown, Demargne & Seo (2011), 'A wavelet-based approach to assessing timing errors in hydrologic predictions.' Pure hydrologic-forecasting engineering/statistical methodology paper (cross wavelet transform technique for streamflow prediction evaluation); no institutional/legal content whatsoever."),
    "R7DF428757F6D": ("E01", "Mancilla Garcia & Bodin (2019), 'Participatory Water Basin Councils in Peru and Brazil: Expert discourses as means and barriers to inclusion.' Qualitative study (116 interviews) of participatory-forum inclusion/exclusion dynamics in basin-scale water-RESOURCE-management councils (irrigation/industrial allocation); zero mentions of household, drinking water, or domestic water access -- basin-scale resource-governance study, consistent with the established Tapela/Roncoli basin-scale exclusion precedent, this same segment."),
    "R7DC5A97E31CC": ("E05", "Thompson (2016), 'Intersectionality and water: how social relations intersect with ecological difference.' Feminist-geography conceptual/theoretical framework paper elaborating an intersectionality-theory framework for eco-social water relations, using secondary-literature case studies from Sudan and Bangladesh as illustrative examples rather than original empirical data collection of its own."),
    "R6CA3DF70B3CE": ("E12", "Batley (2006), 'Guest editor's preface. Symposium on non-state provision of basic services.' This is an editorial preface introducing a five-article journal symposium, not itself a primary empirical study -- summarizes but does not report original findings."),
    "R779433B8EBD3": ("E04", "Crocker, Shields, Venkataramanan, Saywell & Bartram (2016), 'Building capacity for water, sanitation, and hygiene programming: Training evaluation theory applied to CLTS management training in Kenya.' Training-evaluation study measuring trainees' learning, individual performance, and organizational-programming outcomes from a 7-month CLTS management training program for government officials; outcome is training/capacity-building program effectiveness, not household water/sanitation access."),
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

print(f"Batch 186 recorded: {n_inc} includes, {n_exc} excludes.")
