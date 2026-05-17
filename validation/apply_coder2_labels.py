import csv
from collections import Counter

LABELS = {
    169: ("NOT_WATER",  "Wet verantwoorde groei melkveehouderij — dairy farming act, no water content"),
    196: ("WATER",      "Construction in watershed protection area (mananciais); demolition ordered"),
    151: ("NOT_WATER",  "Vehicle registration cancellation (tenaamstelling voertuig) — no water"),
    65:  ("WATER",      "Watervergunning for PWN works in Schoorlse duingebied; Waterwet enforcement"),
    117: ("NOT_WATER",  "Asylum/immigration — verblijfsvergunning asiel"),
    40:  ("WATER",      "Discharge into surface water without Waterwet permit; last onder dwangsom"),
    193: ("WATER",      "Churrasqueira built in watershed protection area (mananciais); demolition upheld"),
    164: ("UNCERTAIN",  "No summary available"),
    30:  ("WATER",      "Enforcement includes cleaning fat-contaminated storm water drains (hemelwaterafvoerputten)"),
    200: ("WATER",      "Irregular subdivision in watershed protection area (manancial); state/municipal liability"),
    86:  ("WATER",      "Enforcement: wastewater discharge with PFOA/FRD-903 into municipal sewer"),
    119: ("UNCERTAIN",  "Only states Afdeling confirmed lower court and rejected damages; no water subject identifiable"),
    10:  ("NOT_WATER",  "Odor nuisance from manure processing facility (mestkorrels) — Activiteitenbesluit, not water"),
    150: ("UNCERTAIN",  "No summary available"),
    51:  ("NOT_WATER",  "Meststoffenwet fine for nitrogen/stikstof norm exceedance — fertilizer regulation only"),
    14:  ("WATER",      "Waterwet permit explicitly stated; beroep ongegrond"),
    153: ("NOT_WATER",  "Gambling machine permit (aanwezigheidsvergunning kansspelautomaten) — no water"),
    33:  ("NOT_WATER",  "Meststoffenwet — manure processing obligation (verwerkingsplicht), no water"),
    159: ("NOT_WATER",  "Competition law (Mededingingsrecht) — antitrust cartel fine"),
    198: ("WATER",      "Construction in watershed protection area (mananciais); demolition upheld"),
    75:  ("WATER",      "Waterwet article 5.4 projectplan 'Kadeverlaging Scherpekamp' — flood management"),
    103: ("NOT_WATER",  "Artikel 23 E-wet aansluitplicht — electricity network connection; WOZ valuation. No water"),
    184: ("WATER",      "Illegal subdivision in watershed protection area; municipal responsibility"),
    66:  ("WATER",      "Waterwet: handhavingsverzoek terecht afgewezen — explicitly Waterwet"),
    192: ("WATER",      "Irregular subdivision in watershed area; demolition + refund to buyers"),
    8:   ("NOT_WATER",  "Randvoorwaardenkorting, manure application — cross-compliance, fertilizer regulation"),
    85:  ("WATER",      "Waterwet article 5.4 projectplan 'Hazeldonkse Beek' — watercourse management"),
    53:  ("WATER",      "Waterwet water discharge permit changed — effluent from IAZI wastewater plant"),
    23:  ("WATER",      "Watervergunning: discharge from soil depot into surface water (oppervlaktewaterlichaam)"),
    43:  ("WATER",      "Waterwet art. 5.24 gedoogplicht — dike reinforcement (dijkversterking) project"),
    32:  ("NOT_WATER",  "Meststoffenwet — phosphate norm exceedance and manure transport certificate"),
    115: ("NOT_WATER",  "Fosfaatrechten — dairy farming phosphate rights, EP Protocol — no water"),
    177: ("WATER",      "Irregular building in watershed area (lote de mananciais - APP); regularization order"),
    95:  ("WATER",      "Watervergunning for groundwater extraction (grondwateronttrekking) — Waterwet"),
    146: ("NOT_WATER",  "Fence height (erfscheiding) — building permit dispute, no water content"),
    98:  ("NOT_WATER",  "Fosfaatrechten — dairy milk production and penicillin milk, no water"),
    94:  ("WATER",      "Appeal against Waterwet projectplan declared inadmissible — explicitly Waterwet"),
    46:  ("NOT_WATER",  "Soil contamination enforcement (Wet bodembescherming) — pesticide spray on soil, not water law"),
    157: ("UNCERTAIN",  "No summary available"),
    49:  ("WATER",      "Omgevingsvergunning for water purification of oilfield wastewater for injection — water treatment"),
    179: ("WATER",      "Area of permanent environmental protection (APP); court allows removal of occupants"),
    100: ("NOT_WATER",  "Gas/heat connection (Gaswet art. 66f, Warmtewet) — aansluitplicht gas, not water"),
    171: ("UNCERTAIN",  "Only 'Rectificatiebeslissing' — correction order, no substantive content"),
    172: ("WATER",      "Inert waste deposit in Guarapiranga watershed area; groundwater contamination risk assessed"),
    145: ("NOT_WATER",  "Regular residence permit (verblijfsvergunning regulier) — immigration"),
    104: ("NOT_WATER",  "Artikel 23 E-wet aansluitplicht — electricity network connection obligation"),
    81:  ("UNCERTAIN",  "Bestemmingsplan suspension; petitioner references Waterwet projectplan but land use is core"),
    76:  ("NOT_WATER",  "Meststoffenwet — false VDM manure transport documents; randvoorwaardenkorting"),
    132: ("NOT_WATER",  "Childcare allowance (kinderopvangtoeslag) — no water"),
    133: ("UNCERTAIN",  "No summary available"),
    128: ("UNCERTAIN",  "No summary available"),
    113: ("UNCERTAIN",  "No summary available"),
    54:  ("WATER",      "Enforcement: discharge of urban wastewater (stedelijk afvalwater) — Westland municipality"),
    188: ("WATER",      "Guarapiranga reservoir watershed protection — park construction and environmental protection"),
    105: ("NOT_WATER",  "Artikel 23 E-wet aansluitplicht — electricity connection; same series as 103/104"),
    71:  ("WATER",      "Wastewater discharge from catering: maatwerkvoorschrift for grease trap (vetafscheider)"),
    77:  ("WATER",      "Waterwet watervergunning refused for ground remediation in boezemgebied"),
    84:  ("WATER",      "Waterwet watervergunning for bridge replacement over Vecht river"),
    158: ("NOT_WATER",  "Legal aid for Google defamation appeal — no water"),
    163: ("UNCERTAIN",  "No summary available"),
    56:  ("WATER",      "Waterwet/waterbesluit — open bodemenergiesysteem (ground source heat pump) permit"),
    18:  ("NOT_WATER",  "Meststoffenwet — manure transport company fines, saw shavings classified as manure"),
    22:  ("WATER",      "Watergebiedsplan for Bloemendalerpolder — water quality, flexible levels, drainage routes"),
    44:  ("UNCERTAIN",  "Omgevingsvergunning for manure processing; wastewater quality raised but EIA is primary issue"),
    97:  ("UNCERTAIN",  "Energy park; watervergunning is one of six coordinated permits, not the core subject"),
    181: ("WATER",      "Illegal building in watershed protection area; demolition upheld"),
    28:  ("NOT_WATER",  "Manure processing facility — odor nuisance enforcement refused; no water content"),
    130: ("NOT_WATER",  "Fosfaatrechten — dairy farming, animal health problems"),
    21:  ("NOT_WATER",  "Meststoffenwet — fine for fertilizer norm exceedance"),
    24:  ("WATER",      "Watervergunning application rejected — explicitly water permit, appeal upheld"),
    202: ("WATER",      "Corrego dos Cubas basin degradation — watershed preservation areas; MP action"),
    9:   ("NOT_WATER",  "Randvoorwaardenkorting, low-emission manure application — fertilizer regulation"),
    29:  ("WATER",      "Waterwet watervergunning for barn construction in core zone of regional dike (regionale kering)"),
    195: ("WATER",      "Watershed protection area occupation — court allows removal of residents"),
    15:  ("WATER",      "Multiple permits including watervergunning for bicycle bridge/bypass — Waterwet element present"),
    194: ("WATER",      "Illegal construction in watershed protection area; demolition and environmental recovery"),
    126: ("NOT_WATER",  "Regular residence permit (verblijfsvergunning regulier) — immigration"),
    186: ("WATER",      "Environmental/urban damage in watershed area due to state/municipal oversight failure"),
    182: ("WATER",      "Illegal sewer connections and infiltration risk; MP action; municipality must relocate residents"),
    183: ("WATER",      "Illegal subdivision in watershed area; state, municipality, and citizen all held responsible"),
    70:  ("WATER",      "Waterwet/Waterschapswet: partial revision of water body register (legger oppervlaktewaterlichamen)"),
    50:  ("WATER",      "Watervergunning enforcement — violation of permit conditions"),
    185: ("WATER",      "Illegal building in watershed protection area; referred to environmental chamber"),
    48:  ("WATER",      "Maatwerkvoorschriften for wastewater discharge (lozing) under Blbi; PCP in wastewater"),
    19:  ("WATER",      "Enforcement: discharge of APFO/PFOA in wastewater — appeal upheld"),
    134: ("NOT_WATER",  "Asylum application not taken into consideration — immigration"),
    176: ("WATER",      "Illegal paving in watershed protection area; demolition of cemented area ordered"),
    11:  ("NOT_WATER",  "Meststoffenwet — manure transport company fines, saw shavings from slaughterhouse"),
    175: ("WATER",      "Multiple irregular subdivisions in watershed protection areas; state/municipal responsibility"),
    93:  ("NOT_WATER",  "Manure processing facility — odor nuisance; maatwerkvoorschriften"),
    35:  ("WATER",      "Coordinated permits for Geertjesgolf including explicit Waterwet vergunning"),
}

with open(r"C:\Users\junio\Documents\water-law-dataset\validation\coder2_labels_template.csv",
          encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

missing = []
for row in rows:
    sid = int(row["sample_id"])
    if sid in LABELS:
        row["coder2_label"], row["coder2_notes"] = LABELS[sid]
    else:
        missing.append(sid)

if missing:
    print("MISSING sample_ids:", missing)
    raise SystemExit(1)

print(f"All {len(rows)} rows labelled")
dist = Counter(r["coder2_label"] for r in rows)
print("Label distribution:", dict(dist))

# Write full annotated file (preserves all columns + notes)
fieldnames = list(rows[0].keys())
with open(r"C:\Users\junio\Documents\water-law-dataset\validation\coder2_labels_full.csv",
          "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print("Written: validation/coder2_labels_full.csv")

# Write slim file for kappa_calculator.py (case_id, label)
with open(r"C:\Users\junio\Documents\water-law-dataset\validation\coder2_labels.csv",
          "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["case_id", "label"])
    for row in rows:
        writer.writerow([row["case_id"], row["coder2_label"]])
print("Written: validation/coder2_labels.csv (slim format for kappa_calculator)")
