#!/usr/bin/env python3
"""Fetch Rechtspraak.nl decisions and keep only small derived features (no full text is stored):
  opening        first ~2,500 characters of the body (parties and procedural history)
  water_hits     number of water-term matches in the full text
  words          body length in words
  water_per_1k   water_hits per 1,000 words
Standard library only; resumable (JSONL checkpoint). Reuses the throttle and retry logic of nl_outcome_coding.py.

Usage: python utils/nl_text_features.py --ids ids.txt --out features.jsonl [--rate 8]
"""
import argparse
import json
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nl_outcome_coding as oc  # noqa: E402

WATER = re.compile(r"\b(?:drinkwater\w*|afvalwater\w*|rioolwater\w*|riolering\w*|riool\w*|waterschap\w*|waterwet|waterleiding\w*|waterbedrijf\w*|"
                   r"grondwater\w*|oppervlaktewater\w*|regenwater\w*|hemelwater\w*|waterkering\w*|waterkwaliteit\w*|waterhuishouding\w*|waterpeil\w*|"
                   r"waterbeheer\w*|waterstaat\w*|waterafvoer\w*|wateroverlast|water\b|dijk\w*|overstroming\w*|lozing\w*|zuivering\w*|kade\b|sloot|sloten|polder\w*)", re.I)


def features(xml_text):
    paras = oc.paragraphs(xml_text)
    body = " ".join(paras)
    words = len(body.split())
    hits = len(WATER.findall(body))
    return {"opening": body[:2500], "water_hits": hits, "words": words, "water_per_1k": round(1000 * hits / words, 2) if words else 0.0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--rate", type=float, default=8.0)
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    ids = [l.strip() for l in Path(a.ids).read_text().splitlines() if l.strip()]
    out = Path(a.out)
    done = set()
    if out.exists():
        for line in out.read_text(encoding="utf-8").splitlines():
            try:
                done.add(json.loads(line)["ecli"])
            except Exception:  # noqa: BLE001
                pass
    todo = [i for i in ids if i not in done]
    print("to fetch: %d" % len(todo), flush=True)
    th = oc.Throttle(a.rate)
    lock = threading.Lock()
    n = [0]

    def work(ecli):
        xml, err = oc.fetch(ecli, th)
        rec = {"ecli": ecli}
        rec.update(features(xml) if xml else {"opening": "", "water_hits": 0, "words": 0, "water_per_1k": 0.0, "error": err})
        with lock:
            with out.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n[0] += 1
            if n[0] % 250 == 0:
                print("  %d done" % n[0], flush=True)

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        list(ex.map(work, todo))
    print("finished", flush=True)


if __name__ == "__main__":
    main()
