"""Offline tests for utils/nl_appellant_coding.py. Synthetic captions only; no network access."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "utils"))
import nl_appellant_coding as a  # noqa: E402


def cap(party, role="appellant"):
    return "uitspraak COLLEGE zaaknummer: 18/1 uitspraak van de enkelvoudige kamer in de zaak tussen %s, %s (gemachtigde: mr. X), en de minister van Landbouw, verweerder. Procesverloop" % (party, role)


class TestAppellant(unittest.TestCase):
    def test_company(self):
        self.assertEqual(a.code_opening(cap("[naam 1] B.V., te [plaats]"))["appellant_type"], "COMPANY")
        self.assertEqual(a.code_opening(cap("V.O.F. [naam 1], te [plaats]", "appellante"))["appellant_type"], "COMPANY")

    def test_placeholder_is_not_called_individual(self):
        self.assertEqual(a.code_opening(cap("[naam], te [plaats]"))["appellant_type"], "PRIVATE_ANONYMISED")

    def test_ngo(self):
        self.assertEqual(a.code_opening(cap("Stichting [naam]"))["appellant_type"], "NGO_ASSOCIATION")

    def test_public_bodies(self):
        self.assertEqual(a.code_opening(cap("het college van burgemeester en wethouders van Ede"))["appellant_type"], "MUNICIPALITY")
        self.assertEqual(a.code_opening(cap("het dagelijks bestuur van het waterschap Rijn en IJssel"))["appellant_type"], "WATER_BOARD")
        self.assertEqual(a.code_opening(cap("de staatssecretaris van Infrastructuur en Waterstaat"))["appellant_type"], "STATE_BODY")

    def test_respondent_is_not_the_appellant(self):
        r = a.code_opening("in de zaak tussen [naam], te [plaats], appellant, en de gemeente Ede, verweerder")
        self.assertEqual(r["appellant_type"], "PRIVATE_ANONYMISED")

    def test_residence_municipality_is_not_the_party(self):
        r = a.code_opening("in het geding tussen: [appellant], wonend te Langenboom, gemeente Land van Cuijk, appellant, en het college van burgemeester en wethouders van Land van Cuijk, verweerder.")
        self.assertEqual(r["appellant_type"], "PRIVATE_ANONYMISED")

    def test_raad_van_state_caption_without_role_word_first(self):
        r = a.code_opening("Uitspraak op het hoger beroep van: Bewonersvereniging Ter Coulsterlaan, gevestigd in Heiloo, tegen de uitspraak van de rechtbank")
        self.assertEqual(r["appellant_type"], "NGO_ASSOCIATION")

    def test_role_word_inside_placeholder_ignored(self):
        r = a.code_opening("in het geding tussen: [verzoeker], wonend in Beesel, verzoeker, en de raad van de gemeente Beesel, verweerder.")
        self.assertEqual(r["appellant_type"], "PRIVATE_ANONYMISED")

    def test_unknown(self):
        self.assertEqual(a.code_opening("geen partijen hier")["appellant_type"], "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
