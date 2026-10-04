#!/usr/bin/env python3
"""Tests for the search-export adapters (code/search/adapters): RIS parsing, WoS delimiter handling, DOI cleaning and column lookup. These decide what enters the
identification count, so a parsing defect silently changes PRISMA numbers. Includes a golden test: the RIS parser applied to the committed native ProQuest export must
reproduce the committed normalised CSV row for row (titles and abstracts). Run from legal-last-mile-systematic-review/:  python3 code/tests/test_search_adapters.py"""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/search/adapters'))
import pubmed_adapter as pm  # noqa: E402
import ris_adapter as ris  # noqa: E402
import wos_adapter as wos  # noqa: E402

csv.field_size_limit(sys.maxsize)


class TestRis(unittest.TestCase):
    def test_two_records_crlf_and_blank_lines(self):
        text = 'TY  - JOUR\r\nTI  - First\r\nAU  - Smith, A\r\nAU  - Jones, B\r\nPY  - 2020/05/01\r\nER  - \r\n\r\nTY  - JOUR\r\nTI  - Second\r\nER  - \r\n'
        recs = ris.parse_ris(text)
        self.assertEqual(len(recs), 2)
        self.assertEqual(ris.extract_authors(recs[0]), 'Smith, A; Jones, B'); self.assertEqual(ris.extract_year(recs[0]), '2020')
        self.assertEqual(ris.first_of(recs[1], {'TI'}), 'Second')

    def test_end_of_record_without_its_trailing_space(self):
        # editors and some exporters strip the space after "ER  -"; it was once glued onto the previous field ("text ER  -")
        recs = ris.parse_ris('TY  - JOUR\nTI  - A\nAB  - text\nER  -\nTY  - JOUR\nTI  - B\nER  -\n')
        self.assertEqual(len(recs), 2); self.assertEqual(recs[0]['AB'], ['text'])

    def test_wrapped_lines_continue_the_previous_value_and_missing_er_is_tolerated(self):
        recs = ris.parse_ris('TY  - JOUR\nAB  - a long abstract that\nwraps onto a second line\nTY  - BOOK\nTI  - Next with no ER above\n')
        self.assertEqual(len(recs), 2); self.assertEqual(recs[0]['AB'], ['a long abstract that wraps onto a second line'])

    def test_empty_input_and_year_fallbacks(self):
        self.assertEqual(ris.parse_ris(''), [])
        self.assertEqual(ris.extract_year({'PY': ['n.d.']}), 'n.d.')  # no four digits: returned as written, not invented
        self.assertEqual(ris.extract_year({}), '')

    def test_golden_proquest_export_matches_the_committed_csv(self):
        native = ROOT / '01_search/raw_exports/native/SEARCH_039_PROQUEST_2026-09-11_native.RIS'
        recs = ris.parse_ris(native.read_text(encoding='utf-8', errors='replace'))
        with open(ROOT / '01_search/raw_exports/SEARCH_039_PROQUEST_2026-09-11.csv', encoding='utf-8', newline='') as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(recs), len(rows))
        first = lambda rec, tags: next((rec[t][0].strip() for t in tags if rec.get(t)), '')
        for a, b in list(zip(recs, rows))[::25]:
            self.assertEqual(first(a, ('TI', 'T1')), b['title'].strip())
            self.assertEqual(first(a, ('AB', 'N2')), (b.get('abstract') or '').strip())


class TestWosAndPubmed(unittest.TestCase):
    def test_doi_cleaning(self):
        for mod in (wos, pm):
            self.assertEqual(mod.normalize_doi(' doi:10.1/x '), '10.1/x'); self.assertEqual(mod.normalize_doi('DOI: 10.1/x'), '10.1/x')
            self.assertEqual(mod.normalize_doi(None), ''); self.assertEqual(mod.normalize_doi('10.1/x'), '10.1/x')

    def test_find_column_is_case_insensitive_and_ordered(self):
        for mod in (wos, pm):
            self.assertEqual(mod.find_column(['Title', 'DOI'], ['doi']), 'DOI')
            self.assertEqual(mod.find_column(['A', 'B'], ['b', 'a']), 'B')  # the first candidate that exists wins
            self.assertIsNone(mod.find_column(['A'], ['z']))

    def test_delimiter_sniffing(self):
        self.assertEqual(wos.sniff_delimiter('PT\tAU\tTI\tAB'), '\t'); self.assertEqual(wos.sniff_delimiter('Title,Authors,Year'), ',')

    def test_tab_delimited_export_with_a_stray_quote_keeps_every_record(self):
        # a lone double quote in an abstract must not swallow the following rows (the real export lost 12 of 1,000 rows this way)
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'savedrecs.txt'
            p.write_text('PT\tTI\tAB\nJ\tOne\tthe "so-called gap\nJ\tTwo\tplain\nJ\tThree\tplain too\n', encoding='utf-8')
            header, rows = wos.load_records(p)
        self.assertEqual(header, ['PT', 'TI', 'AB']); self.assertEqual([r['TI'] for r in rows], ['One', 'Two', 'Three'])

    def test_utf8_bom_is_ignored(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'x.csv'
            p.write_bytes('﻿Title,DOI\nA,10.1/x\n'.encode('utf-8'))
            header, rows = wos.load_records(p)
        self.assertEqual(header, ['Title', 'DOI'])


if __name__ == '__main__':
    unittest.main(verbosity=1)
