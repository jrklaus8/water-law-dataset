# Dissertation Agent

An agentified version of Klaus Junior (2023), *Direito, Saneamento e Sustentabilidade:
Uma Análise Comparativa entre Municípios do Estado de Santa Catarina, Brasil, e da
Província de Ontário, Canadá à Luz dos Objetivos do Desenvolvimento Sustentável 6 e 11*
(UNIARP master's thesis), built with [Paper2Agent](https://github.com/jmiao24/Paper2Agent)'s
methodology.

The thesis is a doctrinal/comparative-law study with no accompanying code repository, so
this uses Paper2Agent's **Paper2Skill** route (a reviewed, searchable paper package)
rather than Paper2MCP (which wraps a paper's own code as executable tools). An MCP server
is layered on top of the resulting package so any MCP client can query it directly instead
of reading the package files by hand.

## Layout

- `direito-saneamento-sustentabilidade-paper/`: the built Paper2Skill package,
  `SKILL.md`, `references/{index.md,paper.md,supplement.md}`, and
  `assets/{figure,supp_figs,table,supp_table}/`. All 205 pages were reviewed page-by-page
  against the source PDF; every numeric/text discrepancy flagged by the build's automated
  verification was individually checked against the visible source and adjudicated (see
  Limitations below). Final verification status: `reviewed_with_limitations`.
- `mcp/server.py`: a `FastMCP` server exposing the package as resources and tools.
- `mcp/test_server.py`: a smoke test that exercises the server against the built package.

## Running the server

Requires [`uv`](https://docs.astral.sh/uv/). The script is self-contained (PEP 723); `uv`
resolves its `mcp[cli]` dependency automatically.

```bash
cd dissertation_agent/mcp
uv run server.py
```

This starts the server on stdio, ready to be launched by an MCP client.

## Connecting to Claude Code

Add it as a project or user MCP server:

```bash
claude mcp add dissertation-thesis -- uv run /absolute/path/to/dissertation_agent/mcp/server.py
```

Or add it manually to `.mcp.json`:

```json
{
  "mcpServers": {
    "dissertation-thesis": {
      "command": "uv",
      "args": ["run", "/absolute/path/to/dissertation_agent/mcp/server.py"]
    }
  }
}
```

Restart Claude Code (or run `/mcp` to reconnect) and the tools below become available.

## Connecting to another MCP client

Any client that speaks the Model Context Protocol over stdio can launch the same command:
`uv run /absolute/path/to/dissertation_agent/mcp/server.py`. Point the client's server
config at that command exactly as shown above for Claude Code.

## What the server exposes

Resources:
- `thesis://full-text`: the complete reviewed thesis, Markdown formatted (Portuguese).
- `thesis://citation`: citation metadata (author, title, institution, recommended citation).

Tools:
- `list_sections()`: every heading in document order; call this first to see the thesis's
  structure (introduction, ODS 6/11 framework, Santa Catarina and Ontario case studies,
  intervention proposal, etc.).
- `get_section(heading)`: full text of one section, matched by heading (case-insensitive,
  partial match allowed).
- `search_thesis(query, max_results=8)`: keyword/substring search across sections, with a
  short snippet per hit.
- `list_tables()`: every extracted data table (municipal sanitation statistics, funding
  figures, SDG indicators), with column headers.
- `get_table(asset_name)`: full rows of one table by its asset name (e.g. `table-5`).
- `list_currency_notes(status=None)`: dated checks of whether a thesis claim, citation,
  statute, or figure still reflects reality as of the check date, separate from the
  original 2023 text. Filter by `status` ("superseded", "resolved", "still_current",
  "needs_further_check"). See [`currency-notes.json`](currency-notes.json) and "Currency
  notes" below.
- `list_uncheckable_claims()`: claims flagged as worth a currency check but not yet
  verified.

Example prompts once connected: "List the sections of the dissertation," "What does the
thesis say about OCWA?," "Show me table 9," "Search the thesis for Kashechewan," "What in
this thesis is now out of date?"

## Currency notes

Paper2Skill's own verification only checks that the digitized text matches the source
PDF; it says nothing about whether the PDF's claims still hold. `currency-notes.json` is a
separate, dated annotation layer for that second question, checking specific statutes,
court rulings, agency names, and statistics against their current status, the same idea as
a citator flagging whether a cited case is still good law, applied to the thesis's own
citations and figures.

As of the 2026-09-17 check: 16 claims were verified (11 superseded, 3 still current, 1
resolved before the thesis was even defended, 1 needing a live-data recheck), and 7 more
are flagged as worth checking but not yet verified. Nothing in the original thesis text
was changed; see each entry for its source and reasoning.

## Limitations

- The thesis is in Portuguese; `search_thesis` is substring/keyword matching, not semantic
  search, so try a few phrasings (Portuguese and English) if a query comes back empty.
- Page 5 (the signed defense-certificate page) is image-only; OCR failed on it, so it is
  preserved as a full-page image with a manually written descriptive caption rather than a
  verified transcription.
- Table and CSV cell values preserve the source's own Brazilian number formatting (period
  as thousands separator, comma as decimal separator), matching what is printed in the PDF.
- The build's automated numeric cross-check flagged 53 diagnostics across 29 pages during
  review. All were individually checked against the source PDF and adjudicated; nearly all
  were parser tokenization artifacts (footnote-superscript numbers glued to adjacent digits
  in the PDF's native text layer, table cells split across text runs, or URLs/DOIs that
  wrap across PDF lines at a hyphen or percent-encoding boundary). One genuine transcription
  error was found and fixed in the process: a dropped hyphen in a SciELO article identifier
  on page 199, corrected to match the source exactly. Every adjudication's reasoning is
  recorded in [`review-adjudications.json`](review-adjudications.json) for full
  traceability, keyed by page, check, and a content fingerprint bound to the exact
  diagnostic it resolves.
