# Report: Separate-Scope Audit of the Global Water Law Judicial Decisions Dataset (`v0.3.0`), Full `207`-Case Blind Jurimetric Validation, & Open Claude PRs `#2, #6, #8, #9` (`Item 1B.4`)

*AI-generated second-model output. Not human verification.*

---

## 1. Closing the `116`-Case Validation Ceiling (`validation/RESIDUAL_AUDIT.md` §5.1): Full `207 / 207` Blind Second-Model Jurimetric Audit

In `validation/RESIDUAL_AUDIT.md` (§5.1, L292–297), `116` of the `207` stratified `not_water_related` (NWR) validation decisions had **zero second-coder or LLM verification**, and the `91` checked cases were coded only by Claude. We ran `207` blind `blind_jurimetric_coder` passes + `15` self-consistency reruns (`0` non-`finish` tool calls; `0/15` flips; `344/344 = 100.00%` Dutch/Portuguese quotes verified), stripped of `coder1_label`, `coder2_label`, `governance_cat`, and `stratum`:

| Inter-Coder Specification | `N` | Cohen's $\kappa$ | Bootstrap `95% CI` | Observed Agreement |
|---|---:|---:|---|---|
| Full N=207: Author (Coder1) vs Gemini (Coder3) — Mananciais Rule Applied | `207` | **`0.836`** | `[0.762, 0.900]` | `90.8%` |
| Full N=207: Binary WATER/NOT_WATER (Exclude UNCERTAIN) | `190` | **`0.873`** | `[0.808, 0.937]` | `93.7%` |
| Full N=207: Coder1-Confident Subset | `170` | **`0.856`** | `[0.777, 0.928]` | `92.9%` |
| Full N=207: Strict Pre-Rule 3-Label Baseline | `207` | **`0.820`** | `[0.748, 0.883]` | `88.9%` |
| Matched N=91: Author (Coder1) vs Gemini (Coder3) — Mananciais Rule | `91` | **`0.867`** | `[0.763, 0.958]` | `92.3%` |
| Matched N=91: Claude (Coder2) vs Gemini (Coder3) — Cross-AI Agreement | `91` | **`0.924`** | `[0.838, 0.982]` | `95.6%` |
| Matched N=91: Author (Coder1) vs Claude (Coder2) — Published Baseline | `91` | **`0.832`** | `[0.728, 0.925]` | `90.1%` |

- **Independent Cross-Family Population-Weighted NWR Filter Precision (`N = 207`, Gemini `Coder3` Ground Truth):** **`99.77%`** (compared with `99.79%` under Author `Coder1` ground truth — independently replicating the `>99.5%` precision of the `v0.3.0` filter across all `207` cases!).
- **Thesis Falsification Test Across All `207` NWR Decisions (`connection_refusal` / `informal_settlement`):** **`0` household water/sanitation connection-refusal or informal-settlement cases found** (`NL_plain=100.0%`, `NL_aansluiting=100.0%`, `NL_broad_water=38.0%`, `BR_all=5.7%` NWR precision).

---

## 2. Repo-Root Judicial Decisions Dataset (`v0.3.0`) & Open Claude PRs (`#2, #6, #8, #9`) Audit Findings

| ID | Severity / Status | Target | Finding & Recommended Action |
|---|---|---|---|
| `RD-01` | `CRITICAL` | `arxiv/main.tex (L35, L154, L181, Table 1 L206-220) & arxiv/water_law_preprint.pdf` | arXiv preprint is completely frozen at pre-v0.3.0 (v0.2.x): reports 12 categories instead of 21, 9,108 unclear instead of 7,205, Brazil Tariff=5,634 (vs 5,689), Other water=4,252 (vs 3,769), Connection=1,160 (vs 1,275), Informal=96 (vs 88), and omits the 67,703 not_water_related filter and validation/ infrastructure. |
| `RD-02` | `HIGH` | `CITATION.cff (L18)` | Lists `- name: "Antigravity"` as a software/dataset author alongside Claudio Klaus; COPE, ICMJE, JELS, and Law & Society Review authorship rules prohibit AI tools as listed authors (move to acknowledgements/AI-disclosure as done in legal-last-mile-systematic-review/CITATION.cff). |
| `RD-03` | `HIGH` | `validation/second_coder_protocol.md (L60 vs L74)` | Three-letter category code `INF` is assigned twice to two distinct categories: `informal_settlement` (L60, core thesis category!) and `water_infrastructure_contract` (L74, procurement/PPP). Rename contract code to `WIC` or `CON_INFRA` before human RA coding. |
| `RD-04` | `HIGH` | `validation/README.md (L8, L18, L108-109) & SUPERVISOR_REPORT_v0.3.0.md (§3.2-4.3)` | Three conflicting residual baselines appear in validation/README.md (`57,695 [69%]` -> `1,207` vs `89.2% -> 8.3%` / `67,703`), and SUPERVISOR_REPORT_v0.3.0.md conflates v0.3.0 `67,703 + 6,904 = 74,607` with v0.2.x `57,695`. Resolved cleanly by our `git apply --check`-verified `pr9_conflict_resolved_against_main.patch`. |
| `RD-05` | `LOW` | `validation/second_coder_sample_raw.csv` | Saved with UTF-8 BOM (`\ufeffsample_id`), causing `csv.DictReader(..., encoding='utf-8')` `KeyError: 'sample_id'` unless opened with `utf-8-sig`. |
| `PR-02` | `MERGE_READY_WITH_NOTE` | `PR #2 (claude/dataset-gaps-coverage-VWc7b)` | MERGEABLE (+835/-6): Adds REURB terminology, `post_marco_legal` (Law 14.026/2020) analysis, and `utils/nl_outcome_coding.py`. Note: `data/` is `.gitkeep` in git, so re-run `jurimetric_coding.py` against local `water_law_global_coded.csv` and refresh Zenodo/Dataverse v0.3.1 deposits if merging. |
| `PR-06` | `MERGE_READY_WITH_NOTE` | `PR #6 (claude/relaxed-babbage-s0z3cz — dissertation_agent/)` | MERGEABLE (+4,645/-0): Adds 2023 thesis MCP agent & `llms.txt`. Modifies root `CITATION.cff` and `docs/index.html` — merge BEFORE or rebase AFTER `PR #9` since both touch `docs/index.html` (different lines, currently clean). |
| `PR-08` | `NEEDS_MINOR_UPDATE` | `PR #8 (claude/wiki-update)` | MERGEABLE (+1,137/-191): `wiki/Systematic-Review.md` quotes `26,222` deduplicated TA records in `AI-Disclosure.md` vs `27,481` in `CURRENT_FIGURES.md`, and `13` borderline includes vs `14` rows carrying `BORDERLINE` in `full_text_screening_database.csv`; also update second-AI counts once Gemini PRs `#10-#42` merge. |
| `PR-09` | `CONFLICT_RESOLVED_HERE` | `PR #9 (claude/fix-validation-docs)` | Currently CONFLICTING on GitHub due to `validation/README.md` L59-63 (`main` already has richer `coder1_kappa.csv` warning). Our `pr9_conflict_resolved_against_main.patch` preserves `main`'s L59-63 warning, fixes L8/L18/L108-109, includes all 7 other PR #9 files, and passes `git apply --check` cleanly. |

---

## 3. Ready-to-Apply Conflict Resolution for `PR #9` (`pr9_conflict_resolved_against_main.patch`)

Verified against `origin/main` (`2cd44e7`) via `git apply --check` (`exit 0`). Apply from repo root with:
```bash
git apply legal-last-mile-systematic-review/gemini_review/root_dataset_and_open_prs_audit/pr9_conflict_resolved_against_main.patch
```
