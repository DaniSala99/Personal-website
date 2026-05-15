---
title: "Multi-Objective Reservoir Operation: Trading Off Hydropower vs. Flood Risk on the Red River"
subtitle: "A neural-network inflow forecast and an evolutionary policy search for the Hoa Binh dam — protecting 16M people in Hanoi while keeping the lights on in Vietnam."
hero_image: "/portfolio/img/04-reservoir/01_red_river_system.png"
client: "Politecnico di Milano · Natural Resources Management"
year: "2023"
duration: "Team project"
tools: ["MATLAB", "ANN (feedforward)", "NSGA-II", "EMODPS", "Radial Basis Functions"]
---

# Multi-Objective Reservoir Operation: Trading Off Hydropower vs. Flood Risk on the Red River

*A neural-network inflow forecast and an evolutionary policy search for the Hoa Binh dam — protecting 16M people in Hanoi while keeping the lights on in Vietnam.*

![Red River basin and Hoa Binh reservoir system](/portfolio/img/04-reservoir/01_red_river_system.png)

## ▸ The Challenge

The Hoa Binh dam on the Red River is a textbook multi-objective management problem. It supplies a meaningful share of Vietnam's electricity (hydropower covers ~46% of national demand) while controlling monsoon-season flooding in Hanoi, a city of 16 million inhabitants. The two objectives **conflict directly**: holding water back for hydropower raises flood risk; releasing it preemptively burns potential energy. Worse, half of the basin sits in China, which doesn't share upstream flow data — so the dam operator is effectively blind to incoming inflow. **How do you find a release policy that's measurably better than the current one on both objectives, despite the data gap?**

## ▸ My Approach

Politecnico di Milano team project. Two-part workflow:

**Part 1 — 5-day inflow forecast model**

1. **Data integration** — combined 5 streamflow stations on the Da River (the only Vietnamese-side feeder) and 6 precipitation stations across the broader Red River basin, despite the missing Chinese data.
2. **Model comparison** — benchmarked linear models, feedforward Artificial Neural Networks (ANN), CART trees, and Random Forests on the same K-fold cross-validation scheme (5 years calibration / 2 years validation, sliding window).
3. **Best model selection** — final ANN architecture: 45 inputs, 3 hidden neurons, 142 parameters; achieved **R² = 0.67 in calibration, 0.63 in validation** — outperforming linear models and tree-based approaches, with no overfitting signature.
4. **Error diagnostics** — verified zero-mean prediction error (σ = 0.61 deseasonalized, slightly left-skewed), identified residual temporal autocorrelation, and proposed RNN architectures as the natural next step.

**Part 2 — Multi-objective policy optimization (EMODPS)**

5. **Baseline quantification** — simulated the current Standard Operating Policy (piecewise linear, 5 parameters) over 1995–2005, getting baseline metrics: 1.69 × 10⁷ kWh/day hydropower, 569.6 cm² mean squared water-level excess in Hanoi.
6. **Policy search** — ran **NSGA-II** (70 individuals, 50 generations) on both the SOP parametrization and a more flexible **Gaussian Radial Basis Function** policy (4 RBFs, 13 parameters).
7. **Pareto analysis** — extracted three operationally relevant solutions: Best Hydropower, Best Floods, Best Compromise (closest to utopia point).

## ▸ The Solution

A complete decision-support pipeline: forecast → simulation → multi-objective optimization. The framework outputs a **Pareto front** — not a single answer — letting decision-makers explicitly choose where to sit on the hydropower-vs-flood trade-off, with quantified consequences at every point.

![Pareto front before and after optimization](/portfolio/img/04-reservoir/02_pareto_front.png)

## ▸ Key Results

- **Forecast accuracy**: ANN model with R² = 0.67 (cal) / 0.63 (val), outperforming linear models and Random Forests despite missing upstream Chinese data.
- **RBF policy outperforms the piecewise SOP** across the entire Pareto front: smoother level-release relationship adapts better to inflow variability.
- **Three operational policies delivered** (Best Hydropower, Best Floods, Best Compromise) — a decision-ready menu for the regulator, not a black-box recommendation.
- **End-to-end reproducibility**: 11 input variables, 142 ANN parameters, 13 RBF parameters, K-fold cross-validation, full MATLAB pipeline.

![ANN forecast — observed vs predicted Hoa Binh inflow](/portfolio/img/04-reservoir/03_ann_forecast.png)

## ▸ Business Impact

The framework generalizes beyond Hoa Binh to any reservoir system facing competing objectives:

- **Hydropower operators** in Italy and Europe (Alpine reservoirs, Po basin) — climate-change-driven inflow shifts are forcing operational policy reviews.
- **Multi-purpose dam authorities** — irrigation vs. hydropower vs. flood control trade-offs (e.g. Po River reservoirs, Iberian peninsula, Greek/Turkish basins).
- **CSRD/ESRS E1 physical-risk reporting** for energy companies with hydropower exposure: quantified climate-vs-operations sensitivity replaces qualitative narrative.
- **Climate adaptation planning** — same EMODPS + NSGA-II machinery applies to coastal flood defense, urban drainage capacity, water supply optimization under drought.

## ▸ Tech Stack

`MATLAB` (full pipeline) · `Artificial Neural Networks` (Levenberg-Marquardt training) · `NSGA-II` (multi-objective evolutionary algorithm) · `EMODPS` (Evolutionary Multi-Objective Direct Policy Search) · `Radial Basis Functions` (parametric policy class) · `K-fold cross-validation`

---

*Looking at a reservoir or water-system trade-off problem? [Get in touch →](/contact)*
