"""
TJRJ (Rio de Janeiro) water law scraper.
System: ejuris ASP.NET WebForms at www3.tjrj.jus.br/ejuris/
Flow:
  1. GET ConsultarJurisprudencia.aspx → VIEWSTATE
  2. POST search → session stored as cookie (ParPesqEjuris_{pageSeq})
  3. POST to WebMethod ExecutarConsultarJurisprudencia with {numPagina, pageSeq} → JSON
"""
import os
import urllib.request, urllib.parse, ssl, sys, re, json, time, http.cookiejar
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE    = 'https://www3.tjrj.jus.br/ejuris/ConsultarJurisprudencia.aspx'
PROC    = 'https://www3.tjrj.jus.br/EJURIS/ProcessarConsJurisES.aspx'
WM_URL  = PROC + '/ExecutarConsultarJurisprudencia'

HDRS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0',
    'Accept-Language': 'pt-BR,pt;q=0.9',
}

YEAR_START = 2016
YEAR_END   = 2026

QUERIES = [
    'agua saneamento',
    'abastecimento agua',
    'CEDAE agua',
    'fornecimento agua',
    'esgoto saneamento',
    'agua potavel',
    'tarifa agua',
    'corte fornecimento agua',
    'suspensao agua',
    'servico agua',
    'recurso hidrico',
    'manancial agua',
]

DL = Path(os.getenv('OUTPUT_DIR', '.'))

def make_session():
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(jar),
        urllib.request.HTTPSHandler(context=ctx))
    return opener, jar

def get_viewstate(opener):
    req = urllib.request.Request(BASE, headers={**HDRS, 'Accept': 'text/html,*/*'})
    with opener.open(req, timeout=20) as r:
        html = r.read().decode('utf-8', errors='replace')
    return {
        'vs':  re.search(r'id="__VIEWSTATE"\s+value="(.*?)"', html).group(1),
        'vsg': re.search(r'id="__VIEWSTATEGENERATOR"\s+value="(.*?)"', html).group(1),
        'ev':  re.search(r'id="__EVENTVALIDATION"\s+value="(.*?)"', html).group(1),
    }

def post_search(opener, state, query):
    post = {
        '__VIEWSTATE':          state['vs'],
        '__VIEWSTATEGENERATOR': state['vsg'],
        '__EVENTVALIDATION':    state['ev'],
        '__EVENTTARGET':        '',
        '__EVENTARGUMENT':      '',
        'ctl00$ContentPlaceHolder1$hfListaPalavrasBloqueadas': '',
        'ctl00$ContentPlaceHolder1$hfCodRamos': '',
        'ctl00$ContentPlaceHolder1$hfCodMags':  '',
        'ctl00$ContentPlaceHolder1$hfCodOrgs':  '',
        'ctl00$ContentPlaceHolder1$txtTextoPesq': query,
        'ctl00$ContentPlaceHolder1$chkAtivo':   'on',
        'ctl00$ContentPlaceHolder1$chkAcordao': 'on',
        'ctl00$ContentPlaceHolder1$chkDecMon':  'on',
        'ctl00$ContentPlaceHolder1$btnPesquisar': 'Pesquisar',
    }
    data = urllib.parse.urlencode(post).encode('utf-8')
    req = urllib.request.Request(BASE, data=data, headers={
        **HDRS, 'Accept': 'text/html,*/*',
        'Content-Type': 'application/x-www-form-urlencoded', 'Referer': BASE})
    with opener.open(req, timeout=30) as r:
        final_url = r.url
        r.read()
    m = re.search(r'PageSeq=(\d+)', final_url)
    return m.group(1) if m else '0'

def call_webmethod(opener, page_seq, page_num=0):
    body = json.dumps({'numPagina': page_num, 'pageSeq': page_seq}).encode('utf-8')
    req = urllib.request.Request(WM_URL, data=body, headers={
        **HDRS,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json; charset=utf-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': f'{PROC}?PageSeq={page_seq}&Version=1.2.1.0',
    })
    with opener.open(req, timeout=30) as r:
        return json.loads(r.read())

def clean(text):
    if not text:
        return ''
    text = re.sub(r'<[^>]+>', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def extract_year(proc_cnj):
    """Extract year from CNJ case number NNNNNNN-NN.YYYY.N.NN.NNNN"""
    m = re.search(r'\d{7}-\d{2}\.(\d{4})\.', str(proc_cnj))
    return int(m.group(1)) if m else None

# ── Scraping ──────────────────────────────────────────────────────────────────
all_cases = {}

for query in QUERIES:
    print(f'\nQuery: "{query}"')
    opener, jar = make_session()

    try:
        state = get_viewstate(opener)
        page_seq = post_search(opener, state, query)
        print(f'  pageSeq: {page_seq}')
    except Exception as e:
        print(f'  INIT ERROR: {e}')
        time.sleep(3)
        continue

    page_num = 0
    query_new = 0

    while True:
        try:
            resp = call_webmethod(opener, page_seq, page_num)
        except Exception as e:
            print(f'  Page {page_num}: WM ERROR {e}')
            time.sleep(3)
            break

        d = resp.get('d') or {}
        total = d.get('TotalDocs', 0)
        docs  = d.get('DocumentosConsulta', [])

        if page_num == 0:
            print(f'  Total: {total}')
        if not docs:
            break

        for doc in docs:
            proc_cnj = doc.get('NumProcCnj', '')
            cod      = str(doc.get('CodDoc', ''))
            key      = proc_cnj or cod
            if not key or key in all_cases:
                continue

            year = extract_year(proc_cnj)
            if year is None or not (YEAR_START <= year <= YEAR_END):
                continue

            ementa = clean(doc.get('Texto', ''))
            classe = doc.get('Classe', '')
            camara = clean(doc.get('NomeOrgaoJulg', '') or doc.get('DescricaoOrgaoJulg', ''))
            relator = clean(doc.get('NomeRelator', ''))
            data_julg = doc.get('DataPublicacao', '') or doc.get('DataJulgamento', '')
            if isinstance(data_julg, str):
                data_julg = data_julg[:10]

            all_cases[key] = {
                'tribunal': 'TJRJ', 'estado': 'RJ',
                'num_processo': proc_cnj,
                'cod_doc': cod,
                'data_julgamento': data_julg,
                'ano': year,
                'classe': classe,
                'camara_orgao': camara,
                'relator': relator,
                'ementa': ementa[:3000],
                'url': f'https://www3.tjrj.jus.br/ejuris/ConsultarJurisprudencia.aspx',
            }
            query_new += 1

        print(f'  page {page_num}: {len(docs)} docs, {query_new} new (total {len(all_cases)})')

        # Check if more pages exist
        # TJRJ paginates by 10 docs per page
        if len(docs) < 10 or page_num * 10 + len(docs) >= total:
            break

        page_num += 1
        time.sleep(0.5)

    time.sleep(1)

# ── Save ──────────────────────────────────────────────────────────────────────
cases_list = list(all_cases.values())
out = DL / 'tjrj_cases_2016_2026.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(cases_list, f, ensure_ascii=False, indent=2)

print(f'\n=== DONE: {len(cases_list)} TJRJ cases (2016-2026) ===')
print(f'Saved: {out}')

yc = Counter(c['ano'] for c in cases_list)
print('\nYear distribution:')
for yr in sorted(yc): print(f'  {yr}: {yc[yr]}')

if cases_list:
    s = cases_list[0]
    print(f'\nSample:')
    print(f'  proc: {s["num_processo"]}  ano: {s["ano"]}  classe: {s["classe"]}')
    print(f'  ementa: {s["ementa"][:300]}')