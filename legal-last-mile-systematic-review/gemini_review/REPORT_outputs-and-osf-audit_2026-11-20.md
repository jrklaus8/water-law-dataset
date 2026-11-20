# Report: Workstream U — Audit of `06_outputs/` (`EVIDENCE_ATLAS_INTERACTIVE.html`, `.docx` Reports, `fig1–5.svg`, `supplementary/*.md`) & `osf_preregistration_draft.md`

*AI-generated second-model output. Not human verification.*

> **Why This Audit Was Needed:** `verify_repository.py` checks `CURRENT_FIGURES.md`, `EVIDENCE_ATLAS_INTERACTIVE.html`, and selected Markdown sections, but does **not** parse binary `.docx` Word outputs inside `06_outputs/`, does **not** check all tables inside `00_admin/preregistration/osf_preregistration_draft.md`, and does **not** scan `06_outputs/supplementary/*.md` for retired `study_id`s still presented as active included studies.

---

## 1. Critical Pre-Publication & Pre-OSF Findings (`OA-01` through `OA-06`)

### `OA-01` (CRITICAL — Fix Before Uploading Open Item `A7` to OSF!): `00_admin/preregistration/osf_preregistration_draft.md` Line 80 Contradicts Line 66 and Freezes Pre-`A28` Effect-Size Counts
- **Location:** `00_admin/preregistration/osf_preregistration_draft.md` §4 ("Headline figures at the freeze", Line 80).
- **Bug:** Line 66 accurately records the Round-14 `A28` exclusions (*"Family A 16 to 13, B 5 to 3, C 16 to 15; 31 studies in the three families; included reports 1,078 to 1,072"*), **but Line 80 in the Headline Freeze Table was never updated after Round 13 (`A29`)** and still states:
  > `| Effect-size rows | **58**: Family A 16, Family B 5, Family C 16 and 21 reasoned non-fits; **none pooled** |`
  instead of **`52`: Family A 13, Family B 3, Family C 15 and 21 reasoned non-fits**. Also, Line 4 still points to `(branch claude/legal-last-mile-review-spec-8ri0zs)` rather than `main`.
- **Ready-to-apply fix:** `outputs_and_osf_audit/fix_osf_preregistration_line80_effect_counts.patch` (`git apply --check` verified).

### `OA-02` (HIGH): Binary Word Report `06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.docx` Is Frozen at the Pre-`A16` `1,159`-Study State!
- **Location:** `06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.docx` (`word/document.xml`, `25,851` bytes).
- **Bug:** While `PRELIMINARY_RESULTS_REPORT_2026-09-29.md` and `.html` were updated to `1,072` included / `1,205` excluded, the `.docx` file in the same folder was **never regenerated** and still tells readers:
  - *"2,276 of 3,659 assessed (62.2%) : 1,159 include / 1,117 exclude ; 1,383 never assessed"*
  - *"human confirmed 100 includes and no excludes"*
  - *"Extraction 1,159 studies, 92 codebook fields, by the AI; 37 from abstract/metadata only"*
  - *"This was not human-adjudicated"* (referring to A16, which CK subsequently adjudicated!)
  - Lists retired reviews (`S324`, `S327`, `S328`) as active AMSTAR 2 studies.
- **Contrast:** `06_outputs/EXECUTIVE_SUMMARY_2026-10-14.docx` **is** cleanly synced to `1,072` studies (`85%` [`909/1072 = 84.8%`] since 2010; `812` [`75.7%`] qualitative/mixed/doctrinal; `58` [`5.4%`] causal-tool studies; `944` water access; `415` sanitation access; `29` certainty `3–4`; `52` effect rows = `31` in families + `21` non-fits; `17` Critically Low + `1` Low on AMSTAR 2 — **every single headline integer in `EXECUTIVE_SUMMARY_2026-10-14.docx` verified `100%` exact against the CSVs!**).

### `OA-03` (HIGH): `06_outputs/supplementary/preliminary_results.md` (`465 KB`) Still Quotes `1,080` Included Reports, `467` Human-Verified, `59`/`58` Effect Rows, and Cites `46` Retired Study IDs
- **Location:** `06_outputs/supplementary/preliminary_results.md`.
- **Bug:** Contains pre-Round-14 numbers (`1,080` included reports, `467` human-verified before `A31` relabelled the 18 AI-checked SWiM studies to `459`, `59`/`58` effect rows) and references `46` retired `study_id`s (`S1020, S1042, S1053, S1056, S1057, ...`) as active corpus members.

### `OA-04` (MODERATE): Unflagged Retired Studies Still Appearing in `phase11_quantitative_feasibility_judgment.md`, `phase11_blank_family_resolution_2026-09-28.md`, and `2026-09-28_evidence_limitations.md`
- `phase11_blank_family_resolution_2026-09-28.md` still quotes `37 studies` in SWiM families (pre-`A28`) and lists retired `S312, S435, S1121, S1143`.
- `2026-09-28_evidence_limitations.md` still contains `1,159` and `1,080` alongside `10` retired `study_id`s.

### `OA-05` (LOW / VERIFIED CLEAN): `06_outputs/EVIDENCE_ATLAS_INTERACTIVE.html` & `06_outputs/figures/fig1–fig5.svg` Pass Exact Structural Sync!
- **Interactive HTML Atlas (`1.46 MB`):** Embedded `STUDIES` array contains **`1072` records**, matching `extraction_database.csv`'s `1,072` `study_id`s with **`0` retired-study leaks and `0` missing active studies**. (Note: `368` rows in `evidence_map.csv`'s `evidence_level` text still contain the substring `"deferred"` — e.g. `"rating deferred"` historical text — which carries into `0` Atlas detail cards.)
- **SVG Figures (`fig1`–`fig5.svg`):** Verified clean (`fig4_direction_by_family.svg` displays `k = 13` [`7, 4, 2`], `k = 3` [`3`], `k = 15` [`4, 8, 3`] = `31` SWiM studies, matching `SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv` exactly).

---

## 2. File-by-File Consistency Matrix (`OUTPUTS_AND_SUPPLEMENTARY_CONSISTENCY_MATRIX_2026-11-20.csv`)

| File | Distinct `S###` Cited | Total Retired `S###` Present | Retired `S###` Cited Without Local Retirement Cue | Stale Count / Claim Cues |
|---|---:|---:|---|---|
| `00_admin/preregistration/osf_preregistration_draft.md` | 28 | 8 | `none` | `1,080; 37 studies` |
| `00_admin/RELEASE_0.2.0-interim_2026-10-14.md` | 18 | 2 | `none` | `clean` |
| `README.md` | 78 | 33 | `S079; S197; S199; S227; S233; S299; S348; S399; S435; S1121; S1143; S1163` | `1,159; 1,080` |
| `06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md` | 73 | 13 | `S201; S947; S1144; S1163` | `clean` |
| `06_outputs/supplementary/effect_sizes_remining_2026-09-28.md` | 11 | 3 | `S348; S696` | `clean` |
| `06_outputs/supplementary/family_A_swim_synthesis_2026-09-28.md` | 24 | 5 | `S1020; S1042; S1057` | `clean` |
| `06_outputs/supplementary/family_B_swim_synthesis_2026-09-28.md` | 8 | 2 | `S1144; S1163` | `clean` |
| `06_outputs/supplementary/family_C_swim_synthesis_2026-09-28.md` | 21 | 3 | `none` | `clean` |
| `06_outputs/supplementary/phase11_blank_family_resolution_2026-09-28.md` | 29 | 4 | `S312; S435` | `37 studies` |
| `06_outputs/supplementary/phase11_pooling_feasibility_S526_S539_S749.md` | 3 | 0 | `none` | `clean` |
| `06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md` | 65 | 12 | `S312; S348; S435; S969; S1020; S1042; S1057; S1121; S1143; S1144; S1163` | `clean` |
| `06_outputs/supplementary/preliminary_corpus_characterization.md` | 18 | 2 | `S227; S399` | `clean` |
| `06_outputs/supplementary/preliminary_narrative_synthesis.md` | 31 | 0 | `none` | `clean` |
| `06_outputs/supplementary/preliminary_results.md` | 752 | 46 | `S227; S356; S399; S430; S435; S479; S513; S653; S673; S677; S693; S696; S697; S700; S707; ` | `1,080; 467; 59 effect; 58 effect` |
| `06_outputs/supplementary/SWIM_SYNTHESIS_TEMPLATE.md` | 0 | 0 | `none` | `clean` |
| `06_outputs/supplementary/title_only_triage_memo.md` | 0 | 0 | `none` | `clean` |
| `04_quality/risk_of_bias/2026-09-16_evidence_limitations.md` | 48 | 4 | `S079; S329; S356` | `clean` |
| `04_quality/risk_of_bias/2026-09-28_evidence_limitations.md` | 43 | 10 | `S260; S324; S326; S347; S356` | `1,159; 1,080` |
| `04_quality/risk_of_bias/EVIDENCE_LIMITATIONS_TEMPLATE.md` | 0 | 0 | `none` | `clean` |
