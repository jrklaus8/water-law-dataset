"""
CanLII water law scraper — Canada 2016–2026
==========================================
API docs: https://github.com/canlii/API_documentation
Free key: fill feedback form at https://developer.canlii.org/

Strategy
--------
  1. Auto-discover all ~150+ CanLII databases; classify into tiers.
  2. Tier 1 courts (SCC, FCA, FCT + CoAs): browse ALL 2016-2026 cases,
     apply water-keyword filter on title/keywords fields.
  3. Tier 2 courts (superior/district courts): same browse approach,
     water-keyword filter cuts volume to manageable subset.
  4. Tier 3 tribunals: discover by name any env/water/utility/resources
     tribunal and browse their full 2016-2026 output.
  5. Try the unofficial caseSearch endpoint as a supplementary pass.
  6. Checkpoint every save; resume-safe.

Rate limits (free tier)
-----------------------
  2 req/s  -> enforce 0.6s between requests (conservative)
  5,000 req/day -> counter tracked; script warns at 4,500.

Output: canada_water_law_2016_2026.json
Format matches normalize_canada() in merge_all_countries.py.

Usage
-----
  Windows:  set CANLII_API_KEY=your_key && python canlii_scraper.py
  Linux:    CANLII_API_KEY=your_key python canlii_scraper.py
"""
import os, sys, json, re, time, urllib.request, urllib.parse
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

# ── CONFIG ────────────────────────────────────────────────────────────────────
API_KEY = os.getenv('CANLII_API_KEY', '')
if not API_KEY:
    raise SystemExit(
        '\n  ERROR: CANLII_API_KEY environment variable not set.\n'
        '  Windows: set CANLII_API_KEY=your_key_here\n'
        '  Linux:   export CANLII_API_KEY=your_key_here\n'
        '  Get a key at: https://developer.canlii.org/\n'
    )

BASE       = 'https://api.canlii.org/v1'
LANG       = 'en'
DATE_FROM  = '2016-01-01'
DATE_TO    = '2026-12-31'
YEAR_START = 2016
YEAR_END   = 2026
PAGE_SIZE  = 10_000    # CanLII max resultCount per page
MIN_SLEEP  = 0.6       # seconds between requests (safe for 2 req/s limit)
WARN_REQS  = 4_500     # warn when approaching 5,000/day limit

DL  = Path(os.environ.get('OUTPUT_DIR', r'C:\Users\junio\Downloads'))
OUT = DL / 'canada_water_law_2016_2026.json'
TMP = DL / 'canada_water_law_TEMP.json'

HDRS = {
    'User-Agent': 'research/water-law-dataset (academic use; github.com/jrklaus8/water-law-dataset)',
    'Accept': 'application/json',
}

# ── WATER LAW KEYWORDS ────────────────────────────────────────────────────────
# Matched against case title + keywords metadata.
# Covers services, contamination, rights, statutes, infrastructure, and more.
WATER_KEYWORDS = [
    # ── English: core water services ──────────────────────────────────────────
    'water supply', 'water service', 'water utility', 'water rate',
    'water meter', 'water bill', 'water connection', 'water disconnection',
    'drinking water', 'potable water', 'water treatment', 'water distribution',
    # Contamination / quality
    'water quality', 'water contamination', 'water pollution', 'water safety',
    'water standard', 'boil water', 'water advisory', 'groundwater contamination',
    # Infrastructure
    'wastewater', 'sewage', 'sewer', 'stormwater', 'storm water',
    'water main', 'water pipe', 'waterworks', 'water infrastructure',
    # Resource rights
    'water rights', 'water licence', 'water permit', 'water allocation',
    'water diversion', 'water extraction', 'water use',
    'groundwater', 'aquifer', 'well water',
    'surface water', 'watershed', 'watercourse', 'waterway',
    # Environmental protection
    'source water', 'source water protection',
    'water conservation', 'water shortage', 'drought',
    'irrigation', 'water district', 'water board',
    # Flood / dams (note: bare 'dam' handled via whole-word regex below)
    'flood', 'reservoir', 'floodplain', 'riparian', 'hydroelectric',
    # Named Canadian statutes / agencies
    'Canada Water Act', 'Safe Drinking Water', 'Clean Water Act',
    'Water Act', 'Water Resources Act', 'Water Security Agency',
    'water authority', 'Fisheries Act', 'fisheries', 'Navigation Protection',
    # Indigenous
    'Indigenous water', 'First Nations water', 'treaty water',

    # ── French: eau / services d'eau ──────────────────────────────────────────
    # (Quebec Court of Appeal cases are in French — 'water' never appears in title)
    "eau potable", "eau souterraine", "eaux usées", "eaux de surface",
    "distribution d'eau", "service d'eau", "approvisionnement en eau",
    "réseau d'eau", "alimentation en eau", "qualité de l'eau",
    "contamination de l'eau", "pollution de l'eau",
    "aqueducs", "aqueduc", "égout", "égouts", "assainissement",
    "inondation", "inondations", "barrage", "barrages",
    # NOTE: "crue" (flood) handled via whole-word regex — "crue" in "cruelty"/"McRuer" etc.
    "nappe phréatique", "cours d'eau", "bassin versant",
    "droits sur l'eau", "ressources hydriques", "ressources en eau",
    "loi sur les ressources en eau", "gestion des eaux",
    "eaux pluviales", "zone inondable", "ripicole",
    # French statutes / agencies
    "Loi sur les pêches", "pêcheries", "Loi sur la protection de la navigation",
    "Loi sur l'eau", "régie des eaux", "Office des eaux",
    # Indigenous (French)
    "droits de l'eau", "eau des Premières Nations",
]

WATER_KW_LOWER = [k.lower() for k in WATER_KEYWORDS]

# Whole-word patterns for ambiguous short terms (avoids 'dam' in 'Adam', 'random', etc.)
import re as _re
WATER_WORD_PATTERNS = [
    _re.compile(r'\bdam\b', _re.I),
    _re.compile(r'\bdams\b', _re.I),
    _re.compile(r'\blevee\b', _re.I),
    _re.compile(r'\bdike\b', _re.I),
    _re.compile(r'\bdyke\b', _re.I),
    _re.compile(r'\bcrue\b', _re.I),   # French: crue (flood/high water) — avoid "cruelty"/"McRuer"
    _re.compile(r'\bcrues\b', _re.I),  # plural
]

def is_water_case(title, keywords):
    haystack = (title + ' ' + keywords).lower()
    if any(kw in haystack for kw in WATER_KW_LOWER):
        return True
    full = title + ' ' + keywords
    return any(p.search(full) for p in WATER_WORD_PATTERNS)

# ── TRIBUNAL DISCOVERY KEYWORDS ───────────────────────────────────────────────
# Database names matching these are auto-included as Tier 3.
TRIBUNAL_KEYWORDS = [
    'environment', 'water', 'natural resource', 'energy', 'municipal',
    'drainage', 'irrigation', 'utility', 'utilities', 'conservation',
    'pollution', 'land use', 'planning', 'pipeline', 'oil and gas',
    'oil sands', 'surface rights', 'reclamation', 'fisheries',
]
TRIBUNAL_KW_LOWER = [k.lower() for k in TRIBUNAL_KEYWORDS]

def is_water_tribunal(db_name):
    name_l = db_name.lower()
    return any(k in name_l for k in TRIBUNAL_KW_LOWER)

# ── TIER 1: Always browse all cases, then keyword-filter ─────────────────────
TIER1_IDS = {
    # Federal (correct CanLII IDs — fca-caf/fct-cf are wrong, real IDs are fca/fct)
    'csc-scc': 'Supreme Court of Canada',
    'fca':     'Federal Court of Appeal',
    'fct':     'Federal Court',
    # Provincial / territorial courts of appeal
    'bcca':  'Court of Appeal for British Columbia',
    'abca':  'Court of Appeal of Alberta',
    'skca':  'Court of Appeal for Saskatchewan',
    'mbca':  'Court of Appeal of Manitoba',
    'onca':  'Court of Appeal for Ontario',
    'qcca':  'Court of Appeal of Quebec',
    'nbca':  'Court of Appeal of New Brunswick',
    'nsca':  'Nova Scotia Court of Appeal',
    'peica': 'Prince Edward Island Court of Appeal',
    'nlca':  'Court of Appeal of Newfoundland and Labrador',
    'ykca':  'Court of Appeal of Yukon',
    'nwtca': 'Court of Appeal of Northwest Territories',
    'nuca':  'Nunavut Court of Appeal',
}

# ── TIER 2: Browse + keyword filter ─────────────────────────────────────────
TIER2_IDS = {
    'bcsc':    'Supreme Court of British Columbia',
    'abkb':    "Court of King's Bench of Alberta",
    'skqb':    "Court of King's Bench for Saskatchewan",
    'mbqb':    "Court of King's Bench of Manitoba",
    'onsc':    'Superior Court of Justice (Ontario)',
    'qccs':    'Superior Court (Quebec)',
    'nbkb':    "Court of King's Bench of New Brunswick",
    'nssc':    'Supreme Court of Nova Scotia',
    'peisc':   'Supreme Court of Prince Edward Island',
    'nlsc':    'Supreme Court of Newfoundland and Labrador',
    'yksc':    'Supreme Court of Yukon',
    'nwtsc':   'Supreme Court of Northwest Territories',
    'nucj':    'Nunavut Court of Justice',
    # Federal special courts — Indigenous water rights, treaty claims
    'sct-trp': 'Specific Claims Tribunal Canada',
    'cart-crac': 'Canada Agricultural Review Tribunal',
}

# ── REQUEST COUNTER ───────────────────────────────────────────────────────────
_req_count = 0

def api_get(path, params=None):
    global _req_count
    p = {'api_key': API_KEY}
    if params:
        p.update(params)
    url = f'{BASE}{path}?' + urllib.parse.urlencode(p)
    req = urllib.request.Request(url, headers=HDRS)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.loads(r.read())
            _req_count += 1
            if _req_count == WARN_REQS:
                print(f'\n  WARNING: Approaching daily request limit ({_req_count}/5000). '
                      'Continuing — may slow down.')
            time.sleep(MIN_SLEEP)
            return data
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 30 * (attempt + 1)
                print(f'    [429] waiting {wait}s (attempt {attempt+1}/5)...', flush=True)
                time.sleep(wait)
            elif e.code == 404:
                return {}
            else:
                print(f'    [HTTP {e.code}] {path}')
                return {}
        except Exception as e:
            print(f'    [ERR] {e}')
            time.sleep(3)
    return {}

def extract_year(date_str):
    """Extract year from a date string (YYYY-MM-DD) or None."""
    if not date_str:
        return None
    m = re.match(r'(\d{4})', str(date_str))
    yr = int(m.group(1)) if m else None
    return yr if (yr and YEAR_START <= yr <= YEAR_END) else None

def year_from_citation(citation):
    """
    caseBrowse does NOT return decisionDate — extract year from citation string.
    Typical format: '2019 SCC 12 (CanLII)' or '2019 CanLII 12345 (ONSC)'
    Year is always the leading 4-digit token.
    """
    if not citation:
        return None
    m = re.match(r'(\d{4})', str(citation).strip())
    if not m:
        return None
    yr = int(m.group(1))
    return yr if YEAR_START <= yr <= YEAR_END else None

def make_case(c, db_id, db_name):
    citation = c.get('citation', '')
    # caseBrowse API does not return decisionDate; derive year from citation
    yr = year_from_citation(citation)
    # date is not in browse response either — store empty, year is enough for analysis
    return {
        'country':    'Canada',
        'source':     'CanLII',
        'tribunal':   db_id,
        'court_name': db_name,
        'citation':   citation,
        'title':      c.get('title', ''),
        'date':       c.get('decisionDate', ''),   # empty from browse; filled if doc fetched
        'year':       yr,
        'docket':     c.get('docketNumber', ''),
        'keywords':   c.get('keywords', ''),
        'url':        c.get('url', ''),
        'language':   c.get('language', 'en'),
        'snippet':    '',   # not available in browse API
    }

def browse_database(db_id, db_name, tier):
    """Fetch all 2016-2026 cases from a database. Tier 1 = include all, 2/3 = filter."""
    cases = []
    offset = 0

    while True:
        resp = api_get(f'/caseBrowse/{LANG}/{db_id}/', {
            'decisionDateAfter':  DATE_FROM,
            'decisionDateBefore': DATE_TO,
            'resultCount': PAGE_SIZE,
            'offset': offset,
        })
        if not resp:
            break

        page = resp.get('cases', [])
        if not page:
            break

        for c in page:
            # caseBrowse doesn't return decisionDate — rely on server-side date filter
            # (decisionDateAfter/decisionDateBefore params). Year comes from citation.
            title = c.get('title', '')
            kw    = c.get('keywords', '')   # often empty in browse; filter on title
            if tier >= 2 and not is_water_case(title, kw):
                continue
            cases.append(make_case(c, db_id, db_name))

        offset += PAGE_SIZE
        if len(page) < PAGE_SIZE:
            break

    return cases

# ── LOAD CHECKPOINT ───────────────────────────────────────────────────────────
if TMP.exists():
    with open(TMP, encoding='utf-8') as f:
        all_cases = json.load(f)
    seen = {c.get('citation') or c.get('url') or '' for c in all_cases}
    print(f'Resuming: {len(all_cases)} cases, {len(seen)} seen')
else:
    all_cases, seen = [], set()

def add_cases(new_cases):
    added = 0
    for c in new_cases:
        key = c.get('citation') or c.get('url') or (c['tribunal'] + c['title'])
        if key in seen:
            continue
        seen.add(key)
        all_cases.append(c)
        added += 1
    return added

def checkpoint():
    with open(TMP, 'w', encoding='utf-8') as f:
        json.dump(all_cases, f, ensure_ascii=False)

# ── PHASE 1: Discover all databases ───────────────────────────────────────────
print('=' * 60)
print('CANLII WATER LAW SCRAPER — Canada 2016-2026')
print('=' * 60)
print('\n=== Phase 1: Discovering all CanLII databases ===')

resp = api_get(f'/caseBrowse/{LANG}/')
all_dbs = {db['databaseId']: db.get('name', db['databaseId'])
           for db in resp.get('caseDatabases', [])}
print(f'  Total databases: {len(all_dbs)}')

# Tier 3: water/env tribunals discovered by name
tier3_ids = {}
for db_id, db_name in all_dbs.items():
    if db_id in TIER1_IDS or db_id in TIER2_IDS:
        continue
    if is_water_tribunal(db_name):
        tier3_ids[db_id] = db_name

print(f'  Tier 1 (CoAs + federal):     {len(TIER1_IDS)} courts')
print(f'  Tier 2 (superior courts):    {len(TIER2_IDS)} courts')
print(f'  Tier 3 (env/water tribunals): {len(tier3_ids)} tribunals discovered')
for db_id, name in sorted(tier3_ids.items()):
    print(f'    {db_id:25s}  {name}')

# ── PHASE 2: Tier 1 courts ────────────────────────────────────────────────────
print('\n=== Phase 2: Tier 1 courts (all cases, water filter) ===')
for db_id, db_name in TIER1_IDS.items():
    if db_id not in all_dbs:
        print(f'  {db_id}: not in API  — skipping')
        continue
    print(f'  {db_id:12s}', end=' ', flush=True)
    cases = browse_database(db_id, db_name, tier=1)
    water = [c for c in cases if is_water_case(c['title'], c['keywords'])]
    n = add_cases(water)
    print(f'{len(cases):>6,} total -> {len(water):>4,} water -> +{n} new  [{len(all_cases):,} total]')
    checkpoint()

# ── PHASE 3: Tier 2 superior courts ───────────────────────────────────────────
print('\n=== Phase 3: Tier 2 superior courts (water filter) ===')
for db_id, db_name in TIER2_IDS.items():
    if db_id not in all_dbs:
        print(f'  {db_id}: not in API  — skipping')
        continue
    print(f'  {db_id:12s}', end=' ', flush=True)
    cases = browse_database(db_id, db_name, tier=2)
    n = add_cases(cases)
    print(f'+{n} new  [{len(all_cases):,} total]')
    checkpoint()

# ── PHASE 4: Tier 3 tribunals ────────────────────────────────────────────────
print('\n=== Phase 4: Water/env/resource tribunals ===')
for db_id, db_name in sorted(tier3_ids.items()):
    print(f'  {db_id:30s}', end=' ', flush=True)
    cases = browse_database(db_id, db_name, tier=2)
    n = add_cases(cases)
    print(f'+{n} new  [{len(all_cases):,} total]')
    if n > 0:
        checkpoint()

# ── PHASE 5: Supplementary caseSearch (unofficial endpoint) ──────────────────
print('\n=== Phase 5: Supplementary caseSearch (unofficial) ===')
test = api_get(f'/caseSearch/{LANG}/', {'keyword': 'drinking water', 'resultCount': 1})
if 'cases' in test:
    print('  caseSearch available — supplementary keyword pass')
    for kw in WATER_KEYWORDS:
        print(f'  "{kw[:50]}"', end=' ', flush=True)
        offset = 0
        kw_new = 0
        while True:
            resp = api_get(f'/caseSearch/{LANG}/', {
                'keyword': kw, 'resultCount': 100, 'offset': offset,
            })
            page = resp.get('cases', [])
            if not page:
                break
            for c in page:
                db_id = c.get('databaseId', '')
                rec = make_case(c, db_id, all_dbs.get(db_id, db_id))
                if rec['year'] is None:
                    continue   # caseSearch does return decisionDate; skip out-of-range
                rec['source'] = 'CanLII-search'
                key = rec.get('citation') or rec.get('url')
                if key and key not in seen:
                    seen.add(key)
                    all_cases.append(rec)
                    kw_new += 1
            total = resp.get('totalCount', 0)
            offset += 100
            if offset >= total or not page:
                break
        print(f'+{kw_new}  [{len(all_cases):,} total]')
        if kw_new > 0:
            checkpoint()
else:
    print('  caseSearch not available — caseBrowse results are complete')

# ── SAVE ─────────────────────────────────────────────────────────────────────
all_cases.sort(key=lambda x: (x.get('tribunal', ''), x.get('date', '')))
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(all_cases, f, ensure_ascii=False, indent=2)
if TMP.exists():
    TMP.unlink()

print(f'\n{"=" * 60}')
print(f'DONE  —  {len(all_cases)} Canadian water law cases  (2016-2026)')
print(f'API requests made this run: {_req_count:,}')
print(f'Saved: {OUT}')

yc = Counter(c['year'] for c in all_cases if c.get('year'))
print('\nYear distribution:')
for yr in sorted(yc):
    bar = 'x' * min(yc[yr] // 5, 50)
    print(f'  {yr}: {yc[yr]:4d} {bar}')

cc = Counter(c['tribunal'] for c in all_cases)
print('\nTop 20 courts / tribunals:')
for tribunal, n in cc.most_common(20):
    name = (TIER1_IDS.get(tribunal) or TIER2_IDS.get(tribunal)
            or tier3_ids.get(tribunal, tribunal))
    print(f'  {tribunal:25s}: {n:4d}  {name[:45]}')

if all_cases:
    s = all_cases[0]
    print('\nSample case:')
    print(f'  Citation : {s.get("citation", "")}')
    print(f'  Title    : {s.get("title", "")[:80]}')
    print(f'  Date     : {s.get("date", "")}')
    print(f'  URL      : {s.get("url", "")}')
