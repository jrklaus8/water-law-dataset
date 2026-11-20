# Report: Task K — Stratified Blind Second Extraction & Risk-of-Bias Sample on `S201–S1169` (`60` Studies / `540` Rows)

*AI-generated second-model output. Not human verification.*

> **Why This Sample Exists:** Tasks C & D (`PR #14` & `PR #15`) covered `S001–S200` only (`197` active studies = `18.4%` of the `1,072`-study corpus), leaving **`875` later studies (`S201–S1169` = `81.6%`)** with zero second-extractor or full-text second-AI risk-of-bias check. This fixed-seed (`20261119`) `60`-study stratified sample directly covers `S201–S1169` across all seven appraisal-tool strata. Per `GEMINI_HANDOFF_BRIEF_2026-11-17.md` §3 Task C, the `540` blind extraction rows (`GEMINI_S201_S1169_BLIND_EXTRACTION_2026-11-19.csv`) have **not** been merged or scored against `extraction_database.csv` by Gemini.

---

## 1. Summary Counts (`60` Sampled Studies from `S201–S1169`)

- **Readable Page 1–2 verified full texts:** **`54 / 60` (`90.0%`)**
- **Inaccessible full texts (`cannot_tell`, zero header guessing):** **`6 / 60` (`10.0%`)**
- **Sparse-audit studies included in sample:** `1`
- **`CODEBOOK.md` §9 design-ceiling violations:** `0`
- **Quote verification (`QUOTE_VERIFICATION_s201-s1169-blind-sample_2026-11-19.csv`):** **`641 / 649` (`98.77%`)** verbatim quotes verified.

### 1.1 Blind `chosen_tool` Distribution (`N = 60`)

| Blind Chosen Instrument | Studies (`N = 60`) |
|---|---:|
| `CASP Qualitative Checklist` | 13 |
| `MMAT (Mixed Methods Appraisal Tool)` | 10 |
| `Legal Institutional Evidence Appraisal Framework` | 9 |
| `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | 8 |
| `ROBINS-I` | 6 |
| `cannot_tell` | 6 |
| `AMSTAR 2` | 3 |
| `RoB 2 (cluster-randomized trials variant)` | 3 |
| `JBI Critical Appraisal Checklist for Cohort Studies` | 1 |
| `NONE` | 1 |

### 1.2 Key Corpus Verification & Google Drive File-Identity Catches

- **`S879` (`Coville et al. 2025`, 54-page NBER working paper) cluster-RCT confirmed (`RISK_OF_BIAS.md` §4 open item):** `RISK_OF_BIAS.md` §4 flagged `S879`'s cluster-randomized status as *"inferred, not confirmed, pending direct verification against the source paper."* Blind full-text appraisal independently confirmed `RoB 2 (cluster-randomized trials variant)` across all `3 / 3` sampled `RoB 2` studies (`S294`, `S366`, `S879`).
- **Google Drive PDF misfiling #1 caught blind (`S530`):** For `S530` (`Hofstetter, Bolding, & Boelens 2023`, *Water* `15(21):3736`, DOI `10.3390/w15213736`), Google Drive stores a different 2023 publication by the exact same three authors (`Hofstetter, Bolding, & Boelens 2023`, *International Journal of the Commons* `17(1):375–389`, DOI `10.5334/ijc.1256`, SHA-256 `6475bd9c...`). Both `blind_second_extractor` and `blind_rob_appraiser` enforced the strict Page 1–2 bibliographic gate, caught the DOI/journal mismatch, and recorded `cannot_tell` with zero header-guessing.
- **Google Drive PDF misfiling #2 caught in pre-flight (`S294`):** Google Drive's `S294_Quattrochi_2025_effects-community-driven-wash-intervention.pdf` actually contains `S366` (`Quattrochi et al. 2021`, *BMJ Global Health* `6:e005030`); pre-flight preparation replaced the local working copy with the genuine 17-page `2025` *PLOS Medicine* open-access PDF (`10.1371/journal.pmed.1004524`) before subagent execution.

---

## 2. Independent Design-to-Tool Shifts vs. Original `S201–S1169` Stratum (`41 / 54` Concordant)

- **`S679`**: Claude stratum `Legal Framework` -> Gemini blind `CASP Qualitative Checklist` (*Primary qualitative field and documentary case study (stakeholder interviews, CMA public participation meeting and informal 'stoep' observations, and comparative local narratives in the Breede-Overberg Water Management Area, South Africa)*)
- **`S853`**: Claude stratum `ROBINS-I` -> Gemini blind `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` (*Cross-national longitudinal macro-panel observational regression (two-way country and year fixed-effects Prais-Winsten GLS panel analysis of 135 low- and middle-income countries, nominally 1990-2015) without a discrete policy/intervention comparator*)
- **`S450`**: Claude stratum `ROBINS-I` -> Gemini blind `NONE` (*Global macro-epidemiological burden-of-disease estimation, time-series forecasting (BAPC and ARIMA), and demographic decomposition modeling study using secondary GBD 2021 and WHO country-level aggregates (2000–2030)*)
- **`S331`**: Claude stratum `JBI` -> Gemini blind `ROBINS-I` (*Retrospective non-randomized comparative administrative evaluation (cohort of failed onsite wastewater treatment systems followed for 120-day Notice of Violation compliance, analyzed via unadjusted and multivariable logistic regression)*)
- **`S1152`**: Claude stratum `CASP` -> Gemini blind `Legal Institutional Evidence Appraisal Framework` (*Single-country legal/policy institutional case study and secondary narrative policy synthesis (desk-based policy discourse critique and secondary empirical synthesis with no Methods section, no primary fieldwork, and no systematic search)*)
- **`S363`**: Claude stratum `MMAT` -> Gemini blind `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` (*Analytical cross-sectional survey study (Exploratory Factor Analysis, cluster segmentation, and multivariable binary logistic regression on N=396 survey respondents; nominally described in Abstract/Methods as mixed-methods with interviews, observations, and educational campaigns, but empirically reporting only cross-sectional quantitative survey analyses)*)
- **`S944`**: Claude stratum `Legal Framework` -> Gemini blind `MMAT (Mixed Methods Appraisal Tool)` (*Single-town mixed-methods case study combining quantitative descriptive GIS spatial analysis (2000 Census demographics and geo-coded municipal/ETJ, zoning, sewer, and highway records) with qualitative participant observation and documentary content analysis of town council deliberations*)
- **`S966`**: Claude stratum `Legal Framework` -> Gemini blind `CASP Qualitative Checklist` (*Primary qualitative multi-tier case study using Problem-Driven Governance and Political Economy (PGPE) analysis (81 semi-structured interviews and group discussions across national, regional, district, ward, and village levels, plus policy and grey-literature review)*)
- **`S904`**: Claude stratum `Legal Framework` -> Gemini blind `CASP Qualitative Checklist` (*Qualitative comparative case study (two-phase fieldwork comprising community visits, narrative walks, 72 in-person and virtual interviews, and archival research across two Cairo settlements)*)
- **`S1122`**: Claude stratum `ROBINS-I` -> Gemini blind `JBI Critical Appraisal Checklist for Cohort Studies` (*Retrospective cohort / life-course event-history survival study (semi-parametric Cox proportional hazards and Kaplan-Meier analysis of longitudinal residential and water-access trajectories reconstructed from a nationally representative 2000 retrospective survey)*)
- **`S643`**: Claude stratum `Legal Framework` -> Gemini blind `CASP Qualitative Checklist` (*Primary qualitative historical-geographical case study combining archival/policy document analysis and stakeholder/vendor interviews in Kampala (Kisenyi I and II parishes)*)
- **`S494`**: Claude stratum `MMAT` -> Gemini blind `Legal Institutional Evidence Appraisal Framework` (*Single-city institutional and urban water governance diagnostic case study combining secondary national/municipal indicator benchmarking (Trends and Pressures Framework and City Blueprint Performance Framework, N=1 city) with a semiquantitative stakeholder-informed Governance Capacity Framework (GCF) scoring matrix*)
- **`S834`**: Claude stratum `Legal Framework` -> Gemini blind `CASP Qualitative Checklist` (*Primary qualitative ethnographic case study (nearly two years of ethnographic fieldwork combining participant observation/shadowing of municipal water engineers, qualitative interviews with municipal engineers and World Bank/Castalia consultants, and qualitative documentary analysis of water-audit reports and presentations in Mumbai)*)
