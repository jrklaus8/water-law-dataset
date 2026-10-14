# EXP-002 Reproducing the coding-agreement audit

Status: PARTIAL. Data: authentic labels for 91 court decisions (71 Dutch, 20 Brazilian), case ids hashed.
Recomputes the four kappa specifications published in `validation/RESIDUAL_AUDIT.md` section 5.2 and the baseline per-category counts from `validation/kappa_results.json`.

Reproduced within rounding: n, observed agreement and kappa for all four specifications; baseline tp/fp/fn counts.
Not reproduced: bootstrap interval endpoints. See `unresolved` in the manifest.
Cross-checks: independent Python implementation, and the original `cohen_kappa` function extracted from `validation/kappa_calculator.py` (when that file sits next to this project).
Import script: `pipelines/ingest/import_water_law_validation.py` (read-only, aborts if the three source files disagree).
Not human inter-coder reliability: the second coder is an LLM under written rules.
