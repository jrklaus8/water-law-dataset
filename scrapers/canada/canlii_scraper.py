"""
CanLII (Canada) water law jurisprudence scraper.
API docs: https://developer.canlii.org/
Free API key required — register at https://developer.canlii.org/

Covers: all 10 provincial + 3 territorial courts of appeal and superior courts.
Date filter: 2016-01-01 to 2026-12-31 (client-side from decisionDate field).
"""
import os
import urllib.request, urllib.parse, json, sys, time, re
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

# ── CONFIG ────────────────────────────────────────────────────────────────────
# Set CANLII_API_KEY in your environment or .env file.
# Get a free key at https://developer.canlii.org/
API_KEY = os.getenv('CANLII_API_KEY', '')
if not API_KEY:
    raise SystemExit('ERROR: CANLII_API_KEY environment variable not set.\n'
                     'Register at https://developer.canlii.org/ and set the variable.')
# ─────────────────────────────────────────────────────────────────────────────

BASE    = 'https://api.canlii.org/v1'
LANG    = 'en'
HDRS    = {'User-Agent': 'research/water-law-dataset (academic use)'}

YEAR_START = 2016
YEAR_END   = 2026

# Provincial + territorial courts of appeal and superior/king's bench courts
TARGET_COURTS = [
    # Appellate courts
    'bcca', 'abca', 'skca', 'mbca', 'onca', 'qcca',
    'nbca', 'nsca', 'peica', 'nlca', 'ykca', 'nwtca', 'nuca',
    # Superior/King's Bench courts
    'bcsc', 'abkb', 'skkb', 'mbqb', 'onsc', 'qccs',
    'nbkb', 'nssc', 'peisc', 'nlsc', 'yksc', 'nwtsc', 'nucj',
    # Federal
    'fca-caf', 'fct-cf',
    # Supreme Court of Canada
    'csc-scc',
]

KEYWORDS = [
    'water supply',
    'drinking water',
    'wastewater',
    'water services',
    'water utility',
    'water treatment',
    'water rates',
    'sewage',
    'water board',
    'water quality',
]

RESULT_COUNT = 100

def api_get(path, params=None):
    p = {'api_key': API_KEY}
    if params:
        p.update(params)
    url = f'{BASE}{path}?' + urllib.parse.urlencode(p)
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

def search_keyword(keyword, offset=0):
    return api_get(f'/caseSearch/{LANG}/', {
        'keyword': keyword,
        'resultCount': RESULT_COUNT,
        'offset': offset,
    })

def extract_year(date_str):
    if not date_str:
        return None
    m = re.match(r'(\d{4})', str(date_str))
    return int(m.group(1)) if m else None

# ── Step 1: get all available courts (to validate TARGET_COURTS) ──────────────
print('Fetching available courts from CanLII...')
try:
    db_resp = api_get(f'/caseBrowse/{LANG}/')
    all_dbs = {db['databaseId']: db for db in db_resp.get('caseDatabases', [])}
    print(f'  Available databases: {len(all_dbs)}')
    valid_courts = [c for c in TARGET_COURTS if c in all_dbs]
    print(f'  Target courts matched: {len(valid_courts)}/{len(TARGET_COURTS)}')
    for c in TARGET_COURTS:
        if c not in all_dbs:
            print(f'    WARNING: {c} not found in API — skipping')
except Exception as e:
    print(f'ERROR fetching courts: {e}')
    valid_courts = TARGET_COURTS  # use as-is, errors handled per-request

# ── Step 2: keyword search across all courts ──────────────────────────────────
all_cases = {}

for keyword in KEYWORDS:
    offset = 0
    kw_count = 0

    # Get first page to know total
    try:
        resp = search_keyword(keyword, offset=0)
    except Exception as e:
        print(f'  ERROR "{keyword}": {e}')
        continue

    total = resp.get('totalCount', 0)
    print(f'\nKeyword: "{keyword}" → {total} total results')

    while True:
        try:
            resp = search_keyword(keyword, offset=offset)
        except Exception as e:
            print(f'  Page offset={offset}: ERROR {e}')
            time.sleep(3)
            break

        cases = resp.get('cases', [])
        if not cases:
            break

        for case in cases:
            db_id  = case.get('databaseId', '')
            case_id = case.get('caseId', '')
            key = (db_id, case_id)
            if key in all_cases:
                continue

            # Court filter
            if db_id not in valid_courts:
                continue

            # Date filter
            date = case.get('decisionDate', '') or ''
            year = extract_year(date)
            if year is None or not (YEAR_START <= year <= YEAR_END):
                continue

            all_cases[key] = {
                'country':       'Canada',
                'jurisdiction':  db_id,
                'case_id':       case_id,
                'citation':      case.get('citation', ''),
                'title':         case.get('title', ''),
                'decision_date': date,
                'year':          year,
                'keywords':      ', '.join(case.get('keywords', [])),
                'url':           case.get('url', ''),
            }
            kw_count += 1

        offset += RESULT_COUNT
        print(f'  offset={offset}: {kw_count} new cases so far (total unique: {len(all_cases)})')
        time.sleep(0.15)  # ~6 req/s — well within limits

        if offset >= total:
            break

# ── Step 3: Save ──────────────────────────────────────────────────────────────
cases_list = list(all_cases.values())
out = os.path.join(os.getenv('OUTPUT_DIR', '.'), 'canada_water_law_2016_2026.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(cases_list, f, ensure_ascii=False, indent=2)

print(f'\n=== DONE: {len(cases_list)} Canadian water law cases (2016-2026) ===')
print(f'Saved to: {out}')

# Year distribution
yc = Counter(c['year'] for c in cases_list)
print('\nYear distribution:')
for yr in sorted(yc):
    print(f'  {yr}: {yc[yr]}')

# Court distribution
cc = Counter(c['jurisdiction'] for c in cases_list)
print('\nTop courts:')
for court, n in cc.most_common(15):
    print(f'  {court}: {n}')

# Sample
if cases_list:
    s = cases_list[0]
    print(f'\nSample case:')
    print(f'  citation: {s["citation"]}')
    print(f'  title: {s["title"]}')
    print(f'  date: {s["decision_date"]}')
    print(f'  url: {s["url"]}')