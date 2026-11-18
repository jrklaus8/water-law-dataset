"""Offline tests of pure helper functions in the scrapers, the merge utility and the jurimetric coding engine.

SAFETY: no network access, no file reads outside the repository, no credentials. All fixtures below are short synthetic strings written for
this test file; none is a real court decision or a real person's data. The scripts are loaded with tests/_safe_load.py, which executes only
function definitions and side-effect-free assignments, never a scraper's top-level collection code.

SCOPE: these are CHARACTERIZATION tests. They record what the current code does so that an unintended change is noticed. They are not a
validation of the research coding and they say nothing about coverage of real sources. Known defects that a researcher still has to rule on
are marked @unittest.expectedFailure with the behaviour they should have; see docs/audit-report.md (findings F-07, F-08).
Run from the repository root:  python -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _safe_load as L  # noqa: E402


class TestRechtspraakHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ns = L.load('scrapers/netherlands/rechtspraak_scraper.py')

    def test_ecli_year(self):
        self.assertEqual(self.ns['parse_ecli_year']('ECLI:NL:RVS:2019:1234'), 2019)
        self.assertEqual(self.ns['parse_ecli_year']('ECLI:NL:CBB:2024:7'), 2024)
        self.assertIsNone(self.ns['parse_ecli_year']('not an ecli'))
        self.assertIsNone(self.ns['parse_ecli_year']('ECLI:BE:CA:2019:1'))

    SYNTHETIC_XML = (
        '<open-rechtspraak><rdf:RDF>'
        '<dcterms:date rdfs:label="Uitspraakdatum" xmlns:dcterms="x">2019-05-14</dcterms:date>'
        '<psi:zaaknummer rdfs:label="Zaaknummer" xmlns:psi="x">201900123/1/A1</psi:zaaknummer>'
        '<dcterms:creator rdfs:label="Instantie" xmlns:dcterms="x">Raad van State</dcterms:creator>'
        '<dcterms:subject rdfs:label="Rechtsgebied" xmlns:dcterms="x">Bestuursrecht; Omgevingsrecht</dcterms:subject>'
        '<psi:procedure rdfs:label="Procedure" xmlns:psi="x">Hoger beroep</psi:procedure>'
        '</rdf:RDF><inhoudsindicatie><para>Vergunning voor <b>lozing</b> op\n oppervlaktewater.</para></inhoudsindicatie></open-rechtspraak>'
    )

    def test_parse_content_extracts_documented_fields(self):
        p = self.ns['parse_content'](self.SYNTHETIC_XML)
        self.assertEqual(p['date'], '2019-05-14')
        self.assertEqual(p['zaak'], '201900123/1/A1')
        self.assertEqual(p['court'], 'Raad van State')
        self.assertEqual(p['rechtsgebied'], 'Bestuursrecht; Omgevingsrecht')
        self.assertEqual(p['procedure'], 'Hoger beroep')
        self.assertEqual(p['inhoudsindicatie'], 'Vergunning voor lozing op oppervlaktewater.')

    def test_parse_content_missing_fields_are_empty_strings_not_errors(self):
        p = self.ns['parse_content']('<open-rechtspraak></open-rechtspraak>')
        self.assertEqual(set(p), {'date', 'zaak', 'court', 'rechtsgebied', 'procedure', 'inhoudsindicatie'})
        self.assertTrue(all(v == '' for v in p.values()))

    def test_inhoudsindicatie_is_truncated_to_2000_characters(self):
        xml = '<inhoudsindicatie>' + ('water ' * 1000) + '</inhoudsindicatie>'
        self.assertEqual(len(self.ns['parse_content'](xml)['inhoudsindicatie']), 2000)

    def test_is_water_filter(self):
        f = self.ns['is_water']
        self.assertTrue(f({'inhoudsindicatie': 'Heffing door het waterschap', 'rechtsgebied': ''}))
        self.assertTrue(f({'inhoudsindicatie': 'geen bijzonderheden', 'rechtsgebied': 'Omgevingsrecht'}))
        self.assertFalse(f({'inhoudsindicatie': 'Verblijfsvergunning asiel', 'rechtsgebied': 'Vreemdelingenrecht'}))

    def test_is_water_matches_any_text_containing_the_substring_water(self):
        # Characterization of a known precision limit: the filter is a substring test, so any word containing "water" counts.
        self.assertTrue(self.ns['is_water']({'inhoudsindicatie': 'Het Waterfront-project', 'rechtsgebied': ''}))


class TestBrazilHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.to = L.load('scrapers/brazil/tjto_scraper.py')
        cls.df = L.load('scrapers/brazil/tjdft_scraper.py')

    def test_cnj_number_formatting_and_year(self):
        cnj = self.to['num20_to_cnj']('00190457420248272700')
        self.assertEqual(cnj, '0019045-74.2024.8.27.2700')
        self.assertEqual(self.to['year_from_cnj'](cnj), '2024')

    def test_cnj_helpers_leave_unexpected_input_alone(self):
        self.assertEqual(self.to['num20_to_cnj']('123'), '123')
        self.assertEqual(self.to['year_from_cnj']('no number here'), '')

    def test_tjdft_year_and_html_cleaning(self):
        self.assertEqual(self.df['extract_year']('2022-03-15T10:00:00Z'), 2022)
        self.assertIsNone(self.df['extract_year'](None))
        self.assertIsNone(self.df['extract_year']('15/03/2022'))
        self.assertEqual(self.df['clean_html']('<mark>água</mark>\xa0 fornecida '), 'água  fornecida')
        self.assertEqual(self.df['clean_html'](None), '')


class TestCanadaHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ns = L.load('scrapers/canada/canlii_scraper.py')

    def test_year_from_citation_respects_the_collection_window(self):
        f = self.ns['year_from_citation']
        self.assertEqual(f('2019 SCC 12 (CanLII)'), 2019)
        self.assertEqual(f('2018 CanLII 12345 (ON SC)'), 2018)
        self.assertIsNone(f('2005 SCC 12 (CanLII)'))   # before 2016
        self.assertIsNone(f(''))
        self.assertIsNone(f('SCC 12'))

    def test_extract_year_from_date(self):
        f = self.ns['extract_year']
        self.assertEqual(f('2020-06-30'), 2020)
        self.assertIsNone(f('1999-01-01'))
        self.assertIsNone(f(None))


class TestMergeNormalisation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ns = L.load('utils/merge_national.py')

    EXPECTED_KEYS = {'country', 'tribunal', 'court_name', 'case_id', 'title', 'date', 'year', 'case_type', 'chamber', 'judge', 'legal_area', 'summary', 'url'}

    def test_all_three_normalisers_emit_the_unified_schema(self):
        for fn, rec in (('normalize_brazil', {'tribunal': 'TJSC', 'estado': 'Santa Catarina', 'num_processo': '1', 'ano': 2020, 'ementa': 'x'}),
                        ('normalize_canada', {'tribunal': 'ONSC', 'citation': '2019 ONSC 1', 'title': 'A v B', 'year': 2019}),
                        ('normalize_netherlands', {'court': 'RvS', 'ecli': 'ECLI:NL:RVS:2019:1', 'year': 2019, 'inhoudsindicatie': 'x'})):
            out = self.ns[fn](rec)
            self.assertEqual(set(out), self.EXPECTED_KEYS, fn)

    def test_summary_is_truncated_to_3000_characters(self):
        self.assertEqual(len(self.ns['normalize_brazil']({'ementa': 'a' * 5000})['summary']), 3000)
        self.assertEqual(len(self.ns['normalize_netherlands']({'inhoudsindicatie': 'a' * 5000})['summary']), 3000)

    def test_legal_area_is_a_constant_for_brazil_and_canada_not_source_data(self):
        # Characterization of a provenance point documented in docs/data-management.md: this field is set by the pipeline, not read from the source.
        self.assertEqual(self.ns['normalize_brazil']({})['legal_area'], 'Direito à Água / Saneamento')
        self.assertEqual(self.ns['normalize_canada']({})['legal_area'], 'Water Law')
        self.assertEqual(self.ns['normalize_netherlands']({'rechtsgebied': 'Bestuursrecht'})['legal_area'], 'Bestuursrecht')


class TestJurimetricCoding(unittest.TestCase):
    """Synthetic phrases only. Expected values record the CURRENT behaviour of the regex engine."""

    @classmethod
    def setUpClass(cls):
        cls.ns = L.load('utils/jurimetric_coding.py')

    def test_governance_categories(self):
        g = self.ns['code_governance']
        self.assertEqual(g('cobrança indevida de tarifa de água pela concessionária'), 'tariff_dispute')
        self.assertEqual(g('recusa de ligação de água em área irregular'), 'connection_refusal')
        self.assertEqual(g('waterschap heffing watersysteem'), 'waterboard_governance')

    def test_text_without_water_vocabulary_is_not_water_related(self):
        self.assertEqual(self.ns['code_governance']('vreemdelingenrecht verblijfsvergunning asiel'), 'not_water_related')

    def test_human_rights_language(self):
        h = self.ns['code_hr']
        self.assertEqual(h('o direito à água é um direito fundamental'), 1)
        self.assertEqual(h('recht op drinkwater'), 1)
        self.assertEqual(h('the right to safe water'), 1)
        self.assertEqual(h('contrato de fornecimento de energia'), 0)

    def test_win_loss_is_only_coded_for_brazil(self):
        self.assertEqual(self.ns['code_win_loss']('cobrança indevida de água', 'Netherlands'), 'not_coded')
        self.assertEqual(self.ns['code_win_loss']('cobrança indevida de água', 'Brazil'), 'user_wins')
        self.assertEqual(self.ns['code_win_loss']('texto sem desfecho', 'Brazil'), 'unclear')

    def test_ministerio_publico_only_for_brazil(self):
        self.assertEqual(self.ns['code_mp']('ação civil pública do ministério público', 'Brazil'), 1)
        self.assertEqual(self.ns['code_mp']('ação civil pública do ministério público', 'Canada'), 0)

    def test_coding_is_deterministic(self):
        t = 'suspensão do fornecimento de água por débito'
        self.assertEqual([self.ns['code_governance'](t) for _ in range(3)], [self.ns['code_governance'](t)] * 3)

    # ---- known defects awaiting the researcher's ruling (audit findings F-07, F-08) ------------------------------------------------------------
    # The win/loss patterns contain truncated stems followed by \b, and "devido" matches inside "indevido", so some "improper" phrases are coded
    # in the wrong direction. These tests state the behaviour the researcher would presumably want; they are expected to FAIL today. When the
    # patterns are corrected (a change that alters results and needs approval) they will start to pass and the markers must be removed.
    @unittest.expectedFailure
    def test_improper_disconnection_should_favour_the_user(self):
        self.assertEqual(self.ns['code_win_loss']('corte indevido do fornecimento de água', 'Brazil'), 'user_wins')

    @unittest.expectedFailure
    def test_improper_suspension_should_favour_the_user(self):
        self.assertEqual(self.ns['code_win_loss']('suspensão indevida do fornecimento de água', 'Brazil'), 'user_wins')


if __name__ == '__main__':
    unittest.main(verbosity=2)
