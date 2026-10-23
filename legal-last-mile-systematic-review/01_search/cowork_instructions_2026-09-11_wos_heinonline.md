# Instructions for Claude Cowork — Web of Science and HeinOnline searches

Paste this whole document into Claude Cowork as-is. It is self-contained —
you do not need repository access to follow it, just EUR institutional
access through a browser. When you're done, send the export file(s) and
your filled-in report back to the researcher (who will hand them to the
Claude Code session running "The Legal Last Mile" systematic review
pipeline).

## What this is for

A systematic review needs its searches run on real, structured databases
through institutional access this automated pipeline cannot reach itself.
Scopus is done (18 batches, ~5,984 records). This is the next database:
**Web of Science**, then **HeinOnline**. Same three-concept Boolean
search as Scopus, adapted to each platform's own syntax.

## The one rule that matters most

**Always include the abstract in the export, if the platform offers it.**
Every field-selection screen below has this option somewhere — take it
even if it makes the file bigger. Without it, none of what you find can
be properly screened.

---

## Part 1: Web of Science

### Setup

1. Go through **EUR's library database list** (not wokinfo.com or
   webofscience.com directly) — search the library site for "Web of
   Science" and use the link it gives you. Log in with EUR SSO if
   prompted.
2. Use **Advanced Search**, not the plain search box — look for a tab or
   toggle labeled "Advanced Search" near the basic search bar.

### The search string

Paste this into the Advanced Search query box exactly as written. The
`TS=` field searches Topic (title, abstract, author keywords, and
Keywords Plus together):

```
TS=(
  sanitation OR wastewater OR sewerage OR "sewer connection*" OR
  "water supply" OR "piped water" OR "municipal water" OR
  "water connection*" OR "water service*" OR "sanitation service*" OR WASH
)
AND
TS=(
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
TS=(
  access OR connection OR coverage OR reliability OR affordability OR
  exclusion OR inclusion OR inequality OR inequity OR "service delivery"
)
```

### Before you run it

- **Restrict to Web of Science Core Collection**, and within that,
  explicitly select these indexes if the interface lets you choose:
  SCI-EXPANDED, SSCI, A&HCI, ESCI. Different index combinations return
  different results, so note exactly which ones you had selected.
- `TS=` is broader than Scopus's `TITLE-ABS-KEY` (it also searches
  Keywords Plus), so **expect a noticeably higher raw hit count than
  Scopus got for the same three concept blocks (~5,984 total)**. That is
  expected, not a sign the string is wrong — don't treat the two
  databases' counts as directly comparable.

### Run it and note the count

Run the search. Before exporting anything, **write down the total result
count Web of Science shows** — you'll need it for the report below.

### Export

1. Select all results (not just the visible page — look for "Select all
   [N]" or similar).
2. Click **Export** → **CSV** (if CSV isn't offered, use "Tab-delimited
   (Win)" or "Tab-delimited (Mac)" instead — say which one you used).
3. **Field set: choose "Full Record" (or "Full Record and Cited
   References" if that's the only option that includes the abstract) —
   NOT the default "Author, Title, Source" set**, which omits the
   abstract entirely.
4. If Web of Science caps a single export (e.g. at 500 or 1,000 records)
   and your result count exceeds that cap, **export in that many batches
   rather than truncating silently** — e.g. by adding a `PY=` year range
   to the query to split it into chunks, similar to how the Scopus search
   was split by year when it exceeded that platform's practical export
   size. Say clearly how you split it if you do.
5. Save the file(s). Suggested name:
   `SEARCH_035_WOS_2026-09-11.csv` (or `SEARCH_035a_WOS_2026-09-11.csv`,
   `SEARCH_035b_...`, etc. if split into batches — the researcher's
   Claude Code session will confirm/adjust the numbering if `035` is no
   longer the next free one by the time this runs).

---

## Part 2: HeinOnline

### Setup

1. Go through **EUR's library database list**, search for "HeinOnline,"
   use the link it gives you, log in with EUR SSO if prompted.
2. Use **Advanced Search** within the **Law Journal Library** (or
   whichever HeinOnline library/collection the EUR subscription covers
   for law journals) — not the plain search box. HeinOnline's basic
   search bar doesn't handle deep Boolean nesting well, so this search is
   run differently from Scopus/WoS: as **three separate fielded clauses,
   ANDed together via the Advanced Search builder**, not one long pasted
   string.

### The three clauses

Add each of these as its own field row in the Advanced Search builder
(Full Text field for each, unless noted), combined with **AND** between
rows:

**Clause 1 (service):**
```
sanitation OR wastewater OR sewerage OR "sewer connection" OR "water
supply" OR "piped water" OR "municipal water" OR "water connection" OR
"water service" OR "sanitation service"
```

**Clause 2 (mechanism):**
```
"administrative burden" OR "administrative barrier" OR "administrative
law" OR "legal barrier" OR eligibility OR "legal recognition" OR "land
tenure" OR "property title" OR documentation OR "building permit" OR
zoning OR formalization OR formalisation OR regularization OR
regularisation OR "administrative discretion" OR enforcement OR
"regulatory governance" OR bureaucratic
```

**Clause 3 (outcome):**
```
access OR connection OR coverage OR reliability OR affordability OR
exclusion OR inclusion OR "service delivery"
```

Run this as its own search — log it as one `search_id` (suggested:
`SEARCH_036`).

### Second, narrower search (do this too, don't skip it)

HeinOnline is a full-text law-journal archive, so the search above will
catch a lot of noise from incidental word co-occurrence — precision here
will be lower than Scopus/WoS. Also run a **second, Title-restricted**
search using only the narrower legal-mechanism terms combined with
water/sanitation terms, to surface doctrinal/legal-scholarship pieces the
full-text search would otherwise bury:

```
Title field: ("administrative burden" OR "legal recognition" OR
"regularização fundiária" OR "aansluitplicht") AND (water OR sanitation)
```

Log this as its own `search_id` (suggested: `SEARCH_037`) — do not merge
its results into the first search's file.

### Run it and note the count

For **each** of the two searches above, write down the total result count
HeinOnline shows before you export.

### Export

HeinOnline typically does **not** offer a bulk CSV export of an entire
result set the way Scopus/WoS do — exporting is usually per-document
(download citation / download PDF). Handle it like this:

1. Check first whether the results list has any "Export results,"
   "Download list," or "Export to Excel/CSV" option — some HeinOnline
   collections do have this for search results specifically (distinct
   from single-document export). If it exists, use it, with abstract
   included if offered.
2. **If no bulk export exists**: export/copy the results list as a
   simple table (title, author, journal, year, citation, link) into a
   CSV yourself — e.g. via "Cite: Export" per result if the list is
   short enough, or by copying the results-list text and reformatting
   it into rows. Note clearly in your report that this search likely
   has **no abstracts** either way (HeinOnline citation exports usually
   don't carry one, and many law review articles don't have a
   structured abstract at all) — that's expected, not a mistake, this
   just means this search's records will get title-only screening
   rather than title/abstract screening, same as this project's first
   Scopus batch before abstracts were added.
3. Save the file(s):
   `SEARCH_036_HEINONLINE_2026-09-11.csv` (main search) and
   `SEARCH_037_HEINONLINE_2026-09-11.csv` (title-restricted search).

---

## What to send back — for EACH search you ran (WoS, HeinOnline main, HeinOnline title-only)

Send the export file(s), plus this information for each one (a short
list or table is fine):

- `search_id` used (or your best guess at the next free number — it'll
  get confirmed/renumbered if needed)
- Database (Web of Science / HeinOnline)
- Exact date you ran it
- Exact search string/clauses actually run (copy-paste, not paraphrased)
- Any filters applied (index selection for WoS; which HeinOnline
  library/collection for HeinOnline)
- Total result count the platform showed **before** export
- Number of records actually in the exported file
- Export format used (CSV / tab-delimited / hand-compiled)
- Which fields you exported (and whether abstract was included — say
  explicitly if it wasn't, and why)
- Anything that didn't go as expected (a cap you hit, an ambiguous
  setting, a field you couldn't find) — flag it rather than guessing
  silently

This is exactly what went into `scopus_batch_run_log_20260910.csv` for
the Scopus batches, which is what let the pipeline verify every record
count instead of just trusting an assumption — the same discipline
applies here.
