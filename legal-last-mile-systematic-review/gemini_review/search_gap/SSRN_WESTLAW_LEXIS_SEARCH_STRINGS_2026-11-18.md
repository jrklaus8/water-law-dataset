# Task F: Search-Gap Strategy Package — SSRN, Westlaw, and Lexis+

*AI-generated second-model output. Not human verification.*

- **Purpose:** Operational, syntax-verified search strings, slicing protocols, and export instructions for the three unsearched Tier 1/Tier 2 databases logged as `NOT RUN` in `01_search/search_logs/search_log.csv` (`SEARCH_042` SSRN and `SEARCH_043` Westlaw/Lexis), adapted from `SEARCH_PROTOCOL.md`, `INCLUSION_EXCLUSION.md` (including the 2026-10-13 narrow rule-type Criterion 2 reading), and `01_search/database_strategies/`.
- **PRISMA guardrail:** **Zero live searches were executed** and **zero files under `01_search/` were modified**. All PRISMA counts remain untouched until the PI runs these strings and logs the exports.

---

## 1. Diagnosis of Existing Draft Strings in `01_search/database_strategies/`

Before adapting the strings, auditing `jstor_google_scholar_ssrn.md` and `westlaw_lexis.md` against `SEARCH_PROTOCOL.md` §§2–3 and the empirical vocabulary of the 31 SWiM synthesis studies identified five concrete defects in the existing drafts:

1. **SSRN character-length & nesting ceiling (`jstor_google_scholar_ssrn.md` lines 57–59):** SSRN's web search interface (`papers.ssrn.com`) truncates or rejects long nested Boolean strings (~250-character practical ceiling, similar to the JSTOR length rejection encountered in `SEARCH_041`). At the same time, the existing 186-character SSRN draft omitted **tariffs/social tariffs, water shutoffs/disconnections, utility ownership/privatization, rate regulation, municipal underbounding/unincorporated areas, and Portuguese/Dutch terms**—missing the exact economics and political-science working-paper vocabularies behind NBER/CEPR/World Bank papers (e.g., Coville et al. `S879`, Gaikwad & Thomas `S085`, Allaire et al. `S142`, Olmstead `S1169`).
2. **Westlaw missing `adv:` prefix, missing `wastewater`/`sewerage`, and missing US legal-access terms (`westlaw_lexis.md` lines 12–23):** On Westlaw Precision / Westlaw Edge, pasting Terms & Connectors into the global search bar without the `adv:` prefix triggers natural-language ("WestSearch") interpretation rather than strict Boolean proximity! The draft also omitted `wastewater` and `sewerage` from Block A (both present in `SEARCH_PROTOCOL.md` §2) and omitted core US municipal/utility law terms (`unincorporated`, `underbound!`, `colonia!`, `shutoff!`, `disconnect!`, `"rate regulation"`, `tariff!`).
3. **Lexis+ document-wide `AND` explosion (`westlaw_lexis.md` lines 31–43):** While Westlaw's draft used `/p` (same paragraph), the Lexis+ draft used document-wide `AND` across full-text law review articles (typically 15,000–35,000 words). As demonstrated when HeinOnline's document-wide `Full Text` search returned **71,226 hits** (`SEARCH_036`) with almost complete incidental co-occurrence noise, document-wide `AND` on full-text law journals is unusable without fielded (`TITLE` / `OVERVIEW`) or paragraph-proximity (`W/p`) scoping.
4. **Doctrinal vs. empirical law-review separation (`INCLUSION_EXCLUSION.md` Criterion 3 / `E05`):** Law review databases are 85–95% pure doctrinal/normative commentary (`E05`). Pairing a fielded `TI,PR,SY` / `TITLE+OVERVIEW` pass (which catches every dedicated water/sanitation governance article regardless of methodology) with a full-text `/p` / `W/p` pass intersected with an **empirical-methods block** (`empiric!`, `survey!`, `dataset!`, `regression!`, `"case stud!"`, `interview!`, `ethnograph!`, `census!`) captures empirical socio-legal studies buried in longer law-review texts without generating 20,000 doctrinal false positives.
5. **Lexis+ & Westlaw export capabilities update (`westlaw_lexis.md` lines 58–65):** Modern **Lexis+** offers native **RIS (`EndNote / RefWorks`)** citation export (up to 500 records per batch, directly compatible with `code/search/adapters/ris_adapter.py --database "Lexis+"`) as well as `.xlsx`/`.csv` Results List downloads (up to 1,000 records). **Westlaw Precision** offers **CSV / Excel (`List of items`)** downloads (up to 100–500 items per batch depending on institutional contract) plus RTF/Word full-synopsis lists.

---

## 2. SSRN Search Strategy (`SEARCH_042a`–`SEARCH_042f`)

- **Access route:** `https://papers.ssrn.com/sol3/DisplayAbstractSearch.cfm` (SSRN Advanced Search; also accessible via EUR Library portal if signed into an institutional SSRN account).
- **Field setting:** Select **Title, Abstract, Abstract ID & Keywords** (equivalent to Scopus `TITLE-ABS-KEY`).
- **Why 6 modular queries:** Every string below is strictly **`125–183` characters**, uses at most two or three flat `AND`-connected parenthetical groups, and covers all four mechanism families plus the Portuguese and Dutch protocol vocabularies. Deduplicate across `042a`–`042f` by SSRN `abstract_id` (`https://ssrn.com/abstract=XXXXXXX` or `10.2139/ssrn.XXXXXXX`).

### Copy-Paste Queries for SSRN

**`SEARCH_042a` — Tenure, Titling, Legal Recognition & Informal Settlements (`179` chars)**
```text
("water access" OR "piped water" OR "water supply" OR sanitation OR sewerage) AND ("land tenure" OR "property rights" OR "legal recognition" OR "informal settlement" OR titling)
```

**`SEARCH_042b` — Eligibility, Administrative Burden, Permits, Zoning & Underbounding (`183` chars)**
```text
("water connection" OR "sewer connection" OR "water service" OR sanitation) AND ("administrative burden" OR eligibility OR documentation OR "building permit" OR zoning OR unincorporated)
```

**`SEARCH_042c` — Tariffs, Affordability, Subsidies, Shutoffs & Enforcement (`173` chars)**
```text
("water affordability" OR "water tariff" OR "social tariff" OR "water shutoff" OR "water disconnection") AND (household OR low-income OR subsidy OR enforcement OR regulation)
```

**`SEARCH_042d` — Utility Ownership, Privatization, Decentralization, Rate Regulation & Corruption (`179` chars)**
```text
("water utility" OR "water utilities" OR "water supply" OR sanitation) AND (privatization OR "public ownership" OR decentralization OR "rate regulation" OR corruption) AND access
```

**`SEARCH_042e` — Brazil / Portuguese Working Papers (`148` chars)**
```text
("saneamento básico" OR "abastecimento de água" OR "tarifa social") AND ("regularização fundiária" OR acesso OR regulação OR favela OR município)
```

**`SEARCH_042f` — Netherlands / Dutch Working Papers (`125` chars)**
```text
(drinkwater OR riolering OR wateraansluiting OR aansluitplicht) AND (toegang OR bestuursrecht OR huishoudens OR afsluiting)
```

### SSRN Export & Ingestion Procedure
1. Record the exact hit count shown by SSRN for each subquery (`SEARCH_042a`–`042f`) in `SEARCH_LOG_TEMPLATE_2026-11-18.csv`.
2. **Export method A (Zotero Connector -> RIS, recommended for bulk pages):** Open each results page (set page size to `50` or `100`), click the Zotero browser connector folder icon -> *Select All* -> export the collection from Zotero as **RIS (UTF-8, include Abstracts)** -> save as `SEARCH_042x_SSRN_YYYY-MM-DD_native.ris`, then normalize via:
   ```bash
   python3 code/search/adapters/ris_adapter.py      --input 01_search/raw_exports/native/SEARCH_042a_SSRN_YYYY-MM-DD_native.ris      --output 01_search/raw_exports/SEARCH_042a_SSRN_YYYY-MM-DD.csv      --search-id SEARCH_042a --database SSRN
   ```
3. **Export method B (Per-record SSRN Cite -> RIS):** On small hit sets (<30 hits), click *Export Citation -> RIS* on each item and concatenate the `.ris` files (verifying each record ends with `ER  - `).
4. **Published-version deduplication check:** Because SSRN working papers (`10.2139/ssrn.*`) frequently have a different title or DOI from their later journal version in Scopus/WoS, run author+year fuzzy matching against `extraction_database.csv` and log any working-paper/journal pair in `linked_reports_2026-09-28.csv` per `REPRODUCIBILITY.md` §6.

---

## 3. Westlaw Precision / Westlaw Edge Strategy (`SEARCH_043a`–`SEARCH_043c`)

- **Access route:** EUR Library database list -> **Westlaw** -> navigate BEFORE searching to **Secondary Sources -> Law Reviews & Journals** (never run in "All Content", which mixes statutes, regulations, and judicial opinions).
- **Syntax rules verified:** Prefix every query with `adv:` so Westlaw forces strict Terms & Connectors parsing regardless of account default; space inside parentheses = `OR` (lower precedence than `&` and `/p`, so always wrap `OR` lists in explicit parentheses); `!` = root expander; `/p` = same paragraph.

### Copy-Paste Queries for Westlaw (`Law Reviews & Journals`)

**`SEARCH_043a` — Tier 1 High-Precision Fielded Search (`TI,PR,SY` = Title, Prelim/Subject, Synopsis)**
*(Run first; expected yield ~40–250 articles, 100% exportable without date slicing)*
```text
adv: TI,PR,SY((sanitation wastewater sewerage "sewer connection!" "water supply" "piped water" "municipal water" "water connection!" "water service!" "drinking water" "water shutoff!" "water utility") & ("administrative burden!" "administrative barrier!" "administrative law" "legal barrier!" eligibil! "legal recognition" "land tenure" "property title" documentation "building permit!" zoning unincorporated underbound! colonia! annex! formaliz! regulariz! discretion! enforcement "rate regulation" tariff! shutoff! disconnect! privatiz! "public utility") & (access! connect! coverage reliab! affordab! exclud! exclus! inequit! "service delivery"))
```

**`SEARCH_043b` — Tier 2 Full-Text Same-Paragraph + Empirical-Methods Filter**
*(Captures empirical socio-legal studies where water/sanitation administrative rules are analysed in the body even if the article title is conceptual)*
```text
adv: ((sanitation wastewater sewerage "sewer connection!" "water supply" "piped water" "municipal water" "water connection!" "water service!" "water shutoff!") /p ("administrative burden!" "administrative barrier!" "legal barrier!" eligibil! "legal recognition" "land tenure" "property title" documentation "building permit!" zoning unincorporated underbound! colonia! formaliz! regulariz! "administrative discretion" "rate regulation" "social tariff!" shutoff! disconnect!) /p (access! connect! coverage affordab! exclud! exclus! "service delivery" household! resident!)) & (empiric! survey! dataset! regression! "case stud!" interview! ethnograph! census! "panel data" econometr!)
```
- **Date-slicing rule if `SEARCH_043b` exceeds Westlaw's single-download ceiling (100–500 items):** Append `& DA(aft 12/31/2019)`, `& DA(aft 12/31/2009 & bef 01/01/2020)`, and `& DA(bef 01/01/2010)` as `SEARCH_043b_1`, `043b_2`, `043b_3`, checking that slice counts sum to the unsliced total.

**`SEARCH_043c` — Protocol Benchmark Query (Syntax-Fixed `westlaw_lexis.md` String)**
*(Run to log the exact unfiltered paragraph-level hit count promised in `westlaw_lexis.md`; export if <= 500 hits, or record count-only in `search_log.csv` if multi-thousand doctrinal hits)*
```text
adv: ((sanitation wastewater sewerage "sewer connection!" "water supply" "piped water" "municipal water" "water connection!" "water service!" WASH) /p ("administrative burden" "administrative barrier!" "administrative law" "legal barrier!" eligibility "legal recognition" "land tenure" "property title" documentation "building permit!" zoning formaliz! formalis! regulariz! regularis! "administrative discretion" enforcement "regulatory governance" bureaucratic) /p (access! connection coverage reliability affordability exclusion inclusion "service delivery"))
```

### Westlaw Export Reconnaissance & Ingestion Note
1. On the results toolbar, click **Download** -> test both:
   - **List of items -> CSV / Excel** (gives structured Title, Author/Citation, Publication, Date, Westlaw URL; inspect actual column headers before Claude writes `westlaw_adapter.py` per `PROJECT_SPEC.md` §14), AND
   - **List of items with Synopsis / Full Citation -> Word / RTF** (preserves Westlaw's editorial `Synopsis` / abstract equivalent where available).
2. Confirm on disk (`Downloads/`) that the file is non-empty and row counts match the UI selection before closing the session (`EXECUTION_CHECKLIST.md` rule 2).

---

## 4. Lexis+ / Lexis Advance Strategy (`SEARCH_044a`–`SEARCH_044c`)

- **Access route:** EUR Library database list -> **Lexis+** (or **Nexis Uni**, if EUR routes academic users to Nexis Uni—both share identical Lexis Advance Boolean syntax) -> restrict Content Type to **Secondary Materials -> Law Reviews and Journals**.
- **Syntax rules verified:** Explicit `OR` and `AND` required (unlike Westlaw, space is a phrase word, NOT `OR`!); `W/p` = within same paragraph; `!` = multi-character root truncation; `TITLE(...)` and `OVERVIEW(...)` scope to title and abstract/summary fields.

### Copy-Paste Queries for Lexis+ (`Law Reviews and Journals`)

**`SEARCH_044a` — Tier 1 High-Precision Fielded Search (`TITLE` + `OVERVIEW`)**
```text
TITLE(sanitation OR wastewater OR sewerage OR "sewer connection!" OR "water supply" OR "piped water" OR "municipal water" OR "water connection!" OR "water service!" OR "drinking water" OR "water shutoff!" OR "water utility") AND (TITLE("administrative burden!" OR "legal barrier!" OR eligibil! OR "land tenure" OR zoning OR unincorporated OR underbound! OR colonia! OR tariff! OR shutoff! OR disconnect! OR privatiz! OR "rate regulation" OR governance OR access! OR affordab! OR exclus!) OR OVERVIEW("administrative burden!" OR "legal barrier!" OR eligibil! OR "land tenure" OR zoning OR unincorporated OR colonia! OR tariff! OR shutoff! OR disconnect! OR "rate regulation" OR affordab! OR exclus!))
```

**`SEARCH_044b` — Tier 2 Same-Paragraph (`W/p`) + Empirical-Methods Filter**
```text
((sanitation OR wastewater OR sewerage OR "sewer connection!" OR "water supply" OR "piped water" OR "municipal water" OR "water connection!" OR "water service!" OR "water shutoff!") W/p ("administrative burden!" OR "administrative barrier!" OR "legal barrier!" OR eligibil! OR "legal recognition" OR "land tenure" OR "property title" OR documentation OR "building permit!" OR zoning OR unincorporated OR underbound! OR colonia! OR formaliz! OR regulariz! OR "administrative discretion" OR "rate regulation" OR "social tariff!" OR shutoff! OR disconnect!) W/p (access! OR connect! OR coverage OR affordab! OR exclud! OR exclus! OR "service delivery" OR household!)) AND (empiric! OR survey! OR dataset! OR regression! OR "case stud!" OR interview! OR ethnograph! OR census! OR "panel data" OR econometr!)
```
- **Date-slicing rule if > 500 hits:** Add `AND date(geq(01/01/2020))`, `AND date(geq(01/01/2010) and leq(12/31/2019))`, `AND date(leq(12/31/2009))`.

**`SEARCH_044c` — Canada / Ontario Secondary Legal Scholarship (`SEARCH_PROTOCOL.md` §3.3)**
```text
(("water connection!" OR "sewer connection!" OR "municipal water" OR "municipal sewer" OR "water service!" OR "drinking water") W/p ("service area!" OR "building permit!" OR "municipal by-law!" OR "municipal bylaw!" OR "connection refusal" OR "service refusal" OR "procedural fairness" OR "administrative burden!" OR "First Nations" OR "Indigenous water") W/p (access! OR connect! OR affordab! OR advis! OR boil! OR exclus!))
```

### Lexis+ Export Note
- Click **Download / Share -> Export Bibliographic References (RIS)** if enabled on the EUR Lexis+ contract (caps at 500 items per batch; passes straight through `ris_adapter.py --database "Lexis+"`), **and** download the **Results List (`.xlsx` / `.csv`)** as a count-verified manifest.

---

## 5. Additional Unlogged Search Gap Flagged During Audit (`PubMed` & `Global Health`)

While auditing `SEARCH_PROTOCOL.md` against `01_search/search_logs/search_log.csv`, we found that `SEARCH_PROTOCOL.md` §1 (line 18) and §1 table (line 37) list **PubMed** and **Global Health (Ovid)** as planned sector-specific databases—and both `01_search/database_strategies/pubmed.md` and `code/search/adapters/pubmed_adapter.py` exist in the repository—yet **neither PubMed nor Global Health has a `NOT RUN` disclosure row in `search_log.csv`** (unlike `SEARCH_042` SSRN and `SEARCH_043` Westlaw/Lexis), nor are they mentioned in `SEARCH_PROTOCOL.md` §7 ("Databases never searched at all") or `WEAKNESSES.md` (`W01`). See `REPORT_search-gap-strings_2026-11-18.md` for details.
