# Jurimetric Coding

The dataset includes seven jurimetric variables coded by the `utils/jurimetric_coding.py` engine (**version 2.0**, with the **v0.3.0 residual fix**) using regular-expression pattern matching across Portuguese, English, Dutch and French. All figures below are for dataset **v0.3.0** (83,596 decisions: Brazil 11,724 · Netherlands 68,654 · Canada 3,218). Full country tables are on [[Key Findings]]; the audit behind the v0.3.0 engine is on [[Validation]].

---

## Variables

### 1. `hr_language` — Human rights / right-to-water framing

**Definition:** whether the decision treats water access as a fundamental right rather than a commercial service dispute.
**Coded from:** the case summary (`inhoudsindicatie` / `ementa`) only, to avoid false positives from procedural metadata.

| Country | HR language | % |
|---------|-------------|---|
| Brazil | 226 / 11,724 | 1.93% |
| Canada | 0 / 3,218 | 0.0% |
| Netherlands | 0 / 68,654 | 0.0% |

HR language is 0.0% in the Brazilian informal-settlement decisions specifically.

### 2. `sust_language` — Sustainability framing

**Definition:** whether the decision invokes sustainability, environmental protection or intergenerational equity language. Coded from the case summary only. (The count of 193 cases reported for the earlier release has not been recomputed in the v0.3.0 documents; recompute it from the coded CSV if you need it.)

### 3. `governance_cat` — Governance category (21 values)

**Definition:** the primary dispute type. Nineteen substantive categories are matched by patterns, plus two residual values:

| Group | Categories |
|-------|-----------|
| Household service | `tariff_dispute`, `connection_refusal`, `informal_settlement`, `pipe_leak_damage`, `water_theft_fraud`, `water_quality`, `sanitation_sewage`, `water_infrastructure_contract` |
| Resource and infrastructure governance | `groundwater`, `riparian_waterway`, `irrigation_agricultural`, `fisheries_water`, `hydroelectric_dam`, `regulatory_permit` |
| Environment, flood and planning | `environmental_protection`, `flooding`, `flood_protection`, `spatial_planning_water`, `waterboard_governance` |
| Residual | `other_water` (water vocabulary present but no specific category — the **genuine residual**, 6,904 decisions or 8.3%), `not_water_related` (no substantive water vocabulary — 67,703 decisions or 81.0%) |

The thesis-critical categories are `tariff_dispute`, `connection_refusal` and `informal_settlement`.

### 4. `win_loss` — Litigation outcome *(Brazil only)*

**Definition:** whether the household/user or the utility won.

| Outcome | Count | % of coded |
|---------|-------|-----------|
| `user_wins` | 1,400 | 31.2% |
| `utility_wins` | 1,165 | 26.0% |
| `mixed` | 1,916 | 42.8% |
| `unclear` / not coded | ~7,243 | — |

Win/loss coding covers 4,481 decisions. It is unavailable where outcome language is non-standard, especially for TJDFT (Brasília), which uses administrative-docket framing. By thesis-critical category: tariff dispute 18.4% user wins (n = 5,689), connection refusal 17.3% (n = 1,275), **informal settlement 0.0% (n = 88)**. The coding is AI-assisted and only partly validated; the Netherlands and Canada carry no outcome coding.

### 5. `mp_involvement` — Ministério Público *(Brazil only)*

Whether the Ministério Público acts as a public-interest litigant: 427 cases (3.6% of Brazilian cases).

### 6. `indigenous_water` — Indigenous / First Nations water rights

**Result in v0.3.0: 0 cases.** This is almost certainly an undercount caused by keyword coding on title-only CanLII records (86.9% of Canadian records are title-only), not evidence that no such disputes exist.

### 7. `public_interest` — Collective / public-interest framing

Whether the case is framed as a collective action or public-interest matter (class action, diffuse rights): 1,616 Brazilian cases (13.8%).

---

## Coding engine

- **Text scope:** human-rights and sustainability patterns are applied to the summary only; governance patterns are applied to all text fields.
- **Languages:** Portuguese (`[aáàâã]gua`, `abastecimento`), English (`water supply`, `right to water`), Dutch (`waterlevering`, `drinkwater`), French (`eau`, `fourniture`).
- **False-positive control (v0.3.0):** every decision is checked for substantive water vocabulary in its title or summary; decisions without any are coded `not_water_related`. Three Brazil rescue patterns (tariff, connection, pipe damage) recover cases the main regexes missed.
- **Early finding that shaped the design:** restricting the human-rights and sustainability variables to summary text was necessary after early tests found over 98% false positives from `legal_area = "Direito à Água / Saneamento"`, a court classification label rather than rights framing.

See the [source code](https://github.com/jrklaus8/water-law-dataset/blob/main/utils/jurimetric_coding.py) for every pattern.

> **Separate from the systematic review.** The systematic review ([[Systematic Review]]) codes studies, not court decisions, with its own 92-field extraction codebook and a two-column direction coding (raw sign and substantive direction). The two coding schemes are independent.
