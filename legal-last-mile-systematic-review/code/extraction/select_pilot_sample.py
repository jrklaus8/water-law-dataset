#!/usr/bin/env python3
"""Select the ~10-study pilot sample for Phase 7 (pilot extraction).

PROTOCOL.md S6 and PRISMA_WORKFLOW.md Phase 7 require piloting the
extraction codebook/form on a small sample before full extraction. This
script draws that sample from every full-text record already decided
`include` (02_screening/full_text/full_text_screening_database.csv),
stratified by source database (proportional, largest remainders
distributed by database size) so the pilot isn't unconsciously skewed
toward whichever database happened to be easiest to retrieve full text
for. A fixed seed makes the exact sample reproducible and auditable, the
same practice already used for exclude_spotcheck_sample.csv (see
DATA_DICTIONARY.md).

Refuses to draw a sample smaller than requested -- prints how many
records are actually available instead of silently shrinking the pilot,
since a pilot too small to be meaningful is worse than no pilot yet.

Standard library only, consistent with this repository's existing
scrapers (see ../../../README.md).

INPUT
-----
--full-text-db : path to 02_screening/full_text/full_text_screening_database.csv
--screening-db : path to 02_screening/title_abstract/screening_database.csv
                 (used only to look up each record's source `database`)
--pilot-out    : path to write the pilot sample list to
--n            : pilot size (default 10, per PROTOCOL.md S6)
--seed         : fixed seed for reproducibility (default 20260912, this
                 script's write date -- change only if a documented
                 re-draw is needed, and log why in CHANGELOG.md)

USAGE
-----
    python3 select_pilot_sample.py \\
        --full-text-db ../../02_screening/full_text/full_text_screening_database.csv \\
        --screening-db ../../02_screening/title_abstract/screening_database.csv \\
        --pilot-out ../../03_extraction/extraction_form/pilot_sample.csv \\
        --n 10
"""
from __future__ import annotations

import argparse
import csv
import random
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

OUTPUT_FIELDS = ["record_id", "database", "title", "authors", "year", "doi", "url"]

DEFAULT_SEED = 20260912


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def stratified_sample(included: list[dict], database_by_id: dict, n: int, seed: int) -> list[dict]:
    by_database: dict[str, list[dict]] = {}
    for rec in included:
        db = database_by_id.get(rec["record_id"], "unknown")
        by_database.setdefault(db, []).append(rec)

    total = len(included)
    rng = random.Random(seed)

    # Largest-remainder apportionment so each database's pilot share is
    # proportional to its share of the included pool, summing to exactly n.
    raw_shares = {db: len(recs) * n / total for db, recs in by_database.items()}
    base_shares = {db: int(share) for db, share in raw_shares.items()}
    remainder = n - sum(base_shares.values())
    remainders_sorted = sorted(raw_shares, key=lambda db: raw_shares[db] - base_shares[db], reverse=True)
    for db in remainders_sorted[:remainder]:
        base_shares[db] += 1

    sample = []
    for db, recs in by_database.items():
        k = min(base_shares.get(db, 0), len(recs))
        sample.extend(rng.sample(recs, k))
    return sample


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--full-text-db", type=Path, required=True)
    parser.add_argument("--screening-db", type=Path, required=True)
    parser.add_argument("--pilot-out", type=Path, required=True)
    parser.add_argument("--n", type=int, default=10)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()

    if not args.full_text_db.exists():
        print(f"No full-text database at {args.full_text_db} -- nothing to sample from.")
        return 0

    full_text_records = read_csv(args.full_text_db)
    included = [r for r in full_text_records if (r.get("final_decision") or "").strip() == "include"]
    database_by_id = {r["record_id"]: r.get("database", "") for r in read_csv(args.screening_db)}

    if len(included) < args.n:
        print(f"Only {len(included)} full-text record(s) currently have final_decision == 'include' "
              f"-- fewer than the requested pilot size of {args.n}.")
        print("Refusing to draw a pilot sample this small silently. Either wait for more full-text "
              "decisions (see 02_screening/full_text/FULL_TEXT_README.md), or explicitly decide with "
              "the researcher to pilot on fewer studies and document that decision in CHANGELOG.md.")
        return 0

    sample = stratified_sample(included, database_by_id, args.n, args.seed)

    args.pilot_out.parent.mkdir(parents=True, exist_ok=True)
    with args.pilot_out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        for r in sample:
            writer.writerow({
                "record_id": r["record_id"],
                "database": database_by_id.get(r["record_id"], ""),
                "title": r.get("title", ""),
                "authors": r.get("authors", ""),
                "year": r.get("year", ""),
                "doi": r.get("doi", ""),
                "url": r.get("url", ""),
            })

    print(f"Drew {len(sample)} pilot record(s) from {len(included)} eligible, seed={args.seed}, "
          f"stratified by database. Written to {args.pilot_out}")
    print("See 03_extraction/extraction_form/PILOT_EXTRACTION.md for what to do next.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
