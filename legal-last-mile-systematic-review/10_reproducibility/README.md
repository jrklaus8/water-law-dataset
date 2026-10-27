# 10_reproducibility — can this be reproduced, and how far?

| File | What it is |
|---|---|
| `REPRODUCE.md` | **Start here.** The levels of reproducibility (read, verify, regenerate, re-derive from sources, redo the judgments, redo the search), what each needs, and what a recorded fresh-clone run did and did not reproduce |
| `DATA_MANIFEST.csv` | Size, shape and SHA-256 (line endings normalised) of every data file, with its role and where it came from. `verify_repository.py` fails if it is stale |
| `ENVIRONMENT.md` | The software versions the run used and which scripts need which packages |
| `requirements-reproduce.txt` | The optional packages, pinned to the versions the fresh-clone run used |
| `REPRODUCTION_RUN_2026-10-27.md` | The log of that run |

The databases are plain CSV files under version control, so `git log` is the version history. One command rebuilds every derived file and re-checks the repository: `bash code/analysis/regenerate_all.sh`.
