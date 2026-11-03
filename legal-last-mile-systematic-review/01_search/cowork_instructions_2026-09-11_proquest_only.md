# Instructions for Claude Cowork — ProQuest, full export via your account

Paste this whole document into Claude Cowork as-is. This assumes you've
already created your personal ProQuest "My Research" account and are
signed in (or are about to sign in) — if not, do that first; Cowork
can't create the account or enter your password for you.

**Standing caution, worth repeating**: a network response (HTTP 200, an
export dialog closing normally) is **not proof a file was actually
written to disk**. This has caused real problems twice already in this
project (once on Web of Science, once on ProQuest's own guest-export
path last round). Confirm every export against the actual file before
reporting it done.

## Background — why this needs a real account

Guest (no-account) export on ProQuest works mechanically but caps at
roughly 100–200 records per session before throwing a "Login or create a
My Research account" error, and saves files under an unrecoverable
random-GUID filename in Downloads. Not viable for the full result set.
Your own account unlocks a documented bulk export of up to 20,000
records in one operation — the actual fix.

## Step 1: Confirm you're signed in, re-run the search

- Library route: EUR library database list → "ProQuest."
- Confirm you're logged into your own "My Research" account (not
  browsing as a guest) — check for your account name/email somewhere in
  the top-right UI before proceeding.
- Advanced Search → Command Line mode. Select **all 16 EUR-licensed
  ProQuest sub-databases** via "Change databases" → Select all.
- Paste this exact query (same one already logged as `SEARCH_039`):

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

- Note the total result count shown (last round it was 8,137 — confirm
  whether it's still the same; platform counts can drift slightly day to
  day).

## Step 2: Full bulk export via your account

- Select all results (there should now be a "Select all [N]" option
  distinct from per-page selection, or an export path that doesn't
  require manual selection at all — that's specifically what the
  account unlocks).
- Export → **RIS** format → include **Abstract** in the field selection
  (also Title, Authors, Author affiliations, Journal, full
  citation/DOI — same field set as the guest-mode batch already pulled).
- This should be **one operation covering all ~8,137 results**, not
  batches of 100 like the guest path required.
- **Verify on disk**: does the exported file actually exist, with a
  record count matching the platform total (or close to it — some drift
  between "shown" and "exported" is normal, e.g. from duplicate/withdrawn
  records)? Check it's well-formed: balanced `TY`/`ER` pairs, no visible
  truncation partway through, unique accession numbers throughout — same
  checks as before, just at full scale now.
- If the account's export still hits some limit or error, **report the
  exact error text** rather than falling back to guest-mode batching —
  that path is already established as inadequate for this volume.
- If the file is large, it may still land under a non-obvious filename —
  check Downloads directly (including recently-modified files) rather
  than assuming a normal name.

## Step 3: Sociological Abstracts secondary search (log as SEARCH_040)

Once Step 2 is done, run a second, narrower search specifically for
**Sociological Abstracts** (a ProQuest sub-database), restricted to the
platform's own controlled-vocabulary thesaurus terms rather than free-text
keywords — this catches records indexed by subject that the keyword
search might miss. Use whatever thesaurus/subject-term picker
Sociological Abstracts' interface offers, and pick the closest matches
to these four example terms:

- "public utilities"
- "water resources"
- "bureaucracy"
- "administrative agencies"

Export the same way (RIS, abstract included, via your account). Log this
as its own `search_id` (`SEARCH_040`) — keep it separate from
`SEARCH_039`'s results, don't merge the files.

## What to send back

- The full `SEARCH_039` export file (or confirmation of exactly how many
  records it contains if the total differs from 8,137, and why)
- The `SEARCH_040` export file
- For each: exact query/filters used, total count shown by the platform,
  records actually in the export, and anything that didn't go as
  expected

**Please attach the actual export files this time** — the last three
searches (HeinOnline, ProQuest's guest batch, JSTOR) were all reported
in detail via run logs, but the files themselves never made it back to
the pipeline, so none of that data has been ingested yet.
