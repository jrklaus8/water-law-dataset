"""
TJSC (Tribunal de Justiça de Santa Catarina) water law case scraper.
Searches https://busca.tjsc.jus.br/jurisprudencia/ year-by-year 2016-2026.

Usage:
    python -m scrapers.brazil.tjsc_scraper --dry-run --years 2024 2024
    python scrapers/brazil/tjsc_scraper.py            # full run, writes $OUTPUT_DIR/tjsc_cases_2016_2026.json
"""
import argparse
import logging
import os
import re
import sys
import urllib.parse
from typing import Dict, List, Mapping, Optional, Sequence

if __package__ in (None, ""):  # run as a plain script: make `scrapers` importable
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from scrapers.base import BaseScraper, FetchError, LayoutChangeError, ScraperError, preview  # noqa: E402

BASE = 'https://busca.tjsc.jus.br/jurisprudencia/'
AJAX = BASE + 'buscaajax.do?categoria=acordaos'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9',
    'Referer': BASE,
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
}

RESULT_SECTION = re.compile(r'###inicio_resultado###(.+?)###fim_resultado###', re.DOTALL)


def default_output() -> str:
    return os.path.join(os.getenv('OUTPUT_DIR', '.'), 'tjsc_cases_2016_2026.json')


def parse_blocks(html: str, tag: str) -> List[Dict[str, str]]:
    """Parse every result block that carries a process number into a raw record (no validation)."""
    records = []
    for block in re.split(r'<div class="resultados">', html)[1:]:
        m_num = re.search(r"openLinkAcompanhamento\('[^']+','([0-9\-\.]+)'\)", block)
        if not m_num:
            continue

        clean = re.sub(r'<[^>]+>', ' ', block)
        clean = re.sub(r'\s+', ' ', clean).strip()

        relator = (re.search(r'Relator:\s*([^\n<]+?)(?:\s*<|\s*Origem:)', block, re.IGNORECASE) or
                   re.search(r'Relator.*?</strong>\s*([^<\n]+)', block, re.IGNORECASE))
        relator = relator.group(1).strip() if relator else ''

        orgao = re.search(r'Org[^:]+:\s*</strong>\s*([^<\n]+)', block, re.IGNORECASE)
        orgao = orgao.group(1).strip() if orgao else ''

        julgado = re.search(r'Julgado em:\s*</strong>\s*(\d{2}/\d{2}/\d{4})', block, re.IGNORECASE)
        julgado = julgado.group(1).strip() if julgado else ''

        classe = re.search(r'Classe:\s*</strong>\s*([^<\n]+)', block, re.IGNORECASE)
        classe = classe.group(1).strip() if classe else ''

        # Ementa from textarea (most complete), else a plain-text excerpt
        ementa = re.search(r'<textarea[^>]*>([^<]{10,})</textarea>', block, re.DOTALL | re.IGNORECASE)
        em_text = ementa.group(1).strip()[:800] if ementa else clean[:500]

        if not relator:
            m_r = re.search(r'Relator:\s+([A-ZÀ-Ü][a-zà-ü\s]+?)(?=\s+Origem:|\s+Org)', clean)
            relator = m_r.group(1).strip() if m_r else ''

        if not orgao:
            m_o = re.search(r'Org[ãa]o Julgador:\s+([^\n]+?)(?=\s+Julgado|\s+Classe)', clean)
            orgao = m_o.group(1).strip() if m_o else ''

        records.append({
            'num': m_num.group(1),
            'processDate': julgado,
            'publicDate': '',
            'classe': classe,
            'relator': relator,
            'camara': orgao,
            'comarca': '',
            'ementa': em_text,
            'tag': tag,
            'court': 'TJSC',
            'state': 'SC',
        })
    return records


def extract_cases(html: str, tag: str, scraper: Optional[BaseScraper] = None) -> List[Dict[str, str]]:
    """Parse, validate against the case schema and deduplicate one result section.

    Pass a scraper to have rejections, warnings and duplicates counted in its report.
    """
    scraper = scraper or TJSCScraper(output_path=None)
    valid = [r for r in parse_blocks(html, tag) if scraper.accept(r)]
    return scraper.dedupe(valid)


def parse_totals(html: str):
    """Return (total_results, total_pages) from a search response; (0, 1) if absent."""
    # Count may use '.' as thousands separator: "<b>2.251</b> resultados"
    total_m = re.search(r'<b>([\d\.]+)</b>\s*resultados', html)
    total = int(total_m.group(1).replace('.', '')) if total_m else 0
    # "Página X de Y": the accented char may be mangled by encoding, hence the dot
    pages_m = re.search(r'P.gina\s+\d+\s+de\s+(\d+)', html)
    pages = int(pages_m.group(1)) if pages_m else 1
    return total, pages


class TJSCScraper(BaseScraper):
    court = 'TJSC'
    encoding = 'iso-8859-1'

    def __init__(self, output_path: Optional[str] = None, page_delay: float = 2.0, year_delay: float = 5.0,
                 **kwargs):
        super().__init__(BASE, output_path=output_path, headers=HEADERS, **kwargs)
        self.page_delay = page_delay
        self.year_delay = year_delay

    def _page_cases(self, html: str, tag: str) -> List[Dict[str, str]]:
        section = RESULT_SECTION.search(html)
        return extract_cases(section.group(1), tag, self) if section else []

    def search_year(self, year: int, query: str, max_pages: int = 20) -> List[Dict[str, str]]:
        d1, d2, tag = '01/01/%d' % year, '31/12/%d' % year, '%d-sc' % year

        post = urllib.parse.urlencode([
            ('q', ''), ('frase', query), ('qualquer', ''), ('excluir', ''),
            ('prox1', ''), ('prox2', ''), ('proxc', ''),
            ('busca', 'avancada'), ('radio_campo', 'ementa'),
            ('datainicial', d1), ('datafinal', d2),
            ('resultado', '2'),
        ]).encode('utf-8')
        html = self.fetch(AJAX, data=post)

        total, total_pages = parse_totals(html)
        self.log.info('%d: %d results, %d pages', year, total, total_pages)

        cases = self._page_cases(html, tag)
        if total > 0 and not cases:
            # The portal says there are results but nothing parsed: do not silently save an empty year.
            raise LayoutChangeError('%d: portal reports %d results but 0 were parsed (markup changed?)'
                                    % (year, total))

        for pg in range(2, min(total_pages, max_pages) + 1):
            if len(cases) >= total:
                break
            self._sleep(self.page_delay)
            params = urllib.parse.urlencode([
                ('q', ''), ('only_ementa', ''), ('frase', query), ('excluir', ''),
                ('qualquer', ''), ('prox1', ''), ('prox2', ''), ('proxc', ''),
                ('sort', 'dtJulgamento desc'), ('ps', '20'),
                ('busca', 'avancada'), ('pg', str(pg)),
                ('categoria', 'acordaos'), ('flapto', '1'),
                ('datainicial', d1), ('datafinal', d2),
                ('radio_campo', 'ementa'),
            ])
            try:
                page_html = self.fetch(BASE + 'buscaajax.do?' + params)
            except FetchError as exc:
                self.report.failed_units.append('%d page %d: %s' % (year, pg, exc))
                continue
            new = self._page_cases(page_html, tag)
            if not new and not RESULT_SECTION.search(page_html):
                self.report.failed_units.append('%d page %d: no result section' % (year, pg))
            cases = self.dedupe(cases + new)
            self.log.info('  page %d: %d cases so far', pg, len(cases))
        return cases

    def run(self, years: Sequence[int], query: str = 'CASAN', max_pages: int = 20) -> List[Mapping]:
        self.check_output_dir()
        self.warm_up()
        all_cases: List[Mapping] = []

        for i, year in enumerate(years):
            try:
                cases = self.search_year(year, query, max_pages)
            except ScraperError as exc:
                self.report.failed_units.append('%d: %s' % (year, exc))
                self.log.error('year %d failed: %s', year, exc)
                cases = []
            all_cases = self.dedupe(all_cases + cases)
            self.save(all_cases)  # incremental: a crash in a later year keeps earlier years
            if i < len(years) - 1:
                self._sleep(self.year_delay)

        self.report.kept = len(all_cases)
        return all_cases


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Scrape TJSC water law decisions (ementa phrase search).')
    p.add_argument('--query', default='CASAN', help='exact phrase searched in the ementa (default: CASAN)')
    p.add_argument('--start-year', type=int, default=2016)
    p.add_argument('--end-year', type=int, default=2026)
    p.add_argument('--max-pages', type=int, default=20)
    p.add_argument('--output', default=default_output(), help='JSON output path')
    p.add_argument('--dry-run', action='store_true', help='fetch and parse, print a preview, write nothing')
    p.add_argument('--verbose', '-v', action='store_true')
    return p


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format='%(asctime)s %(levelname)s %(name)s: %(message)s')
    if args.start_year > args.end_year:
        build_parser().error('--start-year must be <= --end-year')

    scraper = TJSCScraper(output_path=args.output, dry_run=args.dry_run)
    try:
        cases = scraper.run(range(args.start_year, args.end_year + 1), args.query, args.max_pages)
    except ScraperError as exc:  # e.g. unusable output directory: nothing was scraped
        print('ERROR: %s' % exc, file=sys.stderr)
        return 2

    print('\n=== TJSC: %d unique cases ===' % len(cases))
    print(scraper.report.summary())
    if args.dry_run:
        print('\n[dry-run] nothing written; would save to %s\nPreview:\n%s' % (args.output, preview(cases)))
    else:
        print('Saved to: %s' % args.output)
    return 0 if scraper.report.ok else 1


if __name__ == '__main__':
    sys.exit(main())
