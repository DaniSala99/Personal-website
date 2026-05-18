# danielesala.com — Personal Portfolio

Personal portfolio site for Daniele Sala, environmental engineer specialised in flood risk modeling, hydrological forecasting and CSRD-aligned physical risk analytics.

Built with [Astro](https://astro.build/) (v6), deployed on GitHub Pages.

## Stack

- **Astro** — static site generator
- **Astro Content Collections** — case study markdown files in `src/content/work/`
- **Custom rehype plugin** — wraps markdown `<img>` in `<figure class="img-placeholder">` with figcaptions
- **CSS custom properties** — dark/light theme via `src/styles/global.css`

## Pages

| Route | Description |
|---|---|
| `/` | Home with two-column hero (text + portrait) and case studies preview |
| `/work/` | All case studies |
| `/work/[slug]` | Individual case study (rendered from markdown) |
| `/about/` | Background, experience, education |
| `/projects/` | Lab and side projects |
| `/contact/` | Contact links |

## Development

```sh
npm install
npm run dev        # localhost:4321
npm run build      # production build to ./dist/
npm run preview    # preview build locally
```

### Quick start
```sh
aprisito           # Starts dev server and opens browser automatically
```

The `aprisito` command launches the dev server and automatically opens the site in your default browser.

## Case studies

Markdown files in `src/content/work/`, loaded via Astro Content Collections. Each file requires the following frontmatter:

```yaml
title: string
subtitle: string
client: string
year: string
duration: string
tools: [array of strings]
hero_image: string (optional)
```

## Portfolio images

High-resolution case study images (300 DPI PNGs, ~4 MB total) organized in `public/portfolio/img/`. The rehype plugin automatically wraps images in `<figure>` elements with alt-text captions.

| Folder | Content | Slug |
|---|---|---|
| `01-po/` | Po River Basin: basin map, discharge timeseries, sensitivity analysis | case-study-1-po-river |
| `02-olona/` | Olona Flood Protection: DEM, critical hydrographs, HEC-RAS profile | case-study-2-olona-flood-protection |
| `03-statistical/` | Paleoclimate Statistical Analysis: reconstructions, Bland-Altman, regime change | case-study-3-statistical-paleoclimate |
| `04-reservoir/` | Reservoir Optimization (Hoa Binh): system map, Pareto front, ANN forecast | case-study-4-reservoir-optimization |

Images are embedded in markdown via `![alt text](/portfolio/img/{01-04}-{slug}/filename.png)` and automatically wrapped in figures with captions.

## Content files

- `about-me.md` — About text (two versions: site and freelance platforms)
- `experience.md` — CV-style experience and education
- `taglines.md` — Headline and tagline variants
