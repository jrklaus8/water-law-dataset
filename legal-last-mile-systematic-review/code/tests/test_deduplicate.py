#!/usr/bin/env python3
"""Tests for code/search/deduplicate.py, the step that fixes the PRISMA identification counts and the record_id every later file keys on.

Two kinds of test. (1) Golden identity tests: record_id is a content hash, so ANY change to normalize_doi / normalize_title / compute_record_id would silently re-key
the whole corpus; the tests recompute the id of real rows of 01_search/deduplicated/deduplicated_records.csv and require them to match. (2) Behaviour tests on
synthetic records: the two merge rules, the title similarity threshold, same-year requirement, abstract backfill, and order-independence of ids.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_deduplicate.py"""
import csv
import hashlib
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/search'))
import deduplicate as dd  # noqa: E402

csv.field_size_limit(sys.maxsize)


def rec(title, year='2020', doi='', abstract='', **kw):
    return dict(title=title, authors='A', year=year, doi=doi, url='', database='db', search_id='S1', abstract=abstract, **kw)


class TestIdentity(unittest.TestCase):
    def test_record_ids_of_real_rows_are_unchanged(self):
        n = checked = 0
        with open(ROOT / '01_search/deduplicated/deduplicated_records.csv', encoding='utf-8', newline='') as f:
            for r in csv.DictReader(f):
                n += 1
                if n % 97 == 0 or n <= 50:  # a spread of rows including the first fifty
                    self.assertEqual(dd.compute_record_id(r), r['record_id'].split('-')[0] if '-' in r['record_id'] else r['record_id'], r['title'][:60])
                    checked += 1
                if n >= 6000:
                    break
        self.assertGreater(checked, 100)

    def test_id_is_the_documented_hash(self):
        self.assertEqual(dd.compute_record_id(rec('T', doi='https://doi.org/10.1/ABC')), 'R' + hashlib.sha1(b'doi:10.1/abc').hexdigest()[:12].upper())
        self.assertEqual(dd.compute_record_id(rec('The Title: A Study!', year='2019')), 'R' + hashlib.sha1(b'title_year:the title a study|2019').hexdigest()[:12].upper())

    def test_normalisers(self):
        for raw, want in {'https://doi.org/10.1/X': '10.1/x', 'http://dx.doi.org/10.1/X': '10.1/x', ' 10.1/X ': '10.1/x', '': '', None: ''}.items():
            self.assertEqual(dd.normalize_doi(raw), want, raw)
        # pinned on purpose: a "doi:" prefix is NOT stripped (changing that would re-key every record that has one)
        self.assertEqual(dd.normalize_doi('doi:10.1/x'), 'doi:10.1/x')
        self.assertEqual(dd.normalize_title('  Water,  Law & Access: (2020) '), 'water law access 2020')

    def test_ids_do_not_depend_on_input_order(self):
        a, b = rec('Alpha study', doi='10.1/a'), rec('Beta study', doi='10.1/b')
        k1, _ = dd.deduplicate([dict(a), dict(b)]); k2, _ = dd.deduplicate([dict(b), dict(a)])
        self.assertEqual({r['title']: r['record_id'] for r in k1}, {r['title']: r['record_id'] for r in k2})


class TestMerging(unittest.TestCase):
    def test_doi_match_merges_and_logs(self):
        kept, log = dd.deduplicate([rec('One title', doi='10.1/x'), rec('One title', year='2015', doi='HTTPS://DOI.ORG/10.1/X')])
        self.assertEqual(len(kept), 1); self.assertEqual([m['match_rule'] for m in log], ['doi_match'])
        self.assertEqual(log[0]['kept_record_id'], kept[0]['record_id'])

    def test_same_doi_with_a_different_title_is_merged_but_logged_under_a_suffixed_id(self):
        # Known quirk, pinned so nobody changes it unknowingly: the id is keyed on the DOI, so a second record with that DOI and a different title trips the
        # "hash collision" branch and is renamed -1 before the DOI rule merges it. About 4% of merge_log.csv's dropped ids (318 of 7,113) look like this; the kept
        # records never carry a suffix and no record is lost. Fixing it would rewrite merge_log.csv, which is why it is left.
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            kept, log = dd.deduplicate([rec('One title', doi='10.1/x'), rec('A completely different title', year='2015', doi='10.1/x')])
        self.assertEqual(len(kept), 1); self.assertTrue(log[0]['dropped_record_id'].endswith('-1')); self.assertNotIn('-', log[0]['kept_record_id'])

    def test_title_and_year_match_needs_the_same_year_and_high_similarity(self):
        base = 'Legal recognition of informal settlements and access to piped water in urban Africa'
        kept, log = dd.deduplicate([rec(base), rec(base.upper() + '.')])
        self.assertEqual((len(kept), [m['match_rule'] for m in log]), (1, ['title_year_match']))
        kept, _ = dd.deduplicate([rec(base, year='2020'), rec(base, year='2021')])
        self.assertEqual(len(kept), 2)  # same title, different year: kept apart on purpose
        kept, _ = dd.deduplicate([rec(base), rec('Legal recognition and water access in rural Asia')])
        self.assertEqual(len(kept), 2)

    def test_records_without_a_title_are_never_title_matched(self):
        kept, _ = dd.deduplicate([rec(''), rec('')])
        self.assertEqual(len(kept), 2)

    def test_abstract_is_backfilled_into_the_kept_record(self):
        kept, log = dd.deduplicate([rec('Same paper here', doi='10.1/z'), rec('Same paper here', doi='10.1/z', abstract='An abstract.')])
        self.assertEqual(kept[0]['abstract'], 'An abstract.'); self.assertEqual(log[0]['match_rule'], 'doi_match+abstract_backfilled')
        kept, _ = dd.deduplicate([rec('Same', doi='10.1/z', abstract='First.'), rec('Same', doi='10.1/z', abstract='Second.')])
        self.assertEqual(kept[0]['abstract'], 'First.')  # an existing abstract is never overwritten

    def test_a_hash_collision_between_unrelated_records_is_disambiguated(self):
        orig = dd.compute_record_id
        dd.compute_record_id = lambda r: 'RSAME'
        self.addCleanup(setattr, dd, 'compute_record_id', orig)
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            kept, _ = dd.deduplicate([rec('Completely unrelated first title'), rec('Another wholly different subject entirely')])
        self.assertEqual([r['record_id'] for r in kept], ['RSAME', 'RSAME-1'])


if __name__ == '__main__':
    unittest.main(verbosity=1)
