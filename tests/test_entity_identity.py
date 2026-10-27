import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "utils"))
import entity_identity as ei  # noqa: E402

PERSON_ID = "https://claudioklaus.com/#person"


def orcid_checksum_ok(orcid):
    digits = orcid.replace("-", "")
    total = 0
    for ch in digits[:-1]:
        total = (total + int(ch)) * 2
    check = (12 - total % 11) % 11
    return digits[-1] == ("X" if check == 10 else str(check))


class EntityTests(unittest.TestCase):
    def setUp(self):
        self.data = ei.load()
        self.full = ei.build_graph(self.data, full=True)
        self.nodes = {n["@id"]: n for n in self.full["@graph"]}

    def test_canonical_person_id(self):
        self.assertEqual(self.data["person"]["@id"], PERSON_ID)
        self.assertEqual(self.nodes[PERSON_ID]["@type"], "Person")

    def test_references_use_canonical_id(self):
        for nid in self.nodes:
            node = self.nodes[nid]
            for key in ("author", "creator"):
                if key in node:
                    self.assertEqual(node[key], {"@id": PERSON_ID})

    def test_entities_are_separate(self):
        ids = [n["@id"] for n in self.full["@graph"]]
        self.assertEqual(len(ids), len(set(ids)))
        podcast = next(n for n in self.full["@graph"] if n["@type"] == "PodcastSeries")
        self.assertNotEqual(podcast["@id"], PERSON_ID)
        person_urls = set(self.nodes[PERSON_ID]["sameAs"])
        self.assertFalse(person_urls & set(podcast["sameAs"]))

    def test_profile_urls_unique_https(self):
        urls = [p["url"] for p in self.data["profiles"]]
        for pc in self.data["podcast"]["sameAs"]:
            urls.append(pc["url"])
        self.assertEqual(len(urls), len(set(urls)))
        self.assertTrue(all(u.startswith("https://") for u in urls))

    def test_identifiers_match_profile_urls(self):
        ids = {i["propertyID"]: i["value"] for i in self.data["identifiers"]}
        urls = " ".join(p["url"] for p in self.data["profiles"])
        self.assertIn(ids["ORCID"], urls)
        self.assertIn(ids["Wikidata"], urls)
        self.assertIn(ids["Google Scholar"], urls)
        self.assertIn(ids["Lattes"], urls)
        self.assertEqual(len(ids), len(self.data["identifiers"]))
        for v in ids.values():
            self.assertNotIn("http", v)

    def test_orcid_checksum(self):
        orcid = next(i["value"] for i in self.data["identifiers"] if i["propertyID"] == "ORCID")
        self.assertTrue(orcid_checksum_ok(orcid))

    def test_unverified_entries_not_emitted(self):
        data = json.loads(json.dumps(self.data))
        data["profiles"].append({"label": "x", "url": "https://example.com/x", "status": "candidate"})
        self.assertNotIn("https://example.com/x", ei.person_node(data)["sameAs"])

    def test_every_entry_has_known_status(self):
        known = ei.EMIT_STATUSES | {"candidate"}
        entries = (self.data["profiles"] + self.data["identifiers"] + self.data["works"]
                   + self.data["podcast"]["sameAs"])
        for e in entries:
            self.assertIn(e["status"], known)

    def test_no_unsupported_claims(self):
        person = self.nodes[PERSON_ID]
        for key in ("jobTitle", "worksFor", "alumniOf", "award", "image"):
            self.assertNotIn(key, person)

    def test_affiliation_is_separate_entity(self):
        person = self.nodes[PERSON_ID]
        org_id = "https://www.eur.nl/en/esl#organization"
        self.assertEqual(person["affiliation"], [{"@id": org_id}])
        self.assertEqual(self.nodes[org_id]["@type"], "CollegeOrUniversity")
        self.assertNotIn("jobTitle", person)

    def test_json_roundtrip(self):
        block = ei.render_block(self.data)
        payload = re.search(r'<script type="application/ld\+json">\n(.*)\n</script>', block, re.S).group(1)
        self.assertEqual(json.loads(payload), ei.build_graph(self.data))

    def test_published_page_in_sync(self):
        for page in ei.PAGES:
            html = page.read_text(encoding="utf-8")
            self.assertEqual(ei.apply_block(html, ei.render_block(self.data)), html, f"run --inject: {page}")

    def test_page_markup_matches_visible_content(self):
        html = ei.PAGES[0].read_text(encoding="utf-8")
        self.assertIn("Claudio Klaus Junior", html)
        self.assertIn("Global Water Law Judicial Decisions Dataset", html)
        self.assertIn("10.5281/zenodo.19836413", html)


if __name__ == "__main__":
    unittest.main()
