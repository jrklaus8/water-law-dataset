#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R98EE7A8CD53B",  # Hossain - Dhaka bosti utility negotiation
    "R95641AC1C405",  # Baud & Dhanalakshmi - Chennai sewerage governance
    "R9499AFC94021",  # Dugard - South Africa urban basic services rights
    "R934020F5D9E0",  # Gopakumar - Bengaluru water PPP experiments
    "R8FA24A9DD2C8",  # Toure et al - Mbour Senegal water-poverty GIS
    "R984395E64462",  # Crane - Jakarta water market deregulation
]

EXCLUDES = {
    "R9DF6B20973C6": ("E01", "van Steenbergen (1995), 'The Frontier Problem in Incipient Groundwater Management Regimes in Balochistan (Pakistan).' Basin/resource-scale analysis of common-pool groundwater management-regime evolution (access-rights definition, overexploitation dynamics) for irrigated agriculture; basin-scale resource governance distinct from household water-access institutional mechanisms, consistent with the established Kabogo WUA / van Steenbergen-type exclusion precedent."),
    "R9D4038D0E695": ("E01", "Isunju, Orach & Kemp (2016), 'Community-level adaptation to minimize vulnerability and exploit opportunities in Kampala's wetlands.' Household survey (n=551) and focus groups on wetland-community adaptation to flood/disease hazards and livelihood benefits (crop farming, cheap rentals, free spring water); an environmental-vulnerability/livelihood-adaptation study in which water access is one minor benefit among several wetland-location benefits, not a dedicated water-access institutional-mechanism study."),
    "R996153B78E54": ("E06", "Rehan, Knight, Haas & Unger (2011), 'Application of system dynamics for developing financially self-sustaining management policies for water and wastewater systems.' System Dynamics causal-loop-diagram simulation/demonstration model for utility asset-management financial planning, Canada; a technical/financial-modeling methodology paper, not an empirical institutional/legal-mechanism study."),
}

# wrong_file_retrieved: R99433B75F8E9 ("Ecology in Public Health", Kiss 2005) -- delivered PDF
# is an unrelated 2025 PRRSV swine-virus One Health veterinary paper (Chen, Weng, Huang, Li & Duan).
# Flagged, not screened, not moved.
WRONG_FILE = {
    "R99433B75F8E9": (
        "Ecology in Public Health",
        "Kiss, Laszlo",
        "2005",
        "Chen, Weng, Huang, Li & Duan (2025), 'Integrated PRRSV prevention and control strategy "
        "based on the One Health concept: across the boundaries of virology, ecology and public "
        "health', Frontiers in Microbiology -- an entirely different, unrelated veterinary/swine-"
        "virology review with different authors and no connection to the target citation "
        "('Ecology in Public Health' by Kiss, 2005). Flagging wrong_file_retrieved; not screened; "
        "Drive file left in place, not moved to Processed."
    )
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

n_inc = n_exc = n_wf = 0
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
        target_title, target_authors, target_year, actual_desc = WRONG_FILE[rid]
        row["full_text_status"] = "wrong_file_retrieved"
        row["notes"] = (
            f"[{TODAY}] wrong_file_retrieved: Delivered PDF content does not match target record. "
            f"DB target: '{target_title}' by {target_authors} ({target_year}). "
            f"Actual PDF content: {actual_desc}"
        )
        n_wf += 1

assert n_inc == len(INCLUDES), f"expected {len(INCLUDES)} includes, matched {n_inc}"
assert n_exc == len(EXCLUDES), f"expected {len(EXCLUDES)} excludes, matched {n_exc}"
assert n_wf == len(WRONG_FILE), f"expected {len(WRONG_FILE)} wrong_file, matched {n_wf}"

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

print(f"Batch 181 recorded: {n_inc} includes, {n_exc} excludes, {n_wf} wrong_file_retrieved.")
