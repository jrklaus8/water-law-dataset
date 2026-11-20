# Report: Workstream M — Abstract Recovery & Blind Title/Abstract Screening of the `1,259` Undecided `screening_database.csv` Rows

*AI-generated second-model output. Not human verification.*

> **Why This Workstream Matters (`WEAKNESSES.md` & `PR #17`):** In `02_screening/title_abstract/screening_database.csv` (`27,481` de-duplicated records), **`1,259` records (`4.58%`)** have blank `abstract` and blank `title_abstract_decision` (`ProQuest`: `868`, `ProQuest (Sociological Abstracts)`: `335`, `WebSearch(general)`: `33`, `JSTOR`: `20`, `EXEMPLAR_SOURCES`: `1`, `Web of Science`: `1`, `HeinOnline`: `1`; `169` carry DOIs). None of those `1,259` records was ever screened by Claude or by a human. Using OpenAlex, Crossref, and EuropePMC APIs with strict bibliographic verification (`DOI` match or normalized title similarity `>= 0.92` + year/author verification, minimum `120` chars), we recovered **`70` genuine scholarly abstracts** (`5.6%` of `1,259`) and screened all `70` blind (`+ 10` self-consistency reruns) without editing `screening_database.csv`.

---

## 1. Recovery & Disposition Summary Across All `1,259` Undecided Rows

- **Total undecided blank-abstract rows in `screening_database.csv`:** `1,259`
- **Verified scholarly abstracts recovered & blind-screened:** **`70`** (`70` from the `169` original-DOI rows + `0` from non-DOI rows matched strictly by title + author + year)
- **Remaining unrecovered rows (no open scholarly abstract in OpenAlex/Crossref/EuropePMC):** **`1189`**

### 1.1 Recovered Abstracts by Metadata Source (`N = 70`)

| Recovery Source | Records (`N = 70`) |
|---|---:|
| `OpenAlex_DOI` | 70 |

### 1.2 Unrecovered Rows by Metadata Profile (`N = 1189`)

| Metadata Category | Records (`N = 1189`) |
|---|---:|
| `proquest_trade_press_or_news_wire_no_author` | 808 |
| `sociological_abstracts_unindexed_or_missing_abstract` | 248 |
| `proquest_periodical_or_trade_article_no_oa_abstract` | 60 |
| `websearch_grey_or_report_link_no_abstract` | 33 |
| `book_review_or_editorial_notice` | 26 |
| `jstor_article_or_note_no_oa_abstract` | 13 |
| `other_unrecovered_Web of Science` | 1 |

---

## 2. Blind Second-Model Title/Abstract Screening Verdicts (`N = 70`)

| Phase 5 Verdict | Narrow Rule-Type Criterion 2 (`2026-10-13`) | Literal / Plain Criterion 2 |
|---|---:|---:|
| **`include`** | **0** (`0.0%`) | **0** (`0.0%`) |
| **`unsure` (promote to full-text retrieval)** | **0** (`0.0%`) | **0** (`0.0%`) |
| **`exclude`** | **70** (`100.0%`) | **70** (`100.0%`) |

- **Total newly surfaced full-text candidates (`include` + `unsure` under narrow Criterion 2):** **`0 / 70` (`0.0%`)**
- **Self-consistency (`10` blind reruns, `SELF_CONSISTENCY_blank-abstract-recovery_2026-11-19.csv`):** **`0 / 10` flips** (`100.0%` exact stability)
- **Verbatim quote verification (`QUOTE_VERIFICATION_blank-abstract-recovery_2026-11-19.csv`):** **`184 / 184` (`100.00%`)** verified

### 2.1 Primary Exclusion Codes Among Excluded Recovered Abstracts (`N = 70`)

| Exclusion Code | Count |
|---|---:|
| `E01` | 55 |
| `E07` | 7 |
| `E05` | 7 |
| `E06` | 1 |

---

## 3. Newly Surfaced Candidate Studies (`include` or `unsure` Under Narrow Criterion 2; `N = 0`)

These `0` records sat unscreened in `screening_database.csv` solely because their export lacked an abstract; on their recovered abstracts they warrant PI full-text assessment (if the Phase 5/6 freeze is reopened or reported as a sensitivity bound):

- None.
