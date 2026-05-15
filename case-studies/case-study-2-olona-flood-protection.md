---
title: "End-to-End Flood Protection Workflow on the Olona River — From DEM to Pluviometric Alert Thresholds"
subtitle: "GIS basin delineation, flood frequency analysis, HEC-RAS hydraulic modeling, levee design, and bivariate copula-based dam safety verification — all on one Alpine catchment."
hero_image: "/portfolio/img/02-olona/01_olona_basin_dem.png"
client: "Politecnico di Milano · Hydraulic Protection of Territory"
year: "2023"
duration: "Course-integrated project"
tools: ["QGIS", "HEC-RAS (1D steady)", "R (copula, fExtremes)", "FEST", "Python"]
---

# End-to-End Flood Protection Workflow on the Olona River — From DEM to Pluviometric Alert Thresholds

*GIS basin delineation, flood frequency analysis, HEC-RAS hydraulic modeling, levee design, and bivariate copula-based dam safety verification — all on one Alpine catchment.*

![Olona basin DEM and slope analysis (Ponte Gurone, ~80 km²)](/portfolio/img/02-olona/01_olona_basin_dem.png)

## ▸ The Challenge

Flood risk management isn't one model — it's a chain. A municipality, river basin authority or insurer asking *"is this section of river safe for a 200-year return period?"* needs the full pipeline answered: catchment hydrology, statistical flood frequency, hydraulic capacity of the channel, design of mitigation works, dam safety, and operational early-warning thresholds. **A single weak link in the chain — and the answer breaks.** Most consultancies stitch these analyses together from different tools and people, losing internal consistency along the way.

## ▸ My Approach

Hydraulic Protection of Territory project at Politecnico di Milano (Prof. Giovanni Ravazzani). Built one integrated workflow on the **Olona River basin**, closed at Ponte Gurone (Varese, ~80 km², mean elevation 147 m a.s.l., mean slope 0.146 rad). Ten linked analyses:

1. **GIS pre-processing** — DEM depitting, basin masking, flow-direction reconstruction, drainage network extraction (1 km² threshold), catchment area / height / slope mapping.
2. **Soil hydrology characterization** — basin-average SCS Curve Number = 73.4 (low permeability), spatial CN map for runoff modeling.
3. **Flood frequency analysis** — direct methods (AFS, PDS) on discharge records and indirect methods (Rational Formula, geomorphoclimatic) with depth-duration-frequency (LSPP) curves rescaled from Varese reference station, including areal reduction factor (ARF).
4. **Critical event identification** — iterative search for critical duration (ponding + concentration time) yielding the maximum peak discharge for return periods T = 50, 100, 200, 500 years at two sections (Lozza and Ol7a).
5. **1D hydraulic modeling in HEC-RAS** — channel geometry, bridges, roughness, expansion/compression coefficients; steady-flow profiles for the four return periods on section Ol7a (Q = 86, 106, 129, 166 m³/s).
6. **Levee design** — sized embankments for the 200-year event (legal standard) with 1 m safety freeboard, then re-simulated to verify that upstream protection doesn't push flooding downstream.
7. **Pluviometric alert thresholds** — back-calculated the rainfall conditions that produce the channel-capacity discharge (80 m³/s, slightly below the 86 m³/s 50-year peak), tested against three hyetograph types (front-loaded, uniform, end-loaded) and three antecedent moisture classes (AMC1/2/3).
8. **Bivariate dam safety verification** — modeled the joint Q-V (peak-volume) distribution using a **Gumbel copula** fitted via maximum pseudo-likelihood, with GEV marginals; selected the Most Likely Realization quantile for a 200-year design hydrograph.
9. **Reservoir routing** — solved the continuity equation at the dam via Runge-Kutta integration to verify that water level stays below the spillway crest under the 200-year inflow.
10. **Documentation & reproducibility** — full R code for steps 8-9, full HEC-RAS project for steps 5-7, all GIS layers exportable.

## ▸ The Solution

A single, internally consistent flood-protection assessment for a real Italian catchment — covering everything a municipality, civil protection agency, or insurer would need: hydrology, hydraulics, mitigation design, dam safety, and early-warning thresholds. Each step's output is the next step's input, so assumptions and uncertainties propagate transparently.

![Critical-event hydrographs at sections Lozza and Ol7a, T = 50/100/200/500](/portfolio/img/02-olona/02_critical_hydrographs.png)

## ▸ Key Results

- **Basin geomorphology characterized**: ~80 km² catchment, mean elevation 147 m, mean slope 0.146 rad, mean CN = 73.4, drainage network extracted at 1 km² threshold.
- **Design discharges quantified** at section Ol7a: **Q₅₀ = 86 m³/s · Q₁₀₀ = 106 m³/s · Q₂₀₀ = 129 m³/s · Q₅₀₀ = 166 m³/s**, with critical durations between 25 and 35 minutes (fast-responding catchment).
- **Hydraulic deficits localized in HEC-RAS** for the 200-year event, with levee design (1 m freeboard) restoring containment without inducing downstream flooding.
- **Pluviometric alert threshold = 80 m³/s**, with corresponding rainfall envelopes derived for three hyetograph shapes and three AMC classes — operationally usable by a civil protection agency.
- **Dam safety verified for T = 200 years** via Gumbel-copula bivariate analysis (Q-V joint distribution), with reservoir routing showing peak water level below the maximum allowed spillway elevation.

![HEC-RAS 1D profile — Olona section under T = 200 years, with levee design](/portfolio/img/02-olona/03_hecras_profile.png)

## ▸ Business Impact

This is the deliverable a real client buys when they need flood protection done end-to-end:

- **Municipalities & river basin authorities** — *EU Floods Directive 2007/60/EC* compliance: hazard maps, mitigation design, alert thresholds in one package.
- **Civil protection agencies** — operational pluviometric thresholds tied directly to channel capacity, not generic rainfall warnings.
- **Insurers & reinsurers** — return-period-specific hazard layers feeding into property exposure pricing and accumulation modeling.
- **Engineering consultancies** — a reproducible reference workflow for any small-to-medium Alpine or Apennine catchment in Italy.
- **Dam owners (utilities, A2A, ENEL Green Power)** — bivariate Q-V dam safety verification, going beyond univariate return periods which systematically underestimate risk.

The same chain (GIS → frequency analysis → HEC-RAS → levee design → copula dam check) applies to any catchment under 1,000 km² — the typical scale for Italian and Alpine flood-management studies.

## ▸ Tech Stack

`QGIS` (GIS pre-processing, basin delineation) · `HEC-RAS` (1D steady-flow hydraulic modeling) · `R` (copula, fExtremes, plot3D — bivariate frequency analysis & Runge-Kutta routing) · `FEST` (`festCmax` executable for critical-event search) · `Python` (post-processing) · LSPP / IDF curves · SCS Curve Number method

---

*Need an end-to-end flood protection study on your catchment? [Get in touch →](/contact)*
