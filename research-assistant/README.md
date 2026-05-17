# Legal Last Mile Research Assistant

A natural-language research assistant for water law, built on 83,596 court decisions from Brazil, the Netherlands, and Canada — coded under the **Legal Last Mile** theoretical framework.

Built for the **WashU Law International Vibe Coding Challenge** (June 2026).

> **AI Disclosure** — This tool uses Claude (Anthropic) to analyse a curated legal dataset. Responses reflect dataset patterns, not comprehensive legal research. It is not legal advice.

## What It Does

Ask plain-language research questions and get evidence-grounded answers about:

- How water law disputes are classified and resolved across jurisdictions
- The Legal Last Mile theory — administrative law as gatekeeper between physical water access and enforceable legal entitlement
- Outcome patterns by country, governance category, and legal framing
- Human rights language in water litigation
- Comparative patterns (Brazil vs. Netherlands vs. Canada)

## The Dataset

**Global Water Law Dataset** — 83,596 court decisions, 1997–2026

| Country | Cases | Top Category |
|---|---|---|
| Brazil | 11,724 | Tariff disputes (48.52%) |
| Netherlands | 68,654 | Flood protection & waterboard governance |
| Canada | 3,218 | Fisheries & riparian disputes |

Dataset: [github.com/jrklaus8/water-law-dataset](https://github.com/jrklaus8/water-law-dataset)  
DOI: [10.5281/zenodo.19836413](https://doi.org/10.5281/zenodo.19836413)

## The Legal Last Mile Theory

The Legal Last Mile (Claudio Klaus) holds that administrative law acts as a gatekeeper between physical water infrastructure and enforceable legal entitlement. Even when pipes exist, residents can be excluded by tariff disputes, connection refusals, lack of formal address, or permit denials. The theory identifies an "Administrative Ghost" — households physically adjacent to water infrastructure but legally invisible to it.

The dataset was built to test this theory across three jurisdictions with different administrative law traditions.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your Anthropic API key to .env
streamlit run app.py
```

## Example Questions

- "Why does Brazil have so many tariff disputes compared to the Netherlands?"
- "What happens to residents of informal settlements who seek water connections in Brazil?"
- "How do Dutch courts handle connection refusal cases differently from Brazilian courts?"
- "Does using human rights language in water disputes improve outcomes for users?"
- "What does the data reveal about the Legal Last Mile theory across all three countries?"

## Credits

- **Claudio Klaus** — Legal Last Mile theory and Global Water Law Dataset
- **Claude (Anthropic)** — AI research analysis engine

## License

AGPL-3.0
