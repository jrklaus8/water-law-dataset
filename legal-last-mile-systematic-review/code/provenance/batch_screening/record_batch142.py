#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["R2772B94F6E5E", "R2830B61ED4DE", "R24E80DAAD57D", "R29303CD53875", "R37FED9503C6D", "R198957B7D1CB"]

EXCLUDES = {
    "R2B628DEA4272": ("E07", "Study is about stormwater drainage/urban flooding infrastructure in Semarang (stagnant river, flood management); sanitation/drinking-water access are only incidental/contextual mentions, not the study's focus. Extends the Ley 2022-type / drainage-as-distinct-service-category precedent under E07 (wrong service): drainage/flood control is treated as a distinct service category from water supply or sanitation per INCLUSION_EXCLUSION.md scope-discipline guidance."),
    "RD54062398124": ("E01", "Technical/engineering longitudinal analysis of motorized borehole functionality (hours running per day) in Northern Kenya using remote sensors and a multilevel statistical model. 'Institutions' in the paper refers to organizational/coordination capacity-building (NDMA, county water ministries, NGOs) for drought management, not a legal/institutional access-barrier mechanism (no discretion, eligibility, documentation, disconnection, or tenure mechanism examined at the household level; no household-level water-access outcome). No legal/regulatory framework or court/statute discussed. Excluded under E01 (no legal/institutional mechanism tied to a household water-access outcome)."),
}

WRONG_FILE = {
    "R31E29BB9CFED": "Delivered PDF content does not match target record. DB target: 'WORLD BANK: India, World Bank launch series on India's water resources management' (2000). Actual PDF content: The Lancet Commission's 'Global health 2035: a world converging within a generation' (Jamison, Summers et al., Lancet 2013;382:1898-1955) -- an entirely unrelated global health investment report with no connection to India water resources. Flagging wrong_file_retrieved; not screened.",
    "R19FD5701BC0D": "Delivered PDF content does not match target record. DB target: 'Water, governance and human development variables in developing countries: multivariate...' (Dondeynaz, Celine, 2014). Actual PDF content: 'Determinants of Corporate Sustainability in the Malaysian Construction Industry' (Kwek Choon Ling et al., Journal of Management and Sustainability 13(1), 2023) -- an entirely unrelated paper on corporate sustainability in Malaysia's construction sector. Flagging wrong_file_retrieved; not screened.",
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

n_inc = n_exc = n_wrong = 0
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
    elif rid in WRONG_FILE:
        row["full_text_status"] = "wrong_file_retrieved"
        note = WRONG_FILE[rid]
        row["notes"] = (row["notes"] + " | " if row["notes"] else "") + f"[{TODAY}] wrong_file_retrieved: {note}"
        n_wrong += 1

atomic_write(SCREEN, fieldnames, rows)

with open(EXCLOG, newline="") as f:
    r = csv.DictReader(f)
    ex_fieldnames = r.fieldnames
    ex_rows = list(r)

# lookup title/authors/year for exclusion log
meta = {}
with open(SCREEN, newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        meta[row["record_id"]] = row

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

print(f"Batch 142 recorded: {n_inc} includes, {n_exc} excludes, {n_wrong} wrong_file_retrieved flags.")
