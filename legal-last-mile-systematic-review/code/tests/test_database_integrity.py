#!/usr/bin/env python3
"""Integrity tests for the study map, the retired/merged studies and the effect-size table, written independently of verify_repository.py.

 * study_record_map: unique study ids, one active study per record, retired rows all point to full-text excludes whose code matches the retirement reason
   (retired_duplicate -> E08 and the kept record is an active include named in the note; retired_excluded -> the stated code), and a retired study is absent from the
   extraction database, the evidence map, the effect-size table and the linked-report table.
 * effect_sizes.csv: one row per study, every study extracted, required descriptive fields filled, and any row flagged for pooling must be numeric (estimate and SE),
   which the R scripts rely on. A census of how many rows are numerically poolable at all is asserted too, so a change in that picture is noticed.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_database_integrity.py"""
import csv
import re
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
csv.field_size_limit(sys.maxsize)


def rows(rel):
    with open(ROOT / rel, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def numeric(x):
    try:
        float(str(x).replace(',', '')); return True
    except ValueError:
        return False


class TestStudyMap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mp = rows('03_extraction/extracted_data/study_record_map.csv')
        cls.ft = {r['record_id']: r for r in rows('02_screening/full_text/full_text_screening_database.csv')}
        cls.ed_ids = {r['study_id'] for r in rows('03_extraction/extracted_data/extraction_database.csv')}
        cls.em_ids = {r['study_id'] for r in rows('05_analysis/descriptive/evidence_map.csv')}
        cls.es_ids = [r['study_id'] for r in rows('05_analysis/effect_sizes/effect_sizes.csv')]
        links = rows('03_extraction/extracted_data/linked_reports_2026-09-28.csv')
        cls.linked = {r['study_id_a'] for r in links} | {r['study_id_b'] for r in links}

    def test_uniqueness(self):
        self.assertEqual(len(self.mp), len({r['study_id'] for r in self.mp}))
        active = [r['record_id'] for r in self.mp if r['status'] == 'active']
        self.assertEqual(len(active), len(set(active)))
        self.assertEqual(Counter(r['status'] for r in self.mp), Counter({'active': 1159, 'retired_duplicate': 2, 'retired_excluded': 1}))

    def test_retired_studies(self):
        active_by_study = {r['study_id']: r for r in self.mp if r['status'] == 'active'}
        for r in self.mp:
            if r['status'] == 'active':
                continue
            s, f = r['study_id'], self.ft[r['record_id']]
            self.assertEqual(f['final_decision'], 'exclude', s)
            self.assertTrue(s not in self.ed_ids and s not in self.em_ids and s not in self.es_ids and s not in self.linked, f'{s} still present downstream')
            if r['status'] == 'retired_duplicate':
                self.assertEqual(f['exclusion_reason'], 'E08', s)
                kept = re.search(r'merged into (S\d+)', r['note'])
                self.assertIsNotNone(kept, s)
                self.assertIn(kept.group(1), active_by_study, f'{s} merge target {kept.group(1)} is not an active study')
                rec = re.search(r'record (R[0-9A-F]{12})', r['note'])
                self.assertIsNotNone(rec, s); self.assertEqual(active_by_study[kept.group(1)]['record_id'], rec.group(1), f'{s}: the note names a different kept record')
                self.assertIn(rec.group(1), f['exclusion_reason_detail'], f'{s}: the E08 reason does not name the kept record')
            else:
                self.assertIn(f['exclusion_reason'], {c for c in re.findall(r'excluded (E\d\d)', r['note'])}, s)

    def test_study_ids_never_reused(self):
        ids = [int(r['study_id'][1:]) for r in self.mp]
        self.assertEqual(len(ids), len(set(ids)))
        gaps = set(range(1, max(ids) + 1)) - set(ids)
        # S227 and S399 were retired on 2026-09-16, before the map was built, and are documented permanent gaps (README, CURRENT_FIGURES.md); any other gap means an id was dropped
        self.assertEqual(gaps, {227, 399}, 'an unexpected study-id gap: retired ids must stay listed in the map')


class TestEffectSizes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.es = rows('05_analysis/effect_sizes/effect_sizes.csv')
        cls.ed = {r['study_id'] for r in rows('03_extraction/extracted_data/extraction_database.csv')}

    def test_shape(self):
        self.assertEqual(len(self.es), 62)
        self.assertEqual(len({r['study_id'] for r in self.es}), len(self.es))
        self.assertTrue({r['study_id'] for r in self.es} <= self.ed)
        for col in ('study_id', 'outcome_family', 'exposure_definition', 'comparator_definition', 'effect_measure', 'effect_estimate', 'sample_size', 'direction', 'adjusted',
                    'evidence_status', 'provenance_note', 'included_in_pooled_estimate'):
            self.assertTrue(all(r[col].strip() for r in self.es), f'blank {col}')
        self.assertTrue(all(r['synthesis_family'] in ('A', 'B', 'C', '') for r in self.es))
        self.assertTrue(all(r['evidence_status'] == 'OBSERVED' for r in self.es))

    def test_pooled_rows_are_numeric(self):
        pooled = [r for r in self.es if r['included_in_pooled_estimate'].strip().upper() == 'TRUE']
        self.assertTrue(all(numeric(r['effect_estimate']) and numeric(r['standard_error']) for r in pooled), 'a pooled row lacks a numeric estimate or SE')
        self.assertTrue(all(r['exclusion_from_pooling_reason'].strip() for r in self.es if r not in pooled), 'a non-pooled row gives no reason')

    def test_numeric_census(self):
        """How many of the 62 rows could be pooled on their numbers at all: this is the picture behind the Phase 11 'nothing pooled' verdict."""
        n_est = sum(numeric(r['effect_estimate']) for r in self.es)
        n_se = sum(numeric(r['standard_error']) for r in self.es)
        n_ci = sum(numeric(r['lower_CI']) and numeric(r['upper_CI']) for r in self.es)
        self.assertLess(n_est, 10); self.assertLess(n_se, 10); self.assertLess(n_ci, 10)  # a jump means a dated enrichment script ran: update the documentation that quotes these


if __name__ == '__main__':
    unittest.main(verbosity=1)
