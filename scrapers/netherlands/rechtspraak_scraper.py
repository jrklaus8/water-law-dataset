"""
Rechtspraak.nl (Netherlands) water law scraper.
Open Data API — no auth required.
Strategy:
  1. Enumerate all Raad van State + CBb ECLIs via creator feed filter (fast)
  2. Parse year from ECLI string → keep only 2016-2026
  3. Fetch content XML for each → parse inhoudsindicatie, rechtsgebied, date
  4. Filter for water-related terms
  5. Save to JSON

Estimated runtime: ~2 hours for ~35k content fetches at 5 req/s
"""
import os
import urllib.request, urllib.parse, ssl, sys, re, json, time
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDRS = {'User-Agent': 'research/water-law-dataset (academic use; contact your-email@example.com)'}

FEED_URL    = 'https://data.rechtspraak.nl/uitspraken/zoeken'
CONTENT_URL = 'https://data.rechtspraak.nl/uitspraken/content'

YEAR_START = 2016
YEAR_END   = 2026

# Courts to enumerate (use full OWMS URI)
TARGET_CREATORS = {
    'RvS': 'http://standaarden.overheid.nl/owms/terms/Raad_van_State',
    'CBb': 'http://standaarden.overheid.nl/owms/terms/College_van_Beroep_voor_het_bedrijfsleven',
}

# Water law keywords (Dutch) — checked against inhoudsindicatie + rechtsgebied
WATER_TERMS = [
    'water', 'drinkwater', 'watervergunning', 'waterbeheer', 'waterhuishouding',
    'waterschap', 'waterschapsheffing', 'waterschapsbelasting', 'waterzuivering',
    'afvalwater', 'grondwater', 'oppervlaktewater', 'hemelwater', 'rioolwater',
    'waterkering', 'overstroming', 'wateroverlast', 'riolering', 'zuivering',
    'waterwet', 'drinkwaterwet', 'waterschapswet', 'watervoorziening',
    'waterverontreiniging', 'watervervuiling', 'wateronttrekking',
    'waterkwaliteit', 'waterstand',
]

# Rechtsgebied URIs that relate to water/environment (partial match)
WATER_RECHTSGEBIED = [
    'omgevingsrecht', 'milieurecht', 'waterrecht',
]

DL = Path(os.getenv('OUTPUT_DIR', '.'))
OUT_FILE    = DL / 'netherlands_water_law_2016_2026.json'
TEMP_FILE   = DL / 'netherlands_water_law_TEMP.json'  # checkpoint

def feed_get(params):
    url = FEED_URL + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
        return r.read().decode('utf-8', errors='replace')

def content_get(ecli):
    url = CONTENT_URL + '?id=' + urllib.parse.quote(ecli)
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
        return r.read().decode('utf-8', errors='replace')

def parse_ecli_year(ecli):
    """ECLI:NL:RVS:2020:1234 → 2020"""
    m = re.match(r'ECLI:NL:\w+:(\d{4}):', ecli)
    return int(m.group(1)) if m else None

def parse_content(xml_body):
    """Extract key fields from content XML."""
    def rx(pattern, body=xml_body):
        m = re.search(pattern, body, re.DOTALL | re.IGNORECASE)
        return m.group(1).strip() if m else ''

    date     = rx(r'dcterms:date[^>]*Uitspraakdatum[^>]*>(\d{4}-\d{2}-\d{2})<')
    zaak     = rx(r'psi:zaaknummer[^>]*>([^<]+)<')
    court    = rx(r'dcterms:creator[^>]*rdfs:label="Instantie"[^>]*>([^<]+)<')
    if not court:
        court = rx(r'<dcterms:creator[^>]*>([^<]+)</dcterms:creator>')
    rechtsgebied = rx(r'dcterms:subject[^>]*Rechtsgebied[^>]*>([^<]+)<')
    if not rechtsgebied:
        rechtsgebied = rx(r'resourceIdentifier="([^"]*rechtsgebied[^"]*)"')
    procedure = rx(r'psi:procedure[^>]*rdfs:label="Procedure"[^>]*>([^<]+)<')
    if not procedure:
        procedure = rx(r'psi:procedure[^>]*>([^<]+)<')

    # inhoudsindicatie — remove XML tags inside
    inhoud_raw = rx(r'<inhoudsindicatie[^>]*>(.*?)</inhoudsindicatie>')
    inhoud = re.sub(r'<[^>]+>', ' ', inhoud_raw).strip()
    inhoud = re.sub(r'\s+', ' ', inhoud)[:2000]

    return {
        'date': date,
        'zaak': zaak,
        'court': court,
        'rechtsgebied': rechtsgebied,
        'procedure': procedure,
        'inhoudsindicatie': inhoud,
    }

def is_water(parsed):
    """Check if a parsed case is water-relevant."""
    text = (parsed['inhoudsindicatie'] + ' ' + parsed['rechtsgebied']).lower()
    return (
        any(t in text for t in WATER_TERMS) or
        any(t in parsed['rechtsgebied'].lower() for t in WATER_RECHTSGEBIED)
    )

# ─── Phase 1: Enumerate ECLIs ─────────────────────────────────────────────────
print('=== Phase 1: Enumerating ECLIs ===')
candidate_eclis = {}   # ecli → court_label

for court_label, creator_uri in TARGET_CREATORS.items():
    offset = 0
    page_size = 1000
    court_total = 0

    print(f'\n{court_label}:')
    while True:
        params = {
            'creator': creator_uri,
            'max': page_size,
            'from': offset,
        }
        try:
            body = feed_get(params)
        except Exception as e:
            print(f'  offset={offset}: FEED ERROR {e}')
            time.sleep(5)
            continue

        # Total
        if offset == 0:
            total_m = re.search(r"Aantal gevonden ECLI'?s[^:]*: (\d+)", body)
            total = int(total_m.group(1)) if total_m else 0
            print(f'  Total in feed: {total}')

        # Extract ECLIs
        eclis_in_page = re.findall(r'<id>(ECLI:[^<]+)</id>', body)
        if not eclis_in_page:
            break

        for ecli in eclis_in_page:
            year = parse_ecli_year(ecli)
            if year and YEAR_START <= year <= YEAR_END:
                if ecli not in candidate_eclis:
                    candidate_eclis[ecli] = court_label
                    court_total += 1

        if offset == 0 or offset % 10000 == 0:
            print(f'  offset={offset}: {len(eclis_in_page)} ECLIs on page, {court_total} in 2016-2026 so far')

        offset += page_size
        if offset >= total or not eclis_in_page:
            break

        time.sleep(0.1)

    print(f'  → {court_label}: {court_total} ECLIs in 2016-2026')

print(f'\nTotal candidate ECLIs (2016-2026): {len(candidate_eclis)}')

# ─── Phase 2: Fetch content + filter ─────────────────────────────────────────
print('\n=== Phase 2: Fetching content & filtering ===')

all_cases = []
errors = 0
water_count = 0
checkpoint_every = 500

ecli_list = list(candidate_eclis.keys())
total_eclis = len(ecli_list)

for i, ecli in enumerate(ecli_list):
    if i % 500 == 0:
        pct = i / total_eclis * 100
        print(f'  [{i}/{total_eclis} {pct:.1f}%] water={water_count} errors={errors}')

    try:
        xml_body = content_get(ecli)
        parsed = parse_content(xml_body)

        if is_water(parsed):
            year = parse_ecli_year(ecli)
            case = {
                'country':           'Netherlands',
                'court':             candidate_eclis[ecli],
                'ecli':              ecli,
                'zaak_nummer':       parsed['zaak'],
                'court_name':        parsed['court'],
                'decision_date':     parsed['date'],
                'year':              year,
                'rechtsgebied':      parsed['rechtsgebied'],
                'procedure':         parsed['procedure'],
                'inhoudsindicatie':  parsed['inhoudsindicatie'],
                'url': f'https://uitspraken.rechtspraak.nl/details?id={urllib.parse.quote(ecli)}',
            }
            all_cases.append(case)
            water_count += 1

    except Exception as e:
        errors += 1
        if errors <= 10:
            print(f'  CONTENT ERR {ecli}: {str(e)[:60]}')

    # Checkpoint save
    if (i + 1) % checkpoint_every == 0 and all_cases:
        with open(TEMP_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_cases, f, ensure_ascii=False, indent=2)

    time.sleep(0.2)  # ~5 req/s

# ─── Phase 3: Save ────────────────────────────────────────────────────────────
with open(OUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(all_cases, f, ensure_ascii=False, indent=2)

print(f'\n=== DONE: {len(all_cases)} Dutch water law cases (2016-2026) ===')
print(f'Saved: {OUT_FILE}')

yc = Counter(c['year'] for c in all_cases)
print('\nYear distribution:')
for yr in sorted(yc): print(f'  {yr}: {yc[yr]}')

cc = Counter(c['court'] for c in all_cases)
print('\nBy court:', dict(cc))

if all_cases:
    s = all_cases[0]
    print(f'\nSample:')
    print(f'  ECLI: {s["ecli"]}')
    print(f'  Date: {s["decision_date"]}')
    print(f'  Rechtsgebied: {s["rechtsgebied"]}')
    print(f'  Inhoud: {s["inhoudsindicatie"][:200]}')