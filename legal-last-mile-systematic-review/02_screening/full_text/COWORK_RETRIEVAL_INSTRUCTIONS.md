# Full-Text Retrieval — Instructions for a Cowork Session

Paste this whole document as the opening message of a browser-capable
Claude Cowork session, alongside the batch file it references (see
"What to bring" below). This mirrors how the real database searches for
this project were done earlier: Cowork does the actual browser work
(here, retrieving PDFs via institutional access) and reports results
back as a file the researcher uploads to the main project session, which
then applies them to the tracking database with a script built for
exactly this handoff.

## What this task is — and isn't

**Is:** for each record in the batch, find and retrieve the full-text
PDF (or determine, honestly, that it can't be retrieved), and record
where the file ended up.

**Is not:** reading the full text and making an include/exclude
decision. That's a separate, later step (full-text *screening*, not
retrieval) requiring careful judgment against `INCLUSION_EXCLUSION.md` —
don't do it as part of this task, even if a PDF is open in front of you
and the answer looks obvious. Keep `full_text_decision` and everything
after it in the output blank.

## What to bring into the Cowork session

A **batch** of rows from `full_text_retrieval_queue.csv` — not all
3,659 at once. That file is sorted by database then year, so a natural
batch is "the next 30–50 rows for one database" (e.g. all the Scopus
rows, or all the JSTOR rows) — working one platform at a time means one
login/proxy setup covers the whole batch instead of switching contexts
every record. Copy just those rows (with the header) into a small CSV
and attach or paste it into the Cowork session. Pick a batch size that
feels doable in one sitting — this is meant to run as several Cowork
sessions over time, not one marathon covering the whole queue.

## Access

Use EUR (Erasmus University Rotterdam) institutional access the same way
it was used for the original database searches (`SEARCH_PROTOCOL.md`
§7) — via the university library's proxy/EZproxy sign-in, or by
resolving the DOI through the institutional link resolver rather than
the public internet, whichever gets past a paywall a public search
wouldn't. If a title has no DOI (some grey-literature/JSTOR records
don't), use the `url` column instead.

## Per record

1. Try the DOI first (resolves to the publisher's page, often the
   fastest path once institutional access is active). Fall back to the
   `url` column if there's no DOI, or if the DOI resolves somewhere
   unhelpful.
2. If a PDF is obtainable, download it and save it in a clearly-named
   local folder (see "Where PDFs actually live" below) using a filename
   that starts with the record's `record_id` (e.g.
   `R9E24EC349D72_gaikwad_thomas_2026.pdf`) — this makes the file
   findable later without cross-referencing anything.
3. If it's not obtainable (hard paywall with no institutional access,
   genuinely out of print with no digital copy, a broken/dead link with
   no working alternative), **don't skip the row silently** — record
   that outcome. A `not_retrievable` result is itself a legitimate,
   PRISMA-reportable finding (there's a dedicated line for exactly this
   in `06_outputs/prisma/prisma_flow.md`), not a failure to hide or a
   reason to leave the row blank.
4. **Never guess or fabricate a retrieval outcome.** If you're not sure
   whether what you found is actually the right paper (title mismatch,
   wrong year, a similarly-named different article), say so in `notes`
   rather than recording `retrieved` on a guess — a wrong PDF attached to
   the wrong `record_id` is worse than an honest `not_retrievable`.

## Where PDFs actually live

**Do not commit retrieved PDFs into this git repository.** Two reasons:
publisher copyright generally doesn't permit redistributing a paywalled
article's PDF, even in a private repo, and PDFs would bloat the
repository unnecessarily. Save them instead to the researcher's own
storage (a local folder, a Zotero/Mendeley library, an institutional
shared drive, a cloud folder) and record **that location** — a file
path or a stable link the researcher can open later — in
`full_text_location`. If you (the Cowork session) don't have direct
access to the researcher's storage, describe where you're leaving the
files clearly enough that the researcher can find and move them
afterward.

## What to produce: the results file

One CSV per batch, with exactly these columns:

```
record_id,full_text_status,full_text_location,notes
```

- `record_id` — copy exactly from the input batch, don't retype it.
- `full_text_status` — exactly one of `sought` (you tried but haven't
  finished — e.g. waiting on an interlibrary loan request), `retrieved`,
  or `not_retrievable`. Nothing else is a valid value.
- `full_text_location` — where the PDF actually is (per "Where PDFs
  actually live" above), or blank if not retrieved.
- `notes` — anything useful: why something wasn't retrievable, a
  title-mismatch concern, an interlibrary-loan request reference number,
  etc.

Include a row for **every** record in the batch, even the
`not_retrievable` ones — a missing row looks like "not yet attempted,"
which is different from "attempted and failed."

Name the file something identifiable, e.g.
`full_text_retrieval_results_<database>_<date>.csv`, and hand it back to
the researcher (as a download, or however this Cowork session delivers
files) so it can be uploaded to the main project session.

## What happens after you upload the results

The main session applies your batch with a script built for exactly this
handoff:

```
python3 code/screening/bulk_import_full_text_results.py \
    --full-text-db 02_screening/full_text/full_text_screening_database.csv \
    --results <your_results_file>.csv \
    --dry-run
```

(the `--dry-run` first, to check what it would do — then again without
that flag to actually apply it). It validates every row before writing
anything — an invalid value anywhere in the batch rejects the *whole*
batch with nothing written, rather than partially applying a mix of good
and bad rows — and it never touches a record that's already been fully
decided. See `02_screening/full_text/FULL_TEXT_README.md` for the rest
of the Phase 6 workflow once retrieval is done and screening begins.

## Regenerating the next batch

Once a batch is applied, regenerate the queue to drop whatever's now
settled and see what's left:

```
python3 code/screening/build_full_text_queue.py \
    --full-text-db 02_screening/full_text/full_text_screening_database.csv \
    --screening-db 02_screening/title_abstract/screening_database.csv \
    --queue-out 02_screening/full_text/full_text_retrieval_queue.csv
```

Only records still open (no `final_decision`) will remain — but note
`build_full_text_queue.py`'s queue only drops a record once it has a
`final_decision`, not just a `full_text_status`. A record marked
`retrieved` this way still needs the actual full-text screening step
(`FULL_TEXT_README.md`) before it drops out of the queue — retrieval and
screening are two different completions of the same row.
