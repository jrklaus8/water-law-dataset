# 02_screening — who was included and who was excluded, and why

Two stages, each with its own database, because their reviewers and rules differ.

| Folder | What it holds |
|---|---|
| `title_abstract/` | `screening_database.csv` — one row per unique record, with the AI's decision and a written reason (`ai_first_pass_rationale.csv`); the human second pass on the include-or-unsure records (`reviewer_2_queue.csv`, `REVIEWER_2_README.md`); a random spot-check of the exclusions |
| `full_text/` | `full_text_screening_database.csv` — **the single source of truth for the full-text stage**: one row per candidate with the decision, the coded reason, `reviewer_1` (the AI) and `reviewer_2` (human, `CK`, or another AI). Start with `FULL_TEXT_README.md` |
| `exclusion_log/exclusion_log.csv` | One row per full-text exclusion with its code (`E01` … `E12`, defined in `../INCLUSION_EXCLUSION.md`) |

**The `A…` files in `full_text/`** (`A16_ADJUDICATION_FILLED_…csv`, `A28_ADJUDICATION_FILLED_…csv`, `A6_TIER1_…`, …) are the sheets on which the principal investigator recorded rulings on contested decisions; the `*_SHEET_*` files are the blank versions the AI prepared with the evidence to read. The number refers to the item in `../00_admin/DECISIONS_AND_OPEN_ITEMS.md`.

**Who checked it:** the AI made the first decision on every record. A human second reviewer covered the title/abstract include-or-unsure records (not the AI's exclusions) and part of the full-text decisions; a second AI model blind re-screened a sample. The exact counts are in `../00_admin/CURRENT_FIGURES.md` and `../AI_USE_STATEMENT.md`.

**Known limitation:** full-text retrieval was closed with part of the candidates never assessed; those rows are marked `not_retrievable` or `wrong_file_retrieved`.
