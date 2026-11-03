# Instructions for Claude Cowork — next round: 5 items

Paste this whole document into Claude Cowork as-is. It covers five
separate items — work through them in order, but each stands alone, so
report back on whatever you finish even if you don't get through all
five in one session. Send files/findings back to the researcher as you
go rather than batching everything to the end.

**Before anything else, re-read the standing caution added after the
last round**: a network response (HTTP 200, an export dialog closing
normally) is **not proof a file was actually written**. For every export
below, confirm the file exists on disk with a plausible size/record
count before reporting it as done.

---

## Item 0: Recover the SEARCH_038 file (HeinOnline, Title-restricted, 3 records)

This was already produced last round but never made it back to the
researcher's Claude Code session. Find it — likely in Downloads, possibly
under a name like `SEARCH_038_HEINONLINE_2026-09-11.csv` or similar — and
send it. If it's genuinely gone, no need to re-run the search from
scratch: it was only 3 results (Title-restricted search from
`cowork_instructions_2026-09-11_followup.md` Part 2, Option A), quick to
redo — the three records were: (1) a 2006 EJIL piece on urban water
services and global administrative law, (2) a 2019 piece on the right to
basic sanitation, and (3) a Georgia state tax act that only matched
incidentally and should be flagged as likely-exclude, not silently
included.

---

## Item 1: ProQuest and Sociological Abstracts

- Library route: EUR library database list → "ProQuest" (Sociological
  Abstracts is usually a sub-database selectable within ProQuest, or
  filter the search to include it).
- Search interface: Advanced Search, command-line query box.

**Main search** (log as `SEARCH_039`):

```
noft(sanitation OR wastewater OR sewerage OR "sewer connection*" OR "water
supply" OR "piped water" OR "municipal water" OR "water connection*" OR
"water service*" OR "sanitation service*" OR WASH)
AND
noft("administrative burden" OR "administrative barrier*" OR
"administrative law" OR "legal barrier*" OR eligibility OR "legal status"
OR "legal recognition" OR "land tenure" OR "property title" OR
documentation OR "building permit*" OR zoning OR formalization OR
formalisation OR regularization OR regularisation OR "service area*" OR
"administrative discretion" OR accommodation OR enforcement OR regulation
OR "regulatory governance" OR governance OR institutional* OR bureaucratic)
AND
noft(access OR connection OR coverage OR reliability OR affordability OR
exclusion OR inclusion OR inequality OR inequity OR "service delivery")
```

(`noft` = "anywhere except full text" — if searching interactively rather
than pasting into the command-line box, use that field picker instead.)

**Second, narrower search specifically for Sociological Abstracts** (log
as its own `search_id`, `SEARCH_040`, do not merge into the main
results): restricted to the platform's own controlled-vocabulary
thesaurus terms — e.g. "public utilities", "water resources",
"bureaucracy", "administrative agencies" — to catch records indexed on
subject rather than keyword. Use whatever thesaurus/subject-term picker
the interface offers; there's no single fixed string for this the way
there is for the main search, since it depends on ProQuest's actual
thesaurus term list — pick the closest matches to those four example
terms.

**Export**: select all → "Export/Save" → **RIS** if offered (an adapter
already exists for RIS and is validated against real HeinOnline/WoS-style
data) → include **Abstract** in the field selection. CSV also works if
RIS isn't available — say which you used.

---

## Item 2: JSTOR and SSRN

(Not Google Scholar — it has no bulk export at all; skip it unless the
researcher asks for the manual relevance-ranked approach separately.)

### JSTOR (log as `SEARCH_041`)

- Library route: EUR library database list → "JSTOR."
- Advanced Search, stacked-field Boolean:

```
((sanitation OR wastewater OR "water supply" OR "water connection" OR
"sewer connection") AND ("administrative burden" OR "administrative
barrier" OR "legal recognition" OR "land tenure" OR eligibility OR
"regulatory governance" OR bureaucratic) AND (access OR connection OR
exclusion OR inclusion OR "service delivery"))
```

Note: JSTOR doesn't support `*` truncation beyond `?` (single character)
in most interfaces — the string above already spells out variants rather
than truncating, don't add `*` yourself.

### SSRN (log as `SEARCH_042`)

- Library route: EUR library database list → "SSRN" (or access directly
  if EUR doesn't broker it — SSRN is often freely searchable).
- Basic keyword search:

```
("water connection" OR "sanitation access" OR "water access") AND
("administrative burden" OR "legal recognition" OR "administrative
barrier" OR "regulatory governance" OR "land tenure")
```

- SSRN is mostly working papers/preprints — **expect real overlap with
  papers already captured via Scopus/WoS**, which the pipeline's
  deduplication will catch (DOI match first, title/year match second).
  This is expected and useful, not a sign of a bad search.

**Export for both**: RIS if offered (same shared adapter as Item 1),
include abstract if the platform offers one. If neither export is
available and result counts are small, hand-compile the same way
`SEARCH_037` was done (Title, Journal/Source, Year, Authors, DOI,
Citation, Abstract, Notes).

---

## Item 3: Investigate Westlaw and Lexis — recon only, don't run the full search yet

Neither platform has a standard bulk CSV/RIS export the way the others
do, so no adapter exists yet for either. Before running the actual
search:

1. Log into Westlaw and/or Lexis+ via the EUR library route.
2. Run a **small, throwaway test search** (anything on-topic, doesn't
   need to be the real query) restricted to Secondary Sources / Law
   Reviews & Journals.
3. Find whatever "Download," "Export," or "Send to" option exists on the
   results list, and actually try it on a handful of results.
4. **Report back exactly what format comes out** — Word/RTF citation
   list? PDF? CSV? Does it include an abstract/summary? Is there a bulk
   "export all results" option or only per-selected-item export?

This determines whether a real adapter can be built at all, or whether
these two need the same hand-compile fallback as HeinOnline's oversized
search. Don't spend time running the full three-clause query
(`database_strategies/westlaw_lexis.md` has it, for later) until this
format question is answered — building on a guessed format would violate
this project's "never invent structure it hasn't verified" rule.

---

## Item 4: Not a Cowork task — flagging for awareness

The researcher has 1,958 candidate records (`reviewer_2_queue.csv`)
waiting on a **human** second-reviewer pass — this is a core part of the
project's methodology (`PROTOCOL.md`'s two-reviewer requirement) and
isn't something to delegate to an AI search session. No action needed
here from Cowork; just flagging it exists so it isn't lost among the
database-search tasks above. The researcher may choose to pause new
searches to work through it, or keep searching in parallel — that's
their call, not something this prompt needs to resolve.

---

## Reporting discipline (same as every prior round)

For each search actually run, report: exact query string run, filters
applied, total result count shown by the platform **before** export,
records actually in the export, export format, fields exported
(abstract included or not, and why if not), and anything that didn't go
as expected. Confirm each export file exists on disk (Item 0's caution)
before calling it done.
