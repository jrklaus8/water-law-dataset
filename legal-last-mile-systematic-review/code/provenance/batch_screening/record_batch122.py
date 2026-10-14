import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

INCLUDES = {
    "RC089E19DF34F": "Documents a real institutional/legal regulatory framework (Indonesia's Law No. 7/2004 on Water Resources, Regulation No. 16/2005, Presidential Decree No. 67/2005, Governor Decree establishing the Jakarta Water Supply Regulatory Body) governing 25-year private-concession contracts, with real longitudinal household-level connection/coverage data (1993-2022 service coverage %, non-revenue water %, water sold, actual vs. target), tariff-adjustment history, and documented small-scale provider types (public hydrants, water tanks, resellers) serving the urban poor via a cross-subsidy policy. Extracted as S659.",
    "R371D7DD278E0": "Documents a real litigated judicial-review case (six local authorities v. the Director General of Water Services challenging pre-payment 'Budget Payment Units' as unlawful disconnection, Mr Justice Harrison ruling for the local authorities) and the resulting Water Industry Act 1999 (banning water disconnection for non-payment to domestic premises, prohibiting BPUs, establishing Vulnerable Groups Regulations), with real household-level uptake data (7,693 successful Vulnerable Groups applications in 2003-04, 9,217 in 2004-05; 1.4% take-up rate) and disconnection statistics, Great Britain. Extracted as S660.",
    "R32DF2C4FFB4F": "Documents the post-1989 privatization institutional shift from 'social equity' to 'market environmental' water-charging (Water Act 2003 drought-management provisions, EU Water Framework Directive, statutory no-disconnection 'right to water'), against real household-level empirical data (water bills by company 2005-07, per-capita-consumption figures, affordability data -- 51.7% of non-working households spending >3% of disposable income on water) plus primary interviews (22 households and 4 water-resource teams during the 2006 drought), England and Wales. Extracted as S661.",
}

EXCLUDES = {
    "RDD25A310EACB": {
        "title": "Urban governance and multilateral aid organizations: The case of informal water supply systems",
        "authors": "Moretto L.",
        "year": "2007",
        "code": "E05",
        "detail": "Comparative policy-document/discourse-analysis review comparing World Bank, UN-HABITAT, and EU governance philosophies toward informal water providers, citing other studies' secondary findings rather than conducting its own primary empirical data collection -- no methodology section, no original household-level data, same rationale as the Gurria/McClanahan/van Dijk & Blokland policy-discourse-review exclusions.",
    },
    "RDABCD99464D4": {
        "title": "Regulation of environmental-protection water releases in the Upper Volga basin as a method of increasing the reliability of water supply in the Moscow Region",
        "authors": "Klepov V.I.",
        "year": "2007",
        "code": "E06",
        "detail": "Purely technical hydraulic-engineering simulation-modeling study of reservoir water-release regulation for environmental protection and supply reliability in the Moscow region; no legal/institutional factor, no household-level data -- matches the Delhi hydrological IDW-interpolation/Jimenez-Perez-Foguet GIS water-point-mapping engineering-only precedent.",
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
