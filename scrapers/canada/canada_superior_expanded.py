"""
CanLII — expanded keyword re-run on large superior courts
=========================================================
Targets the 10 highest-volume provincial superior courts that are most
likely to contain water law decisions missed by the title-only keyword filter.

Expanded keyword set adds:
  - Riparian / property water law terms
  - Drainage / stormwater / flooding (tort)
  - Provincial water statutes by name
  - Aquatic environment / wetland
  - Additional French terms for Quebec

Output: canada_superior_expanded_2016_2026.json
Deduplicates against all 3 existing Canada JSON files.
"""
import os, sys, json, re, time, urllib.request, urllib.parse
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

API_KEY = os.getenv('CANLII_API_KEY', '')
if not API_KEY:
    raise SystemExit('ERROR: set CANLII_API_KEY')

BASE      = 'https://api.canlii.org/v1'
LANG      = 'en'
DATE_FROM = '2016-01-01'
DATE_TO   = '2026-12-31'
PAGE_SIZE = 10_000
MIN_SLEEP = 0.65
DL        = Path(os.environ.get('OUTPUT_DIR', r'C:\Users\junio\Downloads'))
OUT       = DL / 'canada_superior_expanded_2016_2026.json'

HDRS = {
    'User-Agent': 'research/water-law-dataset (academic; github.com/jrklaus8/water-law-dataset)',
    'Accept': 'application/json',
}

# ── Target courts (highest-volume superior courts) ────────────────────────────
TARGET_COURTS = {
    'onsc':  'Superior Court of Justice (Ontario)',
    'bcsc':  'Supreme Court of British Columbia',
    'abkb':  "Court of King's Bench of Alberta",
    'qccs':  'Superior Court (Quebec)',
    'nssc':  'Supreme Court of Nova Scotia',
    'nlsc':  'Supreme Court of Newfoundland and Labrador',
    'nbkb':  "Court of King's Bench of New Brunswick",
    'skqb':  "Court of King's Bench for Saskatchewan",
    'mbqb':  "Court of King's Bench of Manitoba",
    'peisc': 'Supreme Court of Prince Edward Island',
    # Courts of appeal — re-run for any missed French/expanded terms
    'qcca':  'Court of Appeal of Quebec',
    'onca':  'Court of Appeal for Ontario',
    'bcca':  'Court of Appeal for British Columbia',
}

# ── Expanded keyword set ──────────────────────────────────────────────────────
WATER_KEYWORDS = [
    # Core water services (existing)
    'water supply', 'water service', 'water utility', 'water rate',
    'water meter', 'water bill', 'water connection', 'water disconnection',
    'drinking water', 'potable water', 'water treatment', 'water distribution',
    'water quality', 'water contamination', 'water pollution', 'water safety',
    'water standard', 'boil water', 'water advisory', 'groundwater contamination',
    'wastewater', 'sewage', 'sewer', 'stormwater', 'storm water',
    'water main', 'water pipe', 'waterworks', 'water infrastructure',
    'water rights', 'water licence', 'water permit', 'water allocation',
    'water diversion', 'water extraction', 'water use',
    'groundwater', 'aquifer', 'well water',
    'surface water', 'watershed', 'watercourse', 'waterway',
    'source water', 'water conservation', 'water shortage', 'drought',
    'irrigation', 'water district', 'water board',
    'flood', 'reservoir', 'floodplain', 'riparian', 'hydroelectric',
    'Canada Water Act', 'Safe Drinking Water', 'Clean Water Act',
    'Water Act', 'Water Resources Act', 'water authority',
    'Fisheries Act', 'fisheries', 'Navigation Protection',
    'Indigenous water', 'First Nations water', 'treaty water',

    # ── NEW: Riparian / property water law ────────────────────────────────────
    'riparian rights', 'riparian owner', 'riparian property',
    'water damage', 'flood damage', 'flooding damage', 'water intrusion',
    'water ingress', 'water seepage', 'water runoff', 'surface runoff',
    'water easement', 'water access', 'water frontage', 'waterfront',
    'shoreline', 'lakeshore', 'lakefront', 'lake shore',
    'navigable water', 'navigable waterway',
    'tidal water', 'tidal flat', 'tidal zone',

    # ── NEW: Drainage / stormwater / municipal ────────────────────────────────
    'drainage', 'drainage works', 'drainage system', 'municipal drain',
    'tile drain', 'Drainage Act', 'drain commissioner',
    'detention pond', 'retention pond', 'stormwater management',
    'stormwater pond', 'stormwater runoff',
    'municipal water', 'municipal waterworks', 'water works',
    'water bylaw', 'water regulation', 'water system',
    'water infrastructure', 'water treatment plant',

    # ── NEW: Provincial water statutes ────────────────────────────────────────
    'Ontario Water Resources Act', 'Clean Water Act',
    'BC Water Sustainability Act', 'Water Sustainability Act',
    'Alberta Water Act', 'Water Act Alberta',
    'Saskatchewan Water Security Agency',
    'Manitoba Water Rights Act', 'Water Rights Act',
    'Nova Scotia Water Act',
    'Newfoundland Water Resources Act',
    'New Brunswick Clean Water Act',

    # ── NEW: Aquatic / environmental ──────────────────────────────────────────
    'wetland', 'wetlands', 'wet land', 'marshland',
    'aquatic habitat', 'aquatic environment', 'aquatic species',
    'fish habitat', 'fish passage', 'fish kill', 'fishery',
    'lake', 'river', 'stream', 'creek', 'pond', 'marsh', 'swamp',
    'water table', 'water level', 'water flow', 'water body',
    'water taking', 'water withdrawal', 'water well',

    # ── NEW: Indigenous water rights (expanded) ────────────────────────────────
    'drinking water advisory', 'long-term drinking water advisory',
    'water on reserve', 'reserve water', 'water system on reserve',

    # ── French: existing ──────────────────────────────────────────────────────
    "eau potable", "eau souterraine", "eaux usées", "eaux de surface",
    "distribution d'eau", "service d'eau", "approvisionnement en eau",
    "réseau d'eau", "alimentation en eau", "qualité de l'eau",
    "contamination de l'eau", "pollution de l'eau",
    "aqueducs", "aqueduc", "égout", "égouts", "assainissement",
    "inondation", "inondations", "barrage", "barrages",
    "nappe phréatique", "cours d'eau", "bassin versant",
    "droits sur l'eau", "ressources hydriques", "ressources en eau",
    "eaux pluviales", "zone inondable", "ripicole",
    "Loi sur les pêches", "pêcheries", "Loi sur la protection de la navigation",
    "Loi sur l'eau", "régie des eaux",

    # ── NEW French: property / drainage / environment ─────────────────────────
    "droit riverain", "riverain", "dommages causés par l'eau",
    "dommages d'inondation", "infiltration d'eau", "ruissellement",
    "fossé de drainage", "drain municipal", "gestion des eaux pluviales",
    "bassin de rétention", "milieu humide", "milieux humides", "marais",
    "habitat aquatique", "espèce aquatique", "milieu aquatique",
    "lac", "rivière", "ruisseau", "étang",
    "Loi sur la qualité de l'environnement", "évaluation environnementale",
    "eau des Premières Nations", "réserve d'eau",
    "droit d'accès à l'eau", "accès à l'eau potable",
    "plan d'eau", "voie navigable",
]

WATER_KW_LOWER = [k.lower() for k in WATER_KEYWORDS]

WORD_PATTERNS = [
    re.compile(r'\bdam\b', re.I),   re.compile(r'\bdams\b', re.I),
    re.compile(r'\blevee\b', re.I), re.compile(r'\bdike\b', re.I),
    re.compile(r'\bdyke\b', re.I),  re.compile(r'\bcrue[s]?\b', re.I),
    re.compile(r'\bdrainage\b', re.I),  # covered as substring too but just in case
]

def is_water(title, kw=''):
    h = (title + ' ' + kw).lower()
    if any(k in h for k in WATER_KW_LOWER):
        return True
    return any(p.search(title + ' ' + kw) for p in WORD_PATTERNS)

# ── Load existing cases for deduplication ────────────────────────────────────
seen = set()
total_loaded = 0
for fname in [
    'canada_water_law_2016_2026.json',
    'canada_canlii_extra_2016_2026.json',
    'canada_ldh_2016_2026.json',
]:
    fpath = DL / fname
    if not fpath.exists():
        continue
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    for c in data:
        uid = (c.get('citation') or c.get('case_id') or c.get('url') or '').strip().lower()
        if uid:
            seen.add(uid)
    total_loaded += len(data)
print(f'Loaded {total_loaded} existing cases for dedup ({len(seen)} unique IDs)')

# ── API helper ────────────────────────────────────────────────────────────────
_req = 0
def api_get(path, params=None):
    global _req
    p = {'api_key': API_KEY}
    if params:
        p.update(params)
    url = f'{BASE}{path}?' + urllib.parse.urlencode(p)
    req = urllib.request.Request(url, headers=HDRS)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.loads(r.read())
            _req += 1
            time.sleep(MIN_SLEEP)
            return data
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 30 * (attempt + 1)
                print(f'  [429] sleeping {wait}s...', flush=True)
                time.sleep(wait)
            elif e.code == 404:
                return {}
            else:
                print(f'  [HTTP {e.code}] {path}', flush=True)
                return {}
        except Exception as e:
            print(f'  [ERR] {e}', flush=True)
            time.sleep(3)
    return {}

def year_from_citation(cit):
    if not cit:
        return None
    m = re.match(r'(\d{4})', str(cit).strip())
    if not m:
        return None
    yr = int(m.group(1))
    return yr if 2016 <= yr <= 2026 else None

# ── Main loop ─────────────────────────────────────────────────────────────────
all_new = []
print('\n' + '='*60)
print('CanLII expanded keyword re-run — large superior courts')
print('='*60)

for db_id, db_name in TARGET_COURTS.items():
    print(f'\n--- {db_id}: {db_name} ---', flush=True)
    court_new = 0
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
            title = c.get('title', '')
            kw    = c.get('keywords', '')
            if not is_water(title, kw):
                continue
            citation = c.get('citation', '')
            yr = year_from_citation(citation)
            if not yr:
                continue
            uid = (citation or c.get('url', '')).strip().lower()
            if uid and uid in seen:
                continue
            if uid:
                seen.add(uid)
            all_new.append({
                'country':    'Canada',
                'source':     'CanLII',
                'tribunal':   db_id,
                'court_name': db_name,
                'citation':   citation,
                'title':      title,
                'date':       '',
                'year':       yr,
                'docket':     c.get('docketNumber', ''),
                'keywords':   kw,
                'url':        c.get('url', ''),
                'language':   c.get('language', 'en'),
                'snippet':    '',
            })
            court_new += 1

        print(f'  offset {offset:>6,} — page {len(page):,} — running new: {court_new}', flush=True)
        if len(page) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    print(f'  → {court_new} new cases for {db_id}', flush=True)

# ── Save ──────────────────────────────────────────────────────────────────────
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(all_new, f, ensure_ascii=False, indent=2)

print(f'\n{"="*60}')
print(f'DONE — {len(all_new)} new cases from expanded superior court run')
print(f'API requests: {_req:,}')
print(f'Saved: {OUT}')

yc = Counter(c['year'] for c in all_new if c.get('year'))
print('\nYear distribution:')
for yr in sorted(yc):
    print(f'  {yr}: {yc[yr]:4d}')

cc = Counter(c['tribunal'] for c in all_new)
print('\nBy court:')
for court, n in cc.most_common():
    print(f'  {court:<10} {n:4d}  {TARGET_COURTS.get(court,"")}')
