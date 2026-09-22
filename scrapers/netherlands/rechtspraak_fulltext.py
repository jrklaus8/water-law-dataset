#!/usr/bin/env python3
"""
rechtspraak_fulltext.py — retrieve the full decision body for Dutch cases
=========================================================================
The main Netherlands scraper (`rechtspraak_scraper.py`) fetches the content XML
for every ECLI and keeps only the `inhoudsindicatie` (the court's own summary).
The XML it already receives also contains `<uitspraak>`, the complete text of
the ruling. This script re-fetches that XML and keeps the body, producing a
full-text corpus keyed by ECLI.

Why this exists
---------------
Two of the dataset's stated limitations trace back to the missing body text:

  1. No outcome coding for the Netherlands (README, "Known Limitations"). You
     cannot code who won from a one-sentence inhoudsindicatie. You can from the
     ruling.
  2. Classification false negatives. RESIDUAL_AUDIT.md §3.1 records that the
     supervisor's full-text check found ~2,487 NL decisions with substantive
     water vocabulary against 263 found in the indexed title/summary fields.
     That gap is a text-coverage gap, not a regex gap.

Licensing
---------
Rechtspraak.nl publishes its Open Data for reuse, which is why this corpus can
be redistributed where CanLII's and the Brazilian tribunals' cannot. CONFIRM THE
CURRENT TERMS at https://www.rechtspraak.nl/Uitspraken/paginas/open-data.aspx
before depositing the output. See DATA_ACCESS.md for the per-jurisdiction
redistribution posture.

Usage
-----
    export OUTPUT_DIR=./data
    # ECLIs from the merged dataset:
    python scrapers/netherlands/rechtspraak_fulltext.py --from-csv data/water_law_global.csv
    # or from the scraper's own JSON output:
    python scrapers/netherlands/rechtspraak_fulltext.py --from-json data/netherlands_water_law_2016_2026.json
    # resume after an interruption (skips ECLIs already written):
    python scrapers/netherlands/rechtspraak_fulltext.py --from-csv ... --resume

Output: $OUTPUT_DIR/nl_fulltext/<ECLI>.json, one file per decision, plus a
manifest CSV. Roughly 2 hours for 68k decisions at the default 5 req/s.
"""
import argparse
import csv
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

CONTENT_URL = 'https://data.rechtspraak.nl/uitspraken/content'
HDRS = {'User-Agent': 'research/water-law-dataset (academic use; '
                      'https://github.com/jrklaus8/water-law-dataset)'}
ctx = ssl.create_default_context()

ECLI_RE = re.compile(r'\bECLI:NL:[A-Z0-9]+:\d{4}:[A-Z0-9.\-]+', re.I)


def content_get(ecli, timeout=25):
    url = CONTENT_URL + '?id=' + urllib.parse.quote(ecli)
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read().decode('utf-8', errors='replace')


def _strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = (s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
          .replace('&quot;', '"').replace('&#39;', "'").replace('&nbsp;', ' '))
    return ' '.join(s.split())


def parse_fulltext(xml_body):
    """Pull the decision body and the fields needed to audit it."""
    def rx(pattern, flags=re.S | re.I):
        m = re.search(pattern, xml_body, flags)
        return m.group(1) if m else ''

    uitspraak = rx(r'<uitspraak\b[^>]*>(.*?)</uitspraak>')
    conclusie = rx(r'<conclusie\b[^>]*>(.*?)</conclusie>')
    body = uitspraak or conclusie
    return {
        'inhoudsindicatie': _strip_tags(rx(r'<inhoudsindicatie[^>]*>(.*?)</inhoudsindicatie>')),
        'fulltext': _strip_tags(body),
        'fulltext_chars': len(_strip_tags(body)),
        'fulltext_source': 'uitspraak' if uitspraak else ('conclusie' if conclusie else 'none'),
        'creator': _strip_tags(rx(r'<dcterms:creator[^>]*>(.*?)</dcterms:creator>')),
        'date': _strip_tags(rx(r'<dcterms:date[^>]*>(.*?)</dcterms:date>')),
        'rechtsgebied': _strip_tags(rx(r'<dcterms:subject[^>]*>(.*?)</dcterms:subject>')),
    }


def eclis_from_csv(path):
    out = []
    with open(path, newline='', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            blob = ' '.join(str(row.get(k, '')) for k in ('case_id', 'title', 'url'))
            m = ECLI_RE.search(blob)
            if m:
                out.append(m.group(0).upper())
    return out


def eclis_from_json(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    recs = data if isinstance(data, list) else data.get('cases', [])
    out = []
    for r in recs:
        blob = ' '.join(str(r.get(k, '')) for k in ('ecli', 'case_id', 'title', 'url'))
        m = ECLI_RE.search(blob)
        if m:
            out.append(m.group(0).upper())
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument('--from-csv')
    src.add_argument('--from-json')
    src.add_argument('--ecli', nargs='+', help='fetch specific ECLIs (for spot checks)')
    ap.add_argument('--rate', type=float, default=5.0, help='requests per second (default 5)')
    ap.add_argument('--limit', type=int, help='stop after N decisions (for a trial run)')
    ap.add_argument('--resume', action='store_true', help='skip ECLIs already on disk')
    ap.add_argument('--out', help='output dir (default $OUTPUT_DIR/nl_fulltext)')
    a = ap.parse_args()

    if a.ecli:
        eclis = [e.upper() for e in a.ecli]
    elif a.from_csv:
        eclis = eclis_from_csv(a.from_csv)
    else:
        eclis = eclis_from_json(a.from_json)

    seen, ordered = set(), []
    for e in eclis:
        if e not in seen:
            seen.add(e)
            ordered.append(e)
    eclis = ordered
    if a.limit:
        eclis = eclis[:a.limit]
    if not eclis:
        raise SystemExit('No ECLIs found in the input.')

    out_dir = Path(a.out or (Path(os.getenv('OUTPUT_DIR', './data')) / 'nl_fulltext'))
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / 'manifest.csv'

    if a.resume:
        before = len(eclis)
        eclis = [e for e in eclis if not (out_dir / (e.replace(':', '_') + '.json')).exists()]
        print(f'Resume: {before - len(eclis):,} already on disk, {len(eclis):,} to go.')

    print(f'Fetching {len(eclis):,} decisions at {a.rate} req/s -> {out_dir}')
    delay = 1.0 / a.rate if a.rate > 0 else 0
    ok = fail = empty = 0
    manifest_exists = manifest_path.exists()

    with open(manifest_path, 'a', newline='', encoding='utf-8-sig') as mf:
        w = csv.writer(mf)
        if not manifest_exists:
            w.writerow(['ecli', 'status', 'fulltext_chars', 'fulltext_source', 'file'])

        for i, ecli in enumerate(eclis, 1):
            if i % 250 == 0:
                print(f'  {i:,}/{len(eclis):,}  ok={ok:,} empty={empty:,} fail={fail:,}', flush=True)
            dest = out_dir / (ecli.replace(':', '_') + '.json')
            try:
                rec = parse_fulltext(content_get(ecli))
                rec['ecli'] = ecli
                dest.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding='utf-8')
                if rec['fulltext_chars'] == 0:
                    empty += 1
                    status = 'no_body'
                else:
                    ok += 1
                    status = 'ok'
                w.writerow([ecli, status, rec['fulltext_chars'], rec['fulltext_source'], dest.name])
            except Exception as exc:
                fail += 1
                w.writerow([ecli, f'error: {type(exc).__name__}', 0, '', ''])
            mf.flush()
            if delay:
                time.sleep(delay)

    print(f'\nDone. body retrieved={ok:,}  published without body={empty:,}  errors={fail:,}')
    print(f'Manifest: {manifest_path}')
    if empty:
        print('\nNote: Rechtspraak publishes many decisions as metadata + summary only,')
        print('with no body text. Those rows are "no_body" in the manifest and are a')
        print('genuine ceiling on Netherlands outcome coding — report the ratio.')


if __name__ == '__main__':
    sys.exit(main())
