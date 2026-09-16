#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Lightweight tests for the thesis MCP server's helper functions.

Run with: uv run test_server.py
Exits non-zero on failure so it can be used as a smoke test after building the
paper skill package (see ../../skills/paper2agent/paper2skill).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import server  # noqa: E402


def check(name: str, condition: bool, detail: str = "") -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail and not condition else ""))
    return condition


def main() -> int:
    failures = 0

    if not server.PAPER_MD.exists():
        print(f"SKIP: {server.PAPER_MD} does not exist yet — build the paper skill first.")
        return 1

    text = server._read_paper_text()
    failures += not check("paper.md is non-empty", len(text) > 1000)

    sections = server.list_sections()
    failures += not check("list_sections returns headings", len(sections) > 5, str(len(sections)))

    # Known content checks against the thesis (facts transcribed from the source PDF).
    intro = server.get_section("Introdução")
    failures += not check(
        "Introdução section found and mentions ODS 6/11",
        "ODS" in intro and ("Objetivo 6" in intro or "ODS 6" in intro),
    )

    resumo_hits = server.search_thesis("Objetivos de Desenvolvimento Sustentável", max_results=3)
    failures += not check("search_thesis finds ODS mentions", len(resumo_hits) > 0)

    cacador_hits = server.search_thesis("Caçador", max_results=5)
    failures += not check("search_thesis finds Caçador case study", len(cacador_hits) > 0)

    ontario_hits = server.search_thesis("Ontario", max_results=1) or server.search_thesis(
        "Ontário", max_results=1
    )
    failures += not check("search_thesis finds Ontario/Ontário", len(ontario_hits) > 0)

    tables = server.list_tables()
    failures += not check("list_tables returns at least one table", len(tables) >= 1, str(len(tables)))

    if tables:
        first = tables[0]["asset_name"]
        result = server.get_table(first)
        failures += not check(
            f"get_table('{first}') returns rows", "rows" in result and len(result["rows"]) > 0
        )

    cite = server.CITATION
    failures += not check(
        "citation metadata has author/title/year",
        bool(cite.get("author")) and bool(cite.get("title")) and cite.get("year") == 2023,
    )

    print(f"\n{'ALL PASS' if failures == 0 else f'{failures} FAILURE(S)'}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
