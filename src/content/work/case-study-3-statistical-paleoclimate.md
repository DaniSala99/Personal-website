---
title: "Validating 11 Paleoclimate Reconstruction Methods Across 1,000 Years of European Temperatures"
subtitle: "How do you trust temperature data that nobody measured? Statistical validation of proxy-based reconstructions from 500 BC to 2018."
hero_image: "/portfolio/img/03-statistical/01_timeseries_overview.png"
client: "Politecnico di Milano · Statistical Models and Stochastic Processes"
year: "2023"
duration: "Team project"
tools: ["R", "Bland-Altman analysis", "Shapiro-Wilk test", "Paired t-test", "Linear regression with breakpoints"]
---

![Time series of 11 paleoclimate reconstruction methods](/portfolio/img/03-statistical/01_timeseries_overview.png)

## ▸ The Challenge

Climate risk modeling, CSRD physical-risk disclosures, and reinsurance pricing all depend on long-term temperature baselines that pre-date instrumental records. These baselines come from **proxy reconstructions**: tree rings, grape harvest dates, lake sediments, ice cores, built by different research groups using different methods over different time windows. A practical question follows: **are these reconstructions actually consistent with each other, or do they tell different stories?** If two methods disagree on the Little Ice Age temperature, downstream climate baselines inherit that disagreement.

## ▸ My Approach

Politecnico di Milano team project for the *Statistical Models and Stochastic Processes* course. End-to-end validation pipeline in R:

1. **Dataset assembly**: consolidated 11 published paleoclimate reconstructions covering the European Alps and Central Europe, spanning from 500 BC to 2018 AD across 4 proxy families: tree-ring dendrochronology, Grape Harvest Dates (GHD), lake sediment chironomids, and historical/documentary indices.
2. **Pre-processing**: standardized anomalies to a common reference period, applied outlier removal to isolate climate signal from local noise, addressed non-uniform temporal coverage and missing-data patterns.
3. **Pairwise method comparison**: applied **Bland-Altman analysis** to quantify systematic bias and limits of agreement between every pair of methods; ran **paired t-tests** with normality verified via **Shapiro-Wilk** (p > 0.5 confirmed).
4. **Regime change detection**: fit segmented linear regression with breakpoint detection on each series to test whether all methods captured the same well-known climate events (Little Ice Age 1645–1715 and 1816–1850, Medieval Warm Period).
5. **Cross-proxy reconciliation**: assessed which proxy families agreed and which diverged, and explained the divergence mechanistically (e.g. dendrochronology underestimating cold extremes vs. hemispheric reconstructions like Mann's Hockey Stick).

## ▸ The Solution

A reproducible R workflow that takes any set of paleoclimate (or modern climate) time series and outputs: pairwise bias matrices, agreement intervals, regime-change diagnostics, and a synthesis on which methods can (and cannot) be combined for downstream use.

![Bland-Altman analysis of dendrochronology methods](/portfolio/img/03-statistical/02_bland_altman.jpg)

## ▸ Key Results

- **Validated 11 reconstruction methods** across 4 proxy families on a dataset spanning 2,500 years (500 BC – 2018 AD).
- **Identified systematic bias between proxy families**: dendrochronology methods systematically underestimate cold extremes compared to hemispheric reconstructions (Mann et al. 1999), a non-trivial finding for any user mixing the two.
- **Quantified regime-change detection capability**: only 1 method out of 4 tested captured both Little Ice Age sub-periods (1645–1715 and 1816–1850); chironomid-based methods detect the broad regime but miss the sharper 1816–1850 sub-event.
- **Statistical assumptions verified**: Shapiro-Wilk p-values consistently > 0.5 confirmed normality of differences, validating the use of parametric tests.

![Regime change detection via segmented regression on 4 representative methods](/portfolio/img/03-statistical/03_regime_change.png)

## ▸ Applied Context

Directly applicable for:
- **Climate risk analytics**: defensible long-term baselines for ESRS E1 / TCFD physical-risk disclosures, where regulators ask "how do you justify your historical reference period?"
- **Reinsurance & catastrophe modeling**: quantified uncertainty bands on pre-instrumental climate, feeding into return-period estimates for extreme events.
- **Climate model validation**: same statistical toolkit (Bland-Altman, paired tests, segmented regression) applies to comparing GCM outputs against reanalyses (ERA5, MERIDA, MERRA-2), a recurring need in CSRD climate scenario work.
- **Any decision-making with multi-source environmental data**: the methodology generalizes to remote sensing product comparison, multi-station hydrological data, multi-model ensembles.

## ▸ Tech Stack

`R` (statistical pipeline) · `Bland-Altman analysis` · `Shapiro-Wilk normality test` · `Paired t-test` · `Segmented linear regression` (breakpoint detection) · `ggplot2`

---

*Need defensible climate baselines for your CSRD or risk model? [Get in touch →](/contact)*
