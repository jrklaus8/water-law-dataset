# Report: Workstream Z — First Empirical Source-PDF Validation of `evidence_map.csv` Controlled-Vocabulary Taxonomies & All `37` AI Overrides (`Open Items A5 & A20`)

*AI-generated second-model output. Not human verification.*

> **Why This Validation Was Needed (`WEAKNESSES.md` & `DECISIONS` Items `A5` / `A20`):** All `1,072` rows in `evidence_map.csv` (and the interactive `EVIDENCE_ATLAS_INTERACTIVE.html` built from it) carry mechanical keyword-derived labels for `mechanism_family` (`493 / 1,072 = 46.0%` collapsed into `"multiple"`), `outcome_family`, and `study_design_class`, plus `37` manual AI overrides in `family_vocabulary_overrides_2026-10-14.csv`—with **zero prior source-PDF validation**. We classified `80` studies (`37` AI overrides + `43` stratified `evidence_map` rows; **`73 / 80` readable full texts**) `100%` blind from their source PDFs (`244 / 247 = 98.79%` quotes verified).

---

## 1. Inter-Model Agreement & Cohen's Kappa (`N = 73` Readable Source PDFs)

| `evidence_map.csv` Controlled Vocabulary | Exact Agreement (`%`) | Unweighted Cohen's $\kappa$ | Key Finding |
|---|---:|---:|---|
| **`mechanism_family` (`10` categories incl. `multiple`)** | **`34.2%`** | **`0.199`** | Keyword `"multiple"` (`493` corpus rows) over-lumps single-focal-mechanism papers (`11 / 23` readable `"multiple"` studies have a single dominant primary mechanism on full text; `6` test no rule-type mechanism at all!) |
| **`outcome_family` (`5` categories incl. `multiple`)** | **`28.8%`** | **`0.116`** | Moderate divergence between `primary_connection`, `effective_access`, and `multiple` |
| **`study_design_class` (`9` categories)** | **`69.9%`** | **`0.583`** | Highest concordance, with shifts between `qualitative` and `doctrinal` / `mixed_methods` |
