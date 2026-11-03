# 03_extraction — what each included study says

**The file that matters:** `extracted_data/extraction_database.csv` — one row per included report, 92 fields defined in `../CODEBOOK.md` and `../DATA_DICTIONARY.md`. Every extracted statistic carries its source location (page, table or section).

| File | What it is |
|---|---|
| `extracted_data/extraction_database.csv` | The extraction database. The last column, `record_id`, links each row to its screening record |
| `extracted_data/study_record_map.csv` | How each study ID was linked to its screening record |
| `extracted_data/linked_reports_2026-09-28.csv` | Companion papers that report the same underlying study (extraction is **per report**, not per study) |
| `extracted_data/abstract_only_fulltext_request_list_*.csv` | Studies extracted from an abstract or metadata only, listed so the full text can be found |
| `extraction_form/EXTRACTION_FORM.md` | The form the extraction followed |
| `second_extractor/` | Materials for a blind second extraction by a human: a blank sheet and a blind sheet of the AI's values (scored by `../code/analysis/score_second_extractor_sheet.py`). **Not yet done**; see `second_extractor/README.md` |

**Who checked it:** nobody yet. The AI extracted every study, largely from the full text; there is no second extractor, so no extracted value is independently verified. This is the largest open verification gap (item `A30`).
