#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RCEA1E794B05B", "RCD415D6E7610", "RCC81F64B0502", "RCB895D9C44DB", "RCA8EBC5427E6"]

EXCLUDES = {
    "RCFB3EAA5343C": ("E01", "Boland (2007), 'The Trickle-down Effect: Ideology and the Development of Premium Water Networks in China's Cities.' Ideology/discourse analysis of affluent urban residents bypassing municipal tap water via privately-built 'premium networked spaces' (secondary purified-water pipe systems). The article's own stated finding is the 'noticeable absence of debate regarding the distributional outcomes' -- it does not empirically analyze impacts on the remaining public-system users or a legal/administrative access-barrier mechanism for the poor."),
    "RCFA80916BCB0": ("E01", "Nayak & Samal (2025), 'An Evaluation of Water Security in Coastal Urban Areas: A Comprehensive Case Study of Bhubaneswar, Odisha.' Constructs a composite Water Security Index (12 weighted indicators) from secondary agency data (PHEO, OWSSB, OSPCB reports). A descriptive index-construction/assessment exercise, not a study isolating a specific legal/institutional access-barrier mechanism with primary field evidence."),
    "RCF3A1AF89150": ("E05", "Douvitsa & Kassavetis (2014), 'Cooperatives: an alternative to water privatization in Greece.' A normative case-study/policy-proposal essay evaluating a water-cooperative alternative (Initiative 136) to the privatization of Thessaloniki's EYATH utility, based on literature review of cooperatives and privatization effects worldwide rather than original empirical data collection on Greek water access outcomes."),
    "RCE03521BFFE3": ("E01", "Barrington et al. (2016), 'Improving community health through marketing exchanges: A participatory action research study on water, sanitation, and hygiene in three Melanesian countries.' Applies a social/behavioural marketing-exchange theoretical framework to WASH behaviour-change interventions. Analytical object is marketing/behavioural-science theory, not a legal/institutional water-access-barrier mechanism."),
    "RCB664E1D2F9E": ("E01", "Zeitoun, Eid-Sabbagh & Loveless (2014), 'The analytical framework of water and armed conflict: a focus on the 2006 Summer War between Israel and Lebanon.' International Humanitarian Law analysis of armed-conflict damage to water infrastructure during wartime. Concerns law-of-war/IHL violations against infrastructure, not a legal/administrative last-mile access-barrier mechanism for the poor in ordinary governance conditions."),
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

print(f"Batch 152 recorded: {n_inc} includes, {n_exc} excludes.")
