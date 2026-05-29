# Claude Code Instructions — WitchcraftStudiesDB

Digital humanities project: historical witchcraft studies knowledge portal combining a relational JSON database, static website, and academic corpus. Core discipline: rigorous historiography of European and transatlantic witch trials (1428–1692).

## Navigation — Read the Local CLAUDE.md Before Working in a Section

| Directory | Local Guide | Loads When You… |
|-----------|-------------|-----------------|
| `data/` | `data/CLAUDE.md` | Add or edit any JSON entry |
| `data/accused_person/` | `data/accused_person/CLAUDE.md` + `WRITING_STYLE_GUIDE.md` | Write biographical prose |
| `scripts/` | `scripts/CLAUDE.md` | Run tools or debug conversion |
| `corpus/` | `corpus/CLAUDE.md` | Ingest or map academic PDFs |

## Essential Constraints

1. **No frameworks**: Vanilla HTML/CSS/JS only in `web/` — no React, no Node, no build steps
2. **JSON schema is immutable**: Once a field is added to an entity type, every entry of that type must have it
3. **Slug-based IDs only**: All cross-references use `lowercase-with-hyphens`, not UUIDs or numeric IDs
4. **Idempotent scripts**: All Python scripts are safe to re-run without side effects
5. **Provenance non-negotiable**: Every substantive claim in every JSON entry requires `source_method` + `confidence` fields

## Historiographical Framework — Always Applies

**Three Scholarly Traditions** (the interpretive lens for all database entries):
- **Stuart Clark** — Intellectual history: demonology as coherent theological tradition, not irrational belief (*Thinking with Demons*, 1997)
- **Ronald Hutton** — Social history: cunning folk as legitimate practitioners; demographic analysis of trial victims (*The Witch*, 2017)
- **Carlo Ginzburg** — Microhistory: interrogation analysis, torture-shaped confessions, recovery of subaltern voices (*Night Battles* 1983, *Ecstasies* 1991)

**8 Principles** applied to every database entry and all written prose:
1. Provenance on every claim — name the source, not just the confidence level
2. Rationality within framework — accused and accusers acted within coherent belief systems
3. Actor/Analyst distinction — use quotation marks or framing for contemporaries' own terms; identify modern scholarly categories as such
4. Regional variation as primary — no monolithic "witch hunt"; context is always specific
5. Microhistorical attention to individuals — structural analysis must not erase personal specificity
6. Material grounding — what people actually did, not only what was alleged against them
7. Intellectual history taken seriously — demonological theory is theology, not superstition
8. Ambiguity preserved — state historiographical disagreement explicitly, with named scholars

## Current Phase

**Phase 2: Academic Corpus Ingestion** (In Progress)
- PDF extraction pipeline: ✅ Complete and tested
- First conversion: ✅ Clark's *Thinking with Demons* (3MB Markdown)
- Tier 1 queue: ⏳ Ginzburg, Hutton, Ankarloo/Clark Vol 2-4
- Target: 30+ academic sources converted by end of phase

## Quick Reference

| File | Purpose |
|------|---------|
| `PROJECT_STATUS.md` | Current phase status and metrics |
| `INGEST_MANIFEST.md` | Catalog of PDFs to ingest (559MB) |
| `data/` | JSON database (6 entity types) |
| `corpus/` | Converted academic PDFs (Markdown) |
| `scripts/` | Python tools: PDF extraction, validation, templates |
| `web/` | Static HTML website (7 pages) |
