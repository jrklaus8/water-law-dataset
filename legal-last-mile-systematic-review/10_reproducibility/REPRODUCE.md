# How far can this review be reproduced, and how?

Reproducing an AI-assisted review is not one thing. Some parts reproduce exactly on any machine in under two minutes; some need the source papers; some can only be *redone*, not re-run, because they rest on AI or human judgment. This page separates the levels so that nobody mistakes the first for the last.

**The short version.** Every number, table, register and figure can be re-derived from the stored decisions, byte for byte (the Word and figure files differ in rendering details only). The decisions themselves (the AI's screening, extraction and appraisal) cannot be re-run to the same result and have been checked by a human only in part. A passing reproduction therefore shows that the pipeline is honest about what the stored decisions say; it does not show that the decisions are right. Where they are weak, `../00_admin/WEAKNESSES.md` says so.

## The levels

| Level | What you reproduce | You need | Time | Status |
|---|---|---|---|---|
| **0. Read** | Everything the project reports | A browser | minutes | The atlas, `../START_HERE.md`, the registers |
| **1. Verify** | That the databases, the documents and the registers agree with each other and with the SHA-256 manifest | Python 3 (standard library) | about 30 s | Recorded: 204 checks pass (206 with `openpyxl`). The `verify-review-repository` GitHub Actions workflow also runs it on a clean GitHub runner (Python 3.11, `openpyxl` installed) on every push and pull request, and passed on the latest commit |
| **2. Regenerate** | Every derived table, register, report, the atlas and the figures from the stored decisions | + `openpyxl`, `python-docx`, `matplotlib` | about 90 s | Recorded: all 25 test files and 206 checks pass; 7 binary or rendered files differ (below) |
| **3. Re-derive from the sources** | Whether the extracted numbers match the papers | The papers (not in the repository) and `pdftotext` | days | Only partly possible: 31 synthesis studies have a verbatim-passage dossier with every box blank; a 60-study blind second extraction is prepared and not done |
| **4. Redo the judgments** | Screening, extraction, appraisal and direction coding by humans or another AI | The archived criteria and codebook; the ledger lists what is not archived | weeks | Not reproducible by re-running: AI decisions are not deterministic and the prompts and model versions are not recorded for most of the work. Redo a random sample and measure agreement |
| **5. Redo the search** | The 34,594 records | Institutional access to Scopus, Web of Science, ProQuest, JSTOR, HeinOnline | days | Strategies are in `../01_search/database_strategies/`; database contents change over time, so a re-run will not return the same records; SSRN and Westlaw/Lexis were never searched |

## Level 1 and 2, step by step

```bash
git clone --branch claude/legal-last-mile-review-spec-8ri0zs https://github.com/jrklaus8/water-law-dataset.git   # or the main branch once the review is merged
cd water-law-dataset/legal-last-mile-systematic-review

python3 code/analysis/verify_repository.py            # level 1: expect "N checks passed, 0 failed"

pip install -r 10_reproducibility/requirements-reproduce.txt
bash code/analysis/regenerate_all.sh                   # level 2: rebuilds everything, runs the tests, then the verifier
git status --short                                     # expect only the files listed below
```

What the verifier checks: the headline figures re-derived from the CSV databases; that the databases agree with each other; that each current-status document quotes the computed figure; that every generated file (the registers, the study audit trail, the START_HERE figures, the manifest) is exactly what its generator writes today. Change one byte of a data file and it says which file.

To confirm you hold the analysed files, compare `DATA_MANIFEST.csv`: it lists the size, shape and SHA-256 (line endings normalised to LF) of 477 data files, including the untouched raw search exports and the 295 raw outputs of the independent AI model runs.

## What differs after regenerating, and why

On the recorded run, after `regenerate_all.sh` only these tracked files differed from the committed versions:

| Files | Difference | Why |
|---|---|---|
| `06_outputs/figures/fig1` to `fig5` (SVG) | Path coordinates and clip-path ids; the text in every figure is identical | matplotlib draws the same chart slightly differently in different versions |
| `06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.html` | The same differences, because it embeds the SVGs | as above |
| `06_outputs/EXECUTIVE_SUMMARY_2026-10-14.docx` | File size and embedded figure data | python-docx and matplotlib versions |

Every CSV, JSON, Markdown file, the atlas, the registers and the manifest came out byte-identical. If your run differs elsewhere, that is a finding: please report it with `../.github/ISSUE_TEMPLATE/audit-report.yml`.

## What a reproduction does not show

- That the AI's screening, extraction or appraisal decisions are correct. The ledger and the study audit trail show how little of this a human has checked.
- That the search was complete (`W01`, `W02`, `W05` in the weakness register).
- That the recorded run is independent: it was made by the AI that wrote the code, in a container of the same family. The GitHub Actions run of the verifier is a second environment but runs the same code, on Linux and Python 3.11 only. A run on Windows or macOS, another Python version, or by someone who did not write the code is still wanted, and Windows line endings in particular have not been tested.

See `REPRODUCTION_RUN_2026-10-27.md` for the log, `ENVIRONMENT.md` for versions, and `../00_admin/AI_USE_LEDGER.md` for the AI work.
