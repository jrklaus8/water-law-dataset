#!/usr/bin/env python3
"""Safely update one record in the full-text screening database.

Hand-editing full_text_screening_database.csv in a text editor risks
breaking CSV quoting on titles/authors that contain commas or quotes, and
gives no protection against typo'd enum values (e.g. "retreived") that
would silently fail validate_schemas.py's enum checks -- it only checks
headers, not cell values. This script is the safe path for the one-record
update loop the researcher will run repeatedly while doing retrieval and
full-text screening: it validates every field it touches and writes
atomically so a crash mid-write can never corrupt the file.

Only the fields explicitly passed are changed; everything else on the row
is left exactly as it was. Standard library only, consistent with this
repository's existing scrapers (see ../../../README.md).

USAGE
-----
    # mark a record retrieved and where the PDF lives
    python3 update_full_text_record.py --full-text-db ... --record-id <id> \\
        --status retrieved --location "/path/to/paper.pdf"

    # record a full-text decision
    python3 update_full_text_record.py --full-text-db ... --record-id <id> \\
        --decision exclude --exclusion-reason E01 \\
        --exclusion-detail "p.4: discusses only pipe-network engineering, no legal/administrative mechanism" \\
        --reviewer-1 "Jane Doe"

    # record it as not retrievable
    python3 update_full_text_record.py --full-text-db ... --record-id <id> \\
        --status not_retrievable --notes "no institutional access, publisher paywall"

Refuses to run if --record-id is not found, or if any value fails its
enum check -- nothing is written in that case.
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import tempfile
from pathlib import Path

csv.field_size_limit(sys.maxsize)

SCHEMA = [
    "record_id", "title", "authors", "year", "doi", "url",
    "full_text_status", "full_text_location",
    "full_text_decision", "exclusion_reason", "exclusion_reason_detail",
    "reviewer_1", "reviewer_2", "conflict", "final_decision", "notes",
]

VALID_STATUS = {"", "sought", "retrieved", "not_retrievable"}
VALID_DECISION = {"", "include", "exclude"}
VALID_EXCLUSION_REASON = {"", "E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12"}
VALID_CONFLICT = {"", "true", "false"}


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv_atomic(path: Path, rows: list[dict]) -> None:
    fd, tmp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=SCHEMA)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(tmp_path, path)
    except BaseException:
        Path(tmp_path).unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--full-text-db", type=Path, required=True)
    parser.add_argument("--record-id", required=True)
    parser.add_argument("--status", choices=sorted(VALID_STATUS - {""}), help="full_text_status")
    parser.add_argument("--location", help="full_text_location -- file path or URL")
    parser.add_argument("--decision", choices=sorted(VALID_DECISION - {""}), help="full_text_decision")
    parser.add_argument("--exclusion-reason", choices=sorted(VALID_EXCLUSION_REASON - {""}), help="E01-E12")
    parser.add_argument("--exclusion-detail", help="exclusion_reason_detail -- cite the specific page/section")
    parser.add_argument("--reviewer-1")
    parser.add_argument("--reviewer-2")
    parser.add_argument("--conflict", choices=["true", "false"])
    parser.add_argument("--final-decision", choices=sorted(VALID_DECISION - {""}))
    parser.add_argument("--notes")
    args = parser.parse_args()

    if not args.full_text_db.exists():
        print(f"No full-text database at {args.full_text_db}.")
        return 1

    rows = read_csv(args.full_text_db)
    target = next((r for r in rows if r["record_id"] == args.record_id), None)
    if target is None:
        print(f"record_id {args.record_id!r} not found in {args.full_text_db} -- nothing written.")
        return 1

    if args.decision == "exclude" and not args.exclusion_reason and not (target.get("exclusion_reason") or "").strip():
        print("WARNING: --decision exclude with no --exclusion-reason and none already recorded.")

    updates = {
        "full_text_status": args.status,
        "full_text_location": args.location,
        "full_text_decision": args.decision,
        "exclusion_reason": args.exclusion_reason,
        "exclusion_reason_detail": args.exclusion_detail,
        "reviewer_1": args.reviewer_1,
        "reviewer_2": args.reviewer_2,
        "conflict": args.conflict,
        "final_decision": args.final_decision,
        "notes": args.notes,
    }
    changed = []
    for field, value in updates.items():
        if value is not None:
            target[field] = value
            changed.append(field)

    if not changed:
        print("No fields given to update -- nothing written. See --help for available fields.")
        return 0

    write_csv_atomic(args.full_text_db, rows)
    print(f"Updated {args.record_id}: {', '.join(changed)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
