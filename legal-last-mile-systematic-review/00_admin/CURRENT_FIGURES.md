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
| Full-text decided | 2,276 (1,159 include / 1,117 exclude) |
| Never decided (retrieval closed) | 1,383 (1,201 not_retrievable, 182 wrong_file_retrieved) |
| Exclusion-log rows | 1,117 — by code: E01 496, E02 34, E03 34, E04 77, E05 135, E06 106, E07 26, E08 8, E09 2, E10 151, E12 48 |
| Decided rows with blank reviewer_1 | 73 |
| Includes confirmed by a human reviewer_2 | 200 |
| Decided rows blind-re-screened by a second AI model (reviewer_2 `Codex-…`) / conflicts | 121 / 38 |

## Extraction and classification

| Item | Figure |
|---|---|
| Extraction rows / evidence-map rows | 1,159 / 1,159 |
| Highest study ID; retired-ID gaps | S1164; S227, S233, S299, S356, S399 |
| Quantitative-synthesis-eligible / qualitative-synthesis-eligible | 247 / 1,059 |
| Abstract/metadata-only extractions | 11 |
| Linked-report links (same data yes / partial) | 12 (2 / 2) |
| Distinct studies (definite links / incl. partial) | 1,157 / 1,155 |

## Risk-of-bias tool distribution

Method: the *earliest* tool keyword in `risk_of_bias_tool` decides (substring matching anywhere mis-buckets annotated rows).

| Tool | Studies | % |
|---|---|---|
| RoB 2 | 5 | 0.4 |
| ROBINS-I | 63 | 5.4 |
| JBI Cross-Sectional | 140 | 12.1 |
| MMAT | 205 | 17.7 |
| CASP Qualitative | 263 | 22.7 |
| AMSTAR 2 | 23 | 2.0 |
| Legal Framework | 447 | 38.6 |
| NONE | 13 | 1.1 |

Tool-applicable studies (all tools except NONE): 1,146; unrated among them: 0. NONE studies: 13 (5 with an explicit NOT APPLICABLE note, 8 blank by design). Causal-capable designs (ROBINS-I + RoB 2): 68. CASP + MMAT: 468; with Legal Framework: 915. JBI "High concern" (sparse extraction): 55 of 140. Legal Framework studies with legal_measurement_quality populated: 389 of 447.

## Jurisdiction coverage (free-text fields; rule-based buckets, see current_figures.py)

`country`: 1,031 studies name exactly one country, 126 name several countries or a region, 2 are blank. Top single-country values: India 133, Brazil 87, South Africa 84, United States 71, Ghana 53, Kenya 50, Mexico 37, Indonesia 30, Nigeria 28, Bangladesh 27. `legal_system` buckets: blank 28, civil law 394, common law 546, mixed / both / customary 188, other 3.

## Certainty scale and ratings

`mechanism_certainty` numeric levels: 0: 4, 1: 238, 2: 286, 3: 27, 4: 8; 596 studies carry narrative text instead of a 0-4 code. ROBINS-I ratings: Moderate 54, Serious 9. RoB 2 ratings: Some concerns 5.

## Effect sizes

62 rows (61 from quantitative-synthesis-eligible studies, 1 from a study not flagged eligible); by family: (none: reasoned non-fit) 16, A 20, B 6, C 20; rows pooled: 0.

