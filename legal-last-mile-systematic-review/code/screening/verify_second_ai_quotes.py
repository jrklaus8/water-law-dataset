#!/usr/bin/env python3
"""Check that every quotation a second AI cites really appears in the paper text.

Each per-record JSON must hold "evidence_quotes": [{"criterion": "...", "page": "...", "quote": "..."}]. The paper text is read from <text-dir>/<record_id>.txt, which stays LOCAL
(papers are copyrighted and are never committed). Matching ignores case, whitespace, hyphenation at line ends and curly versus straight quotes; nothing else is forgiven.
Output: one CSV row per quote and a summary line. A record with any unverified quote is flagged; the pre-registration says a batch below 100% verified is reported as such, not tidied.
Run from legal-last-mile-systematic-review/."""
import argparse, csv, json, re
from pathlib import Path


def squash(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    t = re.sub(r'-\s*\n\s*', '', t)  # hyphenated line breaks
    t = re.sub(r'\s+', ' ', t)
    return t.strip().lower()


def check(json_dir, text_dir):
    rows = []
    for jp in sorted(Path(json_dir).glob('*.json')):
        with open(jp, encoding='utf-8') as fh:
            d = json.load(fh)
        rid = d.get('record_id') or jp.stem
        tp = Path(text_dir) / f'{rid}.txt'
        text = squash(tp.read_text(encoding='utf-8', errors='replace')) if tp.exists() else None
        quotes = d.get('evidence_quotes') or []
        if not quotes:
            rows.append({'record_id': rid, 'criterion': '', 'page': '', 'quote': '', 'result': 'NO QUOTES GIVEN'})
        for qd in quotes:
            q = (qd.get('quote') or '').strip()
            if text is None:
                res = 'TEXT NOT AVAILABLE'
            elif len(q) < 20:
                res = 'TOO SHORT TO CHECK'
            else:
                res = 'verified' if squash(q) in text else 'NOT FOUND IN TEXT'
            rows.append({'record_id': rid, 'criterion': qd.get('criterion', ''), 'page': qd.get('page', ''), 'quote': q[:300], 'result': res})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json-dir', required=True); ap.add_argument('--text-dir', required=True); ap.add_argument('--out-csv', required=True)
    a = ap.parse_args()
    rows = check(a.json_dir, a.text_dir)
    with open(a.out_csv, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['record_id', 'criterion', 'page', 'quote', 'result']); w.writeheader(); w.writerows(rows)
    v = sum(r['result'] == 'verified' for r in rows)
    print(f'{v} of {len(rows)} quotes verified; {len({r["record_id"] for r in rows if r["result"] != "verified"})} records with at least one problem')


if __name__ == '__main__':
    main()
