# Full-Text Screening (Phase 6) — Start Here

`full_text_screening_database.csv` was seeded 2026-09-12 by
`code/screening/init_full_text_db.py` from every record in
`02_screening/title_abstract/screening_database.csv` with
`final_decision == "include"` — **3,659 records**, one row each, all other
fields blank. This is a separate file from the title/abstract stage's
`screening_database.csv` on purpose — see "Why a separate file" below —
and it is the single source of truth for Phase 6 going forward.

## What to do, per record

1. **Try to retrieve the full text**, then set `full_text_status`:
   - `sought` — you've started looking but don't have it yet
   - `retrieved` — you have the full text in hand
   - `not_retrievable` — you looked and genuinely could not get it (paywall
     with no institutional access, out-of-print with no digital copy, etc.)
     — this is itself a PRISMA-reportable outcome, not a failure to hide.
     Leave `full_text_decision` blank in this case; the PRISMA flow diagram
     has a dedicated "Reports not retrieved" line for exactly this.
2. **Record where the file lives** in `full_text_location` — a local file
   path, a URL, or whatever lets you (or someone auditing this review)
   find that exact PDF again. Free text, but be specific enough to be
   useful six months from now.
3. **Once retrieved, screen the full text** against `INCLUSION_EXCLUSION.md`
   and set:
   - `full_text_decision` — `include` or `exclude`
   - `exclusion_reason` — one of E01–E12 if excluded (see table below);
     blank if included
   - `exclusion_reason_detail` — unlike the title/abstract stage, you now
     have the whole document: cite the specific page, section, or passage
     that drove the exclusion, not just a restatement of the code. This is
     the main thing full-text screening can do that title/abstract
     screening couldn't.
4. **Two reviewers, same as Phase 5** (`PROTOCOL.md` §6): fill `reviewer_1`
   and, where feasible, `reviewer_2` independently. `conflict` follows the
   exact same rule as the title/abstract stage (see `DATA_DICTIONARY.md`):
   true only when `reviewer_1` made a firm `include`/`exclude` call that
   `reviewer_2` then contradicted — never when a stage is only partially
   filled in. `final_decision` is set once any conflict is resolved by
   discussion or a third reviewer, per `PROTOCOL.md`.
5. **Log every full-text exclusion** in
   `02_screening/exclusion_log/exclusion_log.csv` as well, with
   `stage=full_text` — that file already supports multiple stages via its
   `stage` column, no schema change needed.

## Standardized exclusion codes (E01–E12)

Same codes as title/abstract screening, full definitions in
`INCLUSION_EXCLUSION.md`:

| Code | Meaning |
|---|---|
| E01 | Wrong topic |
| E02 | Wrong population |
| E03 | Wrong exposure |
| E04 | Wrong outcome |
| E05 | No empirical evidence |
| E06 | Engineering only |
| E07 | Wrong service |
| E08 | Duplicate |
| E09 | Insufficient information |
| E10 | Inaccessible full text |
| E11 | Wrong jurisdiction / context |
| E12 | Wrong study design |

(E10 is the code for `not_retrievable` records if a decision is forced
without the text — but prefer leaving `full_text_decision` blank and using
`full_text_status=not_retrievable` instead, since that keeps "we never saw
it" distinct from "we saw it and it failed inclusion criteria.")

## Why a separate file

`screening_database.csv` already has an unused `full_text_decision` column
and its own `reviewer_1`/`reviewer_2`/`conflict` columns from the
title/abstract stage. Reusing them for Phase 6 was considered and
rejected: it would either overwrite the title/abstract stage's already-
recorded reviewer identities and conflict history, or require cramming two
independent stages' worth of reviewer bookkeeping into one set of columns.
`full_text_screening_database.csv` also needs fields the title/abstract
stage has no use for at all (`full_text_status`, `full_text_location`).
So: **`screening_database.csv`'s own `full_text_decision`/`reviewer_1`/
`reviewer_2`/`conflict` columns are unused and superseded going forward —
this file is authoritative for Phase 6.** See `DATA_DICTIONARY.md` for the
full schema and this note in context.

## Keeping this file in sync

`code/screening/init_full_text_db.py` is idempotent and append-only, same
design as `init_screening_db.py` for the prior stage: re-running it never
overwrites a retrieval status or decision you've already recorded, and it
only appends record_ids newly marked `final_decision == "include"`
upstream (e.g. if `exclude_spotcheck_sample.csv` review or a future
independent reviewer changes something in `screening_database.csv`). If a
record_id already in this file no longer shows `final_decision == "include"`
upstream, the script leaves your existing full-text work in place but
prints a warning — resolve that manually rather than silently deleting
work already done.

## A note on timing

The researcher has indicated a possible future independent second review
of the title/abstract stage (Phase 5) by a different assistant. That does
not block Phase 6: the 3,659-record pool this file tracks is the current,
recorded `final_decision` set, and if that upstream set changes later,
re-running `init_full_text_db.py` will pick up the delta without
disturbing any full-text work already logged here.
