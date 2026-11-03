#!/usr/bin/env python3
"""Eighty-first full-text screening batch: 10 excludes, 5 includes."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
FT_DB = os.path.join(BASE, "02_screening/full_text/full_text_screening_database.csv")
EXCL_LOG = os.path.join(BASE, "02_screening/exclusion_log/exclusion_log.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

EXCLUDES = {
    "R7BC30D37A001": {
        "code": "E05",
        "detail": "Pure literature-review/synthesis book chapter on water quality in India and Nepal; relies exclusively on secondary sources (government reports, prior studies); no original data collection.",
        "note": "No original empirical data collection; doctrinal/synthesis literature review.",
    },
    "R2DDCC2FC03E7": {
        "code": "E01",
        "detail": "Macro/basin-level OECD water-governance-principles and toxicological-index analysis of Nigeria's water policy reform; does not examine any household/applicant-level legal-administrative access mechanism.",
        "note": "Wrong topic/unit of analysis; macro governance-index study, no household-level access examination.",
    },
    "RF16C02EE1F2F": {
        "code": "E05",
        "detail": "Explicitly self-described 'doctrinal legal research methodology' paper on South Africa's Free Basic Water policy and constitutional right to water; Ethics Statement confirms no human participants, relies exclusively on secondary/documentary sources.",
        "note": "No original empirical data collection; doctrinal constitutional-law analysis.",
    },
    "RC28E7E20373D": {
        "code": "E01",
        "detail": "Validation study of a Group Maturity Index tool for community health clubs' hygiene-promotion program organizational monitoring in Zimbabwe; does not examine any water/sanitation legal-administrative access mechanism.",
        "note": "Wrong topic entirely; hygiene-promotion organizational-monitoring tool validation, not access mechanism.",
    },
    "R178AF8716D6A": {
        "code": "E06",
        "detail": "Pure hydrological/engineering water-balance study of Delhi's urban water system using IDW spatial interpolation on secondary DJB/CGWB/CPCB datasets; no household-level empirical data collection.",
        "note": "Engineering-only study; secondary hydrological/GIS data, no household-level access examination.",
    },
    "RDC76C62702D0": {
        "code": "E01",
        "detail": "Zero-inflated negative binomial regression modeling retail water store locations across California census tracts as a proxy for tap-water-alternative reliance, using secondary SDWA/ACS datasets; examines market substitution behavior, not any legal-administrative access mechanism.",
        "note": "Wrong topic; market-substitution/retail-store-siting study, not legal-administrative access.",
    },
    "RD5DE21EB6425": {
        "code": "E05",
        "detail": "Explicit systematic literature review ('mini review') of 76 secondary sources on WASH barriers in Sub-Saharan Africa, with a documented PRISMA-style search/screening methodology; no original data collection.",
        "note": "No original empirical data collection; systematic literature review of secondary sources.",
    },
    "R7E702A70F8C6": {
        "code": "E01",
        "detail": "Process-review paper on WaterAid's SusWASH programmatic system-strengthening approach in Uganda and Cambodia; Likert-scale stakeholder perception surveys of institutional 'building blocks,' not an empirical examination of household-level legal-administrative water access.",
        "note": "Wrong topic/unit of analysis; NGO programmatic capacity-building process evaluation.",
    },
    "R3B73F903D49F": {
        "code": "E01",
        "detail": "Review of national data-monitoring systems (EMIS/HMIS) for WASH in schools and health care facilities (non-household settings) across ten countries; explicitly excludes household-level water access.",
        "note": "Wrong topic; institutional/non-household WASH monitoring-data-systems review.",
    },
    "R345D7E2BCAC6": {
        "code": "E01",
        "detail": "Cross-national regression analysis (140 states, 2000-2015) of national/local democratic institutions and basic water access using aggregate World Bank/V-Dem/REIGN datasets; macro governance-index study with no household/applicant-level legal-administrative access examination.",
        "note": "Wrong topic/unit of analysis; macro cross-national governance-index regression study.",
    },
}

INCLUDES = {
    "R17BBF0A9B354": "Robust mixed-methods study (647 water-point WSSI quantitative assessments + 103 semi-structured qualitative committee interviews) in Cameroon's Mvila Division documenting legal-institutional content including the General Code of Decentralized Territorial Collectivities (Law No. 2019/024), institutional/governance/economic analysis of water-point committee failures, and a proposed intermunicipal syndicate legal structure. record_id R17BBF0A9B354.",
    "R0A361F399C81": "Mixed-methods household-level study (152 house-unit toilet mapping + natural group discussions + focus groups) in Kumasi, Ghana examining landlord-tenant exclusion from shared-sanitation access, the legal abolition of bucket latrines, and proposed legal/regulatory instruments (building-code enforcement) to ensure landlord provision of adequate tenant sanitation. record_id R0A361F399C81.",
    "R25C5F4851EB7": "Qualitative study (243 interviews + 39 FGDs across 18 communities in Ghana, Kenya, and Zambia) examining institutional governance of community-managed rural water supplies, including tariff-setting decision-making, transparency/accountability rights, and community participation in water-committee governance. record_id R25C5F4851EB7.",
    "R22849E39FE23": "Mixed-methods study (299 respondents: surveys, interviews, FGDs across 30 water points) in Nkhata Bay District, Malawi examining Water Point Committee governance, traditional-authority by-law enforcement, and informal contribution-based exclusionary access rules, with recommendations to codify inter-village access rights and responsibilities. record_id R22849E39FE23.",
    "R44ED9C065C16": "Qualitative study (98 participants: interviews and FGDs) in Central Gonja District, Ghana and Mtubatuba Municipality, South Africa examining household-level access barriers under South Africa's Water Services Act, National Water Act, Free Basic Water policy, and Ghana's Community Water and Sanitation Agency Act, including corruption/favouritism in distribution and a public-private-partnership water-treatment model. record_id R44ED9C065C16.",
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
