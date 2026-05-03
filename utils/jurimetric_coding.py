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
        # Quebec FR: aqueduct billing, water supply authority
        r'\baqueduc\b', r'\bréseau d\'eau\b', r'\beau potable\b',
        r'\bapprovisionn\w+.*?eau\b', r'\brégied\'aqueduc\b',
        r'\brégie.*?aqueduc\b', r'\baqueduc.*?régie\b',
        r'\bservice.*?eau\b', r'\beau.*?service\b',
        r'\btaux.*?eau\b', r'\bfacturation.*?eau\b',
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
        # Quebec FR / Canada EN: supply refusal, water service access
        r'\balimentation en eau\b', r'\bapprovisionnement en eau\b',
        r'\bbranchement.*?eau\b', r'\beau.*?branchement\b',
        r'\bwater service.*?refus\w*\b', r'\bwater.*?cut.?off\b',
        r'\bdisconnect.*?water service\b',
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
    # ── Flooding / flood damage claims ───────────────────────────────────────
    # Damage claims and liability from flooding events.
    # flood_protection (above) = infrastructure/defence; this = the damage side.
    ('flooding', [
        r'\binunda[çc][aã]o\b', r'\benchente\b', r'\balagamento\b',
        r'\bdano.*?chuva\b', r'\bdano.*?inunda[çc][aã]o\b',
        r'\bflood(?:ing|plain|damage|s)?\b',
        r'\bflood damage\b', r'\bfloodplain\b',
        r'\binondation\b', r'\bdommage.*?inondation\b',
        r'\boverstromings?\b', r'\bwateroverlast\b',
        r'\bzone inondable\b',
        r'\bwaterschade\b',
        r'\bschadevergoeding.*?wateroverlast\b',
        r'\bstormwater.*?damage\b', r'\bfloodwater.*?damage\b',
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
        # Quebec: lac (lake) access and boundary disputes
        r'\bassociation du lac\b', r'\bassociation.*\blac\b',
        r'\blac\b.*\b(?:riverain|riveraine|droit|pollution|accès|propri[eé]t)\b',
        r'\bniveau du lac\b', r'\blac\b.*\b(?:municipalit[eé]|ville)\b',
        r'\brive\b.*\beau\b', r'\beau\b.*\brive\b',
        r'\blittoral\b', r'\bberge\b',
        r'\bstream\b', r'\bcreek\b', r'\briver.*right\b',
    ]),
    # ── Irrigation / agricultural water ──────────────────────────────────────
    ('irrigation_agricultural', [
        r'\birriga[çc][aã]o\b', r'\b[aáàâã]gua.*?agr[ií]cola\b',
        r'\bagr[ií]cola.*?[aáàâã]gua\b', r'\bperímetro irrigado\b',
        r'\bdistrito de irriga[çc][aã]o\b',
        r'\birrigation\b', r'\birrigation district\b',
        r'\bagricultural water\b', r'\bwater licence.*?farm\b',
        r'\birrigatie\b',
        r'\birrigati\w+.*?eau\b',
    ]),
    # ── Sanitation / sewage / wastewater ─────────────────────────────────────
    ('sanitation_sewage', [
        r'\bsaneamento b[aá]sico\b', r'\besgoto\b', r'\bfossa\b',
        r'\btratamento.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?tratamento\b',
        r'\besta[çc][aã]o de tratamento\b', r'\beta\b',
        r'\bwastewater\b', r'\bsewage\b', r'\bsewer\w*\b',
        r'\bsanitation\b', r'\bwaste water treatment\b',
        r'\bdrainage district\b', r'\bsewerage district\b',
        r'\bstorm sewer\b', r'\bcombined sewer\b',
        r'\briolering\b', r'\bafvalwater\b', r'\bwaterzuivering\b',
        r'\beaux usées\b', r'\bassainissement\b',
        r'\bdrains\b.*?\bwater\b', r'\bwater.*?\bdrains\b',
        r'\bégout\w*\b', r'\bstation d\'épuration\b',
    ]),
    # ── Environmental protection / natural resource management ───────────────
    # Distinct from water_quality (which covers contamination/potability);
    # this captures APA/manancial protection, wetlands, natura 2000, ecological
    # conservation where water is the protected resource.
    ('environmental_protection', [
        # Brazil: APA, manancial, mata ciliar
        r'\bárea de prote[çc][aã]o ambiental\b',
        r'\bmanancial\b',
        r'\bmata ciliar\b',
        r'\bzona de prote[çc][aã]o.*[aáàâã]gua\b',
        r'\b[aáàâã]gua.*zona de prote[çc][aã]o\b',
        r'\bdano ambiental.*[aáàâã]gua\b',
        r'\b[aáàâã]gua.*dano ambiental\b',
        r'\bprote[çc][aã]o.*manancial\b', r'\bmanancial.*prote[çc][aã]o\b',
        r'\breserva hídrica\b', r'\brecurso hídrico.*prote[çc][aã]o\b',
        r'\bzona ripária\b', r'\bapp\b.*\b[aáàâã]gua\b',   # Área de Preservação Permanente
        # EN: wetland, aquatic habitat (Canada/NL)
        r'\bwetland\b', r'\baquatic habitat\b', r'\bfish habitat\b',
        r'\briparian.*protect\b', r'\baquifer protection\b',
        # NL: natura 2000, waterbergingsgebied, ecological water
        r'\bnatura\s*2000\b', r'\bwaterbergingsgebied\b',
        r'\bwaterbeheer.*ecolog\b', r'\becolog.*water\b',
        r'\bbeekherstel\b', r'\bwaternatuur\b',
        r'\bkaderrichtlijn water\b',   # EU Water Framework Directive (NL)
        # FR
        r'\bzone humide\b', r'\bmilieu aquatique\b',
    ]),

    # ── Flood protection infrastructure ───────────────────────────────────────
    # Different from 'flooding' (which = flood damage claims).
    # This captures disputes about dikes, levees, flood barriers — the
    # construction, maintenance, legal status of flood defence works.
    # Dominant in Netherlands (RvS dijk/kade decisions).
    ('flood_protection', [
        r'\bdijk\w*\b', r'\bkade\w*\b', r'\bwaterkering\w*\b',
        r'\bhoogwaterbescherming\b', r'\bprimaire waterkering\b',
        r'\bdijkversterking\b', r'\bdijkverbetering\b',
        r'\bwaterwet\b', r'\bwaterstaatswet\b',
        r'\bveiligheidsnorm.*waterkering\b', r'\bwaterkering.*toetsing\b',
        r'\blevee\b', r'\bseawall\b', r'\bflood barrier\b',
        r'\bflood defence\b', r'\bflood protection.*infrastructure\b',
        r'\bdigue\b', r'\bdike\b',
    ]),

    # ── Spatial planning / land-use permits with water dimension ──────────────
    # Captures NL omgevingsvergunning / bestemmingsplan decisions where water
    # management (drainage, flood risk, watertoets) is a core element.
    # The watertoets (water test) is a mandatory assessment in Dutch planning.
    ('spatial_planning_water', [
        r'\bwatertoets\b',
        r'\bwaterparagraaf\b',
        r'\bwaterbergingsfunctie\b',
        r'\bomgevingsvergunning\b.*\b(?:water|riolering|afwater|overstromingsrisico)\b',
        r'\b(?:water|riolering|afwater|overstromingsrisico)\b.*\bomgevingsvergunning\b',
        r'\bbestemmingsplan\b.*\b(?:water|riolering|overstromingsrisico|waterberging|natte zone)\b',
        r'\b(?:riolering|overstromingsrisico|waterberging)\b.*\bbestemmingsplan\b',
        r'\bhemelwaterberging\b',   # stormwater retention in planning
        r'\bafkoppeling.*riolering\b',  # disconnection from sewer in development
        r'\bstormwater.*zoning\b', r'\bflood risk.*planning\b',
        r'\bfloodplain.*zoning\b', r'\bfloodplain.*bylaw\b',
        r'\bstormwater.*bylaw\b',
    ]),

    # ── Waterboard / drainage district governance ─────────────────────────────
    # NL waterschap (water board) authority decisions: levies, keur (by-law),
    # peilbesluiten (water level decisions), drainage enforcement.
    ('waterboard_governance', [
        r'\bwaterschap\b',
        r'\bwaterschapsbelasting\b', r'\bzuiveringsheffing\b',
        r'\bwaterschapskeur\b', r'\bkeur\b.*\bwaterschap\b',
        r'\bpeilbesluit\b', r'\bwaterpeil\b',
        r'\bafwaterings\w+\b', r'\bpeilgebied\b',
        r'\bpoldergemaal\b', r'\bgemaal\b.*\bwater\b',
        r'\birrigation district\b.*\b(?:levy|rate|tax|decision|bylaw)\b',
        r'\bwater board\b.*\b(?:levy|rate|tax|decision|bylaw)\b',
        r'\bwater authority\b.*\b(?:levy|rate|tax|charge)\b',
        r'\bwater district.*tax\b',
    ]),

    # ── Pipe leak / infrastructure damage liability ────────────────────────────
    # Civil liability for burst mains, leaks from water utility infrastructure.
    # Dominant in Brazil (SABESP/CAESB pipe damage to property).
    ('pipe_leak_damage', [
        r'\bvazamento.*tubula[çc][aã]o\b', r'\btubula[çc][aã]o.*vazamento\b',
        r'\bvazamento.*cano\b', r'\bcano.*vazamento\b',
        r'\brompimento.*cano\b', r'\brompimento.*rede\b',
        r'\bruptura.*tubula[çc][aã]o\b', r'\bruptura.*rede.*[aáàâã]gua\b',
        r'\binfiltração.*[aáàâã]gua.*dano\b',
        r'\bdano.*vazamento.*[aáàâã]gua\b', r'\bvazamento.*dano\b',
        r'\bresponsabilidade civil.*sabesp\b', r'\bsabesp.*responsabilidade civil\b',
        r'\bresponsabilidade civil.*caesb\b', r'\bcaesb.*responsabilidade civil\b',
        r'\bresponsabilidade.*concession[aá]ria.*dano.*[aáàâã]gua\b',
        r'\bdano.*rede.*distribui[çc][aã]o.*[aáàâã]gua\b',
        r'\bwater main break\b', r'\bpipe burst\b',
        r'\bwater leak.*property damage\b', r'\bdamage.*burst.*water\b',
        r'\bwaterleiding.*schade\b',
    ]),

    # ── Water theft / fraud / meter tampering ────────────────────────────────
    # Criminal/civil cases involving illegal water connections, meter fraud,
    # clandestine abstraction. Mainly Brazil (furto de água).
    ('water_theft_fraud', [
        r'\bfurto.*[aáàâã]gua\b', r'\b[aáàâã]gua.*furto\b',
        r'\bfurto.*hidr[oô]metro\b', r'\bhidr[oô]metro.*furto\b',
        r'\badultera[çc][aã]o.*medidor\b', r'\bmedidor.*adultera[çc][aã]o\b',
        r'\bliga[çc][aã]o clandestina\b',
        r'\bfraude.*consumo.*[aáàâã]gua\b',
        r'\bdesvio.*[aáàâã]gua\b', r'\b[aáàâã]gua.*clandestina\b',
        r'\bwater theft\b', r'\bwater meter.*tamper\b',
        r'\billegal.*connection.*water\b', r'\billegal.*water.*abstract\b',
        r'\bongeoorloofde.*wateronttrekking\b',
    ]),

    # ── Public procurement / concession contracts for water works ─────────────
    # Disputes about tenders, contracts, PPPs for water/sanitation infrastructure.
    # Distinct from tariff_dispute (which = individual billing); this = B2G/B2B.
    ('water_infrastructure_contract', [
        r'\blicita[çc][aã]o.*saneamento\b', r'\bsaneamento.*licita[çc][aã]o\b',
        r'\blicita[çc][aã]o.*[aáàâã]gua\b', r'\b[aáàâã]gua.*licita[çc][aã]o\b',
        r'\bconcorrência.*saneamento\b', r'\bobra.*saneamento\b',
        r'\bconcess[aã]o.*saneamento\b', r'\bsaneamento.*concess[aã]o\b',
        r'\bprivati[sz]a[çc][aã]o.*saneamento\b',
        r'\bcontrato.*abastecimento.*[aáàâã]gua\b',
        r'\bempresa.*saneamento.*contrat\b',
        r'\bppp.*[aáàâã]gua\b', r'\b[aáàâã]gua.*ppp\b',
        r'\bwater.*procurement\b', r'\bwater.*concession.*contract\b',
        r'\bpublic.*contract.*water.*service\b',
        r'\bwaterwerk.*aanbesteding\b', r'\baanbesteding.*waterwerk\b',
        r'\bmarché.*eau\b', r'\bcontrat.*eau\b',
    ]),

    # ── Fisheries / aquaculture water rights ─────────────────────────────────
    # Water law intersecting with fisheries management, aquaculture licensing.
    # Canada dominant (BC/AB fisheries, recreational fishing licence decisions).
    # Note: patterns do NOT require "water" as second term — Canadian case titles
    # name the decision-maker ("Regional Manager, Recreational Fisheries & Wildlife")
    # without repeating "water" even when the substance is water-based.
    ('fisheries_water', [
        r'\bfisheries act\b',
        r'\brecreational fish\w+\b',    # Recreational Fisheries & Wildlife Programs
        r'\bfish\w*.*habitat\b', r'\bhabitat.*fish\w*\b',
        r'\bfisheries.*water\b', r'\bwater.*fisheries\b',
        r'\bfishery\b',
        r'\baquaculture\b',
        r'\bfishing.*licen\w+\b', r'\bfishing.*permit\b',
        r'\bdepartment of fisheries\b', r'\bDFO\b',
        r'\bfish.*pass\b',              # fish passage on dams
        r'\bpiscicultura\b', r'\baquicultura\b',
        r'\bpêcheries\b', r'\bpêche.*eau\b', r'\beau.*pêche\b',
        r'\bvisserij\b', r'\bwatervisserij\b',
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
        r'\bwater licen\w+\b', r'\bwater permit\b', r'\bwater allocation\b',
        r'\bwater rights\b', r'\bwater taking\b',
        r'\bwatervergunning\b', r'\bonttrekking\b',
        r'\bpermis.*?eau\b', r'\bautorisati\w+.*?eau\b',
        # Canada: provincial Water Acts and water approval processes
        r'\bwater act\b',               # Alberta/BC/NWT Water Act
        r'\bclean water act\b',
        r'\bsafe drinking water act\b',
        r'\bwater resources act\b',
        r'\bwater sustainability act\b',
        r'\bwater approval\b', r'\bwater licence.*director\b',
        r'\bdirector.*water\b.*\b(?:act|licence|approval)\b',
        r'\benvironment.*water.*approv\w+\b',
        # Quebec FR: water management permits
        r'\bautorisation.*eau\b', r'\bpermis.*eau\b',
        r'\bgestion.*eau\b', r'\bloi sur l\'eau\b',
        r'\bprotection des eaux\b',
    ]),
]

def code_governance(text):
    # Pre-filter: NL immigration/asylum false positives.
    # The RvS handles both immigration appeals and water/planning appeals;
    # if a case is about immigration with no water-infrastructure content,
    # it is a false positive from the broad Rechtspraak keyword search.
    _IMMIGRATION_RE = re.compile(
        r'vreemdelingenrecht|verblijfsvergunning|asielverzoek|asielzoeker'
        r'|ongewenstverklaring|uitzetting.*vreemdeling|vreemdeling.*uitzetting'
        r'|asielrecht|mvv\b|verblijfsrecht',
        re.I
    )
    _WATER_CORE_RE = re.compile(
        r'\bwater(?:schap|leiding|kering|winning|onttrekking|toets|berging|peil|beheer)?\b'
        r'|\bdrinkwater\b|\bgrondwater\b|\briolering\b|\bwateroverlast\b'
        r'|\b[aáàâã]gua\b|\bfornecimento\b|\bsaneamento\b|\bcaesb\b|\bsabesp\b'
        r'|\beau\b|\bhydraulic\b|\baquifer\b|\birrigat\b|\bwetland\b',
        re.I
    )
    if _IMMIGRATION_RE.search(text) and not _WATER_CORE_RE.search(text):
        return 'not_water_related'

    for cat, patterns in GOV_CATS:
        for p in patterns:
            if re.search(p, text, re.I):
                return cat
    return 'other_water'

# ════════════════════════════════════════════════════════════════════════════════
# 4. WIN/LOSS — who prevailed
# ════════════════════════════════════════════════════════════════════════════════
# Three tiers of pattern strength:
#   Tier 1 — UNAMBIGUOUS: outcome is structurally determined regardless of who
#            filed the appeal (cobranÃ§a indevida, restabelecimento, corte indevido).
#            Safe to apply to all Brazilian courts.
#   Tier 2 — CONTEXTUAL: outcome word co-occurs with water keyword (provido +
#            água, procedente + água). Works for TJSC/TJRJ/TJSP where ementas
#            are tightly structured.
#   Tier 3 — TJDFT-LENIENT: procedente/improcedente with CAESB or water context
#            in the summary text. TJDFT is pre-filtered to water disputes so
#            bare procedente is reliable; used only when tribunal == TJDFT.

# ── Tier 1: unambiguous (all courts) ──────────────────────────────────────────
WIN_USER_T1 = [
    # Charge ruled improper → user wins regardless of appeal direction
    r'\bcobran[çc]a indevida\b', r'\bcobran[çc]a abusiva\b',
    r'\bcobran[çc]a irregular\b',
    r'\bvalor indevido.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?valor indevido\b',
    # Service restoration ordered → utility was in the wrong
    r'\brestabelec\w+.*?fornecimento\b', r'\brestabelec\w+.*?[aáàâã]gua\b',
    r'\bfornecimento.*?restabelecid\w+\b',
    # Illegal / improper disconnection confirmed as such
    r'\bcorte.*?indevid\b', r'\bcorte.*?ileg[ií]t\b',
    r'\bsuspens[aã]o.*?indevida\b', r'\bsuspens[aã]o.*?ileg[ií]tima\b',
    r'\binterrup[çc][aã]o.*?indevida\b', r'\bdesligamento.*?indevido\b',
    # Utility explicitly condemned to pay/act
    r'\bcaebs.*?condenada?\b', r'\bcondenada?.*?caesb\b',
    r'\bconcession[aá]ria.*?condenada?\b', r'\bcondenada?.*?fornec\w+\b',
    r'\bdano moral.*?configurado.*?[aáàâã]gua\b',
    r'\b[aáàâã]gua.*?dano moral.*?configurado\b',
    r'\bdano moral.*?caesb\b.*?\bconfigurado\b',
    # Connection/supply ordered (obligation to connect)
    r'\bobriga[çc][aã]o de fazer.*?fornecer [aáàâã]gua\b',
    r'\bfornecer [aáàâã]gua.*?obriga[çc][aã]o de fazer\b',
    r'\bliga[çc][aã]o.*?deferida\b', r'\breliga[çc][aã]o.*?determinada\b',
    r'\bordem.*?ligar.*?[aáàâã]gua\b', r'\bliga[çc][aã]o predial.*?deferida\b',
    # English
    r'\bmandatory.*?water.*?connection\b', r'\bwater.*?reconnect\w+.*?order\w*\b',
]
WIN_UTIL_T1 = [
    # Charge ruled proper → utility wins
    r'\bcobran[çc]a devida\b', r'\bcobran[çc]a leg[ií]tima\b',
    r'\bcobran[çc]a regular\b',
    # Legal / legitimate disconnection confirmed
    r'\bcorte.*?leg[ií]tim\b', r'\bsuspens[aã]o.*?leg[ií]tima\b',
    r'\binterrup[çc][aã]o.*?leg[ií]tima\b',
    r'\bcorte.*?devido\b', r'\bsuspens[aã]o.*?devida\b',
    # Debt confirmed (consumer owes, utility may disconnect)
    r'\bd[eé]bito.*?devido.*?[aáàâã]gua\b', r'\b[aáàâã]gua.*?d[eé]bito.*?devido\b',
    # English
    r'\bwater.*?disconnect.*?lawful\b', r'\butility.*?prevail\w*\b',
]

# ── Tier 2: contextual (all courts, outcome + água word) ──────────────────────
WIN_USER_T2 = [
    r'\bprovido\b.*\bdireito [aáàâã] [aáàâã]gua\b',
    r'\bdireito [aáàâã] [aáàâã]gua\b.*\bprovido\b',
    r'\bdireito [aáàâã] [aáàâã]gua\b.*\bprocedente\b',
    r'\bprocedente\b.*\b[aáàâã]gua\b',
    r'\bliga[çc][aã]o.*?[aáàâã]gua.*?deferida\b',
    r'\bresponsabilidade.*?empresa.*?[aáàâã]gua\b',
    r'\bdano moral.*?[aáàâã]gua.*?provid\w+\b',
    r'\bpedido.*?procedente.*?[aáàâã]gua\b',
    r'\b[aáàâã]gua.*?pedido.*?procedente\b',
    r'\border\w*.*?prov\w+.*?water\b', r'\bwater.*?order\w*.*?prov\w+\b',
    r'\bdismiss\w+.*?water\b',  # EN: challenge dismissed → utility approach won
]
WIN_UTIL_T2 = [
    r'\bimprovido\b.*\b[aáàâã]gua\b', r'\b[aáàâã]gua\b.*\bimprovido\b',
    r'\bimprocedente\b.*\b[aáàâã]gua\b', r'\b[aáàâã]gua\b.*\bimprocedente\b',
    r'\bcorte.*?[aáàâã]gua.*?leg[ií]tim\b',
    r'\bsuspens[aã]o.*?leg[ií]tima.*?[aáàâã]gua\b',
    r'\bd[eé]bito.*?[aáàâã]gua.*?prov\w+\b',
    r'\bwater.*?claim.*?dismiss\w+\b',
]

# ── Tier 3: TJDFT-lenient (only when tribunal == TJDFT) ───────────────────────
# TJDFT data is pre-filtered to water disputes — bare procedente/improcedente
# reliably identifies the outcome for the water claim.
WIN_USER_T3 = [
    r'\bprocedente\b',
    r'\bdar provimento\b', r'\bdou provimento\b', r'\bprovimento dado\b',
    r'\bsentença reformada.*?favor\w*\b',
]
WIN_UTIL_T3 = [
    r'\bimprocedente\b',
    r'\bnegar provimento\b', r'\bnegado provimento\b', r'\bprovimento negado\b',
    r'\bnego provimento\b',
]

MIXED_PATTERNS = [
    r'\bparcialmente provido\b', r'\bprovimento parcial\b',
    r'\bparcialmente procedente\b', r'\bprovido em parte\b',
    r'\bparcial provimento\b', r'\bapela[çc][aã]o parcialmente\b',
]

WIN_USER_RE_T1 = [re.compile(p, re.I | re.DOTALL) for p in WIN_USER_T1]
WIN_UTIL_RE_T1 = [re.compile(p, re.I | re.DOTALL) for p in WIN_UTIL_T1]
WIN_USER_RE_T2 = [re.compile(p, re.I | re.DOTALL) for p in WIN_USER_T2]
WIN_UTIL_RE_T2 = [re.compile(p, re.I | re.DOTALL) for p in WIN_UTIL_T2]
WIN_USER_RE_T3 = [re.compile(p, re.I | re.DOTALL) for p in WIN_USER_T3]
WIN_UTIL_RE_T3 = [re.compile(p, re.I | re.DOTALL) for p in WIN_UTIL_T3]
MIXED_RE       = [re.compile(p, re.I | re.DOTALL) for p in MIXED_PATTERNS]

def code_win_loss(text, country, tribunal=''):
    if country not in ('Brazil', 'BR'):
        return 'not_coded'

    # Mixed check first (applies to all courts)
    if any(r.search(text) for r in MIXED_RE):
        return 'mixed'

    # Tier 1 — unambiguous (all courts)
    u1 = any(r.search(text) for r in WIN_USER_RE_T1)
    v1 = any(r.search(text) for r in WIN_UTIL_RE_T1)
    if u1 and not v1: return 'user_wins'
    if v1 and not u1: return 'utility_wins'
    if u1 and v1:     return 'mixed'

    # Tier 2 — contextual (all courts)
    u2 = any(r.search(text) for r in WIN_USER_RE_T2)
    v2 = any(r.search(text) for r in WIN_UTIL_RE_T2)
    if u2 and not v2: return 'user_wins'
    if v2 and not u2: return 'utility_wins'
    if u2 and v2:     return 'mixed'

    # Tier 3 — TJDFT-lenient: only apply when there is actual water-utility context
    # in the summary text. Guards against false-positive TJDFT records (real estate,
    # electricity, pension cases that incidentally matched water search keywords).
    # T3 guard: require explicit water-utility context — CAESB, or water service
    # billing/supply language. This filters out false-positive TJDFT records
    # (criminal, real estate, pension cases that incidentally mention "água").
    T3_GUARD = re.compile(
        r'caesb'
        r'|companhia de saneamento'
        r'|concession[aá]ria.*?[aáàâã]gua|[aáàâã]gua.*?concession[aá]ria'
        r'|fatura.*?[aáàâã]gua|conta de [aáàâã]gua|tarifa.*?[aáàâã]gua'
        r'|fornecimento.*?[aáàâã]gua|[aáàâã]gua.*?fornecimento'
        r'|cobran[çc]a.*?[aáàâã]gua|[aáàâã]gua.*?cobran[çc]a'
        r'|medidor.*?[aáàâã]gua|hidr[oô]metro'
        r'|liga[çc][aã]o.*?[aáàâã]gua|[aáàâã]gua.*?esgoto',
        re.I
    )
    if 'TJDFT' in str(tribunal).upper() and T3_GUARD.search(text):
        u3 = any(r.search(text) for r in WIN_USER_RE_T3)
        v3 = any(r.search(text) for r in WIN_UTIL_RE_T3)
        if u3 and not v3: return 'user_wins'
        if v3 and not u3: return 'utility_wins'
        if u3 and v3:     return 'mixed'

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
countries  = df[country_col].fillna('').tolist() if country_col in df.columns else [''] * len(df)
tribunals  = df['tribunal'].fillna('').tolist() if 'tribunal' in df.columns else [''] * len(df)

hr, sust, gov, wl, mp, ind, pub = [], [], [], [], [], [], []

for i, (text, text_sub, country, tribunal) in enumerate(zip(texts, texts_sub, countries, tribunals)):
    if i % 5000 == 0:
        print(f'  {i:,}/{len(df):,}...', flush=True)
    hr.append(code_hr(text_sub))
    sust.append(code_sust(text_sub))
    gov.append(code_governance(text))
    wl.append(code_win_loss(text_sub, country, tribunal))
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
