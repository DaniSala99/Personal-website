# Wiki — Personal Site Content System

This directory documents how content flows into the website.

## How it works

All editable content lives in `input/`. The Astro site reads from there; you never need to touch `src/` to update personal data.

```
input/
├── about.md              ← bio, contact info, languages, certifications
├── work/                 ← professional experience (one file per role)
│   ├── 01-progesi.md
│   └── 02-enel.md
├── education/            ← degrees and exchanges (one file per entry)
│   ├── 01-msc-polimi.md
│   ├── 02-erasmus-upv.md
│   └── 03-bsc-polimi.md
├── projects/             ← research and professional case studies
│   ├── 01-po-river.md
│   ├── 02-olona.mdx
│   ├── 03-statistical-paleoclimate.md
│   └── 04-reservoir-optimization.md
├── portfolio/            ← side projects, tools, experiments
│   └── 01-three-gorges.md
└── assets/               ← binary files (cv.pdf, avatar image, etc.)
    └── (place files here, then reference them in frontmatter)
```

## Pages generated

| URL | Source |
|-----|--------|
| `/` | `input/about.md` + `input/projects/` |
| `/about/` | `input/about.md` + `input/work/` + `input/education/` |
| `/work/` | `input/projects/` |
| `/work/[slug]/` | `input/projects/[file].md` |
| `/portfolio/` | `input/portfolio/` |
| `/contact/` | `input/about.md` |

## Guides

- [Naming conventions](naming-conventions.md)
- [Content guide — how to write each file type](content-guide.md)
