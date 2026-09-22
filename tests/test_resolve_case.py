"""Tests for the permalink resolver.

These check identifier normalisation and routing, not that the remote hosts are
up. Network reachability is a property of the courts, not of this code.
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'utils'))
from resolve_case import normalise_cnj, normalise_ecli, resolve  # noqa: E402


@pytest.mark.parametrize('raw,expected', [
    ('0001234-56.2022.8.26.0100', '0001234-56.2022.8.26.0100'),
    ('00012345620228260100', '0001234-56.2022.8.26.0100'),      # unpunctuated
    ('Processo 0001234-56.2022.8.26.0100 - Apelação', '0001234-56.2022.8.26.0100'),
    ('not a process number', None),
    ('', None),
    (None, None),
])
def test_cnj_normalisation(raw, expected):
    assert normalise_cnj(raw) == expected


@pytest.mark.parametrize('raw,expected', [
    ('ECLI:NL:RVS:2019:2481', 'ECLI:NL:RVS:2019:2481'),
    ('ecli:nl:rvs:2019:2481', 'ECLI:NL:RVS:2019:2481'),          # case-insensitive
    ('see ECLI:NL:RBAMS:2025:1111 at para 4', 'ECLI:NL:RBAMS:2025:1111'),
    ('ECLI:NL:HR:2020:1234.5', 'ECLI:NL:HR:2020:1234.5'),        # dotted suffix
    ('TJSP 123', None),
])
def test_ecli_normalisation(raw, expected):
    assert normalise_ecli(raw) == expected


def test_ecli_gets_permanent_resolver_and_fulltext():
    r = resolve(case_id='ECLI:NL:RVS:2019:2481', country='Netherlands')
    assert r['permalink_kind'] == 'ecli_deeplink'
    assert r['permalink'].startswith('https://deeplink.rechtspraak.nl/')
    assert 'data.rechtspraak.nl' in r['fulltext_url'], \
        'Netherlands is the one corpus whose full text is retrievable'


def test_ecli_wins_even_if_country_is_wrong():
    """An ECLI is unambiguous; a mislabelled country must not lose the resolver."""
    r = resolve(case_id='ECLI:NL:RVS:2019:2481', country='Brazil')
    assert r['permalink_kind'] == 'ecli_deeplink'


def test_brazil_cnj_routes_to_its_tribunal():
    r = resolve(case_id='0001234-56.2022.8.26.0100', country='Brazil', tribunal='TJSP')
    assert r['permalink_kind'] == 'court_search'
    assert r['identifier'] == '0001234-56.2022.8.26.0100'
    assert 'tjsp.jus.br' in r['permalink']


def test_brazil_unknown_tribunal_falls_back_nationally():
    r = resolve(case_id='0001234-56.2022.8.99.0100', country='Brazil', tribunal='TJXX')
    assert r['permalink_kind'] == 'court_form'
    assert r['identifier'] == '0001234-56.2022.8.99.0100', \
        'the normalised number is the durable identifier even without a portal'


def test_legacy_tjsp_record_is_still_reachable():
    """Pre-CNJ TJSP records carry only an ESAJ key and no URL."""
    r = resolve(case_id='2687421', country='Brazil', tribunal='TJSP')
    assert r['permalink_kind'] == 'court_record_id'
    assert 'cdAcordao=2687421' in r['permalink']


def test_canada_prefers_a_real_canlii_url():
    r = resolve(case_id='2019 FC 1', country='Canada',
                url='https://www.canlii.org/en/ca/fct/doc/2019/2019fc1/2019fc1.html')
    assert r['permalink_kind'] == 'canlii_citation'
    assert r['permalink'].startswith('https://www.canlii.org/')


def test_canada_without_url_falls_back_to_search():
    r = resolve(case_id='Smith v Canada', country='Canada')
    assert r['permalink_kind'] == 'canlii_search'


def test_nothing_resolvable_keeps_the_scraped_url():
    r = resolve(case_id='???', country='Atlantis', url='http://example.org/x')
    assert r['permalink_kind'] == 'scraped_url'
    assert r['permalink'] == 'http://example.org/x'


def test_every_validation_sample_row_resolves():
    """No decision in the published validation sample may be unreachable."""
    import csv
    root = Path(__file__).resolve().parent.parent
    with open(root / 'validation' / 'second_coder_sample_raw.csv',
              newline='', encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    assert rows, 'validation sample is empty'
    unresolved = [r['case_id'] for r in rows
                  if resolve(case_id=r['case_id'], country=r['country'],
                             tribunal=r['tribunal'], url=r.get('url'),
                             title=r.get('title'))['permalink_kind'] == 'unresolved']
    assert not unresolved, f'{len(unresolved)} unreachable: {unresolved[:5]}'
