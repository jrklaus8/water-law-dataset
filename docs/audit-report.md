# Open-research, reproducibility and transparency audit

**Date of audit:** 2026-10-27 · **Repository:** `jrklaus8/water-law-dataset` · **Branch audited:** `claude/legal-last-mile-review-spec-8ri0zs` (base: its state after the 2026-10-27 reproducibility pack, commit `3eadd0e`)

> **What this document is.** A self-assessment prepared by an AI assistant (Claude Code) at the researcher's request. It is **not an official university review, a certification, an ethics approval or a legal opinion**, and nothing in it states that the project complies with any university policy, law, licence or research standard. Severity ratings are the assistant's judgment, not the researcher's or an independent reviewer's. The assistant also wrote parts of the code and documents it examined, and no person has yet reviewed these findings. Treat them as leads to check.
>
> **Limits the researcher set for this audit, and how they were kept.** No data or source records were overwritten or deleted; no secret values are reproduced (findings identify file and line only); nothing was published, pushed, released or uploaded; no live request was made to any court, database, university or AI service for this audit (a search tool was used to locate institutional pages, whose content could not be opened); no change was made that could alter collected data, coding results or scope. Changes that would do so are listed in section H as decisions.

## Contents

[A. Executive summary](#a-executive-summary) · [B. Findings register](#b-findings-register) · [C. Standards and requirements](#c-standards-and-requirements-matrix) · [D. Reproducibility assessment](#d-reproducibility-assessment) · [E. AI transparency assessment](#e-ai-transparency-assessment) · [F. Data and publication risk register](#f-data-and-publication-risk-register) · [G. Changes made](#g-changes-made) · [H. Outstanding decisions](#h-outstanding-decisions) · [I. Release readiness](#i-release-readiness)

Method, scope and coverage of the eleven audit phases are in [Scope and method](#scope-and-method) at the end.

## A. Executive summary

**What was examined.** The repository holds 1,682 tracked files in two linked projects: a court-decision dataset and its tools (15 scrapers, a merge step, a regex coding engine, validation scripts, a research-assistant app; about 80 files outside the review) and an AI-assisted systematic review (1,604 files). The audit read the documents, scripts and registers named in the findings, ran pattern scans across the rest, ran the existing review verifier, and wrote and ran 41 new offline tests (35 pass, 6 are documented defects recorded as expected failures).

**What is in good shape.**
- The systematic review is unusually transparent about itself: dated deviations and errors registers, a weakness register with ways to test each weakness, a per-study audit trail, an AI-use ledger that says what is *not* archived, a SHA-256 manifest of 477 data files, a verifier that recomputes headline figures (206 checks pass), and a recorded fresh-clone reproduction.
- No credential or token pattern was found in code, configuration or documents. API keys are read from environment variables, with placeholders in `.env.example`.
- The four Canadian and two of the three Dutch scrapers identify the project honestly in their User-Agent; 14 of the 15 scripts pause between requests; the court scrapers use only the standard library apart from one loader.
- The root README already says outcome coding is AI-assisted and only partly validated, and says the Dutch data carry no outcome coding.

**What most needs attention** (the four findings rated High, plus the pattern behind them):
1. **F-04: subscription-database exports are in the public repository** (about 124 MB). Whether redistribution is allowed was not checked; this is a legal and library question, not answerable from here.
2. **F-08: Brazilian win/loss patterns code some "improper cut-off" phrases in the wrong direction** (for example "corte indevido" is coded as the utility winning). The size of the effect is unknown because the coded dataset is not in the repository. Fixing it changes results, so it was left unchanged and encoded as an expected-failure test.
3. **F-19: licensed and unpublished material was sent to external AI services**, including a free-tier quota. Whether this was allowed under the services' terms, the publishers' terms and EUR guidance was not established.
4. **F-27: limited human verification in the review** (459 of 2,277 full-text decisions, 20.2%; no second extractor). This is disclosed throughout; it is listed because it bounds every claim the review can make.
5. **The pattern:** the court dataset side of the repository has far less documentation, testing and provenance than the review side. Collection dates, per-source terms, tool versions, hashes of the deposits, a TJSP scraper and the coded data itself are missing (F-11, F-12, F-20, F-30), so the headline 83,596-decision dataset cannot currently be re-derived or verified from the repository.

**What was fixed during the audit (small, safe, reversible).** Offline tests and a CI step (F-13); explicit read-only permissions in three workflows (F-14); inaccurate README and `.env.example` statements (F-28); two invalid `CITATION.cff` files made valid (F-29); and the audit documents themselves. See section G.

**What was deliberately not changed** (needs your decision): scraper TLS verification, User-Agent and default paths (F-01 to F-03), the coding patterns (F-08, F-09), the wording of the "absorbed before litigation" claim (F-10), authorship, licences and the database exports (F-04, F-17, F-18).

**Counts, not scores.** 31 findings: 4 High, 15 Medium, 11 Low, 1 Info; 4 fixed here, 8 partly addressed (mostly by documentation that records the question), 19 open. 21 standards rows: none verified as compliant, one not met, the rest partly verified or awaiting confirmation. These are descriptions of what was found, not a compliance score; no such score is meaningful here.

**Next step.** Section H lists 13 decisions. The first is whether the local commit that holds this audit may be pushed; it has not been.


## B. Findings register

Full detail for every finding (severity rationale, all locations, evidence, why it matters, recommended correction, whether fixed, verification, uncertainty, decision needed) is in [`findings-register.csv`](findings-register.csv); the table below is its summary and is checked against it by `tests/test_repository_hygiene.py`.

**Severity scale (the assistant's judgment).** *High*: could invalidate a headline result, expose licensed or personal material irreversibly, or undermine a stated integrity claim, and needs a decision from the researcher or institution. *Medium*: weakens reproducibility, the legal or ethical posture, or the support for a claim; fixable with a decision or bounded work. *Low*: hygiene or documentation problem with limited consequence. *Info*: an observation.

<!-- findings-table:start -->
| ID | Severity (AI) | Finding | Where | Fixed here? | Decision needed? |
|---|---|---|---|---|---|
| F-01 | Medium | TLS certificate verification disabled in four scrapers | `scrapers/brazil/tjrj_scraper.py:16-17 (+3 files)` | no | yes |
| F-02 | Medium | Seven scrapers imitate a browser; one gives a placeholder contact | `scrapers/brazil/tjrj_scraper.py:24 (+6 files); scrapers/netherlands/rechtspraak_scraper.py:22` | no | yes |
| F-03 | Medium | Hard-coded personal Windows paths as defaults | `scrapers/canada/canlii_scraper.py:57 (+13 locations)` | partly | yes |
| F-04 | High | Licensed database exports committed to a public repository | `legal-last-mile-systematic-review/01_search/raw_exports/` | no | yes |
| F-05 | Medium | Third-party e-mail addresses in public data files | `legal-last-mile-systematic-review/01_search/deduplicated/deduplicated_records.csv (+11 files)` | no | yes |
| F-06 | Low | Institutional account identifier in stored ProQuest URLs | `legal-last-mile-systematic-review/01_search/raw_exports/SEARCH_039_PROQUEST_2026-09-11.csv (+ derived files)` | no | yes |
| F-07 | Medium | Shared-folder identifier published in a brief | `legal-last-mile-systematic-review/00_admin/PDF_RETRIEVAL_AGENT_BRIEF_2026-10-09.md:16` | no | yes |
| F-08 | High | Win/loss patterns code "indevido" phrases in the wrong direction | `utils/jurimetric_coding.py:581-583, 605-607` | no | yes |
| F-09 | Low | Typo "caebs" in a user-wins pattern | `utils/jurimetric_coding.py:585` | no | yes |
| F-10 | Medium | "Absorbed before litigation" asserted from a classifier share | `RESEARCH_CONTEXT.md:55` | no | yes |
| F-11 | Medium | No per-source record of terms for the lawfulness of collection | `README.md:184-186` | partly | yes |
| F-12 | Medium | Headline dataset cannot be re-derived from the repository | `.gitignore:32-34` | partly | yes |
| F-13 | Medium | No automated tests for the root code before this audit | `.github/workflows/python-package.yml` | yes | no |
| F-14 | Low | CI workflows without least-privilege permissions | `.github/workflows/pylint.yml (+2 files)` | yes | no |
| F-15 | Low | Dependency documentation incomplete and nothing pinned | `requirements.txt` | partly | yes |
| F-16 | Low | Packaging: license string vs declared minimum setuptools | `pyproject.toml:2,10` | no | yes |
| F-17 | Medium | AI tools listed as authors in both citation files | `CITATION.cff:18; legal-last-mile-systematic-review/CITATION.cff:29` | no | yes |
| F-18 | Medium | Licence statements inconsistent across components | `LICENSE:3` | partly | yes |
| F-19 | High | Licensed and unpublished material sent to external AI services | `legal-last-mile-systematic-review/00_admin/AI_USE_LEDGER.md` | partly | yes |
| F-20 | Medium | Prompts, model versions and settings largely not archived | `legal-last-mile-systematic-review/00_admin/AI_USE_LEDGER.md` | partly | yes |
| F-21 | Low | Author name appears in three forms | `README.md:233` | no | yes |
| F-22 | Medium | Reliability evidence weaker than its label suggests | `validation/README.md:3-4, 34-41` | no | yes |
| F-23 | Low | No rate-limit policy or request log for the scrapers | `scrapers/ (all 15 scripts)` | no | yes |
| F-24 | Low | .gitignore pattern design can hide or admit files silently | `.gitignore:32-34, 50` | partly | no |
| F-25 | Info | docs/ is the public Pages root | `docs/ (Pages root)` | no | yes |
| F-26 | Medium | Review protocol not prospectively registered | `legal-last-mile-systematic-review/PROTOCOL.md:3` | no | yes |
| F-27 | High | Review has limited human verification | `legal-last-mile-systematic-review/00_admin/CURRENT_FIGURES.md` | no | yes |
| F-28 | Low | README and .env.example described the code inaccurately | `README.md:68, 227` | yes | no |
| F-29 | Low | CITATION.cff files failed schema validation | `CITATION.cff; legal-last-mile-systematic-review/CITATION.cff` | yes | yes |
| F-30 | Medium | TJSP scraper absent; hand-coded set unprovenanced | `scrapers/brazil/ (no TJSP scraper); README.md` | no | yes |
| F-31 | Low | README maps scripts to Dutch subsets inconsistently | `README.md; scrapers/netherlands/rechtspraak_scraper.py:1-10` | no | no |
<!-- findings-table:end -->

The two ratings the researcher is most likely to want to challenge are F-04 (the terms may well permit redistribution) and F-27 (already disclosed and tracked in the review's own registers). Please say if you disagree with any rating; the CSV is meant to be edited.

## C. Standards and requirements matrix

The full matrix, with official source, date accessed, applicability, evidence, status and action for 21 requirements, is in [`standards-matrix.md`](standards-matrix.md). Its main message: **the institutional requirements could not be read from the audit environment** (the university site could not be opened; the policies were located through search summaries only), so every institutional row is "awaiting confirmation" or at best "partially verified". One row is *not met* (prospective protocol registration, which the review discloses). Three questions for EUR are in section H, decision 9.

## D. Reproducibility assessment

Environment of the audit: Linux, Python 3.11.17 (default), also 3.12 and 3.13 for the new tests; no 3.8, 3.9 or 3.10 interpreter. A scratch virtual environment (not committed) held `cffconvert`; a scratch copy of the packaging files was used for the build test. Commands are in [`reproducibility.md`](reproducibility.md).

| # | Check | Command or method | Result | Notes |
|---|---|---|---|---|
| D1 | Root offline tests, Python 3.11 | `python3 -m unittest discover -s tests` | **passed**: 41 tests, 6 expected failures, no unexpected result | expected failures are documented defects F-01, F-02, F-03, F-08 |
| D2 | Root offline tests, Python 3.12 and 3.13 | same | **passed**: 41 tests, 6 expected failures (each version) | |
| D3 | Syntax valid for Python 3.8 | `ast.parse(..., feature_version=(3, 8))` over scrapers, utils, validation | **passed** (part of D1) | the 3.8 interpreter itself was not available: **could not run** |
| D4 | Python 3.8–3.10 test runs | n/a | **could not run** | interpreters not available; CI matrix covers them once the branch is pushed |
| D5 | Review verifier | `python3 code/analysis/verify_repository.py` (in the review folder) | **passed**: 206 checks, 0 failed, about 30 s | run after the `CITATION.cff` edit |
| D6 | Review unit tests | sample: `test_reader_guides`, `test_study_audit_trail`, `test_ai_use_ledger`, `test_weakness_register`, `test_registers`, `test_evidence_atlas` | **passed** (6 of 25 files) | the other 19 files and `regenerate_all.sh`: **skipped** (it rewrites generated files; a full fresh-clone run was recorded earlier the same day in `10_reproducibility/REPRODUCTION_RUN_2026-10-27.md`) |
| D7 | Citation metadata | `cffconvert --validate` in a scratch environment | **failed before** (empty `orcid`), **passed after** for both files | F-29 |
| D8 | Workflow files | parsed with PyYAML | **passed** (4 files) | not run on GitHub: **could not run** |
| D9 | Credential scan | `tests/test_repository_hygiene.py` (code, configuration, documents) | **passed**: no match | rule self-checked on synthetic positives; data files **not scanned** for secrets (counted PII and identifier patterns only) |
| D10 | Environment variables documented | same test file | **passed** | after the `.env.example` fix |
| D11 | Packaging build | `pip wheel . --no-build-isolation` in a scratch copy with setuptools 68.1.2 | **failed** at metadata generation (`project.license`); with the table form the metadata passed and a later wheel step failed for a reason not diagnosed | F-16; an isolated build (needs network access to fetch setuptools) was **not run** |
| D12 | Scrapers against live sites | n/a | **not run** | not authorised; offline fixtures only |
| D13 | Re-derivation of the 83,596-decision dataset | n/a | **could not run** | data not in the repository (F-12) |
| D14 | Comparison with the Zenodo, Dataverse, DANS, OSF deposits | n/a | **could not run** | not retrieved |
| D15 | Lint (pylint, flake8) as in CI | n/a | **skipped** | no linted file (`scrapers/`, `utils/`) was changed |
| D16 | Independent reproduction by a person | n/a | **not done** | the only recorded reproduction was run by the AI that wrote the code |

**Assessment.** The review can be re-verified from its own files with the standard library alone, and its generated files cannot silently drift. The court-decision dataset cannot be re-derived or compared with its deposits from this repository, and AI-assisted steps in both projects cannot be rerun. The new offline tests make the helper functions and the repository's hygiene checkable; they characterise current behaviour and do not validate the research coding.

## E. AI transparency assessment

| Dimension | State | Evidence |
|---|---|---|
| AI use disclosed | **Present**, prominently for the review (in its title), in the root README for the dataset | `AI_USE_STATEMENT.md`; README "AI Disclosure"; [`ai-use-and-disclosure.md`](ai-use-and-disclosure.md) |
| Tools named | **Present**: Claude, Antigravity, Codex, Gemini, an AI browser assistant | same |
| Model identifiers | **Partial**: recorded for the research assistant and the Codex/Gemini passes; for only 60 early review rows; absent for the dataset-side work | AI-use ledger |
| Dates of use | **Partial**: by label date in the review; absent for the dataset side | |
| Prompts and instructions | **Partial**: criteria, codebook, instruction files and scripts with prompts archived for the review; the interactive conversations are not; nothing for the dataset side | AI-use ledger, "What is NOT archived" |
| Settings, seeds | **Absent** | |
| AI outputs retained | **Present** for the review (per-record rationale, raw second-model JSON); absent for the dataset side | |
| Human oversight | **Recorded with strict counting** in the review (human-verified vs AI-checked); minimal for the dataset (author hand-coded 207 decisions) | `CURRENT_FIGURES.md`; `validation/README.md` |
| Material sent to external services | **Documented here for the first time** (section 4 of `ai-use-and-disclosure.md`); not documented per file | F-19 |
| Alignment with service terms, publisher terms, university guidance | **Unknown**: none of the terms or guidance were read | S-04, S-05, S-10, S-14, S-15 |
| AI errors found and recorded | **Present**: 29 entries in the errors register, several the AI's own | `00_admin/ERRORS_FOUND_REGISTER.csv` |
| AI named as an author | **Yes** in both `CITATION.cff` files | F-17 |

**Assessment.** Disclosure of the fact and extent of AI use is thorough for the review and thin for the dataset side. The traceability needed to rerun or independently assess AI steps (versions, prompts, settings) is largely missing and cannot be reconstructed. Whether the use of external services for licensed and unpublished material was permitted is the largest open question.

## F. Data and publication risk register

Likelihood and impact are the assistant's judgment (low / medium / high / unknown).

| ID | Risk | Material affected | Likelihood | Impact | Mitigation | Decision owner | Findings |
|---|---|---|---|---|---|---|---|
| R-01 | A publisher or database objects to redistribution of exports | `01_search/raw_exports/`, deduplicated records | unknown | high | Read the terms; replace exports by IDs and hashes if needed; decide separately about history | Researcher with library | F-04 |
| R-02 | Personal data of authors or parties is republished without a basis | exports, derived screening files, collected decisions, validation sample | medium | medium | Quantify; drop e-mail columns from public copies; check anonymisation of decisions; consult the privacy contact | Researcher; privacy contact | F-05, F-06, F-11 |
| R-03 | A shared folder of copyrighted PDFs is publicly reachable | Drive inbox | unknown | high | Check and restrict sharing; replace the identifier with a placeholder | Researcher | F-07 |
| R-04 | Incorrect outcome or interpretation is cited by others | Brazilian win/loss variable; "absorbed before litigation" statement; κ | medium | high | Correct and re-code, or label as unreliable; reword; label κ as author-vs-LLM | Researcher | F-08, F-09, F-10, F-22 |
| R-05 | AI service or publisher terms were breached; unpublished work is outside the researcher's control | full texts, records, working documents | unknown | high | Read terms; stop extending the practice; record outcome | Researcher with library | F-19 |
| R-06 | The dataset cannot be verified or rebuilt by others | 83,596-decision dataset | high | medium | Record deposit hashes and code commit; restore or explain the TJSP script; keep a run log | Researcher | F-12, F-23, F-30, F-31 |
| R-07 | A source blocks the project or objects to its conduct | court portals, CanLII, Rechtspraak | low–medium | medium | Honest User-Agent, verified TLS, recorded terms and rate limits | Researcher | F-01, F-02, F-11, F-23 |
| R-08 | Authorship or licence confusion blocks submission or reuse | citation files, licences | medium | medium | Decide authorship wording; one licence statement per component | Researcher; research office | F-17, F-18, F-21 |
| R-09 | The audit documents become public unintentionally | `docs/` Pages root | medium (if merged to `main`) | low–medium | Decide before merging | Researcher | F-25 |
| R-10 | Publishing a GitHub release triggers an irreversible PyPI publication and archive deposit | release workflow | low | medium | Treat release as gated by [`release-checklist.md`](release-checklist.md) | Researcher | (mechanics) |

## G. Changes made

All changes are in the working tree of the audited branch and committed locally; none is pushed. Nothing was deleted; no data, source record, scraper, coding rule or Git history was changed.

| File | Change | Reason | Verification |
|---|---|---|---|
| `tests/_safe_load.py`, `tests/test_offline_helpers.py`, `tests/test_repository_hygiene.py` | New | F-13; make the pure functions and the hygiene of the repository checkable offline | D1–D3, D9, D10; credential rules self-checked on synthetic positives; the register-consistency tests caught a swapped column in the first draft of `findings-register.csv`, corrected before commit |
| `docs/` (ten Markdown files, `findings-register.csv`) | New | Required documents; findings and standards record | links and required files checked by tests |
| `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md` | New | Missing governance files | links checked by test |
| `.env.example` | Rewritten | F-28: documented the variables the code reads; removed an unused name | D10 |
| `README.md` | Two sentences corrected | F-28: stdlib claim and a file that is not in the repository | read back |
| `requirements.txt` | Comments corrected; no versions added | F-15 | read back |
| `.github/workflows/pylint.yml`, `python-package.yml`, `verify-review-repository.yml` | `permissions: contents: read`; test step in `python-package.yml` | F-14, F-13 | D8 (parse only; not run on GitHub) |
| `CITATION.cff`, `legal-last-mile-systematic-review/CITATION.cff` | Removed `orcid: ""` | F-29 | D7, D5 |
| `.gitignore` | One exception added for `docs/findings-register.csv` | the `*.csv` rule would have kept the register out of Git (F-24) | `git check-ignore` |

**Deliberately not changed:** scrapers (TLS, User-Agent, paths, rate limits), the coding engine, data files, licences and authorship statements, the "absorbed before litigation" wording, the database exports. Each is a decision in section H.

## H. Outstanding decisions

| # | Decision | Why it is yours | Options | Recommendation |
|---|---|---|---|---|
| 1 | May the local commit with this audit be pushed to the working branch (which already has pull request #3 into `main` open)? | You said not to push without authorisation | push; push after edits; keep local | Read the report first; push when satisfied |
| 2 | Database exports in the public repository (F-04) | Legal and contractual; irreversible once public | (a) keep, after reading the terms; (b) replace in the working tree by IDs and hashes, keep files privately; (c) also purge history (rewrites history; separate decision) | (b) unless the terms clearly allow (a); decide on (c) only after consulting the library |
| 3 | E-mail addresses, ProQuest account identifier, Drive folder identifier (F-05 to F-07) | Privacy and access | strip from public copies; keep; replace by placeholders; restrict the folder | Check the folder's sharing first (minutes); strip e-mail and account identifiers from derived files |
| 4 | Win/loss patterns and `caebs` typo (F-08, F-09) | Changes coded results | (a) approve the fix and re-code from the deposit; (b) leave unchanged and label the outcome variable unreliable; (c) leave as is and disclose | (a), reporting the size of the change; (b) until then |
| 5 | Wording of "absorbed before litigation" (F-10) | It is your interpretation | reword as hypothesis separate from the classifier share; keep and add the evidence | reword |
| 6 | Scraper conduct (F-01, F-02, F-03, F-23) | Can change what servers return and where outputs land; touches source terms | approve code changes plus a small controlled live test; or document as known limitations | approve after the terms are recorded (decision 8) |
| 7 | Authorship, licences, ORCID, name form (F-17, F-18, F-21, F-29) | Yours and the university's | move AI tools to acknowledgement; one licence statement per component; supply ORCID | decide with the research office |
| 8 | Record the terms of each source (F-11, `source-register.md`) | Someone must read the pages | you or the library fill the register; the assistant can help structure it once the text is provided | do this before any re-collection or new release |
| 9 | Questions for EUR (standards matrix S-01 to S-06) | Only the institution can answer | ask the data steward, the ethics committee and the privacy contact: (i) is ethics review or a documented exemption needed for a project using published decisions and published literature, given party names and AI processing? (ii) which data management plan and storage rules apply, and who is the data steward? (iii) may external generative-AI services be used for licensed or unpublished material, and what disclosure is required? | ask all three |
| 10 | Should the audit documents under `docs/` be public (F-25)? | They name licence and privacy risks and `docs/` is the Pages root | merge as is; move to a non-published folder first; keep private | Your call; none of the findings is secret since the repository is public, but publication should be deliberate |
| 11 | Deposit hashes and versions (F-12) | Needs the deposits | record SHA-256, row counts and commit per deposited version | do it when you next open the deposit |
| 12 | A deviations and errors register for the dataset (`research-protocol.md` §6) | Only you know what happened | start `docs/` or `00_admin`-style registers like the review's | yes |
| 13 | Earlier open items | Still pending from previous rounds | merge pull requests #3, #8, #9 (the ruleset needs your bypass); push the `v0.2.0-interim` tag yourself; A6 tiers 2–3, A30, A32, second extractor, retrospective registration; confirm or alter the AI-drafted severity ratings; tell the supervisor about the corrected baseline in the validation memo | as before |

## I. Release-readiness

**The repository is not ready for a release or a new data deposit.** Items in [`release-checklist.md`](release-checklist.md) sections A (rights), B (privacy) and C (claims) are open or awaiting confirmation: the redistribution status of database exports, e-mail and identifier clean-up, the outcome-coding defects, the "absorbed before litigation" wording, and the per-source terms. Creating a GitHub release also publishes the package to PyPI automatically (`python-publish.yml`), so it should be the last step, not the first.

What is ready: the review's verification tooling, its registers, the new offline tests and the documentation set. None of these substitutes for the decisions in section H.

## Scope and method

**Coverage of the eleven phases.**

| Phase | Done | Main output |
|---|---|---|
| 1. Discovery and baseline | Inventory, history, CI, existing documents read; baseline verifier and tests run | sections A, D |
| 2. Transparency, protocol, provenance | Protocol, registers, changelog, version references checked | F-26, F-31, [`research-protocol.md`](research-protocol.md) |
| 3. Data management and legal-source collection | Data types, storage, personal data, licences, source terms | F-04 to F-07, F-11, F-12, F-30; [`data-management.md`](data-management.md), [`source-register.md`](source-register.md) |
| 4. Scraper quality (offline only) | Static review of 15 scripts; offline tests of parsers; no live request | F-01 to F-03, F-23; `tests/test_offline_helpers.py` |
| 5. AI use and disclosure | Inventory; exposure; gaps | F-17, F-19, F-20; [`ai-use-and-disclosure.md`](ai-use-and-disclosure.md) |
| 6. Review auditability and reporting-framework fit | Read against the review's own registers and PRISMA/PRISMA-S/SWiM references | F-26, F-27; not re-checked item by item |
| 7. Software, dependencies, security | Imports vs requirements; secrets scan; CI permissions; packaging build | F-13 to F-16 |
| 8. Licensing, citation, authorship | Licence texts, CFF validation, authorship | F-17, F-18, F-21, F-29 |
| 9. Institutional and external standards | 21 requirements located; none read in full | [`standards-matrix.md`](standards-matrix.md) |
| 10. Required documents | Written or adapted; existing review documents linked, not duplicated | `docs/`, root files |
| 11. Safe improvements | Section G | |

**What could not be done** is in [`limitations.md`](limitations.md) §3 (L-18 to L-24): no policy, licence or terms page was read; the deposits and the coded dataset were not available; scrapers were not run against live sites; Python 3.8–3.10 were not available; not every tracked file was read; and the audit was done by an AI assistant that also wrote parts of what it examined.

**How to challenge this report.** Open an issue with the finding ID (see [`../CONTRIBUTING.md`](../CONTRIBUTING.md)); run the check in the finding's *verification* column; say what you got. Corrections to this report are welcome and will be recorded, not hidden.
