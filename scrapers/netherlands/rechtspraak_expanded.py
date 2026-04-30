"""
Rechtspraak expanded scraper — Netherlands water law 2016–2026
Covers: RvS, CBb, CRvB, Hoge Raad, 4 Gerechtshoven, 4 key Rechtbanken
Uses date_from/date_to to efficiently target 2016-2026 only.
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
OUT = Path(os.environ.get('OUTPUT_DIR', r'C:\Users\junio\Downloads')) / 'netherlands_water_law_2016_2026.json'
TMP = OUT.with_suffix('.tmp.json')

# ── Courts to scrape ──────────────────────────────────────────────────────────
COURTS = {
    # Tier 1 — Administrative courts (highest water law relevance, ~10h total)
    'RvS':   'http://standaarden.overheid.nl/owms/terms/Raad_van_State',        # 162K ECLIs
    'CBb':   'http://standaarden.overheid.nl/owms/terms/College_van_Beroep_voor_het_bedrijfsleven',  # 18K
    # Tier 2 — Court of appeal covering Rhine/Maas/IJssel delta region (~8h)
    'GHARL': 'http://standaarden.overheid.nl/owms/terms/Gerechtshof_Arnhem-Leeuwarden',  # 143K
    # Tier 3 — Supreme Court (water law as cassation ground) (~7h)
    'HR':    'http://standaarden.overheid.nl/owms/terms/Hoge_Raad_der_Nederlanden',      # 128K
}

COURT_NAMES = {
    'RvS':   'Raad van State',
    'CBb':   'College van Beroep voor het bedrijfsleven',
    'GHARL': 'Gerechtshof Arnhem-Leeuwarden',
    'HR':    'Hoge Raad der Nederlanden',
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
]

WATER_RECHTSGEBIED = ['omgevingsrecht', 'milieurecht', 'waterrecht', 'bestuursrecht']


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read().decode('utf-8', errors='replace')


def get_eclis(creator_uri, court_label):
    """Get all ECLIs for a court in 2016-2026 using date filter."""
    eclis = []
    offset = 0
    page_size = 1000
    total = None

    while True:
        params = {
            'creator':   creator_uri,
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
            print(f'  {court_label}: {total:,d} ECLIs in 2016-2026')

        page_eclis = re.findall(r'<id>(ECLI:[^<]+)</id>', body)
        if not page_eclis:
            break

        eclis.extend(page_eclis)

        if offset % 10000 == 0 and offset > 0:
            print(f'    offset={offset:,d}, collected={len(eclis):,d}')

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


# ── Load existing results (checkpoint) ──────────────────────────────────────
if TMP.exists():
    with open(TMP, encoding='utf-8') as f:
        all_cases = json.load(f)
    seen = {c['ecli'] for c in all_cases}
    print(f'Resuming from checkpoint: {len(all_cases)} cases, {len(seen)} ECLIs seen')
else:
    all_cases = []
    seen = set()

# ── Phase 1: Enumerate ECLIs per court ──────────────────────────────────────
print('=== Phase 1: Enumerating ECLIs ===\n')
court_eclis = {}
for label, uri in COURTS.items():
    eclis = get_eclis(uri, label)
    court_eclis[label] = eclis
    time.sleep(0.5)

total_eclis = sum(len(v) for v in court_eclis.values())
print(f'\nTotal ECLIs to process: {total_eclis:,d}')

# ── Phase 2: Fetch content + filter ─────────────────────────────────────────
print('\n=== Phase 2: Fetching content ===')
processed = 0
errors = 0
checkpoint_every = 200

for court_label, eclis in court_eclis.items():
    court_new = 0
    court_eclis_unseen = [e for e in eclis if e not in seen]
    print(f'\n{court_label}: {len(court_eclis_unseen):,d} new ECLIs to fetch')

    for i, ecli in enumerate(court_eclis_unseen):
        processed += 1
        seen.add(ecli)

        if i % 1000 == 0 and i > 0:
            pct = i / len(court_eclis_unseen) * 100
            print(f'  [{i:,d}/{len(court_eclis_unseen):,d} {pct:.0f}%] water={len(all_cases):,d} total, {court_new} this court')

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
                    'court_name':       COURT_NAMES.get(court_label, court_label),
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

        # Checkpoint
        if processed % checkpoint_every == 0:
            with open(TMP, 'w', encoding='utf-8') as f:
                json.dump(all_cases, f, ensure_ascii=False)

        time.sleep(0.2)

    print(f'  {court_label}: {court_new} water law cases found')

# ── Save final ───────────────────────────────────────────────────────────────
all_cases.sort(key=lambda x: x.get('decision_date', ''), reverse=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(all_cases, f, ensure_ascii=False, indent=2)

if TMP.exists():
    TMP.unlink()

print(f'\n{"="*55}')
print(f'DONE — {len(all_cases)} Dutch water law cases')
print(f'Saved: {OUT}')

yc = Counter(c['year'] for c in all_cases if c.get('year'))
print('\nYear distribution:')
for yr in sorted(yc):
    bar = '█' * min(yc[yr] // 5, 50)
    print(f'  {yr}: {yc[yr]:4d} {bar}')

cc = Counter(c['court'] for c in all_cases)
print('\nBy court:')
for court, n in cc.most_common():
    print(f'  {court:8s}: {n:4d}  {COURT_NAMES.get(court,"")}')
