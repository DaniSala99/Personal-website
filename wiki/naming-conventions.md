# Naming Conventions

## General rules

- All filenames use lowercase kebab-case: `my-file-name.md`
- Files that appear in a list use a two-digit numeric prefix to control sort order: `01-`, `02-`, `03-`
- The numeric prefix determines display order on the site (lower = shown first)
- Do not put spaces or uppercase letters in filenames

## Per-directory conventions

### `input/work/` — professional experience

```
NN-company-slug.md
```

Examples:
- `01-progesi.md`
- `02-enel.md`
- `03-freelance.md`

Order: most recent role first (01 = current position).

### `input/education/` — academic degrees

```
NN-degree-institution-slug.md
```

Examples:
- `01-msc-polimi.md`
- `02-erasmus-upv.md`
- `03-bsc-polimi.md`

Order: most recent degree first.

### `input/projects/` — research and professional case studies

```
NN-short-project-name.md   (plain markdown)
NN-short-project-name.mdx  (if you need interactive components)
```

Examples:
- `01-po-river.md`
- `02-olona.mdx`
- `03-statistical-paleoclimate.md`

Order: feature order on the site (most prominent project = 01).

### `input/portfolio/` — side projects and experiments

```
NN-project-name.md
```

Examples:
- `01-three-gorges.md`
- `02-my-tool.md`

Order: display order on the portfolio page.

### `input/assets/` — binary files

No prefix required. Use descriptive names:
- `cv.pdf`
- `research-proposal.pdf`
- `avatar.jpg`

Reference them in frontmatter as `/assets/filename.ext` (served from `public/assets/`).
