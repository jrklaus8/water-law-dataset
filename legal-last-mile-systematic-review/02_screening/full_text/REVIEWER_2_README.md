# Reviewer 2 — Full-Text Screening (Phase 6) — Start Here

This mirrors `02_screening/title_abstract/REVIEWER_2_README.md`, adapted
to full-text screening. **Not yet needed by anyone** — a human `reviewer_2`
for this phase has not been assigned; the queue below exists so that when
the researcher is ready to assign one, the tooling is instant rather than
something to build from scratch. Regenerate any time with:

```
python3 code/screening/build_full_text_reviewer2_queue.py \
    --full-text-db 02_screening/full_text/full_text_screening_database.csv \
    --queue-out 02_screening/full_text/full_text_reviewer_2_queue.csv
```

## `full_text_reviewer_2_queue.csv` — the actual work

Every record `reviewer_1` (Claude, tag `Claude-AI-fulltext-2026-09-12`)
has decided (`include` or `exclude`) via full-text reading, that does not
yet have a `final_decision` — as of this generation, **175 records: 85
include, 90 exclude**, include first then exclude, most recent year first
within each. For each: read the full text yourself (the researcher's own
PDF, or the record's DOI/URL if institutional access is available — this
environment cannot fetch full texts), form your own independent
`full_text_decision` and, if excluding, an `exclusion_reason` (E01–E12,
per `INCLUSION_EXCLUSION.md`), and record it. `exclusion_reason_detail`
and `notes` carry Claude's stated reasoning for that record — useful
context for what to check, but form your own judgment rather than
anchoring on it; the entire point of a second reviewer is an independent
read.

**Unlike the title/abstract stage, there is no `unsure` category at
full-text**: `update_full_text_record.py` only accepts `include` or
`exclude` for `full_text_decision` — a genuinely ambiguous full-text read
should stay unresolved (no decision recorded) rather than being forced
into either bucket, per the standing "no fabrication/no forced closure"
rule in `PROJECT_SPEC.md` §14.

**Includes are the higher-value check, and not only because they drive
extraction (Phase 8) directly**: every include reviewed here has *also*
already been extracted into `extraction_database.csv` against
`CODEBOOK.md`'s 92-field schema. If a second reviewer's independent read
overturns an include, that is not just a screening correction — the
corresponding `S0xx` extraction row, and any `evidence_map.csv` row
derived from it, need to be removed or flagged too. Check
`extraction_database.csv`'s `source_document` field (or just the
`record_id` cross-reference maintained informally in extraction notes) to
find the matching `study_id` before deciding a disagreement is purely a
screening-level matter.

## Once you're done

Fill `reviewer_2` (and `conflict` where `reviewer_1` ≠ `reviewer_2`)
directly in `full_text_screening_database.csv`, matched by `record_id` —
`code/screening/update_full_text_record.py --record-id <id> --reviewer-2
<name> --conflict true|false` handles this without hand-editing the CSV.
`final_decision` gets set only after conflict resolution (discussion, or
a third reviewer), same rule as the title/abstract stage. Nothing
downstream should treat a record as doubly-confirmed until
`final_decision` is populated — but note that Phase 8 extraction has
already proceeded on `full_text_decision` alone, at the researcher's
explicit instruction to extract every include as it clears Phase 6 rather
than waiting for a second reviewer (`PRISMA_WORKFLOW.md` Phase 7). That
was a deliberate, disclosed methodological choice, not an oversight — but
it does mean a reviewer_2 disagreement on an include is not merely
theoretical until this queue is actually worked.
