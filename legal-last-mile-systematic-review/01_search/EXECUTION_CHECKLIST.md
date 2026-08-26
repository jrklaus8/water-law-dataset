# Execution Checklist — Running a Real Search and Getting It Back to Claude

Purpose: a literal, no-judgment-calls checklist for actually running one of
the searches in `database_strategies/` through your EUR institutional
access and getting the result back into this pipeline. Written so it can
be followed by you directly, or handed to Claude Cowork (or anyone else)
without needing the rest of this repo's context.

**Start with just one database.** Recommended: **Scopus** — cleanest
export format, most standardized UI, and it's the string already refined
as this project's pilot search. Once one file makes it through the
pipeline successfully, repeat the same pattern for the others.

## The one thing that matters most: export the abstract, not just the citation

Every export format below has a field-selection step. **Always include the
abstract if the platform offers it.** Everything Claude has done in this
project so far has been title-only, because nothing else was reachable —
an export with real abstracts is the single biggest upgrade this project
can get, since it turns "title-only triage" into real title/abstract
screening per `INCLUSION_EXCLUSION.md`. If a field-selection screen offers
a checkbox for "Abstract," "Abstract & Keywords," or "Complete record,"
take it, even if it makes the file bigger.

## General pattern (applies to every database below)

1. Go in through **EUR's library database list**, not the database's own
   homepage directly (e.g. not scopus.com, not westlaw.com) — institutional
   access is almost always brokered through the library's own portal or a
   proxy link, and going direct usually won't recognize your access. Search
   the EUR library site for the database by name (e.g. "Scopus") and use
   the link it gives you.
2. Log in with your EUR SSO if prompted.
3. Use the database's **Advanced Search** (not the plain search box) so the
   Boolean structure survives.
4. Paste the exact string from the matching file in `database_strategies/`
   — copied verbatim below for the first one, referenced by path for the
   rest.
5. Run it. Note the total result count somewhere (you'll need it for step
   8).
6. Export **all results**, not just the first page — most platforms have an
   "export all" or "select all X results" option distinct from "export
   selected." If the platform caps bulk export (e.g. at 500 or 2000
   records), export in that many batches rather than truncating silently,
   and say so when you send the files.
7. Export format: **CSV** if offered; otherwise **RIS** or **BibTeX** — any
   of these three works, just say which one you used.
8. **Save the file with this name:**
   `SEARCH_0NN_<DATABASE>_2026-08-25.csv` (or `.ris` / `.bib`), e.g.
   `SEARCH_018_SCOPUS_2026-08-25.csv` — the next unused number is
   `SEARCH_018` (check `search_logs/search_log.csv` if more searches have
   happened since this checklist was written; the highest `SEARCH_0NN` used
   so far is `SEARCH_017`, plus one non-search log row).
9. Send the file back — either commit it to `01_search/raw_exports/` in
   this repo yourself, or just hand it to Claude directly (upload, paste
   the path, whatever's easiest). Also tell Claude: the exact search string
   you actually ran (copy-paste, not paraphrased), any filters you applied
   (date range, document type, language), and the total result count before
   export. This is exactly the `search_log.csv` row — see
   `SEARCH_PROTOCOL.md` §6 — and Claude will need it to log the search
   properly rather than treating the file as anonymous data.

## Scopus — batch plan for the remaining ~4,944 records

The first Scopus run (`SEARCH_018`, 2026-08-26) only captured 500 of the
~5,444 total matching records, and missed the Abstract field. See
[`scopus_batch_plan_2026-08-26.md`](scopus_batch_plan_2026-08-26.md) for
16 ready-to-paste batch queries (split by year, sized against the real
result distribution) to get the rest — start there instead of the section
below if you're returning to finish Scopus specifically.

## Scopus (recommended first)

- Library route: EUR library database list → "Scopus."
- Search interface: Advanced Search (there's a toggle/tab for it near the
  basic search box).
- String to paste (verbatim, also in `database_strategies/scopus.md`):

```
TITLE-ABS-KEY(
  sanitation OR wastewater OR sewerage OR "sewer connection*" OR
  "water supply" OR "piped water" OR "municipal water" OR
  "water connection*" OR "water service*" OR "sanitation service*" OR WASH
)
AND
TITLE-ABS-KEY(
  "administrative burden" OR "administrative barrier*" OR
  "administrative law" OR "legal barrier*" OR eligibility OR
  "legal status" OR "legal recognition" OR "land tenure" OR
  "property title" OR documentation OR "building permit*" OR zoning OR
  formalization OR formalisation OR regularization OR regularisation OR
  "service area*" OR "administrative discretion" OR accommodation OR
  enforcement OR regulation OR "regulatory governance" OR governance OR
  institutional* OR bureaucratic
)
AND
TITLE-ABS-KEY(
  access OR connection OR coverage OR reliability OR affordability OR
  exclusion OR inclusion OR inequality OR inequity OR "service delivery"
)
```

- Export: select all results → "Export" → format **CSV** → in the field
  picker, tick **Abstract** (and Author Keywords, if offered) in addition
  to the default citation fields.
- No date range or document-type filter needed for this first pilot — run
  it as-is. If the result count is enormous (a few thousand+), that's fine,
  just export all of it in batches per the general step 6 above.

## Web of Science

- Library route: EUR library database list → "Web of Science."
- Search interface: Advanced Search, using `TS=` (Topic) field.
- String: `database_strategies/wos.md` (same three concept blocks, `TS=`
  syntax instead of `TITLE-ABS-KEY`).
- Export: "Export" → **CSV** (or "Tab-delimited" if CSV isn't offered) →
  field set "Full Record" if available (this includes the abstract) rather
  than the default "Author, Title, Source" set.

## HeinOnline

- Library route: EUR library database list → "HeinOnline."
- Search interface: Advanced Search / Search within a specific library
  (Law Journal Library).
- Approach: `database_strategies/heinonline.md` recommends three separate
  fielded clauses ANDed together rather than one long string — HeinOnline's
  basic search bar doesn't handle deep Boolean nesting well.
- Export: HeinOnline typically exports per-document (download PDF/citation)
  rather than bulk CSV of a whole result set — if there's no bulk export,
  instead export/copy the results list as a simple text or CSV of
  title/author/citation for each hit, and note in your message to Claude
  that abstracts likely aren't available this way (law review articles
  often don't have them anyway).

## Westlaw / Lexis

- Library route: EUR library database list → "Westlaw" and/or "Lexis+"
  (may be separate entries).
- String: `database_strategies/westlaw_lexis.md` — note the two platforms
  use different connector syntax (`&`/`/p` for Westlaw, `AND`/`W/n` for
  Lexis) — use the block matching whichever platform you're in.
- Restrict to **Secondary Sources / Law Reviews & Journals** if the
  interface offers that scope (both platforms usually do) — this avoids
  mixing in primary case law and statutes, which aren't "studies" for this
  review.
- Export: both platforms support exporting a result list to CSV or Excel
  via a "Download" or "Export" option in the results toolbar.

## ProQuest / Sociological Abstracts

- Library route: EUR library database list → "ProQuest" (Sociological
  Abstracts is usually a sub-database selectable within ProQuest, or filter
  the search to include it).
- String: `database_strategies/proquest_sociological_abstracts.md`.
- Export: select all → "Export/Save" → **RIS** or **CSV** → include
  "Abstract" in the field selection.

## What happens once Claude has the file

1. If it's not already CSV, Claude converts/reads the RIS or BibTeX
   directly.
2. Claude normalizes it to this project's common schema (title, authors,
   year, doi, url, database, search_id) — writing a new per-database
   adapter if one doesn't exist yet (`code/search/adapters/`), the same way
   `pubmed_adapter.py` was built.
3. The file goes in `01_search/raw_exports/` under the name from step 8
   above, and a row goes in `search_logs/search_log.csv`.
4. `code/search/deduplicate.py` runs against everything in
   `raw_exports/` together, including the existing WebSearch-pilot data —
   real duplicates across the two sources get caught for the first time.
5. `code/screening/init_screening_db.py` merges the new unique records into
   `02_screening/title_abstract/screening_database.csv`.
6. If abstracts came through, Claude can do real title/abstract screening
   against `INCLUSION_EXCLUSION.md` for the first time in this project —
   actual `include`/`exclude`/`unsure` decisions, not the title-only triage
   memo this has been limited to so far.

That last point is the actual payoff: one real export with abstracts moves
this project from "candidates identified" to "records actually screened,"
which is the first result that means anything for the review itself.
