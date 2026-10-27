# Environment

What the review's code needs, and the exact environment of the recorded fresh-clone run (`REPRODUCTION_RUN_2026-10-27.md`).

## What needs what

| Task | Needs |
|---|---|
| Read the atlas, the registers and every CSV | A browser; any CSV reader |
| `python3 code/analysis/verify_repository.py` (all consistency checks, the registers, the manifest) | Python 3 (tested with 3.11; other versions untested), **standard library only**. Without `openpyxl` one check (the `.xlsx` sheet sync) is skipped and says so |
| `bash code/analysis/regenerate_all.sh` (rebuild every derived file, run the unit tests, then the verifier) | The above plus `openpyxl`, `python-docx`, `matplotlib` (`requirements-reproduce.txt`) |
| Check a value against its source paper | The paper (not in the repository), and for the verbatim-passage tools `pdftotext` from poppler |
| R meta-analysis templates (`08_code/R/`) | R with `metafor`, `dplyr`, `ggplot2`. They stop with a message on the real data: nothing was poolable |
| Redo the searches | Institutional access to Scopus, Web of Science, ProQuest, JSTOR, HeinOnline (and SSRN, Westlaw/Lexis, which were never searched) |
| Redo the AI judgments | An AI system and the archived criteria; see `00_admin/AI_USE_LEDGER.md` for what is and is not archived |

## The environment of the recorded run

| Item | Value |
|---|---|
| Operating system | Linux (container) |
| Python | 3.11.17, in a fresh virtual environment created for the run |
| openpyxl | 3.1.5 |
| python-docx | 1.2.0 (with lxml 6.1.3, typing_extensions 4.16.0) |
| matplotlib | 3.11.2 (with numpy 2.4.6, pillow 13.0.0) |
| Source | A fresh `git clone` of the review branch at the commit named in the run log |
| Line endings | LF. The manifest hashes normalise CRLF to LF, so a Windows checkout with `core.autocrlf` gives the same hashes |

The scripts under `code/provenance/` are **not** part of this environment: they are a record of what was run once to write the data, hard-code paths from the original sessions, and are not re-runnable (see `code/provenance/README.md`).
