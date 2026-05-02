"""
Jurimetric regex coding for the Global Water Law Judicial Decisions Dataset
============================================================================
Applies coded variables to water_law_global.csv for dissertation analysis.

Variables coded per case:
  hr_language       — human rights / right-to-water framing
  sust_language     — sustainability / environmental framing
  governance_cat    — type of dispute (tariff, connection, quality, etc.)
  win_loss          — outcome (plaintiff/user wins vs defendant/utility wins)
  mp_involvement    — Ministério Público involvement (Brazil only)
  indigenous_water  — Indigenous / First Nations water rights (Canada/intl)
  informal_settle   — irregular settlement / informal housing context
  public_interest   — public interest / collective action framing

All patterns are applied to the combined text field (ementa/title/snippet).
Each variable is a binary flag (1/0) or categorical string.
"""
import re, json, sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

try:
    import pandas as pd
except ImportError:
    raise SystemExit('pip install pandas openpyxl')

DL  = Path(r'C:\Users\junio\Downloads')
CSV = DL / 'water_law_global.csv'

if not CSV.exists():
    raise SystemExit(f'Not found: {CSV}\nRun merge_all_countries.py first.')

print('Loading dataset...')
df = pd.read_csv(CSV, low_memory=False, encoding='utf-8-sig')
print(f'  {len(df):,} cases loaded')
print(f'  Columns: {list(df.columns)}')

# ── Text fields to search ─────────────────────────────────────────────────────
# Two text fields:
# _text     : all available columns — used for governance classification
#             (court name, legal_area, case_type help identify dispute type)
# _text_sub : only substantive decision text — used for HR/sustainability
#             (avoids false positives from procedural metadata like
#              legal_area="Direito à Água / Saneamento" which is TJSP's
#              classification label, not actual human rights framing)
ALL_TEXT_COLS = ['ementa', 'title', 'text', 'snippet', 'keywords',
                 'num_processo', 'class', 'classe',
                 'summary', 'case_type', 'legal_area', 'court_name', 'chamber']
SUB_TEXT_COLS = ['ementa', 'text', 'summary', 'snippet']  # decision body only

existing_all = [c for c in ALL_TEXT_COLS if c in df.columns]
existing_sub = [c for c in SUB_TEXT_COLS if c in df.columns]
print(f'\nGovernance text columns: {existing_all}')
print(f'HR/sust text columns: {existing_sub}')

df['_text'] = df[existing_all].fillna('').apply(
    lambda row: ' '.join(str(v) for v in row if v), axis=1
).str.lower()

df['_text_sub'] = df[existing_sub].fillna('').apply(
    lambda row: ' '.join(str(v) for v in row if v), axis=1
).str.lower()

# ════════════════════════════════════════════════════════════════════════════════
# 1. HUMAN RIGHTS / RIGHT-TO-WATER LANGUAGE
# ════════════════════════════════════════════════════════════════════════════════
HR_PATTERNS = [
    # Portuguese
    r'\bdireito (?:fundamental|humano|b[aá]sico).*?[aáàâã]gua\b',
    r'\b[aáàâã]gua.*?direito (?:fundamental|humano|b[aá]sico)\b',
    r'\bdireito [aáàâã] [aáàâã]gua\b',
    r'\bdireito ao saneamento\b',
    r'\bdireito [aáàâã] vida.*?[aáàâã]gua\b',
    r'\bm[ií]nimo existencial\b',
    r'\bdignidade da pessoa humana.*?[aáàâã]gua\b',
    r'\b[aáàâã]gua.*?dignidade da pessoa humana\b',
    r'\bdireitos fundamentais.*?[aáàâã]gua\b',
    r'\bnorma programática\b',
    # English
    r'\bright to (?:safe |clean |drinking )?water\b',
    r'\bhuman right.*?water\b',
    r'\bwater.*?human right\b',
    r'\bconstitutional right.*?water\b',
    r'\bfundamental right.*?water\b',
    r'\bcharter right.*?water\b',
    r'\bwater.*?charter right\b',
    r'\bminimum water\b',
    # French
    r'\bdroit [àa] l\'eau\b',
    r'\bdroit fondamental.*?eau\b',
    r'\beau.*?droit fondamental\b',
    r'\bdroit [àa] l\'eau potable\b',
    # Dutch
    r'\brecht op (?:schoon |drink)?water\b',
    r'\bgrondrecht.*?water\b',
    r'\bwater.*?grondrecht\b',
]
HR_RE = [re.compile(p, re.I | re.DOTALL) for p in HR_PATTERNS]

def code_hr(text):
    return int(any(r.search(text) for r in HR_RE))

# ════════════════════════════════════════════════════════════════════════════════
# 2. SUSTAINABILITY / ENVIRONMENTAL FRAMING
# ════════════════════════════════════════════════════════════════════════════════
SUST_PATTERNS = [
    # Portuguese
    r'\bdesenvolvimento sustent[aá]vel\b',
    r'\bmeio ambiente.*?[aáàâã]gua\b',
    r'\b[aáàâã]gua.*?meio ambiente\b',
    r'\brecursos h[ií]dricos\b',
    r'\bpreserva[çc][aã]o.*?[aáàâã]gua\b',
    r'\bprincípio da precau[çc][aã]o\b',
    r'\bprincípio do poluidor-pagador\b',
    r'\bdano ambiental.*?[aáàâã]gua\b',
    r'\bimpacto ambiental.*?[aáàâã]gua\b',
    r'\bprotec[çc][aã]o ambiental\b',
    r'\blicen[çc]a ambiental\b',
    r'\bàrea de prote[çc][aã]o\b',
    # English
    r'\bsustainab\w+.*?water\b',
    r'\bwater.*?sustainab\w+\b',
    r'\benvironmental.*?water\b',
    r'\bwater.*?environment\b',
    r'\bprecautionary principle\b',
    r'\bpolluter pays\b',
    r'\becosystem.*?water\b',
    r'\bwater.*?ecosystem\b',
    r'\bwatershed management\b',
    r'\baquatic habitat\b',
    r'\benvironmental assessment.*?water\b',
    r'\bclimate change.*?water\b',
    # French
    r'\bdéveloppement durable.*?eau\b',
    r'\beau.*?développement durable\b',
    r'\benvironnement.*?eau\b',
    r'\bressources hydriques\b',
    r'\bprincipe de précaution\b',
    # Dutch
    r'\bduurzaam.*?water\b',
    r'\bwater.*?duurzaam\b',
    r'\bmilieu.*?water\b',
    r'\bwater.*?milieu(?:bescherming)?\b',
    r'\bwaterbeheer\b',
    r'\bwaterbeleid\b',
]
SUST_RE = [re.compile(p, re.I | re.DOTALL) for p in SUST_PATTERNS]

def code_sust(text):
    return int(any(r.search(text) for r in SUST_RE))

# ════════════════════════════════════════════════════════════════════════════════
# 3. GOVERNANCE CATEGORY (dispute type)
# Returns the FIRST matching category (ordered by specificity)
# ════════════════════════════════════════════════════════════════════════════════
GOV_CATS = [
    # ── Tariff / billing disputes ────────────────────────────────────────────
    ('tariff_dispute', [
        r'\btarifa.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?tarifa\b',
        r'\bcobran[çc]a.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?cobran[çc]a\b',
        r'\bfatura.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?fatura\b',
        r'\bwater rate\b', r'\bwater bill\b', r'\bwater meter\b',
        r'\bwater tariff\b', r'\btarif.*?eau\b', r'\beau.*?tarif\b',
        r'\bwaterprijzen\b', r'\btarieven.*?water\b',
        r'\bwater utility rate\b', r'\brate dispute.*?water\b',
        # Brazil case_type phrases (appear without context words):
        r'\bregime tarif[aá]rio\b', r'\binadimpl\w+.*?[aáàâã]gua\b',
        r'\b[aáàâã]gua.*?inadimpl\w+\b', r'\bmedid[ao]r.*?[aáàâã]gua\b',
        r'\bconsumo.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?consum\w+\b',
        r'\bleitura.*?[aáàâã]gua\b', r'\breclama[çc][aã]o.*?[aáàâã]gua\b',
        r'\bclassifica[çc][aã]o.*?economi\w+\b',
    ]),
    # ── Connection refusal / access denial ───────────────────────────────────
    ('connection_refusal', [
        r'\bliga[çc][aã]o.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?liga[çc][aã]o\b',
        r'\bconex[aã]o.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?conex[aã]o\b',
        r'\brecusa.*?fornecimento.*?[aáàâã]gua\b',
        r'\bfornecimento.*?[aáàâã]gua.*?recusa\b',
        r'\bsuspens[aã]o.*?fornecimento.*?[aáàâã]gua\b',
        r'\bsuspens[aã]o.*?[aáàâã]gua\b',
        r'\bcorte.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?corte\b',
        r'\bwater connection\b', r'\bdenied.*?water\b', r'\bwater.*?refus\w*\b',
        r'\bwater disconnection\b', r'\bdisconnect.*?water\b',
        r'\baansluiting.*?water\b', r'\bwater.*?aansluiting\b',
        r'\braccordement.*?eau\b', r'\beau.*?raccordement\b',
        # Brazil: "fornecimento de água" often means a connection/supply dispute
        r'\bfornecimento de [aáàâã]gua\b', r'\b[aáàâã]gua e esgoto\b',
        r'\bliga[çc][aã]o predial\b', r'\breliga[çc][aã]o\b',
        r'\bnegativa.*?fornecimento\b', r'\binterrup[çc][aã]o.*?[aáàâã]gua\b',
    ]),
    # ── Water quality / contamination ────────────────────────────────────────
    ('water_quality', [
        r'\bqualidade.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?qualidade\b',
        r'\bcontamina[çc][aã]o.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?contamina[çc][aã]o\b',
        r'\bpolu[ií][çc][aã]o.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?polu[ií][çc][aã]o\b',
        r'\bfornecimento.*?[aáàâã]gua.*?impr[oó]pria\b',
        r'\b[aáàâã]gua.*?impr[oó]pria\b',
        r'\bwater quality\b', r'\bcontaminated water\b', r'\bwater contamination\b',
        r'\bboil water\b', r'\bdrinking water advisory\b',
        r'\bwater pollution\b', r'\bwater safety\b',
        r'\bwaterkwaliteit\b', r'\bverontreiniging.*?water\b',
        r'\bqualité.*?eau\b', r'\bcontamination.*?eau\b',
    ]),
    # ── Informal settlement / irregular access ───────────────────────────────
    ('informal_settlement', [
        r'\bassentamento.*?irregular\b', r'\bloteamento.*?irregular\b',
        r'\b[aáàâã]rea.*?irregular.*?[aáàâã]gua\b',
        r'\b[aáàâã]gua.*?[aáàâã]rea.*?irregular\b',
        r'\bocupa[çc][aã]o.*?irregular.*?[aáàâã]gua\b',
        r'\binvasão.*?[aáàâã]gua\b',
        r'\bfavela.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?favela\b',
        r'\binformal settlement.*?water\b',
        r'\bsquatter.*?water\b',
        r'\bunauthori[sz]ed.*?water\b',
        r'\billegal.*?connection.*?water\b',
    ]),
    # ── Groundwater / aquifer ────────────────────────────────────────────────
    ('groundwater', [
        r'\b[aáàâã]gua subterr[aâ]nea\b', r'\baqüífero\b', r'\baquífero\b',
        r'\bpoço.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?po[çc]o\b',
        r'\bgroundwater\b', r'\baquifer\b', r'\bwell water\b',
        r'\bwater table\b', r'\bsub-surface water\b',
        r'\bgrondwater\b', r'\bwaterwinning\b',
        r'\beau souterraine\b', r'\bnappe phréatique\b',
    ]),
    # ── Flooding / flood damage ──────────────────────────────────────────────
    ('flooding', [
        r'\binunda[çc][aã]o\b', r'\benchente\b', r'\balagamento\b',
        r'\bdano.*?chuva\b', r'\bdano.*?inunda[çc][aã]o\b',
        r'\bflood(?:ing|plain|damage|s)?\b',
        r'\bflood damage\b', r'\bfloodplain\b',
        r'\binondation\b', r'\bdommage.*?inondation\b',
        r'\boverstromings?\b', r'\bwateroverlast\b',
        r'\bzone inondable\b',
    ]),
    # ── Riparian / waterway / navigation ─────────────────────────────────────
    ('riparian_waterway', [
        r'\bripari[ao]\w*\b',
        r'\bcurso d[\'e]? ?[aáàâã]gua\b', r'\briacho\b', r'\bcórrego\b',
        r'\brio.*?[aáàâã]gua\b', r'\bnaveg[aá]v\w+\b',
        r'\briparian\b', r'\bwatercourse\b', r'\bnavigable water\b',
        r'\briverbank\b', r'\bwaterway\b', r'\bshoreline\b',
        r'\bwatergang\b', r'\bwaterloop\b', r'\bwaterscheiding\b',
        r'\bcours d[\'e]? ?eau\b', r'\bnavigabilité\b',
    ]),
    # ── Irrigation / agricultural water ──────────────────────────────────────
    ('irrigation_agricultural', [
        r'\birriga[çc][aã]o\b', r'\b[aáàâã]gua.*?agr[ií]cola\b',
        r'\bagr[ií]cola.*?[aáàâã]gua\b', r'\bperímetro irrigado\b',
        r'\bdistrito de irriga[çc][aã]o\b',
        r'\birrigation\b', r'\bwater district\b', r'\birrigation district\b',
        r'\bagricultural water\b', r'\bwater licence.*?farm\b',
        r'\birrigatie\b', r'\bwaterschap\b',
        r'\birrigati\w+.*?eau\b',
    ]),
    # ── Sanitation / sewage / wastewater ─────────────────────────────────────
    ('sanitation_sewage', [
        r'\bsaneamento b[aá]sico\b', r'\besgoto\b', r'\bfossa\b',
        r'\btratamento.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?tratamento\b',
        r'\besta[çc][aã]o de tratamento\b', r'\beta\b',
        r'\bwastewater\b', r'\bsewage\b', r'\bsewer\b',
        r'\bsanitation\b', r'\bwaste water treatment\b',
        r'\briolering\b', r'\bafvalwater\b', r'\bwaterzuivering\b',
        r'\beaux usées\b', r'\bassainissement\b',
    ]),
    # ── Hydroelectric / dam / reservoir ──────────────────────────────────────
    ('hydroelectric_dam', [
        r'\bhidroel[eé]trica\b', r'\busina.*?[aáàâã]gua\b',
        r'\bbarragem\b', r'\breservatório\b',
        r'\bhidrel[eé]trica\b',
        r'\bhydroelectric\b', r'\bdam\b', r'\breservoir\b',
        r'\bwater power\b',
        r'\bwaterkrachtcentrale\b', r'\bstuwdam\b',
        r'\bbarrage\b', r'\bhydroélectrique\b',
    ]),
    # ── Regulatory / permit / licence ────────────────────────────────────────
    ('regulatory_permit', [
        r'\boutorga.*?[aáàâã]gua\b', r'\blicen[çc]a.*?[aáàâã]gua\b',
        r'\bpermiss[aã]o.*?[aáàâã]gua\b', r'\bconcess[aã]o.*?[aáàâã]gua\b',
        r'\bregula[çc][aã]o.*?[aáàâã]gua\b',
        r'\bwater licence\b', r'\bwater permit\b', r'\bwater allocation\b',
        r'\bwater rights\b', r'\bwater taking\b',
        r'\bwatervergunning\b', r'\bonttrekking\b',
        r'\bpermis.*?eau\b', r'\bautorisati\w+.*?eau\b',
    ]),
]

def code_governance(text):
    for cat, patterns in GOV_CATS:
        for p in patterns:
            if re.search(p, text, re.I):
                return cat
    return 'other_water'

# ════════════════════════════════════════════════════════════════════════════════
# 4. WIN/LOSS — who prevailed
# ════════════════════════════════════════════════════════════════════════════════
# Proxy: did the user/plaintiff win (utility ordered to provide/reconnect/compensate)?
# Only reliable for Brazil (ementa usually states the outcome)
WIN_USER_PATTERNS = [
    # Portuguese — user wins
    r'\bprovido\b.*\bdireito [aáàâã] [aáàâã]gua\b',
    r'\bdireito [aáàâã] [aáàâã]gua\b.*\bprovido\b',
    r'\bdireito [aáàâã] [aáàâã]gua\b.*\bprocedente\b',
    r'\bprocedente\b.*\b[aáàâã]gua\b',
    r'\bobriga[çc][aã]o de fazer.*?fornecer [aáàâã]gua\b',
    r'\bfornecer [aáàâã]gua.*?obriga[çc][aã]o de fazer\b',
    r'\bliga[çc][aã]o.*?deferida\b',
    r'\breliga[çc][aã]o.*?determinada\b',
    r'\brestabelecer.*?fornecimento\b',
    r'\bresponsabilidade.*?empresa.*?[aáàâã]gua\b',
    r'\bdano moral.*?[aáàâã]gua.*?provid\w+\b',
    r'\bpedido.*?procedente.*?[aáàâã]gua\b',
    # English
    r'\border\w*.*?prov\w+.*?water\b',
    r'\bwater.*?order\w*.*?prov\w+\b',
    r'\bmandatory.*?water.*?connection\b',
    r'\bwater.*?reconnect\w+.*?order\w*\b',
]
WIN_UTILITY_PATTERNS = [
    # Portuguese — utility wins
    r'\bimprovido\b.*\b[aáàâã]gua\b',
    r'\b[aáàâã]gua\b.*\bimprovido\b',
    r'\bimprocedente\b.*\b[aáàâã]gua\b',
    r'\b[aáàâã]gua\b.*\bimprocedente\b',
    r'\bcorte.*?[aáàâã]gua.*?leg[ií]timo\b',
    r'\bsuspens[aã]o.*?leg[ií]tima.*?[aáàâã]gua\b',
    r'\bdébito.*?[aáàâã]gua.*?prov\w+\b',
    # English
    r'\butility.*?prevail\w*\b',
    r'\bwater.*?disconnect.*?lawful\b',
    r'\bdismiss\w+.*?water\b',
    r'\bwater.*?claim.*?dismiss\w+\b',
]

WIN_USER_RE = [re.compile(p, re.I | re.DOTALL) for p in WIN_USER_PATTERNS]
WIN_UTIL_RE = [re.compile(p, re.I | re.DOTALL) for p in WIN_UTILITY_PATTERNS]

def code_win_loss(text, country):
    if country not in ('Brazil', 'BR'):
        return 'not_coded'
    user_wins = any(r.search(text) for r in WIN_USER_RE)
    util_wins = any(r.search(text) for r in WIN_UTIL_RE)
    if user_wins and not util_wins:
        return 'user_wins'
    if util_wins and not user_wins:
        return 'utility_wins'
    if user_wins and util_wins:
        return 'mixed'
    return 'unclear'

# ════════════════════════════════════════════════════════════════════════════════
# 5. MINISTÉRIO PÚBLICO INVOLVEMENT (Brazil only)
# ════════════════════════════════════════════════════════════════════════════════
MP_PATTERNS = [
    r'\bministério público\b', r'\bmp\b.*\b[aáàâã]gua\b',
    r'\bação civil pública\b', r'\bacp\b.*\b[aáàâã]gua\b',
    r'\bpromotor(?:ia)?\b.*\b[aáàâã]gua\b',
    r'\btutela coletiva\b', r'\bdifusos\b.*\b[aáàâã]gua\b',
    r'\binteresses difusos\b', r'\bação coletiva\b.*\b[aáàâã]gua\b',
]
MP_RE = [re.compile(p, re.I | re.DOTALL) for p in MP_PATTERNS]

def code_mp(text, country):
    if country not in ('Brazil', 'BR'):
        return 0
    return int(any(r.search(text) for r in MP_RE))

# ════════════════════════════════════════════════════════════════════════════════
# 6. INDIGENOUS WATER RIGHTS
# ════════════════════════════════════════════════════════════════════════════════
INDIGENOUS_PATTERNS = [
    # English
    r'\bindigenous.*?water\b', r'\bwater.*?indigenous\b',
    r'\bfirst nations.*?water\b', r'\bwater.*?first nations\b',
    r'\btreaty.*?water\b', r'\bwater.*?treaty\b',
    r'\baboriginal.*?water\b', r'\bwater.*?aboriginal\b',
    r'\bmetis.*?water\b', r'\binuit.*?water\b',
    r'\bdrinking water advisory.*?reserve\b',
    r'\bwater.*?reserve\b.*\bfirst nations\b',
    r'\bsection 35.*?water\b',
    # Portuguese
    r'\bindígena.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?indígena\b',
    r'\bterritório indígena.*?[aáàâã]gua\b',
    r'\bpopula[çc][aã]o indígena.*?[aáàâã]gua\b',
    # Dutch
    r'\binheems.*?water\b',
]
IND_RE = [re.compile(p, re.I | re.DOTALL) for p in INDIGENOUS_PATTERNS]

def code_indigenous(text):
    return int(any(r.search(text) for r in IND_RE))

# ════════════════════════════════════════════════════════════════════════════════
# 7. PUBLIC INTEREST / COLLECTIVE FRAMING
# ════════════════════════════════════════════════════════════════════════════════
PUBLIC_PATTERNS = [
    r'\binteresse p[úu]blico.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?interesse p[úu]blico\b',
    r'\bservi[çc]o p[úu]blico.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?servi[çc]o p[úu]blico\b',
    r'\baco coletiva\b', r'\binteresses coletivos\b',
    r'\bpopula[çc][aã]o.*?[aáàâã]gua\b',
    r'\bpublic interest.*?water\b', r'\bwater.*?public interest\b',
    r'\bcollective.*?water\b', r'\bclass action.*?water\b',
    r'\bwater.*?class action\b',
    r'\bpubliek belang.*?water\b', r'\balgemeen belang.*?water\b',
    r'\bintérêt public.*?eau\b', r'\beau.*?intérêt public\b',
]
PUB_RE = [re.compile(p, re.I | re.DOTALL) for p in PUBLIC_PATTERNS]

def code_public(text):
    return int(any(r.search(text) for r in PUB_RE))

# ════════════════════════════════════════════════════════════════════════════════
# APPLY CODING
# ════════════════════════════════════════════════════════════════════════════════
print('\nApplying jurimetric coding...')
country_col = 'country' if 'country' in df.columns else 'pais'

texts     = df['_text'].tolist()       # all fields — for governance
texts_sub = df['_text_sub'].tolist()   # body text only — for HR/sust
countries = df[country_col].fillna('').tolist() if country_col in df.columns else [''] * len(df)

hr, sust, gov, wl, mp, ind, pub = [], [], [], [], [], [], []

for i, (text, text_sub, country) in enumerate(zip(texts, texts_sub, countries)):
    if i % 5000 == 0:
        print(f'  {i:,}/{len(df):,}...', flush=True)
    hr.append(code_hr(text_sub))          # substantive text only — avoids metadata FP
    sust.append(code_sust(text_sub))      # substantive text only
    gov.append(code_governance(text))     # full text helps classify dispute type
    wl.append(code_win_loss(text_sub, country))
    mp.append(code_mp(text_sub, country))
    ind.append(code_indigenous(text_sub))
    pub.append(code_public(text_sub))

df['hr_language']      = hr
df['sust_language']    = sust
df['governance_cat']   = gov
df['win_loss']         = wl
df['mp_involvement']   = mp
df['indigenous_water'] = ind
df['public_interest']  = pub

# Drop working columns
df.drop(columns=['_text', '_text_sub'], inplace=True)

# ════════════════════════════════════════════════════════════════════════════════
# SAVE
# ════════════════════════════════════════════════════════════════════════════════
OUT_CSV  = DL / 'water_law_global_coded.csv'
OUT_XLSX = DL / 'water_law_global_coded.xlsx'

print('\nSaving...')
df.to_csv(OUT_CSV, index=False, encoding='utf-8-sig')
print(f'  Saved: {OUT_CSV}')
df.to_excel(OUT_XLSX, index=False)
print(f'  Saved: {OUT_XLSX}')

# ════════════════════════════════════════════════════════════════════════════════
# SUMMARY STATISTICS
# ════════════════════════════════════════════════════════════════════════════════
print('\n' + '='*60)
print('JURIMETRIC CODING SUMMARY')
print('='*60)
print(f'\nTotal cases coded: {len(df):,}')

by_country = df[country_col].value_counts() if country_col in df.columns else {}
if len(by_country):
    print(f'\nBy country:')
    for c, n in by_country.items():
        print(f'  {c:<15} {n:>6,}')

print(f'\nHuman rights language:   {df["hr_language"].sum():>5,} ({df["hr_language"].mean()*100:.1f}%)')
print(f'Sustainability language: {df["sust_language"].sum():>5,} ({df["sust_language"].mean()*100:.1f}%)')
print(f'MP involvement (BR):     {df["mp_involvement"].sum():>5,}')
print(f'Indigenous water:        {df["indigenous_water"].sum():>5,}')
print(f'Public interest:         {df["public_interest"].sum():>5,}')

print(f'\nGovernance categories:')
for cat, n in Counter(gov).most_common():
    pct = n/len(df)*100
    bar = '█' * min(int(pct/2), 30)
    print(f'  {cat:<25} {n:>6,} ({pct:.1f}%) {bar}')

# Brazil win/loss
br_mask = df[country_col].isin(['Brazil','BR']) if country_col in df.columns else pd.Series([False]*len(df))
if br_mask.any():
    print(f'\nBrazil win/loss (where coded):')
    wl_counts = df.loc[br_mask, 'win_loss'].value_counts()
    for outcome, n in wl_counts.items():
        print(f'  {outcome:<15} {n:>5,}')

# Cross-tab: HR language by country
if country_col in df.columns:
    print(f'\nHR language by country:')
    xt = df.groupby(country_col)['hr_language'].agg(['sum','count'])
    xt['pct'] = xt['sum'] / xt['count'] * 100
    for c, row in xt.iterrows():
        print(f'  {c:<15} {int(row["sum"]):>5,}/{int(row["count"]):>6,} ({row["pct"]:.1f}%)')

# Cross-tab: governance category by country
if country_col in df.columns:
    print(f'\nTop governance categories by country:')
    for country in df[country_col].unique():
        subset = df[df[country_col] == country]
        top = subset['governance_cat'].value_counts().head(3)
        print(f'  {country}:')
        for cat, n in top.items():
            print(f'    {cat:<25} {n:>5,} ({n/len(subset)*100:.1f}%)')

print('\nDone.')
