# Reviewer 2 — Start Here

Two files, generated 2026-09-10, refreshed 2026-09-11 once `SEARCH_026`
(last of 18 planned Scopus batches) was screened, and refreshed again the
same day once `SEARCH_035` (first Web of Science batch) was screened —
from `screening_database.csv` after Claude's first-pass screening
(`reviewer_1`, tag `Claude-AI-1stpass-2026-09-10`) — see `CHANGELOG.md`
and `ai_first_pass_rationale.csv` for the full method.

## `reviewer_2_queue.csv` — the actual work

Every record `reviewer_1` marked `include` (1,710) or `unsure` (248) — 1,958
rows, `include` first then `unsure`, most recent year first within each.
For each: read the title + abstract (both included in the row, no need to
go back to `screening_database.csv`), form your own independent
`title_abstract_decision` per `INCLUSION_EXCLUSION.md`, and record it —
where exactly is your call (a `reviewer_2` column added to a copy of this
file, directly in `screening_database.csv`'s `reviewer_2` column keyed by
`record_id`, whatever's easiest to work with). `ai_rationale` is Claude's
stated reasoning for that record — useful context, but form your own
judgment rather than anchoring on it; the entire point of a second reviewer
is an independent read.

**Why `unsure` is included and no non-candidate records are**: `unsure`
means the first-pass reviewer couldn't confidently resolve the record from
title+abstract alone — genuine uncertainty, not a soft exclude. Everything
`reviewer_1` did mark `exclude` is *not* in this file; see the sample below
if you want to spot-check that side too. This is the full-review analog of
piloting only the ambiguous cases first, not a shortcut around a real
second pass — `PROTOCOL.md`'s two-reviewer requirement is for the whole
title/abstract stage, and screening only these 1,958 does not by itself
satisfy it. If your capacity is limited, this is at least the
highest-value subset to prioritize.

## `exclude_spotcheck_sample.csv` — a false-negative check, not full review

A **random** sample of 120 of the 5,151 records `reviewer_1` excluded
(~2.3%), fixed seed `20260911035` for reproducibility (anyone can
regenerate the identical sample from `screening_database.csv`). This is
standard systematic-review QA practice: spot-checking a random slice of
excludes catches a systematic false-negative pattern (e.g., a whole class
of relevant records the first pass was consistently too strict about)
that a single full pass over 5,151 records has no other way to surface
cheaply. It is **not** a substitute for reviewing the whole exclude set,
and finding zero problems in the sample doesn't certify every exclude —
it just gives some confidence the exclusion logic wasn't systematically
broken. If you find a pattern of disagreement in the sample, that's a
signal to look harder at the exclude population generally (or re-run a
full second pass over all 5,151), not to fix only the 120 sampled rows.

**Worth knowing before you start**: the Web of Science batch that landed
2026-09-11 had a much lower include/unsure rate (~13%) than the Scopus
batches (~25-30%) — expected, since WoS's broader `TS=` field pulls in
more off-topic noise and this batch is only the WoS-unique residue after
cross-database overlap with Scopus was already removed, but worth keeping
in mind if the exclude sample above reads as unusually WoS-heavy.

## Once you're done

Whatever you decide, it needs to end up somewhere `code/analysis/
validate_schemas.py` and any downstream script can find it — the cleanest
path is filling `reviewer_2` (and `conflict` where `reviewer_1` ≠
`reviewer_2`) directly in `screening_database.csv`, matched by
`record_id`. `final_decision` gets set only after conflict resolution
(`PROTOCOL.md` §"Selection process": discussion, or a third reviewer).
Nothing downstream (extraction, evidence map, any of Phase 6+) should
treat a record as settled until `final_decision` is populated.
