#!/usr/bin/env python3
"""Batch-import full-text retrieval results into the tracking database.

update_full_text_record.py handles one record at a time -- fine for a
researcher's own spot updates, but impractical for the hundreds of
records a single retrieval session (e.g. a Cowork batch working through
full_text_retrieval_queue.csv) can realistically produce results for at
once. This script applies many rows in one atomic write, with the exact
same validation and never-silently-overwrite discipline as
update_full_text_record.py and init_full_text_db.py -- see
02_screening/full_text/FULL_TEXT_README.md and
02_screening/full_text/COWORK_RETRIEVAL_INSTRUCTIONS.md for the workflow
this feeds.

Reuses init_full_text_db.py's own SCHEMA/VALID_STATUS/VALID_DECISION
constants (loaded dynamically, same pattern as
code/analysis/validate_schemas.py) rather than redeclaring them, so the
two scripts can never silently drift apart on what counts as valid.

Standard library only, consistent with this repository's existing
scrapers (see ../../../README.md).

INPUT
-----
--full-text-db : path to 02_screening/full_text/full_text_screening_database.csv
--results      : path to a results CSV with columns:
                 record_id, full_text_status, full_text_location, notes
                 (any other full_text_screening_database.csv column is
                 also accepted if present, e.g. full_text_decision,
                 exclusion_reason, exclusion_reason_detail, reviewer_1 --
                 but a plain retrieval-only batch normally has just the
                 first four)
--dry-run      : validate and report what WOULD change, write nothing

BEHAVIOR
--------
- A record_id not found in the full-text database is skipped and
  reported -- never silently dropped, never auto-added (that's
  init_full_text_db.py's job, seeded only from real Phase 5 includes).
- A record_id that already has a non-blank `final_decision` is skipped
  and reported -- a finished record is never overwritten by a later
  retrieval-only batch.
- Any row with an invalid enum value (full_text_status, full_text_decision,
  exclusion_reason) is REJECTED IN FULL, not partially applied -- the
  whole import stops with nothing written if any row fails validation,
  so a typo in row 400 of a 500-row batch can never silently corrupt the
  database with 399 good rows and one bad one. Fix the results file and
  re-run.
- Only columns actually present in the results CSV are touched on each
  row; every other field on that row in the full-text database is left
  exactly as it was.

USAGE
-----
    python3 bulk_import_full_text_results.py \\
        --full-text-db ../../02_screening/full_text/full_text_screening_database.csv \\
        --results /path/to/cowork_retrieval_results_batch01.csv \\
        --dry-run

    # once the dry run looks right:
    python3 bulk_import_full_text_results.py \\
        --full-text-db ../../02_screening/full_text/full_text_screening_database.csv \\
        --results /path/to/cowork_retrieval_results_batch01.csv
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import os
import sys
import tempfile
from pathlib import Path

csv.field_size_limit(sys.maxsize)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALID_EXCLUSION_REASON = {"", "E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12"}
VALID_CONFLICT = {"", "true", "false"}


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv_atomic(path: Path, rows: list[dict], schema: list[str]) -> None:
    fd, tmp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=schema)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(tmp_path, path)
    except BaseException:
        Path(tmp_path).unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--full-text-db", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.full_text_db.exists():
        print(f"No full-text database at {args.full_text_db}.")
        return 1
    if not args.results.exists():
        print(f"No results file at {args.results}.")
        return 1

    here = Path(__file__).resolve().parent
    init_mod = load_module(here / "init_full_text_db.py", "init_full_text_db")
    schema = init_mod.SCHEMA
    valid_status = init_mod.VALID_STATUS
    valid_decision = init_mod.VALID_DECISION

    updatable_fields = [f for f in schema if f != "record_id"]

    db_rows = read_csv(args.full_text_db)
    db_by_id = {r["record_id"]: r for r in db_rows}

    result_rows = read_csv(args.results)
    if not result_rows:
        print(f"{args.results} has no data rows -- nothing to import.")
        return 0

    incoming_fields = [f for f in result_rows[0].keys() if f in updatable_fields]
    unknown_fields = [f for f in result_rows[0].keys() if f not in schema]
    if unknown_fields:
        print(f"WARNING: results file has column(s) not in the full-text schema, ignored: {unknown_fields}")

    errors = []
    not_found = []
    already_decided = []
    to_apply = []

    for i, row in enumerate(result_rows, start=2):  # header is line 1
        rid = row.get("record_id", "").strip()
        if not rid:
            errors.append(f"line {i}: blank record_id")
            continue
        if rid not in db_by_id:
            not_found.append(rid)
            continue
        if (db_by_id[rid].get("final_decision") or "").strip():
            already_decided.append(rid)
            continue

        status = row.get("full_text_status")
        if status is not None and status.strip() not in valid_status:
            errors.append(f"line {i} ({rid}): invalid full_text_status {status!r}, must be one of {sorted(valid_status)}")
        decision = row.get("full_text_decision")
        if decision is not None and decision.strip() not in valid_decision:
            errors.append(f"line {i} ({rid}): invalid full_text_decision {decision!r}, must be one of {sorted(valid_decision)}")
        exclusion_reason = row.get("exclusion_reason")
        if exclusion_reason is not None and exclusion_reason.strip() not in VALID_EXCLUSION_REASON:
            errors.append(f"line {i} ({rid}): invalid exclusion_reason {exclusion_reason!r}")
        conflict = row.get("conflict")
        if conflict is not None and conflict.strip().lower() not in VALID_CONFLICT:
            errors.append(f"line {i} ({rid}): invalid conflict {conflict!r}, must be true/false/blank")
        final_decision = row.get("final_decision")
        if final_decision is not None and final_decision.strip() not in valid_decision:
            errors.append(f"line {i} ({rid}): invalid final_decision {final_decision!r}")

        to_apply.append((rid, row))

    if errors:
        print(f"REJECTING ENTIRE IMPORT: {len(errors)} invalid row(s) found. Nothing written.")
        for e in errors:
            print(f"  {e}")
        print("Fix the results file and re-run -- a partially-valid batch is never partially applied.")
        return 1

    print(f"Validated {len(result_rows)} row(s): {len(to_apply)} to apply, "
          f"{len(not_found)} record_id(s) not found, {len(already_decided)} already final_decision'd (skipped).")
    if not_found:
        print(f"  not found (never auto-added by this script): {not_found}")
    if already_decided:
        print(f"  already decided (left untouched): {already_decided}")

    if args.dry_run:
        print("--dry-run: no changes written.")
        return 0

    for rid, row in to_apply:
        target = db_by_id[rid]
        for field in incoming_fields:
            value = row.get(field)
            if value is not None and value != "":
                target[field] = value

    write_csv_atomic(args.full_text_db, db_rows, schema)
    print(f"Applied {len(to_apply)} update(s) to {args.full_text_db}.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
