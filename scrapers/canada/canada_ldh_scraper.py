"""
Canada water law — Legal Data Hunter + CanLII expansion
=======================================================
Two-pass strategy:
  Pass 1 — LDH: semantic+keyword search across all CA sources
  Pass 2 — CanLII: browse remaining databases not yet covered

Output: canada_ldh_2016_2026.json (LDH cases only, deduped against CanLII)
        canada_canlii_extra_2016_2026.json (extra CanLII cases)

Both files use same schema as canada_water_law_2016_2026.json.
"""
import os, sys, json, re, time, urllib.request, urllib.parse
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')

# ── Config ────────────────────────────────────────────────────────────────────
LDH_KEY  = os.getenv('LDH_API_KEY', '')  # set LDH_API_KEY env var
LDH_URL  = 'https://legaldatahunter.com/mcp'

CANLII_KEY = os.getenv('CANLII_API_KEY', '')
CANLII_BASE = 'https://api.canlii.org/v1'

YEAR_START, YEAR_END = 2016, 2026
DL  = Path(os.environ.get('OUTPUT_DIR', r'C:\Users\junio\Downloads'))
OUT_LDH    = DL / 'canada_ldh_2016_2026.json'
OUT_EXTRA  = DL / 'canada_canlii_extra_2016_2026.json'

# Load existing CanLII cases for deduplication
EXISTING_FILE = DL / 'canada_water_law_2016_2026.json'
existing_ids = set()
if EXISTING_FILE.exists():
    with open(EXISTING_FILE, encoding='utf-8') as f:
        for c in json.load(f):
            cid = c.get('case_id') or c.get('citation','')
            if cid:
                existing_ids.add(cid.strip().lower())
    print(f'Loaded {len(existing_ids)} existing CanLII case IDs for dedup')

HDRS_LDH = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {LDH_KEY}',
    'Accept': 'application/json, text/event-stream',  # LDH requires both
}

# ── Water queries for LDH ─────────────────────────────────────────────────────
WATER_QUERIES = [
    # English
    'water supply connection service utility',
    'drinking water potable water quality',
    'wastewater sewage treatment stormwater',
    'groundwater aquifer contamination',
    'water rights licence permit allocation',
    'flood floodplain dam reservoir',
    'irrigation water district board',
    'Fisheries Act fisheries habitat',
    'Safe Drinking Water Act water standard',
    'Indigenous First Nations water rights',
    'water infrastructure municipal water rate',
    'environmental assessment water impact',
    'Clean Water Act source water protection',
    # French
    'eau potable distribution aqueduc égout',
    'inondation barrage cours d eau ressources hydriques',
    'Loi sur les pêches pêcheries eau souterraine',
]

def ldh_raw(method, params):
    """Low-level LDH JSON-RPC call — returns parsed SSE data or raises."""
    body = json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}).encode('utf-8')
    req = urllib.request.Request(LDH_URL, data=body, headers=HDRS_LDH, method='POST')
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read().decode('utf-8', errors='replace')
    for line in reversed(raw.split('\n')):
        if line.startswith('data: ') and line[6:] != '[DONE]':
            payload = json.loads(line[6:])
            text = payload.get('result', {}).get('content', [{}])[0].get('text', '{}')
            return json.loads(text)
    return {}

def ldh_init():
    """MCP initialize handshake — required before any tool calls."""
    ldh_raw('initialize', {
        'protocolVersion': '2024-11-05',
        'capabilities': {},
        'clientInfo': {'name': 'research', 'version': '1.0'},
    })
    time.sleep(2)

def ldh_call(tool, arguments, retries=4):
    """Call an LDH tool with exponential backoff on 429/5xx."""
    for attempt in range(retries):
        try:
            return ldh_raw('tools/call', {'name': tool, 'arguments': arguments})
        except Exception as e:
            code = getattr(e, 'code', 0)
            wait = 60 * (attempt + 1)  # 60s, 120s, 180s, 240s
            print(f'  LDH err (attempt {attempt+1}, HTTP {code}): {e} — waiting {wait}s', flush=True)
            time.sleep(wait)
            if attempt == 0:
                ldh_init()  # re-initialize after first failure
    return {}

def year_from_text(text):
    """Extract year from a citation or date string."""
    if not text:
        return None
    m = re.search(r'\b(201[6-9]|202[0-6])\b', str(text))
    return int(m.group(1)) if m else None

def normalize_ldh(hit, source):
    """Normalize an LDH hit to the project schema."""
    meta = hit.get('metadata', {})
    title = meta.get('title') or hit.get('title', '')
    date  = meta.get('date') or meta.get('decision_date', '')
    yr    = year_from_text(date) or year_from_text(meta.get('citation','')) or year_from_text(title)
    cid   = meta.get('citation') or meta.get('source_id') or hit.get('id', '')
    url   = meta.get('url') or meta.get('source_url', '')
    court = meta.get('court') or meta.get('tribunal') or source
    return {
        'country':    'Canada',
        'source':     'LDH',
        'tribunal':   court,
        'court_name': court,
        'case_id':    cid,
        'title':      title,
        'date':       date,
        'year':       yr,
        'docket':     meta.get('docket', ''),
        'keywords':   meta.get('keywords', ''),
        'url':        url,
        'language':   meta.get('language', 'en'),
        'snippet':    hit.get('text', '')[:500],
        'ldh_score':  hit.get('score', 0),
        '_ldh_source': source,
    }

# ══════════════════════════════════════════════════════════════════════════════
# PASS 1 — LDH
# ══════════════════════════════════════════════════════════════════════════════
print('\n' + '='*60, flush=True)
print('PASS 1 — Legal Data Hunter (CA sources)', flush=True)
print('='*60, flush=True)

# MCP initialize — required before any tool calls
print('\nInitializing LDH connection...', flush=True)
ldh_init()

# Discover all CA sources
print('--- Discovering CA sources ---', flush=True)
result = ldh_call('discover_sources', {'country_code': 'CA'})
ca_sources = ['CA/A2AJ']  # always include primary source
if result:
    raw_text = str(result)
    namespaces = list(dict.fromkeys(re.findall(r'CA/[\w]+', raw_text)))
    if namespaces:
        ca_sources = namespaces
        print(f'  Found namespaces: {namespaces}', flush=True)
    else:
        print(f'  Fallback to: {ca_sources}', flush=True)
else:
    print(f'  Fallback to: {ca_sources}', flush=True)

if 'CA/A2AJ' not in ca_sources:
    ca_sources.insert(0, 'CA/A2AJ')

print(f'\nSources to search: {ca_sources}', flush=True)

ldh_cases = []
seen_ids = set(existing_ids)  # start with existing CanLII IDs

for source in ca_sources:
    print(f'\n--- Searching {source} ---')
    source_hits = []
    for i, query in enumerate(WATER_QUERIES):
        print(f'  [{i+1}/{len(WATER_QUERIES)}] "{query[:50]}"')
        args = {
            'query':   query,
            'country': ['CA'],
            'top_k':   100,
            'alpha':   0.5,
        }
        if source:
            args['namespace'] = source
        result = ldh_call('search', args)

        hits = []
        if isinstance(result, dict):
            hits = result.get('results', result.get('hits', []))
            if not hits and 'matches' in result:
                hits = result['matches']
        elif isinstance(result, list):
            hits = result

        new_this_query = 0
        for hit in hits:
            norm = normalize_ldh(hit, source)
            yr = norm.get('year')
            if yr and not (YEAR_START <= yr <= YEAR_END):
                continue
            # Dedup by case_id or title
            uid = (norm.get('case_id') or norm.get('title', '')).strip().lower()
            if uid and uid not in seen_ids:
                seen_ids.add(uid)
                source_hits.append(norm)
                new_this_query += 1

        print(f'    → {len(hits)} hits, {new_this_query} new in-range', flush=True)
        time.sleep(60)  # LDH rate limit: very aggressive, 60s gap

    ldh_cases.extend(source_hits)
    print(f'  {source} total new: {len(source_hits)}')

print(f'\nLDH total: {len(ldh_cases)} new Canadian water law cases (2016-2026)')

# Save LDH results
with open(OUT_LDH, 'w', encoding='utf-8') as f:
    json.dump(ldh_cases, f, ensure_ascii=False, indent=2)
print(f'Saved: {OUT_LDH}')

# ══════════════════════════════════════════════════════════════════════════════
# PASS 2 — CanLII extra databases
# ══════════════════════════════════════════════════════════════════════════════
if not CANLII_KEY:
    print('\nNo CANLII_API_KEY — skipping Pass 2')
    sys.exit(0)

print('\n' + '='*60)
print('PASS 2 — CanLII extra databases')
print('='*60)

CANLII_HDRS = {
    'User-Agent': 'research/water-law-dataset (academic; github.com/jrklaus8/water-law-dataset)',
    'Accept': 'application/json',
}

# Already-covered database IDs from the main scraper
ALREADY_COVERED = {
    # Tier 1
    'csc-scc','fca','fct','bcca','abca','skca','mbca','onca','qcca',
    'nbca','nsca','peica','nlca','ykca','nwtca','nuca',
    # Tier 2
    'bcsc','abkb','skqb','mbqb','onsc','qccs','nbkb','nssc','peisc',
    'nlsc','yksc','nwtsc','nucj','sct-trp','cart-crac',
    # Tier 3 discovered
    'abaer','abeab','abmgb','absrb','bceab','bcogat','cer-rec','eptc',
    'fpca','nbapab','nbeub','nsuarb','onconrb','ondr','onert','onmb',
    'onmic','onoeb','qccm','qccmnq','skmbr','sksmb','sopf',
}

# Water-relevant keywords for discovering extra databases
EXTRA_DB_KEYWORDS = [
    'water', 'drainage', 'irrigation', 'watershed', 'aquifer',
    'flood', 'fisheries', 'fish', 'wetland', 'riparian',
    'sanitation', 'sewage', 'utility', 'utilities',
    'resource', 'environment', 'environmental', 'ecology',
    'conservation', 'municipal', 'land', 'agriculture',
    'mining', 'pipeline', 'petroleum', 'energy',
]

def canlii_get(url, sleep=0.6):
    url_with_key = url + ('&' if '?' in url else '?') + f'api_key={CANLII_KEY}'
    try:
        req = urllib.request.Request(url_with_key, headers=CANLII_HDRS)
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        return None

def year_from_citation(citation):
    if not citation: return None
    m = re.match(r'(\d{4})', str(citation).strip())
    if not m: return None
    yr = int(m.group(1))
    return yr if YEAR_START <= yr <= YEAR_END else None

import re as _re
WATER_KEYWORDS_CA = [
    'water supply','water service','water utility','water rate','water meter',
    'drinking water','potable water','water treatment','water distribution',
    'water quality','water contamination','groundwater contamination',
    'wastewater','sewage','sewer','stormwater','storm water',
    'water rights','water licence','water permit','water allocation',
    'water diversion','groundwater','aquifer','well water',
    'surface water','watershed','watercourse','waterway',
    'water conservation','drought','irrigation','water district','water board',
    'flood','reservoir','floodplain','riparian','hydroelectric',
    'Canada Water Act','Safe Drinking Water','Fisheries Act','fisheries',
    'Navigation Protection','Indigenous water','First Nations water',
    'eau potable','eaux usées','aqueduc','égout','inondation',
    "cours d'eau",'Loi sur les pêches',
]
WATER_KW_LOWER = [k.lower() for k in WATER_KEYWORDS_CA]
WORD_PATTERNS = [
    _re.compile(r'\bdam\b',_re.I), _re.compile(r'\bdams\b',_re.I),
    _re.compile(r'\blevee\b',_re.I), _re.compile(r'\bdike\b',_re.I),
    _re.compile(r'\bdyke\b',_re.I), _re.compile(r'\bcrue[s]?\b',_re.I),
]

def is_water(title):
    h = title.lower()
    if any(kw in h for kw in WATER_KW_LOWER): return True
    return any(p.search(title) for p in WORD_PATTERNS)

# Get all databases
print('\nFetching all CanLII databases...')
data = canlii_get(f'{CANLII_BASE}/caseBrowse/en/')
time.sleep(0.6)
if not data:
    print('  ERROR fetching database list')
    sys.exit(1)

all_dbs = data.get('databases', [])
print(f'  Total databases: {len(all_dbs)}')

# Find uncovered water-relevant databases
extra_dbs = []
for db in all_dbs:
    db_id = db.get('databaseId', '')
    name  = db.get('name', '').lower()
    if db_id in ALREADY_COVERED:
        continue
    if any(kw in name for kw in EXTRA_DB_KEYWORDS):
        extra_dbs.append(db)

print(f'  Extra relevant databases not yet browsed: {len(extra_dbs)}')
for db in extra_dbs[:30]:
    print(f'    {db["databaseId"]:<20} {db.get("name","")[:50]}')

extra_cases = []
seen_extra = set(seen_ids)

for db in extra_dbs:
    db_id   = db['databaseId']
    db_name = db.get('name', db_id)
    cases_found = 0
    offset = 0

    while True:
        url = f'{CANLII_BASE}/caseBrowse/en/{db_id}/?offset={offset}&resultCount=10000'
        resp = canlii_get(url)
        time.sleep(0.6)
        if not resp:
            break
        batch = resp.get('cases', [])
        if not batch:
            break

        for c in batch:
            title    = c.get('title', '')
            citation = c.get('citation', '')
            yr = year_from_citation(citation)
            if not yr:
                continue
            if not is_water(title):
                continue
            uid = citation.strip().lower()
            if uid in seen_extra:
                continue
            seen_extra.add(uid)
            extra_cases.append({
                'country':    'Canada',
                'source':     'CanLII',
                'tribunal':   db_id,
                'court_name': db_name,
                'case_id':    c.get('caseId', ''),
                'title':      title,
                'date':       '',
                'year':       yr,
                'docket':     '',
                'keywords':   '',
                'url':        f'https://www.canlii.org/en/{db_id}/{c.get("caseId","")}/doc.html',
                'language':   'en',
                'snippet':    '',
                'citation':   citation,
            })
            cases_found += 1

        if len(batch) < 10000:
            break
        offset += 10000

    if cases_found:
        print(f'  {db_id:<20} +{cases_found} water cases')

print(f'\nCanLII extra total: {len(extra_cases)} new cases')
with open(OUT_EXTRA, 'w', encoding='utf-8') as f:
    json.dump(extra_cases, f, ensure_ascii=False, indent=2)
print(f'Saved: {OUT_EXTRA}')

# ── Summary ───────────────────────────────────────────────────────────────────
print('\n' + '='*60)
print('DONE')
print(f'  LDH cases:          {len(ldh_cases)}')
print(f'  CanLII extra cases: {len(extra_cases)}')
print(f'  Combined new:       {len(ldh_cases) + len(extra_cases)}')
print('='*60)
