import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

INCLUDES = {
    "R110426752017": "Legal-geography case study examining two companion 1971-1976 legal cases (Jimenez v. Hidalgo WCID 2 et al.; Fonseca v. Hidalgo WCID 2 et al.) documenting farmer-controlled water control and improvement districts' territorial exclusion of colonias from district boundaries, denying colonias residents the right to vote for WCID board candidates and thus the political standing to redirect district operations from irrigation to domestic water supply. Documents real population-level access-deficiency data (238,000 people in 1,350+ south Texas colonias, 119,000 facing water/sanitation deficiencies; specific 1971 exclusion of 39 subdivisions/2,950 lots, 11 tracts totaling 325 houses without domestic water service). Extracted as S658.",
}

EXCLUDES = {
    "RFF03643FADFA": {
        "title": "Hydrodynamic-ecological model analyses of the water quality of Lake Manzala nile delta, northern Egypt",
        "authors": "Rasmussen E.K.; Svenstrup Petersen O.; Thompson J.R.; Flower R.J.; Ahmed M.H.",
        "year": "2009",
        "code": "E01",
        "detail": "Hydrodynamic-ecological modeling study of nutrient loading/eutrophication in an Egyptian coastal lake; no legal/institutional factor examined and no household-level water/sanitation access data -- environmental/ecological hydrology, wrong topic.",
    },
    "R48AC741E5758": {
        "title": "How can inequalities in the oral health of Australian Aboriginal people be addressed?",
        "authors": "Green J.; Blinkhorn A.",
        "year": "2010",
        "code": "E01",
        "detail": "Discussion paper on Aboriginal oral/dental health disparities; water fluoridation appears only as one input/health-intervention mechanism for dental-caries outcomes, not as a water/sanitation service-access outcome, and the paper is a non-empirical discussion piece synthesizing secondary statistics rather than original data collection -- wrong topic.",
    },
}

ALL_IDS = set(INCLUDES) | set(EXCLUDES)

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

found = {r["record_id"]: r for r in rows if r["record_id"] in ALL_IDS}
missing = ALL_IDS - set(found)
assert not missing, f"Missing record_ids: {missing}"

for rid, r in found.items():
    assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided: {r}"

for rid in INCLUDES:
    r = found[rid]
    r["full_text_decision"] = "include"
    r["final_decision"] = "include"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["notes"] = INCLUDES[rid]

for rid, info in EXCLUDES.items():
    r = found[rid]
    r["full_text_decision"] = "exclude"
    r["final_decision"] = "exclude"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["exclusion_reason"] = info["code"]
    r["exclusion_reason_detail"] = info["detail"]

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"Updated {len(found)} records in full_text_screening_database.csv")

with open(EXCLOG, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    exc_fieldnames = reader.fieldnames
    exc_rows = list(reader)

for rid, info in EXCLUDES.items():
    exc_rows.append({
        "record_id": rid,
        "title": info["title"],
        "authors": info["authors"],
        "year": info["year"],
        "stage": "full_text",
        "exclusion_code": info["code"],
        "exclusion_reason_detail": info["detail"],
        "reviewer": REVIEWER,
        "date": DATE,
    })

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EXCLOG))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=exc_fieldnames)
    writer.writeheader()
    writer.writerows(exc_rows)
os.replace(tmppath, EXCLOG)
print(f"Appended {len(EXCLUDES)} rows to exclusion_log.csv. New total: {len(exc_rows)}")
