#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["mcp[cli]>=1.2.0,<2"]
# ///
"""MCP server exposing Klaus Junior (2023) "Direito, Saneamento e Sustentabilidade"
(UNIARP master's thesis) as agent-readable resources and retrieval tools.

This is a *resource-layer* paper agent in the Paper2Agent sense: the source thesis
is a doctrinal/comparative-law study with no accompanying code repository, so there
is no scientific computation to wrap as executable tools. Instead, this server
exposes the reviewed paper package (built by the Paper2Skill workflow from
skills/paper2agent/paper2skill) as searchable resources: full text by section,
extracted data tables, and citation metadata.

Run directly with `uv run server.py` (stdio transport) or import `mcp` and mount it
in another server. See ../USAGE.md for how to connect this to Claude Code or another
MCP client.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

from mcp.server.fastmcp import FastMCP

SKILL_DIR = Path(__file__).resolve().parent.parent / "direito-saneamento-sustentabilidade-paper"
REFERENCES_DIR = SKILL_DIR / "references"
ASSETS_DIR = SKILL_DIR / "assets"
PAPER_MD = REFERENCES_DIR / "paper.md"
CURRENCY_NOTES_PATH = Path(__file__).resolve().parent.parent / "currency-notes.json"

CITATION = {
    "author": "Cláudio Antônio Klaus Júnior",
    "title": (
        "Direito, Saneamento e Sustentabilidade: Uma Análise Comparativa entre "
        "Municípios do Estado de Santa Catarina, Brasil, e da Província de Ontário, "
        "Canadá à Luz dos Objetivos do Desenvolvimento Sustentável 6 e 11"
    ),
    "title_en": (
        "Law, Sanitation and Sustainability: a Comparative Analysis Between "
        "Municipalities in the State of Santa Catarina, Brazil and the Province of "
        "Ontario, Canada in the Light of Sustainable Development Goals 6 and 11"
    ),
    "degree": "Master of Development and Society (Mestrado em Desenvolvimento e Sociedade)",
    "institution": "Universidade Alto Vale do Rio do Peixe (UNIARP)",
    "advisor": "Dr. Levi Hülse",
    "year": 2023,
    "date_awarded": "2023-08-14",
    "source_url": "https://scholarlycommons.pacific.edu/mcgeorge-dissertations/3",
    "citation": (
        'Klaus, Claudio Antonio Junior, "Direito, Saneamento e Sustentabilidade: Uma '
        "Análise Comparativa entre Municípios do Estado de Santa Catarina, Brasil, e "
        "da Província de Ontário, Canadá à Luz dos Objetivos do Desenvolvimento "
        'Sustentável 6 e 11" (2023). University of the Pacific, McGeorge School of Law '
        "Dissertations. 3."
    ),
}

mcp = FastMCP("direito-saneamento-sustentabilidade-thesis")


def _read_paper_text() -> str:
    if not PAPER_MD.exists():
        raise FileNotFoundError(
            f"{PAPER_MD} not found. Build the paper skill first "
            "(see skills/paper2agent/paper2skill) before running this server."
        )
    return PAPER_MD.read_text(encoding="utf-8")


_HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$", re.MULTILINE)


def _split_sections(text: str) -> list[dict]:
    """Split paper.md into sections by markdown heading, keeping heading + body."""
    matches = list(_HEADING_RE.finditer(text))
    sections = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        level = len(m.group(1))
        heading = m.group(2).strip()
        body = text[start:end]
        sections.append({"level": level, "heading": heading, "text": body})
    if not sections:
        sections = [{"level": 0, "heading": "(full document)", "text": text}]
    return sections


@mcp.resource("thesis://full-text")
def full_text() -> str:
    """The complete reviewed thesis text (Portuguese), Markdown formatted."""
    return _read_paper_text()


@mcp.resource("thesis://citation")
def citation() -> dict:
    """Citation metadata for the thesis (author, title, institution, recommended citation)."""
    return CITATION


@mcp.tool()
def list_sections() -> list[str]:
    """List every section/subsection heading in the thesis, in document order.

    Use this first to discover the thesis structure (chapters, ODS 6/11 discussion,
    municipal case studies, methodology, findings, intervention proposal, etc.)
    before calling get_section().
    """
    text = _read_paper_text()
    return [s["heading"] for s in _split_sections(text) if s["heading"] != "(full document)"]


@mcp.tool()
def get_section(heading: str) -> str:
    """Return the full text of one thesis section, matched by heading (case-insensitive substring).

    Args:
        heading: A heading or partial heading, e.g. "ODS 6", "Caçador", "Proposta de Intervenção",
            "considerações finais". Use list_sections() to see exact headings first.

    Returns the matched section's full Markdown text, or an error message listing close
    candidates if nothing matched.
    """
    text = _read_paper_text()
    sections = _split_sections(text)
    needle = heading.strip().lower()
    exact = [s for s in sections if s["heading"].lower() == needle]
    if exact:
        return exact[0]["text"]
    partial = [s for s in sections if needle in s["heading"].lower()]
    if partial:
        if len(partial) == 1:
            return partial[0]["text"]
        headings = "\n".join(f"- {s['heading']}" for s in partial)
        return f"Multiple sections matched '{heading}'. Be more specific:\n{headings}"
    return f"No section matched '{heading}'. Call list_sections() to see available headings."


@mcp.tool()
def search_thesis(query: str, max_results: int = 8) -> list[dict]:
    """Full-text search across the thesis. Returns matching sections with a short snippet.

    Args:
        query: Portuguese or English keyword(s)/phrase, e.g. "OCWA", "Equalização Fiscal",
            "connection refusal", "privatização", "Kashechewan".
        max_results: maximum number of matching sections to return (default 8).

    This is substring/keyword search over section bodies, not semantic search — try a few
    phrasings if you don't find what you expect.
    """
    text = _read_paper_text()
    sections = _split_sections(text)
    needle = query.strip().lower()
    if not needle:
        return []
    results = []
    for s in sections:
        body_lower = s["text"].lower()
        idx = body_lower.find(needle)
        if idx == -1:
            continue
        start = max(0, idx - 200)
        end = min(len(s["text"]), idx + len(query) + 200)
        snippet = s["text"][start:end].strip()
        results.append({"heading": s["heading"], "snippet": snippet})
        if len(results) >= max_results:
            break
    return results


def _table_dirs() -> list[Path]:
    return [ASSETS_DIR / "table", ASSETS_DIR / "supp_table"]


@mcp.tool()
def list_tables() -> list[dict]:
    """List every extracted data table available from the thesis (municipal sanitation
    statistics, SDG indicators, investment figures, etc.), with its asset name and column headers.
    """
    out = []
    for d in _table_dirs():
        if not d.exists():
            continue
        for csv_path in sorted(d.glob("*.csv")):
            try:
                with csv_path.open(encoding="utf-8", newline="") as f:
                    reader = csv.reader(f)
                    header = next(reader, [])
            except Exception as exc:  # pragma: no cover - defensive
                out.append({"asset_name": csv_path.stem, "error": str(exc)})
                continue
            out.append({"asset_name": csv_path.stem, "columns": header, "category": d.name})
    return out


@mcp.tool()
def get_table(asset_name: str) -> dict:
    """Return the full rows of one extracted data table by its asset name (see list_tables()).

    Args:
        asset_name: e.g. "table-5", "table-9" (from list_tables()).
    """
    for d in _table_dirs():
        csv_path = d / f"{asset_name}.csv"
        if csv_path.exists():
            with csv_path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.reader(f))
            return {"asset_name": asset_name, "rows": rows}
    available = [t["asset_name"] for t in list_tables()]
    return {"error": f"No table named '{asset_name}'.", "available": available}


def _load_currency_notes() -> dict:
    if not CURRENCY_NOTES_PATH.exists():
        return {"entries": [], "not_yet_checked": []}
    return json.loads(CURRENCY_NOTES_PATH.read_text(encoding="utf-8"))


@mcp.tool()
def list_currency_notes(status: str | None = None) -> list[dict]:
    """List currency notes: dated checks of whether a thesis claim, citation, or figure
    still reflects reality, separate from the original 2023 text.

    This is not part of Paper2Skill's own verification (which only checks that the
    digitized text matches the source PDF). It is a distinct annotation layer added
    afterward, checking whether the *content* is still current, similar in spirit to a
    citator flagging whether a cited authority is still good law.

    Args:
        status: optional filter, one of "superseded", "resolved", "still_current",
            "needs_further_check". Omit to return all checked entries.

    Returns entries with a page reference, what the thesis claims, its current status,
    and the source used to check it. Call list_uncheckable_claims() for claims flagged
    as worth checking but not yet verified.
    """
    notes = _load_currency_notes()
    entries = notes.get("entries", [])
    if status:
        entries = [e for e in entries if e.get("status") == status]
    return entries


@mcp.tool()
def list_uncheckable_claims() -> list[dict]:
    """List thesis claims flagged as checkable for currency but not yet verified.

    Use this to see what still needs a currency check, as opposed to
    list_currency_notes() which returns claims already checked.
    """
    return _load_currency_notes().get("not_yet_checked", [])


if __name__ == "__main__":
    mcp.run()
