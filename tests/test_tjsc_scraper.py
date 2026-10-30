import json
import urllib.parse
from pathlib import Path

import pytest

from scrapers.base import LayoutChangeError
from scrapers.brazil import tjsc_scraper
from scrapers.brazil.tjsc_scraper import AJAX, BASE, TJSCScraper, extract_cases, parse_blocks, parse_totals

FIXTURES = Path(__file__).parent / 'fixtures'


def fixture(name):
    return (FIXTURES / name).read_text(encoding='utf-8')


def make_scraper(**kwargs):
    kwargs.setdefault('sleep', lambda s: None)
    return TJSCScraper(**kwargs)


# --- parsing --------------------------------------------------------------

def test_parse_good_page_extracts_all_fields():
    scraper = make_scraper()
    cases = extract_cases(fixture('tjsc_page_good.html'), '2024-sc', scraper)
    assert [c['num'] for c in cases] == ['2016.012345-6', '2017.000777-1']
    first = cases[0]
    assert first['processDate'] == '01/02/2024'
    assert first['relator'] == 'João Silva'
    assert first['camara'] == '1ª Câmara de Direito Público'
    assert first['classe'] == 'Apelação Civel'
    assert first['ementa'].startswith('APELACAO CIVEL. CASAN')
    assert (first['court'], first['state'], first['tag']) == ('TJSC', 'SC', '2024-sc')
    assert scraper.report.duplicates == 1


def test_parse_totals():
    assert parse_totals(fixture('tjsc_page_good.html')) == (3, 1)
    assert parse_totals(fixture('tjsc_page_changed_layout.html')) == (41, 3)
    assert parse_totals('<b>2.251</b> resultados Página 1 de 113') == (2251, 113)
    assert parse_totals('nothing here') == (0, 1)


def test_partial_page_keeps_cases_with_empty_optional_fields_and_counts_warnings():
    scraper = make_scraper()
    cases = extract_cases(fixture('tjsc_page_partial.html'), '2020-sc', scraper)
    nums = [c['num'] for c in cases]
    assert '2020.000001-1' in nums
    # block without any ementa text still falls back to a plain-text excerpt, so it is kept too
    assert scraper.report.warnings['empty field: relator'] >= 1
    assert scraper.report.warnings['empty field: camara'] >= 1


def test_block_without_process_number_is_ignored():
    records = parse_blocks(fixture('tjsc_page_partial.html'), '2020-sc')
    assert all(r['num'] for r in records)
    assert len(records) == 2


def test_record_with_bad_date_is_rejected_and_counted():
    html = ('<div class="resultados"><a onclick="openLinkAcompanhamento(\'SC\',\'1.2\')"></a>'
            '<textarea>Ementa long enough</textarea></div>')
    scraper = make_scraper()
    monkey = parse_blocks(html, 't')
    monkey[0]['processDate'] = '2024-01-01'
    assert not scraper.accept(monkey[0])
    assert scraper.report.rejected['bad date in processDate'] == 1


# --- search flow (network stubbed) ---------------------------------------

class Stub:
    def __init__(self, scraper, pages):
        self.pages = pages  # url-substring -> html
        self.requested = []
        scraper.fetch = self

    def __call__(self, url, data=None, headers=None):
        self.requested.append((url, data))
        for key, html in self.pages.items():
            if key == 'POST' and data is not None:
                return html
            if key != 'POST' and key in url:
                return html
        raise AssertionError('unexpected request: %s' % url)


def test_search_year_posts_query_and_returns_cases():
    scraper = make_scraper()
    stub = Stub(scraper, {'POST': fixture('tjsc_page_good.html')})
    cases = scraper.search_year(2024, 'CASAN')
    assert [c['num'] for c in cases] == ['2016.012345-6', '2017.000777-1']
    url, data = stub.requested[0]
    assert url == AJAX
    sent = urllib.parse.parse_qs(data.decode())
    assert sent['frase'] == ['CASAN'] and sent['datainicial'] == ['01/01/2024']


def test_search_year_raises_when_layout_changed():
    scraper = make_scraper()
    Stub(scraper, {'POST': fixture('tjsc_page_changed_layout.html')})
    with pytest.raises(LayoutChangeError):
        scraper.search_year(2016, 'CASAN')


def test_search_year_paginates_and_records_failed_page():
    page1 = fixture('tjsc_page_good.html').replace('Página 1 de 1', 'Página 1 de 3').replace(
        '<b>3</b>', '<b>40</b>')
    scraper = make_scraper()

    def fetch(url, data=None, headers=None):
        if data is not None:
            return page1
        if 'pg=2' in url:
            from scrapers.base import FetchError
            raise FetchError('boom')
        return fixture('tjsc_page_partial.html')

    scraper.fetch = fetch
    cases = scraper.search_year(2024, 'CASAN')
    assert len(cases) == 4  # 2 from page 1, 2 from page 3 (page 2 failed)
    assert len(scraper.report.failed_units) == 1 and 'page 2' in scraper.report.failed_units[0]
    assert not scraper.report.ok


# --- run / output --------------------------------------------------------

def run_scraper(tmp_path, dry_run, pages=None):
    out = tmp_path / 'out' / 'tjsc.json'
    scraper = make_scraper(output_path=str(out), dry_run=dry_run)
    Stub(scraper, pages or {'POST': fixture('tjsc_page_good.html'), BASE: '<html></html>'})
    return scraper, out, scraper.run([2024], 'CASAN')


def test_run_writes_deduplicated_json(tmp_path):
    scraper, out, cases = run_scraper(tmp_path, dry_run=False)
    assert len(cases) == 2
    assert [c['num'] for c in json.loads(out.read_text(encoding='utf-8'))] == ['2016.012345-6', '2017.000777-1']
    assert scraper.report.ok


def test_run_dry_run_writes_nothing(tmp_path):
    scraper, out, cases = run_scraper(tmp_path, dry_run=True)
    assert len(cases) == 2
    assert not out.exists() and not out.parent.exists()


def test_run_reports_failed_year_instead_of_saving_silently(tmp_path):
    scraper, out, cases = run_scraper(
        tmp_path, dry_run=False,
        pages={'POST': fixture('tjsc_page_changed_layout.html'), BASE: '<html></html>'})
    assert cases == []
    assert not scraper.report.ok and 'markup changed' in scraper.report.failed_units[0]


def test_main_dry_run_exit_code_and_output(tmp_path, monkeypatch, capsys):
    out = tmp_path / 'never.json'

    def fake_fetch(self, url, data=None, headers=None):
        return fixture('tjsc_page_good.html') if data is not None else '<html></html>'

    monkeypatch.setattr(TJSCScraper, 'fetch', fake_fetch)
    monkeypatch.setattr(TJSCScraper, '_sleep', lambda self, s: None, raising=False)
    code = tjsc_scraper.main(['--start-year', '2024', '--end-year', '2024', '--output', str(out), '--dry-run'])
    printed = capsys.readouterr().out
    assert code == 0 and '2 unique cases' in printed and '[dry-run]' in printed
    assert not out.exists()
