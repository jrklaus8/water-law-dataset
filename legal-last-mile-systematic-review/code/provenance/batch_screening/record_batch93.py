#!/usr/bin/env python3
"""Batch 93: 1 new include (Ecuador fiscal space World Bank report, S589)."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
FT_DB = os.path.join(BASE, "02_screening/full_text/full_text_screening_database.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

INCLUDES = {
    "R98669D9A19CA": "World Bank/IDB fiscal management and public expenditure review of Ecuador documenting original World-Bank-staff quantile-based subsidy-incidence analysis for the water sector (Table 3.4: water subsidies regressively distributed, 7.9% to poorest quintile vs 41.3% to richest) and a household-level case study (Box 3.2, Machala, El Oro) showing households with a formal water connection pay 0.4% of monthly income for water versus 9.0% for unconnected households served by tankers, tied to decentralized/incomplete municipal water-governance institutions (MIDUVI transfer cuts, no integrated national water-resource-management system). record_id R98669D9A19CA.",
}

def main():
    with open(FT_DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {row["record_id"]: row for row in rows}

    for rid in INCLUDES:
        assert rid in by_id, f"record_id {rid} not found in full-text DB"
        row = by_id[rid]
        assert not row["full_text_decision"], f"{rid} already has full_text_decision={row['full_text_decision']!r}"
        assert not row["final_decision"], f"{rid} already has final_decision={row['final_decision']!r}"

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

    print(f"done, db changed {len(INCLUDES)}")


if __name__ == "__main__":
    main()
