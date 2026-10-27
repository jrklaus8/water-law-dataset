"""Build the Schema.org entity graph for Claudio Klaus and the dataset pages.

Data lives in identity/entity.json. Only entries whose status is in
EMIT_STATUSES are published. Usage:

    python utils/entity_identity.py --print     # show the JSON-LD graph
    python utils/entity_identity.py --inject    # write it into docs/index.html
    python utils/entity_identity.py --check     # fail if docs/index.html is stale
"""
import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTITY_FILE = ROOT / "identity" / "entity.json"
PAGES = [ROOT / "docs" / "index.html"]

EMIT_STATUSES = {"fetched_verified", "user_asserted", "search_corroborated"}
START = '<!-- entity-jsonld:start -->'
END = '<!-- entity-jsonld:end -->'

SITE = "https://jrklaus8.github.io/water-law-dataset/"
DATASET_ID = SITE + "#dataset"


def load(path=ENTITY_FILE):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _emit(items):
    return [i for i in items if i.get("status") in EMIT_STATUSES]


def person_node(data):
    p = data["person"]
    node = {
        "@type": "Person",
        "@id": p["@id"],
        "name": p["name"],
        "alternateName": list(p["alternateName"]),
        "url": p["url"],
        "sameAs": [x["url"] for x in _emit(data["profiles"])],
        "identifier": [
            {"@type": "PropertyValue", "propertyID": i["propertyID"], "value": i["value"]}
            for i in _emit(data["identifiers"])
        ],
    }
    affiliations = _emit(data.get("affiliations", []))
    if affiliations:
        node["affiliation"] = [{"@id": a["@id"]} for a in affiliations]
    return node


def affiliation_nodes(data):
    return [{
        "@type": "CollegeOrUniversity",
        "@id": a["@id"],
        "name": a["name"],
        "url": a["url"],
        "parentOrganization": {"@type": "CollegeOrUniversity", "name": a["parentOrganization"]},
    } for a in _emit(data.get("affiliations", []))]


def podcast_node(data):
    pc = data["podcast"]
    return {
        "@type": "PodcastSeries",
        "@id": pc["@id"],
        "name": pc["name"],
        "author": {"@id": data["person"]["@id"]},
        "sameAs": [x["url"] for x in _emit(pc["sameAs"])],
    }


def work_nodes(data):
    out = []
    for w in _emit(data["works"]):
        out.append({
            "@type": w["@type"],
            "@id": w["@id"],
            "headline": w["headline"],
            "url": w["url"],
            "publisher": {"@type": "Organization", "name": w["publisher"]},
            "author": {"@id": data["person"]["@id"]},
        })
    return out


def dataset_node(data):
    return {
        "@type": "Dataset",
        "@id": DATASET_ID,
        "name": "Global Water Law Judicial Decisions Dataset",
        "url": SITE,
        "version": "0.3.0",
        "license": "https://opensource.org/licenses/MIT",
        "identifier": "https://doi.org/10.5281/zenodo.19836413",
        "sameAs": [
            "https://doi.org/10.5281/zenodo.19836413",
            "https://github.com/jrklaus8/water-law-dataset",
        ],
        "creator": {"@id": data["person"]["@id"]},
    }


def build_graph(data=None, full=False):
    """Page graph: person + dataset. full=True adds podcast and authored works."""
    data = data or load()
    graph = [person_node(data), dataset_node(data)] + affiliation_nodes(data)
    if full:
        graph += [podcast_node(data)] + work_nodes(data)
    return {"@context": "https://schema.org", "@graph": graph}


def render_block(data=None):
    body = json.dumps(build_graph(data), indent=2, ensure_ascii=False).replace("</", "<\\/")
    return f'{START}\n<script type="application/ld+json">\n{body}\n</script>\n{END}'


def apply_block(html, block):
    if START in html and END in html:
        head, rest = html.split(START, 1)
        _, tail = rest.split(END, 1)
        return head + block + tail
    return html.replace("</head>", block + "\n</head>", 1)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--print", action="store_true")
    mode.add_argument("--inject", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    block = render_block()
    if args.print:
        print(block)
        return 0
    stale = False
    for page in PAGES:
        html = page.read_text(encoding="utf-8")
        new = apply_block(html, block)
        if new != html:
            if args.inject:
                page.write_text(new, encoding="utf-8")
                print(f"updated {page.relative_to(ROOT)}")
            else:
                print(f"stale: {page.relative_to(ROOT)}")
                stale = True
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
