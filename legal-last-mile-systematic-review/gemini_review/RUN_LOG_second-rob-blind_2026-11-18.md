# Run Log: Task D — Blind Second Risk-of-Bias Appraisal (60 Studies)

*AI-generated second-model output. Not human verification.*

- **Ledger label:** `Gemini-gemini-4-carbon-medium-second-rob-blind-2026-11-18`
- **Human-checked count for `AI_USE_LEDGER`:** `0` (AI-versus-AI check; never counted as human verification)
- **Git base commit (`main`):** `2cd44e7` (`Merge pull request #3 from jrklaus8/claude/legal-last-mile-review-spec-8ri0zs`)
- **Working branch:** `gemini/second-rob-blind-2026-11-18`

---

## 1. Model Identity, Isolation Architecture, Timing, and Telemetry

- **Interface:** Google Antigravity IDE (`run_workflow` dynamic workflow orchestrator invoking `60` isolated single-use `blind_rob_appraiser` subagents, one per study, in batches of `5`; `workspace="inherit"`, `model="inherit"`).
- **Host-verified model metadata:** Active Antigravity session model recorded in `<USER_SETTINGS_CHANGE>`: `Gemini 4 Carbon (Medium)` (`gemini-4-carbon-medium (Antigravity session inherit)`).
- **Execution window (UTC):** `2026-11-19T01:37:32Z` to `2026-11-19T02:09:16Z`.
- **Host token telemetry across all 60 subagent runs:** `input_tokens = 2,112,220`, `cache_read_tokens = 0`, `output_tokens = 463,213`.
- **Tool-isolation audit across all 60 subagent transcripts:** **`0` non-`finish` tool calls** (`[]`). Zero subagents called `read_file`, `view_file`, `grep_search`, `find_by_name`, `list_dir`, or `search_web`.

---

## 2. Blinding, Checklist Verification, and Data-Use Compliance

- **Files read before & during Task D:**
  - `00_admin/GEMINI_HANDOFF_BRIEF_2026-11-17.md` (`988b522f9d5f86c167fc913e5976cb448274fc2e6d526e0733f7c1f1baf31303`)
  - `03_extraction/second_extractor/second_extractor_sheet_BLIND_VALUES_2026-10-14.csv` (`e2d428cb8a1d399948475b65e03fd21601cb123e387f36d0206d7167d53ef443`)
  - `RISK_OF_BIAS.md` (`344d5428effdf355abe4ccdd2527fe0682172e98b294dfe15688f9eede03f86d`), `04_quality/appraisal_forms/APPRAISAL_FORM.md` (`577f8927763328b140c62d67c664fe3cb1dbfa842e0352f48bb601bcfa102535`), `04_quality/appraisal_forms/legal_institutional_evidence_appraisal_framework_form.md` (`c04f09ce3240ddeb9af92436ef6d038e6636f207682666873edd0fc9b5da1389`), and `00_admin/A9_INSTRUMENT_VERIFICATION_2026-10-04.md`
  - Official domain/item structures verified via primary guideline publications prior to running (`RoB 2` parallel 5-domain and cluster 6-domain `D1a`/`D1b` templates [Sterne et al. 2019]; `ROBINS-I` 7 domains [Sterne et al. 2016]; `JBI Analytical Cross-Sectional` 8 items and `JBI Cohort` 11 items [Moola et al. 2020]; `CASP Qualitative` 10 questions [CASP UK 2018]; `MMAT 2018` `S1–S2` + `1.1–5.5` [Hong et al. 2018]; `AMSTAR 2` 16 items with critical items `2, 4, 7, 9, 11, 13, 15` [Shea et al. 2017]).
- **Blinding strictly maintained (`100%` blind):**
  - `03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-10-04.csv` and `.xlsx` were **never** opened.
  - `03_extraction/extracted_data/extraction_database.csv` rows for `S001–S200` were **never** read.
  - `04_quality/appraisal_forms/*` study appraisal forms and batch tables (`*_batch_2026-09-28.md`) were **never** opened.
- **Data-use terms & PI authorization (Section 7.2b):** Explicit PI sign-off recorded via `ask_question` at `2026-11-18T15:00:50-05:00`. Full paper PDFs and text remain strictly local outside git; committed `gemini_review/raw/rob_<study_id>.json` files withhold copyrighted full text per Section 6 while preserving exact cryptographic digests and unedited `raw_response` JSON.

---

## 3. Per-Study Instrument Assignment & Cryptographic Hash Ledger (60 Studies)

| # | Study ID | Record ID | Blind Chosen Instrument | `file_sha256` (16-hex) | `text_sha256` (16-hex) | Subagent UUID |
|---:|---|---|---|---|---|---|
| 1 | `S037` | `R6092FE0E5919` | `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | `06fb6783ffcab2e0` | `b11b946e19e7f1ec` | `17316c04-f17e-47f9-8751-548a33e83c88` |
| 2 | `S057` | `R29C42DF9EAF6` | `RoB 2 (cluster-randomized trials variant)` | `a54d0acd82030e0d` | `7fdf2853337e4e3a` | `5cb7cc7a-1ae9-4af6-a442-d2c9b0d8f221` |
| 3 | `S085` | `R9E24EC349D72` | `RoB 2 (cluster-randomized trials variant)` | `4a223351f48dee4d` | `d4c88a652f9544d8` | `03b5377a-6e8f-49fe-b84e-f87289bac7fd` |
| 4 | `S121` | `RCA79A474E34C` | `ROBINS-I` | `800deeafef2e704a` | `9326d0be578a3244` | `ebf7088c-c583-43b8-819e-e36680a47f58` |
| 5 | `S142` | `R0A2F971E2D86` | `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | `4e5a952f1306c4d0` | `77b281fe3c86db6c` | `17af620c-53d9-4ce5-a90d-7ee75ee2e007` |
| 6 | `S143` | `R0F0103F9EB42` | `cannot_tell` | `none` | `none` | `2369f8ef-e060-41fb-a4b5-3a9c8f4758aa` |
| 7 | `S169` | `RFD8DD6384F91` | `ROBINS-I` | `26fad4e5a3cd6bfc` | `aeaa9096497c1f7f` | `8ed39ba3-c53f-4004-9c46-3fc8f9b047fe` |
| 8 | `S189` | `R23930997D036` | `MMAT (Mixed Methods Appraisal Tool)` | `1d54253730730fea` | `fa781845dcd406c3` | `2f0b41bc-847f-42cc-bf4b-f0958cc5bd07` |
| 9 | `S084` | `R205DDBDB40FB` | `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | `fee6deca3f148a1d` | `491cb0790489f6b6` | `61b8df25-eca2-4718-b58e-bfd80a9f4a44` |
| 10 | `S104` | `R38E0597A9B61` | `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | `3c21e97468bb921c` | `6aad5f1c3ac5ddc8` | `2192a2f7-fc22-4168-9317-8b89e26583d9` |
| 11 | `S149` | `R3B7D3DFF4E72` | `MMAT (Mixed Methods Appraisal Tool)` | `21b83cba9e1a22bb` | `9704b85c8aac775a` | `6e2dcf7d-5c16-404a-bbaa-3e6a851a745f` |
| 12 | `S174` | `RF18D44C79805` | `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | `c53f264065c67d5e` | `e90bb9193ba72c28` | `769395d7-3d97-4b21-87f0-07b17da7c84f` |
| 13 | `S178` | `R8C5602D36BCD` | `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | `2f25a5ca9efd698e` | `d193e7ed158c8bad` | `5ddcd341-a50f-4e25-9854-8e2e47e8e33c` |
| 14 | `S019` | `R5D8BA8CBD832` | `AMSTAR 2` | `1ed88e5f5d350a62` | `1c258a0e9ee881e5` | `ade4bb12-c0e3-44e0-863b-5985f4fb3951` |
| 15 | `S052` | `R172DC9C2AD24` | `AMSTAR 2` | `f5a75821a7b184df` | `c7c55cf69b89f3ad` | `3d5d7f26-9cfa-4e78-96a6-66b5c9caeb84` |
| 16 | `S116` | `RC738D26100A7` | `AMSTAR 2` | `d8cf75906350d1ea` | `076e64acbaa1f181` | `39b957f1-33b9-4d8f-ac5d-0016481a7a8f` |
| 17 | `S021` | `R2AA5F5039CC7` | `cannot_tell` | `none` | `none` | `393a7262-1b35-4f7d-b51f-95c5192818ca` |
| 18 | `S060` | `R1297067D6EE3` | `cannot_tell` | `none` | `none` | `5cd79331-4db0-4c7c-ae43-6fb1299d414e` |
| 19 | `S075` | `R746445B4F65D` | `cannot_tell` | `none` | `none` | `68a667b1-840c-4841-abe6-9de6786f8377` |
| 20 | `S150` | `R3C7BDCAC160F` | `MMAT (Mixed Methods Appraisal Tool)` | `17beec22c307d5a4` | `26d3aef632f983ba` | `2352c7b4-8c2f-4c7e-a617-aca7425c0530` |
| 21 | `S167` | `REF809F611CC2` | `cannot_tell` | `none` | `none` | `4593a109-0fe4-4553-bd15-2eb8b9037fd5` |
| 22 | `S181` | `R31E7B1B06D5E` | `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | `e4d59bbe8910a4aa` | `629a2c5ce714a0d6` | `a962668d-b873-43ee-baa8-4c837efcc9f8` |
| 23 | `S182` | `RA9578886BE98` | `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | `137ae7c2d54f6b03` | `72c085a450b5c5e3` | `9512bd50-7546-4295-b6ad-23d49625c792` |
| 24 | `S192` | `R63CBCB8C5C0B` | `JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies` | `08aedfe179704710` | `d419cc1b63c7eed0` | `4bf1b4a5-fe22-4de4-b23d-f4a12e0b406c` |
| 25 | `S013` | `RAC07BE1CB046` | `cannot_tell` | `none` | `none` | `fe0e3acc-200b-42a5-8580-19e7c77775d4` |
| 26 | `S030` | `R09518DE2A78A` | `CASP Qualitative Checklist` | `8c202d0d2e7980b3` | `62ecb5e56033a387` | `660306f6-aaff-4c6f-8d73-dd7f47373d4b` |
| 27 | `S040` | `RC3383A9FBC47` | `cannot_tell` | `none` | `none` | `ef4079a0-c900-447f-91e0-29bd0be41995` |
| 28 | `S070` | `RC41D17900D05` | `MMAT (Mixed Methods Appraisal Tool)` | `56215cab1ffb31c9` | `a1aae762b8d31b41` | `b9b93620-7a4a-4c3a-9103-1bd4b8d6d436` |
| 29 | `S081` | `R03E54611539A` | `CASP Qualitative Checklist` | `35ba164ea903dd9e` | `dee892a3d7e73a24` | `518f6a19-fdfd-4ba1-994f-8f8a8eb5a0de` |
| 30 | `S126` | `R8D5E31FA5115` | `MMAT (Mixed Methods Appraisal Tool)` | `6c535c6f914b1bdd` | `1bc6704f0093c421` | `d8d951a6-60a8-4f21-89fb-22c9f1b14dc0` |
| 31 | `S140` | `R1FE793483944` | `MMAT (Mixed Methods Appraisal Tool)` | `d294750724d4e7ec` | `4411056016934a93` | `79ac3413-d5a6-4e76-9e63-aaf1ecb29ca2` |
| 32 | `S191` | `R85FEE8235DF2` | `MMAT (Mixed Methods Appraisal Tool)` | `4f3103e4e5d4d9ca` | `62a007844838e75d` | `996a1fa8-a030-4c39-9b12-e9627ce32478` |
| 33 | `S007` | `RA9BC8541CADC` | `cannot_tell` | `none` | `none` | `7817bfa0-71a3-47d4-8d7b-cc424961063d` |
| 34 | `S046` | `RAEC333DFD828` | `cannot_tell` | `none` | `none` | `e6235a40-adf6-4692-b1da-ab6888c73a9b` |
| 35 | `S053` | `R85EE23F80FDB` | `CASP Qualitative Checklist` | `bd1c4438e2aa8e5a` | `d22bda6916aec5b7` | `a24f7782-f451-40d9-96d6-9e5ede3b08ff` |
| 36 | `S138` | `R71511A4E582D` | `cannot_tell` | `none` | `none` | `a00c6a9d-f63c-40f6-b256-60a82226beb3` |
| 37 | `S145` | `R211E08161A0B` | `cannot_tell` | `none` | `none` | `c033ec92-ed47-4a9a-810c-94d620f8d4b7` |
| 38 | `S157` | `R8C49F531C4D5` | `CASP Qualitative Checklist` | `d6bff38df699021c` | `624702bb78147b4b` | `0de987b4-9d2c-4a0d-88e5-2cc7128ed895` |
| 39 | `S160` | `RBCA94FE579EF` | `MMAT (Mixed Methods Appraisal Tool)` | `3d3a86c8b19590f2` | `2e4a033d847ec81e` | `6b0394b1-7015-4cd6-8fe1-9490717a3e89` |
| 40 | `S179` | `RD4146C231B07` | `CASP Qualitative Checklist` | `ae835bae8c7ed04d` | `e6d1ec00cae69c85` | `420ab497-adfb-4141-83c9-be5c8b8a6a26` |
| 41 | `S063` | `RF043AAD78E8E` | `Legal Institutional Evidence Appraisal Framework` | `a44ce921a019850b` | `5431f43e72327b35` | `0de90c1f-9a15-4a46-9823-e17fe4a2f05f` |
| 42 | `S076` | `RF96F4D7A891A` | `Legal Institutional Evidence Appraisal Framework` | `505d2512b3c74a55` | `e12d896398ef6f61` | `1ed2ede3-bb0d-4bc5-b1a3-66f9c9a4a23f` |
| 43 | `S124` | `R8DC8D6A54823` | `Legal Institutional Evidence Appraisal Framework` | `7111081a8543fa55` | `a270d4a993439b52` | `449c5086-eb52-4c93-9112-f257b7273201` |
| 44 | `S146` | `R26BBC984E24B` | `Legal Institutional Evidence Appraisal Framework` | `adf2492b91309833` | `2f3f1ed8201d6669` | `06461fa9-154e-4db1-bf46-b97f19e57b6c` |
| 45 | `S148` | `R3B4E6A0D63A0` | `cannot_tell` | `none` | `none` | `aaaafb62-2cda-4c3f-b380-0a42166182a1` |
| 46 | `S196` | `RAD1230DD5FD1` | `Legal Institutional Evidence Appraisal Framework` | `44b3ca36157c5f3b` | `96d6205613a1f3ed` | `d13992c4-f87a-49de-9453-4848e33d1cb3` |
| 47 | `S198` | `R9E86C5C2D0CF` | `Legal Institutional Evidence Appraisal Framework` | `d5edec92ca359c72` | `b0e00f376712df82` | `6a3b6409-b332-4b25-8d0d-259675ca698c` |
| 48 | `S006` | `R6B4F2B51A205` | `cannot_tell` | `none` | `none` | `01afcc4d-5a6f-48fa-8d9f-b1b9b70528b4` |
| 49 | `S014` | `R8E5477234032` | `cannot_tell` | `none` | `none` | `eb1382ce-05cc-4553-ba9f-a692d209415d` |
| 50 | `S064` | `R9F1DCD966DA0` | `CASP Qualitative Checklist` | `0f516eadd9d0f17d` | `59591862c43d3af5` | `7110ad3f-31c8-4a0a-9569-c3c377e698c3` |
| 51 | `S067` | `RD8BFB5AE38C5` | `cannot_tell` | `none` | `none` | `a20b5e25-cd5f-4a2d-8d16-6ed741b6e770` |
| 52 | `S083` | `R529852719FAB` | `cannot_tell` | `none` | `none` | `1d357c00-dbf9-4c4f-8e9f-b1da7c591947` |
| 53 | `S088` | `RE5CE972CD6DB` | `cannot_tell` | `none` | `none` | `f21f8edd-5610-422b-92e8-69c7fd33a88a` |
| 54 | `S109` | `R500A70E3BC4E` | `Legal Institutional Evidence Appraisal Framework` | `37d975f02ad644aa` | `f4221329686d2f66` | `5c74a9ed-47b8-4cab-b18e-af5777891da8` |
| 55 | `S120` | `R947DFEA65396` | `Legal Institutional Evidence Appraisal Framework` | `357e2ab1e8e7818e` | `9314e2af077b3402` | `d4d5eff4-9b57-430b-835e-265510a04e88` |
| 56 | `S134` | `RF8804799E515` | `cannot_tell` | `none` | `none` | `0f3ccf1a-390e-45cd-a120-209b1de63c8f` |
| 57 | `S141` | `R2A4AE48CE394` | `CASP Qualitative Checklist` | `cc75c52512588357` | `7f2f01fa3e2daf2f` | `cbff9569-75ac-4815-aac5-3c62a6e544f3` |
| 58 | `S163` | `RC9714BB70FA1` | `CASP Qualitative Checklist` | `8966848c2c4b9b1d` | `f4ebab2983d5a953` | `8b81cd79-64d1-40c2-9545-fa7fcab56ac2` |
| 59 | `S164` | `RD51F09762BFA` | `Legal Institutional Evidence Appraisal Framework` | `ce553f8f2b17926d` | `70516e23b2a80ff5` | `4f782b8a-cd53-4f70-a785-de654825b2f8` |
| 60 | `S175` | `R8DE65838848E` | `NONE` | `031903a9e7bddd66` | `69cc44ca49020a13` | `34819326-c57b-43f8-961a-ad3787b57c19` |

---

## 4. Verbatim System Instruction & Prompt Template

### 4.1 `blind_rob_appraiser` Agent Definition

```markdown
---
name: blind_rob_appraiser
description: Independent blind risk-of-bias appraiser for Task D (60 studies); selects appraisal instrument from RISK_OF_BIAS.md and rates every domain with page-cited verbatim evidence and zero external tool calls.
tools:
    - send_message
    - view_file
    - search_web
    - schedule
    - generate_image
hidden: true
---

# Agent System Instructions

You are an independent, blind methodologist conducting Task D (blind second risk-of-bias / quality appraisal) for "The Legal Last Mile" systematic review.

HARD RULES:
1. ZERO EXTERNAL TOOL USE: Do NOT call `read_file`, `view_file`, `grep_search`, `find_by_name`, `list_dir`, `search_web`, or ANY tool other than `finish`. Reading workspace files is strictly prohibited and breaks blinding.
2. WORK STRICTLY FROM THE PROVIDED PAPER FULL TEXT:
   - If the paper text is NOT ACCESSIBLE or unreadable, set `chosen_tool` to `"cannot_tell"`, `overall_rating` to `"cannot_tell"`, all cross-tool bias fields to `"cannot_tell"`, and explain that full text was not accessible. Never guess from citation or title.
3. CLASSIFY DESIGN FIRST, THEN APPLY THE EXACT OFFICIAL CHECKLIST (`RISK_OF_BIAS.md` §§1-2):
   - Independently classify the study's empirical design from its Methods section.
   - Select the single matching instrument from `RISK_OF_BIAS.md`:
     * `"RoB 2 (parallel-trial variant)"` (5 domains: D1 randomization process; D2 deviations from intended interventions; D3 missing outcome data; D4 measurement of the outcome; D5 selection of the reported result. Overall: `"Low"`, `"Some concerns"`, `"High"`.)
     * `"RoB 2 (cluster-randomized trials variant)"` (6 domains: D1a randomization process; D1b timing of identification or recruitment of participants; D2 deviations from intended interventions; D3 missing outcome data; D4 measurement of the outcome; D5 selection of the reported result. Overall: `"Low"`, `"Some concerns"`, `"High"`.)
     * `"ROBINS-I"` (7 domains: D1 confounding; D2 selection of participants into the study; D3 classification of interventions; D4 deviations from intended interventions; D5 missing data; D6 measurement of outcomes; D7 selection of the reported result. Overall: `"Low"`, `"Moderate"`, `"Serious"`, `"Critical"`, `"No information"`. Note: requires a genuine intervention/policy comparator; do not force single-case histories into ROBINS-I.)
     * `"JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies"` (8 items: Q1 inclusion criteria clearly defined; Q2 study subjects and setting described in detail; Q3 exposure measured validly and reliably; Q4 objective standard criteria used for condition measurement; Q5 confounding factors identified; Q6 strategies to deal with confounding stated; Q7 outcomes measured validly and reliably; Q8 appropriate statistical analysis used. Item responses: `"Yes"`, `"No"`, `"Unclear"`, `"Not applicable"`. Overall judgment in JBI narrative terms: `"Low concern"`, `"Some concern"`, `"High concern"` — no numeric score.)
     * `"JBI Critical Appraisal Checklist for Cohort Studies"` (11 items Q1-Q11 rated `"Yes"`, `"No"`, `"Unclear"`, `"Not applicable"`; narrative overall judgment.)
     * `"CASP Qualitative Checklist"` (10 questions Q1-Q10: Q1 clear statement of aims; Q2 qualitative methodology appropriate; Q3 research design appropriate to aims; Q4 recruitment strategy appropriate; Q5 data collected in way that addressed research issue; Q6 researcher-participant relationship/reflexivity considered; Q7 ethical issues considered; Q8 data analysis sufficiently rigorous; Q9 clear statement of findings; Q10 how valuable is the research [narrative]. Responses Q1-Q9: `"Yes"`, `"No"`, `"Can't tell"`. Narrative overall judgment, noting count of `"Can't tell"` items per CASP guidance.)
     * `"MMAT (Mixed Methods Appraisal Tool)"` (2 screening questions S1-S2 + 5 qualitative items 1.1-1.5 + 5 quantitative items [2.1-2.5 randomized, 3.1-3.5 non-randomized, or 4.1-4.5 descriptive, matching the quantitative component] + 5 mixed-methods integration items 5.1-5.5; rated `"Yes"`, `"No"`, `"Can't tell"`. Per MMAT 2018 guidance, NEVER compute a numeric composite score; provide criterion-by-criterion ratings and a concise narrative summary.)
     * `"AMSTAR 2"` (16 items Q1-Q16, flagging the 7 critical domains: items 2, 4, 7, 9, 11, 13, 15. Overall confidence: `"High"`, `"Moderate"`, `"Low"`, `"Critically Low"`. ONLY apply to genuine systematic reviews, meta-analyses, or scoping reviews with a systematic search; NEVER apply to non-systematic narrative literature reviews.)
     * `"Legal Institutional Evidence Appraisal Framework"` (13 narrative domains from `RISK_OF_BIAS.md` §2: 1 Legal source accuracy, 2 Jurisdictional specificity, 3 Exposure definition, 4 Outcome definition, 5 Sampling transparency, 6 Selection process, 7 Measurement transparency, 8 Causal identification, 9 Treatment of confounding, 10 Institutional context, 11 Replication potential, 12 Coding transparency, 13 Researcher reflexivity. Rate each `"strong"`, `"adequate"`, `"weak"`, or `"not assessable"` with justification. Explicitly treat as a structured non-validated judgment, NEVER a numeric composite score.)
     * `"NONE"` — if the study design fits NONE of the listed instruments (e.g., pure mathematical/simulation optimization model, or non-systematic narrative review/commentary without primary empirical data or systematic search). Do NOT force an ill-fitting checklist; explain clearly why `NONE` applies.
4. COMPLETE BOTH TOOL-SPECIFIC DOMAINS AND THE 7 CROSS-TOOL SUMMARY FIELDS (`CODEBOOK.md` §8):
   - Rate every item/domain of the chosen instrument with exact page/section citations.
   - Map honestly onto `selection_bias`, `measurement_bias`, `confounding`, `attrition`, `reporting_bias`, `legal_measurement_quality`, and `outcome_measurement_quality`. Where the paper provides no information on a domain, state `"Can't tell"` / `"No information"` / `"Not assessable"` honestly rather than assuming low risk.
5. VERBATIM QUOTES ONLY: Every entry in `evidence_quotes` MUST be an exact, contiguous, character-for-character substring of the provided paper text (at least 25 characters long, no `...` ellipses, no bracketed edits, no paraphrasing), with exact `[PAGE N]` / section location.

Return the schema-validated JSON via `finish`.
```

### 4.2 Per-Study Prompt Template

```text
BLIND SECOND RISK-OF-BIAS APPRAISAL (TASK D) — STUDY {study_id}

REMINDER: Do NOT call read_file, view_file, grep_search, find_by_name, list_dir, search_web, or ANY tool other than `finish`. Reading workspace files is strictly prohibited and breaks blinding. Work ONLY from `== SOURCE PAPER FULL TEXT ==` below.

== RECORD HEADER ==
- Study ID: {study_id}
- Record ID: {record_id}
- Citation string: {citation}
- DOI: {doi}
- Retrieval status: {retrieval_status}

== APPRAISAL INSTRUCTIONS (GEMINI_HANDOFF_BRIEF §3 Task D; RISK_OF_BIAS.md §§1-2; APPRAISAL_FORM.md; CODEBOOK.md §8) ==
1. ACCESSIBILITY GATE:
   - If `Retrieval status` is `not_accessible` (or the paper text below says `[FULL TEXT NOT ACCESSIBLE]`), you MUST set `paper_read = "not accessible"`, `study_design_identified = "cannot_tell (full text not accessible)"`, `chosen_tool = "cannot_tell"`, `why_tool_chosen = "full text not accessible"`, `overall_rating = "cannot_tell"`, `domain_ratings = []`, all 7 `cross_tool_domains` fields to `"cannot_tell"`, `overall_narrative_summary = "Full text not accessible; no risk-of-bias appraisal performed."`, `where_found_summary = "not accessible"`, and `evidence_quotes = []`. NEVER guess study design or bias ratings from citation/title!

2. STEP 1 — INDEPENDENT DESIGN CLASSIFICATION & TOOL SELECTION (`RISK_OF_BIAS.md` §1):
   Classify the study's actual design from its Methods section, then select the matching appraisal tool:
   - `"RoB 2 (parallel-trial variant)"`: Individually randomized controlled trial. Rate all 5 domains (`D1` Randomization process; `D2` Deviations from intended interventions; `D3` Missing outcome data; `D4` Measurement of the outcome; `D5` Selection of the reported result) as `"Low"`, `"Some concerns"`, or `"High"`, and overall rating as `"Low"`, `"Some concerns"`, or `"High"`.
   - `"RoB 2 (cluster-randomized trials variant)"`: Cluster-randomized trial (villages, compounds, neighbourhoods, schools, utilities randomized as clusters). Rate all 6 domains (`D1a` Randomization process; `D1b` Timing of identification or recruitment of participants within clusters; `D2` Deviations from intended interventions; `D3` Missing outcome data; `D4` Measurement of the outcome; `D5` Selection of the reported result) as `"Low"`, `"Some concerns"`, or `"High"`, and overall rating as `"Low"`, `"Some concerns"`, or `"High"`.
   - `"ROBINS-I"`: Non-randomized study of an intervention / policy with a genuine comparator (DiD, IV, RDD, PSM, ITS, controlled before-after, comparative longitudinal/panel evaluation). Rate all 7 domains (`D1` Bias due to confounding; `D2` Bias in selection of participants into the study; `D3` Bias in classification of interventions; `D4` Bias due to deviations from intended interventions; `D5` Bias due to missing data; `D6` Bias in measurement of outcomes; `D7` Bias in selection of the reported result — note `No information` honestly if no pre-analysis plan/protocol exists) as `"Low"`, `"Moderate"`, `"Serious"`, `"Critical"`, or `"No information"`, and overall rating in the same vocabulary. Do NOT assign single-case histories with no comparator arm to ROBINS-I!
   - `"JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies"`: Quantitative cross-sectional survey / observational regression without a quasi-experimental intervention structure. Rate all 8 items (`Q1` Inclusion criteria in sample clearly defined; `Q2` Study subjects and setting described in detail; `Q3` Exposure measured validly and reliably; `Q4` Objective, standard criteria used for measurement of condition; `Q5` Confounding factors identified; `Q6` Strategies to deal with confounding factors stated; `Q7` Outcomes measured validly and reliably; `Q8` Appropriate statistical analysis used) as `"Yes"`, `"No"`, `"Unclear"`, or `"Not applicable"`. Provide overall narrative judgment (`"Low concern"`, `"Some concern"`, or `"High concern"` — no numeric score).
   - `"JBI Critical Appraisal Checklist for Cohort Studies"`: Observational comparative cohort design (not framed as a ROBINS-I intervention). Rate all 11 items (`Q1` Similar groups from same population; `Q2` Exposures measured similarly; `Q3` Exposure measured validly/reliably; `Q4` Confounding factors identified; `Q5` Strategies to deal with confounding stated; `Q6` Participants free of outcome at start; `Q7` Outcomes measured validly/reliably; `Q8` Follow-up time reported and sufficient; `Q9` Follow-up complete or loss explored; `Q10` Strategies to address incomplete follow-up utilized; `Q11` Appropriate statistical analysis used) as `"Yes"`, `"No"`, `"Unclear"`, or `"Not applicable"`, plus narrative overall judgment (`"Low concern"`, `"Some concern"`, `"High concern"`).
   - `"CASP Qualitative Checklist"`: Primary qualitative study (interviews, ethnography, focus groups, qualitative documentary/field case study). Rate all 10 items (`Q1` Clear statement of aims; `Q2` Qualitative methodology appropriate; `Q3` Research design appropriate to address aims; `Q4` Recruitment strategy appropriate to aims; `Q5` Data collected in a way that addressed research issue; `Q6` Relationship between researcher and participants adequately considered [reflexivity]; `Q7` Ethical issues considered; `Q8` Data analysis sufficiently rigorous; `Q9` Clear statement of findings; `Q10` How valuable is the research [narrative assessment]). Rate Q1-Q9 `"Yes"`, `"No"`, or `"Can't tell"`, and Q10 narratively; give narrative `overall_rating` (e.g. `"Low methodological concern"`, `"Moderate concern (X Can't tell / No items)"`, `"High methodological concern"` — no numeric score).
   - `"MMAT (Mixed Methods Appraisal Tool)"`: Genuine mixed-methods primary study combining qualitative AND quantitative empirical components (do NOT assign purely quantitative or purely qualitative studies to MMAT). Rate Screening `S1`-`S2`, Qualitative `1.1`-`1.5`, the matching Quantitative 5-item block (`2.1`-`2.5` randomized, `3.1`-`3.5` non-randomized, or `4.1`-`4.5` descriptive), AND Mixed-Methods integration `5.1`-`5.5` (`5.1` adequate rationale for mixed methods; `5.2` components effectively integrated; `5.3` outputs of integration adequately interpreted; `5.4` divergences/inconsistencies adequately addressed; `5.5` components adhere to quality criteria of each tradition) as `"Yes"`, `"No"`, or `"Can't tell"`. Per MMAT 2018 rules, NEVER compute a numeric score; provide a concise criterion-grounded narrative `overall_rating` noting that overall quality cannot exceed the weakest component.
   - `"AMSTAR 2"`: Secondary systematic review, meta-analysis, or scoping review with an explicit systematic search/screening method (NEVER apply AMSTAR 2 to non-systematic narrative literature reviews!). Rate all 16 items `Q1`-`Q16` (explicitly marking critical domains `Q2`, `Q4`, `Q7`, `Q9`, `Q11`, `Q13`, `Q15`) as `"Yes"`, `"Partial Yes"` (where applicable), `"No"`, or `"Not applicable (no meta-analysis)"`, and apply AMSTAR 2 overall confidence (`"High"`, `"Moderate"`, `"Low"`, `"Critically Low"`).
   - `"Legal Institutional Evidence Appraisal Framework"`: Doctrinal-empirical hybrid, jurimetric analysis, or institutional/legal-historical case study that fits NONE of the six conventional designs above. Rate all 13 narrative domains (`D1` Legal source accuracy; `D2` Jurisdictional specificity; `D3` Exposure definition; `D4` Outcome definition; `D5` Sampling transparency; `D6` Selection process; `D7` Measurement transparency; `D8` Causal identification; `D9` Treatment of confounding; `D10` Institutional context; `D11` Replication potential; `D12` Coding transparency; `D13` Researcher reflexivity) as `"strong"`, `"adequate"`, `"weak"`, or `"not assessable"`. Explicitly frame `overall_rating` as a structured non-validated judgment (NEVER a numeric composite score!).
   - `"NONE"`: Use when the study fits NONE of the listed instruments (e.g., pure mathematical/simulation optimization model with no empirical sample, or non-systematic narrative essay/review with no primary empirical method and no systematic search). Set `overall_rating = "NOT APPLICABLE (design fits no listed tool)"`, explain clearly in `why_tool_chosen` and `overall_narrative_summary` rather than forcing an inappropriate checklist, and still fill the 7 `cross_tool_domains` honestly from the paper!

3. STEP 2 — CROSS-TOOL SUMMARY DOMAINS (`CODEBOOK.md` §8) & VERBATIM QUOTES:
   - Populate `selection_bias`, `measurement_bias`, `confounding`, `attrition`, `reporting_bias`, `legal_measurement_quality` (how rigorously the legal/administrative/institutional rule or exposure was operationalized), and `outcome_measurement_quality` (how rigorously the water/sanitation outcome was measured).
   - Provide 3 to 6 exact, contiguous verbatim substrings (`>= 25` chars, zero `...` ellipses, zero bracketed edits, zero paraphrasing) from `== SOURCE PAPER FULL TEXT ==` in `evidence_quotes` with exact PDF page/section citations.

== SOURCE PAPER FULL TEXT (SHA-256: {input_sha256}{trunc_note}) ==
{paper_body}
== END SOURCE PAPER FULL TEXT ==
```

---

## 5. Run Counts & Quality-Control Audit

- **Studies attempted / completed:** `60 / 60` (`60` summary CSV rows, `60` JSON appraisals, `60` filled Markdown forms in `gemini_review/risk_of_bias/forms/`)
- **Readable verified full texts appraised:** `42 / 60`
- **Inaccessible full texts (`cannot_tell` across tool and all domains):** `18 / 60`
- **Parse / schema / quota errors:** `0`
- **Verbatim quote verification (`verify_second_ai_quotes.squash()`):** **`243 / 245` (`99.18%`)** quotes verified across the 42 readable studies (left unedited per Section 8).
