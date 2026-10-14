#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RE6E898E698B5",  # Kim - Malaysian Water Sector Reform: Policy and Performance
    "R82AEE5CC7ACC",  # Morvaridi - Management of Water Supply and Sanitation Projects, Maharashtra
    "R74AD122FBBD1",  # Hanchett, Akhter & Khan - WaterAid-Bangladesh Urban Programme
    "R3C8C664DF35D",  # Mumme & Ingram - Community Values in Southwest Water Management
]

EXCLUDES = {
    "REA41C1AC010A": ("E01", "Bradshaw & Schafer (2000), 'Urbanization and Development: The Emergence of International Nongovernmental Organizations Amid Declining States.' A cross-national quantitative regression study testing INGO density/strength's effect on overurbanization, economic growth, and aggregate access-to-safe-water rates; the exposure is civil-society/NGO organizational presence, not a documented legal/institutional water-access mechanism, and the analysis is at the country-aggregate level with no household-level access-barrier content."),
    "RDE97BBA1228E": ("E01", "Payne, Nakato & Nabalango (2008), 'Building Rain Water Tanks and Building Skills: A Case Study of a Women's Organization in Uganda.' An NGO skills-training/gender-empowerment case study of women trained as masons to construct household rainwater-harvesting tanks; concerns gender-based income/skills development and household technology adoption, not a documented legal/institutional water-access mechanism."),
    "RC4B9336131E4": ("E06", "Whittington, Briscoe, Mu & Barron (1990), 'Estimating the Willingness to Pay for Water Services in Developing Countries: A Case Study of the Use of Contingent Valuation Surveys in Southern Haiti.' A methodological validation study testing whether contingent-valuation survey techniques can reliably estimate household willingness-to-pay for water-tariff design purposes; a survey-methodology/economic-valuation study, not an empirical study of a legal/institutional access-barrier mechanism."),
    "RB39539FFABEC": ("E01", "Presbey (2015), 'Globalization and the Crisis in Detroit.' A broad political-economy analysis of Detroit's bankruptcy, emergency management, mortgage foreclosure and auto-industry globalization; the 2014 water shutoffs are one section within this much broader theoretical analysis, consistent with the established Safransky-Detroit precedent (water as one minor topic within a broader theoretical analysis, not a dedicated water-access institutional-mechanism study)."),
    "R5229ABCF8511": ("E05", "Loftus (2009), 'Rethinking Political Ecologies of Water.' A theoretical/conceptual review essay surveying political-ecology literature on water governance and power, drawing primarily on secondary sources and the author's prior published work; consistent with the established E05 theoretical-essay precedent (Bond water-commodification narratives; Castro water struggles Latin America), not an original empirical study of a specific legal/institutional water-access mechanism."),
}

WRONG_FILE = {
    "RE07A5B3A53CD": "Database record is 'Essays on Industrial Organization, Environmental and Health Economics' (Tojal Ramos dos Santos, Carolina, 2024, ProQuest dissertation). The delivered PDF is a completely different dissertation: 'Essais en economie industrielle et economie de la sante' by Lea Bignon (Toulouse School of Economics, defended 10 July 2025, advisor Pierre Dubois), covering three chapters on pharmaceutical/health-insurance industrial organization (Continuous Glucose Monitors and the insulin market; Medicare Part D drug-tier design; biologic-drug learning-by-doing) -- different author, different institution, different year, and no environmental/water content whatsoever despite the target title's 'Environmental' component. Not screened. Not moved from the inbox. Needs re-retrieval of the correct Tojal Ramos dos Santos dissertation.",
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
        row["full_text_status"] = "wrong_file_retrieved"
        row["notes"] = WRONG_FILE[rid]
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

print(f"Batch 173 recorded: {n_inc} includes, {n_exc} excludes, {n_wf} wrong_file_retrieved.")
