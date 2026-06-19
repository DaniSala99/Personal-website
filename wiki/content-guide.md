# Content Guide

## `input/about.md`

The single source of truth for personal information. Frontmatter fields:

```yaml
---
name: "Your Name"
tagline: "Short professional tagline"
avatar: "/assets/avatar.png"       # path relative to public/
location: "City, Country"
email: "you@example.com"
linkedin: "https://linkedin.com/in/handle"
github: "https://github.com/handle"
certifications:
  - "Certificate name (issuer)"
languages:
  - "Italian (native)"
  - "English (C1)"
---
```

The markdown body becomes the bio paragraph on the About page.

---

## `input/work/NN-company.md`

One file per job. Frontmatter:

```yaml
---
title: "Job Title"
company: "Company Name"
start: "2024"          # year as string
end: "2025"            # year as string, or null for current role
skills:
  - "skill one"
  - "skill two"
---
```

The markdown body is the full role description. Use `**bold**` for highlights and `*italic*` for NDA notices.

---

## `input/education/NN-degree.md`

One file per degree or exchange. Frontmatter:

```yaml
---
degree: "M.Sc. Degree Name"
institution: "University Name"
location: "City, Country"
start: 2021              # integer year
end: 2024                # integer year, or null if ongoing
grade: "106/110"         # string, or null if not applicable
description: "One-line summary of coursework or focus"
---
```

No markdown body needed (description covers it). Add a body only for extra context.

---

## `input/projects/NN-slug.md`

Full case study. Frontmatter:

```yaml
---
title: "Full Project Title"
subtitle: "One-sentence summary shown on the card."
hero_image: "/portfolio/img/NN-slug/hero.png"   # optional
client: "Institution · Course or context"
year: "2024"
duration: "12 months"
tools:
  - "Python"
  - "QGIS"
---
```

The markdown body is the full case study. Recommended section structure:

```markdown
## ▸ The Challenge
## ▸ My Approach
## ▸ The Solution
## ▸ Key Results
## ▸ Applied Context
## ▸ Tech Stack
```

Use `.mdx` extension (instead of `.md`) only if you need to embed interactive Astro components.

---

## `input/portfolio/NN-project.md`

Side project or experiment. Frontmatter:

```yaml
---
title: "Project Title"
year: "2023"
type: "Type label shown as badge (e.g. 'Side Project', 'Open Source')"
description: "2–3 sentence description"
tools:
  - "HTML5"
  - "Python"
repo: "https://github.com/handle/repo"   # optional
url: "https://live-demo.com"              # optional
---
```

No markdown body needed; description covers it.

---

## Adding images

Place images under `public/portfolio/img/NN-slug/` and reference them in markdown as:

```markdown
![Alt text](/portfolio/img/01-po/figure-name.png)
```

Place static binary documents (PDF) under `public/assets/` and reference in frontmatter as `/assets/cv.pdf`.
