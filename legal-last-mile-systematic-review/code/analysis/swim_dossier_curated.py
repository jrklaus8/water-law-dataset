"""Hand-picked source passages for the four SWiM core studies the author kept in open item A28 (2026-10-14: S920, S1102, S1146 and the DRC trial, S366), for the source-verification dossier. The quotes for the six studies the author excluded under A28 (S1020, S1042, S1057, S1144, S1163, S947) are in the archived 37-study dossier, 11_archive/SWIM_37_SOURCE_VERIFICATION_DOSSIER_2026-10-14.md.

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
    'S366': {
        'summary': "The PDF on file is the 2021 BMJ Global Health report of the trial, which is the report catalogued as S366 (the 2025 companion report, S294, has no PDF on file and carries no effect row). Exposure in the trial: the DRC government's national Healthy Villages and Schools (VEA) programme, "
                   "a community-driven WASH programme that works through village WASH committees, randomised by cluster. Outcome in the effect row: whether the household's primary drinking-water source is improved (83% in intervention clusters against 43% in control clusters; adjusted ITT difference 0.33, "
                   "95% CI 0.22 to 0.45). The author kept this study under A28 and anchored the Family B row to this estimate.",
        'quotes': [
            ('Programme', "Since 2008, the Democratic Republic of Congo government has implemented a national programme, Healthy Villages and Schools (Villages et Ecoles Assainis (VEA), with support from UNICEF, financed by UK’s Foreign, Commonwealth and Development Office."),
            ('Programme aim', "The VEA’s main objective is to support improved access to WASH, especially in rural areas."),
            ('Design and sample', "A cluster-level randomised controlled trial of VEA was implemented throughout 2019 across 332 rural villages, grouped into 50 treatment and 71 control clusters."),
            ('Primary access result', "In the intervention group, 83% of households reported that their primary water source was improved, compared with 43% in the control group (adjusted treatment effect 33% points; 95% CI 22 to 45) (table 2)."),
            ('Table 2 row', "Improved water source 732 0.43 580 0.83 0.33 (0.22 to 0.45)"),
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
