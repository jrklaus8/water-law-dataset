# Instructions for Claude Cowork — execute the ProQuest and JSTOR decisions

Paste this whole document into Claude Cowork as-is. Two decisions from
the researcher, both ready to execute now. Standing caution still
applies: **confirm every export against the actual file on disk, not a
network status code or a closing dialog** — this has mattered twice
already in this project (once with Web of Science, once with ProQuest's
own GUID-named export files).

---

## Decision 1: ProQuest — full 8,137-record export via a "My Research" account

Last round, guest/no-account export worked mechanically but capped at
roughly 100-200 records per session before throwing a login-required
error, and saved files under an unrecoverable random-GUID filename —
not viable for the full result set. **The researcher has decided to
create a personal ProQuest "My Research" account** to unlock the
platform's documented bulk export of up to 20,000 records in one
operation.

- **Check whether the account exists and is logged in yet.** You cannot
  create the account or enter a password on the researcher's behalf —
  if it's not set up, stop here on this item and say so plainly, rather
  than attempting the guest-export workaround again (already established
  as insufficient for the full set).
- **Once logged in**, re-run (or confirm still active) the same query
  already logged as `SEARCH_039`:

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

  across all 16 EUR-licensed ProQuest sub-databases (same selection as
  before — "Change databases" → Select all). Confirm the total count
  still shows ~8,137 (platform counts can drift slightly day to day;
  note the exact figure either way).

- **Export via the "My Research" bulk export option** (not the guest
  "All save & export options" path used last time) — this should be a
  single operation covering all results, not batches of 100. RIS format,
  include **Abstract** in the field selection. Verify the resulting file
  on disk: record count matches the platform total, well-formed (TY/ER
  pairs balanced, no truncation), unique accession numbers throughout.

- **Then run `SEARCH_040`**, the Sociological-Abstracts-specific
  secondary search using the platform's own controlled-vocabulary
  thesaurus terms — pick the closest matches to "public utilities,"
  "water resources," "bureaucracy," "administrative agencies" from
  whatever thesaurus/subject-term picker ProQuest offers for
  Sociological Abstracts specifically. Log as its own `search_id`, keep
  it separate from `SEARCH_039`'s results. Same export method (now that
  the account is active) and same abstract requirement.

- If the bulk export itself hits some new limit or error even with the
  account, report the exact error text rather than falling back to
  guest-mode batching — that path is already known to be inadequate for
  8,137 records.

---

## Decision 2: JSTOR — finish exporting the full 356 (not just the 7-record sample), don't widen further

**The researcher has decided to accept the narrower, Subject:Law-filtered
JSTOR search as a supplementary source** rather than running further
subject-filtered sub-searches (Development Studies, Public Policy &
Administration, Urban Studies, etc.) to widen it. What's still needed is
finishing the export of the **already-identified 356 results** — only 7
were exported last round as a proof-of-concept sample.

- Return to the same JSTOR search already run and logged as `SEARCH_041`:
  the trimmed query `(((sanitation OR wastewater OR "water supply" OR
  "sanitation service") AND ("administrative burden" OR "administrative
  barrier" OR eligibility)) AND (access OR "service delivery" OR
  affordability))`, All Content, **Subject: Law** filter applied, Access
  type = Content I can access. Confirm it still shows 356 results before
  proceeding (don't re-widen or re-trim it — that question is settled).
- JSTOR has no bulk "select all" — export happens via per-item checkbox
  selection, so this means working through all ~15 pages (25 results
  per page) of the filtered result list, selecting each page's items,
  and using **Cite → Export a RIS file** in batches (whatever the
  interface allows per selection — likely one page at a time, i.e. up to
  25 per export).
- **Verify each batch on disk** before moving to the next page (same
  GUID-filename caveat as last time — these won't have a normal
  filename) — confirm TY/ER record counts match what you selected before
  trusting the export and moving on.
- No abstract field will be present in any of these exports — already
  confirmed absent from JSTOR's RIS format entirely, not worth
  re-checking each batch for.
- Once all ~15 batches are done, you should have all 356 records total
  (minus the 7 already delivered, if you're resuming rather than
  restarting — check for that overlap by accession/stable-URL before
  re-exporting the same items twice).

---

## Reporting discipline (same as every round)

For each: final record count achieved vs. the target (8,137 for
ProQuest's main search, 356 for JSTOR), export format, whether abstract
was included, and anything that didn't go as expected — a new error, a
count that doesn't match, anything requiring another decision rather
than just executing. Confirm every file exists on disk with a plausible
record count before reporting either item as done.
