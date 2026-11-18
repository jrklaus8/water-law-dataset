# Research protocol of the court-decision dataset

This page reconstructs, from the repository, how the court-decision dataset was designed, collected, coded and validated. It exists because **no protocol for the dataset was written before collection that the repository can show**. Everything below is therefore a *description of what the files say was done*, not a plan that was fixed in advance. Where the repository is silent the page says so.

The systematic review that accompanies the dataset does have a dated protocol: see [`legal-last-mile-systematic-review/PROTOCOL.md`](../legal-last-mile-systematic-review/PROTOCOL.md) (fixed 2026-08-22, before any database was searched; not registered). This page does not repeat it.

*Written by an AI assistant (Claude Code), 2026-10-27, for the researcher to check and correct. It records no research activity that the repository does not show.*

## 1. Purpose

The dataset is the empirical backbone of the researcher's preliminary research "The Legal Last Mile" (`RESEARCH_CONTEXT.md`): how administrative law frameworks condition access to sanitation infrastructure at the point of connection, compared across Brazil, the Netherlands and Canada (Ontario) with a most-different-systems design. The research context states a theory (gatekeeper thesis, "administrative ghost", pre- versus post-litigation accommodation) and treats the dataset as a way to test it.

## 2. Unit of analysis and scope

- Unit: one published court decision (a record in the unified 13-field schema in `utils/merge_national.py`).
- Years: 2016–2026, plus 200 hand-coded São Paulo decisions from 1997–2015.
- Jurisdictions and sources: see [`source-register.md`](source-register.md). Brazil: 8 of 27 state courts (the others were not accessible); Canada: CanLII and Legal Data Hunter; Netherlands: Rechtspraak open data, appellate and district courts.
- Text analysed: the decision summary or ementa, and the title and metadata fields. For the Netherlands the stored text is the summary field (*inhoudsindicatie*, truncated to 2,000 characters in `rechtspraak_scraper.py`); the full decision text is not coded.

## 3. Selection of decisions

| Country | How a decision gets into the dataset |
|---|---|
| Brazil | Search of each court's portal with the three queries in the README (`água abastecimento fornecimento saneamento`; `corte suspensão fornecimento água`; `proteção manancial recursos hídricos ambiental`); results kept for the years 2016–2026 |
| Canada | CanLII API title and keyword search, additional CanLII databases, superior and appellate courts, and Legal Data Hunter semantic search; a case-level water filter (`is_water_case` in `canlii_scraper.py`) tests title and keywords against water terms |
| Netherlands | Enumeration of decisions per court through the open-data feed, then a water filter on the summary and legal-area text (`is_water`); district-court enumeration is pre-filtered to the environmental/planning subject area |

The Dutch filter is deliberately wide (a substring test), which is why most of the Dutch records are later classified as not water-related.

## 4. Coding framework

Coding is done by `utils/jurimetric_coding.py`, a set of regular-expression rules, not by a statistical model. From the code and README:

- **Governance category** (`code_governance`): 21 categories (README), assigned by the first matching rule in a fixed order; a decision without core water vocabulary is coded `not_water_related`.
- **Human-rights language** (`code_hr`), **sustainability language** (`code_sust`), **public-interest and Indigenous indicators** (`code_public`, `code_indigenous`): binary flags from keyword patterns in four languages (Portuguese, English, Dutch, French).
- **Outcome** (`code_win_loss`): Brazil only; classes `user_wins`, `utility_wins`, `mixed`, `unclear`, `not_coded` (other countries). **Known defects** in some patterns are documented in finding F-08 and are recorded as expected failures in `tests/test_offline_helpers.py`.
- **Ministério Público involvement** (`code_mp`): Brazil only.

The rules were written with AI assistance ([`ai-use-and-disclosure.md`](ai-use-and-disclosure.md)). Their intended definitions are in `RESEARCH_CONTEXT.md` and the code comments; there is no separate codebook for the court dataset (see [`data-management.md`](data-management.md)).

## 5. Validation that the repository records

| Check | What it covers | Who | Result stated in the repository | Limit |
|---|---|---|---|---|
| Residual audit | The `other_water` residual bucket | author | genuine residual reduced from 89.2% to 8.3% by the v0.3.0 filter (`validation/README.md`) | the same README states the starting residual as 69% of all decisions (57,695) in its opening paragraph and as 89.2% in the next sentence; the two should be reconciled (pull request #9, not merged, corrects related validation documents) |
| Gold standard for the water/not-water filter | 207 decisions hand-coded | author alone | population-weighted precision 99.79% | single coder; the author also designed the rules; recall is not estimated for the whole data |
| Agreement check | 91 decisions relabelled by an LLM | LLM vs author | κ = 0.832 with a documented rule (0.568 before it was added) | not a human second coder (F-22); the rule was added after the disagreements were seen |
| Outcome coding (win/loss) | not described as validated | none | none | F-08 |
| Governance categories (21) | not described as validated | none | "future work" (`validation/README.md`) | |

## 6. What was fixed in advance, what changed, and what is not recorded

- **Fixed in advance:** not documented for the dataset.
- **Changed after results were visible:** the water/not-water filter was revised in v0.3.0 after the residual audit (`validation/README.md`, `SUPERVISOR_REPORT_v0.3.0.md`). Earlier states are in Git history.
- **Not recorded:** collection dates; the order in which courts were tried; which queries were dropped; whether any decisions were removed by hand. The review has registers of deviations and errors; the dataset has none. A register for the dataset would be a good addition (see [`audit-report.md`](audit-report.md), section H).

## 7. Pre-registration and ethics

No registration of the dataset's design and no ethics review or exemption is recorded in the repository. An OSF project is linked in the README (`osf.io/admrq`); its contents were not inspected. See [`standards-matrix.md`](standards-matrix.md), rows S-03 and S-19.
