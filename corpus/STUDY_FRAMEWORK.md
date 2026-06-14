# Corpus Study Framework — Artifact Extraction

## Purpose

This framework governs how agents extract structured knowledge from corpus Markdown files into **artifacts** — reusable, structured extractions that let future agents write database entries without re-reading the full text.

A corpus text should be read **once** and turned into an artifact. All subsequent database entries drawn from that text are written from the artifact, not from the source file. This eliminates redundant context consumption and ensures consistency.

---

## Corpus Inventory

| Filename | Source Work | Author | DB Entry |
|----------|------------|--------|----------|
| `thinking-with-demons-the-idea-of-witchcraft-in-ear.md` | *Thinking with Demons* | Stuart Clark | `clark-thinking-with-demons-2001` |
| `the-witch-history-fear-ancient-present.md` | *The Witch* | Ronald Hutton | `hutton-the-witch-2017` |
| `night-battles-witchcraft-agrarian-cults.md` | *Night Battles* | Carlo Ginzburg | `ginzburg-night-battles-1983` |
| `witchcraft-magic-europe-vol3-middle-ages.md` | *Witchcraft and Magic in Europe*, Vol. 3 | Ankarloo & Clark (eds.) | `ankarloo-clark-vol3-middle-ages-2002` |
| `witchcraft-magic-europe-vol4-early-modern-trials.md` | *Witchcraft and Magic in Europe*, Vol. 4 | Ankarloo & Clark (eds.) | `ankarloo-clark-vol4-witch-trials-2001` |
| `the-triumph-of-the-moon-a-history-of-modern-pagan-.md` | *The Triumph of the Moon* | Ronald Hutton | `hutton-triumph-moon-1999` |
| `queens-of-the-wild.md` | *Queens of the Wild* | Ronald Hutton | (needs scholarly_text entry) |
| `pagan-britain.md` | *Pagan Britain* | Ronald Hutton | (needs scholarly_text entry) |
| `the-pagan-religions-of-the-ancient-british-isles-t.md` | *Pagan Religions of the Ancient British Isles* | Ronald Hutton | (needs scholarly_text entry) |
| `biblical-and-pagan-societies.md` | *Biblical and Pagan Societies* | (TBD — check first pages) | (needs entry) |

---

## Navigation Strategy for Large Corpus Files

These files range from 344KB to 2.9MB (Markdown). Do NOT attempt to read them linearly.

### Step 1: Find the Structure

```bash
# Get the first 300 lines (title, TOC, preface)
Read file_path, limit=300

# Find chapter headings
Grep pattern="^## |^### |^# [A-Z]" path=<corpus-file>

# Find page markers (PDF conversion artifacts)
Grep pattern="^---$|^\*\*\*$|^={3,}" path=<corpus-file>
```

### Step 2: Locate Key Sections by Keyword

```bash
# Find mentions of specific scholars
Grep pattern="Ginzburg|Hutton|Clark|Briggs|Levack" path=<corpus-file> output_mode=content

# Find demonological figures
Grep pattern="Nider|Kramer|Bodin|Weyer|Rémy|Binsfeld" path=<corpus-file>

# Find specific concepts
Grep pattern="sabbath|maleficium|pact|familiar|benandanti" path=<corpus-file>
```

### Step 3: Read Targeted Sections

```bash
# Read 100-200 lines around a hit (use offset + limit)
Read file_path, offset=<hit-line-minus-10>, limit=200
```

### Step 4: Build Artifact

Write findings into `corpus/artifacts/<text-slug>/artifact.md`. See artifact template below.

---

## Artifact Template

Create one directory per source text: `corpus/artifacts/<text-slug>/`

Files inside:
- `artifact.md` — Main structured extraction (required)
- `passages.md` — Direct quotes for use in DB entries (optional, for rich texts)
- `gap-list.md` — Generated list of DB entries to create/enhance (required)

### artifact.md Template

```markdown
# Artifact: [Full Title]

**Source file**: `corpus/[filename].md`
**DB entry**: `data/scholarly_text/[slug].json`
**Extracted**: [ISO date]
**Pages (approx.)**: [based on PDF metadata or estimate]

---

## Core Thesis (2–4 sentences)

[State the central argument of the work in full sentences. Not bullet points.]

---

## Major Arguments by Chapter / Section

### [Part/Chapter Title]
- **Argument**: [One sentence]
- **Evidence**: [What the author uses to support it]
- **DB relevance**: [Which entity types or specific entries this supports]

[Repeat for each major section]

---

## Historical Figures Mentioned

| Name | Dates | Role | Works | Pages | DB entry (or needed) |
|------|-------|------|-------|-------|----------------------|
| Johannes Nider | c.1380–1438 | Dominican theologian | *Formicarius* (1437) | pp. 55–78 | `nider-johannes-b1380` ✓ |
| Bernardino of Siena | 1380–1444 | Franciscan preacher | Sermons (1427) | pp. 60–62 | MISSING |

---

## Modern Scholars Discussed or Engaged

| Scholar | Position taken | Key work cited | DB entry |
|---------|---------------|----------------|---------|
| Cohn | Opposed — sabbath is elite fabrication | *Europe's Inner Demons* | `cohn-norman-b1915` ✓ |

---

## Concepts Developed in This Text

| Concept name | Category | Definition | DB entry (or needed) |
|-------------|----------|-----------|----------------------|
| Preternatural | ACTOR_TERM | The category between natural and supernatural in scholastic thought | `preternatural-category` ✓ |

---

## Trial Events and Cases Referenced

| Event | Date | Location | Pages | DB entry |
|-------|------|----------|-------|---------|
| Bamberg trials | 1626–1631 | Bamberg | pp. 121–130 | `bamberg-1626-mass-prosecution` ✓ |

---

## Timeline Events (Specific Dates/Publications)

| Date | Event | Significance for DB | DB entry |
|------|-------|--------------------|---------| 
| 1484 | *Summis Desiderantes* issued | First papal endorsement of witch prosecution | `summis-desiderantes-papal-bull-1484` ✓ |

---

## Scholarly Works Cited (not yet in DB)

| Author | Title | Year | DB entry needed? |
|--------|-------|------|-----------------|
| Ostorero, Martine | *L'imaginaire du sabbat* | 1999 | YES |

---

## Key Passages

Collect direct quotes (100–300 words max each) relevant to specific DB entries:

### For: `witches-sabbath-collective`
> "[Quote from pp. X]"
*Why this passage matters: [one sentence]*

---

## Gap List — DB Entries to Create

Generated from this extraction:

### New `demonological_scholar` entries
- [ ] `bernardino-of-siena-b1380` — Franciscan preacher, early anti-witchcraft sermons (pp. 60-62)
- [ ] `peter-of-berne-fl1430` — Secular judge, source for Nider's cases (pp. 63-65)

### New `scholarly_text` entries  
- [ ] `ostorero-imaginaire-sabbat-1999` — Critical edition of Alpine trial documents

### New `demonological_concept` entries
- [ ] `learned-vs-popular-magic` — Kieckhefer's foundational distinction

### Entries to enhance (add passages/analysis)
- [ ] `clark-thinking-with-demons-2001` — Enhance `key_arguments` with chapter-specific claims
- [ ] `nider-johannes-b1380` — Add specific Formicarius chapter analysis
```

---

## Quality Standards for Artifacts

1. **No paraphrase inflation** — Extract what the text actually says. If you're not sure what a section argues, say so rather than guessing.

2. **Page references** — Include them where the PDF conversion preserves them. Many Markdown conversions drop page numbers; if so, note "page refs unavailable from Markdown conversion."

3. **Gap list must be actionable** — Every item in the gap list must include: entity type, proposed ID, brief justification, page reference if available.

4. **Distinguish primary from secondary claims** — Note when the corpus text is itself citing another work (e.g., Clark citing Cohn) vs. making an original argument.

5. **Actor/Analyst discipline** — When extracting concepts, tag them as ACTOR_TERM (contemporary terminology) or ANALYST_TERM (modern scholarly category). This distinction matters throughout the database.

---

## Workflow Sequence

```
1. NAVIGATE: Find TOC and chapter structure (Read first 300 lines + Grep headings)
2. SURVEY: Read 1-2 pages from each major section (Grep + targeted Read)
3. EXTRACT: Fill artifact template sections in order
4. GAP-LIST: Generate gap-list.md from extraction
5. COMMIT: Write artifact files to corpus/artifacts/<slug>/
6. POPULATE: Use gap-list.md to queue DB entry creation
```

---

## Priority Queue

Artifacts to create (in order):

| Priority | Text | Status | Target |
|----------|------|--------|--------|
| 1 | Clark, *Thinking with Demons* | NOT STARTED | `corpus/artifacts/clark-thinking-with-demons/` |
| 2 | Hutton, *The Witch* | NOT STARTED | `corpus/artifacts/hutton-the-witch/` |
| 3 | Ginzburg, *Night Battles* | NOT STARTED | `corpus/artifacts/ginzburg-night-battles/` |
| 4 | Ankarloo/Clark Vol. 3 | NOT STARTED | `corpus/artifacts/ankarloo-clark-vol3/` |
| 5 | Ankarloo/Clark Vol. 4 | NOT STARTED | `corpus/artifacts/ankarloo-clark-vol4/` |
| 6 | Hutton, *Triumph of the Moon* | NOT STARTED | `corpus/artifacts/hutton-triumph-moon/` |
