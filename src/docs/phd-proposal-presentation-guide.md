# Guide to Presenting the PhD Research Proposal Page

This document is a practical reading and presentation guide for the `/phd-proposal/` page on the site. It explains what each section contains, why it is structured that way, and how to walk a supervisor or selection committee through it during a PhD interview or informal meeting.

---

## Overview: What the Page Is

The page is a structured, web-native version of the two-page written proposal (`research-proposal.pdf`). It covers the same content but breaks it into clearly labelled sections that are easy to navigate in a browser. It is designed to be used in two ways:

1. **As a self-standing document** — a supervisor or committee member can read it independently before or after a meeting.
2. **As a live presentation aid** — you can scroll through it during a video call or in-person meeting, using each section as a talking prompt.

A link to download the original PDF is provided at the top (in the meta bar) and at the bottom of the page.

---

## Section-by-Section Reading Guide

### Meta bar (top strip)
Shows programme (ForFuS Doctoral Training Unit · LIST), duration (48 months), and date (June 2026) at a glance. The **Download PDF** link is here — offer it early in a conversation so the other person can follow along on paper if they prefer.

---

### Abstract box (blue-bordered block)
This is the single most important paragraph on the page. It states in three sentences what the current knowledge gap is, what the PhD will do to close it, and in what institutional and programme context. **Always start here when presenting.** If you only have 30 seconds, read this aloud and stop.

Key message: *"Current models can't resolve foliar water uptake and forest floor evaporation from the dominant transpiration signal. This PhD will use isotopic tracers and sub-canopy micrometeorology to quantify them across three sites over 48 months at LIST — within the ForFuS training unit."*

---

### 1. Problem Statement and Motivation
This section answers *"why does this PhD need to exist?"* Three building blocks:

- **The ET partitioning assumption** — Penman-Monteith and Shuttleworth-Wallace assume transpiration dominates the forest water flux. Forest floor evaporation is treated as a residual, and energy balance non-closure (10–30% of Rn) buries it further. This is the observational gap.
- **The foliar water uptake inversion** — during severe drought, the hydraulic gradient along the soil-plant-atmosphere continuum can reverse. Neither sap flow sensors nor above-canopy eddy covariance can detect foliar uptake independently. This is the process gap.
- **The climate change context** — increasing drought frequency and severity in central Europe means these minor pathways have growing relevance for predicting forest mortality risk and informing management decisions.

**Presentation tip:** Don't rush the second point — the concept of a reversed hydraulic gradient is counterintuitive. Explain it as: "normally water moves from soil to leaf to atmosphere; during extreme stress, the leaf can become a net water importer rather than a net exporter." This is the most scientifically striking point in the motivation and worth a moment's pause.

---

### 2. Research Questions
Three research questions, each addressing one progressive component of the overall problem:

| RQ | Addresses | What a good answer achieves |
|---|---|---|
| RQ1 | Quantification | Establishes the magnitude and site-to-site variation of the target fluxes |
| RQ2 | Method | Tests whether isotopic tracers can reliably separate these fluxes from the transpiration signal |
| RQ3 | Integration | Connects the observational findings to a modelling framework with drought resilience implications |

**Presentation tip:** Frame this as a deliberate progression from "how large is the signal?" to "can we measure it reliably?" to "what does it mean for models?" This de-risks the project: if RQ1 yields a well-constrained dataset and RQ2 establishes methodological limits, the PhD has already produced a publishable contribution before the modelling work in RQ3 is complete.

---

### 3. Work Packages
Five WPs, each shown as a colour-coded card with a badge. The pipeline logic runs WP1 → WP2 + WP3 in parallel → WP4 → WP5.

**How to walk through them:**

- **WP1** is the foundation. Stress that the multi-site observational dataset it produces by end of Year 1 is a publishable output in itself — a standalone contribution (data paper or methods paper) even if later WPs require more time than planned.
- **WP2** is the isotopic analysis. Key word: *Bayesian*. The mixing models are implemented in a Bayesian framework so that uncertainty in source proportions is explicitly propagated rather than collapsed into a point estimate.
- **WP3** runs in parallel with WP2. Emphasise the cross-validation between the energy balance approach (WP3) and the isotopic mass balance (WP2) as the central methodological safeguard. If both methods converge, the result is robust; if they diverge, the nature of the discrepancy is itself scientifically informative.
- **WP4** begins once the observational baseline is established (Year 2). Avoid over-specifying which modelling platform will be used — the appropriate framework will be informed by what Prof. Keim's group uses and what the WP2–3 data support. Describe it as "a stand-scale ecohydrological model with explicit process representations of foliar uptake and forest floor evaporation."
- **WP5** is the synthesis in Year 4. This is where the inter-site comparison pays off scientifically and where the implications for forest management and drought resilience modelling are articulated for a broader audience.

---

### 4. Project Timeline
A visual Gantt-style bar chart showing which WPs are active in each of the four years. Three things to point out:

1. **Year 1 is publishable on its own** — WP1 produces the multi-site dataset. Even if modelling work in WP4 slips, there is a standalone scientific output.
2. **WP2 and WP3 overlap throughout Years 1–2** — isotopic analysis and sub-canopy energy balance measurement run in parallel, allowing cross-validation as data accumulate rather than waiting for one to complete before starting the other.
3. **WP4 and WP5 are sequenced deliberately** — modelling begins once the observational basis is established, and the inter-site synthesis comes last when all three sites have comparable data coverage.

**Presentation tip:** Use the timeline to demonstrate that you have thought through sequencing and risk. Supervisors want to see that Year 1 has a clear, achievable deliverable that does not depend on later WPs succeeding.

---

### 5. Expected Challenges and Mitigations
Four cards, one per challenge. Each states the challenge name, a one-line description of why it is a problem, and the specific technical mitigation already built into the project design.

This section demonstrates methodological maturity — the challenges are anticipated, not afterthoughts:

- **Energy balance closure**: The key point is that this is not a dead end — the isotopic mass balance in WP2 provides an independent check. Be ready to explain what "independent" means here: the isotopic approach does not use eddy covariance at all, so its estimate of forest floor evaporation is not contaminated by the same closure error.
- **Xylem water extraction**: Acknowledge that this is an active methodological debate in the isotope hydrology community. The triangulation approach (multiple methods on the same sample set) is the standard response to this uncertainty. Don't overstate confidence in any single extraction protocol.
- **Inter-site heterogeneity**: The hierarchical random-effects model is the right statistical framing. It allows process-level relationships (fixed effects) to be estimated separately from site-specific intercepts (random effects), so the three-site design becomes an asset rather than a source of uncontrolled noise.
- **Stand vs. tree scale**: The stratified sampling design is the structural solution. Be ready to sketch what "stratified by diameter class" means in practice: sap flow sensors and isotopic samples are collected from trees spanning three or four size classes, not only from the largest or most accessible individuals.

---

### 6. Expected Outputs
Three bullet points: papers, dataset, ForFuS contribution. Keep this brief in a presentation — one sentence per point. The journals listed (*HESS*, *Agricultural and Forest Meteorology*, *Ecohydrology*) are the standard outlets for this type of ecohydrology work and signal familiarity with the publishing landscape in this community.

---

### 7. Background and Added Value
Your personal fit argument. Three paragraphs:

1. **Thesis → methodological parallel**: FEST calibration over the Po basin involved the same problem of inferring poorly identifiable sub-processes from aggregate observations. The methodological link is real and precise, not a generic "relevant experience" claim — make that precision explicit when speaking.
2. **Progesi → operational data management**: Multi-source data integration, quality control, and real-time monitoring are directly transferable to the demands of a multi-site field campaign with heterogeneous instruments and sample types.
3. **Honest skills gap**: Isotope hydrology and ecophysiological instrumentation are competences to be acquired during the PhD. State this clearly and frame it as structured learning in an appropriate context, not as a deficit that disqualifies you.

**Presentation tip:** This section is where you make it personal. Do not read from the screen — speak it. Especially the third paragraph: if a committee asks about your lack of isotope experience before you get to it, you want to have your answer ready and comfortable, not defensive. The framing to use is in the FAQ below.

---

## How to Use This Page in an Interview

### Scenario 1: Video call with Prof. Keim or a ForFuS committee member (30–45 min)
1. Share your screen and open the page at the start of the call.
2. Start with the abstract box — read it aloud or invite them to read it.
3. Walk through RQ1–3 and explain the progressive logic and de-risking design (Year 1 is publishable regardless of later outcomes).
4. Go to WP1, WP2, and WP3 in some detail — these define what Years 1 and 2 look like concretely.
5. Use the Challenges section to demonstrate methodological awareness and a realistic view of the project's difficulty.
6. End with Section 7 (Background) — make it conversational, not scripted. Acknowledge the isotope hydrology gap directly and frame it as planned, structured learning.
7. Offer the PDF link from the meta bar before you close the call.

### Scenario 2: Formal selection panel interview
- Do not use the web page as a slide deck — it was not designed for that format.
- Use the PDF (`research-proposal.pdf`) as the formal document to hand or submit.
- The web page is your reference: keep it open on a second screen to stay oriented during the interview.
- Have the page ready in case a panel member asks to see a specific detail (e.g., the challenge mitigations or the timeline progression).

### Scenario 3: Informal first contact by email
- Include the page URL (`/phd-proposal/`) directly in the email body.
- Say: *"I have also put together a structured version of the proposal on my site at [URL] — the PDF link is at the top of the page."*
- Do not attach the PDF unsolicited in a first contact; let them choose their preferred format.

---

## Common Questions and How to Answer Them

**"What makes foliar water uptake scientifically interesting beyond its quantitative magnitude?"**  
The interest lies in what it implies about the directionality of water flux in the soil-plant-atmosphere system. Classical models treat the hydraulic gradient as unidirectional — from soil to leaf to atmosphere. Foliar uptake demonstrates that this gradient can reverse under drought, which challenges the parametric assumptions of transpiration models that represent leaves only as sources of water vapour flux. If foliar uptake is a quantitatively significant pathway during drought, then models calibrated without accounting for it will have systematically wrong representations of plant hydraulics under water stress, with downstream effects on predictions of carbon assimilation, stomatal conductance, and mortality risk.

**"How do you plan to distinguish foliar water uptake from condensation on leaf surfaces that simply re-evaporates?"**  
This is a genuine methodological challenge. The isotopic approach is the primary tool: foliar-absorbed water integrates into the leaf water pool and shifts the isotopic signature of xylem water in a way that condensate that re-evaporates from the leaf surface without being absorbed does not. The combination of xylem water sampling at multiple canopy heights and measurements of sub-canopy atmospheric water vapour isotopic composition allows partial separation of the two processes. This is exactly the kind of methodological nuance I expect to develop in WP1 and WP2 under Prof. Keim's guidance — I would not claim to have the protocol fully designed before starting.

**"Why three sites? Couldn't you characterise one site more thoroughly?"**  
A single-site study can quantify the fluxes under one climate-soil-species combination. The scientific question that has management implications — which factors control the relative importance of these minor pathways — requires variation across sites. Three sites spanning a gradient of climate, species composition, and soil type (Luxembourg lowland forest, Swiss montane conditions, Netherlands coastal-influenced forest) provide enough contrast to identify dominant controls, without becoming logistically unmanageable for a single PhD researcher. The inter-site design is also what connects the project to the ForFuS framework's comparative and interdisciplinary goals.

**"What is your timeline for a publishable result from Year 1?"**  
WP1 — a harmonised, quality-controlled multi-site dataset of isotopic ratios, micrometeorological fluxes, and sap flow records under drought and non-drought conditions — is a scientific contribution in its own right. Publishing the dataset alongside its collection protocols and the multi-method quality control approach is a realistic 12–15 month target, suitable for a data paper in *Earth System Science Data* or a methods-focused contribution to *Ecohydrology*.

**"You don't have experience with isotopic methods or ecophysiological instrumentation. How do you plan to close that gap?"**  
This is a fair and expected question, and I want to answer it directly. I do not have hands-on isotope hydrology experience — I have hydrological modelling, multi-source data integration, and operational risk assessment experience. The gap is real and I am not minimising it. What I bring instead is a methodological foundation — in uncertainty quantification, Bayesian parameter estimation, and process-based model calibration — that is directly applicable to the design and interpretation of isotopic mixing model studies. The technical field skills (xylem water extraction protocols, sub-canopy eddy covariance system setup, sap flow sensor installation and maintenance) are learned in a laboratory and field setting under expert supervision. Prof. Keim's group at LIST has that expertise; my role in Year 1 is to develop those skills systematically while contributing the modelling and data analysis competences I already have. A PhD is precisely the setting where this kind of structured competence development is designed to happen — and the fact that I can articulate clearly which skills I lack, and why they are acquirable in this specific context, reflects methodological self-awareness rather than unpreparedness.

**"How does the ForFuS training unit framework affect the project design?"**  
ForFuS is an interdisciplinary doctoral training unit, which means structured interactions with doctoral researchers from adjacent disciplines — ecology, climatology, environmental social science — are built into the programme. For this project, the most direct benefit is access to the multi-site experimental network and the supervisory expertise of LIST's Environmental Sensing and Modelling Unit. The interdisciplinary requirements will also shape how the resilience implications in WP5 are framed: connecting hydrological process findings to ecosystem management and policy questions requires working across disciplinary boundaries in a structured and documented way, which the ForFuS training framework explicitly supports.
