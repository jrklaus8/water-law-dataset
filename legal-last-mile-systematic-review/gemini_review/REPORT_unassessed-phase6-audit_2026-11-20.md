# Report: Workstream T — Empirical Non-Retrieval Bias Audit on the `1,382` Unassessed Phase-6 Full-Text Records (`Weakness W-01` / PRISMA Item 16a)

*AI-generated second-model output. Not human verification.*

> **Why This Audit Matters (`WEAKNESSES.md` W-01):** Of the `3,659` records entering Phase 6 full-text assessment, **`1,382` (`37.8%`)** were never assessed (`182` `wrong_file_retrieved` + `1,200` `not_retrievable`, `327` carrying DOIs). Without altering the 2026-09-28 Phase-6 freeze or PRISMA counts, we drew a fixed-seed (`20261120`) stratified sample of **`80` unassessed records** (`40` `wrong_file_retrieved` + `28` DOI-bearing `not_retrievable` + `12` non-DOI `not_retrievable`), attempted legitimate Google Drive + Open-Access recovery with strict Page 1–2 identity verification, and blind-screened all recovered full texts (`+ 4` reruns).

---

## 1. Recovery & Blind Eligibility Results (`N = 80` Sampled Unassessed Records)

- **Complete Page 1–2 verified full texts recovered:** **`2 / 80` (`2.5%`)** (`wrong_file_retrieved`: `2/40` via direct Open-Access CDN endpoints; `not_retrievable`: `0/40`)
- **Independent blind validation of `wrong_file_retrieved` on Google Drive (`20` Drive PDFs inspected blind):** All `20` Google Drive PDFs matched by `record_id` in the `wrong_file_retrieved` stratum were independently flagged by `blind_screener_v2` (without seeing `stored_ft_status`) as `cannot_tell` — `19 / 20` as `WRONG_PAPER_MISMATCH` (genuinely wrong paper downloaded under that `record_id` in September 2026) and `1 / 20` (`R58E83E4193E6`, Cahill-Ripley 2011 Routledge monograph) as a partial preview missing empirical chapters. This independently confirms that `wrong_file_retrieved` (`182` rows) reflects genuine Sept-2026 scraper file-mismatch rather than mislabelled valid PDFs on Drive, while direct publisher OA endpoints (such as `mdpi-res.com` for `R909EC228A5A0`) can recover genuine OA articles from that pool.
- **Blind Eligibility Verdicts Among Recovered Full Texts (`N = 2`):**
  - **`include` (narrow Criterion 2):** **`1 / 2` (`50.0%`)** (`plain Criterion 2`: `1 / 2`)
  - **`exclude` (narrow Criterion 2):** **`1 / 2` (`50.0%`)**
- **Self-consistency (`4` reruns):** **`0 / 4` flips**
- **Verbatim quote verification:** **`95 / 95` (`100.00%`)** verified

---

## 2. Unassessed Phase-6 Records Judged `include` Under Narrow Criterion 2 (`N = 1`)

- **`R909EC228A5A0`** (2022, stored `wrong_file_retrieved`, source `https://mdpi-res.com/d_attachment/water/water-14-02369/article_deploy/water-14-02369.pdf`) — *"Performance Assessment for Increasing Connection Rates of Private Water Supply Operators in Cambodia"* -> **`include` (`high`)**: This empirical study in Cambodia meets all inclusion criteria under both the plain wording and the narrow 2026-10-13 rule-type reading of Criterion 2. Beyond testing physical network performance (pressure, turbidity, residual chlorine, and EPANET modeling) to rule out service-quality explanations for non-connection, it empirically evaluates MISTI-regulated connection-fee and flat-rate water-tariff rules, customer-borne pipe/meter connection charges, PWSO cost-recovery operating ratios, and MISTI-licensed service-area boundaries across three licensed private operators and 109 connected and non-connected households, demonstrating how regulated connection charges, flat tariffs, and oversized licensed service areas restrict household piped-water connection and low-income consumption.
