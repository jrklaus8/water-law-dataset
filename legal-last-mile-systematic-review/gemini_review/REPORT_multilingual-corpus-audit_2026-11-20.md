# Report: Workstream AD — Multilingual Corpus (`ES / PT / FR / SK-CZ`) Blind Full-Text Eligibility & `20`-Study Cross-Lingual Second-Extraction Audit

*AI-generated second-model output. Not human verification.*

---

## 1. Headline Findings

| Multilingual Sub-Cohort | Readable Full Texts | Gemini Narrow `include` | Gemini Narrow `exclude` |
|---|---:|---:|---:|
| **Criterion-10 Non-`EN/PT/NL` Includes (`Spanish, French, Slovak/Czech`)** | **`41`** | **`16`** | **`25` (`61.0%`)** |
| **Criterion-9 `Portuguese` / Bilingual Includes** | **`10`** | **`0`** | **`10` (`100.0%`)** |
| **Multilingual / Special-Code Exclude Decoys** | **`14`** | **`2`** | **`12` (`85.7%`)** |

- **Unscored Cross-Lingual Blind Second Extraction (`20` readable Criterion-10 Spanish/French/Slovak-Czech studies, `180` field rows):** Delivered unscored in `c10_non_en_pt_nl_second_extractor_BLIND_VALUES_2026-11-20.csv` per `GEMINI_HANDOFF_BRIEF_2026-11-17.md` §5 (`0` ceiling violations; Claude can score directly via `score_second_extractor_sheet.py` to test cross-lingual extraction accuracy).
- **Verbatim original-language quote verification:** **`512 / 514` (`99.61%`)**.
