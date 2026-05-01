"""
Canada CanLII extra databases — browse all 409 databases not yet covered.
Standalone script (no LDH dependency).
Output: canada_canlii_extra_2016_2026.json
"""
import os, sys, json, re, time, urllib.request, urllib.parse
from pathlib import Path
from collections import Counter
import re as _re

sys.stdout.reconfigure(encoding='utf-8')

CANLII_KEY  = os.getenv('CANLII_API_KEY', '')
CANLII_BASE = 'https://api.canlii.org/v1'
YEAR_START, YEAR_END = 2016, 2026
DL  = Path(os.environ.get('OUTPUT_DIR', r'C:\Users\junio\Downloads'))
OUT = DL / 'canada_canlii_extra_2016_2026.json'

if not CANLII_KEY:
    raise SystemExit('Set CANLII_API_KEY env var')

HDRS = {
    'User-Agent': 'research/water-law-dataset (academic; github.com/jrklaus8/water-law-dataset)',
    'Accept': 'application/json',
}

# Databases already covered by the main canlii_scraper.py
ALREADY_COVERED = {
    'csc-scc','fca','fct','bcca','abca','skca','mbca','onca','qcca',
    'nbca','nsca','peica','nlca','ykca','nwtca','nuca',
    'bcsc','abkb','skqb','mbqb','onsc','qccs','nbkb','nssc','peisc',
    'nlsc','yksc','nwtsc','nucj','sct-trp','cart-crac',
    'abaer','abeab','abmgb','absrb','bceab','bcogat','cer-rec','eptc',
    'fpca','nbapab','nbeub','nsuarb','onconrb','ondr','onert','onmb',
    'onmic','onoeb','qccm','qccmnq','skmbr','sksmb','sopf',
}

# Keywords for discovering extra relevant databases
EXTRA_DB_KEYWORDS = [
    'water','drainage','irrigation','watershed','aquifer','flood',
    'fisheries','fish','wetland','riparian','sanitation','sewage',
    'utility','utilities','resource','environment','environmental',
    'ecology','conservation','municipal','land','agriculture',
    'mining','pipeline','petroleum','energy','tribunal',
    'appeal','review','planning','assessment',
]

# Water keyword filter (same as main scraper, without 'crue' substring issue)
WATER_KW_LOWER = [k.lower() for k in [
    'water supply','water service','water utility','water rate',
    'water meter','water bill','water connection','water disconnection',
    'drinking water','potable water','water treatment','water distribution',
    'water quality','water contamination','water pollution','water safety',
    'water standard','boil water','water advisory','groundwater contamination',
    'wastewater','sewage','sewer','stormwater','storm water',
    'water main','water pipe','waterworks','water infrastructure',
    'water rights','water licence','water permit','water allocation',
    'water diversion','water extraction','water use',
    'groundwater','aquifer','well water',
    'surface water','watershed','watercourse','waterway',
    'source water','source water protection',
    'water conservation','water shortage','drought',
    'irrigation','water district','water board',
    'flood','reservoir','floodplain','riparian','hydroelectric',
    'Canada Water Act','Safe Drinking Water','Clean Water Act',
    'Water Act','Water Resources Act','Water Security Agency',
    'water authority','Fisheries Act','fisheries','Navigation Protection',
    'Indigenous water','First Nations water','treaty water',
    'eau potable','eau souterraine','eaux usées','eaux de surface',
    "distribution d'eau","service d'eau",'approvisionnement en eau',
    "réseau d'eau",'alimentation en eau',"qualité de l'eau",
    "contamination de l'eau","pollution de l'eau",
    'aqueducs','aqueduc','égout','égouts','assainissement',
    'inondation','inondations','barrage','barrages',
    'nappe phréatique',"cours d'eau",'bassin versant',
    "droits sur l'eau",'ressources hydriques','ressources en eau',
    'gestion des eaux','eaux pluviales','zone inondable',
    'Loi sur les pêches','pêcheries',
]]

WORD_PATTERNS = [
    _re.compile(r'\bdam\b',_re.I), _re.compile(r'\bdams\b',_re.I),
    _re.compile(r'\blevee\b',_re.I), _re.compile(r'\bdike\b',_re.I),
    _re.compile(r'\bdyke\b',_re.I), _re.compile(r'\bcrue[s]?\b',_re.I),
]

# Load existing cases for dedup
existing_ids = set()
for fname in ['canada_water_law_2016_2026.json']:
    fp = DL / fname
    if fp.exists():
        with open(fp, encoding='utf-8') as f:
            for c in json.load(f):
                cid = (c.get('case_id') or c.get('citation','')).strip().lower()
                if cid: existing_ids.add(cid)
print(f'Loaded {len(existing_ids)} existing case IDs for dedup')

def canlii_get(url):
    url_key = url + ('&' if '?' in url else '?') + f'api_key={CANLII_KEY}'
    try:
        req = urllib.request.Request(url_key, headers=HDRS)
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

def is_water(title):
    h = title.lower()
    if any(kw in h for kw in WATER_KW_LOWER): return True
    return any(p.search(title) for p in WORD_PATTERNS)

# ── Fetch all databases ───────────────────────────────────────────────────────
print('\nFetching all CanLII databases...')
data = canlii_get(f'{CANLII_BASE}/caseBrowse/en/')
time.sleep(0.7)
if not data:
    raise SystemExit('ERROR: Could not fetch database list')

all_dbs = data.get('caseDatabases', data.get('databases', []))
print(f'Total databases: {len(all_dbs)}')

extra_dbs = []
for db in all_dbs:
    db_id = db.get('databaseId', '')
    name  = db.get('name', '').lower()
    if db_id in ALREADY_COVERED:
        continue
    if any(kw in name for kw in EXTRA_DB_KEYWORDS):
        extra_dbs.append(db)

print(f'Extra relevant databases: {len(extra_dbs)}')
for db in extra_dbs:
    print(f'  {db["databaseId"]:<22} {db.get("name","")[:55]}')

# ── Browse each extra database ────────────────────────────────────────────────
extra_cases = []
seen = set(existing_ids)
req_count = 0

for db in extra_dbs:
    db_id   = db['databaseId']
    db_name = db.get('name', db_id)
    found   = 0
    offset  = 0

    while True:
        url = f'{CANLII_BASE}/caseBrowse/en/{db_id}/?offset={offset}&resultCount=10000'
        resp = canlii_get(url)
        req_count += 1
        time.sleep(0.7)

        if req_count >= 4500:
            print('WARNING: approaching CanLII daily limit (4500 req)')
            break

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
            if uid in seen:
                continue
            seen.add(uid)
            found += 1
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

        if len(batch) < 10000:
            break
        offset += 10000

    if found:
        print(f'  {db_id:<22} +{found} water cases', flush=True)

# ── Save ──────────────────────────────────────────────────────────────────────
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(extra_cases, f, ensure_ascii=False, indent=2)

print(f'\n{"="*60}')
print(f'DONE — {len(extra_cases)} extra Canadian water law cases (2016-2026)')
print(f'Saved: {OUT}')

if extra_cases:
    years = Counter(c['year'] for c in extra_cases)
    print('\nYear distribution:')
    for yr in sorted(years):
        print(f'  {yr}: {years[yr]:4d} {"x"*(years[yr]//2)}')
    courts = Counter(c['tribunal'] for c in extra_cases)
    print('\nTop courts:')
    for court, n in courts.most_common(15):
        print(f'  {court:<22} {n}')
print('='*60)
