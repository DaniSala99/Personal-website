# danielesala-portfolio

Content source-of-truth for [danielesala.com](https://danielesala.com) — the freelance portfolio site of Daniele Sala, environmental engineer (Politecnico di Milano M.Sc., 106/110), specialised in hydrology, flood risk modeling and climate risk analytics.

The actual website is built on Framer. This repository is the **canonical text source**: case studies, about, experience and taglines live here as version-controlled Markdown.

## Structure

```
case-studies/                    Four PASRI-format case studies (~500–700 words each)
├── case-study-1-po-river.md     Flagship: Po River basin irrigation impact (M.Sc. Thesis)
├── case-study-2-olona-flood-protection.md   End-to-end flood protection workflow on the Olona River (HEC-RAS + copula)
├── case-study-3-statistical-paleoclimate.md Validation of 11 paleoclimate reconstruction methods
└── case-study-4-reservoir-optimization.md   Multi-objective reservoir operation on the Red River (Hoa Binh dam)

about-me.md                      Two versions: A (story-driven, for Framer + LinkedIn), B (B2B, for Upwork / Malt / Toptal)
experience.md                    Progesi + Enel NDA-safe summaries, Education, Certifications & Languages
taglines.md                      Channel-mapped taglines (LinkedIn / Framer homepage / Upwork / email signature)

img/                             Image assets per case study (PNG @300dpi, populated manually)
├── 01-po/                       3 visuals — Po basin map, discharge timeseries, sensitivity tornado
├── 02-olona/                    3 visuals — Olona DEM, critical hydrographs, HEC-RAS profile
├── 03-statistical/              3 visuals — Timeseries overview, Bland-Altman, regime change
└── 04-reservoir/                3 visuals — Red River system, Pareto front, ANN forecast
```

## License

All content © Daniele Sala. Not for redistribution.
