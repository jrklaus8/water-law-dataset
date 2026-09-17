# Direito, Saneamento e Sustentabilidade, Agentified

This folder takes a 2023 master's thesis and makes it queryable by AI agents, using
[Paper2Agent](https://github.com/jmiao24/Paper2Agent)'s methodology. It is not a new
argument or a revision of the original work. It is the same thesis, made interactive.

## What this is

**Direito, Saneamento e Sustentabilidade: Uma Análise Comparativa entre Municípios do
Estado de Santa Catarina, Brasil, e da Província de Ontário, Canadá à Luz dos Objetivos do
Desenvolvimento Sustentável 6 e 11** ("Law, Sanitation and Sustainability: a Comparative
Analysis Between Municipalities in the State of Santa Catarina, Brazil and the Province of
Ontario, Canada in the Light of Sustainable Development Goals 6 and 11") was my Master of
Development and Society thesis at Universidade Alto Vale do Rio do Peixe (UNIARP), defended
14 August 2023 under Dr. Levi Hülse, and hosted by the University of the Pacific's
McGeorge School of Law Dissertations series.

| | |
|---|---|
| Author | Claudio Antonio Klaus Junior, Universidade Alto Vale do Rio do Peixe |
| Date of Award | 8-14-2023 |
| Document Type | Thesis |
| First Advisor | Levi Hülse |
| Degree Name | Master of Development and Society |
| Department | Department of Graduate Studies in Development and Society |
| Source | [scholarlycommons.pacific.edu/mcgeorge-dissertations/3](https://scholarlycommons.pacific.edu/mcgeorge-dissertations/3) |

**Recommended citation:** Klaus, Claudio Antonio Junior, "Direito, Saneamento e
Sustentabilidade: Uma Análise Comparativa entre Municípios do Estado de Santa Catarina,
Brasil, e da Província de Ontário, Canadá à Luz dos Objetivos do Desenvolvimento
Sustentável 6 e 11" (2023). University of the Pacific, McGeorge School of Law
Dissertations. 3.

**Abstract:** The relevance of sanitation and sustainability is manifested in the
promotion of public health, improvement of quality of life, and ensuring access to basic
services as essential human rights. The comparative analysis between the cities of
Caçador, Videira, and Concórdia, in Santa Catarina, Brasil, and Sault Ste. Marie, Thunder
Bay, North Bay, Chatham-Kent, Woodstock, and Kenora, in Ontário, Canadá, allows for the
identification of differences and similarities in sanitation systems, understanding of
challenges and opportunities, and consequently, the foundation for effective public
policies aimed at improving access to sanitation. The present study analyzes the situation
of Brazilian municipalities concerning Sustainable Development Goals (SDGs) 6 and 11 in
comparison with Canadian municipalities, using a qualitative and descriptive methodology
grounded in literature review, legal documents, and quantitative data on potable water and
sewage disposal.

## AI assistance disclosure

The thesis text, argument, case studies, and citations in this folder are unchanged from
the version I defended on 14 August 2023. Nothing in that scholarly record was reworded,
reinterpreted, or extended by AI.

What AI did produce, starting September 2026, is everything else in this folder, built by
[Claude Code](https://claude.com/claude-code) (Anthropic) under my direction, across two
distinct kinds of work with two different levels of reliability. I'd rather over-explain
this than have anyone assume more rigor than actually happened.

**1. The digitization (high confidence).** Claude Code ran the Paper2Agent methodology to
convert the PDF into this package: extracting it page by page, reviewing all 205 pages
against the source for reading order, headings, and transcription accuracy, then running
the build's automated numeric cross-check and individually verifying and resolving every
discrepancy it flagged, recorded in [`review-adjudications.json`](review-adjudications.json)
with the reasoning for each one. This is a mechanical, checkable claim: does the digitized
text match what is printed in the PDF. One genuine transcription error (a dropped hyphen
in a citation identifier) was found and corrected this way. It also wrote the MCP server
code in `mcp/` and this documentation.

**2. The currency check (lower confidence, and said so on purpose).** Separately,
[`currency-notes.json`](currency-notes.json) checks whether specific claims, statutes, and
figures in the *thesis itself* still hold, a different and much less mechanical question.
This layer was built by Claude Code running web searches and querying a third-party legal
database (Legal Data Hunter), i.e. AI-conducted secondary-source research, not primary
legal research and not equivalent to a professional citator service (Shepard's, KeyCite,
or a lawyer actually pulling the statute). Every entry names its source and the date it
was checked so it can be independently re-verified, and that is exactly what happened with
the most significant single finding in the file: a real citation error (Lei nº 17.717/2019
misattributed as Santa Catarina's sanitation policy law) was caught by me checking the
state legislature's own portal directly, not by the AI on its own. The AI corroborated it
afterward and found the correct citation. Treat every "checked via web search" entry as a
lead worth five minutes of your own verification before you rely on it for anything that
matters, not as settled fact.

The full commit history is public, and the session that did each piece of work is linked
from the commit trailers if you want to see exactly what was generated, by which method,
and when.

## Why agentify a law thesis

Paper2Agent was built for papers with a code repository: genomics tools, single-cell
pipelines, statistical packages. A doctrinal comparative-law thesis has no code to run, so
there is nothing to wrap as an executable tool. What it does have is 205 pages of
structured legal argument, case studies, and statistical tables that are genuinely useful
to someone researching the same comparison, if they can find the right paragraph.

So this uses Paper2Agent's other path, **Paper2Skill**: instead of executable tools, the
thesis becomes a reviewed, page-verified knowledge package (full text, tables, figures,
citation metadata) that an AI agent can search, quote, and cite precisely, section by
section, table by table. On top of that package sits a small MCP server, so any MCP client
(Claude Code included) can query the thesis directly instead of a person opening the PDF
and Ctrl-F-ing through it.

The point worth sitting with: legal scholarship almost never gets this treatment. Code
papers have GitHub, requirements.txt, and now agent frameworks built around them. A law
thesis gets a PDF on a repository and, if it is lucky, a citation count. There is no
structural reason a comparative-law dissertation could not be exposed the same way a
genomics tool is, searchable, queryable, citable at the paragraph level. This is a small
proof of that.

## The connection to my current research

This thesis is where the comparative method I still use started: Brazil against Ontario,
on sanitation, under the SDG 6/11 framework. The dataset this folder lives inside (see the
[repository root README](../README.md)) extends that same design into "The Legal Last
Mile," a Most Different Systems Design comparison across Brazil, Canada, and the
Netherlands, now with 83,596 judicial decisions behind it. That research is the empirical
core of the PhD in sanitation law I am currently applying for, comparing the same three
jurisdictions.

Agentifying the 2023 thesis is not a detour from that work. It is a way of testing, on my
own earlier scholarship, a question the PhD proposal has to answer anyway: how do you make
comparative legal research usable by someone other than the person who wrote it, and by
systems, not just readers. An agentified dissertation is a small, concrete answer.

## What is in this folder

- [`direito-saneamento-sustentabilidade-paper/`](direito-saneamento-sustentabilidade-paper/): the built Paper2Skill package, full text, tables, and figures, reviewed page by page against the source PDF.
- [`mcp/server.py`](mcp/server.py): the MCP server exposing the package as searchable tools and resources.
- [`review-adjudications.json`](review-adjudications.json): the record of every discrepancy the automated verification flagged during conversion, and how each was checked and resolved.
- [`currency-notes.json`](currency-notes.json): a separate, dated layer checking whether specific claims, citations, and figures in the thesis still hold, not whether the digitization is accurate (that is what `review-adjudications.json` is for).
- [`USAGE.md`](USAGE.md): how to run the server and connect it to Claude Code or another MCP client.

## Limitations, stated plainly

One page (the signed defense certificate) is a scanned image with no machine-readable
text; it is preserved as an image with a descriptive caption rather than a transcription.
Table figures keep the source's own Brazilian number formatting. Everything else is
verified against the source PDF; see `USAGE.md` for the full account, including the one
real transcription error found and corrected during review.

## Is this still accurate today

A 2023 legal thesis making empirical claims does not stay accurate forever, and pretending
otherwise would be dishonest. [`currency-notes.json`](currency-notes.json) checks specific
statutes, a constitutional challenge, agency names, and population/investment figures
against their current status, without rewriting the original argument. As of the last
check: the STF had already resolved the constitutional question the thesis frames as
pending before the thesis was even defended; two of the regulatory decrees it cites as
current were repealed weeks before the defense; the national data source behind most of
its tables (SNIS) has been discontinued and replaced; one citation is confirmed wrong (a
law numbered as the source of Santa Catarina's sanitation policy is actually an unrelated
fire-safety-council amendment, verified directly against the state's own legislation
portal); and all three Brazilian case-study cities have since restructured their water and
sewage services in three different ways (two into private concessions, one into a new
municipal authority) with real coverage numbers now far more specific, and in places far
starker, than the 2000/2010 data the thesis had to work with. See `USAGE.md` for the full
breakdown.
