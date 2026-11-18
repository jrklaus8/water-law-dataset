# Data management

This page describes what data the repository holds or depends on, where it lives, who may reuse it, and what has not been decided. It is a **draft for the researcher to confirm**, written by an AI assistant (Claude Code) on 2026-10-27 from the repository's contents. It is not a data management plan approved by any institution and not a legal opinion. Items that depend on facts outside the repository say "unknown" or "awaiting confirmation".

The review has its own detailed data documents: `legal-last-mile-systematic-review/DATA_DICTIONARY.md`, `CODEBOOK.md`, `10_reproducibility/DATA_MANIFEST.csv` and `REPRODUCE.md`. This page covers the repository as a whole and links to them instead of repeating them.

## 1. What data exist

| Data | Description | In this repository? | Where it lives | Size or count |
|---|---|---|---|---|
| Collected court decisions (raw) | JSON per court written by the scrapers: 8 Brazilian state courts plus a hand-coded TJSP 1997–2015 set; Canadian courts via the CanLII API, CanLII extra databases and Legal Data Hunter; Dutch courts via Rechtspraak open data | No. `data/` holds only `.gitkeep`; `.gitignore` excludes `*.json`, `*.csv`, `*.xlsx` | Researcher's machine; Zenodo, Harvard Dataverse, DANS, OSF deposits (README) | 83,596 decisions (README) |
| Merged national datasets and the coded dataset | `merge_national.py` unifies the three countries (13 fields); `jurimetric_coding.py` adds governance, rights, outcome and other flags | No | as above | not verified by this audit |
| Validation samples | 207-decision stratified sample with decision title, summary and URL; labels from the author and from an LLM relabelling; kappa and precision results | Yes, in `validation/` (tracked by explicit exceptions in `.gitignore`) | repository | 207 and 91 rows |
| Review: database exports | Subscription-database exports (Scopus, Web of Science, HeinOnline, ProQuest, JSTOR), SSRN and pilot searches, with native-format copies | Yes, `legal-last-mile-systematic-review/01_search/raw_exports/` | repository | about 124 MB |
| Review: screening, extraction, appraisal, synthesis data | CSV databases (27,481 de-duplicated records; 3,659 full-text candidates; 1,072 extracted studies with 92 fields; evidence map; effect sizes) | Yes | repository | 477 data files in the manifest |
| Review: full-text PDFs | The articles read for full-text screening | No: withheld for copyright and licence reasons (stated in `AI_USE_STATEMENT.md`) | Researcher's Drive "inbox" and local copies | not counted |
| Review: raw AI outputs | JSON outputs of second-model reviewers | Yes, `_reviewer2_codex/` | repository | see manifest |
| Code and documentation | Scrapers, utilities, validation scripts, review generators and tests, documents | Yes | repository | 1,682 tracked files |

## 2. Provenance and integrity

- The review records provenance in `00_admin/STUDY_AUDIT_TRAIL.csv`, `code/provenance/` and the registers of deviations and errors, and it fixes file contents with SHA-256 hashes in `10_reproducibility/DATA_MANIFEST.csv` (LF-normalised). A script and the verifier fail if the manifest is out of date.
- The court-decision dataset has **no equivalent**. No hash, row count or code revision links the deposited files to the scripts that produced them (finding F-12). Because the scrapers query live websites, a new run will not reproduce the same set.
- Recommended: after checking the deposits, record in this file the SHA-256 and row count of each deposited file and the commit of the scripts used (`git rev-parse HEAD` at the time of the run).

## 3. Formats and documentation

| Item | Status |
|---|---|
| File formats | CSV (UTF-8) and JSON for data, Markdown for documents. Some validation CSVs begin with a byte-order mark. Open formats. |
| Data dictionary for the review | Exists (`DATA_DICTIONARY.md`, `CODEBOOK.md`). |
| Data dictionary for the coded court dataset | **Missing.** The unified schema (13 fields) is visible in `utils/merge_national.py`; the coded variables are described in `RESEARCH_CONTEXT.md` and the code but not in a dictionary. Not created here because the definitions are the researcher's. |
| Windows paths and encodings | See F-03. |

## 4. Storage, backup and access

| Question | Answer from the repository | Status |
|---|---|---|
| Where is the master copy? | GitHub (public repository `jrklaus8/water-law-dataset`) for code and the review; deposits for the court dataset | stated |
| Is there a backup? | Not stated. Zenodo, Dataverse, DANS and OSF act as archives for deposited versions only | unknown |
| Who has access? | The repository is public. The Drive inbox of PDFs is controlled by the researcher; sharing settings unknown (finding F-07) | awaiting confirmation |
| Is storage approved by the institution? | Not stated | awaiting confirmation |
| Are unpublished or licensed materials sent to third-party AI services? | Yes, for the review (see [`ai-use-and-disclosure.md`](ai-use-and-disclosure.md)) | open (F-19) |

## 5. Personal data and sensitive material

| Item | Where | Notes |
|---|---|---|
| Names and e-mail addresses of authors | Review exports and files derived from them (finding F-05) | Scanned by pattern only; counts not established |
| Account identifier in ProQuest URLs | Review exports and derived files (F-06) | Not inspected |
| Party names in court decisions | Collected decisions and the 207-decision validation sample (title, summary) | Whether the courts anonymise the published text differs by country and was not checked (see [`source-register.md`](source-register.md)) |
| A Google Drive folder identifier | `00_admin/PDF_RETRIEVAL_AGENT_BRIEF_2026-10-09.md:16` (F-07) | Check the folder's sharing |
| Credentials | None found. The secret scan in `tests/test_repository_hygiene.py` checks code, configuration and documents for common key patterns and found none; data files are not scanned by that test | Verified for code, configuration and documents only |

## 6. Rights and licences (what the repository states)

| Component | Stated licence | Where | Comment |
|---|---|---|---|
| Code at the root | MIT, copyright holder given as the GitHub handle `jrklaus8` | `LICENSE`, `pyproject.toml`, README badge | Holder name form to be settled (F-21) |
| Court-decision dataset | "CC BY 4.0" appears only in `research-assistant/SUBMISSION.md:47`; no licence statement in the root README | deposits unknown | Confirm what the Zenodo/Dataverse/DANS records say |
| Research assistant | AGPL-3.0 (`research-assistant/README.md:62`) | | Differs from the root MIT licence |
| Review folder (code, documents, data) | MIT (`legal-last-mile-systematic-review/LICENSE`) | | MIT is a software licence; the status of the data is not stated separately |
| Third-party bibliographic exports | The databases' own terms | not read | F-04 |
| Court decisions as such | Public documents; terms of each portal | not read | [`source-register.md`](source-register.md) |
| University rights in the work | Unknown | | Ask the research office whether EUR claims any rights in the code, data or text |

## 7. Retention, deletion and take-down

No retention period, deletion procedure or take-down contact is stated. Suggested minimum: a contact address in `SECURITY.md` and the README; a rule that records a person asks to have removed are removed from the next version and from the deposits where the repository host allows it; a note that earlier versions in Git history and deposits may still contain them. Removing material from Git history is a separate decision that has not been taken (rewriting history was out of scope for this audit).

## 8. Responsibilities and decisions

| Decision | Owner |
|---|---|
| Whether to keep database exports and e-mail columns in the public repository (F-04, F-05, F-06) | Researcher, after reading the database terms and consulting the library and privacy contact |
| Licence per component (F-18) | Researcher; research office for any university claim |
| Hashes and versions of the deposits (F-12) | Researcher |
| Whether a formal data management plan exists or is required (standards matrix S-01, S-02) | Researcher and data steward |
