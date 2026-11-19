# Report: Task H — Blind Second-Model Spot-Check of Title/Abstract Exclusions (`120` Sampled + `1,259` Undecided Audit)

*AI-generated second-model output. Not human verification.*

---

## 1. Headline Results on the Fixed-Seed `120`-Record Exclude Sample (`22,557` Population)

- **Under active narrow Criterion 2 (`2026-10-13` rule-type scope):**
  - `exclude`: **`117 / 120`** (`97.5%`)
  - `unsure` (advance to full text): **`3 / 120`** (`2.5%`)
  - `include` (advance to full text): **`0 / 120`** (`0.0%`)
  - **Combined Phase 5 false-negative candidate rate (`include + unsure`):** **`3 / 120` (`2.5%`; 95% Wilson CI `0.9%–7.1%`)** — corresponding to roughly `564` candidate full-text advances across the `22,557` AI excludes (95% Wilson interval `193–1,600`, AI-vs-AI flag rate prior to human adjudication).
- **Under literal/plain Criterion 2 wording (any institutional/governance factor):**
  - `exclude`: **`115 / 120`**, `unsure`: **`5 / 120`**, `include`: **`0 / 120`** (`5 / 120 = 4.2%`, 95% Wilson CI `1.8%–9.4%`).
- **Self-consistency (`12` blind reruns):** **`0 / 12` flips**.
- **Verbatim quote verification:** **`332 / 332` (`100.00%`)** verified.

---

## 2. Records Flagged `include` or `unsure` by Gemini Under Narrow Criterion 2 (Priority for `CK` Inspection)

| Record ID | Database | Year | Title (truncated) | Claude Code | Gemini Verdict | Gemini Blind Rationale |
|---|---|---|---|---|---|---|
| `RDC29A2195184` | `ProQuest (Sociological Abstracts)` | `2015` | Who Pays, Who Benefits, Who Decides? Urban Infrastructure in Nineteenth-Cen… | `E01` | **`unsure`** (plain: `unsure`) | The abstract examines specific legal and fiscal infrastructure-financing rules—nineteenth-century property special assessments in Chicago and 1987 development impact fees in Phoeni |
| `R989C1B70DCFD` | `Scopus` | `1997` | Global urbanization and urban water: Can sustainability be afforded?… | `E05` | **`unsure`** (plain: `unsure`) | The title and abstract examine sustainable urban water infrastructure in large developing-country urban areas with a focus on affordability and financial and institutional alternat |
| `RA0DA18CA4E34` | `ProQuest` | `2002` | Economic Instruments For Improved Water Resources Management In Egypt… | `E07` | **`unsure`** (plain: `unsure`) | Although framed broadly around water resources management in Egypt (including irrigation and ambient water pollution), the abstract explicitly examines municipal water supply servi |

### 2.1 Additional Borderline Records Passing Plain Criterion 2 Only (`exclude` Narrow, `include/unsure` Plain)

- **`R53A0427D2D25`** (2017, `Scopus`, Claude `E01` -> Gemini narrow `exclude [E03]`, plain `unsure`): *Challenges of menstruation in girls and adolescents from rural communities of the Colombian Pacific; [Desafíos de la menstruación en niñas y adolescentes de comunidades rurales del Pacífico Colombiano]* — Under the narrow rule-type Criterion 2 reading, the study clearly excludes (E03) because it examines sociocultural constructs around menstruation and school menstrual hygiene conditions rather than any legal, regulatory, tenure, tariff, or administrative rule governing water or sanitation service access. Under the literal plain Criterion 2 wording covering any institutional or governance factor, it would be marked unsure because institutional officers from the Vice-ministry of Water and Sanitation and public policy management gaps were included in the qualitative inquiry alongside school restroom and water access.
- **`R848F97A4578B`** (2009, `ProQuest (Sociological Abstracts)`, Claude `E04` -> Gemini narrow `exclude [E03]`, plain `unsure`): *Fluid lives: subjectivities, gender and water in rural Bangladesh* — Under the narrow 2026-10-13 rule-type reading of Criterion 2, the study is excluded (E03) because it examines sociocultural gender ideologies, embodied subjectivities, informal norms, and socio-ecological materialities rather than any legal, administrative, regulatory, tenure/documentation, tariff, or utility-governance rule. Under the literal/broad Criterion 2 wording, references to 'water management', 'direct resource use/control/access', and 'prevailing norms and practices' could plausibly encompass informal institutional or community governance arrangements, yielding 'unsure'.

---

## 3. Programmatic Audit of the `1,259` Undecided Blank-Abstract Records in `screening_database.csv`

Read-only inspection of the `1,259` rows in `02_screening/title_abstract/screening_database.csv` with `title_abstract_decision == ""` (`UNDELIVERED_1259_BLANK_ABSTRACT_PROFILE_2026-11-19.json`) revealed three concrete findings:

1. **One `EXEMPLAR_SOURCES` record sits unscreened (`title_abstract_decision == ""`):** `1` exemplar source added from `SOURCES.md`, plus `1` lone `HeinOnline` export record, `1` `Web of Science` record, `20` `JSTOR` Law records (out of only `47` deduplicated JSTOR records in the entire database!), and `33` `WebSearch(general)` records were left permanently undecided solely because their export rows lacked an abstract.
2. **`169` of the `1,259` blank-abstract records carry a non-empty `doi`:** Their abstracts can be fetched deterministically from OpenAlex / Crossref metadata APIs without needing publisher full-text access, allowing immediate title/abstract screening.
3. **Database breakdown of the `1,259` undecided records:** `ProQuest`: `868`, `ProQuest (Sociological Abstracts)`: `335`, `WebSearch(general)`: `33`, `JSTOR`: `20`, `EXEMPLAR_SOURCES`: `1`, `HeinOnline`: `1`, `Web of Science`: `1` (`1,259 / 1,259` carry a `url`).
