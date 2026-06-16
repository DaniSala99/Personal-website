# Guide to Presenting the PhD Research Proposal Page

This document is a practical reading and presentation guide for the `/phd-proposal/` page on the site. It explains what each section contains, why it is structured that way, and how to walk a supervisor or committee through it during a PhD interview or informal meeting.

---

## Overview: What the Page Is

The page is a structured, web-native version of the two-page written proposal (`research-proposal.pdf`). It covers the same content but breaks it into clearly labelled sections that are easy to navigate in a browser. It is designed to be used in two ways:

1. **As a self-standing document** — a supervisor or committee member can read it independently before or after a meeting.
2. **As a live presentation aid** — you can scroll through it during a video call or in-person meeting, using each section as a talking prompt.

A link to download the original PDF is provided at the top (in the meta bar) and at the bottom of the page.

---

## Section-by-Section Reading Guide

### Meta bar (top strip)
Shows programme, duration, and date at a glance. The **Download PDF** link is here — offer it early in a conversation so the other person can follow along on paper if they prefer.

---

### Abstract box (blue-bordered block)
This is the single most important paragraph on the page. It states in three sentences what the PhD will *deliver*, why it matters, and how it works. **Always start here when presenting.** If you only have 30 seconds, read this aloud and stop. It frames everything that follows.

Key message: *"The PhD delivers a satellite-fed VIC Denmark system with a probabilistic four-pillar drought index. It closes a groundwater gap in existing operational systems using data assimilation and hybrid ML."*

---

### 1. Problem Statement and Motivation
This section answers *"why does this PhD need to exist?"* There are three building blocks:

- **The 2018 drought** — a concrete, quantified event (DKK 6 billion in losses) that gives the problem an operational face. Use it as an opening anchor.
- **The structural gap** — HIP and the DK model deliver diagnostics but not probabilistic seasonal outlooks. This is the gap the DREAM call is specifically targeting.
- **The groundwater argument** — Denmark's 99% groundwater dependency for drinking water + sub-surface drainage over half of agricultural land. This is the strongest argument for why VIC without a groundwater module is insufficient. Emphasise this if the supervisor works on the DK model side.

**Presentation tip:** Pause after the three bullet points about Denmark's groundwater context. Let the numbers land. Then introduce Forootan et al. (2024) as external validation that the gap is real and recently confirmed.

---

### 2. Research Questions
Three research questions, each testing one core component of the system:

| RQ | Tests | What a "yes" answer proves |
|---|---|---|
| RQ1 | Groundwater-coupled VIC + data assimilation | The physics-based backbone works and adds skill over uncoupled baselines |
| RQ2 | Hybrid differentiable hydrology + LSTM | The ML layer recovers skill specifically in groundwater-dominated catchments |
| RQ3 | Four-pillar copula-aggregated drought index | The combined index outperforms the existing benchmark (EDO CDI v4) |

**Presentation tip:** Present RQ1 as the necessary precondition — if VIC+GW+DA doesn't outperform the baseline, the rest of the project needs to be redesigned. Describe this as intentional de-risking: Year 1 produces a publishable result regardless of whether RQ2 and RQ3 succeed.

---

### 3. Work Packages
Five WPs, each shown as a colour-coded card with a badge. The left border accent colour is intentional — it visually groups them as a pipeline, not a list of independent tasks.

**How to walk through them:**

- **WP1** is the foundation. Stress the *staged escalation* approach: start with SIMGM (proven, simple), collect evidence, then decide at month 12 whether 2D lateral coupling is justified. This avoids over-engineering Year 1.
- **WP2** runs throughout all years. Explain that this is not a sequential step — LETKF and ConBay assimilation constrain WP1 parameters continuously. Mention PyGLDA as the existing AAU infrastructure you will build on.
- **WP3** begins in Year 2. The key word is *residual* post-processor: the LSTM does not replace VIC, it corrects the biases VIC cannot explain in groundwater-dominated catchments. This addresses the common supervisor concern about physical consistency.
- **WP4** is the science deliverable with the most direct policy impact: the Multi-pillar Combined Drought Index (MCDI). Copula aggregation is the technical choice that preserves tail dependence between drought categories — explain this if the supervisor has a statistics background.
- **WP5** is the operational output in Year 3. SEAS5 and AIFS/GenCast are the forcing datasets; CRPS and Brier score are the verification metrics. Mention EFAS Seasonal as the benchmark — it's what Danish civil protection currently uses.

---

### 4. Project Timeline
A visual Gantt-style bar chart showing which WPs are active in each year. Three things to point out:

1. **Year 1 is publishable on its own** — WP1 alone (physics-based VIC-Denmark baseline) is a contribution, even if WP2–5 slip. This is the de-risking argument.
2. **WP2 overlaps all years** — data assimilation is not a phase; it is the continuous constraint on the whole system.
3. **WP3 and WP4 are parallel in Years 2–3** — the hybrid ML and the drought index development can proceed simultaneously once the VIC+DA backbone is stable.

**Presentation tip:** Use the timeline to show you have thought about sequencing and risk. Supervisors want to see that Year 1 has a clear, achievable deliverable.

---

### 5. Expected Challenges and Mitigations
Four cards, one per challenge. Each card has the challenge name, a one-line description of why it is a problem, and the specific technical mitigation.

This section shows methodological maturity. **For each challenge, the mitigation is already part of the project design** — it is not an afterthought. Key points to stress:

- **Scale mismatch** (GRACE FO ~300 km vs Denmark 43,000 km²): the sub-monthly L1B assimilation from Retegui-Schiettekatte et al. (2025) is a very recent result — citing it shows you are tracking the literature actively.
- **Equifinality**: GEUS-derived priors on aquifer parameters are the structural solution — you are not calibrating blind, you are using stratigraphic data from Jupiter wells. This is the key differentiator from a pure remote-sensing approach.
- **ML physical consistency**: keeping VIC as the backbone and restricting LSTM to a residual role is a deliberate choice. Be ready to explain why conformal prediction is preferred over Bayesian credible intervals here (computational tractability at 3,330 basins).
- **Index collapse**: the choice of pillar-appropriate scales (SPI 1–3 months, SGI 6–12 months) is based on known propagation timescales in the drought literature. Validation against Naturskaderådet insurance claims is the operational ground truth.

---

### 6. Expected Outputs
Three bullet points: papers, open-source code, operational prototype. Keep this brief in a presentation — one sentence per point. The journals listed (WRR, HESS, RSE/STOTEN) are the standard outlets for this type of work and signal familiarity with the field.

---

### 7. Background and Added Value
This is your personal fit argument. Two paragraphs:

1. **Thesis → RQ1 link**: FEST calibration over the Po basin is directly analogous to VIC calibration over Denmark — same challenge of constraining subsurface parameters from surface observations. This is not a generic "relevant experience" claim; it is a methodological parallel.
2. **Progesi → operational relevance**: running ICON and ECMWF-IFS forcing for Regione Lombardia is operational practice for exactly the kind of NWP-driven hydrological forecasting system the PhD will build for Denmark.

**Presentation tip:** This section is where you make it personal. Do not read from the screen — speak it. The numbers (106/110, 3,330 basins, DKK 6 billion) are on the page if the supervisor needs them; your job is to explain *why your specific path leads naturally here*.

---

## How to Use This Page in an Interview

### Scenario 1: Video call with a potential supervisor (30–45 min)
1. Share your screen and open the page at the start of the call.
2. Start with the abstract box — read it aloud or ask them to read it.
3. Walk through RQ1–3 and explain the de-risking logic.
4. Go to WP1 and WP2 in detail (these are most relevant to what Year 1 looks like).
5. Use the Challenges section to show methodological awareness.
6. End with Section 7 (Background) — make it conversational, not scripted.
7. Offer the PDF link from the meta bar before you close.

### Scenario 2: Formal committee or panel interview
- Do not use the web page as a slide deck — it was not designed for that.
- Use the PDF (`research-proposal.pdf`) as the formal document.
- The web page is your reference: you can glance at it on a second screen to keep your place.
- Have the page open in the background in case a committee member asks to see a detail (e.g., the challenge mitigations or the timeline).

### Scenario 3: Informal first contact by email
- Include the page URL (`/phd-proposal/`) directly in the email body.
- Say: *"I have also put together a structured version of the proposal on my site at [URL] — the PDF link is at the top of the page."*
- Do not send the PDF unsolicited in a first email; let them choose their format.

---

## Common Questions and How to Answer Them

**"Why VIC and not the DK model directly?"**
VIC is the model specified in the DREAM call. The DK model is a MIKE-based fully distributed model with excellent calibration for Denmark but no satellite-assimilation pathway. VIC has an active data assimilation community (PyGLDA, LETKF) and a growing differentiable hydrology ecosystem (dPL, NeuralHydrology) that would be much harder to build on the DK model.

**"You mentioned LSTM underperformance in groundwater-dominated catchments — how severe is it?"**
Liu et al. (2024) is the reference: they show that in catchments where more than ~40% of baseflow comes from groundwater, pure LSTM Nash-Sutcliffe efficiencies are meaningfully lower than in surface-runoff-dominated systems. The residual post-processor architecture (WP3) is designed specifically for this failure mode.

**"What is your timeline for a publishable result from Year 1?"**
WP1 alone — a calibrated groundwater-coupled VIC Denmark at 5 km resolution, validated against Jupiter wells and USGS-style streamflow metrics — is a methodological contribution to the HESS or WRR community. A 12-month timeline to a first submission is realistic given the existing VICGlobal parameterisation and the AAU infrastructure.

**"How do you handle the GIA correction for GRACE FO?"**
ICE-6G_D is the standard correction for Fennoscandian GIA, applied as a forward model subtraction before GRACE FO L1B assimilation. The Retegui-Schiettekatte et al. (2025) sub-monthly L1B approach reduces the effective footprint relative to the standard monthly mascon products, which is important at Denmark's scale.

**"Why copulas for index aggregation and not a simple weighted average?"**
Copulas preserve tail dependence between drought categories. A drought event that is simultaneously in the 90th percentile for soil moisture deficit (SSMI) and the 90th percentile for groundwater depletion (SGI) is not captured by a linear average, which would return a moderate composite value. The Hao & AghaKouchak (2013) framework is the standard reference for this choice.
