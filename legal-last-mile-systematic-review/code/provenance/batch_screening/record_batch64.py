import csv, tempfile, os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-21"

DECISIONS = [
    ("R33EDCF0902FE", "exclude", "E01",
     "Jensen, Boratto, Rossi et al. (2025), Environmental Science: "
     "Advances 4:1373-1402, 'The status of domestic wastewater "
     "treatment in the Arctic.' A Panarctic critical review of national "
     "regulations, treatment technologies and levels, and ecosystem "
     "impacts of wastewater discharge across all Arctic nations. A "
     "broad, multi-country infrastructure/regulatory review at the "
     "national/utility level (effluent quality standards, treatment "
     "plant technology types, sludge disposal); no household-level "
     "eligibility, documentation, fee, discretion, or enforcement "
     "mechanism governing individual connection access is examined -- "
     "wrong topic, consistent with prior E01 precedent for broad "
     "infrastructure/regulatory-review studies."),
    ("RD1D7FB8C4689", "exclude", "E01",
     "Mansfield (2023), Children's Geographies 21(5):944-960, \"'They'll "
     "be the ones that's looking after it' -- unravelling institutional "
     "factors that shape children's participation in urban planning for "
     "informal settlements.\" Qualitative case study (32 staff "
     "interviews, institutional-logics framework) of an NGO/research "
     "program's (RISE, Fiji) internal organisational culture around "
     "including children in water/sanitation-infrastructure co-design "
     "workshops. The study examines program-governance and "
     "participation-typology dynamics within a donor-funded NGO "
     "research project, not a government/utility legal-administrative "
     "mechanism (eligibility, documentation, fee, discretion, "
     "enforcement) governing household water/sanitation connection "
     "access -- wrong topic."),
    ("RE6A753BADE5C", "exclude", "E01",
     "Gulumbe, Yusuf, Faggo, Yahaya & Manga (2023), Public Health "
     "Challenges 2:e118, 'The interplay among conflict, water scarcity, "
     "and cholera in Northern Nigeria.' A narrative commentary (not "
     "primary empirical research) synthesising the literature on how "
     "armed conflict, displacement and water scarcity interact to drive "
     "cholera transmission in Northern Nigeria. Broad public-health "
     "epidemiology/conflict commentary; no primary data collection and "
     "no analysis of a specific household-level legal-administrative "
     "water/sanitation access mechanism -- wrong topic."),
    ("R844EAC3AEE12", "exclude", "E01",
     "Dewi, Kusumoarto & Rejoni (2026), IOP Conf. Ser.: Earth Environ. "
     "Sci. 1622:012019, 'Strengthening Community Participation in Slum "
     "Settlement Arrangement of Pasirjaya Urban Kampong, Bogor.' "
     "Descriptive qualitative study (16 respondents, FGDs) assessing "
     "settlement conditions against Indonesia's seven official slum "
     "indicators (building, road, water, drainage, wastewater, waste, "
     "fire protection) and community-participation level via Arnstein's "
     "ladder. A broad slum-upgrading/participatory-planning assessment "
     "across many infrastructure domains; water discussion is limited "
     "to existing PDAM/well source usage and reliability, with no "
     "specific household-level eligibility, documentation, fee, "
     "discretion, or enforcement mechanism governing water/sanitation "
     "connection access examined -- wrong topic."),
]

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

found = set()
exlog_rows = []
for row in rows:
    for rid, decision, code, detail in DECISIONS:
        if row["record_id"] == rid:
            found.add(rid)
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = decision
            row["final_decision"] = decision
            row["reviewer_1"] = REVIEWER
            if decision == "exclude":
                row["exclusion_reason"] = code
                row["exclusion_reason_detail"] = detail
                exlog_rows.append({
                    "record_id": rid,
                    "title": row["title"],
                    "authors": row["authors"],
                    "year": row["year"],
                    "stage": "full_text",
                    "exclusion_code": code,
                    "exclusion_reason_detail": detail,
                    "reviewer": REVIEWER,
                    "date": DATE,
                })

missing = {rid for rid, *_ in DECISIONS} - found
if missing:
    raise SystemExit(f"records not found: {missing}")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, DB)

with open(EXLOG, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    ex_fieldnames = reader.fieldnames
    ex_rows = list(reader)
ex_rows.extend(exlog_rows)
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXLOG))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=ex_fieldnames)
    writer.writeheader()
    writer.writerows(ex_rows)
os.replace(tmp, EXLOG)

print("screening db updated:", found)
print("exclusion log rows appended:", len(exlog_rows))
