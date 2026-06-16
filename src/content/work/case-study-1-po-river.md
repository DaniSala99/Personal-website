---
title: "Quantifying the Hydrologic Impact of Agricultural Irrigation in the Po River Basin"
subtitle: "10 years of data, a process-based hydrological model, and clear answers on irrigation's footprint on Italy's largest river basin."
hero_image: "/portfolio/img/01-po/01_po_basin_map.png"
client: "Politecnico di Milano · M.Sc. Thesis"
year: "2024"
duration: "12 months"
tools: ["FEST (Fortran)", "Python", "R", "QGIS", "MERIDA dataset"]
---

![Po River Basin: sub-catchments and measurement stations](/portfolio/img/01-po/01_po_basin_map.png)

## ▸ The Challenge

The Po River basin is Italy's agricultural heartland and one of Europe's most water-stressed catchments under climate change. Stakeholders (irrigation consortia, regional water authorities, agribusinesses, hydropower operators) need a quantitative, defensible answer to a critical question: **how much does agricultural irrigation actually alter the natural hydrologic regime, and when does it bite hardest?** Without numbers, water concession reviews, drought management plans, and CSRD physical-risk disclosures are guesswork.

## ▸ My Approach

Master Thesis at Politecnico di Milano (DICA, supervisor Prof. Giovanni Ravazzani). Built and validated a process-based water-balance model on a 10-year dataset (2011–2020):

1. **Data engineering**: assembled and quality-checked 10 years of MERIDA reanalysis meteo data, hydrometric records from 6 measurement stations along the Po (Spessa Po, Piacenza, Cremona, Boretto, Borgoforte, Pontelagoscuro), and irrigation records sourced directly from the regional reclamation and irrigation consortia.
2. **Model implementation**: customized the **FEST** (Flash Flood Event-based Simulation Technique) hydrological model in Fortran, including a new module for stream–groundwater interaction.
3. **Sensitivity analysis**: ran a structured sensitivity assessment on 5 parameter families: deep percolation factor, SCS Curve Number, hydraulic conductivity, river–aquifer interaction coefficients, and channel routing.
4. **Calibration & validation**: calibrated the model on observed discharges, validated on the 2011–2020 period across all 6 stations using ∆% on cumulative volumes, NRMSE, and Nash-Sutcliffe Efficiency (NSE).
5. **Scenario analysis**: designed a counterfactual "no-irrigation" simulation to isolate the irrigation signal from natural hydrologic variability.

## ▸ The Solution

A calibrated, validated water-balance model that disentangles natural hydrologic variability from the irrigation signal, with quantified uncertainty bands at every step. The framework is reproducible: same FEST + sensitivity stack applies to any data-scarce or regulation-driven river basin in Europe.

![Simulated vs observed discharge at Pontelagoscuro, 2017](/portfolio/img/01-po/02_po_discharge_timeseries.png)

## ▸ Key Results

- **Irrigation reduces annual cumulative river volumes by 5.7% on average** across the basin, jumping to **15.0% during the irrigation window (15 April – 15 September)** when farms compete with the river for water.
- **Validation across 6 stations**: mean NSE = 0.58, mean NRMSE = 0.50, ∆% on cumulative volume between 1% and 11%, performance stable between calibration and validation periods.
- **Sensitivity analysis identified deep percolation factor and SCS Curve Number as the dominant controls** on simulated discharge, while hydraulic conductivity matters most for aquifer-level dynamics, a non-obvious result for parameter prioritization in future calibration work.
- **No-irrigation scenario** showed measurably higher river flows and aquifer levels during dry months, confirming that irrigation amplifies summer low-flow stress.

![Sensitivity analysis: relative impact of FEST model parameters](/portfolio/img/01-po/03_sensitivity_tornado.png)

## ▸ Applied Context

Directly relevant for:
- **Irrigation consortia**: resource allocation and drought planning under water concession reviews.
- **Regional water authorities**: quantitative basis for regulatory decisions and Po River Basin Authority planning.
- **Agritech & precision farming**: ROI on water-efficient irrigation under realistic water-availability scenarios.
- **Energy companies** with hydropower exposure on the Po, for long-term flow projections under combined climate and management stress.
- **CSRD/ESRS E1 physical-risk disclosures** for any company with operational exposure to the basin.

The same FEST + sensitivity workflow applies to any data-scarce or regulation-driven river basin in Europe where stakeholders need a defensible, uncertainty-aware answer rather than a black-box estimate.

## ▸ Tech Stack

`Fortran` (FEST customization) · `Python` (pre/post-processing, sensitivity analysis) · `R` (statistical validation) · `QGIS` (spatial analysis & mapping) · `MERIDA` reanalysis dataset · `ERA5` cross-validation

---

*Want a similar analysis for your basin? [Get in touch →](/contact)*
