# Task G Report: Adversarial Critique of `WEAKNESSES.md` and `WEAKNESS_REGISTER.csv`

*AI-generated second-model output. Not human verification.*

- **Date:** 2026-11-18
- **Model:** `gemini-4-carbon-medium` (`Gemini-gemini-4-carbon-medium-weaknesses-adversarial-review-2026-11-18`)
- **Mandate (Brief §3 Task G):** *"Read `00_admin/WEAKNESSES.md` and `WEAKNESS_REGISTER.csv`. List weaknesses that are missing, mis-rated or easy to resolve. This is deliberately a request for criticism, not agreement."*
- **Method:** Every claim in `WEAKNESSES.md` (`W01`–`W34`) was cross-tested directly against `extraction_database.csv`, `exclusion_log.csv`, `search_log.csv`, `SEARCH_PROTOCOL.md`, `SENSITIVITY_ANALYSIS_2026-09-28.md`, `code/analysis/sensitivity_analysis.py`, `VERIFIER_MUTATION_MAP_2026-10-04.md`, and our empirical blind/adversarial findings from **Task A** (`PR #10`) and **Task E** (`PR #11`).

---

## Executive Summary

`WEAKNESSES.md` is unusually candid by published systematic-review standards, **but because it was drafted by the same AI that built the review, it shares that AI's blind spots**: it audits consistency and high-level workflow gaps well while missing **within-study statistical multiplicity, prose-over-table extraction shortcuts, silent omissions from `search_log.csv`, unlogged non-EPD translations, sensitivity-script no-ops/rendering bugs, and overstated claims about its own mutation map**.

Specifically, our adversarial audit identifies:
1. **11 Missing Weaknesses (`NEW_W35`–`NEW_W45`)** — including **4 `high`-severity** threats absent from `WEAKNESS_REGISTER.csv`.
2. **10 Mis-Rated or Factually Inaccurate Entries** among `W01`–`W34` — backed by direct database queries (including executing `W10`'s own proposed pre/post-2026-10-03 test on `exclusion_log.csv`).
3. **12 High-Leverage Quick Wins** that the PI or Claude can resolve in **under one day** before manuscript submission.

---

## 1. Eleven Missing Weaknesses (`NEW_W35` to `NEW_W45`)

### `NEW_W35` — Planned PubMed, Global Health (Ovid), Google Scholar, and multilingual (§3 PT/NL/ON) database searches are silently omitted from search_log.csv NOT RUN rows, SEARCH_PROTOCOL.md §7, START_HERE.md, and W01.
- **Stage / Target:** (new — Search) · **Recommended severity:** `high` · **Easy to resolve?** partly (disclosure easy; running searches medium)
- **Empirical proof in repo:** SEARCH_PROTOCOL.md §1 (lines 16, 18, 37, 41) & pubmed.md / pubmed_adapter.py exist, yet search_log.csv has NOT RUN rows only for SSRN (SEARCH_042) and Westlaw/Lexis (SEARCH_043). 0 Dutch studies exist in extraction_database.csv because §3.2 Dutch terms were never run in any bibliographic database.
- **Concrete fix:** Add explicit NOT RUN disclosure rows to search_log.csv for PubMed, Global Health, Google Scholar, and §3 multilingual queries; expand W01 and SEARCH_PROTOCOL.md §7.

### `NEW_W36` — 36 of 37 included non-English/Portuguese/Dutch studies (29/30 Spanish, 6/6 French, 1/1 Slovak/Czech) violate INCLUSION_EXCLUSION.md Criterion 10 by omitting translation method and translator from extraction_note.
- **Stage / Target:** (new — Eligibility / Extraction) · **Recommended severity:** `high` · **Easy to resolve?** yes (audit & backfill extraction_note)
- **Empirical proof in repo:** Direct scan of extraction_database.csv (`language` vs `extraction_note`): 30 Spanish-only, 6 French-only, and 1 Slovak/Czech study are included; only 1 Spanish row mentions translation in `extraction_note`.
- **Concrete fix:** Audit all 37 non-EPD rows, backfill AI translation provenance in `extraction_note`, and add a verifier check enforcing Criterion 10 on non-EPD languages.

### `NEW_W37` — Severe within-study specification and outcome multiplicity across 24 of 31 SWiM synthesis studies (77.4%), including cherry-picking partial models or secondary factors over null/opposite primary results.
- **Stage / Target:** (new — Synthesis) · **Recommended severity:** `high` · **Easy to resolve?** yes (via A30 adjudication)
- **Empirical proof in repo:** Task E adversarial audit (PR #11): S471 is null (b=-1.03, SE=0.76) in the authors' designated primary Combined model (coded Favourable from partial Col. 3); S085 is null on 7 of 8 primary pre-registered tests incl. Full Sample N=6,652; S930 is null on 8/8 water and 5/8 sewerage models; S174 omits statutory sanitation-plan factor Capacidade_Politica (-1.890, p=0.033) in favour of endogenous billing revenue.
- **Concrete fix:** Pre-specify a deterministic primary-specification selection hierarchy (authors' designated full/combined model > partial block; direct legal rule > financial proxy) and recode S471, S593, and contested rows during A30.

### `NEW_W38` — Construct-validity dilution in SWiM: 16 of 31 synthesis studies measure indirect utility/ecological/institutional proxies rather than household water/sanitation connection or affordability.
- **Stage / Target:** (new — Synthesis) · **Recommended severity:** `high` · **Easy to resolve?** yes (reclassify to non-fits or stratify)
- **Empirical proof in repo:** Task E audit: S593 models Coulter's municipal inequity formula (penalizing 99%-covered low-tariff cities); S526 models 30k/6k gal tariff steepness; S749 models corporate revenue/m3 across industrial/agricultural/domestic users; S879 codes Mixed from landlord loan repayment while all 8 household WASH access outcomes (Table 7) are null.
- **Concrete fix:** Move S593 (out-of-scope construct) to reasoned non-fits or exclude; separate household-level access outcomes from utility-tariff/revenue proxies in SWiM tables.

### `NEW_W39` — Four of nine SWiM sensitivity scenarios (S1, S1b, S2, S3) drop 0 studies (no-ops identical to baseline), S3 fails to test probable overlap LR09 (S526/S539), and sensitivity_analysis.py omits Null counts from Family B/C rendered cells.
- **Stage / Target:** (new — Sensitivity / Code) · **Recommended severity:** `medium` · **Easy to resolve?** yes (<15 lines of Python)
- **Empirical proof in repo:** SENSITIVITY_ANALYSIS_2026-09-28.md lines 19-35 & code/analysis/sensitivity_analysis.py line 195: in S4c, S4e, and S5, recoded Null studies vanish from the printed `C raw +/-/mixed` and `C Fav/Unfav/mixed` ratios so displayed sub-counts sum to 14 or 13 while `C k = 15`.
- **Concrete fix:** Fix line 195 of sensitivity_analysis.py to print `+/-/null/mixed` and `Fav/Unfav/Null/Mixed` for all three families; add scenario S3b collapsing probable overlap LR09 (S526/S539) and a scenario dropping Task E `unsupported` rows.

### `NEW_W40` — Systematic prose-skimming over regression tables and PDF Unicode minus-sign stripping in numerical extractions.
- **Stage / Target:** (new — Extraction) · **Recommended severity:** `medium` · **Easy to resolve?** partly (easy for 31 SWiM rows)
- **Empirical proof in repo:** Task E found partial/rounding/table issues in 10 of 31 SWiM studies (32.3%): S398 recorded `table: none`, `SE: none`, `N=962` from prose despite Table 3 Col. 5 printing `23.479* (SE=12.189, p<0.10, N=216 across 72 tracts)`; S930 mistook adjacent `%Δ` t-stat `0.595` for a p-value; Elsevier/IWA PDFs strip `−` glyphs in Tables (`S920`, `S930`, `S1062`, `S1162`).
- **Concrete fix:** Correct the 10 SWiM table/SE/N records identified in Task E and disclose prose-vs-table extraction error rates once Task C (60-study second extraction) is scored.

### `NEW_W41` — AI-framed adjudication sheets risk anchoring human (`CK`) rulings across the 262 adjudicated records.
- **Stage / Target:** (new — Screening / Governance) · **Recommended severity:** `medium` · **Easy to resolve?** partly (mitigated prospectively in A6)
- **Empirical proof in repo:** In A16, A22, A24, A25, A26, and A28, the primary AI selected paper excerpts, framed binary options, and printed its recommended verdict adjacent to the human fill-in column; A6_TIER3_EVIDENCE_CARDS_2026-11-15.md likewise includes AI extraction and AI reasoning on the card.
- **Concrete fix:** Disclose AI-framed dossier anchoring alongside the 20.2% human-verified figure, and keep `saw_AI_reasoning_before_deciding` audit tracking strict for remaining A6/A30 passes.

### `NEW_W42` — 18 secondary reviews (AMSTAR 2, including scoping/integrative hybrids) are counted inside the 1,072 included studies without checking primary-study overlap against the 1,054 primary studies; S879 still carries an unverified RoB 2 placeholder string.
- **Stage / Target:** (new — Synthesis / Overlap) · **Recommended severity:** `medium` · **Easy to resolve?** yes
- **Empirical proof in repo:** CURRENT_FIGURES.md counts 18 AMSTAR 2 reviews in the 1,072 corpus; extraction_database.csv S879 `risk_of_bias_tool` still reads `randomization unit (compound-level) inferred ... verify against source paper before finalizing rating` despite full PDF showing Exp. 1 compound-randomized (N=2,584) and Exp. 2 street-cluster-randomized (142 streets, N=1,001); S294 RoB 2 has mechanism_certainty=3 vs 4 on the other 4 RoB 2 rows.
- **Concrete fix:** Separate primary studies (1,054) from secondary reviews (18) in headline tables, audit citation overlap for the 18 reviews, and finalize S879's RoB 2 string.

### `NEW_W43` — Web of Science (`SEARCH_035`, 4,058 records) has unconfirmed Core Collection index/edition selection and unconfirmed pre-export hit total.
- **Stage / Target:** (new — Search) · **Recommended severity:** `medium` · **Easy to resolve?** yes (check EUR WoS subscription)
- **Empirical proof in repo:** search_log.csv row 37 (`SEARCH_035`) states `UNCONFIRMED -- which Core Collection indexes (SCI-EXPANDED/SSCI/A&HCI/ESCI) were selected has not been reported back` and pre-export hit total `UNCONFIRMED`.
- **Concrete fix:** Log into EUR Web of Science once, check default subscribed editions and total hit count (or log permanently in W01/W03 if historical count shifted).

### `NEW_W44` — Cross-platform verification crash on 64-bit Windows (`csv.field_size_limit(sys.maxsize)`), `.gitignore` blocking `gemini_review/**/*.json`, and failing EOL Python 3.8/3.9 GitHub Actions jobs.
- **Stage / Target:** (new — Reproducibility / CI) · **Recommended severity:** `low` · **Easy to resolve?** yes (<15 minutes)
- **Empirical proof in repo:** Running `verify_repository.py` on Windows 64-bit Python 3.12 raises `OverflowError: Python int too large to convert to C long` at current_figures.py:18 and validate_schemas.py:41; root `.gitignore` line 32 `*.json` ignores `gemini_review/`; CI fails on Python 3.8/3.9.
- **Concrete fix:** Replace `sys.maxsize` with `min(sys.maxsize, 2**31 - 1)`, add `!legal-last-mile-systematic-review/gemini_review/**/*.json` to `.gitignore`, and drop EOL Python 3.8/3.9 from `.github/workflows/`.

### `NEW_W45` — Class base-rate leakage in second-AI task headers when Tier 3 (100% AI includes) and Tier 2 (100% AI excludes) are run as separate named batches.
- **Stage / Target:** (new — AI Validation) · **Recommended severity:** `medium` · **Easy to resolve?** yes (mix tiers in Task B)
- **Empirical proof in repo:** GEMINI_HANDOFF_BRIEF_2026-11-17.md §3 titles Task A `50 tier-3 includes` and Task B `102 tier-2 excludes`. Although we stripped this from `blind_screener_v2`'s prompt in Task A, running pure-include or pure-exclude batches leaks base rates to any agent reading the brief.
- **Concrete fix:** When generating the Tier-2 blind input file, mix in seeded control includes (or combine with human-verified calibration records per A6_COMPARISON_PREREGISTRATION) without disclosing base rates.

---

## 2. Ten Mis-Rated or Factually Inaccurate Existing Weaknesses

### `W04` (`CRIT_W04`) — `medium` → **`medium (rewrite description)`**
- **Issue:** W04 claims non-EPD languages (e.g. Spanish, French) were excluded, whereas 37 Spanish/French/Slovak studies ARE included without translation logs and 0 Dutch studies were found.
- **Empirical proof in repo:** extraction_database.csv holds 30 Spanish, 6 French, 1 Slovak/Czech, plus 8 bilingual Spanish/French rows, and 0 Dutch rows. Meanwhile English-only search strings excluded non-English-indexed papers at search time.
- **Concrete fix:** Rewrite W04 to distinguish (a) English-only database search bias (excluding papers without English titles/abstracts, including Dutch) from (b) inconsistent ad-hoc inclusion of 37 Spanish/French/Slovak hits without Criterion 10 translation logs.

### `W09` (`CRIT_W09`) — `high` → **`high (update empirical bound)`**
- **Issue:** W09 cites a 3/40 (7.5%) informal false-inclusion estimate, whereas blind second-AI screening of Tier 3 (Task A, PR #10) excluded 26 of 46 readable includes (56.5%).
- **Empirical proof in repo:** Task A blind Gemini run (`gemini-4-carbon-medium`, 0/10 self-consistency flips): 26/46 readable Tier-3 AI includes excluded (13 E03 narrow Criterion 2, 5 E04 wrong outcome, 4 E05 non-empirical essays, 3 E01, 1 E07).
- **Concrete fix:** Update W09 once CK completes the A6 Tier-3 human pass; expect substantial false-inclusion concentration among unverified broad-governance and commentary includes.

### `W10` (`CRIT_W10`) — `medium` → **`high`**
- **Issue:** W10 rates mid-stream adoption of narrow Criterion 2 as `medium` with `unknown` bias, but running W10's own date test proves a 20-fold regime shift in exclusion coding.
- **Empirical proof in repo:** In exclusion_log.csv: pre-2026-10-03 (`n=1,113`) has E01=44.0% (490) and E03=3.1% (35); post-2026-10-03 (`n=92`) has E01=0.0% (0) and E03=63.0% (58). Meanwhile 785 AI-only includes were only screened on extracted flags (`A24`), not full-text re-read (which is why Task A still found 56.5% excludes).
- **Concrete fix:** Upgrade W10 from `medium` to `high` and report the pre/post-2026-10-03 exclusion distribution directly in W10.

### `W14` (`CRIT_W14`) — `medium` → **`high (for Family C synthesis)`**
- **Issue:** Sample overlap between S526 (1,183 large US utilities, AWWA/SDWIS) and S539 (500 largest US utilities, AWWA) directly inflates Family C's US ownership pattern and is NOT tested by sensitivity scenario S3.
- **Empirical proof in repo:** sensitivity_analysis.py line 94 filters `same_underlying_data == 'yes'`, skipping LR09 (`S526`/`S539`, coded `probable`). Both studies analyse the 2017–2019 AWWA US utility survey on investor-owned vs public pricing.
- **Concrete fix:** Verify AWWA survey year overlap from the two PDFs already in Drive (`S526`, `S539`), upgrade LR09 to `partial`/`yes`, and add scenario S3b.

### `W17` (`CRIT_W17`) — `low` → **`medium`**
- **Issue:** Labelling 51 of 127 (40.2%) JBI Cross-Sectional studies `High concern` due to sparse AI extraction rather than study conduct distorts quality distributions across a major quantitative stratum.
- **Empirical proof in repo:** CURRENT_FIGURES.md line 50: 51/127 JBI ratings are sparse-extraction artefacts; Task E also found S631 (a 10-year 2001–2010 panel Difference-GMM study) misassigned to JBI Cross-Sectional.
- **Concrete fix:** Relabel extraction-limited domains as `Not assessable from extraction` rather than `High concern`, and audit panel studies misassigned to JBI Cross-Sectional.

### `W22` (`CRIT_W22`) — `medium` → **`high`**
- **Issue:** W22 downplays that Family C's pre-stated raw-sign conclusion test (`C_test_no_dominant_sign`) actively FAILS at baseline (`8/15 = 53.3%` negative raw signs) and in 7 of 9 sensitivity scenarios.
- **Empirical proof in repo:** SENSITIVITY_ANALYSIS_2026-09-28.md line 10 & 25: `S0 baseline — C_test_no_dominant_sign: FAILS` (4 positive / 8 negative / 3 mixed).
- **Concrete fix:** Upgrade W22 or ensure every Family C narrative explicitly states that raw signs show a narrow negative majority (8/15) while substantive directions do not (5/7/3).

### `W23` (`CRIT_W23`) — `medium` → **`high`**
- **Issue:** Single human investigator executing eligibility refinements and synthesis exclusions (`D09`, `D15`–`D17`) with results visible for a companion dissertation review is a `high` ROBIS governance risk, not `medium`.
- **Empirical proof in repo:** DEVIATIONS_AND_ERRORS.md lines 19–27: 4 departures (`D12`, `D15`, `D16`, `D17`) and 2 partial departures (`D09`, `D10`) were made by a single investigator after results existed.
- **Concrete fix:** Rate W23 `high` to match ROBIS / Cochrane standards and publish a pre-ruling (`k=44`) vs post-ruling (`k=31`) SWiM comparison table (`W21` quick win).

### `W30` (`CRIT_W30`) — `medium` → **`high (fix mutation map claim)`**
- **Issue:** W30 claims `VERIFIER_MUTATION_MAP_2026-10-04.md` records what the verifier `does and does not catch`, when in fact the file shows `27 of 27 defects caught` (0 UNCAUGHT) and quotes stale `1,159` counts.
- **Empirical proof in repo:** 00_admin/VERIFIER_MUTATION_MAP_2026-10-04.md line 30 (`1,159 studies extracted`) and line 35 (`27 of 27 defects caught`). Real uncaught error classes (double sign+polarity inversion `S142`, t-stat for p-value `S930`, unlogged Spanish/French translations) are absent from `check_verifier_mutations.py`.
- **Concrete fix:** Add `check_verifier_mutations.py --write` to `regenerate_all.sh` and add negative-control mutations (`UNCAUGHT` rows: swapped exposure/outcome text, flipped direction code, unlogged translation) so the mutation map genuinely documents verifier blind spots.

### `W31` (`CRIT_W31`) — `low` → **`medium`**
- **Issue:** Lack of SHA-256 file manifests for 1,041 of 1,072 included studies (plus `.pdf`-named HTML files on Drive such as `RA13F19846E9D`) is a `medium` auditability barrier, not `low`.
- **Empirical proof in repo:** Task A found `RA13F19846E9D` stored on Drive as `.pdf` when its bytes are SciELO HTML; `A14` previously found ~20 Drive `.pdf` files were portal landing pages.
- **Concrete fix:** Run a non-copyright-infringing metadata manifest script over the Drive folder recording `(record_id, study_id, mime_detected, bytes, sha256, pages, text_chars)` for all held files.

### `W33` (`CRIT_W33`) — `low` → **`medium`**
- **Issue:** Missing SWiM (2020) 9-item checklist and PRISMA-S search checklist—while PRISMA 2020 was filled by the same AI—is a `medium` peer-review vulnerability and an easy quick win.
- **Empirical proof in repo:** 06_outputs/prisma/ has only AI-completed `PRISMA_2020_CHECKLIST.md`; SWiM is the primary synthesis method (`PROTOCOL.md` §9) yet has no checklist.
- **Concrete fix:** Complete official SWiM (Campbell et al. 2020) and PRISMA-S (Rethlefsen et al. 2021) checklists with human sign-off before manuscript submission.

---

## 3. Twelve High-Leverage "Quick Wins" Easy to Resolve Before Submission

Ranked by Effort-to-Impact ratio (all doable in hours, not weeks):

1. **Fix `sensitivity_analysis.py` line 195 + add `LR09` (`S526`/`S539`) collapse (`NEW_W39`, `CRIT_W14` — *15 mins, Claude*):** Display `Null` counts in Family B/C markdown cells (fixing the `14 != 15` row-sum bug in `S4c`/`S4e`/`S5`), label `S1/S1b/S2/S3` honestly as `0-drop` checks on the post-cleanup set, and add scenario `S3b` collapsing `probable` overlap `LR09` (`S526`/`S539`).
2. **Add missing `NOT RUN` disclosure rows to `search_log.csv` & `W01` (`NEW_W35` — *15 mins, Claude*):** Log `PubMed`, `Global Health (Ovid)`, `Google Scholar`, and the §3 Portuguese/Dutch/Ontario database queries as `NOT RUN` so `search_log.csv` matches `SEARCH_PROTOCOL.md` §1 & §5.
3. **Fix `VERIFIER_MUTATION_MAP_2026-10-04.md` & add true `UNCAUGHT` negative-control mutations (`CRIT_W30` — *30 mins, Claude*):** Wire `check_verifier_mutations.py --write` into `regenerate_all.sh` (eliminating the stale `1,159` figure) and add 4–5 genuine `UNCAUGHT` mutations (e.g., cancelled double sign/polarity flip, prose-vs-table number drift, unlogged Spanish translation) so `W30`'s claim is true.
4. **Backfill Criterion 10 translation provenance on the 36 non-EPD included rows & rewrite `W04` (`NEW_W36`, `CRIT_W04` — *30 mins, Claude*):** Append explicit AI-translation provenance notes to the 29 Spanish, 6 French, and 1 Slovak/Czech rows lacking them, and correct `W04`'s false statement that Spanish/French studies were excluded.
5. **Adjudicate the 2 `unsupported` Family C rows (`S471`, `S593`) and fix the 10 SWiM table/sign/SE errors (`W20`, `NEW_W37`, `NEW_W40` — *1–2 hours, PI + Claude using PR #11*):** Using Task E's table-and-page audit, fix `S142`'s double sign/polarity inversion, `S930`'s `0.595` t-stat/p-value misread, `S398`'s exact `23.479* (SE = 12.189, N = 216)` Table 3 values, `S471`'s null primary Combined model, and `S593`'s inverted Coulter inequity index.
6. **Build the Pre-Ruling (`k = 44`) vs. Post-Ruling (`k = 31`) SWiM Comparison Table (`W21` — *30 mins, Claude*):** `11_archive/effect_sizes_removed_2026-10-13.csv` and `SWIM_37_SOURCE_VERIFICATION_DOSSIER_2026-10-14.md` already hold every retired row—rendering a side-by-side table directly neutralizes the post-hoc scope-ruling critique (`D15`–`D17`).
7. **Publish `W10`'s Pre/Post-2026-10-03 Exclusion Shift Table (`CRIT_W10` — *20 mins, Claude*):** Put the exact `exclusion_log.csv` numbers (`E03`: `3.1% -> 63.0%`; `E01`: `44.0% -> 0.0%`) straight into `EXCLUSION_BASIS_AUDIT` and `W10` rather than leaving `W10` as an unexecuted hypothetical test.
8. **Finalize `S879`'s unverified RoB 2 note & separate the 18 AMSTAR 2 reviews from the 1,054 primary studies (`NEW_W42` — *30 mins, Claude*):** Replace `S879`'s `"verify against source paper"` placeholder with its verified design (Exp. 1 compound-randomized `N=2,584`; Exp. 2 street-cluster-randomized `142` streets `N=1,001`), harmonize `S294`'s `mechanism_certainty`, and check citation overlap for the 18 secondary reviews.
9. **Submit the already-written retrospective OSF registration + Zenodo `v0.2.0-interim` snapshot (`W24` / Item `A7` — *30 mins, PI*):** Immediately closes `W24` with an immutable external timestamp prior to final manuscript submission.
10. **Eliminate remaining hardcoded stale counts in `README.md` items 6 & 16 (`W32` — *15 mins, Claude*):** Add `<!-- BEGIN GENERATED -->` markers or verifier assertions for `README.md` limitation items 6 & 16 and `EXECUTION_CHECKLIST.md`.
11. **Complete the 9-item SWiM (2020) and 16-item PRISMA-S Checklists (`CRIT_W33` — *2 hours, PI + Claude*):** Closes `W33` and prevents desk-review checklist objections.
12. **Fix cross-platform Windows `csv.field_size_limit`, `.gitignore` `gemini_review/**/*.json`, and EOL Python 3.8/3.9 CI (`NEW_W44` — *15 mins, Claude*):** Makes `verify_repository.py` pass out-of-the-box on Windows, tracks second-AI JSONs cleanly, and turns GitHub Actions green on every PR.
