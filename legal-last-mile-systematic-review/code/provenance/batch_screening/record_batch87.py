#!/usr/bin/env python3
"""Eighty-second full-text screening batch: 2 excludes, 4 includes."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
FT_DB = os.path.join(BASE, "02_screening/full_text/full_text_screening_database.csv")
EXCL_LOG = os.path.join(BASE, "02_screening/exclusion_log/exclusion_log.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

EXCLUDES = {
    "R4BFAEC61E31D": {
        "code": "E04",
        "detail": "Output-oriented data envelopment analysis (DEA) of 23 Ghanaian water utilities measuring technical/scale efficiency, revenue slack, and OPEX slack against utility-level financial/archival data; outcome is utility operational performance, not household-level legal-administrative access. Matches established E04 utility/company-performance-outcome precedent (R8821B3A63A95, REA26B447CC9E, RC47ECBF4C9AF, R23EE2449CF6B, R73C7494E55DD/Gidion).",
        "note": "Wrong outcome; utility-level DEA efficiency/performance-benchmarking study, not household-level access.",
    },
    "R90EB686B9582": {
        "code": "E01",
        "detail": "Methodological/simulation paper presenting a GIS/parcel-level scenario-based approach to estimate household affordability impacts of stormwater utility fees in Sacramento County, California, using tax-assessor, land-cover, and Census data; contribution is a generalizable fee-affordability-modeling methodology, not an empirical examination of a legal-administrative access mechanism. Matches established E01 methodological-contribution sub-precedent (R8AD13170998A/RBE33CDE5272C).",
        "note": "Wrong topic/methodological-contribution; stormwater-fee-affordability simulation methodology, not legal-administrative access mechanism.",
    },
}

INCLUDES = {
    "R70028D9094A5": "Qualitative study (interviews with 3 utility employees, 2 landlord/tenant association members, 1 Sanergy employee, 2 Umande Trust employees, 1 public health officer, 12 residents, and 20 manual pit emptiers) of informal faecal-sludge-management pit emptiers in Mukuru and Kibera informal settlements, Nairobi, Kenya, documenting institutional/legal exclusion of pit emptiers under Kenya's Water Act 2016 (devolving sanitation to counties), lack of legal recognition/licencing, cartel violence and NEMA enforcement threats, and a private transfer-station formalisation model. record_id R70028D9094A5.",
    "R6EE7062C2464": "Quantitative study (local census microdata and CAESB water-utility tariff/consumption records for the Federal District, Brazil, 2019 and 2020/2021) of water-tariff subsidy regressivity and affordability, applying a binary logistic regression identifying significant demographic predictors of water-poverty risk (female household head OR=2.78; brown/indigenous race OR=2.84/1.14; single marital status OR=1.27; presence of children OR=1.49; household size OR=0.68; elderly presence OR=0.70) against the backdrop of Brazil's 2020 New Legal Framework for Basic Sanitation (Law 14,026/2020). record_id R6EE7062C2464.",
    "R5BAA92844EB0": "Mixed-methods case study (90-respondent survey of natural-spring users + 9 semi-structured interviews with CEDAE utility staff, local officials, and residents) of hybrid formal/informal water-supply systems in Queimados, Rio de Janeiro Metropolitan Region, Brazil, documenting the 30-year CEDAE concession contract structure, socio-cultural/politico-institutional/health/technical-infrastructural barriers to integrating grassroots water springs with the public network, and clientelist-politics dynamics in infrastructure provision. record_id R5BAA92844EB0.",
    "R0A9549D920CD": "Mixed-methods comparative case study (household surveys n=95 in Harar and n=96 in Wenji; semi-structured interviews n=90+90 across two Akaki Kality woredas; 19 informal-vendor interviews) of urban water insecurity in Ethiopia, documenting Ethiopia's WASH Implementation Framework/One WASH National Programme, the illegality of the small-scale private/informal water-vending sector, a formal city-wide water-rationing policy in Addis Ababa, the National Guideline for Urban Water Utilities Tariff Setting (2013), and quantified financial burdens (informal water costing up to 20x more than formal tariffs; bottled water up to 76x the public-waterpoint price). record_id R0A9549D920CD.",
}

def main():
    with open(FT_DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {row["record_id"]: row for row in rows}

    all_ids = list(EXCLUDES.keys()) + list(INCLUDES.keys())
    for rid in all_ids:
        assert rid in by_id, f"record_id {rid} not found in full-text DB"
        row = by_id[rid]
        assert not row["full_text_decision"], f"{rid} already has full_text_decision={row['full_text_decision']!r}"
        assert not row["final_decision"], f"{rid} already has final_decision={row['final_decision']!r}"

    exclusion_rows_to_append = []

    for rid, info in EXCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "exclude"
        row["final_decision"] = "exclude"
        row["full_text_status"] = "retrieved"
        row["exclusion_reason"] = info["code"]
        row["exclusion_reason_detail"] = info["detail"]
        row["reviewer_1"] = REVIEWER
        row["notes"] = info["note"]
        exclusion_rows_to_append.append({
            "record_id": rid,
            "title": row["title"],
            "authors": row.get("authors", ""),
            "year": row.get("year", ""),
            "exclusion_code": info["code"],
            "exclusion_reason_detail": info["detail"],
            "stage": "full_text",
            "reviewer": REVIEWER,
            "date": "2026-09-22",
        })

    for rid, note in INCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["full_text_status"] = "retrieved"
        row["reviewer_1"] = REVIEWER
        row["notes"] = note

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(FT_DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    os.replace(tmp_path, FT_DB)

    with open(EXCL_LOG, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        log_fieldnames = reader.fieldnames
        log_rows = list(reader)

    for entry in exclusion_rows_to_append:
        log_row = {k: entry.get(k, "") for k in log_fieldnames}
        log_rows.append(log_row)

    fd2, tmp_path2 = tempfile.mkstemp(dir=os.path.dirname(EXCL_LOG), suffix=".csv")
    with os.fdopen(fd2, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=log_fieldnames)
        writer.writeheader()
        for row in log_rows:
            writer.writerow(row)
    os.replace(tmp_path2, EXCL_LOG)

    print(f"done, db changed {len(all_ids)}, log rows now {len(log_rows)}")


if __name__ == "__main__":
    main()
