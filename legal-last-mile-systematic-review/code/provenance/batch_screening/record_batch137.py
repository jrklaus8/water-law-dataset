import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}
for rid in ("R0D499B7D1D12", "RDCEF86AF76DC", "RA1695DE0E546", "R5807B67AFA98"):
    assert by_id[rid]["full_text_decision"] == "", f"{rid} not open"
    assert by_id[rid]["final_decision"] == "", f"{rid} not open"

# R0D499B7D1D12 - Singh 2006 "Women, Society and Water Technologies" - INCLUDE
r = by_id["R0D499B7D1D12"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"
r["notes"] = ("Ethnographic institutional case study (162 women, 149 men, 12 FGDs, case studies across "
              "villages in Madhya Pradesh, Bihar, Jharkhand, West Bengal, India) documenting India's real "
              "statutory Accelerated Rural Water Supply Program (ARWSP, National Water Policy 1987/2002) "
              "with formal 40-lpcd/250-person coverage criteria and PRI 33%-reserved-seat site-selection "
              "process, showing bureaucratic site-selection failure: only 9 of 46 handpumps installed under "
              "the program were actually located within SC/ST localities despite formal coverage criteria, "
              "reproducing caste-based access exclusion. Included per INCLUSION_EXCLUSION.md criteria 1-9. "
              "Extracted as S681.")

# RDCEF86AF76DC - Singh 2006 "Women's Participation in Local Water Governance" - INCLUDE
r = by_id["RDCEF86AF76DC"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"
r["notes"] = ("Ethnographic institutional case study (fieldwork 2002-2004, 12 villages in Madhya Pradesh, "
              "15 villages in West Bengal, India) documenting India's real Panchayati Raj Institution (PRI) "
              "statutory framework (73rd Constitutional Amendment 1993) and Village Water and Sanitation "
              "Committee/Water and Child Welfare and Health Committee participation structures with 33% "
              "reserved seats for women, showing how caste-based social heterogeneity undermines the "
              "formal participatory institution's intended equitable water-access outcomes via two detailed "
              "case studies of hand-pump siting denying access to SC/Jatav women despite formal "
              "representation. Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S682.")

# RA1695DE0E546 - Avila Garcia 2006 "Water, society and environment - Morelia" - INCLUDE
r = by_id["RA1695DE0E546"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"
r["notes"] = ("Historical-documentary institutional case study of Morelia, Mexico spanning four centuries "
              "(Colonial, Porfiriato, post-revolutionary, and modern periods), documenting real legal/"
              "institutional frameworks governing water access: colonial-era Crown-issued water concessions "
              "(mercedes) restricting access to elite groups and excluding Indians/mestizos/blacks under "
              "penalty of whipping/fines; post-revolutionary State water nationalization and juridical-"
              "institutional reform; 1990s water-legislation changes; with quantified modern-era access "
              "outcomes (89% household connection rate by 2000, unequal distribution 300 lpcd in wealthy "
              "vs. under 100 lpcd in poor neighborhoods, 21% of 230 neighborhoods reliant on irregular "
              "tanker-truck service). Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S683.")

# R5807B67AFA98 - Agnihotri 2008 - EXCLUDE E04
r = by_id["R5807B67AFA98"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "exclude"
r["final_decision"] = "exclude"
r["exclusion_reason"] = "E04"
r["exclusion_reason_detail"] = ("Empirical study of land acquisition and resettlement/rehabilitation (R&R) "
                                  "policy for a large irrigation project (Lower Suktel, Orissa) displacing "
                                  "4,160 families; while the underlying project is nominally framed as "
                                  "providing 'irrigation and potable water', the paper's entire empirical "
                                  "analysis concerns land acquisition law (Land Acquisition Act 1894/1984), "
                                  "compensation, and displacement impacts on landholding/income/caste "
                                  "inequality - no water or sanitation service-access outcome is examined or "
                                  "measured anywhere in the study. Fails inclusion criterion 4 (wrong outcome).")
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"

with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

ex_rows.append({
    "record_id": "R5807B67AFA98",
    "title": "Resettlement issues in water resources development: An empirical study of the lower Suktel irrigation project, Orissa",
    "authors": "Agnihotri, Anita",
    "year": "2008",
    "stage": "full_text",
    "exclusion_code": "E04",
    "exclusion_reason_detail": ("Study of land acquisition/resettlement policy and displacement impacts for "
                                  "an irrigation project; no water or sanitation service-access outcome is "
                                  "examined or measured - fails inclusion criterion 4."),
    "reviewer": "Claude-AI-fulltext-2026-09-21",
    "date": "2026-09-23",
})

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ex_fieldnames)
    w.writeheader()
    w.writerows(ex_rows)
os.replace(tmp, EXLOG)

print("Batch 137 recorded: 3 includes, 1 exclude.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
