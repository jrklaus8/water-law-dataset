# `code/provenance/` — one-off scripts that applied the project's data changes

**Read this before running anything here.** These are **not** a re-runnable pipeline. They are the
literal one-off Python scripts (and two raw-output files) that were run, in sequence, during the
2026-09 AI-assisted screening/extraction/appraisal sessions to write decisions and extracted data
into the project's CSV databases. They were archived here on 2026-09-28 by the repository audit
(`00_admin/audits/2026-09-28_repository_audit.md`) because they had only ever existed in an
ephemeral session scratchpad — `CHANGELOG.md` and several audit documents cite them, and a future
auditor could not otherwise see how a given row came to hold its value.

**The authoritative record is the CSV databases plus `git log`**, not these scripts. Each script:

- hard-codes absolute paths from the original session
  (`/home/user/water-law-dataset/legal-last-mile-systematic-review/...`);
- was written against the state of the databases *at the time it ran* — many assert exact row counts
  (`assert len(rows) == N`) that no longer hold, and many use `date.today()` for the recorded date,
  so re-running one would stamp today's date on an old decision and would fail its own assertions;
- carries its decision text (exclusion reasons, extraction fields, ratings) inline, which is the
  useful part for provenance: `grep -rl "S566" code/provenance/` (or a record ID such as
  `RA1815DB6A8FD`) finds the script that wrote a given study's rows.

Do not "fix" or modernize these files. If you need to change data, write a new, dated script,
follow the atomic-write pattern below, and log it in `CHANGELOG.md`.

## Layout

| Folder | Files | What it holds |
|---|---|---|
| `batch_screening/` | 183 | `record_batch*.py` — full-text screening decisions written into `full_text_screening_database.csv` (and `exclusion_log.csv` for exclusions), one batch per chat upload of PDFs; `flag_wrong_file*.py` — records the "wrong file retrieved" flags; `close_retrieval_phase.py` — the 2026-09-28 Phase 6 closure; `record_reviewer2_fulltext_first100.py` — the reviewer_2 first-100 pass |
| `batch_extraction/` | 159 | `extract_s###_s###.py` — rows appended to `extraction_database.csv`, named by the study-ID range they created |
| `batch_evidence_map/` | 151 | `evidence_map_s###_s###.py` — the matching `evidence_map.csv` rows |
| `batch_effect_sizes/` | 28 | `effect_sizes_s###.py` — rows appended to `effect_sizes.csv` |
| `audit_and_repair/` | 24 | Analysis, corrective, and audit scripts: risk-of-bias batch updates (`rob2_*`, `amstar2_*`, `legal_framework_audit_apply.py`, `rob_and_family_fixes.py`), Phase 11 follow-ups (`resolve_9_blank_family.py`, `add_s348.py`), duplicate audits (`doi_audit.py`, `title_dup_*.py`), field/enum repairs (`fix_adjusted_field.py`, `fix_study_design_class.py`, `resync_study_design_class.py`), the reviewer_2 sample draw (`stratified_draw.py`), `build_study_record_map_2026-09-28.py` / `build_linked_reports_2026-09-28.py` (the study↔record index and the linked-reports table), the two duplicate-paper scripts (`annotate_live_duplicates_2026-09-28.py`, then the researcher-approved `merge_live_duplicates_2026-09-28.py`), and the audit's own recomputation (`live_numbers.py`) and documentation-correction scripts (`fix_evidence_limitations.py`, `fix_readme_prisma.py`) |
| `audit_results/` | 2 | `title_dup_results.txt` (raw candidate pairs from the fuzzy title/author duplicate audit) and `doi_audit_output.txt` — the raw outputs cited by `01_search/deduplicated/*_duplicate_audit_2026-09-28.md` |

## The write pattern the scripts share

Every script that mutates a CSV follows the same pattern, so a reader knows what guarantees to
expect: read the whole CSV with `csv.field_size_limit(sys.maxsize)`; modify rows in memory; assert
the expected row count and the exact number of rows touched; write to a temp file in the same
directory (`tempfile.mkstemp`); `os.replace()` it over the original. A failed assertion therefore
leaves the database untouched. (`evidence_map.csv` uses CRLF line endings — scripts that rewrite it
must pass `lineterminator='\r\n'` or every line of the file shows as changed in `git diff`.)

## Coverage gap: the earliest work has no script archive

The archive starts where the session scratchpad starts. It covers full-text screening batches from
`record_batch64` onward, extraction/evidence-map batches from study S532 onward, and the effect-size
scripts that survived; **the earlier screening batches (before batch 64), the extraction of studies
S001–S531, and any one-off scripts used for the title/abstract stage are not represented here**
(the reusable tooling in `code/screening/`, `code/search/`, and `code/extraction/` is tracked
separately). For those rows, `git log -p` on the CSV
databases and the dated `CHANGELOG.md` entries are the only record. This is disclosed rather than
papered over; it cannot be reconstructed after the fact.

## What was deliberately not archived

Session-tooling scripts that only listed or downloaded files from a cloud-storage connector
(`antigravity_batch_check.py`, `check_and_append.py`, `process_all.py`, `process_latest.py`,
`rebuild_clean.py`, `new_files_page2.py`), the intermediate JSON file listings they read, and the
`pdftotext` conversions of the source PDFs. The PDFs and their text conversions are publisher
material and were never committed to this repository (`git ls-files` contains no PDFs); each database
row records the record ID and retrieval URL/DOI so the source can be re-obtained.

## Screening

This folder was scanned for credentials, tokens, and personal contact details before it was
committed (none found; the only hits were the words "secretary" and "tokenistic" inside extracted
text). All 545 scripts parse (`ast.parse`) under Python 3.
