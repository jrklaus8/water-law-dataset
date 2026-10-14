"""Hand-picked source passages for the ten SWiM core studies flagged in open item A28 (2026-10-14), for the source-verification dossier.

Each quote is copied from the paper's text layer (ligatures expanded, whitespace collapsed; see source_text_tools.py) and is CHECKED against the PDF every time the dossier is built: a quote that is not found
is a build error, never silently dropped. The `summary` is the AI's neutral description of the paper's own exposure and outcome, written from these quotes; it is not a ruling and carries no recommendation.
Each entry is (label, quote). The page is found by the builder, not typed here.
"""

CURATED = {
    'S920': {
        'summary': "Exposure in the paper: who implements and runs a small rural piped-water system, a community water user association following a participatory approach (the municipality signs a concession contract that transfers responsibility "
                   "to the association) against the local government without specific user participation. Outcome: the increase in rural access to piped water on premises between the 2000 and 2010 censuses (difference-in-differences with kernel matching). "
                   "The only legal or administrative device the located passages mention is the concession contract; the paper contrasts two management models and does not test a rule or its enforcement.",
        'quotes': [
            ('Exposure and comparator', "systems implemented, operated, and maintained by water user associations following a participatory approach and systems implemented, operated and maintained by local governments without any specific user participation"),
            ('Legal or administrative element', "In most cases, the local government only signs a concession contract to transfer responsibility for water supply to the association."),
            ('What the contrast is', "responsibility for implementation and management with user associations or with local governments, enables the present study to evaluate the success of demand-driven participatory provision of piped water against traditionally implemented and managed piped water supply systems"),
            ('Outcome', "evaluates and compares the increases in access rates to piped water on premises"),
            ('Estimate', "In municipalities where user associations are involved in the implementation of new projects, the projects lead to an increase in rural access rates that is around six percentage points higher than in municipalities where the investments are solely made by the municipal administration."),
            ('Sample', "# of observations 592 583 3717"),
        ]},
    'S1020': {
        'summary': "Exposure in the paper: residence in a micro-watershed treated by the state's Rajiv Gandhi Mission for Watershed Development programme (pond construction, trenches, tree planting, gully plugs) against a matched untreated watershed. "
                   "Outcome: dry-season domestic water collection time (minutes a day), with agricultural returns as the other outcomes. The paper evaluates a physical rural-development programme; the located passages describe no legal or administrative access rule.",
        'quotes': [
            ('Exposure and comparator', "These challenges inform some of the objectives of the state-level Rajiv Gandhi Mission for Watershed Development (RGWDM) programs, which consolidated all watershed programs in 1994 and has since treated over 1.4 million hectares of land in 7,600 villages by 2006."),
            ('What the programme did', "Responding to domestic water problems, a significant financial investment was made in pond construction accounting for US$81,732."),
            ('Outcome', "Three outcome indicators are derived from the available data: (a) gross returns to kharif agriculture (monsoon crop); (b) gross returns to rabi agriculture (post-monsoon crop); and, (c) domestic water collection time in the dry season (March through July)."),
            ('Estimate and sample', "Full matched sample (n = 470) 17.37 (2.46)"),
        ]},
    'S1042': {
        'summary': "Exposure in the paper: (i) a dummy for whether a community-based organisation (CBO) exists in the municipality and (ii) municipality-wide survey averages of town-hall participation and readiness to exert peer pressure. Outcome: the mayor's valuation "
                   "of access to water in the municipality on a 1 to 4 scale (not a household measure). Sample: about 7.2% of municipalities in two Ukrainian regions. The paper presents CBOs as a vehicle for participation; it notes their legal form (civic organisations or charitable foundations) but the legal form is not the exposure.",
        'quotes': [
            ('Exposure and outcome', "I estimate the effect of participation and established CBOs on the mayors’ valuations of five different public goods and services."),
            ('Legal form of CBOs', "Within Ukrainian legislation, CBOs are typically registered as civic organizations or charitable foundations."),
            ('Why CBOs are studied', "The aim of CBO establishment, as envisaged by development agencies, is to facilitate and harness local community participation (EU 2006)."),
            ('Variable definitions (exposure)', "CBO Dummy for CBO existence within a municipality 0.48 0.50 0 1 TOWNHALL Average municipality-wide frequency of participation in the town hall meetings (1–5 scale)"),
            ('Variable definition (outcome)', "WATER Mayors’ valuation of the access to water within the municipality (1–4 scale)"),
            ('Sample', "Roughly 7.2 % of municipalities were randomly sampled in both regions."),
            ('Result', "I find CBO dummy to be consistently significant only in the specifications with water supply quality as a dependent variable."),
        ]},
    'S1057': {
        'summary': "Exposure in the paper: household and community participation in the design of, and local decision-making about, community-based water services in government demand-responsive rural water programmes (Sri Lanka; Karnataka and Maharashtra, India). "
                   "Outcome: household water-collection time saved (log) and satisfaction with the design. The programme is described as a joint effort of community members and government staff; no legal or administrative access rule is the exposure.",
        'quotes': [
            ('Exposure and programme', "This demand-responsive approach calls for a joint effort by community members and government staff in service design, construction, and operation and maintenance (O&M)."),
            ('What the paper finds first', "well-designed services involve more community members in the design process and final decision-making about service type"),
            ('Estimate and sample', "Karnataka Maharashtra 1.63 * (0.95) 2.92 *** (0.95) 1.06 *** (0.38)"),
            ('Outcome', "Notes: Dependent variable is the log of household-level time-saving."),
        ]},
    'S294': {
        'summary': "IMPORTANT: the PDF on file under S294 is the 2021 BMJ Global Health report of the same trial (the paper catalogued as S366), not the 2025 paper catalogued as S294 whose diarrhoea, child-growth and institutions results are stored in effect_sizes.csv. "
                   "The quotes below are from the 2021 report and describe the programme and the trial. Exposure in the trial: the DRC government's national Healthy Villages and Schools (VEA) programme, a community-driven WASH programme that works through village WASH committees, randomised by cluster. "
                   "The 2021 report's title names infrastructure, access, behaviour and governance as its outcomes, so the stored S294 estimates (diarrhoea, child growth, an institutions index) cannot be checked against this file; stored numbers that happen to appear in it are probably coincidences.",
        'quotes': [
            ('Programme', "Since 2008, the Democratic Republic of Congo government has implemented a national programme, Healthy Villages and Schools (Villages et Ecoles Assainis (VEA), with support from UNICEF, financed by UK’s Foreign, Commonwealth and Development Office."),
            ('Programme aim', "The VEA’s main objective is to support improved access to WASH, especially in rural areas."),
            ('Design and sample', "A cluster-level randomised controlled trial of VEA was implemented throughout 2019 across 332 rural villages, grouped into 50 treatment and 71 control clusters."),
            ('Sample', "leaving a sample of 121 clusters in four provinces and 332 villages (figure 1)."),
        ]},
    'S1102': {
        'summary': "Exposure in the paper: household participation in community-based rural drinking-water projects, measured two ways: attending project meetings and contributing to capital costs (cash, labour or materials). Outcome: an index of water improvements and household satisfaction, "
                   "estimated by propensity-score matching in 45 Indian villages. The contribution each village was supposed to make is a project requirement, which the paper treats as household participation rather than as a legal cost-sharing rule.",
        'quotes': [
            ('Exposure', "During the planning or implementation stage of a project, each village was supposed to come up with a certain amount of contribution, whether in cash, labour or materials and this is the focus of the second equation."),
            ('Design', "Using propensity score matching, this study concludes that participation leads to benefits for the households that participate although these benefits are strongest in regions with higher levels of overall participation."),
            ('Sample', "For this research, a total of 1523 households were surveyed from 45 villages across the two projects; data collection took place in 1999 and 2000."),
            ('Treatment and comparison', "each household in the treatment (participation) sample is then matched with replacement to the nearest five neighbours who did not participate."),
        ]},
    'S1144': {
        'summary': "Exposure in the paper: social proximity, chiefly survey-measured trust in NGOs and CBOs, among urban poor households in Kampala. Outcome: whether the household obtains sanitation or solid-waste services supplied by an NGO or CBO. "
                   "Logit models on 337 households from 12 informal settlements (the NGO and CBO sanitation models use 192 and 189). The exposure is an attitude measure and the outcome is use of NGO or CBO services, not a legal rule or a public-network connection.",
        'quotes': [
            ('Exposure', "Special emphasis is put on analysing the role of social proximity, in comparison with more conventional (spatial proximity, performance perception and socio-economic) factors, in explaining access of the poor to urban services in Kampala, Uganda’s capital city."),
            ('Sample', "Using a sample of 337 households from 12 poor informal settlements in Kampala, social proximity in addition to other conventional factors proved relevant in explaining access of the poor to NGO and CBO solid waste and sanitation services."),
            ('Estimate', "SNF Trust1) Membership 7.014 (1.352)*** -0.509 (0.614) 1.010 -0.065 9.029 (1.706)***"),
            ('How trust is treated', "Social proximity factors such as trust are difficult to address empirically because ‘people carry it inside their heads’"),
        ]},
    'S1163': {
        'summary': "Exposure in the paper: whether the rural school had WaSH programmes sponsored, supported or implemented by an external organisation in the last year, among many school-level factors. Outcome: at least a basic, continuously available on-premises water service at the school. "
                   "Multilevel logistic regression on a survey of rural schools in 14 low- and middle-income countries. The exposure is external programme support, not a legal or administrative rule. The paper reports 2,690 surveys in 14 countries; the stored row says 2,677 schools in 13 countries (see the sample passage).",
        'quotes': [
            ('Exposure (question asked)', "Have there been any WASH programs sponsored/supported/implemented by an external organization here at the school in the last year?"),
            ('Estimate', "or had WaSH programs sponsored, supported, or implemented by an external organization in the last year (OR = 1.4, p = 0.021)."),
            ('Outcome', "basic, on-premises water service if more children were enrolled at the school (OR = 1.1, p = 0.034)"),
            ('Sample', "We conducted 2690 surveys and collected 1946 water samples at randomly selected schools in rural areas of 14 low- and middle-income countries (LMICs)."),
        ]},
    'S947': {
        'summary': "Exposure in the paper's abstract: dependence on natural resource rents. The stored exposure is a control variable, the World Bank Worldwide Governance Indicators 'regulation quality' index, which the paper describes as a perception measure of institutional capacity. "
                   "Outcome: the share of the population with access to water and sanitation, in 44 African countries over 1995 to 2017, two-step system GMM. The paper's own question is the resource curse; no legal rule or mechanism is tested.",
        'quotes': [
            ('What the paper investigates', "This paper therefore investigates the effect of natural resource dependence on access to water and sanitation in 44 African countries, with data covering the period 1995–2017."),
            ('How institutions enter', "The third category of variables is an approximation of institutional capacity as measured by the quality of regulation."),
            ('What the index is', "Regulation quality captures perceptions of the ability of the government to formulate and implement sound policies and regulations that permit and promote private sector development."),
            ('Estimate', "0.0109*** (0.00278) 0.0121*** (0.00346)"),
        ]},
    'S1146': {
        'summary': "Exposure in the paper: the regional incidence of corruption in the utilities sector, the share of households in a region reporting utilities corruption (Afrobarometer round 7). Outcome: whether the household reports having enough clean water "
                   "(probit marginal effects, country fixed effects). The exposure is a governance-quality measure rather than a rule or mechanism of access.",
        'quotes': [
            ('Exposure and outcome', "Using data from the seventh round of the Afrobarometer, we find that a greater regional incidence of corruption in the utilities sector is associated with a reduced likelihood that a household reports that it has access to enough clean water."),
            ('Exposure scale', "This would represent a very large change in the share of households reporting utilities corruption—from zero to 70%."),
            ('Sample', "Observations 44,778 44,887 44,778 44,887 44,887 20,267 24,511"),
            ('Individual versus regional', "While a household that has paid a bribe is more likely to have a water access point, the regional incidence of utilities corruption predicts that the household will not have enough clean water."),
        ]},
}
