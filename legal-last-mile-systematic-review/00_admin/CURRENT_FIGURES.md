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
| Full-text decided | 2,277 (1,078 include / 1,199 exclude) |
| Never decided (retrieval closed) | 1,382 (1,200 not_retrievable, 182 wrong_file_retrieved) |
| Exclusion-log rows | 1,199 — by code: E01 490, E02 34, E03 88, E04 87, E05 157, E06 106, E07 30, E08 8, E09 2, E10 151, E12 46 |
| Decided rows with blank / inferred reviewer_1 | 0 / 73 |
| Includes confirmed by a human reviewer_2 | 197 |
| Further decided rows ruled on by the PI under reviewer CK (adjudication passes, A6 and the A26 SWiM core confirmations) | 270 (166 excludes, 104 includes) |
| Includes confirmed by the PI in A6 as borderline (thin rule-type link; flagged, not removed) | 13 |
| Full-text rows with human verification or adjudication, in all / share of decided rows | 467 / 20.5% |
| SWiM core: studies in the three families / with a human-verified inclusion decision / with both direction codings confirmed by the author / flagged and awaiting the author | 37 / 27 / 18 / 10 |
| Decided rows blind-re-screened by a second AI model (reviewer_2 `Codex-…`) / conflicts | 112 / 31 |

## Extraction and classification

| Item | Figure |
|---|---|
| Extraction rows / evidence-map rows | 1,078 / 1,078 |
| Highest study ID; retired-ID gaps | S1169; S079, S197, S199, S201, S202, S203, S204, S205, S206, S209, S210, S211, S212, S215, S218, S221, S227, S230, S233, S235, S236, S243, S244, S246, S260, S264, S299, S312, S318, S320, S321, S322, S323, S324, S326, S327, S328, S329, S330, S332, S337, S340, S341, S342, S346, S347, S348, S356, S397, S399, S429, S430, S435, S436, S440, S462, S466, S479, S482, S513, S653, S673, S677, S693, S696, S697, S700, S707, S793, S796, S841, S854, S867, S896, S903, S931, S943, S945, S952, S969, S976, S1053, S1056, S1065, S1077, S1079, S1084, S1098, S1117, S1121, S1143 |
| Quantitative-synthesis-eligible / qualitative-synthesis-eligible | 231 / 986 |
| Abstract/metadata-only extractions | 10 |
| Linked-report links (same data yes / partial) | 12 (2 / 2) |
| Distinct studies (definite links / incl. partial) | 1,076 / 1,074 |

## Risk-of-bias tool distribution

Method: the *earliest* tool keyword in `risk_of_bias_tool` decides (substring matching anywhere mis-buckets annotated rows).

| Tool | Studies | % |
|---|---|---|
| RoB 2 | 5 | 0.5 |
| ROBINS-I | 57 | 5.3 |
| JBI Cross-Sectional | 129 | 12.0 |
| MMAT | 195 | 18.1 |
| CASP Qualitative | 248 | 23.0 |
| AMSTAR 2 | 18 | 1.7 |
| Legal Framework | 426 | 39.5 |

Tool-applicable studies (all tools except NONE): 1,078; unrated among them: 0. NONE studies: 0 (0 with an explicit NOT APPLICABLE note, 0 blank by design). Causal-capable designs (ROBINS-I + RoB 2): 62. CASP + MMAT: 443; with Legal Framework: 869. JBI "High concern" (sparse extraction): 51 of 129. Legal Framework studies with legal_measurement_quality populated: 373 of 426.

## Jurisdiction coverage (free-text fields; rule-based buckets, see current_figures.py)

`country`: 965 studies name exactly one country, 112 name several countries or a region, 1 are blank. Top single-country values: India 122, Brazil 80, South Africa 77, United States 62, Ghana 51, Kenya 47, Mexico 36, Indonesia 30, Bangladesh 24, Nigeria 24. `legal_system` buckets: blank 11, civil law 378, common law 509, mixed / both / customary 177, other 3.

## Certainty scale and ratings

`mechanism_certainty` numeric levels: 0: 4, 1: 326, 2: 715, 3: 29, 4: 4; every study carries a 0-4 code (narrative values normalised 2026-10-14). ROBINS-I ratings: Moderate 48, Serious 9. RoB 2 ratings: Some concerns 5.

## Effect sizes

58 rows (58 from quantitative-synthesis-eligible studies, 0 from a study not flagged eligible); by family: (none: reasoned non-fit) 21, A 16, B 5, C 16; rows pooled: 0.

