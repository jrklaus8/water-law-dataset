# Report: Task C — Blind Second Extraction of 60 Studies (540 Rows)

*AI-generated second-model output. Not human verification.*

> **Mandatory Scope Caveat (`GEMINI_HANDOFF_BRIEF_2026-11-17.md` §3 Task C & `score_second_extractor_sheet.py`):** **The 60 studies in this sample come from `S001` to `S200` only and cannot be generalised to `S201–S1169`.** Because `S001–S200` skews heavily toward recent publications compared with the later extraction batches, any agreement or disagreement rate computed after merging this blind sheet applies strictly to `S001–S200`; extrapolating it to `S201–S1169` would be an unverified assumption, not a measurement.

---

## 1. Summary Counts

- **Input sheet:** `03_extraction/second_extractor/second_extractor_sheet_BLIND_VALUES_2026-10-14.csv` (`60` studies, `9` fields per study = `540` rows; `ai_value` completely absent).
- **Output sheet:** `gemini_review/second_extractor/GEMINI_SECOND_EXTRACTOR_BLIND_2026-11-18.csv` (`540` rows with `study_id,citation,doi,field,what_to_check,second_extractor_value,comment,where_found`, directly compatible with `code/analysis/build_second_extractor_passages.py --merge`). Per Section 3 Task C, this blind output was **neither merged with `BLANK` nor scored** by Gemini.
- **Full-text accessibility:**
  - **Readable verified full texts (`full text` / `partial_or_scan`):** **`42 / 60` studies (`70.0%`, `378 / 540` rows)** — retrieved from verified Google Drive PDFs and legitimate Gold/Green Open Access endpoints (PLOS, Frontiers, MDPI, SciELO, Fiocruz Arca, EGU/HESS, RBCIAMB, PUCPR, UERJ, UWO IIPJ) and audited against Page 1–2 author + title metadata before subagent execution.
  - **Inaccessible full texts (`cannot_tell`):** **`18 / 60` studies (`30.0%`, `162 / 540` rows)** — recorded strictly as `second_extractor_value = "cannot_tell"`, `where_found = "not accessible"`, `comment = "full text not accessible"` across all 9 fields (including `publication_year` and `country`, obeying Section 0 Rule 3 & Section 5.2 never to copy metadata from the citation header when the paper itself could not be read).
- **Quote verification (`QUOTE_VERIFICATION_second-extraction-blind_2026-11-18.csv`):** **`247 / 248` (`99.60%`)** verbatim quotes verified on readable papers (`1` unverified quote left unedited per Section 8).

### 1.1 Blind `risk_of_bias_tool` Distribution Across the 42 Readable Studies

| Appraisal Instrument (`RISK_OF_BIAS.md` §1) | Readable Studies (`n = 42`) |
|---|---:|
| `CASP Qualitative Checklist` | 9 |
| `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | 9 |
| `Legal Institutional Evidence Appraisal Framework` | 8 |
| `MMAT (Mixed Methods Appraisal Tool)` | 8 |
| `AMSTAR 2` | 3 |
| `ROBINS-I` | 2 |
| `RoB 2 (cluster-randomized trials variant)` | 2 |
| `NONE` | 1 |

### 1.2 Blind `mechanism_certainty` Distribution Across the 42 Readable Studies (`CODEBOOK.md` §9)

| `mechanism_certainty` Level | Readable Studies (`n = 42`) |
|---|---:|
| `1` | 20 |
| `2` | 20 |
| `4` | 2 |

- **Design-ceiling compliance:** `0` violations (`level 4` assigned solely to the 2 cluster-randomized controlled trials `S057` and `S085`; `0` studies assigned `level 3`; `20` studies assigned `level 2` [mechanism directly observed]; `20` studies assigned `level 1` [documented association]).
- **`not reported` cells on readable studies:** `3` rows (`sample_size` on pure doctrinal/constitutional or non-sample institutional analyses where no empirical N is stated in the paper).

---

## 2. Studies That Could Not Be Read (`18 / 60`) and Why

During pre-flight verification, four potential file-identity hazards were caught and blocked before any subagent ran:
1. **`S014` (Mian et al. 2026, *Journal of Water and Health*):** Loose Google Drive title search returned an unrelated file (`2b. Erasmus School of Law Journal List 2021 (English).pdf`); purged.
2. **`S021` (dos Santos Alves Romanato et al. 2025, *World Water Policy*):** Loose Drive search returned `R31E29BB9CFED__WORLD BANK India...pdf` on pass 1 and `S306_Santos_2025_dos-santos-2025-value-co.pdf` (a different 2025 paper by Márcio Lüders dos Santos & Hupffer) on pass 2; both purged.
3. **`S013` (Paran et al. 2026, Philippines water security):** Loose Drive search returned `R133156D538B6__Water Security in Buenos Aires...` (2012); purged.
4. **`S138` (Ribeiro & Galizoni 2003, *Ambiente & Sociedade*):** Loose Drive surname search returned an unrelated genealogy PDF in Drive; purged.
5. **`S143` (Kanyesigye et al. 2026, *Utilities Policy*):** OpenAlex OA link resolved to `eawag:36048/PDF2/view` (a 15-page supplementary reference list rather than the article), while the main article datastream (`PDF/view`) is under publisher embargo (`HTTP 403 Forbidden`); purged rather than extracting from a supplement.

Several of the 18 inaccessible records carry `full_text_location = "Full text supplied by researcher via chat upload"` in `full_text_screening_database.csv` (meaning the PDF was uploaded directly to an earlier chat session and does not exist in the shared Google Drive corpus) or sit behind paywalls / `HTTP 403` bot gates:

| Study ID | Record ID | DOI | Citation (truncated) | Why Not Accessible |
|---|---|---|---|---|
| `S143` | `R0F0103F9EB42` | `10.1016/j.jup.2025.102106` | Kanyesigye C, Ferrero G, Marks SJ, Niwagaba CB, Kulabako RN, Kansiime F (2026). Evalu… | Reset before strict Page 1-2 verification |
| `S021` | `R2AA5F5039CC7` | `10.1002/wwp2.70022` | dos Santos Alves Romanato L, da Silva NF, Lucena SV, Beser de Deus LA (2025) Managing… | Reset before strict Page 1-2 verification |
| `S060` | `R1297067D6EE3` | `none` | Muyukani WP, Muthama NJ, Mutune MJ (2023). Integration and implementation of rainwate… | https://www.scopus.com/pages/publications/85181919 -> HTTPError: HTTP Error 403: Forbidden |
| `S075` | `R746445B4F65D` | `10.1088/2634-4505/ac61f8` | Armstrong A, Hope R, Koehler J (2022). Piped water revenue and investment strategies … | https://www.scopus.com/pages/publications/85130539 -> HTTPError: HTTP Error 403: Forbidden |
| `S167` | `REF809F611CC2` | `10.36941/jesr-2024-0032` | Toska M, Suparaku S, Hysa X, La Sala A (2024). A Quality Perspective of Sustainable M… | https://www.scopus.com/pages/publications/85189664 -> HTTPError: HTTP Error 403: Forbidden |
| `S013` | `RAC07BE1CB046` | `10.13189/eer.2026.140106` | Paran RC, Ocampo COV, Aparente MEA, Calibo-Senit DI, Ybañez AP (2026) Water Security … | Reset before strict Page 1-2 verification |
| `S040` | `RC3383A9FBC47` | `10.1080/13549839.2024.2376563` | Fordjour G, Anbazu J, Antwi NS, Adam MU, Asibey MO (2024). Self-help and spontaneous … | https://www.scopus.com/pages/publications/85198373 -> HTTPError: HTTP Error 403: Forbidden |
| `S007` | `RA9BC8541CADC` | `10.1080/07900627.2026.2649586` | Lindt K (2026) Community-based to centralized provision: the transformation of aflaj … | https://www.scopus.com/pages/publications/10503559 -> HTTPError: HTTP Error 403: Forbidden |
| `S046` | `RAEC333DFD828` | `10.2166/WS.2023.072` | Maskey G, Pandey CL, Giri M (2023). Water scarcity and excess: water insecurity in ci… | https://www.scopus.com/pages/publications/85160605 -> HTTPError: HTTP Error 403: Forbidden |
| `S138` | `R71511A4E582D` | `none` | Ribeiro EM, Galizoni FM (2003). Água, população rural e políticas de gestão: o caso d… | Reset before strict Page 1-2 verification |
| `S145` | `R211E08161A0B` | `10.1007/s43621-024-00538-2` | Kurniati AS, Nastiti A, Ufaira RM, Safira KF, Sakti AD (2024). Navigating the path: r… | https://www.scopus.com/pages/publications/85206361 -> HTTPError: HTTP Error 403: Forbidden |
| `S148` | `R3B4E6A0D63A0` | `10.21029/JAEL.2025.38.313` | Szekeres A (2025). From Privatisation to Remunicipalisation: How Returning to Public … | https://www.scopus.com/pages/publications/10500941 -> HTTPError: HTTP Error 403: Forbidden |
| `S006` | `R6B4F2B51A205` | `10.1007/s43621-026-03268-9` | Agyeman NK, Tantoh HB, Kamika I (2026) Assessing water security and governance comple… | https://www.scopus.com/pages/publications/10504255 -> HTTPError: HTTP Error 403: Forbidden |
| `S014` | `R8E5477234032` | `10.2166/wh.2026.151` | Mian HR, Avila J, De Coste M, Saleem S, Mohseni M, Hewage K, Sadiq R (2026) Assessing… | https://www.scopus.com/pages/publications/10504113 -> HTTPError: HTTP Error 403: Forbidden |
| `S067` | `RD8BFB5AE38C5` | `none` | Luis N, Raffa C (2022). La accion de Obras Sanitarias de la Nacion en Mendoza: infrae… | https://www.scopus.com/pages/publications/85160964 -> HTTPError: HTTP Error 403: Forbidden |
| `S083` | `R529852719FAB` | `none` | Huston A, Gaskin S, Moriarty P, Watsisi M (2021). More Sustainable Systems Through Co… | https://www.scopus.com/pages/publications/85103334 -> HTTPError: HTTP Error 403: Forbidden |
| `S088` | `RE5CE972CD6DB` | `10.1080/13549839.2016.1149456` | Otsuki K (2016). Infrastructure in informal settlements: co-production of public serv… | https://www.scopus.com/pages/publications/84959051 -> HTTPError: HTTP Error 403: Forbidden |
| `S134` | `RF8804799E515` | `none` | Britto AL, Formiga-Johnsson RM, Carneiro PRF (2016). Water supply and hydrosocial sca… | https://www.proquest.com/docview/1788483818?accoun -> URLError: <urlopen error [SSL: CERTI |

---

## 3. Notable Methodological Findings & Potential Repository Issues Flagged for PI

1. **Study tagged `NONE` for `risk_of_bias_tool`:**
- **`S175`** (Bellaubi F, Pahl-Wostl C (2017). Corruption risks, management practices, and per…): `Exploratory deterministic agent-based simulation model (ABM) built on principal-agent and game theory, parameterized and calibrated using secondary empirical data from 5 comparative case studies` — NONE applies because this study is a deterministic computational simulation (agent-based game-theoretic model in NetLogo) parameterized and calibrated using secondary summary scores from previously published case studies (Bellaubi and Visscher 2014; GII 2011; TIK 2011) rather than reporting primary empirical data collection or a systematic literature search.
2. **Cluster-randomization confirmed blindly on `S057` and `S085`:** Both `S057` (Kozole et al. 2023, village-level randomization in rural Cambodia) and `S085` (Gaikwad & Thomas 2026, cluster/settlement randomization in Mumbai) were independently assigned `RoB 2 (cluster-randomized trials variant)` rather than the parallel-trial variant.
3. **Unverified quote report (left unedited per Section 8):**
- **`S169`** (`effect_estimate`, PDF p. 11, Resultados): `NOT FOUND IN TEXT` — `significativas en la recaudación de impuesto predial en el 50.94%`
4. **Instructions that could not be followed:** `SECOND_EXTRACTOR_SOURCE_PASSAGES.md` is gitignored and exists only on the PI's local machine (as noted in `GEMINI_HANDOFF_BRIEF_2026-11-17.md` §3 Task C); Gemini worked directly from verified full-text PDFs in Google Drive and Open Access, outputting `cannot_tell` for the 18 studies whose full texts were uploaded only via prior chat sessions or paywalled.
