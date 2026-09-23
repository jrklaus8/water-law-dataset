#!/usr/bin/env python3
"""Report current Phase 6 (full-text screening) progress.

Reads full_text_screening_database.csv and prints counts by retrieval
status and by decision -- the same numbers PRISMA_WORKFLOW.md and
06_outputs/prisma/prisma_flow.md need for their "Reports sought for
retrieval" / "Reports not retrieved" / "Reports assessed for eligibility"
/ exclusion-by-reason lines. This script only reads and reports; it never
writes to the database. Update those two docs by hand from its output --
per prisma_flow.md's own instruction, re-derive rather than hand-edit
counts when the underlying data changes.

Standard library only, consistent with this repository's existing
scrapers (see ../../../README.md).

USAGE
-----
    python3 full_text_progress.py --full-text-db ../../02_screening/full_text/full_text_screening_database.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(sys.maxsize)


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--full-text-db", type=Path, required=True)
    args = parser.parse_args()

    if not args.full_text_db.exists():
        print(f"No full-text database at {args.full_text_db}.")
        return 1

    rows = read_csv(args.full_text_db)
    total = len(rows)

    status_counts = Counter((r.get("full_text_status") or "not_started") for r in rows)
    decision_counts = Counter((r.get("full_text_decision") or "undecided") for r in rows)
    final_counts = Counter((r.get("final_decision") or "undecided") for r in rows)
    exclusion_counts = Counter(r.get("exclusion_reason") for r in rows if (r.get("exclusion_reason") or "").strip())
    open_conflicts = [r["record_id"] for r in rows
                       if (r.get("conflict") or "").strip().lower() == "true"
                       and not (r.get("final_decision") or "").strip()]

    print(f"Full-text database: {total} record(s) total (seeded from Phase 5's final_decision == 'include' pool)\n")

    print("Retrieval status:")
    for status in ["not_started", "sought", "retrieved", "not_retrievable"]:
        print(f"  {status}: {status_counts.get(status, 0)}")

    print("\nFull-text decision:")
    for decision in ["undecided", "include", "exclude"]:
        print(f"  {decision}: {decision_counts.get(decision, 0)}")

    print("\nfinal_decision:")
    for decision in ["undecided", "include", "exclude"]:
        print(f"  {decision}: {final_counts.get(decision, 0)}")

    if exclusion_counts:
        print("\nExclusions by reason (E01-E12):")
        for code in sorted(exclusion_counts):
            print(f"  {code}: {exclusion_counts[code]}")

    if open_conflicts:
        print(f"\nWARNING: {len(open_conflicts)} record(s) marked conflict=true with no final_decision yet -- unresolved: {open_conflicts}")

    print(f"\nPRISMA-line values as of now:")
    print(f"  Reports sought for retrieval (n = {total})")
    print(f"  Reports not retrieved (n = {status_counts.get('not_retrievable', 0)})")
    print(f"  Reports assessed for eligibility (n = {decision_counts.get('include', 0) + decision_counts.get('exclude', 0)})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
