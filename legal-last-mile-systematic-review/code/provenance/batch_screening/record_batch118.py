import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

INCLUDES = {
    "RCFD849FB0013": "Documents a real regulatory framework (Indian Easements Act 1882 tying groundwater rights to land ownership, leaving the landless without rights; Chennai Metropolitan Area Ground Water (Regulation) Act 1987/2002 licensing and enforcement, including a documented tanker-seizure enforcement action) against real household-level outcome data (68-household survey, Perumbakkam) showing income-based access bifurcation -- wealthier households buying packaged water vs. poor households dependent on degraded groundwater -- and water-related economic/health stress. Extracted as S654.",
    "R762608282964": "Qualitative comparative case study (15 in-depth interviews across two informal settlements, Banana City Durban and Endlovini Cape Town) documenting a real tenure-based legal struggle (Banana City residents' successful human-rights-lawyer-led eviction defense against the University of KwaZulu-Natal landowner, followed by municipal land purchase enabling service legalization), Cape Town's landowner-consent requirement barring service extension, the Free Basic Water/Indigent Water Policy framework, and real household-level infrastructure data (taps/toilets per settlement section serving named family counts) with a documented gendered access burden. Extracted as S655.",
    "R3551E4A62FAE": "Documents Kenya's Water Act No. 8 of 2002 and tenure-based illegality of informal settlements barring statutory Nairobi City Water and Sewerage Company connection, with real documented enforcement action (2006 mass disconnection of illegal connections; 2007 riot-police response to a 5-day water-protest in Kibera) against large-N household survey data (NUHDSS longitudinal surveillance, 23,344 households, water-source breakdown table) plus 36 focus group discussions (256 participants) documenting illegal-connection pricing, quality, and exclusion patterns. Extracted as S656.",
}

EXCLUDES = {
    "R29856BE0CB68": {
        "title": "Willingness to Pay and Willingness to Accept Compensation for Changes in Urban Water Customer Service Standards",
        "authors": "Hatton MacDonald D.; Morrison M.D.; Barnes M.B.",
        "year": "2010",
        "code": "E01",
        "detail": "Fundamentally a choice-modelling methodological comparison (willingness-to-pay vs. willingness-to-accept elicitation techniques) using hypothetical service-standard scenarios in Adelaide, Australia; General Service Level Agreements are mentioned only as regulatory background, not tested as an exposure -- same rationale as the Lanz & Provins discrete-choice-experiment survey-methodology exclusion.",
    },
    "R1CC50D5011B9": {
        "title": "An optimization model for integrated urban planning: Development and application to Algeria's Reghaïa and Heraoua municipalities",
        "authors": "Zagonari F.",
        "year": "2011",
        "code": "E01",
        "detail": "Mathematical optimization/GIS modeling paper for municipal land-use planning; water quantity/quality is one of several policy variables in a macro simulation, with no legal/institutional factor tested as exposure and no household-level access data -- same rationale as the Porse et al./Nakhla modeling-methodology exclusions.",
    },
    "RD175F8091708": {
        "title": "A review of the relative merits of conserving, using, or draining papyrus swamps",
        "authors": "Maclean I.M.D.; Boar R.R.; Lugo C.",
        "year": "2011",
        "code": "E01",
        "detail": "Wetland-ecosystem economic-valuation review concerning conservation vs. agricultural drainage of African wetlands -- not household water/sanitation service access at all.",
    },
}

WRONG_FILE = {
    "R58E83E4193E6": "Title/author confirmed matching (Cahill-Ripley 2011, 'The Human Right to Water and its Application in the Occupied Palestinian Territories,' Routledge). However, the delivered PDF's extracted text (117K characters) contains only front matter/Introduction and the full Bibliography/List of Treaties -- Chapters 1-7, including the book's entire empirical Chapter 6 case study (45 semi-structured interviews in the southern West Bank, Table 6.1 WHO sufficiency analysis, Table 6.2 violations summary), are missing from the extraction. Zero '[Page N]' markers appear anywhere in the extracted text, unlike every other PDF read this session, suggesting a genuinely incomplete/corrupted delivered file rather than an extraction-tool artifact. Same handling as the R33E4CEE682AC (Mabiza dissertation) precedent: flagged wrong_file_retrieved, left open, pending a complete re-retrieval.",
}

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

ALL_IDS = set(INCLUDES) | set(EXCLUDES) | set(WRONG_FILE)
found = {r["record_id"]: r for r in rows if r["record_id"] in ALL_IDS}
missing = ALL_IDS - set(found)
assert not missing, f"Missing record_ids: {missing}"

for rid, r in found.items():
    assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided: {r}"

for rid in INCLUDES:
    r = found[rid]
    r["full_text_decision"] = "include"
    r["final_decision"] = "include"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["notes"] = INCLUDES[rid]

for rid, info in EXCLUDES.items():
    r = found[rid]
    r["full_text_decision"] = "exclude"
    r["final_decision"] = "exclude"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["exclusion_reason"] = info["code"]
    r["exclusion_reason_detail"] = info["detail"]

for rid, note in WRONG_FILE.items():
    r = found[rid]
    r["full_text_status"] = "wrong_file_retrieved"
    r["notes"] = note

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"Updated {len(found)} records in full_text_screening_database.csv")

with open(EXCLOG, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    exc_fieldnames = reader.fieldnames
    exc_rows = list(reader)

for rid, info in EXCLUDES.items():
    exc_rows.append({
        "record_id": rid,
        "title": info["title"],
        "authors": info["authors"],
        "year": info["year"],
        "stage": "full_text",
        "exclusion_code": info["code"],
        "exclusion_reason_detail": info["detail"],
        "reviewer": REVIEWER,
        "date": DATE,
    })

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EXCLOG))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=exc_fieldnames)
    writer.writeheader()
    writer.writerows(exc_rows)
os.replace(tmppath, EXCLOG)
print(f"Appended {len(EXCLUDES)} rows to exclusion_log.csv. New total: {len(exc_rows)}")
