# Legal Last Mile Research Assistant
## WashU Law International Vibe Coding Challenge — Submission

**Author**: Claudio Klaus  
**Tool**: Legal Last Mile Research Assistant  
**Repository**: https://github.com/jrklaus8/water-law-dataset/tree/main/research-assistant  
**Dataset DOI**: https://doi.org/10.5281/zenodo.19836413

---

## What the Tool Does

The Legal Last Mile Research Assistant is a natural-language research tool for water law, built on 83,596 court decisions from Brazil, the Netherlands, and Canada. Researchers ask plain-English questions and receive evidence-grounded answers drawn directly from the dataset — with citations, case links, and cross-jurisdictional comparisons.

The tool is built around the **Legal Last Mile theory**: the argument that administrative law acts as a gatekeeper between physical water infrastructure and enforceable legal entitlement. Even when pipes exist, residents can be excluded by tariff disputes, connection refusals, lack of formal address, or permit denials. The theory identifies an "Administrative Ghost" — households physically adjacent to water infrastructure but legally invisible to it. The dataset was built to test whether this pattern appears across jurisdictions with different administrative law traditions.

---

## The Problem It Solves

Comparative water law research is fragmented by language, jurisdiction, and the sheer volume of administrative decisions that never reach academic publication. A researcher wanting to compare how Brazilian state courts handle informal settlement cases against Dutch administrative tribunals would normally spend months gathering and translating decisions.

This tool makes that comparison instant. It loads 83,596 coded decisions, detects which jurisdictions are relevant to the research question, and routes the query through a multi-agent pipeline that analyses each jurisdiction separately before synthesising a cross-jurisdictional answer grounded in real case data.

---

## Technical Architecture

The tool uses a **three-stage multi-agent pipeline** built on the Anthropic Claude API:

1. **Country specialist agents** (one per detected jurisdiction, running on Claude Haiku) — each receives only its jurisdiction's statistics and cases, keeping context narrow and analysis focused.
2. **Legal Last Mile theory agent** (Claude Haiku) — reads the country summaries and identifies where the evidence supports or challenges the theory.
3. **Synthesis agent** (Claude Opus) — produces the final research answer from the compact agent outputs, not from raw data.

This architecture applies the principle that smaller, focused agent contexts produce higher-fidelity outputs than a single large prompt. Each agent has one job. The synthesis agent never sees the raw dataset — only the distilled analyses. An Analytics tab provides interactive charts of governance category distributions, year trends, outcome rates, and human rights language usage across all three jurisdictions.

---

## Why It Matters

Water access is a human right recognised by the UN General Assembly in 2010. Yet in Brazil alone, this dataset shows 10.88% of water law cases involve connection refusals — utilities or municipalities denying physical connection to the water network. Only 0.75% of cases involve informal settlements, and that category records zero user wins across 88 decisions — the quantitative signature of the Administrative Ghost. The Netherlands, by contrast, shows only 8 connection refusal cases out of 68,654 — suggesting that pre-litigation administrative mechanisms absorb disputes before they reach courts.

The Legal Last Mile Research Assistant makes these patterns accessible to researchers, advocates, and policymakers without requiring them to process 83,596 decisions in four languages. The dataset is open, the code is open, and every answer the tool produces shows the cases and statistics that generated it.

---

*Built with Claude Code (Anthropic). Dataset: Global Water Law Dataset (CC BY 4.0). Tool: AGPL-3.0.*
