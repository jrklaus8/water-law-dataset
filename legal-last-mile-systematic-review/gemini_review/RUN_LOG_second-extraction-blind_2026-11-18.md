# Run Log: Task C — Blind Second Data Extraction (60 Studies / 540 Rows)

*AI-generated second-model output. Not human verification.*

- **Ledger label:** `Gemini-gemini-4-carbon-medium-second-extraction-blind-2026-11-18`
- **Human-checked count for `AI_USE_LEDGER`:** `0` (AI-versus-AI check; never counted as human verification; neither merged with `BLANK` sheet nor scored)
- **Git base commit (`main`):** `2cd44e7` (`Merge pull request #3 from jrklaus8/claude/legal-last-mile-review-spec-8ri0zs`)
- **Working branch:** `gemini/second-extraction-blind-2026-11-18`

---

## 1. Model Identity, Isolation Architecture, Timing, and Telemetry

- **Interface:** Google Antigravity IDE (`run_workflow` dynamic workflow orchestrator invoking `60` isolated single-use `blind_second_extractor` subagents, one per study, in batches of `5`; `workspace="inherit"`, `model="inherit"`).
- **Host-verified model metadata:** Active Antigravity session model recorded in `<USER_SETTINGS_CHANGE>`: `Gemini 4 Carbon (Medium)` (`gemini-4-carbon-medium (Antigravity session inherit)`).
- **Execution window (UTC):** `2026-11-19T01:04:48Z` to `2026-11-19T01:33:07Z`.
- **Host token telemetry across all 60 subagent runs:** `input_tokens = 2,096,763`, `cache_read_tokens = 0`, `output_tokens = 407,113`.
- **Tool-isolation audit across all 60 subagent transcripts:** **`0` non-`finish` tool calls** (`[]`). Zero subagents called `read_file`, `view_file`, `grep_search`, `find_by_name`, `list_dir`, or `search_web`.

---

## 2. Blinding & Data-Use Compliance (Sections 3, 6, 7.2b, 7.3)

- **Files read before & during Task C:**
  - `00_admin/GEMINI_HANDOFF_BRIEF_2026-11-17.md` (`988b522f9d5f86c167fc913e5976cb448274fc2e6d526e0733f7c1f1baf31303`)
  - `03_extraction/second_extractor/second_extractor_sheet_BLIND_VALUES_2026-10-14.csv` (`e2d428cb8a1d399948475b65e03fd21601cb123e387f36d0206d7167d53ef443`)
  - `CODEBOOK.md` (`ca3c1e080f9b474fbbeb70f6c14ab6c1c3ea956f4f63188602ccd87889ff7851`) and `RISK_OF_BIAS.md` (`344d5428effdf355abe4ccdd2527fe0682172e98b294dfe15688f9eede03f86d`)
  - `03_extraction/extracted_data/study_record_map.csv` (`study_id` -> `record_id` lookup) and `02_screening/full_text/full_text_screening_database.csv` (programmatically reading **only** `record_id`, `url`, and `full_text_location` for paper retrieval)
- **Blinding strictly maintained (`100%` blind):**
  - `03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-10-04.csv` and `.xlsx` were **never** opened.
  - `03_extraction/extracted_data/extraction_database.csv` rows for `S001–S200` were **never** read.
  - `04_quality/appraisal_forms/*` study appraisal files were **never** opened.
  - Per `GEMINI_HANDOFF_BRIEF_2026-11-17.md` §3 Task C, `build_second_extractor_passages.py --merge` and `score_second_extractor_sheet.py` were **not** run.
- **Data-use terms & PI authorization (Section 7.2b):** Explicit PI sign-off recorded via `ask_question` at `2026-11-18T15:00:50-05:00` authorizing full-text paper processing through isolated Antigravity subagents (`Gemini 4 Carbon (Medium)`). Full paper PDFs and extracted text stay strictly outside the git repository in local scratch storage; committed `gemini_review/raw/ext_<study_id>.json` files withhold copyrighted paper bodies per Section 6 while preserving exact `file_sha256`, `input_text_sha256`, `prompt_sha256`, and unedited `raw_response` JSON.

---

## 3. Per-Study Retrieval & Cryptographic Hash Ledger (60 Studies)

| # | Study ID | Record ID | Retrieval Status | `file_sha256` (16-hex) | `text_sha256` (16-hex) | Subagent UUID |
|---:|---|---|---|---|---|---|
| 1 | `S037` | `R6092FE0E5919` | `retrieved_swim_drive_pdf` | `06fb6783ffcab2e0` | `b11b946e19e7f1ec` | `28351acc-2dbe-4e90-8dfa-42ddd02b367e` |
| 2 | `S057` | `R29C42DF9EAF6` | `retrieved_swim_drive_pdf` | `a54d0acd82030e0d` | `7fdf2853337e4e3a` | `65bfaf23-52ec-4def-9d3b-18a9ef805708` |
| 3 | `S085` | `R9E24EC349D72` | `retrieved_swim_drive_pdf` | `4a223351f48dee4d` | `d4c88a652f9544d8` | `0ebc5be3-be86-4ff5-8c39-b3d530b5ba1b` |
| 4 | `S121` | `RCA79A474E34C` | `retrieved_drive_pdf` | `800deeafef2e704a` | `9326d0be578a3244` | `da3b9e21-8472-4250-83eb-843759c0a658` |
| 5 | `S142` | `R0A2F971E2D86` | `retrieved_swim_drive_pdf` | `4e5a952f1306c4d0` | `77b281fe3c86db6c` | `aba6019c-5f3e-4f54-b6ad-89335046a6d0` |
| 6 | `S143` | `R0F0103F9EB42` | `not_accessible` | `none` | `none` | `a51ea863-a358-41a1-bc93-5137009ebe7f` |
| 7 | `S169` | `RFD8DD6384F91` | `retrieved_drive_pdf` | `26fad4e5a3cd6bfc` | `aeaa9096497c1f7f` | `76557522-df8f-4160-8bbd-edc9f2cf073a` |
| 8 | `S189` | `R23930997D036` | `retrieved_drive_pdf` | `1d54253730730fea` | `fa781845dcd406c3` | `51bd3a0e-d2ab-4570-b9bf-5a6e81b58cba` |
| 9 | `S084` | `R205DDBDB40FB` | `retrieved_swim_drive_pdf` | `fee6deca3f148a1d` | `491cb0790489f6b6` | `07d43e9d-3735-48db-b7ab-2e18e13ee023` |
| 10 | `S104` | `R38E0597A9B61` | `retrieved_swim_drive_pdf` | `3c21e97468bb921c` | `6aad5f1c3ac5ddc8` | `c14bf6ed-221d-4ae9-a8a8-3cceebb38561` |
| 11 | `S149` | `R3B7D3DFF4E72` | `retrieved_drive_pdf` | `21b83cba9e1a22bb` | `9704b85c8aac775a` | `a8cbda1d-8799-4857-bbc4-46e2505ebb13` |
| 12 | `S174` | `RF18D44C79805` | `retrieved_swim_drive_pdf` | `c53f264065c67d5e` | `e90bb9193ba72c28` | `7567d8db-4b01-497e-924b-8b86c1132ab9` |
| 13 | `S178` | `R8C5602D36BCD` | `retrieved_drive_pdf` | `2f25a5ca9efd698e` | `d193e7ed158c8bad` | `4085bdbe-762b-47a7-a67d-9a19d33a9c11` |
| 14 | `S019` | `R5D8BA8CBD832` | `retrieved_drive_pdf` | `1ed88e5f5d350a62` | `1c258a0e9ee881e5` | `2ccc2b27-423f-4ece-bb90-ee2d70d4c268` |
| 15 | `S052` | `R172DC9C2AD24` | `retrieved_oa_pdf` | `f5a75821a7b184df` | `c7c55cf69b89f3ad` | `9fe6f657-44b8-4354-998c-6a4a457d6e89` |
| 16 | `S116` | `RC738D26100A7` | `retrieved_drive_pdf` | `d8cf75906350d1ea` | `076e64acbaa1f181` | `9a5d2887-50e8-4c0e-982c-58dddd3f0388` |
| 17 | `S021` | `R2AA5F5039CC7` | `not_accessible` | `none` | `none` | `2692bcfd-cd19-4b70-b0cb-b0c1ec5b48ae` |
| 18 | `S060` | `R1297067D6EE3` | `not_accessible` | `none` | `none` | `92acc2f1-c178-489a-9f3f-17653d097697` |
| 19 | `S075` | `R746445B4F65D` | `not_accessible` | `none` | `none` | `4c1cc597-3a0b-4e96-a0eb-c72a8fb9221f` |
| 20 | `S150` | `R3C7BDCAC160F` | `retrieved_oa_pdf` | `17beec22c307d5a4` | `26d3aef632f983ba` | `39abf68b-544a-47a9-8fe4-61ad17e5e789` |
| 21 | `S167` | `REF809F611CC2` | `not_accessible` | `none` | `none` | `19245e18-e198-4fce-8b69-64462106827c` |
| 22 | `S181` | `R31E7B1B06D5E` | `retrieved_drive_pdf` | `e4d59bbe8910a4aa` | `629a2c5ce714a0d6` | `490771d3-16b8-42bd-ae43-4a89e95f185d` |
| 23 | `S182` | `RA9578886BE98` | `retrieved_drive_pdf` | `137ae7c2d54f6b03` | `72c085a450b5c5e3` | `7dcd506b-8dbc-4f15-b48a-694c96b428bf` |
| 24 | `S192` | `R63CBCB8C5C0B` | `retrieved_drive_pdf` | `08aedfe179704710` | `d419cc1b63c7eed0` | `1228e3bc-a2a1-47eb-8657-9cb55ef52ed5` |
| 25 | `S013` | `RAC07BE1CB046` | `not_accessible` | `none` | `none` | `f9f834f1-dcd7-4442-973a-c45e88916f57` |
| 26 | `S030` | `R09518DE2A78A` | `retrieved_oa_pdf` | `8c202d0d2e7980b3` | `62ecb5e56033a387` | `c0ec702f-6001-41b8-99f8-adc1e2567dae` |
| 27 | `S040` | `RC3383A9FBC47` | `not_accessible` | `none` | `none` | `5a0f5b10-7245-48ac-a558-a81ee19fa71c` |
| 28 | `S070` | `RC41D17900D05` | `retrieved_oa_pdf` | `56215cab1ffb31c9` | `a1aae762b8d31b41` | `6eca9e8c-9f0e-406a-8ef1-7c15801492c0` |
| 29 | `S081` | `R03E54611539A` | `retrieved_oa_pdf` | `35ba164ea903dd9e` | `dee892a3d7e73a24` | `213cca44-b37a-4f23-b3bb-be0ef3ea4d30` |
| 30 | `S126` | `R8D5E31FA5115` | `retrieved_oa_pdf` | `6c535c6f914b1bdd` | `1bc6704f0093c421` | `adb57fb7-3600-4e02-ab3f-1c52cd602291` |
| 31 | `S140` | `R1FE793483944` | `retrieved_oa_pdf` | `d294750724d4e7ec` | `4411056016934a93` | `66484e53-75f8-482f-9ece-6943f1190673` |
| 32 | `S191` | `R85FEE8235DF2` | `retrieved_drive_pdf` | `4f3103e4e5d4d9ca` | `62a007844838e75d` | `22756bec-daa6-4682-a44e-cdcd60d9921a` |
| 33 | `S007` | `RA9BC8541CADC` | `not_accessible` | `none` | `none` | `c103514d-01a8-4cc9-9d15-27e8e4d3c041` |
| 34 | `S046` | `RAEC333DFD828` | `not_accessible` | `none` | `none` | `b8dfd02e-930d-470f-a0ff-3c9b2fde888b` |
| 35 | `S053` | `R85EE23F80FDB` | `retrieved_oa_pdf` | `bd1c4438e2aa8e5a` | `d22bda6916aec5b7` | `64838266-d6cd-48ed-b231-7f29fbd969b0` |
| 36 | `S138` | `R71511A4E582D` | `not_accessible` | `none` | `none` | `9892e474-ba15-4ba1-97d0-311d68eee0a9` |
| 37 | `S145` | `R211E08161A0B` | `not_accessible` | `none` | `none` | `76218d42-3bce-4d1b-9820-1b9c88c70cd4` |
| 38 | `S157` | `R8C49F531C4D5` | `retrieved_oa_pdf` | `d6bff38df699021c` | `624702bb78147b4b` | `306a0df8-dacb-42e6-9686-5cf20f5aa65a` |
| 39 | `S160` | `RBCA94FE579EF` | `retrieved_drive_pdf` | `3d3a86c8b19590f2` | `2e4a033d847ec81e` | `af99125f-994e-412d-b87a-858e5ae72829` |
| 40 | `S179` | `RD4146C231B07` | `retrieved_drive_pdf` | `ae835bae8c7ed04d` | `e6d1ec00cae69c85` | `1d4e6d06-9b69-41b9-9e46-cfc21f15f631` |
| 41 | `S063` | `RF043AAD78E8E` | `retrieved_oa_pdf` | `a44ce921a019850b` | `5431f43e72327b35` | `251ca716-8f9a-4762-a760-037ec90b4c4f` |
| 42 | `S076` | `RF96F4D7A891A` | `retrieved_oa_pdf` | `505d2512b3c74a55` | `e12d896398ef6f61` | `c36a5f2e-d1c7-4017-9133-0da15f854061` |
| 43 | `S124` | `R8DC8D6A54823` | `retrieved_oa_pdf` | `7111081a8543fa55` | `a270d4a993439b52` | `6d9a9318-3ccb-4ef9-877d-bad25e0c51f1` |
| 44 | `S146` | `R26BBC984E24B` | `retrieved_oa_pdf` | `adf2492b91309833` | `2f3f1ed8201d6669` | `e4974fb6-1ef7-490e-836a-c70828292557` |
| 45 | `S148` | `R3B4E6A0D63A0` | `not_accessible` | `none` | `none` | `a5044edf-216f-43e3-8d8c-b895bb582f0a` |
| 46 | `S196` | `RAD1230DD5FD1` | `retrieved_drive_pdf` | `44b3ca36157c5f3b` | `96d6205613a1f3ed` | `34a115a6-948f-4390-a10e-eecadec4aabf` |
| 47 | `S198` | `R9E86C5C2D0CF` | `retrieved_drive_pdf` | `d5edec92ca359c72` | `b0e00f376712df82` | `a1a57c7a-2b1f-4839-b130-9be4137f9e69` |
| 48 | `S006` | `R6B4F2B51A205` | `not_accessible` | `none` | `none` | `8d4faa80-f28e-43f3-8dd7-28e8f2ff19fe` |
| 49 | `S014` | `R8E5477234032` | `not_accessible` | `none` | `none` | `4911e148-dfcf-4940-977f-1a56a3cb9f22` |
| 50 | `S064` | `R9F1DCD966DA0` | `retrieved_oa_pdf` | `0f516eadd9d0f17d` | `59591862c43d3af5` | `15a3e7f3-d77a-471a-8752-2fa9fa61b874` |
| 51 | `S067` | `RD8BFB5AE38C5` | `not_accessible` | `none` | `none` | `63529db6-1125-4055-8c40-cd5227d774e9` |
| 52 | `S083` | `R529852719FAB` | `not_accessible` | `none` | `none` | `1b7603b2-8d88-4610-91ff-c89258ca7fb3` |
| 53 | `S088` | `RE5CE972CD6DB` | `not_accessible` | `none` | `none` | `62362363-feb2-4256-b66a-f122c30e3ab6` |
| 54 | `S109` | `R500A70E3BC4E` | `retrieved_drive_pdf` | `37d975f02ad644aa` | `f4221329686d2f66` | `43005762-4459-43a3-8419-f5533d96211b` |
| 55 | `S120` | `R947DFEA65396` | `retrieved_drive_pdf` | `357e2ab1e8e7818e` | `9314e2af077b3402` | `c3be3c7d-2a7a-4302-ac90-0004bd29a89d` |
| 56 | `S134` | `RF8804799E515` | `not_accessible` | `none` | `none` | `8550f0dc-df47-4538-9c17-55171f1fc2c8` |
| 57 | `S141` | `R2A4AE48CE394` | `retrieved_drive_pdf` | `cc75c52512588357` | `7f2f01fa3e2daf2f` | `e958d98f-86d8-4f1a-bcbc-7d3a71cd40d0` |
| 58 | `S163` | `RC9714BB70FA1` | `retrieved_oa_pdf` | `8966848c2c4b9b1d` | `f4ebab2983d5a953` | `62dffb13-c862-4040-838f-716e36bc4ebb` |
| 59 | `S164` | `RD51F09762BFA` | `retrieved_drive_pdf` | `ce553f8f2b17926d` | `70516e23b2a80ff5` | `0b31deaf-fe3f-4253-81f8-5f7f529e9961` |
| 60 | `S175` | `R8DE65838848E` | `retrieved_drive_pdf` | `031903a9e7bddd66` | `69cc44ca49020a13` | `670b1b50-1b14-494c-86e8-c0c546417bd5` |

---

## 4. Verbatim System Instruction & Prompt Template

### 4.1 `blind_second_extractor` Agent Definition

```markdown
---
name: blind_second_extractor
description: Independent blind second extractor for Task C (60 studies, 9 fields per study = 540 rows); extracts values strictly from provided full-text paper with zero external tool calls.
tools:
    - send_message
    - view_file
    - search_web
    - schedule
    - generate_image
hidden: true
---

# Agent System Instructions

You are an independent, blind methodologist conducting Task C (blind second data extraction) for "The Legal Last Mile" systematic review.

HARD RULES:
1. ZERO EXTERNAL TOOL USE: Do NOT call `read_file`, `view_file`, `grep_search`, `find_by_name`, `list_dir`, `search_web`, or ANY tool other than `finish`. Reading workspace files is strictly prohibited and breaks blinding.
2. WORK STRICTLY FROM THE PROVIDED PAPER FULL TEXT:
   - Never infer or fill a country, publication year, sample size, study design, or effect estimate from the citation header, title, memory, or context.
   - Write a field value ONLY if the provided full paper text explicitly states it; if the paper is readable and does not report a field, write `"not reported"` for that field's value and explain in `comment`.
   - If the paper full text is marked NOT ACCESSIBLE or unreadable, write `"cannot_tell"` for EVERY field's value, `"not accessible"` in `where_found`, and `"full text not accessible"` in `comment`.
3. EXACT CODEBOOK RULES (`CODEBOOK.md`):
   - `publication_year`: 4-digit year stated on the paper itself (e.g. `"2024"`), or `"not reported"` if no publication/working-paper date is printed on the document.
   - `country`: Country or countries studied as stated in the paper (e.g. `"United States"`, `"Cambodia"`, `"India"`, `"Brazil"`, or semicolon-separated list / `"Global (N countries)"` for multi-country studies), or `"not reported"`.
   - `sample_size`: Exact sample size(s) AND explicit unit of analysis as reported in the paper (e.g. `"593 households across 4 neighbourhoods"`, `"96 compounds / 1,420 households"`), or `"not reported"` (e.g. pure doctrinal/conceptual study with no sample).
   - `study_design`: Study design as the authors describe it and as operationalized in the methods section (e.g. `"Cluster-randomized controlled trial"`, `"Cross-sectional household survey with multivariable logistic regression"`, `"Qualitative case study (semi-structured interviews and document analysis)"`, `"Systematic review"`).
   - `effect_estimate`: Headline empirical result of the study regarding legal/administrative/institutional mechanisms and water/sanitation access (with exact printed numbers, units, CIs/p-values if quantitative; or concise factual headline finding if qualitative, explicitly noting `"Qualitative — no numeric effect estimate reported"` if no quantitative estimate exists), in your own words from the paper alone.
   - `risk_of_bias_tool`: Choose the single matching tool from `RISK_OF_BIAS.md` §1 based strictly on the study's actual design:
     * `"RoB 2 (parallel-trial variant)"` — individually randomized controlled trial
     * `"RoB 2 (cluster-randomized trials variant)"` — cluster-randomized trial (randomization at village, settlement, compound, or cluster level)
     * `"ROBINS-I"` — non-randomized intervention / quasi-experimental study (DiD, IV, RDD, PSM, interrupted time series, controlled before-after, panel fixed-effects evaluating a specific policy/intervention with a comparator)
     * `"JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies"` — quantitative cross-sectional / observational survey or regression without quasi-experimental intervention comparator
     * `"JBI Critical Appraisal Checklist for Cohort Studies"` — observational cohort study without quasi-experimental intervention framing
     * `"CASP Qualitative Checklist"` — primary qualitative study (interviews, ethnography, focus groups, qualitative case study)
     * `"MMAT (Mixed Methods Appraisal Tool)"` — genuine mixed-methods study combining both qualitative and quantitative primary empirical components
     * `"AMSTAR 2"` — secondary systematic review, scoping review with systematic search/screening, or meta-analysis (NEVER use AMSTAR 2 for a non-systematic narrative literature review)
     * `"Legal Institutional Evidence Appraisal Framework"` — legal-empirical, doctrinal-empirical, jurimetric, or historical-institutional study that does not fit the six conventional epidemiological/social-science designs above
     * `"NONE"` — study fits none of the listed tools (e.g. pure mathematical simulation/optimization model, or non-systematic narrative commentary/essay with no systematic search); state why in `comment`.
   - `mechanism_certainty`: Single integer `"0"`, `"1"`, `"2"`, `"3"`, or `"4"` strictly obeying `CODEBOOK.md` §9 and its design ceiling:
     * `"4"` = Experimental evidence (ONLY permitted if study is a randomized trial appraised with RoB 2)
     * `"3"` = Quasi-experimental evidence (ONLY permitted if RoB 2 trial OR ROBINS-I study with credible Low/Moderate overall risk of bias; NEVER assign 3 to cross-sectional, qualitative, mixed-methods, doctrinal, review, or Serious/Critical ROBINS-I studies)
     * `"2"` = Mechanism directly observed (empirical study directly observes/documents the legal/administrative mechanism operating on water/sanitation access)
     * `"1"` = Documented association (statistical or descriptive association between legal/institutional variable and outcome without direct observation of the administrative mechanism)
     * `"0"` = Inferred only (mechanism is posited or inferred by authors rather than empirically observed or tested)
   - `outcome_flags`: Comma-separated list using ONLY exact `CODEBOOK.md` §5 codes actually measured/analyzed in the paper (`formal_connection`, `water_access`, `sanitation_access`, `service_coverage`, `service_reliability`, `service_quantity`, `service_quality`, `affordability`, `service_continuity`, `application_success`, `refusal`, `delay`), or `"not reported"` if none apply.
   - `mechanism_flags`: Comma-separated list giving applicable top-level family code(s) (`ELIGIBILITY`, `BURDEN`, `DISCRETION_ACCOMMODATION`, `ENFORCEMENT`) followed by applicable detailed `CODEBOOK.md` §4 code(s) (`documentation`, `tenure`, `property`, `planning`, `zoning`, `building_permit`, `service_area`, `fees`, `procedural_steps`, `delay`, `discretion`, `hardship_exception`, `accommodation`, `administrative_review`, `complaint`, `judicial_review`, `disconnection`, `reconnection`, `sanction`, `participation`, `institutional_fragmentation`, `political_coordination`, `bureaucratic_assistance`) actually examined in the paper, or `"not reported"` if none apply.
4. VERBATIM QUOTES ONLY: Every entry in `evidence_quotes` MUST be an exact, contiguous, character-for-character substring of the provided paper text (at least 25 characters long, no `...` ellipses, no bracketed edits, no paraphrasing), with exact `[PAGE N]` / section / table location.

Return the schema-validated JSON via `finish`.
```

### 4.2 Per-Study Prompt Template

```text
BLIND SECOND EXTRACTION (TASK C) — STUDY {study_id}

REMINDER: Do NOT call read_file, view_file, grep_search, find_by_name, list_dir, search_web, or ANY tool other than `finish`. Reading workspace files is strictly prohibited and breaks blinding. Work ONLY from `== SOURCE PAPER FULL TEXT ==` below.

== RECORD HEADER FROM BLIND SHEET (do NOT infer values from this header if full text is inaccessible!) ==
- Study ID: {study_id}
- Record ID: {record_id}
- Citation string on blind sheet: {citation}
- DOI on blind sheet: {doi}
- Retrieval status: {retrieval_status}

== EXTRACTION RULES (GEMINI_HANDOFF_BRIEF §3 Task C & §5.2; CODEBOOK.md §§1-9; RISK_OF_BIAS.md §1) ==
1. ACCESSIBILITY GATE:
   - If `Retrieval status` is `not_accessible` (or the paper text below says `[FULL TEXT NOT ACCESSIBLE]`), you MUST set `paper_read = "not accessible"`, set `value = "cannot_tell"`, `where_found = "not accessible"`, and `comment = "full text not accessible"` for ALL 9 fields, and `evidence_quotes = []`. NEVER copy publication year or country from the citation header when the full paper was not read!
2. IF FULL TEXT IS READABLE:
   - Extract each of the 9 fields strictly from the paper text. Write a field value ONLY if the paper explicitly states it; if not stated in the paper, write `"not reported"` in `value` and explain in `comment`. Never guess or infer from context.
   - `publication_year`: 4-digit year printed on the paper/report itself (e.g. `"2024"`), or `"not reported"` if undated. Give exact page/header in `where_found`.
   - `country`: Country or countries studied as stated in the paper (use semicolon-separated names if multiple specific countries, or exact global/regional scope as stated, e.g. `"Global (48 countries)"`), or `"not reported"`.
   - `sample_size`: Exact sample size(s) AND explicit unit(s) of analysis stated in the paper (e.g. `"593 households across 4 neighbourhoods"`, `"128 municipalities; 2,048 observations (2010-2025)"`, `"32 semi-structured interviews"`), or `"not reported"` if pure doctrinal/legal analysis with no empirical sample.
   - `study_design`: Study design as the authors describe it and as operationalized in the methods section (be specific about quantitative/qualitative/quasi-experimental/experimental/review structure).
   - `effect_estimate`: Headline result of the study regarding how the legal, administrative, regulatory, institutional, tenure, tariff/subsidy, or participation factor relates to water/sanitation access/outcomes, with exact printed numbers (point estimates, units, 95% CIs, p-values, sample N) if quantitative, or concise factual headline finding if qualitative (noting `"Qualitative — no numeric effect estimate reported"` when purely qualitative), in your own words from the paper alone.
   - `risk_of_bias_tool`: Pick the single design-matched tool per `RISK_OF_BIAS.md` §1:
     * `"RoB 2 (parallel-trial variant)"` (individually randomized trial)
     * `"RoB 2 (cluster-randomized trials variant)"` (cluster-randomized trial — check unit of randomization carefully!)
     * `"ROBINS-I"` (non-randomized intervention / quasi-experimental study with a genuine comparator: DiD, IV, RDD, PSM, ITS, controlled before-after, policy panel FE)
     * `"JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies"` (quantitative cross-sectional survey / observational regression without quasi-experimental intervention comparator)
     * `"JBI Critical Appraisal Checklist for Cohort Studies"` (observational longitudinal cohort study without intervention framing)
     * `"CASP Qualitative Checklist"` (primary qualitative study: interviews, focus groups, ethnography, qualitative case study)
     * `"MMAT (Mixed Methods Appraisal Tool)"` (genuine mixed-methods study combining both qualitative and quantitative primary components)
     * `"AMSTAR 2"` (systematic review, meta-analysis, or scoping review with systematic search/screening; NEVER use for non-systematic narrative literature reviews)
     * `"Legal Institutional Evidence Appraisal Framework"` (legal-empirical, doctrinal-empirical, jurimetric, or institutional-historical study that fits none of the six conventional designs above)
     * `"NONE"` (fits none of the listed tools, e.g., pure mathematical/simulation optimization model, or non-systematic narrative review/essay without primary empirical data or systematic search — explain why in `comment`)
   - `mechanism_certainty`: Single integer `"0"`, `"1"`, `"2"`, `"3"`, or `"4"` strictly obeying `CODEBOOK.md` §9 and its design ceiling:
     * `"4"` ONLY for randomized trials (`RoB 2`)
     * `"3"` ONLY for `RoB 2` trials OR `ROBINS-I` studies with credible Low/Moderate overall risk of bias
     * All other designs (cross-sectional/JBI, cohort, qualitative/CASP, mixed-methods/MMAT, systematic review/AMSTAR 2, Legal Framework, NONE, or Serious/Critical ROBINS-I) CANNOT exceed `"2"`! (`"2"` = mechanism directly observed empirically; `"1"` = documented statistical/descriptive association; `"0"` = inferred only by authors).
   - `outcome_flags`: Comma-separated list using ONLY exact `CODEBOOK.md` §5 codes actually studied in the paper (`formal_connection`, `water_access`, `sanitation_access`, `service_coverage`, `service_reliability`, `service_quantity`, `service_quality`, `affordability`, `service_continuity`, `application_success`, `refusal`, `delay`), or `"not reported"`.
   - `mechanism_flags`: Comma-separated list of applicable top-level family codes (`ELIGIBILITY`, `BURDEN`, `DISCRETION_ACCOMMODATION`, `ENFORCEMENT`) followed by exact detailed `CODEBOOK.md` §4 codes actually studied in the paper (`documentation`, `tenure`, `property`, `planning`, `zoning`, `building_permit`, `service_area`, `fees`, `procedural_steps`, `delay`, `discretion`, `hardship_exception`, `accommodation`, `administrative_review`, `complaint`, `judicial_review`, `disconnection`, `reconnection`, `sanction`, `participation`, `institutional_fragmentation`, `political_coordination`, `bureaucratic_assistance`), or `"not reported"`.
3. `where_found` AND `evidence_quotes`:
   - Every field's `where_found` must give exact PDF page(s), section, and/or table/figure number (e.g. `"PDF p. 4, Section 2.2; Table 1, PDF p. 7"`).
   - Provide 3 to 6 exact, contiguous verbatim substrings (`>= 25` chars, zero `...` ellipses, zero bracketed changes, zero paraphrasing) from `== SOURCE PAPER FULL TEXT ==` in `evidence_quotes` backing your extracted values.

== SOURCE PAPER FULL TEXT (SHA-256: {input_sha256}{trunc_note}) ==
{paper_body}
== END SOURCE PAPER FULL TEXT ==
```

---

## 5. Run Counts & Quality-Control Audit

- **Studies attempted / completed:** `60 / 60` (`540 / 540` field rows in `GEMINI_SECOND_EXTRACTOR_BLIND_2026-11-18.csv`)
- **Readable verified full texts:** `42 / 60` (`378` extracted rows; `41` `full text`, `1` `partial_or_scan` [`S121` NBER working paper])
- **Inaccessible full texts (`cannot_tell` across all 9 fields, zero citation/header guessing):** `18 / 60` (`162` rows)
- **Parse / schema / quota errors:** `0`
- **`CODEBOOK.md` §9 design-ceiling violations:** `0`
- **Verbatim quote verification (`verify_second_ai_quotes.squash()`):** **`247 / 248` (`99.60%`)** quotes verified across the 42 readable studies (left unedited per Section 8).
