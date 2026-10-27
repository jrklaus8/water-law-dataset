#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RF6E3BA87A01A", "RF0E6FD6A757D", "REF5A05B72782"]

EXCLUDES = {
    "RF6A57AF91895": ("E01", "Community-Based Natural Resource Management (CBNRM) framework analysis of potable water's role in community development in North-west Cameroon, based on government-ministry interviews on institutional/policy frameworks. Focus is CBNRM's general contribution to community development rather than a specific legal/administrative access-barrier mechanism; no documented access-exclusion outcome tied to a named statute or regulatory instrument."),
    "RF633F3C10F83": ("E01", "Study of an NGO-piloted 'CBM-lite' community-based management scheme for rural handpump maintenance in Uganda, examining free-riding and peer sanctioning via community byelaws (informal local rules, not government legislation). No government legal/administrative access-barrier mechanism examined; outcome is O&M funding/collective-action behavior, not a legal-mechanism-driven access/exclusion outcome."),
    "RF3B7A5825AAD": ("E01", "Comparative institutional description of Finland's well-functioning municipal water/wastewater service system, citing the Water Services Act 2001 and Local Government Act 365/1995. Describes a largely successful institutional model without documenting an access-exclusion outcome or disparity for any population subgroup tied to the legal framework; rural cooperative reliance is presented as a normal functional alternative, not evidence of exclusion."),
    "RF39E37B1152B": ("E02", "Historical study of Ottoman/Saudi imperial technopolitics governing pilgrimage and potable-water infrastructure in the Hijaz (Mecca/Jeddah). Analysis operates at the level of imperial/state administration and religious-political authority over infrastructure, not household-level water access; no household-level access/exclusion outcome examined."),
    "RF349D3658F7A": ("E06", "Systems-thinking/causal-loop-diagram analysis of non-revenue water (NRW) management reform in Malaysia. Technical/engineering-systems methodology applied to utility operations (leak reduction, tariff-adjustment modeling); no legal/institutional access-barrier mechanism or household-level access-exclusion outcome examined."),
    "RF166266361BD": ("E01", "Qualitative study of drought impacts and local government policy responses among irrigation farmers in rural Victoria, Australia, focused on agricultural water allocation and water trading. Concerns agricultural/irrigation water rights and farm livelihoods, not household drinking-water/sanitation access; wrong population and exposure per established precedent for agricultural water-economics studies."),
    "REF058F229DA8": ("E06", "Engineering/operations case study of Maynilad Water Services' (Metro Manila) non-revenue-water reduction program: district metered areas, leak detection, pipe replacement, meter management. Purely technical/operational utility-management case study; no legal/institutional access-barrier mechanism analyzed beyond passing reference to the 1997 privatization concession structure."),
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

print(f"Batch 145 recorded: {n_inc} includes, {n_exc} excludes.")
