#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R5AE001CE6E9E",  # Mwendera - Rural water supply and sanitation (RWSS) coverage in Swaziland
    "R58857C935BCF",  # Monney, Baffoe-Kyeremeh & Amissah-Reynolds - Accelerating rural sanitation coverage, Ghana
    "R582D32CAA4B0",  # Tantoh & McKay - community-based water management and governance, North-West Cameroon
    "R6A629E95E47B",  # Rydhagen - Feminist Sanitary Engineering in Vioolsdrif, South Africa
    "R57B19F9E60B7",  # Carrera & Flowers - Sanitation Inequity, Lowndes County Alabama
    "R567A3B014963",  # Hossain - informal practice of appropriation and social control, Dhaka bosti
]

EXCLUDES = {
    "R5BE691E02C84": ("E12", "Beck (2018), 'Water operator partnerships: Peer learning and the politics of solidarity in water and sanitation service provision.' Self-labeled 'ADVANCED REVIEW' in WIREs Water reviewing existing literature on Water Operator Partnerships (WOPs); a literature-synthesis review article, not original empirical research."),
    "R58D1D52A0625": ("E06", "Arvai & Post (2012), 'Risk Management in a Developing Country Context: Improving Decisions About Point-of-Use Water Treatment Among the Rural Poor in Africa.' Structured decision-making/deliberative risk-management framework study for household point-of-use water-treatment technology choice in two Tanzanian villages; a technical/behavioral decision-science study of technology adoption, not an institutional/legal access-mechanism study."),
    "R5691BDC5804B": ("E06", "Park & Visvanathan (2018), 'Technology development trajectory for drinking water treatment: a comparative study between South Korea, Thailand, and Lao PDR.' Comparative engineering study of drinking-water treatment technology adoption trajectories; zero mentions of legal or institutional access mechanisms, focused on technical treatment-technology development."),
}

WRONG_FILE = {
    "R57A89A8AFC15": ("Framework for action", "Rey J.", "2003", "Rey (2003), 'Framework for action' (DOI 10.1016/s1366-7017(01)00018-6). The delivered PDF is an entirely unrelated set of 2026 BJPsych Open conference abstracts on mental health services in Wales (maternity mental health beds, physical-activity interventions for mental health service users, parent-mediated autism intervention) -- wrong publication, wrong year, wrong topic entirely."),
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
    elif rid in WRONG_FILE:
        target_title, target_authors, target_year, actual_desc = WRONG_FILE[rid]
        row["full_text_status"] = "wrong_file_retrieved"
        row["notes"] = (row.get("notes") or "") + f" [{TODAY}] wrong_file_retrieved: DB target is \"{target_title}\" by {target_authors} ({target_year}); {actual_desc}"
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

print(f"Batch 189 recorded: {n_inc} includes, {n_exc} excludes, {n_wf} wrong_file_retrieved.")
