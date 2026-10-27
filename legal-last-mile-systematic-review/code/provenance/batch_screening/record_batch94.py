#!/usr/bin/env python3
"""Batch 94: 2 excludes, 3 new includes (S590-S592)."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
FT_DB = os.path.join(BASE, "02_screening/full_text/full_text_screening_database.csv")
EXCL_LOG = os.path.join(BASE, "02_screening/exclusion_log/exclusion_log.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

EXCLUDES = {
    "R4F2E31188545": {
        "code": "E04",
        "detail": "National-level Tobit econometric analysis (1996-2021 annual time series, 25 observations) of macroeconomic, financial-market, and governance determinants of the aggregate USD investment value of water and sanitation PPP transactions reaching financial closure in Zimbabwe; the outcome variable is aggregate PPP investment financing value, not any household/community-level access, connection, coverage, affordability, or reliability outcome.",
        "note": "Wrong outcome; national-level PPP-investment-financing-value econometric study, no access/connection/coverage outcome examined.",
    },
    "RDA48A50740DB": {
        "code": "E01",
        "detail": "Qualitative case study (27 interviews plus documentary/Ontario Municipal Board case-law analysis) of the political-economic evolution of municipal development-charge (infrastructure impact fee) calculation methodology (average cost vs. marginal cost) across 8 Greater Toronto Area municipalities; water/sewer infrastructure is mentioned only generically as one of many bundled 'hard services' (alongside roads, parks, libraries, fire/police stations, land, buildings, even library books/furniture) with no water-specific data, coverage statistics, or access outcome reported anywhere in the paper.",
        "note": "Wrong topic/unit of analysis; general municipal-infrastructure-financing-methodology study bundling water with many unrelated services, no water-specific access outcome.",
    },
}

INCLUDES = {
    "R052039CCB61E": "Historical quasi-experimental logit analysis (244 Prussian cities, 1880-1887) of how the concentration of local voting/franchise power (the tax-weighted 'Three Class System' vs. more equal franchise in Hannover/Holstein) determined the probability that a city invested in waterworks infrastructure; instrumented for cost and adjusted for community wealth, public-health crisis indicators, and industrial demand, with counterfactual coefficient-swap simulations across provinces. Extracted as S590. record_id R052039CCB61E.",
    "R2B84D3F84A28": "Institutional/fiscal-reform case study of Chinese urban infrastructure provision (national statistics plus a Shanghai case study) documenting a legal-institutional household-level water-access mechanism specific to China's socialist housing/employment system (state-employer-provided housing automatically conferring water/electricity/sewerage access) alongside fiscal-decentralization and infrastructure-connection-fee reforms, with tap-water coverage tracked as an explicit outcome variable (81.0% to 94.9% nationally, 1990-1996; 100% in Shanghai both years). Extracted as S591. record_id R2B84D3F84A28.",
    "R639910BFA05F": "Qualitative case study (interviews with utility, municipal, FIS, central-government, and consumer-association stakeholders) of water-utility privatization and network-extension governance in Cochabamba, Bolivia, documenting SEMAPA's legal restructuring and privatization-driven board/boundary changes, a privatization bid structure tying utility ownership to a specific connection-rate target (90% within 5 years), a World-Bank-funded community co-management/training program (FIS) extending formal connections to squatter communities, and household connection-rate disparities by neighborhood income level (99% in affluent Casco Viejo vs. under 4% inside-house connection in some suburban districts). Extracted as S592. record_id R639910BFA05F.",
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
