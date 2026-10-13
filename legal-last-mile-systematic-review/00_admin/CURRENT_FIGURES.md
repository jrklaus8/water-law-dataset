# Current figures (generated — do not edit by hand)

Produced by `code/analysis/current_figures.py --write` from the CSV databases; `code/analysis/verify_repository.py`
checks that the current-status documents quote these values. If a document disagrees with this file, this file is right
(or the databases changed and this file needs regenerating — run the script). Historical, dated documents
(`CHANGELOG.md` entries, audit reports, `preliminary_*` logs) intentionally keep the figures that were true when written.

## Screening

| Stage | Figure |
|---|---|
| Title/abstract | 3,659 include / 6 exclude |
| Full-text records tracked | 3,659 |
| Full-text decided | 2,276 (1,157 include / 1,119 exclude) |
| Never decided (retrieval closed) | 1,383 (1,201 not_retrievable, 182 wrong_file_retrieved) |
| Exclusion-log rows | 1,119 — by code: E01 495, E02 34, E03 34, E04 79, E05 138, E06 104, E07 27, E08 8, E09 2, E10 151, E12 47 |
| Decided rows with blank reviewer_1 | 73 |
| Includes confirmed by a human reviewer_2 | 200 |
| Decided rows blind-re-screened by a second AI model (reviewer_2 `Codex-…`) / conflicts | 114 / 31 |

## Extraction and classification

| Item | Figure |
|---|---|
| Extraction rows / evidence-map rows | 1,157 / 1,157 |
| Highest study ID; retired-ID gaps | S1167; S227, S233, S299, S340, S356, S397, S399, S513, S1053, S1117 |
| Quantitative-synthesis-eligible / qualitative-synthesis-eligible | 247 / 1,057 |
| Abstract/metadata-only extractions | 11 |
| Linked-report links (same data yes / partial) | 12 (2 / 2) |
| Distinct studies (definite links / incl. partial) | 1,155 / 1,153 |

## Risk-of-bias tool distribution

Method: the *earliest* tool keyword in `risk_of_bias_tool` decides (substring matching anywhere mis-buckets annotated rows).

| Tool | Studies | % |
|---|---|---|
| RoB 2 | 5 | 0.4 |
| ROBINS-I | 63 | 5.4 |
| JBI Cross-Sectional | 141 | 12.2 |
| MMAT | 205 | 17.7 |
| CASP Qualitative | 263 | 22.7 |
| AMSTAR 2 | 23 | 2.0 |
| Legal Framework | 444 | 38.4 |
| NONE | 13 | 1.1 |

Tool-applicable studies (all tools except NONE): 1,144; unrated among them: 0. NONE studies: 13 (5 with an explicit NOT APPLICABLE note, 8 blank by design). Causal-capable designs (ROBINS-I + RoB 2): 68. CASP + MMAT: 468; with Legal Framework: 912. JBI "High concern" (sparse extraction): 56 of 141. Legal Framework studies with legal_measurement_quality populated: 386 of 444.

## Jurisdiction coverage (free-text fields; rule-based buckets, see current_figures.py)

`country`: 1,030 studies name exactly one country, 125 name several countries or a region, 2 are blank. Top single-country values: India 132, Brazil 86, South Africa 83, United States 71, Ghana 53, Kenya 50, Mexico 37, Indonesia 30, Nigeria 28, Bangladesh 27. `legal_system` buckets: blank 27, civil law 395, common law 545, mixed / both / customary 187, other 3.

## Certainty scale and ratings

`mechanism_certainty` numeric levels: 0: 4, 1: 241, 2: 283, 3: 27, 4: 8; 594 studies carry narrative text instead of a 0-4 code. ROBINS-I ratings: Moderate 53, Serious 10. RoB 2 ratings: Some concerns 5.

## Effect sizes

63 rows (62 from quantitative-synthesis-eligible studies, 1 from a study not flagged eligible); by family: (none: reasoned non-fit) 17, A 20, B 6, C 20; rows pooled: 0.

