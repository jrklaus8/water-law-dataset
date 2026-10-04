#!/usr/bin/env python3
"""Reconcile the PRISMA identification and screening numbers straight from the files: raw exports by database -> raw total -> merge log -> deduplicated pool ->
title/abstract database -> screening outcomes -> full-text tracking file. Every stated figure in prisma_flow.md and the README is checked against the file it
claims to come from. Run from legal-last-mile-systematic-review/:  python3 code/tests/test_search_reconciliation.py"""
import csv
import re
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
csv.field_size_limit(sys.maxsize)


def nrows(rel):
    with open(ROOT / rel, encoding='utf-8-sig', newline='', errors='replace') as f:
        return sum(1 for _ in csv.reader(f)) - 1


def db_of(name):
    u = name.upper()
    for key, label in (('SCOPUS', 'Scopus'), ('WOS', 'Web of Science'), ('HEIN', 'HeinOnline'), ('PROQUEST', 'ProQuest'), ('JSTOR', 'JSTOR')):
        if key in u:
            return label
    return 'grey/pilot'


class TestPrismaReconciliation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.by_db = Counter()
        for p in sorted((ROOT / '01_search/raw_exports').glob('*.csv')):
            cls.by_db[db_of(p.name)] += nrows(str(p.relative_to(ROOT)))
        cls.flow = (ROOT / '06_outputs/prisma/prisma_flow.md').read_text(encoding='utf-8')
        cls.readme = (ROOT / 'README.md').read_text(encoding='utf-8')

    def test_identification(self):
        self.assertEqual(dict(self.by_db), {'Scopus': 5984, 'Web of Science': 4058, 'HeinOnline': 1, 'ProQuest': 24464, 'JSTOR': 50, 'grey/pilot': 37})
        database = sum(v for k, v in self.by_db.items() if k != 'grey/pilot')
        self.assertEqual(database, 34557); self.assertEqual(sum(self.by_db.values()), 34594)
        self.assertIn('34,557', self.flow); self.assertIn('34,594 raw (34,557 database + 37 grey-literature/pilot)', self.readme)
        # the two ProQuest exports quoted separately in the flow text
        self.assertEqual(7728 + 16736, self.by_db['ProQuest'])

    def test_deduplication(self):
        raw, merged, unique = sum(self.by_db.values()), nrows('01_search/deduplicated/merge_log.csv'), nrows('01_search/deduplicated/deduplicated_records.csv')
        self.assertEqual(raw - merged, unique); self.assertEqual(unique, 27481)
        self.assertEqual(unique, nrows('02_screening/title_abstract/screening_database.csv'))
        self.assertIn('27,481 unique candidates (7,113 duplicates merged)', self.readme)

    def test_title_abstract_screening(self):
        with open(ROOT / '02_screening/title_abstract/screening_database.csv', encoding='utf-8', newline='') as f:
            c = Counter(r['title_abstract_decision'] for r in csv.DictReader(f))
        screened = c['include'] + c['exclude'] + c['unsure']
        self.assertEqual((c['include'], c['exclude'], c['unsure'], c['']), (3062, 22557, 603, 1259))
        self.assertEqual(screened, 26222); self.assertEqual(screened + c[''], 27481)
        self.assertEqual(c['include'] + c['unsure'], 3665)  # the include-plus-unsure records the human second reviewer covered
        self.assertIn('26,222 of 27,481', self.readme); self.assertIn('1,259', self.readme)

    def test_full_text_tracking(self):
        with open(ROOT / '02_screening/full_text/full_text_screening_database.csv', encoding='utf-8', newline='') as f:
            c = Counter(r['final_decision'] for r in csv.DictReader(f))
        self.assertEqual(c['include'] + c['exclude'] + c[''], 3659)
        self.assertEqual((c['include'], c['exclude'], c['']), (1159, 1117, 1383))
        for phrase in ('3,659', '2,276', '1,383', '1,159 include / 1,117 exclude'):
            self.assertIn(phrase, self.flow)
        m = re.search(r'1,383 — (\d+) flagged `wrong_file_retrieved`.*?(\d[\d,]*) `not_retrievable`', self.flow, re.S)
        self.assertIsNotNone(m); self.assertEqual(int(m.group(1)) + int(m.group(2).replace(',', '')), 1383)


if __name__ == '__main__':
    unittest.main(verbosity=1)
