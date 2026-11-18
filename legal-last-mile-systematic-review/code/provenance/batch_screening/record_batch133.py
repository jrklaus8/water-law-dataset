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

# Verify open
for rid in ("R8F361F312043", "RAF15F47BD74F"):
    assert by_id[rid]["full_text_decision"] == "", f"{rid} not open"
    assert by_id[rid]["final_decision"] == "", f"{rid} not open"

# R8F361F312043 - Goldin 2010, INCLUDE
r = by_id["R8F361F312043"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"
r["notes"] = ("Qualitative institutional case study of water governance in South Africa's "
              "Breede-Overberg Water Management Area, documenting real statutory frameworks "
              "(National Water Act No. 36 of 1998; Water Services Act No. 108 of 1997; abolition "
              "of riparian water rights 1996) and Catchment Management Agency/Water User "
              "Association institutional participation structures, contrasted via paired "
              "ethnographic case narratives (white commercial farmers' Ruensveld/Duivenhoks "
              "irrigation scheme vs. Kassiesbaai fishing village) showing differential "
              "institutional access/participation and water-scheme outcomes tied to apartheid-era "
              "legal/network legacies. Included per INCLUSION_EXCLUSION.md criteria 1-9. "
              "Extracted as S679.")

# RAF15F47BD74F - Thunqvist et al 2012, EXCLUDE E01
r = by_id["RAF15F47BD74F"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "exclude"
r["final_decision"] = "exclude"
r["exclusion_reason"] = "E01"
r["exclusion_reason_detail"] = ("Qualitative photo-elicitation methodology research note documenting "
                                  "general infrastructural deprivation (water, sanitation, roads, garbage, "
                                  "shelter) among female-headed households in an informal settlement in "
                                  "Dar es Salaam; no legal, administrative, institutional, regulatory or "
                                  "governance factor is examined anywhere in the paper (no statutory "
                                  "framework, utility governance, tenure, or connection-policy analysis) - "
                                  "fails inclusion criterion 2.")
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"

with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

ex_rows.append({
    "record_id": "RAF15F47BD74F",
    "title": "The Figures behind Facts: Photo-eliciting Infrastructural Consequences in Dar es Salaam, Tanzania",
    "authors": "Thunqvist, Eva-Lotta; Ilskog, Elisabeth; Mvungi, Abu",
    "year": "2012",
    "stage": "full_text",
    "exclusion_code": "E01",
    "exclusion_reason_detail": ("Qualitative photo-elicitation methodology research note on general "
                                  "infrastructural deprivation in a Dar es Salaam informal settlement; "
                                  "no legal/institutional/governance factor examined - fails inclusion "
                                  "criterion 2."),
    "reviewer": "Claude-AI-fulltext-2026-09-21",
    "date": "2026-09-22",
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

print(f"Batch 133 recorded: 1 include, 1 exclude.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
