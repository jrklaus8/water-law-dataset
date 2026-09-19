# Instructions for Claude Cowork — resolve the WoS export question, narrow HeinOnline

Paste this whole document into Claude Cowork as-is. Two separate things to
do, in order. Send everything back to the researcher when done.

## Part 1: Resolve whether the Web of Science export actually happened

There's a live contradiction that needs resolving before this project can
trust or discard `SEARCH_035` (Web of Science, ~4,058 records on the
topic-area search):

- **One account**: 5 export files (`savedrecs.txt`, `savedrecs_1.txt`,
  `savedrecs_2.txt` ×2, `savedrecs_3.txt`) were received and already
  processed into the pipeline — real-looking bibliographic data, 4,058
  unique records total, zero overlap between files, plausible Web of
  Science accession numbers (`WOS:` + 15 digits), correct journal/ISSN
  metadata, and internal fields (ResearcherID, WoS "GA" group-author
  codes) that would be very hard to fabricate at this scale.
- **A later account** (`heinonline_wos_run_log_20260911.csv`) says the
  export backend was returning a server error (HTTP 500) on every
  attempt, across every format and batch size tried, and that "no
  download was ever produced... confirmed both by checking with the
  researcher (nothing in Downloads) and by inspecting network requests."

These can't both be true as stated. Please help resolve it:

1. **Check the actual file timestamps** on `savedrecs.txt`,
   `savedrecs_1.txt`, `savedrecs_2.txt` (both copies), and
   `savedrecs_3.txt` — wherever they currently are (Downloads folder,
   wherever they were uploaded from). When were they actually created?
   If they predate the session that logged the HTTP 500 failures, that
   session's export attempts were likely a *later, separate* (failed)
   retry, and the earlier successful export is real. If no such files
   exist anywhere now, or their timestamps postdate the failure log, that
   points the other way.
2. **Check browser download history** for the Web of Science domain
   around 2026-09-11, if accessible — does it show completed downloads
   matching those filenames/sizes, or only failed/incomplete ones?
3. **Try the export again, right now.** Run the same query from
   `cowork_instructions_2026-09-11_wos_heinonline.md` (Part 1, Web of
   Science) and attempt Export → CSV → Full Record on a small batch
   first (e.g. 100 records) to check whether the HTTP 500 error is still
   happening or was transient. If it works now:
   - Compare the total result count shown to **4,058** (the count both
     the disputed files and the failure log agree the query returns) —
     does it still match?
   - If small batches now succeed, proceed to re-export the full result
     set in batches (same as before, ~1,000 at a time) and send the
     fresh files back regardless of what Part 1's investigation above
     concluded — a clean, freshly-verified export settles this
     regardless of what happened before.
   - If the export still fails, note that clearly (same detail as the
     original failure log: exact error text, which formats/batch sizes
     were tried) rather than assuming Part 1's file check is sufficient
     on its own.

Report back plainly: **do you now believe the original 5 files were a
genuine Web of Science export, or not — and what specifically tells you
that?** If a fresh export succeeded, that supersedes the question either
way; send those files.

## Part 2: Narrow HeinOnline's main search (SEARCH_036) to something exportable

The main three-clause HeinOnline search from
`cowork_instructions_2026-09-11_wos_heinonline.md` returned 71,226 hits —
far too many to hand-compile, and HeinOnline has no bulk results-list
export. Narrow it so it's actually usable. Two options, do both as
separate searches (separate `search_id`s, suggested `SEARCH_038` and
`SEARCH_039` — confirm the next free number with the researcher's Claude
Code session if these are already taken by the time you run this):

**Option A — restrict to Title field instead of Full Text**, same three
clauses:

```
Title: (sanitation OR wastewater OR sewerage OR "sewer connection" OR
"water supply" OR "piped water" OR "municipal water" OR "water connection"
OR "water service" OR "sanitation service")
AND
Title: ("administrative burden" OR "administrative barrier" OR
"administrative law" OR "legal barrier" OR eligibility OR "legal
recognition" OR "land tenure" OR "property title" OR documentation OR
"building permit" OR zoning OR formalization OR formalisation OR
regularization OR regularisation OR "administrative discretion" OR
enforcement OR "regulatory governance" OR bureaucratic)
AND
Title: (access OR connection OR coverage OR reliability OR affordability
OR exclusion OR inclusion OR "service delivery")
```

Check the result count before doing anything else. If it's still in the
thousands, this alone won't be enough — report the count and stop here
for guidance rather than guessing further.

**Option B — if Option A is still too large, split the original Full
Text search by year range** (same three Full Text clauses as the
original `SEARCH_036` string, each ANDed with a `Date: [start TO end]`
restriction) into a handful of chunks small enough that each one's hit
count is in the low hundreds — check each chunk's count before exporting.
This mirrors how the Scopus search was split by `PUBYEAR` when it proved
too large for one batch.

Whichever gets a tractable count, hand-compile the results the same way
`SEARCH_037` was done (Title, Journal, Volume/Issue, Year, Pages, Authors,
DOI, Citation, Abstract, Notes — abstract will likely be "not available"
for most, same as before) if there's no bulk export, or use a bulk export
if one turns out to be available for a filtered/narrower result set even
though it wasn't for the full 71,226.

## What to send back

For Part 1: the timestamp/history findings, and either a fresh successful
export or a clear "still failing, here's the exact error" report.

For Part 2: the result count for Option A, and either its exported/
hand-compiled records or, if still too large, a report of what was tried
and the counts at each step — same reporting discipline as
`scopus_batch_run_log_20260910.csv` (exact query run, filters, counts
before and after export, format used).
