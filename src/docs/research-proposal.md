# PhD Project Plan

**Project:** Monitoring and Predicting Droughts on National Scale: A Satellite-Integrated, Groundwater-Coupled Hybrid Modelling Framework for Denmark  
**Author:** Daniele Sala  
**Date:** May 2026  
**Programme:** DREAM PhD, Aalborg University

---

## Abstract

The PhD will deliver a satellite-fed VIC Denmark system producing a probabilistic four-pillar combined drought index and short- to seasonal-scale predictions of water dynamics. It closes a structural gap in Denmark's drought early warning landscape by coupling groundwater state to a national-scale land surface model and integrating multi-source satellite observations via data assimilation.

---

## 1. Problem Statement and Motivation

The 2018 Danish drought caused agricultural losses exceeding DKK 6 billion and exposed a structural gap in the national early warning landscape. Operational systems such as **HIP** (Hydrologisk Informations- og Prognosesystem) and the **DK model** deliver high resolution diagnostics but lack probabilistic, satellite-integrated outlooks at sub-seasonal to seasonal lead times.

Meanwhile, macro-scale land surface models such as **Variable Infiltration Capacity (VIC)** — the model targeted by the DREAM call — lack a prognostic groundwater state. In a country where:
- >99% of drinking water originates from aquifers
- Water tables typically lie 1–5 metres below surface
- >50% of agricultural area is sub-surface drained

…this gap is not a detail but a first-order limitation.

The recent finding by Forootan et al. (2024) that the severity of the 2017–2021 European drought is systematically underestimated in non-assimilated W3RA confirms that closing this loop — through groundwater coupling, multi-source data assimilation, and hybrid physics/ML integration — is both timely and necessary.

---

## 2. Research Questions

**RQ1.** Can a groundwater-coupled VIC Denmark, calibrated and constrained by joint assimilation of **GRACE FO** terrestrial water storage, **SMAP** and **ESA CCI** soil moisture, streamflow, and Jupiter piezometric heads, reproduce the propagation of meteorological, agricultural, hydrological, and groundwater drought signals at national scale better than uncoupled or non-assimilated baselines?

**RQ2.** Does a hybrid framework — combining differentiable parameter learning for VIC parameters with LSTM or Transformer post-processing trained on **CAMELS DK** — recover predictive skill in groundwater-dominated Danish catchments, where pure LSTMs underperform (Liu et al. 2024)?

**RQ3.** Can a probabilistic four-pillar combined index (SPI/SPEI + SSMI + SSI + SGI), aggregated via copulas with full ensemble and posterior uncertainty propagation, classify drought severity more skilfully than **EDO CDI v4**, and improve seasonal predictability when forced with bias-corrected **SEAS5** and **AIFS ENS** or GenCast?

---

## 3. Approach and Work Packages

### WP1 — VIC Denmark with Groundwater Coupling
National VIC 5 at 1–10 km, parameterised from VICGlobal and refined with Danish hydrostratigraphy from GEUS and Jupiter wells. The groundwater module follows **SIMGM** (Niu et al. 2007), with a staged escalation path to 2D lateral coupling (Zhang and Liang 2021) if validation justifies it.

### WP2 — Joint Calibration and Multi-Source Data Assimilation
**LETKF** and **ConBay** MCMC assimilating GRACE FO terrestrial water storage (sub-monthly L1B), SMAP and ESA CCI soil moisture, streamflow, and Jupiter piezometric heads. Built on **PyGLDA** (Yang et al. 2025) with Fennoscandian GIA correction via ICE-6G_D.

### WP3 — Hybrid Extension via Differentiable Hydrology
Differentiable VIC trained via **dPL** (Tsai et al. 2021; Feng et al. 2022) on CAMELS DK (Liu et al. 2025), replacing per-basin calibration with gradient-based learning across 3,330 basins. An LSTM residual post-processor corrects biases in groundwater-dominated catchments.

### WP4 — Probabilistic Four-Pillar Drought Index
Standardised sub-indices spanning the full propagation chain — SPI/SPEI, SSMI, SSI, SGI — aggregated via copulas into a probabilistic **Multi-pillar Combined Drought Index (MCDI)** with full posterior probabilities of drought severity categories.

### WP5 — Short- to Seasonal-Scale Forecasting
VIC DK forced with SEAS5 and AIFS ENS or GenCast for 1–6 month outlooks, evaluated via **CRPS**, Brier score, and ROC, with reverse ESP diagnostics. Benchmarks: EFAS Seasonal and EDgE.

---

## 4. Expected Challenges and Mitigations

| Challenge | Mitigation |
|---|---|
| **Scale mismatch** — GRACE FO ~300 km vs Denmark 43,000 km² | Sub-monthly L1B assimilation; ConBay merging with SMAP; ML-based downscaling against Jupiter wells; GIA correction via ICE-6G_D |
| **Equifinality** — multiple parameter sets reproduce equivalent streamflow | GEUS-derived priors on aquifer parameters; LETKF localisation and inflation; dPL as deterministic precursor |
| **ML physical consistency** — LSTMs may extrapolate poorly, no mass conservation | VIC as physical backbone; LSTM restricted to residual post-processor; conformal prediction for uncertainty intervals |
| **Index collapse** — naive averaging loses causal propagation and tail dependence | Pillar-appropriate scales (SPI 1–3 months, SGI 6–12 months); copula aggregation; validation against Naturskaderådet claims and crop yield anomalies |

---

## 5. Feasibility, Fit and Expected Outputs

The plan is feasible within three years because Year 1 already delivers a publishable physics-based baseline, even if hybrid extensions slip. AAU PyGLDA, ConBay, and HPC Claaudia infrastructure provide a strong starting point, while CAMELS DK, Jupiter, DMI Klimagrid, and HIPRAD supply the data backbone.

The project aligns with the **Villum Young Investigator Programme** on "Synergy of Physics-based and Data-driven Methods" and complements GEUS DK model expertise, opening natural collaboration with Henriksen, Stisen, and Schneider.

**Expected outputs:**
- Three first-author papers: *Water Resources Research*, *Hydrology and Earth System Sciences*, and *Remote Sensing of Environment* or *Science of The Total Environment*
- An open-source VIC DK + ConBay data assimilation codebase released through PyGLDA
- An operational MCDI prototype co-designed with DMI, GEUS, and Naturskaderådet end-users

---

## 6. Background and Added Value

My M.Sc. thesis at Politecnico di Milano — building, calibrating, and running sensitivity and uncertainty analysis on the FEST process-based hydrological model over the Po basin — gave me direct experience of the central methodological tension this project addresses: constraining subsurface parameters (hydraulic conductivity, deep percolation factors, SCS curve number) from surface observations alone.

My current operational role at Progesi S.p.A., running multi-hazard monitoring with ICON and ECMWF IFS forcing, satellite-derived diagnostics, and Python/R/MATLAB workflows for Regione Lombardia, translates directly to the operational demands of a national-scale drought early warning system.

The combination of process-based modelling, applied data science, and recent exposure to operational hydrometeorology positions me to start contributing to WP1 and WP2 immediately, while developing the hybrid machine learning competence required for WP3 through structured upskilling in NeuralHydrology, PyTorch, and differentiable hydrology.
