#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RC8422265D240",  # Von Schnitzler - Traveling Technologies, South Africa prepaid meters
    "RC819F87A16F8",  # Brown - Unequal burden: water privatisation and women's human rights in Tanzania
    "RC660CF868FA0",  # Marcos - Governing Urban Water in a Decentralized System, Zamboanga Peninsula, Philippines
    "RBEA8F34FFA53",  # Kornberg - Structural Origins of Territorial Stigma, Detroit DWSD
    "RBDD5DD14AEFB",  # Hasna - Street Hydrant Project in Chittagong Low-Income Settlement
]

EXCLUDES = {
    "RC7156CD65FA6": ("E06", "Mohanty & Rout (2020), 'Factors affecting operation and maintenance cost recovery of urban water supply: An evidence from an eastern Indian states.' A bootstrapped multiple-regression econometric study of utility operation-and-maintenance cost-recovery determinants (energy cost, connection mix, tariff revenue) across Odisha's Urban Local Bodies; a utility financial-sustainability/cost-efficiency study, not an empirical study of a legal/institutional mechanism's effect on household water access -- consistent with the established E06 utility-financial-performance exclusion precedent."),
    "RC6ED4CA9878A": ("E01", "Vintges, Hamad, Diab, Abuhamad & Jones (2026), 'Denying humanitarian aid in a war zone: The intersecting impacts of the war on Gaza on adolescent girls' and young women's health.' A mixed-methods study of the Israeli blockade/siege of Gaza and its intersecting health impacts on adolescent girls (menstrual health, maternal health, food, mobility, water/sanitation as one dimension among several); water denial here occurs as a wartime blockade/weapon-of-war context, not a legal/institutional administrative-access mechanism -- consistent with the established E01 armed-conflict/water-as-weapon exclusion precedent (Hagan & Kaiser Darfur)."),
    "RC3D24DCB83DC": ("E05", "Rondinelli (1991), 'Decentralizing Water Supply Services in Developing Countries: Factors Affecting the Success of Community Management.' A conceptual/policy-synthesis article identifying six generic success factors for community water management, drawing on secondary evaluations and examples from other researchers' work (Honduras, Jordan, Egypt) rather than the author's own original fieldwork or data collection -- consistent with the established E05 policy-synthesis-on-secondary-sources exclusion precedent (Munasinghe)."),
    "RC1A2A5291C94": ("E01", "Hope (2013), 'Implementing the Sector Wide Approach for Improved Aid and Development Effectiveness: Assessing the Swaziland Experience.' A stakeholder-interview-based assessment of aid-effectiveness Sector Wide Approach (SWAP) implementation across four priority sectors (agriculture, education, health, water and sanitation) in Swaziland; water and sanitation is one of four sectors examined, and the paper's water-specific finding is that the water SWAP 'has not been functioning' with minimal substantive water-specific content -- consistent with the established E01 precedent for water as one minor topic within a broader cross-sectoral institutional analysis."),
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
    elif rid == "RBEDB6556B711":
        # Undecided: delivered PDF is JSTOR boilerplate/terms-of-use text repeated many
        # times with no actual article content -- content-extraction failure on a
        # correctly-identified file (Olmstead 2004 precedent). Leave open/undecided.
        row["full_text_status"] = "undecided"
        row["notes"] = (row.get("notes") or "") + (
            " [2026-09-27] Retrieved via new_batch_pool.json (Antigravity delivery "
            "folder). Correct title/author match (Olmstead 2004, Land Economics, "
            "'Thirsty Colonias: Rate Regulation and the Provision of Water Service'), "
            "but the extracted PDF content is entirely JSTOR access-terms boilerplate "
            "repeated ~16 times with no actual article text (introduction, methods, "
            "results, discussion all absent). Content-extraction failure on a "
            "correctly-identified file, not a wrong_file_retrieved case. Left "
            "undecided/open pending a re-extraction attempt; not moved from inbox."
        )

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

print(f"Batch 176 recorded: {n_inc} includes, {n_exc} excludes, 1 undecided (RBEDB6556B711).")
