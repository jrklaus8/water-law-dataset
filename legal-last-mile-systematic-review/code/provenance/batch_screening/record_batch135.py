import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}
assert by_id["R2C0C4B70308A"]["full_text_decision"] == ""
assert by_id["R2C0C4B70308A"]["final_decision"] == ""

r = by_id["R2C0C4B70308A"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = "Claude-AI-fulltext-2026-09-21"
r["notes"] = ("Historical-archival/oral-history institutional case study of Orcasitas, an illegal "
              "shantytown on Madrid's periphery (1950s-1986), documenting the informal settlement's "
              "negotiation with formal institutions over water/sanitation infrastructure: the 1971 legal "
              "recognition of the Neighborhood Association (Asociacion de Vecinos), formal negotiations "
              "with the Canal de Isabel II water-canal company (1970 construction), Madrid city council "
              "and Ministry of Housing property/expropriation records, and informal 'stealing water' "
              "workarounds later validated by local authorities. Based on primary archival sources "
              "(Archivo Regional de la Comunidad de Madrid; Spanish Ministry of Housing property files, "
              "a constructed database of 230 of 1,500 families 1950-1971) and oral history interviews. "
              "Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S680.")

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

print("Batch 135 recorded: 1 include, 0 excludes.")
