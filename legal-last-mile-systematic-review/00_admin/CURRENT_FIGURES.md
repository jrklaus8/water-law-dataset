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
| Full-text decided | 2,277 (1,104 include / 1,173 exclude) |
| Never decided (retrieval closed) | 1,382 (1,200 not_retrievable, 182 wrong_file_retrieved) |
| Exclusion-log rows | 1,173 — by code: E01 492, E02 34, E03 82, E04 84, E05 139, E06 106, E07 29, E08 8, E09 2, E10 151, E12 46 |
| Decided rows with blank reviewer_1 | 73 |
| Includes confirmed by a human reviewer_2 | 199 |
| Decided rows blind-re-screened by a second AI model (reviewer_2 `Codex-…`) / conflicts | 112 / 31 |

## Extraction and classification

| Item | Figure |
|---|---|
| Extraction rows / evidence-map rows | 1,104 / 1,104 |
| Highest study ID; retired-ID gaps | S1169; S197, S201, S202, S204, S205, S206, S209, S210, S211, S212, S215, S218, S221, S227, S230, S233, S235, S244, S264, S299, S312, S318, S321, S322, S323, S324, S327, S328, S329, S330, S332, S337, S340, S341, S342, S346, S347, S348, S356, S397, S399, S435, S462, S513, S653, S673, S677, S693, S696, S697, S700, S793, S796, S841, S854, S867, S896, S903, S931, S943, S945, S952, S969, S1053, S1117 |
| Quantitative-synthesis-eligible / qualitative-synthesis-eligible | 232 / 1,012 |
| Abstract/metadata-only extractions | 10 |
| Linked-report links (same data yes / partial) | 12 (2 / 2) |
| Distinct studies (definite links / incl. partial) | 1,102 / 1,100 |

## Risk-of-bias tool distribution

Method: the *earliest* tool keyword in `risk_of_bias_tool` decides (substring matching anywhere mis-buckets annotated rows).

| Tool | Studies | % |
|---|---|---|
| RoB 2 | 5 | 0.5 |
| ROBINS-I | 60 | 5.4 |
| JBI Cross-Sectional | 131 | 11.9 |
| MMAT | 196 | 17.8 |
| CASP Qualitative | 251 | 22.7 |
| AMSTAR 2 | 18 | 1.6 |
| Legal Framework | 433 | 39.2 |
| NONE | 10 | 0.9 |

Tool-applicable studies (all tools except NONE): 1,094; unrated among them: 0. NONE studies: 10 (3 with an explicit NOT APPLICABLE note, 7 blank by design). Causal-capable designs (ROBINS-I + RoB 2): 65. CASP + MMAT: 447; with Legal Framework: 880. JBI "High concern" (sparse extraction): 50 of 131. Legal Framework studies with legal_measurement_quality populated: 377 of 433.

## Jurisdiction coverage (free-text fields; rule-based buckets, see current_figures.py)

`country`: 986 studies name exactly one country, 116 name several countries or a region, 2 are blank. Top single-country values: India 126, Brazil 81, South Africa 78, United States 67, Ghana 51, Kenya 47, Mexico 37, Indonesia 30, Nigeria 27, Bangladesh 24. `legal_system` buckets: blank 13, civil law 385, common law 522, mixed / both / customary 181, other 3.

## Certainty scale and ratings

`mechanism_certainty` numeric levels: 0: 4, 1: 222, 2: 270, 3: 25, 4: 8; 575 studies carry narrative text instead of a 0-4 code. ROBINS-I ratings: Moderate 51, Serious 9. RoB 2 ratings: Some concerns 5.

## Effect sizes

59 rows (59 from quantitative-synthesis-eligible studies, 0 from a study not flagged eligible); by family: (none: reasoned non-fit) 15, A 18, B 6, C 20; rows pooled: 0.

