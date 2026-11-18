# Reproducibility

How far can someone check or repeat this work, and with which commands? This page is for the repository as a whole. The systematic review has its own, more detailed guide with six levels of reproduction and a recorded fresh-clone run: [`legal-last-mile-systematic-review/10_reproducibility/REPRODUCE.md`](../legal-last-mile-systematic-review/10_reproducibility/REPRODUCE.md). This page does not repeat it.

*Written by an AI assistant (Claude Code), 2026-10-27. The results in section 3 are from runs in the audit environment and are not an independent reproduction: the same assistant wrote some of the code it ran.*

## 1. What can and cannot be reproduced

| Claim or output | Can be checked from this repository? | How |
|---|---|---|
| The review's headline numbers (included studies, screening counts, synthesis tables, atlas) | **Yes**, from the CSV databases in the repository | `python3 legal-last-mile-systematic-review/code/analysis/verify_repository.py` recomputes them; `regenerate_all.sh` rebuilds every derived file |
| That the review's data files are the ones analysed | **Yes** | SHA-256 manifest `10_reproducibility/DATA_MANIFEST.csv`; the verifier fails if it is out of date |
| That the review's AI decisions were correct | **No.** Prompts, model versions and settings are not archived and AI output is not deterministic | see `00_admin/AI_USE_LEDGER.md` |
| The helper functions of the scrapers, the merge step and the coding engine behave as characterised | **Yes**, offline | `python3 -m unittest discover -s tests -v` (synthetic fixtures; no network) |
| The 83,596-decision court dataset and its coded variables | **No.** The data are not in the repository (`data/` holds only `.gitkeep`) | obtain the deposit named in the README (Zenodo `10.5281/zenodo.19836413`, Harvard Dataverse, DANS, OSF) and compare; no hash links the deposit to a code revision (F-12) |
| Re-collecting the court data | **Not exactly.** The scrapers query live sites whose content changes; one Brazilian scraper (TJSP) is absent (F-30); runs need explicit approval and, for Canada, API keys | not run in the audit |
| Validation figures for the coding engine (κ, precision) | **Partly.** `validation/generate_all_outputs.py` regenerates the kappa files from the committed CSVs; the full coded dataset is needed for the residual audit | see pull request #9 for a kappa recomputation and documentation fixes (not merged at the time of writing) |

## 2. Environment

| Item | Recorded | Note |
|---|---|---|
| Python | `requires-python >= 3.8` (`pyproject.toml`); CI matrix 3.8–3.12; the audit ran Python 3.11.17, and the new tests also under 3.12 and 3.13; **3.8, 3.9 and 3.10 were not available and were not run** | Syntax valid for 3.8 was checked with `ast.parse(feature_version=(3, 8))` |
| Scrapers | standard library only, except `tjsp_transformation_loader.py` (pandas, openpyxl) | corrected in README and `requirements.txt` |
| Utilities and validation | pandas, openpyxl, matplotlib, numpy, python-docx, lxml; the transformer classifier also scikit-learn, transformers, datasets, torch | **versions not recorded or pinned** (F-15); the author's environment is the only source for the versions actually used |
| Review reproduction | standard library for the verifier; `10_reproducibility/requirements-reproduce.txt` and `ENVIRONMENT.md` for the rest | |
| Operating system | the scrapers' defaults assume Windows paths on the author's machine (F-03); set `OUTPUT_DIR`, `DATA_DIR`, `CODED_CSV` (see `.env.example`) | |
| Random seeds | none needed for the regex coding engine; AI steps are not seeded | |

## 3. Commands and what to expect

Run from the repository root. None needs network access or a secret.

```bash
# 1. Offline tests of helper functions and repository hygiene (about 2 seconds)
python3 -m unittest discover -s tests -v
# Expected: the run ends with "OK (expected failures=N)". Each expected failure is a documented defect (docs/findings-register.csv):
#   test_improper_* (F-08), test_f_tls_* (F-01), test_f_no_hardcoded_* (F-03), test_f_user_agent_* (F-02).
# If one of these starts to PASS, unittest reports an "unexpected success": the defect was fixed, so remove its marker.

# 2. Verify every headline figure of the review (about 30 seconds)
cd legal-last-mile-systematic-review
python3 code/analysis/verify_repository.py
# Expected last line: "<n> checks passed, 0 failed"

# 3. Rebuild every derived file of the review and run its unit tests (about 1.5 minutes; rewrites generated files)
bash code/analysis/regenerate_all.sh
# Afterwards `git status` shows only rendered files (SVG figures, report HTML) differing; see REPRODUCTION_RUN_2026-10-27.md
```

Results of these runs on 2026-10-27, and the ones that could not be run, are in [`audit-report.md`](audit-report.md), section D.

## 4. Re-collecting the court data (not run; needs approval)

1. Read [`source-register.md`](source-register.md) and the terms of each source. Do not start before the terms are recorded.
2. Create the environment: `cp .env.example .env`, set `OUTPUT_DIR`, and for Canada `CANLII_API_KEY` and `LDH_API_KEY`. Scrapers read process environment variables and do not load `.env` themselves.
3. Run a scraper (`python scrapers/brazil/tjsc_scraper.py`). Expect different results from the original: content, rankings and availability change.
4. Merge (`python utils/merge_national.py`), then code (`python utils/jurimetric_coding.py`, which currently reads a hard-coded Windows path, F-03).
5. Compare counts with the README table and, if the deposit is available, compare files by SHA-256.
6. Record the date, the commit (`git rev-parse HEAD`), the Python and package versions, and any difference found.

Before step 3, three known problems should be decided by the researcher: TLS verification is disabled in four scrapers (F-01), seven scrapers present a browser User-Agent (F-02), and no request log is kept (F-23).

## 5. Reporting a reproduction attempt

Use the issue template `.github/ISSUE_TEMPLATE/audit-report.yml`: state what you ran, the commit, the environment, what matched and what did not. A failed reproduction is a result, not a complaint.
