"""
Rechtspraak district courts scraper — Netherlands water law 2016–2026
Covers: 11 Rechtbanken + 3 Gerechtshoven + Centrale Raad van Beroep
Strategy:
  1. Use subject=bestuursrecht_omgevingsrecht to pre-filter ECLIs per court
     (cuts district court volumes from ~200K → ~1-3K each)
  2. Fetch content XML for each → apply water-term filter
  3. Merge output with netherlands_water_law_2016_2026.json

Estimated: ~21K ECLIs to fetch content for → ~2-5 hours at 0.2s/req
"""
import urllib.request, urllib.parse, ssl, re, sys, json, time, os
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDRS = {'User-Agent': 'research/water-law-dataset (academic use; github.com/jrklaus8/water-law-dataset)'}

FEED_URL    = 'https://data.rechtspraak.nl/uitspraken/zoeken'
CONTENT_URL = 'https://data.rechtspraak.nl/uitspraken/content'
DL = Path(os.environ.get('OUTPUT_DIR', r'C:\Users\junio\Downloads'))
OUT = DL / 'netherlands_district_courts_2016_2026.json'
TMP = OUT.with_suffix('.tmp.json')

# Pre-filter by omgevingsrecht (environmental/planning/water admin law)
OMGE_SUBJECT = 'http://psi.rechtspraak.nl/rechtsgebied#bestuursrecht_omgevingsrecht'

# Courts to scrape (NOT already in rechtspraak_expanded.py)
COURTS = {
    # 3 remaining Gerechtshoven (courts of appeal)
    'GHSHE': ("http://standaarden.overheid.nl/owms/terms/Gerechtshof_'s-Hertogenbosch",
               "Gerechtshof 's-Hertogenbosch"),
    'GHAMS': ('http://standaarden.overheid.nl/owms/terms/Gerechtshof_Amsterdam',
               'Gerechtshof Amsterdam'),
    'GHSGR': ('http://standaarden.overheid.nl/owms/terms/Gerechtshof_Den_Haag',
               'Gerechtshof Den Haag'),
    # Centrale Raad van Beroep
    'CRVB':  ('http://standaarden.overheid.nl/owms/terms/Centrale_Raad_van_Beroep',
               'Centrale Raad van Beroep'),
    # 11 Rechtbanken (district courts)
    'RBAMS': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Amsterdam',
               'Rechtbank Amsterdam'),
    'RBDHA': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Den_Haag',
               'Rechtbank Den Haag'),
    'RBROT': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Rotterdam',
               'Rechtbank Rotterdam'),
    'RBMNE': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Midden-Nederland',
               'Rechtbank Midden-Nederland'),
    'RBNHO': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Noord-Holland',
               'Rechtbank Noord-Holland'),
    'RBOBR': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Oost-Brabant',
               'Rechtbank Oost-Brabant'),
    'RBOVE': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Overijssel',
               'Rechtbank Overijssel'),
    'RBGEL': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Gelderland',
               'Rechtbank Gelderland'),
    'RBLIM': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Limburg',
               'Rechtbank Limburg'),
    'RBZWB': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Zeeland-West-Brabant',
               'Rechtbank Zeeland-West-Brabant'),
    'RBNNE': ('http://standaarden.overheid.nl/owms/terms/Rechtbank_Noord-Nederland',
               'Rechtbank Noord-Nederland'),
}

WATER_TERMS = [
    'drinkwater', 'waterschap', 'waterkering', 'grondwater', 'oppervlaktewater',
    'waterwet', 'drinkwaterwet', 'wateronttrekking', 'waterzuivering', 'afvalwater',
    'watervergunning', 'waterbeheer', 'wateroverlast', 'riolering', 'waterhuishouding',
    'waterpeil', 'dijkversterking', 'waterschapsbelasting', 'waterverontreiniging',
    'drinkwatervoorziening', 'waterschapsheffing', 'hemelwater', 'rioolwater',
    'waterleiding', 'waterleidingbedrijf', 'waterbedrijf', 'waterkwaliteit',
    'waterstand', 'waterlopen', 'watergang', 'polder', 'gemaal', 'dijk',
    'inundatie', 'overstroming', 'rivierverruiming', 'baggeren',
    'waterbodem', 'waterveiligheid', 'watertoets',
]

WATER_RECHTSGEBIED = ['omgevingsrecht', 'milieurecht', 'waterrecht', 'bestuursrecht']


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read().decode('utf-8', errors='replace')


def get_eclis(creator_uri, court_label):
    """Get ECLIs pre-filtered by omgevingsrecht subject, 2016-2026."""
    eclis = []
    offset = 0
    page_size = 1000
    total = None

    while True:
        params = {
            'creator':   creator_uri,
            'subject':   OMGE_SUBJECT,
            'date_from': '2016-01-01',
            'date_to':   '2026-12-31',
            'max':       page_size,
            'from':      offset,
        }
        url = FEED_URL + '?' + urllib.parse.urlencode(params)
        try:
            body = fetch(url)
        except Exception as e:
            print(f'    feed error at offset={offset}: {e}')
            time.sleep(5)
            break

        if total is None:
            m = re.search(r"Aantal gevonden ECLI'?s[^:]*: (\d+)", body)
            total = int(m.group(1)) if m else 0
            print(f'  {court_label}: {total:,} omgevingsrecht ECLIs in 2016-2026')

        page_eclis = re.findall(r'<id>(ECLI:[^<]+)</id>', body)
        if not page_eclis:
            break

        eclis.extend(page_eclis)
        offset += page_size
        if offset >= (total or 0):
            break
        time.sleep(0.15)

    return eclis


def parse_content(xml_body):
    def rx(pattern):
        m = re.search(pattern, xml_body, re.DOTALL | re.IGNORECASE)
        return m.group(1).strip() if m else ''

    date = rx(r'dcterms:date[^>]*Uitspraakdatum[^>]*>(\d{4}-\d{2}-\d{2})<')
    if not date:
        date = rx(r'<dcterms:date>(\d{4}-\d{2}-\d{2})</dcterms:date>')
    zaak = rx(r'psi:zaaknummer[^>]*>([^<]+)<')
    rechtsgebied = rx(r'dcterms:subject[^>]*Rechtsgebied[^>]*>([^<]+)<')
    if not rechtsgebied:
        rechtsgebied = rx(r'resourceIdentifier="([^"]*rechtsgebied[^"]*)"')
    procedure = rx(r'psi:procedure[^>]*rdfs:label="Procedure"[^>]*>([^<]+)<')
    if not procedure:
        procedure = rx(r'psi:procedure[^>]*>([^<]+)<')
    inhoud_raw = rx(r'<inhoudsindicatie[^>]*>(.*?)</inhoudsindicatie>')
    inhoud = re.sub(r'<[^>]+>', ' ', inhoud_raw).strip()
    inhoud = re.sub(r'\s+', ' ', inhoud)[:2000]
    return date, zaak, rechtsgebied, procedure, inhoud


def is_water(rechtsgebied, inhoud):
    text = (inhoud + ' ' + rechtsgebied).lower()
    return (
        any(t in text for t in WATER_TERMS) or
        any(t in rechtsgebied.lower() for t in WATER_RECHTSGEBIED)
    )


# ── Load checkpoint ───────────────────────────────────────────────────────────
if TMP.exists():
    with open(TMP, encoding='utf-8') as f:
        all_cases = json.load(f)
    seen = {c['ecli'] for c in all_cases}
    print(f'Resuming from checkpoint: {len(all_cases)} cases, {len(seen)} ECLIs seen')
else:
    all_cases = []
    seen = set()

# ── Phase 1: Enumerate ECLIs ──────────────────────────────────────────────────
print('=== Phase 1: Enumerating ECLIs (omgevingsrecht pre-filter) ===\n')
court_eclis = {}
for label, (uri, name) in COURTS.items():
    eclis = get_eclis(uri, label)
    court_eclis[label] = eclis
    time.sleep(0.5)

total_eclis = sum(len(v) for v in court_eclis.values())
print(f'\nTotal ECLIs to process: {total_eclis:,}')

# ── Phase 2: Fetch content + water filter ─────────────────────────────────────
print('\n=== Phase 2: Fetching content + water filter ===')
processed = 0
errors = 0
checkpoint_every = 200

for court_label, eclis in court_eclis.items():
    uri, court_name = COURTS[court_label]
    court_new = 0
    unseen = [e for e in eclis if e not in seen]
    print(f'\n{court_label} ({court_name}): {len(unseen):,} new ECLIs')

    for i, ecli in enumerate(unseen):
        processed += 1
        seen.add(ecli)

        if i % 500 == 0 and i > 0:
            pct = i / len(unseen) * 100
            print(f'  [{i:,}/{len(unseen):,} {pct:.0f}%] water={len(all_cases):,} total')

        try:
            url = CONTENT_URL + '?id=' + urllib.parse.quote(ecli)
            xml = fetch(url, timeout=20)
            date, zaak, rechtsgebied, procedure, inhoud = parse_content(xml)

            if is_water(rechtsgebied, inhoud):
                year_m = re.match(r'ECLI:NL:\w+:(\d{4}):', ecli)
                year = int(year_m.group(1)) if year_m else None
                all_cases.append({
                    'country':          'Netherlands',
                    'court':            court_label,
                    'court_name':       court_name,
                    'ecli':             ecli,
                    'zaak_nummer':      zaak,
                    'decision_date':    date,
                    'year':             year,
                    'rechtsgebied':     rechtsgebied,
                    'procedure':        procedure,
                    'inhoudsindicatie': inhoud,
                    'url': f'https://uitspraken.rechtspraak.nl/details?id={urllib.parse.quote(ecli)}',
                })
                court_new += 1

        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f'  ERR {ecli}: {str(e)[:60]}')

        if processed % checkpoint_every == 0:
            with open(TMP, 'w', encoding='utf-8') as f:
                json.dump(all_cases, f, ensure_ascii=False)

        time.sleep(0.2)

    print(f'  {court_label}: {court_new} water law cases found')

# ── Save ──────────────────────────────────────────────────────────────────────
all_cases.sort(key=lambda x: x.get('decision_date', ''), reverse=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(all_cases, f, ensure_ascii=False, indent=2)

if TMP.exists():
    TMP.unlink()

print(f'\n{"=" * 55}')
print(f'DONE — {len(all_cases)} Dutch water law cases (district courts)')
print(f'Saved: {OUT}')

yc = Counter(c['year'] for c in all_cases if c.get('year'))
print('\nYear distribution:')
for yr in sorted(yc):
    bar = '█' * min(yc[yr] // 3, 50)
    print(f'  {yr}: {yc[yr]:4d} {bar}')

cc = Counter(c['court'] for c in all_cases)
print('\nBy court:')
for court, n in cc.most_common():
    print(f'  {court:8s}: {n:4d}  {COURTS[court][1]}')
