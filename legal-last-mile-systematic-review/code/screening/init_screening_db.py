#!/usr/bin/env python3
"""Merge newly deduplicated records into the persistent screening database.

The screening database (02_screening/title_abstract/screening_database.csv)
accumulates reviewer decisions over time, potentially across several rounds
of searching and deduplication. This script's only job is to add genuinely
new records to it -- it never overwrites a decision a reviewer has already
made, and it never silently resolves a record_id collision. Per
REPRODUCIBILITY.md, an original record is never clobbered.

Standard library only, consistent with this repository's existing
scrapers (see ../../../README.md).

INPUT
-----
--dedup-file : path to a deduplicated_records.csv produced by
               ../search/deduplicate.py (schema: record_id, database,
               title, authors, year, doi, duplicate,
               title_abstract_decision, full_text_decision,
               exclusion_reason, reviewer_1, reviewer_2, conflict,
               final_decision)
--screening-db : path to 02_screening/title_abstract/screening_database.csv
                 (created if it does not yet exist, with the same schema)

BEHAVIOR
--------
- A record_id already present in the screening database is left untouched,
  even if its title/doi has changed upstream -- report the mismatch instead
  of resolving it silently.
- A record_id not yet present is appended with blank decision fields.
- Nothing is deleted. Nothing already decided is modified.

USAGE
-----
    python3 init_screening_db.py \\
        --dedup-file ../../01_search/deduplicated/deduplicated_records.csv \\
        --screening-db ../../02_screening/title_abstract/screening_database.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

SCHEMA = [
    "record_id", "database", "title", "authors", "year", "doi",
    "duplicate", "title_abstract_decision", "full_text_decision",
    "exclusion_reason", "reviewer_1", "reviewer_2", "conflict", "final_decision",
]


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dedup-file", type=Path, required=True)
    parser.add_argument("--screening-db", type=Path, required=True)
    args = parser.parse_args()

    if not args.dedup_file.exists():
        print(f"No deduplicated-records file at {args.dedup_file} -- nothing to ingest.")
        print("Run code/search/deduplicate.py first once real search exports exist.")
        return 0

    new_records = read_csv(args.dedup_file)
    existing_records = read_csv(args.screening_db)
    existing_by_id = {r["record_id"]: r for r in existing_records}

    appended = 0
    mismatched = []

    for rec in new_records:
        rid = rec["record_id"]
        if rid in existing_by_id:
            prior = existing_by_id[rid]
            if prior.get("title", "") != rec.get("title", "") or prior.get("doi", "") != rec.get("doi", ""):
                mismatched.append(rid)
            continue  # never overwrite an existing row, decided or not
        existing_records.append({field: rec.get(field, "") for field in SCHEMA})
        appended += 1

    args.screening_db.parent.mkdir(parents=True, exist_ok=True)
    with args.screening_db.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA)
        writer.writeheader()
        writer.writerows(existing_records)

    print(f"Appended {appended} new record(s) to {args.screening_db}")
    print(f"Screening database now has {len(existing_records)} total record(s).")
    if mismatched:
        print(f"WARNING: {len(mismatched)} record_id(s) already present with different "
              f"title/doi than the incoming file -- left untouched, resolve manually: {mismatched}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
