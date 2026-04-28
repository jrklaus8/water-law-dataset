"""TJDFT (Brasília) water law jurisprudência scraper.
API: POST https://jurisdf.tjdft.jus.br/api/v1/pesquisa
     body: {query: str, pagina: int, tamanho: int, espelho: bool, sinonimos: bool}
     response: {hits: {value: total}, registros: [...], paginacao: {...}}
"""
import os
import urllib.request, json, sys, re, time
sys.stdout.reconfigure(encoding='utf-8')

API = 'https://jurisdf.tjdft.jus.br/api/v1/pesquisa'
HDRS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json', 'Content-Type': 'application/json',
        'Origin': 'https://jurisdf.tjdft.jus.br', 'Referer': 'https://jurisdf.tjdft.jus.br/'}

QUERIES = [
    'agua saneamento',
    'abastecimento agua',
    'esgoto saneamento',
    'agua potavel',
]
PAGE_SIZE = 20
YEAR_START = 2016
YEAR_END = 2026

def post(body):
    req = urllib.request.Request(API, data=json.dumps(body, ensure_ascii=False).encode('utf-8'), headers=HDRS)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

def extract_year(dt_str):
    """Extract year from ISO datetime string."""
    if not dt_str:
        return None
    m = re.match(r'(\d{4})-', str(dt_str))
    return int(m.group(1)) if m else None

def clean_html(text):
    """Remove <mark> tags and clean HTML entities."""
    if not text:
        return ''
    text = re.sub(r'</?mark>', '', text)
    text = text.replace('\xa0', ' ')
    return text.strip()

all_cases = {}

def process_registros(registros):
    new_cases = 0
    skipped = 0
    for reg in registros:
        proc = reg.get('processo', '')
        uuid = reg.get('uuid', '')
        key = uuid or proc
        if not key or key in all_cases:
            continue
        year = extract_year(reg.get('dataJulgamento'))
        if year is None:
            year = extract_year(reg.get('dataPublicacao'))
        if year is None or not (YEAR_START <= year <= YEAR_END):
            skipped += 1
            continue
        marcadores = reg.get('marcadores', {})
        ementa_list = marcadores.get('ementa', [])
        ementa_raw = ementa_list[0] if ementa_list else reg.get('ementa', '')
        ementa = clean_html(ementa_raw)
        all_cases[key] = {
            'tribunal': 'TJDFT', 'estado': 'DF',
            'num_processo': proc, 'uuid': uuid,
            'identificador': reg.get('identificador', ''),
            'data_julgamento': (reg.get('dataJulgamento','')[:10] if reg.get('dataJulgamento') else ''),
            'data_publicacao': (reg.get('dataPublicacao','')[:10] if reg.get('dataPublicacao') else ''),
            'ementa': ementa[:3000],
            'decisao': clean_html(reg.get('decisao', '')),
            'relator': reg.get('nomeRelator', ''),
            'orgao_julgador': reg.get('descricaoOrgaoJulgador', ''),
            'base': reg.get('base', ''),
            'ano': year,
        }
        new_cases += 1
    return new_cases, skipped

# Run each query
for QUERY in QUERIES:
    r0 = post({'query': QUERY, 'pagina': 0, 'tamanho': 1})
    total = r0['hits']['value']
    pages = (total + PAGE_SIZE - 1) // PAGE_SIZE
    print(f'\nQuery: "{QUERY}" → {total} total, {pages} pages')

    for page in range(pages):
        body = {'query': QUERY, 'pagina': page, 'tamanho': PAGE_SIZE}
        try:
            resp = post(body)
        except Exception as e:
            print(f'  Page {page+1}: ERROR {e}')
            time.sleep(2)
            continue
        registros = resp.get('registros', [])
        new_cases, skipped = process_registros(registros)
        total_so_far = len(all_cases)
        if page == 0 or (page + 1) % 20 == 0 or page == pages - 1:
            print(f'  Page {page+1}/{pages}... {new_cases} new, {skipped} outside range (total {total_so_far})')
        time.sleep(0.25)

# Step 3: Save
cases_list = list(all_cases.values())
output_path = os.path.join(os.getenv('OUTPUT_DIR', '.'), 'tjdft_cases_2016_2026.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(cases_list, f, ensure_ascii=False, indent=2)

print(f'\n=== DONE: {len(cases_list)} TJDFT cases (2016-2026) ===')
print(f'Saved to: {output_path}')

# Sample
if cases_list:
    print('\nSample case:')
    s = cases_list[0]
    print(f'  processo: {s["num_processo"]}')
    print(f'  ano: {s["ano"]}')
    print(f'  relator: {s["relator"]}')
    print(f'  orgão: {s["orgao_julgador"]}')
    print(f'  ementa: {s["ementa"][:200]}')

# Year distribution
from collections import Counter
years = Counter(c['ano'] for c in cases_list)
print('\nYear distribution:')
for yr in sorted(years.keys()):
    print(f'  {yr}: {years[yr]}')