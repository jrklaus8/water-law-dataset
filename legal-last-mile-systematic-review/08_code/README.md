# 08_code — R templates for the meta-analysis that was not run

`R/` holds three scripts (`01_meta_analysis.R`, `02_sensitivity_analysis.R`, `03_publication_bias.R`) for the pooled analyses in `../ANALYSIS_PLAN.md`. **They have never produced a result on the real data**: they stop with an explanatory message, correctly, because no family of studies was judged poolable. They were tested on synthetic data built to exercise every branch (`R/README.md` records the bugs that found); `code/tests/test_r_templates.py` re-checks them.

`Python/` is an empty placeholder. All the Python that runs the project is in `../code/`: `code/analysis/` (figures, verification, generators), `code/screening/`, `code/search/`, and `code/provenance/` (the one-off scripts that wrote the data; read `code/provenance/README.md` before running anything there).
