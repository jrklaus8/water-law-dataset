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
for rid in ("R0AFB571151F8", "RBE58AF9BAF95", "R925A310D75C8", "R22206B3DC3A0"):
    assert by_id[rid]["full_text_decision"] == "", f"{rid} not open"
    assert by_id[rid]["final_decision"] == "", f"{rid} not open"

# R0AFB571151F8 - Sawchuk, Burke & Padiak 2002, Gibraltar infant mortality - INCLUDE
r = by_id["R0AFB571151F8"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"
r["notes"] = ("Historical demographic case study using primary vital-registration archival data (Gibraltar "
              "registry office/government archives, 1870-1899) comparing civilian vs. military-family infant "
              "mortality, documenting a real institutional/legal-status access mechanism: an 1884 order by "
              "Governor Adye granting military personnel and their families free access to newly-installed "
              "condenser-distilled water while civilians had to pay per bucket, on top of a formal military "
              "water-rationing schedule by rank (commanding officers 7 gal/day; rank and file/wives 2.5 gal/day; "
              "children 1 gal/day). Quantified outcome with inferential statistics: infant mortality rate (IMR) "
              "showed no significant civilian-military difference in Phase I 1870-1884 (Kolmogorov-Smirnov "
              "KS=0.730, p=.66) but a statistically significant divergence in Phase II 1885-1899 after the "
              "water-privilege policy took effect (KS=1.461, p=.028), with military infants showing "
              "substantially higher survival. Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as "
              "S685.")

# RBE58AF9BAF95 - Sandhu 2000, Housing poverty in urban India - EXCLUDE E01
r = by_id["RBE58AF9BAF95"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "exclude"
r["final_decision"] = "exclude"
r["exclusion_reason"] = "E01"
r["exclusion_reason_detail"] = ("Narrative secondary-source synthesis (explicitly 'based on secondary sources' "
                                  "per the paper's own abstract) on general urban housing poverty in India, "
                                  "using ~10 indicators (housing stock, homelessness, structure type, rooms, "
                                  "slums, investment, affordability, ownership, water connection, toilets); "
                                  "water connection is discussed only briefly (two paragraphs) as one incidental "
                                  "indicator among many within the broader housing-poverty topic, not the "
                                  "paper's object of study, and no legal/institutional access mechanism specific "
                                  "to water is examined. Fails inclusion criteria 1-2.")
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"

# R925A310D75C8 - Dhar 2000, Equity and access to basic services - EXCLUDE E05
r = by_id["R925A310D75C8"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "exclude"
r["final_decision"] = "exclude"
r["exclusion_reason"] = "E05"
r["exclusion_reason_detail"] = ("Narrative policy essay covering five basic-service sectors generically (water "
                                  "supply/sewerage, public transport, health, education, housing) with no "
                                  "original data collection - relies entirely on secondary citations (National "
                                  "Sample Survey figures, World Bank reports, a handful of named prior "
                                  "zone-level water-supply studies). Water/sewerage is one of five sectors "
                                  "discussed in roughly two pages; no dedicated empirical study design. Extends "
                                  "the established narrative-synthesis/policy-essay exclusion precedent (cf. "
                                  "Crow & McPike 2009, Gurria/policy-essay precedent).")
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"

# R22206B3DC3A0 - Banerjee 2001, Integrated water resources management NCR-Delhi - EXCLUDE E01
r = by_id["R22206B3DC3A0"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "exclude"
r["final_decision"] = "exclude"
r["exclusion_reason"] = "E01"
r["exclusion_reason_detail"] = ("Macro/regional-level Integrated Water Resources Management (IWRM) project "
                                  "proposal/policy document (INTACH/UNESCO/UNDP-funded) for the Delhi National "
                                  "Capital Region, covering surface/groundwater balance, inter-state water "
                                  "agreements, National Water Policy 1987 framework, water harvesting and "
                                  "sewage-treatment engineering proposals, and institutional-capacity-building "
                                  "plans at the river-basin/regional level. No household-level empirical access "
                                  "data or legal/institutional access-barrier analysis at the household/"
                                  "community level anywhere in the document. Extends the established "
                                  "macro-governance-index/regional-water-planning exclusion precedent (cf. "
                                  "Nkiaka/Schiel/Laitinen/Padowski).")
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"

with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

ex_rows.append({
    "record_id": "RBE58AF9BAF95",
    "title": "Housing poverty in urban India",
    "authors": "Sandhu, R S",
    "year": "2000",
    "stage": "full_text",
    "exclusion_code": "E01",
    "exclusion_reason_detail": ("Secondary-source synthesis on general urban housing poverty; water connection "
                                  "is one incidental indicator among ~10, not the paper's object of study - "
                                  "fails inclusion criteria 1-2."),
    "reviewer": "Claude-AI-fulltext-2026-09-21",
    "date": "2026-09-23",
})
ex_rows.append({
    "record_id": "R925A310D75C8",
    "title": "Equity and access to basic services : Issues and options",
    "authors": "Dhar, V K",
    "year": "2000",
    "stage": "full_text",
    "exclusion_code": "E05",
    "exclusion_reason_detail": ("Narrative policy essay covering five basic-service sectors generically with no "
                                  "original data collection; water is one of five sectors discussed - fails "
                                  "inclusion criterion 3."),
    "reviewer": "Claude-AI-fulltext-2026-09-21",
    "date": "2026-09-23",
})
ex_rows.append({
    "record_id": "R22206B3DC3A0",
    "title": "Integrated management of water resources in the National Capital Region-Delhi",
    "authors": "Banerjee, Ashis",
    "year": "2001",
    "stage": "full_text",
    "exclusion_code": "E01",
    "exclusion_reason_detail": ("Macro/regional-level IWRM project proposal/policy document with no "
                                  "household-level access data or legal/institutional access-barrier analysis - "
                                  "fails inclusion criteria 1-2."),
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

print("Batch 139 recorded: 1 include, 3 excludes.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
