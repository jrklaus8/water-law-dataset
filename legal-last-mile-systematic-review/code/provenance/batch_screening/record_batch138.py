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
for rid in ("RBA76411516B7", "R3DF6CF34D9CE"):
    assert by_id[rid]["full_text_decision"] == "", f"{rid} not open"
    assert by_id[rid]["final_decision"] == "", f"{rid} not open"

# RBA76411516B7 - Kucher 2005, Medieval Siena - EXCLUDE E01
r = by_id["RBA76411516B7"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "exclude"
r["final_decision"] = "exclude"
r["exclusion_reason"] = "E01"
r["exclusion_reason_detail"] = ("Historical-legal study of medieval Sienese statutes (1250-1348) regulating "
                                  "industrial water use (guild mills, textile/leather/butchering processes), "
                                  "firefighting, and a physical/legal purity hierarchy across fountain "
                                  "complexes; the paper explicitly notes personal/domestic water consumption "
                                  "is 'the most elusive category' with almost no statutory coverage, and at no "
                                  "point examines differential household/community access, exclusion, or "
                                  "connection outcomes by wealth, class or social status. Pure doctrinal/"
                                  "historical-legal commentary without empirical access evidence - fails "
                                  "inclusion criteria 1 and 4.")
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"

# R3DF6CF34D9CE - Hasan 2006, Orangi Pilot Project - INCLUDE
r = by_id["R3DF6CF34D9CE"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"
r["notes"] = ("Documentary/institutional case study of the Orangi Pilot Project-Research and Training "
              "Institute (OPP-RTI) NGO's low-cost community-built sanitation programme in Karachi, Pakistan "
              "informal settlements (katchi abadis), documenting Pakistan's real Katchi Abadi Improvement "
              "and Regularization Programme (1973, 99-year lease regularization), the Devolution Plan 2001/"
              "Local Government Ordinance 2001 administrative structure, and a provincial ombudsman ruling "
              "compelling the Karachi Water and Sewerage Board (KWSB) to take over maintenance of "
              "community-built sewerage in Manzoor Colony. Quantified outcomes: infant mortality decline "
              "128->37 per 1,000 (1983-1993) in communities that built sanitation; 95,991 sanitary latrines "
              "and 6,408 lane sewers built (87.9% of total) across Orangi by 2004; formal-vs-informal "
              "coverage disparity data (non-OPP area denied assistance by local government until 1987). "
              "Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S684.")

with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

ex_rows.append({
    "record_id": "RBA76411516B7",
    "title": "The Use of Water and its Regulation in Medieval Siena",
    "authors": "Kucher, Michael",
    "year": "2005",
    "stage": "full_text",
    "exclusion_code": "E01",
    "exclusion_reason_detail": ("Historical-legal study of medieval industrial/firefighting water-use "
                                  "regulation; domestic use explicitly noted as barely covered by statutes, "
                                  "no household/community access-exclusion outcome examined - fails "
                                  "inclusion criteria 1 and 4."),
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

print("Batch 138 recorded: 1 include, 1 exclude.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
