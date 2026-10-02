# Instructions for Claude Cowork — round 3: decisions made, finish the exports

Paste this whole document into Claude Cowork as-is. Two open questions
from last round have been decided by the researcher — this picks up
from there. Standing caution still applies: **confirm every export
against the actual file on disk, not a network status code or a closing
dialog.**

---

## Item A: Send the three files already produced but not yet delivered

None of these made it to the researcher's Claude Code session last
round — only the run log describing them did. Find and send:

1. `SEARCH_038_HEINONLINE_2026-09-11.csv` (3 HeinOnline records)
2. The 100-record ProQuest RIS export (`SEARCH_039`) — likely still
   sitting under a random-GUID `.tmp` filename in Downloads per last
   round's note; check recently-modified files if a filename search
   doesn't turn it up
3. The 7-record JSTOR RIS export (`SEARCH_041`) — same GUID-filename
   caveat

If any of these are genuinely lost, say so plainly rather than
re-guessing — they're small enough to redo quickly if needed (the exact
queries are already in `search_log.csv`).

---

## Item B: ProQuest — full export, once the account exists

**Decision: the researcher is creating a personal ProQuest "My Research"
account** to unlock the documented 20,000-record bulk export (the
guest/no-account path caps at ~100-200 records per session and isn't
viable for the full 8,137).

- If the account already exists and is logged in by the time you read
  this: run the full export of all 8,137 results from `SEARCH_039`'s
  query (same string, same 16-sub-database selection) via the "My
  Research" bulk export option. RIS format, include Abstract, same as
  before.
- If the account doesn't exist yet: **don't attempt this yet** — you
  can't create the account or enter a password on the researcher's
  behalf. Move on to Items C and D and come back to this once the
  researcher confirms the account is ready.
- Also run `SEARCH_040` (the Sociological-Abstracts-specific
  controlled-vocabulary search — thesaurus terms like "public
  utilities," "water resources," "bureaucracy," "administrative
  agencies," per `database_strategies/proquest_sociological_abstracts.md`)
  once the account unblocks bulk export — it was held back last round
  pending exactly this.

---

## Item C: JSTOR — finish exporting the full 356, don't widen further

**Decision: accept the narrower Subject:Law-filtered JSTOR search
(356 results) as a supplementary source** — don't run additional
subject-filtered sub-searches to widen it further. What's still needed:
export the **full 356**, not just the 7-record sample already pulled.

No bulk "select all" exists on JSTOR, so this means manually checking
items across the ~15 pages (25/page) of the already-filtered result set
(All Content, Subject: Law, the trimmed 3-clause query already run) and
exporting in multi-item batches via Cite → Export a RIS file. Same
caveats as before apply and don't need re-verifying: no abstract field
will be present in JSTOR's RIS export regardless, and exported files
land under random-GUID filenames — confirm each batch on disk before
moving to the next.

---

## Item D: SSRN (not yet attempted)

- Library route: EUR library database list → "SSRN" (or access directly
  if EUR doesn't broker it — SSRN is often freely searchable).
- Basic keyword search:

```
("water connection" OR "sanitation access" OR "water access") AND
("administrative burden" OR "legal recognition" OR "administrative
barrier" OR "regulatory governance" OR "land tenure")
```

- Log as `SEARCH_042`.
- Expect real overlap with papers already captured via Scopus/WoS/
  ProQuest — SSRN is mostly working papers/preprints, and the
  pipeline's deduplication (DOI match first, title/year match second)
  will catch that overlap. Expected, not a problem.
- Export: RIS if offered (same shared adapter as HeinOnline/ProQuest),
  abstract included if available. Hand-compile if export isn't
  available and the result count is small.

---

## Item E: Westlaw/Lexis — recon only, still pending from last round

If you haven't gotten to this yet: log into Westlaw and/or Lexis+ via
the EUR library route, run a small throwaway test search restricted to
Secondary Sources / Law Reviews & Journals, and find whatever
"Download"/"Export"/"Send to" option exists on the results list. Try it
on a handful of results and report back **exactly what format comes
out** (Word/RTF? PDF? CSV? Does it include an abstract/summary? Bulk
export or only per-item?). Don't run the full three-clause query yet —
this is purely to determine whether an adapter can be built at all
before committing to a real search on a guessed format.

---

## Reporting discipline (same as every round)

For each item: exact query/filters used, total count shown by the
platform before export, records actually in the export, export format,
fields exported (abstract included or not, and why if not), and
anything that didn't go as expected. Confirm every export file exists on
disk before reporting it as done — this has mattered twice already this
project.
