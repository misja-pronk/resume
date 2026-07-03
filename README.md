# misja-pronk.github.io/resume

The personal portfolio of **Misja Pronk** — Data & Platform Engineering Consultant and owner of ProRex Consultancy — built as an engineer's **blueprint**: a technical drawing sheet with registration marks, revision tables, detail drawings and a title block.

**Live:** [misja-pronk.github.io/resume](https://misja-pronk.github.io/resume/) (English) · [/nl/](https://misja-pronk.github.io/resume/nl/) (Nederlands)

> MOTTO: MEASURE TWICE · BUILD ONCE

## The concept

The whole site reads as one drawing set:

| Sheet | Section | What it really is |
|-------|---------|-------------------|
| FIG. 001 | The Consultant | Hero with spec line, taped-on site photo and a pipeline schematic |
| SHT 01 | Design Statement | Bio |
| SHT 02 | Primary Structure | The four load-bearing specialisms |
| SHT 03 | Revision History | Career as a drawing revision table |
| SHT 04 | Detail Drawings | 21 client projects, filterable by role |
| SHT 05 | Shop-Fabricated Parts | Open-source work ([isolinear](https://github.com/misja-pronk/isolinear)) |
| SHT 06 | Secondary Structure | The toolbox (skills) |
| SHT 07 | Materials Testing | Certifications with PASSED stamps |
| SHT 08 | Foundation Works | Education |
| SHT 09 | General Notes | The personal fine print |
| SHT 10 | As-Built Graph | Interactive force-directed knowledge graph, headed by a Cypher query |
| SHT 11 | Document Register | The library (books) |
| SHT 12 | Site Diary | Field notes (blog) — posts as numbered engineering memos |

Two themes: **dark** (classic blueprint) and **light** (drafting paper), toggle in the nav. Fully bilingual **EN/NL** with `hreflang` and a language switcher.

## Tech

- [Astro 5](https://astro.build) — fully static, zero JS frameworks (the graph physics and filters are ~150 lines of vanilla TS)
- Content collections for projects (`en/` + `nl/`) and blog posts
- JetBrains Mono + Space Grotesk, self-hosted via Fontsource
- Native Astro i18n routing (`/` = EN, `/nl/` = NL)
- Deployed to GitHub Pages via GitHub Actions

## Development

Tool versions are pinned in [`.mise.toml`](.mise.toml) ([mise](https://mise.jdx.dev)):

```sh
mise install          # installs the pinned Node version
npm install
npm run dev           # http://localhost:4321/resume/
npm run build         # static build into dist/
```

## Editing content

All content is data, no HTML surgery required:

| What | Where |
|------|-------|
| Bio, tagline, stats, socials | [`src/data/profile.ts`](src/data/profile.ts) |
| Jobs / career | [`src/data/experience.ts`](src/data/experience.ts) |
| Specialisms & toolbox | [`src/data/skills.ts`](src/data/skills.ts) |
| Certifications | [`src/data/certifications.ts`](src/data/certifications.ts) |
| Education | [`src/data/education.ts`](src/data/education.ts) |
| Open-source projects | [`src/data/opensource.ts`](src/data/opensource.ts) |
| Books | [`src/data/library.ts`](src/data/library.ts) — covers in `public/img/books/` |
| UI copy (both languages) | [`src/i18n.ts`](src/i18n.ts) |

**Add a project:** create a markdown file in `src/content/projects/en/` *and* `src/content/projects/nl/` (same filename = linked by the language switcher). Frontmatter: `title`, `description`, `client`, `role`, `employer`, `duration` (months) or `ongoing: true`, `order` (lower = more recent), `tags`.

**Write a blog post (field note):** add a markdown file to `src/content/posts/` with `title`, `date`, `summary`, `tags` and `draft: false`. Drafts are visible in `npm run dev` but excluded from the production build.

## Deployment

Every push to `master` builds the site and publishes `dist/` to the `gh-pages` branch via [`.github/workflows/gh-pages.yml`](.github/workflows/gh-pages.yml). Pull requests get a build check but do not deploy.
