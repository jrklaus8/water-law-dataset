#!/usr/bin/env python3
"""Build a reviewer_2 handoff queue for full-text screening (Phase 6).

full_text_screening_database.csv carries every one of the 3,659 Phase-5
includes, most still unretrieved -- not a convenient work list for a human
second reviewer, who only needs the records reviewer_1 has already decided
on. This mirrors the same pattern already used for the title/abstract
stage (see 02_screening/title_abstract/reviewer_2_queue.csv and
REVIEWER_2_README.md), adapted to full-text screening's own schema:
`full_text_decision`/`exclusion_reason`/`exclusion_reason_detail` instead
of `title_abstract_decision`, and `notes` in place of `ai_rationale` (for
includes, `notes` carries the extraction-relevant rationale; for excludes,
`exclusion_reason_detail` carries it).

This script's only job is to produce that work list. It never writes to
full_text_screening_database.csv itself -- see update_full_text_record.py
for that -- and the queue it produces is disposable and fully
regenerable: rerun this any time to get a fresh, up-to-date queue as more
PDFs clear Phase 6.

Standard library only, consistent with this repository's existing
scrapers (see ../../../README.md).

INPUT
-----
--full-text-db : path to 02_screening/full_text/full_text_screening_database.csv
--queue-out    : path to write the queue CSV to

BEHAVIOR
--------
Includes every record with a `full_text_decision` (include or exclude)
and no `final_decision` yet -- i.e. reviewer_1 has decided but no second
reviewer has confirmed or overridden it. Sorted `include` first then
`exclude` (mirroring the title/abstract queue's priority ordering, since
includes drive extraction and are the higher-value check), most recent
year first within each group. Records with no full_text_decision yet
(not retrieved, or retrieved but not yet screened) are left out entirely
-- there is nothing for a second reviewer to check on them yet.

USAGE
-----
    python3 build_full_text_reviewer2_queue.py \\
        --full-text-db ../../02_screening/full_text/full_text_screening_database.csv \\
        --queue-out ../../02_screening/full_text/full_text_reviewer_2_queue.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

OUTPUT_FIELDS = [
    "record_id", "title", "authors", "year", "doi", "url",
    "full_text_decision", "exclusion_reason", "exclusion_reason_detail",
    "notes",
]


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--full-text-db", type=Path, required=True)
    parser.add_argument("--queue-out", type=Path, required=True)
    args = parser.parse_args()

    if not args.full_text_db.exists():
        print(f"No full-text database at {args.full_text_db} -- run init_full_text_db.py first.")
        return 0

    records = read_csv(args.full_text_db)

    decided = [
        r for r in records
        if (r.get("full_text_decision") or "").strip() in ("include", "exclude")
        and not (r.get("final_decision") or "").strip()
    ]

    def sort_key(r: dict):
        decision_rank = 0 if r.get("full_text_decision") == "include" else 1
        try:
            year = -int(r.get("year") or 0)
        except ValueError:
            year = 0
        return (decision_rank, year)

    decided.sort(key=sort_key)

    args.queue_out.parent.mkdir(parents=True, exist_ok=True)
    with args.queue_out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        for r in decided:
            writer.writerow({field: r.get(field, "") for field in OUTPUT_FIELDS})

    n_include = sum(1 for r in decided if r.get("full_text_decision") == "include")
    n_exclude = sum(1 for r in decided if r.get("full_text_decision") == "exclude")
    print(f"Wrote {len(decided)} record(s) to {args.queue_out} ({n_include} include, {n_exclude} exclude)")
    already_final = sum(1 for r in records if (r.get("final_decision") or "").strip())
    print(f"({already_final} record(s) already have a final_decision and were left out.)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
