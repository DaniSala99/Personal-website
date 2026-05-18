# danielesala.com — Personal Portfolio

Personal portfolio site for Daniele Sala, environmental engineer specialised in flood risk modeling, hydrological forecasting and CSRD-aligned physical risk analytics.

Built with [Astro](https://astro.build/) (v6), deployed on GitHub Pages.

## Stack

- **Astro** — static site generator
- **Astro Content Collections** — case study markdown files in `./case-studies/`
- **Custom rehype plugin** — converts markdown `<img>` to `<figure class="img-placeholder">` for placeholder-aware rendering
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

Markdown files in `./case-studies/`. Each file requires the following frontmatter:

```yaml
title: string
subtitle: string
client: string
year: string
duration: string
tools: [array of strings]
hero_image: string (optional)
```

## Content files

- `about-me.md` — About text (two versions: site and freelance platforms)
- `experience.md` — CV-style experience and education
- `taglines.md` — Headline and tagline variants
