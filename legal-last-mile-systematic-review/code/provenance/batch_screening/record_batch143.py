#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RFF4355ACB420", "RFE2A66422954", "RFDE0B63BD547", "RFD5FA6667229", "RFCCCFA44398C"]

EXCLUDES = {
    "RFFB5BFDE3838": ("E01", "Foucauldian discourse-analysis study of how open defecation is problematized by governments, NGOs and slum residents in Agra, India. Examines representations/discourse of 'shitting' as a problem, not a legal/institutional access-barrier mechanism or a household-level access/exclusion outcome. No tenure, eviction, eligibility, or documentation mechanism examined."),
    "RFF4355C792EF": ("E01", "Analysis of US-Mexico transboundary water allocation politics under the 1944 Water Treaty and NAFTA-era reforms. Real legal/treaty framework but operates entirely at the interstate/binational level (Rio Grande and Colorado River allocation between national governments); no household-level water-access or exclusion outcome examined."),
    "RFECF89F1B231": ("E05", "General international synthesis/opinion essay (1983) surveying community-participation models in water-supply programmes across Latin America, Africa and South Asia. No specific country's legal framework, no empirical case data, and no quantified access/exclusion outcome; a review/commentary piece rather than an empirical study."),
    "RFDB989AF82C5": ("E05", "Conceptual/philosophical paper distinguishing traditional, industrial and reflexive paradigms of water management in Iran (qanat irrigation, ethico-religious frameworks). No empirical case data, no legal/institutional access-barrier mechanism, and no household-level water-access outcome measured."),
}

WRONG_FILE = {
    "RFEBA9E5C7885": "Delivered PDF content does not match target record. DB target: 'Tourism and water' by Madeley, John (2012). Actual PDF content: Arcega-Cabrera, Leon-Aguirre et al. (2023), 'Use of Microbiological and Chemical Data to Evaluate the Effects of Tourism on Water Quality in Karstic Cenotes in Yucatan, Mexico', Bulletin of Environmental Contamination and Toxicology -- an entirely different, unrelated microbiology/water-quality study with different authors and no connection to the target citation. Flagging wrong_file_retrieved; not screened.",
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

print(f"Batch 143 recorded: {n_inc} includes, {n_exc} excludes, {n_wrong} wrong_file_retrieved flags.")
