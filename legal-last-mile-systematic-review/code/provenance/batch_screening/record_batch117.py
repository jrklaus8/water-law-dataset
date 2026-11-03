import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

INCLUDES = {
    "RE9D7E0998707": "Genuine institutional/administrative water-pricing-policy (flat ARV-based tariff) case study with real WASA accounts data 1988-2008 plus interviews (1993, 2000, 2002, 2010); documents household-level reliability decline (45% receiving 24-hour service 1994 down to 18-21% by 2008), equity/expenditure data by income tier, household coping behavior (storage-tank ownership 66%->80%). Extracted as S646.",
    "R0299C96CF472": "Genuine constitutional/legal water-rights litigation study (Mazibuko v. City of Johannesburg, 'Phiri case', Constitution s27(1)(b), Water Services Act 108 of 1997) through High Court/SCA/Constitutional Court 2008-2009; real household-level service-type breakdown (65% standpipes/20% tanker/15% yard taps for water; sanitation breakdown), Free Basic Water block-tariff history, price-elasticity-by-income data, litigated litre-per-person-per-day outcome. Extracted as S647.",
    "RC4DF38E3B363": "Institutional/legal water-service-privatization case study with real census-based household-level access data (Table 3: basic access/in-home piped connection % across DF/ZMCM/ZMVM, 1990-2010) and legal-institutional factors (concession contracts, COMDA's formal appeal under the 2002 Federal Transparency Law). Extracted as S648.",
    "RAFD43FB2362E": "Rigorous GLM/OLS regression study (2372 municipalities) examining fiscal/administrative federal-transfer allocation under Article 115 of the Mexican constitution as an institutional mechanism driving unequal piped-water coverage for indigenous populations; real household-level coverage outcome data, significant coefficients (indigenous -0.031 p=0.014; transfers pc 0.571 p=0.019). Extracted as S649; effect_sizes candidate.",
    "R5A010875D9FB": "Ecuador's 2008 constitutional water-rights framework (Article 318) and institutional fragmentation (SENAGUA/MIDUVI/MAE/MSP) documented with real household-level access data disaggregated by region, income quintile, urban/rural, and ethnicity (indigenous 18% vs national 48% vs white 57% coverage). Extracted as S650.",
    "RE4E5A4029D2D": "Institutional/regulatory water-sector framework (Ghana PURC Act 538/1997, affermage/management-contract privatization) with real household-level survey data disaggregated by income quintile (connection rates 57%/70%/83% by income band; 43% highest vs 18.5% lowest quintile), reliability (46% of connected households 'only sometimes'/'rarely' receive water), affordability (9-15% of household income on water), and health outcome (80% diarrhea reduction with piped access). Extracted as S651.",
    "R658467768162": "Ethnographic study of illegal/informal water-tapping institutional arrangements (DWASA statutory authority, informal political-committee governance, NGO-facilitated legalization efforts) in a Dhaka bosti; real documented household-level outcome variation in water price ($9-22/hour) and reliability/quality by political position, verbal contractual agreements between room-cluster owners and tenants. Extracted as S652.",
    "R34FB4E74EB11": "Large real household-level water-services survey (2010, 14 Iraqi provinces, thousands of respondents, connection-based sampling) examining water-service continuity/satisfaction and willingness-to-pay, contextualized against Iraq's institutional/legal decentralization framework (2005 Constitution, Law 21 of 2008). Extracted as S653.",
}

EXCLUDES = {
    "RD115629ED34F": {
        "title": "Benchmarking of North Indian urban water utilities",
        "authors": "Singh M.R.; Mittal A.K.; Upadhyay V.",
        "year": "2011",
        "code": "E01",
        "detail": "Purely technical DEA efficiency-benchmarking study of utility-level inputs/outputs (unaccounted-for water, staff, O&M expenditure) for 35 North Indian urban water utilities; no legal/institutional/regulatory factor examined and no household-level data -- utility-level technical efficiency analysis only.",
    },
    "RD039A852D35C": {
        "title": "State versus private sector provision of water services in Armenia",
        "authors": "Harutyunyan N.",
        "year": "2012",
        "code": "E01",
        "detail": "Utility-level 'before/after' privatization performance-benchmarking study (5 companies) using partial-indicator technique on operational/financial/environmental metrics (metering, collection rates, labor productivity, non-revenue water); no household-level access data -- study's own conclusion explicitly flags that impacts on affordability and access to services by poor households were not examined.",
    },
}

ALL_IDS = set(INCLUDES) | set(EXCLUDES)

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

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
