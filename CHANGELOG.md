# Changelog

All notable changes to the repository root (the court-decision dataset tools and documentation) are recorded here. The systematic review keeps its own, much more detailed log in [`legal-last-mile-systematic-review/CHANGELOG.md`](legal-last-mile-systematic-review/CHANGELOG.md).

The format follows [Keep a Changelog](https://keepachangelog.com/); versions follow the numbers in `pyproject.toml` and `CITATION.cff`. History before version 0.3.0 is **not reconstructed here**: it is in Git history and in the version list of the Zenodo record `10.5281/zenodo.19836413`. No entry below was written from memory.

## [Unreleased] — 2026-10-27, open-research and reproducibility audit

This entry records changes made while auditing the repository; see [`docs/audit-report.md`](docs/audit-report.md). Nothing here changes the collected data, the scrapers' behaviour or the coding rules.

### Added
- `tests/`: offline characterisation tests for helper functions of the scrapers, `utils/merge_national.py` and `utils/jurimetric_coding.py` (synthetic fixtures; no network), and repository-hygiene tests (credential patterns, environment-variable documentation, versions agree, Python 3.8 syntax, links, required files). Known defects are encoded as expected failures. `tests/_safe_load.py` loads functions from scripts that run collection code at import time without executing that code.
- `docs/`: `audit-report.md`, `findings-register.csv`, `standards-matrix.md`, `release-checklist.md`, `research-protocol.md`, `data-management.md`, `source-register.md`, `ai-use-and-disclosure.md`, `reproducibility.md`, `limitations.md`.
- `CONTRIBUTING.md`, `SECURITY.md` and this changelog.
- CI step running the offline tests (`.github/workflows/python-package.yml`).

### Changed
- `.env.example`: documents the variables the code reads (`OUTPUT_DIR`, `DATA_DIR`, `CANLII_API_KEY`, `LDH_API_KEY`, `CODED_CSV`); the unused name `LEGAL_DATA_HUNTER_API_KEY` was removed.
- `README.md`: the claim that all scrapers use only the standard library now names the one exception; the mention of `merge_all_countries.py` says that file is not in the repository.
- `requirements.txt`: comments corrected to say what is required (no versions were added).
- Workflows `pylint.yml`, `python-package.yml`, `verify-review-repository.yml`: explicit `permissions: contents: read`.
- `CITATION.cff` (root and review): removed an empty `orcid: ""`, which made both files fail validation against the Citation File Format 1.2.0 schema.

### Not changed on purpose
- Scrapers (TLS verification, User-Agent strings, default paths), the coding engine (win/loss patterns), data, licences and authorship statements. These affect collection or results or are the researcher's decisions; they are listed as findings F-01 to F-03, F-08, F-09, F-17 and F-18 awaiting approval.

## [0.3.0] — 2026-05-15

Per `CITATION.cff` and `pyproject.toml`: adds the `validation/` folder (residual audit, Cohen's kappa calculator, transformer classifier) and an improved false-positive filter for the coding engine. Details: `SUPERVISOR_REPORT_v0.3.0.md` and Git history.
