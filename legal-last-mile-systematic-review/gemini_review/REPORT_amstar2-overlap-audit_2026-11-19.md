# Report: Task I — Full-Text Primary-Study Overlap & Eligibility Audit of the 18 Active `AMSTAR 2` Reviews

*AI-generated second-model output. Not human verification.*

---

## 1. Summary Findings

- **Reviews audited:** All `18` active `AMSTAR 2` reviews in `extraction_database.csv` (`S019, S027, S052, S116, S319, S325, S344, S350, S364, S370, S372, S418, S427, S438, S475, S521, S537, S1168`), expanding `AMSTAR2_OVERLAP_CHECK_2026-10-04.md` (which covered only `5` still-active reviews at reference-list level and `0` at included-studies table level).
- **Readable full texts retrieved & verified:** **`18 / 18`** (`0` `not accessible`).
- **True primary-study double-counting (included-studies tables vs `1,072` corpus):**
  - Distinct active corpus studies confirmed inside at least one review's **included primary studies**: **`30`** (`32` review–primary study pairs in `GEMINI_AMSTAR2_PRIMARY_OVERLAP_PAIRS_2026-11-19.csv`).
  - Distinct active corpus studies matched anywhere in readable reviews' **full text / reference lists** (DOI upper bound): **`14`**.
- **Methodological & scope fit across readable reviews:**
  - `narrow_criterion2_fit`: `{'borderline_narrow_c2': 11, 'passes_narrow_c2': 5, 'fails_narrow_c2_e03': 2}`
  - `amstar2_fit`: `{'borderline_scoping_realist_or_hybrid': 15, 'appropriate_systematic_or_meta': 2, 'inappropriate_not_systematic': 1}`
  - `gemini_amstar2_confidence`: `{'Critically Low': 18}`
- **Quote verification:** **`88 / 90` (`97.78%`)** verbatim quotes verified.

---

## 2. Per-Review Summary Table (`18` Active Reviews)

| Study ID | Paper Read | Self-Described Design | Narrow C2 Fit | AMSTAR 2 Fit | Confidence | Extracted / Reported Included N | Corpus Overlaps (Included Primaries) | DOI Refs Anywhere |
|---|---|---|---|---|---|---:|---|---:|
| `S015` | `full text` | systematic review (PRISMA 2020 guidelines wit | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `38 / 45` | **0** (—) | 0 |
| `S019` | `full text` | systematic review (PRISMA 2020 qualitative th | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `20 / 20` | **2** (S152; S266) | 0 |
| `S027` | `full text` | systematic review (PRISMA 2020 deductive qual | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `127 / 470` | **7** (S084; S532; S539; S561; S704; S962; S1068) | 0 |
| `S052` | `full text` | systematic review (descriptive thematic/scopi | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `48 / 37` | **4** (S355; S576; S905; S996) | 3 |
| `S116` | `full text` | systematic realist review (combined systemati | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `57 / 63` | **2** (S360; S1027) | 2 |
| `S319` | `full text` | targeted systematic review following PRISMA 2 | `passes_narrow_c2` | `appropriate_systematic_or_meta` | `Critically Low` | `8 / 8` | **2** (S190; S762) | 4 |
| `S325` | `full text` | Self-described PRISMA systematic review (in p | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `52 / 36` | **0** (—) | 0 |
| `S344` | `full text` | systematic review / systematic literature rev | `passes_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `8 / 31` | **0** (—) | 0 |
| `S350` | `full text` | scoping review | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `33 / 33` | **4** (S091; S572; S588; S940) | 3 |
| `S370` | `full text` | systematic mapping (systematic map / evidence | `fails_narrow_c2_e03` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `0 / 463` | **0** (—) | 0 |
| `S372` | `full text` | realist review | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `73 / 73` | **3** (S833; S988; S1114) | 0 |
| `S418` | `full text` | narrative review with database search (Lancet | `passes_narrow_c2` | `inappropriate_not_systematic` | `Critically Low` | `0 / 0` | **0** (—) | 0 |
| `S427` | `full text` | systematic scoping review | `fails_narrow_c2_e03` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `49 / 88` | **1** (S724) | 2 |
| `S438` | `full text` | systematic review (with thematic synthesis) | `borderline_narrow_c2` | `appropriate_systematic_or_meta` | `Critically Low` | `30 / 28` | **3** (S807; S1124; S1127) | 0 |
| `S475` | `full text` | systematic review (PRISMA 2020-guided mixed s | `passes_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `40 / 73` | **3** (S432; S905; S1139) | 0 |
| `S521` | `full text` | realist review | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `38 / 38` | **0** (—) | 0 |
| `S537` | `full text` | scoping review (following PRISMA-ScR guidelin | `borderline_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `11 / 11` | **0** (—) | 0 |
| `S1168` | `full text` | documentary and integrative review | `passes_narrow_c2` | `borderline_scoping_realist_or_hybrid` | `Critically Low` | `36 / 94` | **0** (—) | 0 |
