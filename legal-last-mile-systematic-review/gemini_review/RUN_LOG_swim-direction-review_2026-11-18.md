# Run Log: Task E — Adversarial Review of the 31 SWiM Direction Codings

*AI-generated second-model output. Not human verification.*

- **Ledger label:** `Gemini-gemini-4-carbon-medium-swim-direction-review-2026-11-18`
- **Human-checked count for `AI_USE_LEDGER`:** `0` (AI-versus-AI check; never counted as human verification; all `ck_*` columns left untouched)
- **Git base commit (`main`):** `2cd44e7` (`Merge pull request #3 from jrklaus8/claude/legal-last-mile-review-spec-8ri0zs`)
- **Working branch:** `gemini/swim-direction-review-2026-11-18`

---

## 1. Model Identity, Two-Phase Blinding Architecture, Timing, and Telemetry

- **Interface:** Google Antigravity IDE (`run_workflow` dynamic workflow orchestrator invoking `62` isolated single-use subagents: `31` `swim_blind_reader` runs in Phase 1, followed strictly sequentially by `31` `swim_adversarial_auditor` runs in Phase 2; `workspace="inherit"`, `model="inherit"`).
- **Host-verified model metadata:** Active Antigravity session model recorded in `<USER_SETTINGS_CHANGE>`: `Gemini 4 Carbon (Medium)` (`gemini-4-carbon-medium (Antigravity session inherit)`).
- **Strict temporal separation between Phase 1 (blind) and Phase 2 (adversarial comparison):**
  - **Phase 1 window (UTC):** `2026-11-18T22:24:02Z` to `2026-11-18T22:52:53Z` (`31` blind source-paper readings completed and locked to disk before `SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv` data rows or `SWIM_31_SOURCE_VERIFICATION_DOSSIER.md` study entries were opened).
  - **Phase 2 window (UTC):** `2026-11-18T22:53:42Z` to `2026-11-18T23:16:28Z` (`31` adversarial comparisons run after `max(Phase 1) < min(Phase 2)` verified).
- **Host token telemetry across all 62 subagent runs:** `input_tokens = 2,743,065`, `cache_read_tokens = 0`, `output_tokens = 799,517`.
- **Tool-isolation audit across all 62 subagent transcripts:** **`0` non-`finish` tool calls** (`[]`).

---

## 2. Cryptographic Input Hashes (SHA-256)

- **`00_admin/GEMINI_HANDOFF_BRIEF_2026-11-17.md`:** `988b522f9d5f86c167fc913e5976cb448274fc2e6d526e0733f7c1f1baf31303`
- **`05_analysis/effect_sizes/SWIM_31_SOURCE_PDF_MANIFEST.csv`:** `75460c4c2d97eb5c4f189c3d2410d570405cbe89d592b1535a19563077366f12`
- **`05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv`:** `a8e0693cf454c4600cd7342cf63d21454b82132d8016d73445f20401baafc015`
- **`05_analysis/effect_sizes/SWIM_31_SOURCE_VERIFICATION_DOSSIER.md`:** `8be854984e0c67d2e94b54b7ade2e7b3c676f58c4afa1f82b29164845a6ff30d`

All **31 of 31** Google Drive PDFs (including `S539` via Drive ID `1KsBr7fB_mCJVGJs3Amah6WSRJsf5_Pfa` and `S1169` via Drive ID `1MmMzZ3z2JVyp3i5mqBCcbWUvgKP4266Z`) matched the exact `sha256` recorded in `SWIM_31_SOURCE_PDF_MANIFEST.csv` (`31 / 31` `manifest_sha256_match = True`). For `S1169` (Olmstead 2004, 16-page scanned JSTOR PDF without an embedded text layer), native `Windows.Media.Ocr` at 220 DPI recovered `61,356` characters across all 16 pages.

| # | Study ID | Drive File ID | `pdf_sha256` (16-hex) | `text_sha256` (16-hex) | Phase 1 Blind Subagent UUID | Phase 2 Audit Subagent UUID |
|---:|---|---|---|---|---|---|
| 1 | `S037` | `1BolXITn0UiGV9BAvWf1qL8Ac8-74acJ1` | `06fb6783ffcab2e0` (`match=True`) | `b11b946e19e7f1ec` | `7d4e50ab-e915-4164-b0b7-f928f2a4c253` | `a228f4c2-4353-487e-951f-b025a29da0d8` |
| 2 | `S057` | `13TB9VVike0m2n8jwHX9Kplk4RPI8AGpM` | `a54d0acd82030e0d` (`match=True`) | `7fdf2853337e4e3a` | `acccb1d7-bc2e-45d5-9eb0-fb9936c35de1` | `9aeeda35-d143-4db7-b718-f7866a1ee369` |
| 3 | `S084` | `1gE1-2EuY52gRivTArhRaajUg1aRr9W2Y` | `fee6deca3f148a1d` (`match=True`) | `491cb0790489f6b6` | `0b0201ca-dde1-4ae3-9822-17f352f1c877` | `71e31725-0b94-474d-8e4e-2a4c89307f26` |
| 4 | `S104` | `1k548crII0SPZT8VagB1qfNmNOw1Vkuo6` | `3c21e97468bb921c` (`match=True`) | `6aad5f1c3ac5ddc8` | `200b68d5-7f15-45cd-97b0-fc72141318e5` | `ae293134-ebb0-4373-bd15-9ac83fbeb919` |
| 5 | `S142` | `1bX785ptcsbS5fi4irjPba2tGtG6S3mnU` | `4e5a952f1306c4d0` (`match=True`) | `77b281fe3c86db6c` | `03d8016e-06f7-401d-9527-343b5def0814` | `c4faaa70-7240-407b-8147-610aee35048e` |
| 6 | `S398` | `1Uh_yV982Yy5SB0BuC2qvrlG0BkVTMygh` | `bfd40c7e490dc2bf` (`match=True`) | `f7186d48c41e2ef5` | `3e3f8aca-ee47-4b64-8732-92152280c104` | `3606619a-d156-4e2d-998a-0c5b9ae01271` |
| 7 | `S404` | `1Iv80KRYPN6vE4qkd-bU5S0BqSuk_9DvY` | `422900c3138ac65e` (`match=True`) | `f89733ebc5e2f516` | `66619cf2-4952-440f-a66e-f5ef9fd901db` | `d3ccd2f2-5f88-4709-8ba0-e53af97e95b3` |
| 8 | `S765` | `10eLEeaECPwQeri3AS2W74iZ0GksWbq0F` | `c21f8fff45e700ea` (`match=True`) | `b0a2e9ddf111211c` | `6067c8f8-aa3e-4d7c-9601-8750a2ada5e8` | `af97fee3-6c44-4fc5-b968-8ee28e6203c8` |
| 9 | `S780` | `1OTaXK1yQcOFZ1Y0od-r3N4BnZjkOZu-g` | `77b932892944f3f4` (`match=True`) | `7c9acc55c08eaa01` | `36aa63ab-d8a3-48f4-a982-5586ceb83aaa` | `a2a9687f-4239-4293-9cb6-fe6868c572b6` |
| 10 | `S882` | `1vgERrRtQtvuGTCuXdw9tVQpebWpQQ9GW` | `35d54140125beb34` (`match=True`) | `2cf0a5b83b4bca69` | `ecea6baf-cc8a-4750-9acf-d439fe63142e` | `3d9d7748-3a4e-47b6-b9dd-e316c2b748b5` |
| 11 | `S920` | `1iYEj8wwK6ZAckZ9skOhhFWFdVDocspZd` | `511d7cf3f9c66a8d` (`match=True`) | `41509e8787669919` | `6a2f467f-b88e-4f90-add5-092f586f8b2d` | `ff19badc-7687-455b-8243-9ac76e02f577` |
| 12 | `S930` | `1TaAyCtu8lCqTrPa6F1fuw7NVQttQRGfV` | `6e66fd075330f681` (`match=True`) | `2c6e1c0ad77173ee` | `877e84e9-4e3b-469f-9173-6ceca563f445` | `2542d830-e567-44ac-83f1-c1173c143402` |
| 13 | `S1122` | `1ljbhK1CFgpwDR1fVRvN6tfRBPeSakWfa` | `a6ec97a948968007` (`match=True`) | `bae52a98bafe6303` | `5c8b2a0e-f819-46de-8e78-fa6990b3cd0e` | `d1d28d47-8d68-44f6-b23e-eda7e949a12d` |
| 14 | `S085` | `1OUG3pEvzFUvyEOmC3cKB9umuTeLCGhYN` | `4a223351f48dee4d` (`match=True`) | `d4c88a652f9544d8` | `437da07b-0448-4fc0-b916-25f6d5a99529` | `be4ef5ae-21c1-4fe4-ba13-5fd5c9280102` |
| 15 | `S366` | `1stu3MeOYTPEPffQrfqEd7IrepVSxedPK` | `7b760ca094592ee1` (`match=True`) | `78f7d6c9f3e78dc9` | `d1940ddb-3d54-4358-afc0-1bd8cc3fc000` | `14465e2c-b93e-46b5-bc41-a90132651a15` |
| 16 | `S1102` | `14H6QDrJrEcqfLBjFElOvXmMGLpA30FDo` | `a23232d270b07be4` (`match=True`) | `9a8f4a304706523b` | `051e0904-fc68-40bd-a39f-4a5d80d7c0c4` | `14a84484-0821-4bf6-80b7-f1bc1b3193f2` |
| 17 | `S174` | `1hVMuZqsRPzyXqBw3Qx1LQaxAL2ykinXQ` | `c53f264065c67d5e` (`match=True`) | `e90bb9193ba72c28` | `2398108c-2cd3-4450-92f5-07f9d2227363` | `123f31ed-5dff-4d53-be68-554256f8f60f` |
| 18 | `S470` | `1-gEJiwruJDqK3YWryGedtc2mmls7E3n1` | `11862f4c64b0b58b` (`match=True`) | `005a147d611caad8` | `2d95731a-3d29-4216-8613-dae17a311d6c` | `20bebb73-3868-4a32-9396-9ddd14c27c18` |
| 19 | `S471` | `10pLNYeRRoeiWPGDt-sTyy-5fKlKkVPcN` | `dd9f12d3ac4dff72` (`match=True`) | `67cdc92b3fec0029` | `66f0a4cc-e838-4620-88f7-4bc65705d901` | `6428af2e-2bb8-47b6-ae6a-29f2e37b334f` |
| 20 | `S526` | `19s7XKgq37R-Bdfjp7KFMtZ8UgRJq2VP4` | `29144adb12650b1f` (`match=True`) | `ee6574a0567e3c70` | `88db6c01-4aba-407e-a6e0-adde7676171d` | `1a705dbd-bbbc-4bba-9407-ceeaaadfac37` |
| 21 | `S539` | `1KsBr7fB_mCJVGJs3Amah6WSRJsf5_Pfa` | `79e36164f955ad0d` (`match=True`) | `edde7dec5aabe6a8` | `b4722be3-0645-4003-a194-0e158a18221a` | `5686e166-bbe3-40d5-adfc-f297a007eef0` |
| 22 | `S593` | `1lJ6LTdbgc-l0aztpY0A0ue1yqS6lAqZb` | `8f2395fe09218ac7` (`match=True`) | `7adb99fea7b19862` | `81080703-3c7c-4e32-aef8-49ed548dd5af` | `9066b4a9-1ba7-42b9-9ddd-d7caa6cc93f0` |
| 23 | `S631` | `1VZ_w3Xoc-jW33nh1Ko-dIxhsEHAMkXAs` | `34432758c58d77f6` (`match=True`) | `0cb84d40c2defc09` | `d6883a9d-4d80-4658-8c10-5857caeeef5a` | `03a78ac4-5346-43a1-a8a7-e4055906122d` |
| 24 | `S749` | `1bP6zoBErgx7C5ryyYYJJw5Fg2vvSHlrY` | `80c40e63f6328ca1` (`match=True`) | `0ef12bfb874ac00b` | `c1145649-276a-4906-a517-2007e2cc6806` | `81b9de4b-d66e-4c3e-9d25-14a4a789da62` |
| 25 | `S879` | `1YheYJ1naNppJFurK4RjQ_FEeDigpXmcO` | `224b5b12312100f2` (`match=True`) | `a8e607b1f27146d4` | `b2fab299-64ca-4bf3-93bc-aaa31ebe431c` | `094805fa-fafc-48e9-ac2a-2e5827d79a03` |
| 26 | `S1032` | `1Z6c4rYg7Bx8_npw4zcB9B5ClxA_Us3kz` | `66af33435710d334` (`match=True`) | `bad6e29fc2feb739` | `3e0614df-ed2e-4f62-acfb-6f6088bdb33c` | `38030806-6aee-426d-a82d-de1eb4b06c52` |
| 27 | `S1038` | `1vIH4Hed15e6KfshgF9Iv9IMwsqQ99H9h` | `099ef4a30d60f176` (`match=True`) | `ccf1f39033962543` | `b6fd8024-39d4-4e47-9256-590766fb903b` | `6c82a807-c6f9-4953-99c3-ca081774a7a2` |
| 28 | `S1062` | `1f_b97XjX0nXDUMa9aSAxFPNx2guyYhHk` | `85632ea13dd17274` (`match=True`) | `12224993a114a504` | `e3d67fd9-cc65-43ad-aa70-165145f1d828` | `d4d11bfb-08c4-4d3d-b300-7061dc817138` |
| 29 | `S1146` | `1spQLMQj6hV6PEQ5swYvH4alaBhR4grWN` | `a000d1a574333641` (`match=True`) | `b8368a27fd8b3ae1` | `685116c8-1526-4a23-b0be-4221f64ee7bb` | `4c7b2ccb-f878-4c6c-88fc-35df81107d81` |
| 30 | `S1162` | `1NC5_KYJ2XfsVbYswAxaaupNcmTVxgaXE` | `e4fa2e1c84d7d0a6` (`match=True`) | `52b2e4679fd477c2` | `410503b1-ad0a-4338-b65b-bc02c353b3ed` | `244ab874-a074-4cd4-a2b3-d6353552f319` |
| 31 | `S1169` | `1MmMzZ3z2JVyp3i5mqBCcbWUvgKP4266Z` | `f5afff9ee416e1bd` (`match=True`) | `5f049d1fe53733ec` | `d3290ad2-5c48-4ae2-8fed-04dea9e99e72` | `9a625514-cbd1-40b1-84c7-1f7118d0b5c8` |

---

## 3. Verbatim Prompt Templates

### 3.1 Phase 1 Blind Reader Prompt Template (`swim_blind_reader`)

````text
BLIND SOURCE-PAPER READING (TASK E PHASE 1) — STUDY {study_id}

REMINDER: Do NOT call read_file, grep_search, find_by_name, list_dir, search_web, or ANY tool other than `finish`. Reading workspace files is strictly prohibited and breaks blinding. Evaluate ONLY the source paper text below.

== BIBLIOGRAPHIC METADATA (prior SWiM family, exposure/outcome choice, and direction coding withheld) ==
- Study ID: {study_id}
- Record ID: {record_id}
- Citation: {citation}
- DOI: {doi}

== INSTRUCTIONS ==
Read the source paper text below from scratch, completely independently of any prior extraction or synthesis coding, and identify:
1. Study design, country, population / unit of analysis, and primary analytic sample size(s) reported in the paper.
2. Whether the paper text is readable full text (`"full text"`), partial/OCR-limited (`"partial_or_scan"`), or unreadable/no text layer (`"unreadable_scan"`). If unreadable without text, do NOT guess any results—mark `headline_direction_for_household_access` as `"cannot_tell"` and explain why.
3. The **primary / headline empirical finding(s)** in the paper that examine how a legal, administrative, institutional, regulatory, utility-ownership, tariff/subsidy, land-tenure/recognition, or participation/governance factor relates to water or sanitation service access, connection, coverage, reliability, continuity, quality, or affordability.
   - List each relevant empirical finding in `findings` (include both the primary/headline specification and any important alternative specifications, outcomes, or adjusted models that show null, attenuated, or opposite-signed results!).
   - For each finding, state explicitly:
     * `exposure_and_reference`: exact exposure variable and comparator/reference group as coded by the authors.
     * `outcome_and_polarity`: exact outcome variable AND whether higher numerical values mean BETTER household access/affordability (e.g., higher piped water coverage) or WORSE household access/affordability (e.g., higher water tariff/bill burden, higher disconnection, higher service failure).
     * `exact_estimate`: verbatim statistical result (coefficient, OR, RR, DiD estimate, group means, SE/CI/t-stat/p-value, adjusted vs. unadjusted, N, and exact Table/Page).
     * `raw_sign`: `"positive"`, `"negative"`, `"null"` (statistically non-significant at conventional p < 0.05 unless authors explicitly treat otherwise—note borderline p < 0.10), `"mixed"`, or `"non_directional"`.
     * `access_valence`: in substantive household-access terms, does the focal legal/institutional mechanism/intervention correspond to `"favorable_to_access"`, `"unfavorable_to_access"`, `"null"`, `"mixed"`, or `"ambiguous_orientation"` (e.g., public vs. private ownership or decentralization where "which pole is the exposure" is symmetrical)?
4. Synthesize the overall `headline_result_summary` and `headline_direction_for_household_access` from the paper alone, plus `specification_or_coding_pitfalls` (any traps where a careless coder could flip the sign, confuse utility price with household access, over-interpret a p > 0.05 coefficient, or pick one significant row out of mostly null tables).
5. `evidence_quotes`: Provide 2 to 5 exact, contiguous verbatim substrings (`>= 25` chars, zero `...` ellipses, zero paraphrasing) from `== SOURCE PAPER TEXT ==` with exact PDF page/table locations.

== SOURCE PAPER TEXT (SHA-256: {input_sha256}{trunc_note}) ==
{paper_body}
== END SOURCE PAPER TEXT ==

````

### 3.2 Phase 2 Adversarial Auditor Prompt Template (`swim_adversarial_auditor`)

````text
ADVERSARIAL SWiM DIRECTION AUDIT (TASK E PHASE 2) — STUDY {study_id}

REMINDER: Do NOT call read_file, grep_search, find_by_name, list_dir, search_web, or ANY tool other than `finish`. Evaluate ONLY the materials below.

== 1. LOCKED PHASE 1 BLIND READING (made from the source paper alone BEFORE seeing Claude's coding) ==
{phase1_json}

== 2. CLAUDE'S STORED SWiM VERIFICATION TABLE ROW (from SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv; ck_* columns excluded) ==
{claude_row_json}

== 3. CLAUDE'S STORED DOSSIER ENTRY (from SWIM_31_SOURCE_VERIFICATION_DOSSIER.md) ==
{dossier_section}

== 4. ADVERSARIAL AUDIT INSTRUCTIONS ==
Compare Claude's stored SWiM row and dossier entry against BOTH the Phase 1 blind reading and the full source paper text below:
1. `numbers_match_paper`: `"yes"`, `"partial_or_rounding_issue"`, `"no"`, or `"cannot_tell"` (if scan without text). Explain exact printed numbers vs. stored numbers in `numerical_check_note`.
2. `raw_sign_assessment`: Is Claude's `raw_coefficient_sign` `"correct"`, `"wrong"`, `"ambiguous_multiple_models"`, or `"cannot_tell"`?
3. `substantive_direction_verdict`: Classify Claude's `substantive_direction` into EXACTLY ONE of:
   - `"supported"`: Numbers, sign, polarity, and substantive direction accurately reflect the paper's primary empirical finding.
   - `"defensible_both_ways"`: Numbers are real, but the substantive direction genuinely depends on a contestable analytic choice (e.g., exposure orientation such as public vs. private / centralization vs. decentralization, outcome polarity, choice among conflicting specifications/outcomes in the same paper, or p > 0.05 / borderline result).
   - `"unsupported"`: The paper's empirical results do not support the directional claim coded (e.g., statistically null primary result coded as directional, cherry-picked minor result against null headline models, or outcome does not measure water/sanitation access/affordability).
   - `"wrong"`: Factual misread, wrong number, inverted sign/polarity, or coding contradicts what the paper actually reports.
   - `"cannot_tell"`: Source PDF has no readable text/OCR to verify.
4. `scope_and_family_fit`: Assess whether the study's actual exposure and outcome fit its assigned SWiM `family` (`A`, `B`, or `C`) and direct household/community water/sanitation access scope (`"fits_cleanly"`, `"borderline_or_indirect_proxy"`, `"poor_fit_or_out_of_scope"`).
5. `adversarial_critique`: 3 to 6 crisp, specific sentences citing exact page/table numbers, detailing every vulnerability, alternative specification, polarity trap, or error found (or explaining why the coding holds up if `"supported"`).
6. `evidence_quotes`: 2 to 4 exact, contiguous verbatim substrings (`>= 25` chars, no `...` or paraphrasing) from `== SOURCE PAPER TEXT ==`.

== 5. SOURCE PAPER TEXT (SHA-256: {input_sha256}) ==
{paper_body}
== END SOURCE PAPER TEXT ==

````

---

## 4. Data-Use Terms, Copyright Redaction, and Counts

- **Data-use authorization (Section 7.2b):** Authorized by PI (`CK` / `jrklaus8`) at `2026-11-18T15:00:50-05:00` for isolated Antigravity subagent execution.
- **Copyright redaction (Section 6 vs. Section 7.2a):** All 62 files in `gemini_review/raw/swim_<study_id>_phase<1|2>.json` preserve 100% unedited `raw_response` objects and SHA-256 digests while withholding copyrighted paper bodies (and long dossier excerpts) from the public repository; unredacted copies remain local in scratch storage.
- **Counts:**
  - Phase 1 blind readings: `31` attempted, `31` completed (`31` `high` confidence), `0` errors.
  - Phase 2 adversarial audits: `31` attempted, `31` completed (`16` `supported`, `13` `defensible_both_ways`, `2` `unsupported`, `0` `wrong`, `0` `cannot_tell`), `0` errors.
  - Automated quote verification (`verify_second_ai_quotes.py` `squash()`): `273 / 279` quotes verified (`97.85%`) across Phase 1 + Phase 2 (`6` `NOT FOUND IN TEXT` rows due to PDF ligatures/minus-glyph stripping/OCR spacing, reported unrepaired per Section 8).
