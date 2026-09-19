#!/usr/bin/env python3
"""Seed and maintain the full-text screening database (Phase 6).

Mirrors init_screening_db.py's idempotent-merge design, one stage later:
this script's only job is to add genuinely new record_ids to
02_screening/full_text/full_text_screening_database.csv -- it never
overwrites a retrieval status or reviewer decision already recorded, and
it never silently resolves a record_id collision. Per REPRODUCIBILITY.md,
an original record is never clobbered.

Why a separate file rather than reusing screening_database.csv's own
full_text_decision column: full-text screening needs fields the
title/abstract stage has no use for (retrieval status, where the PDF
actually lives) and a second, independent reviewer_1/reviewer_2/conflict
pairing -- reusing the title/abstract stage's columns would either
overwrite that stage's already-recorded reviewer identities and conflict
history, or require cramming two stages' worth of reviewer bookkeeping
into one set of columns. See DATA_DICTIONARY.md for how the two files
relate; screening_database.csv's own full_text_decision/reviewer columns
are left unused going forward -- this file is the single source of truth
for Phase 6.

Standard library only, consistent with this repository's existing
scrapers (see ../../../README.md).

INPUT
-----
--screening-db : path to 02_screening/title_abstract/screening_database.csv
                 -- every record with final_decision == "include" is in
                 scope for full-text retrieval.
--full-text-db : path to 02_screening/full_text/full_text_screening_database.csv
                 (created if it does not yet exist)

BEHAVIOR
--------
- A record_id already present in the full-text database is left
  completely untouched, regardless of what changed upstream.
- A record_id with final_decision == "include" not yet present is
  appended with retrieval/decision fields blank.
- A record_id present in the full-text database whose upstream
  final_decision has since changed away from "include" is left in place
  (already-started full-text work is never silently discarded) but
  flagged in this script's output so a human can look at it.
- Nothing is deleted.

USAGE
-----
    python3 init_full_text_db.py \\
        --screening-db ../../02_screening/title_abstract/screening_database.csv \\
        --full-text-db ../../02_screening/full_text/full_text_screening_database.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

SCHEMA = [
    "record_id", "title", "authors", "year", "doi", "url",
    "full_text_status", "full_text_location",
    "full_text_decision", "exclusion_reason", "exclusion_reason_detail",
    "reviewer_1", "reviewer_2", "conflict", "final_decision", "notes",
]

# See FULL_TEXT_README.md for what each status/decision value means and
# the workflow that produces them.
VALID_STATUS = {"", "sought", "retrieved", "not_retrievable"}
VALID_DECISION = {"", "include", "exclude"}


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--screening-db", type=Path, required=True)
    parser.add_argument("--full-text-db", type=Path, required=True)
    args = parser.parse_args()

    if not args.screening_db.exists():
        print(f"No screening database at {args.screening_db} -- nothing to seed from.")
        return 0

    screening_rows = read_csv(args.screening_db)
    included = [r for r in screening_rows if r.get("final_decision") == "include"]
    included_ids = {r["record_id"] for r in included}

    existing_records = read_csv(args.full_text_db)
    existing_by_id = {r["record_id"]: r for r in existing_records}

    appended = 0
    no_longer_included = []

    for rec in included:
        rid = rec["record_id"]
        if rid in existing_by_id:
            continue
        existing_records.append({
            "record_id": rid,
            "title": rec.get("title", ""),
            "authors": rec.get("authors", ""),
            "year": rec.get("year", ""),
            "doi": rec.get("doi", ""),
            "url": rec.get("url", ""),
            "full_text_status": "",
            "full_text_location": "",
            "full_text_decision": "",
            "exclusion_reason": "",
            "exclusion_reason_detail": "",
            "reviewer_1": "",
            "reviewer_2": "",
            "conflict": "",
            "final_decision": "",
            "notes": "",
        })
        appended += 1

    for rid in existing_by_id:
        if rid not in included_ids:
            no_longer_included.append(rid)

    args.full_text_db.parent.mkdir(parents=True, exist_ok=True)
    with args.full_text_db.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA)
        writer.writeheader()
        writer.writerows(existing_records)

    print(f"Appended {appended} new record(s) to {args.full_text_db}")
    print(f"Full-text database now has {len(existing_records)} total record(s).")
    if no_longer_included:
        print(f"WARNING: {len(no_longer_included)} record_id(s) already in the full-text "
              f"database no longer show final_decision == 'include' upstream -- left in "
              f"place, resolve manually if this wasn't expected: {no_longer_included}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
