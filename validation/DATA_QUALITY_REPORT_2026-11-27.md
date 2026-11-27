# Data quality check of the published coded dataset (Harvard Dataverse `water_law_global_coded.csv`)

Checked 2026-11-27 by an AI-assisted pass over the file as deposited (file id 13765568, 83,596 rows). Counts are exact; interpretations are flagged as such. Nothing in the deposited data was changed. Cross-checks against the repository README and RESEARCH_CONTEXT.md are listed at the end.

## Rows per country

| Country | Rows | Distinct non-empty `case_id` | Rows with empty `case_id` |
|---|---|---|---|
| Brazil | 11,724 | 7,973 | 1,884 |
| Canada | 3,218 | 3,218 | 0 |
| Netherlands | 68,654 | 68,654 | 0 |

## Brazil

| Finding | Count |
|---|---|
| Courts present in the file | **TJDFT 8,421; TJRJ 1,219; TJSP 200; one unidentified court 1,884** (`court_name` = "Tribunal de Justiça do " with the state truncated, `tribunal`, `case_id` and `year` empty) |
| Rows sharing a `case_id` with another row | 1,867 extra rows (9,840 non-empty ids, 7,973 distinct) |
| Rows whose `summary` text appears more than once | 245 |
| `win_loss` = `unclear` | 7,243 of 11,724 (61.8%); among the 1,884 unidentified-court rows, 1,593 (84.6%) |
| Empty: `title` 98.3%, `url` 89.6%, `case_type` 72.2%, `date` and `chamber` 26.5%, `judge` 10.6% |  |

Interpretation (not verified): the unidentified rows look like one scraper's output (the recorded fields are those of an ESAJ-style ementa) whose court variable was never filled. The duplicates may be the same decision collected twice or distinct decisions with a reused id; the file cannot tell.

## Canada

- **`summary`, `date`, `case_type`, `chamber` and `judge` are empty for all 3,218 rows**; `url` is empty for 3,061 (95.1%). Only `case_id`, `title`, `year` and the court are populated.
- `year` is stored as a float string (`2023.0`).
- Every row has `win_loss` = `not_coded`.
- **Relevance doubt from titles alone (unverified):** a random draw of 8 titles included "Savard c. Établissement de détention Rivières-des-Prairies", "Nie v Blackfish Sales Ltd." (a yacht lien dispute), "Lakehead District School Board v. Mauro" and "Santé Québec ... c. A.L.". The Canadian set was collected by keyword search on titles, so, like the Dutch `other_water` rows, it likely contains many decisions that are not about water. This was not measured.
- **Text retrieval test (2026-11-27, Legal Data Hunter connector, 4 citations tried):** 2022 BCSC 682 resolved with full text (source CA/A2AJ, about 30 KB); 2023 ABCA 16, 2024 NSSC 296 and 2019 QCCS 2552 did not resolve. Four citations are an anecdote, not a coverage rate. A coverage test over a few hundred citations would need the repository's own `canada_ldh_scraper.py` with the `LDH_API_KEY`.

## Netherlands

- `chamber` and `judge` are empty for all 68,654 rows. `summary` is empty for 9,996 (14.6%), `case_type` for 10,133 (14.8%), `date` for 12.
- `win_loss` = `not_coded` for all rows (see `validation/nl_outcomes/`).
- Years are all within 2016 to 2026 (2026 has 2,616 rows, a partial year).
- 50,883 rows (74.1%) are in the catch-all category `other_water`; only 1,337 of those mention a water term in their summary, and 9,974 have no summary (see `validation/nl_outcomes/README.md`).
- `year` is stored as a float string.

## Cross-checks against repository documents (for the researcher to rule on)

1. `README.md` (line 11) says Brazil has 27 state courts. The deposited file contains three identified courts plus one unidentified.
2. `RESEARCH_CONTEXT.md` (line 91) says 86.9% of the Canadian records are title-only. In the deposited file **100%** are title-only. Either the deposit differs from the analysis file or the figure is out of date.
3. Brazil outcome coding ("AI-assisted", FUTURE_WORK.md Priority 2) leaves 61.8% `unclear`; any win-rate for Brazil should state that denominator.
4. The scrapers for TJAC, TJPI, TJRR, TJSC and TJTO exist in the repository, but no row in the deposited file carries those tribunal codes.
