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
| Full-text decided | 2,276 (1,144 include / 1,132 exclude) |
| Never decided (retrieval closed) | 1,383 (1,201 not_retrievable, 182 wrong_file_retrieved) |
| Exclusion-log rows | 1,132 — by code: E01 495, E02 34, E03 44, E04 81, E05 138, E06 105, E07 27, E08 8, E09 2, E10 151, E12 47 |
| Decided rows with blank reviewer_1 | 73 |
| Includes confirmed by a human reviewer_2 | 200 |
| Decided rows blind-re-screened by a second AI model (reviewer_2 `Codex-…`) / conflicts | 114 / 31 |

## Extraction and classification

| Item | Figure |
|---|---|
| Extraction rows / evidence-map rows | 1,144 / 1,144 |
| Highest study ID; retired-ID gaps | S1167; S206, S227, S233, S299, S312, S321, S322, S323, S324, S327, S328, S329, S337, S340, S356, S397, S399, S435, S513, S696, S841, S1053, S1117 |
| Quantitative-synthesis-eligible / qualitative-synthesis-eligible | 243 / 1,047 |
| Abstract/metadata-only extractions | 11 |
| Linked-report links (same data yes / partial) | 12 (2 / 2) |
| Distinct studies (definite links / incl. partial) | 1,142 / 1,140 |

## Risk-of-bias tool distribution

Method: the *earliest* tool keyword in `risk_of_bias_tool` decides (substring matching anywhere mis-buckets annotated rows).

| Tool | Studies | % |
|---|---|---|
| RoB 2 | 5 | 0.4 |
| ROBINS-I | 61 | 5.3 |
| JBI Cross-Sectional | 138 | 12.1 |
| MMAT | 205 | 17.9 |
| CASP Qualitative | 262 | 22.9 |
| AMSTAR 2 | 18 | 1.6 |
| Legal Framework | 444 | 38.8 |
| NONE | 11 | 1.0 |

Tool-applicable studies (all tools except NONE): 1,133; unrated among them: 0. NONE studies: 11 (3 with an explicit NOT APPLICABLE note, 8 blank by design). Causal-capable designs (ROBINS-I + RoB 2): 66. CASP + MMAT: 467; with Legal Framework: 911. JBI "High concern" (sparse extraction): 55 of 138. Legal Framework studies with legal_measurement_quality populated: 386 of 444.

## Jurisdiction coverage (free-text fields; rule-based buckets, see current_figures.py)

`country`: 1,023 studies name exactly one country, 119 name several countries or a region, 2 are blank. Top single-country values: India 132, Brazil 85, South Africa 83, United States 69, Ghana 52, Kenya 50, Mexico 37, Indonesia 30, Bangladesh 27, Nigeria 27. `legal_system` buckets: blank 19, civil law 395, common law 542, mixed / both / customary 185, other 3.

## Certainty scale and ratings

`mechanism_certainty` numeric levels: 0: 4, 1: 238, 2: 276, 3: 26, 4: 8; 592 studies carry narrative text instead of a 0-4 code. ROBINS-I ratings: Moderate 51, Serious 10. RoB 2 ratings: Some concerns 5.

## Effect sizes

61 rows (60 from quantitative-synthesis-eligible studies, 1 from a study not flagged eligible); by family: (none: reasoned non-fit) 15, A 20, B 6, C 20; rows pooled: 0.

