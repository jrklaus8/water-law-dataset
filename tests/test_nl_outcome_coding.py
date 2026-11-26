"""Offline tests for utils/nl_outcome_coding.py. Synthetic strings only; no network access.
Run from the repository root:  python -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "utils"))
import nl_outcome_coding as n  # noqa: E402


def wrap(*paras):
    return "<open-rechtspraak><uitspraak>" + "".join("<para>%s</para>" % p for p in paras) + "</uitspraak></open-rechtspraak>"


class TestOutcomeRules(unittest.TestCase):
    def test_simple_win(self):
        self.assertEqual(n.classify("verklaart het beroep gegrond; vernietigt het besluit")[0], "WIN")

    def test_simple_loss(self):
        self.assertEqual(n.classify("verklaart het beroep ongegrond")[0], "LOSS")
        self.assertEqual(n.classify("bevestigt de aangevallen uitspraak")[0], "LOSS")

    def test_partial_not_win(self):
        self.assertEqual(n.classify("verklaart het beroep gedeeltelijk gegrond; vernietigt het besluit voor zover")[0], "PARTIAL")

    def test_inadmissible(self):
        self.assertEqual(n.classify("verklaart het hoger beroep niet-ontvankelijk")[0], "INADMISSIBLE")

    def test_multi_step_follows_final_merits_clause(self):
        # The case the FUTURE_WORK.md regex mislabels as WIN: appeal upheld, annulled, then original beroep dismissed.
        label, _, multi = n.classify("I. verklaart het hoger beroep gegrond; II. vernietigt de uitspraak van de rechtbank; III. verklaart het beroep ongegrond.")
        self.assertEqual((label, multi), ("LOSS", 1))

    def test_remand(self):
        self.assertEqual(n.classify("verwijst de zaak terug naar de rechtbank")[0], "REMAND")

    def test_interim_is_not_an_outcome(self):
        self.assertEqual(n.classify("draagt de raad op om binnen 20 weken na de verzending van deze tussenuitspraak een besluit te nemen")[0], "INTERIM")

    def test_costs_only(self):
        self.assertEqual(n.classify("wijst het verzoek om vergoeding van de proceskosten af; veroordeelt de Staat tot vergoeding van proceskosten")[0] in ("NO_MERITS_RULING", "LOSS"), True)

    def test_unrecognised_is_not_guessed(self):
        self.assertEqual(n.classify("doet iets onbekends")[0], "UNCLASSIFIED")

    def test_empty(self):
        self.assertEqual(n.classify("")[0], "NO_TEXT")


class TestExtraction(unittest.TestCase):
    def test_flat_paragraphs_after_heading(self):
        xml = wrap("Overwegingen", "Beslissing", "De rechtbank verklaart het beroep gegrond;", "Aldus gedaan door mr. X", "Uitgesproken in het openbaar")
        r = n.classify_xml(xml)
        self.assertEqual(r["outcome"], "WIN")
        self.assertNotIn("Aldus", r["dispositive"])

    def test_no_heading_uses_leadin(self):
        xml = wrap("Overweging", "De Afdeling bestuursrechtspraak van de Raad van State:", "verklaart het beroep ongegrond.", "Aldus vastgesteld")
        self.assertEqual(n.classify_xml(xml)["outcome"], "LOSS")

    def test_no_dispositive(self):
        self.assertEqual(n.classify_xml(wrap("alleen overwegingen"))["outcome"], "NO_TEXT")


if __name__ == "__main__":
    unittest.main()
