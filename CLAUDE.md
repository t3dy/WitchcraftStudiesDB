# Claude Code Instructions — WitchcraftStudiesDB

Digital humanities project: historical witchcraft studies knowledge portal combining relational database (320+ entries), interactive website (7 pages), and academic corpus (30+ sources being converted to Markdown).

## Quick Reference

| File | Purpose |
|------|---------|
| `README.md` | Public project overview |
| `PROJECT_STATUS.md` | Current phase status and metrics |
| `INGEST_MANIFEST.md` | Catalog of PDFs to ingest (559MB) |
| `data/` | JSON database: trials, accused, concepts, texts, scholars, locations, healers |
| `corpus/` | Converted academic PDFs (Markdown) |
| `scripts/` | Python tools: PDF extraction, validation, templates |
| `web/` | Static HTML website (7 pages, 3 constituencies) |
| `documents/` | Project documentation: schemas, standards, frameworks |

## Current Phase

**Phase 2: Academic Corpus Ingestion** (In Progress)
- PDF extraction pipeline: ✅ Complete and tested
- First conversion: ✅ Clark's *Thinking with Demons* (3MB Markdown)
- Tier 1 queue: ⏳ Ginzburg, Hutton, Ankarloo/Clark Vol 2-4
- Target: 30+ academic sources converted by end of phase

## Key Tools

### PDF Conversion
```bash
# Single file
python scripts/pdf_to_markdown.py --single "path/to/file.pdf" -o corpus/

# Batch conversion (by pattern)
python scripts/pdf_to_markdown.py "E:/pdf/witchcraft studies Hutton" \
  -o corpus/ \
  --pattern "*Hutton*Witch*.pdf"

# Batch script (Tier 1 PDFs)
bash scripts/batch_convert_tier1.sh
```

### Data Validation
```bash
# Full validation report
python scripts/validate_entities.py --all --report json

# Check trial database
python scripts/validate_entities.py trial_event --check-links

# Generate CSV
python scripts/validate_entities.py --report csv
```

### Template Generation
```bash
# Create 10 empty trial templates
python scripts/generate_templates.py trial_event 10 --output data/trial_event/
```

## Data Structure

### 8 Entity Types

1. **TRIAL_EVENT** (40): Dated prosecutions with accused count, outcome, demonological framework
2. **ACCUSED_PERSON** (40): Individual defendants with occupation, reputation, torture records
3. **DEMONOLOGICAL_CONCEPT** (30): Theoretical concepts with Actor/Analyst distinction
4. **TEXT** (40+): Primary and secondary sources (Malleus, Bodin, Clark, Hutton, etc.)
5. **DEMONOLOGICAL_SCHOLAR** (30+): Contemporary historians (Clark, Hutton, Ginzburg, Roper, etc.)
6. **LOCATION** (40+): Geographic entries with coordinates and trial associations
7. **HEALER_PRACTITIONER** (30+): Individual wise women, cunning folk, healers
8. **[Other types]**: Additional entities as needed

### Provenance on Every Entry

```json
{
  "source_method": "Published trial records | primary manuscript | scholarly monograph",
  "review_status": "DRAFT | REVIEWED | VERIFIED",
  "confidence": "HIGH | MEDIUM | LOW",
  "scholarly_disagreement": "Text describing historiographical debate"
}
```

## Historiographical Framework

**Three Scholarly Traditions** (core approach):
- **Stuart Clark** (Intellectual History): Demonology as theological tradition, not irrational belief
- **Ronald Hutton** (Social History): Cunning folk as legitimate practitioners, demographic analysis
- **Carlo Ginzburg** (Microhistory): Interrogation analysis, torture-shaped confessions, voice recovery

**8 Historiographical Principles**:
1. Provenance on every claim
2. Rationality within framework
3. Actor/Analyst distinction (practitioners' own language vs. modern categories)
4. Regional variation as primary
5. Microhistorical attention to individuals
6. Material grounding (what people actually did)
7. Intellectual history seriously
8. Ambiguity preserved (state historiographical disagreement)

## When Working on WitchcraftStudiesDB

### Adding Database Entries

1. Follow `documents/STANDARD_*.md` format (e.g., STANDARD_TRIAL_EVENTS.md)
2. Use slug-based IDs: `trial-location-year` or `accused-name-location-year`
3. Include all provenance fields (source_method, review_status, confidence, scholarly_disagreement)
4. Cross-link related entities using slug arrays
5. Validate: `python scripts/validate_entities.py --check-links`

### Converting PDFs

1. Source PDFs are in `E:/pdf/witchcraft studies Hutton/` (559MB)
2. Use `scripts/pdf_to_markdown.py` for extraction (pdfplumber-based)
3. Output goes to `corpus/` directory
4. After conversion, add entry to `corpus/MANIFEST.md` and update progress
5. Run cross-reference mapping: see `corpus/SOURCE_DATABASE_MAPPING.md`

### Corpus Integration

- Each converted PDF gets metadata entry in `corpus/MANIFEST.md`
- Cross-reference mapping in `corpus/SOURCE_DATABASE_MAPPING.md`
- Link specific corpus sections (pages/chapters) to database entries
- Example: `clark-thinking-with-demons-2001 | pp. 234-240 → bamberg-1626-mass-prosecution`

## Project Constraints

1. **No frameworks**: Vanilla HTML/CSS/JS only (no React, no Node)
2. **JSON is immutable schema**: Once a field is added, it's in every entry of that type
3. **Slug-based linking**: All cross-references use lowercase-hyphenated IDs, not UUIDs or numeric IDs
4. **Idempotent scripts**: All Python scripts safe to re-run (`CREATE TABLE IF NOT EXISTS` style)
5. **Provenance non-negotiable**: Every substantive claim must have source_method + confidence

## Common Workflows

### Ingest a New Academic Source

1. Add PDF to `E:/pdf/witchcraft studies Hutton/` or reference it
2. Update `INGEST_MANIFEST.md` with metadata
3. Run: `python scripts/pdf_to_markdown.py --single "path" -o corpus/`
4. Add entry to `corpus/MANIFEST.md` with status ✅ CONVERTED
5. Map trials/concepts/scholars in `corpus/SOURCE_DATABASE_MAPPING.md`
6. Update `PROJECT_STATUS.md` with progress

### Add a Trial Entry

1. Create `data/trial_event/trial-location-year.json`
2. Follow `documents/STANDARD_TRIAL_EVENTS.md` format
3. Include accused person IDs in `"accused"` array
4. Include concept IDs in `"demonological_framework"` array
5. Link scholarly sources in `"scholarly_sources"` array
6. Run validation: `python scripts/validate_entities.py trial_event --check-links`

### Add an Accused Person Entry

1. Create `data/accused_person/accused-name-location-year.json`
2. Follow `documents/STANDARD_WITCH_BIOGRAPHIES.md` format
3. Link to trial via `"trial_id"`
4. Include torture records with `"torture_method"`, `"torture_sessions"`, `"torture_applied"`
5. Document confession status and content
6. Validate links to trial

### Create a Concept Definition

1. Create `data/demonological_concept/concept-slug.json`
2. Follow `documents/STANDARD_CONCEPT_DEFINITIONS.md` format
3. Set `"category_type"`: `ACTOR_TERM` (historical) or `ANALYST_TERM` (modern)
4. Include trial examples in `"trial_examples"` array
5. Document scholarly debates in `"scholarly_disagreement"`
6. Link related concepts in `"related_concepts"`

## Repository Standards

**Naming Conventions**:
- Files: lowercase-with-hyphens
- IDs: lowercase-hyphenated slugs (not CamelCase)
- JSON keys: lowercase_with_underscores
- Markdown headings: Title Case with proper formatting

**Metadata Requirements**:
- source_method: How we know this (published record, archival, scholarly citation, reconstruction)
- review_status: DRAFT (unreviewed) | REVIEWED (second reader) | VERIFIED (source checked)
- confidence: HIGH (well-established) | MEDIUM (some inference, scholarly debate) | LOW (sparse, speculative)
- scholarly_disagreement: Explicit statement of historiographical debate (where historians disagree)

## Deployment & Output

### Current
- Data: JSON files in `data/*/`
- Website: Static HTML in `web/`
- Corpus: Markdown in `corpus/`
- Tools: Python scripts in `scripts/`

### Future
- Static site generation: `python scripts/build_website.py` (TBD)
- GitHub Pages deployment: Push to `gh-pages` branch
- Search interface: Full-text search across corpus + database
- Historiographical visualization: Clark vs. Hutton vs. Ginzburg approaches

## Troubleshooting

### PDF Conversion Fails
- Check file exists: `ls "E:/pdf/witchcraft studies Hutton/"`
- Check permissions: User has read access
- Try single file: `python scripts/pdf_to_markdown.py --single "path"`
- Check file format: Some PDFs may be corrupted from library genesis

### Link Validation Errors
- Run: `python scripts/validate_entities.py trial_event --check-links`
- Fix missing slug references (trial_id, accused IDs, concept IDs)
- Check slug format: lowercase-hyphenated, no spaces or uppercase

### Memory Issues
- Large PDFs (69M+) may need more RAM
- Run conversions one at a time instead of batch
- Increase Python memory: `python -Xmx4g scripts/pdf_to_markdown.py`

## Project History

**Phase 1 Completion**: May 2026
- Conceptual framework (8 historiographical principles)
- Complete database (320+ entities across 8 types)
- Static website prototype (7 pages)
- Validation tools

**Phase 2 Start**: May 23, 2026
- PDF extraction pipeline implemented
- First conversion successful (Clark)
- Tier 1-3 queue established
- Cross-reference mapping structure designed

## References & Attribution

- **Clark, Stuart**: *Thinking with Demons* (intellectual history of demonology)
- **Hutton, Ronald**: *Pagan Britain*, *The Witch* (social history, cunning folk)
- **Ginzburg, Carlo**: *Night Battles*, *Ecstasies* (microhistory, interrogation analysis)
- **Roper, Lyndal**: *Witch Craze* (gender history)
- **Levack, Brian**: *The Witch-Hunts in Early Modern Europe* (comparative history)
- **Briggs, Robin**: *Witches and Neighbors* (community-based analysis)

## Contact

For questions about this project, see the main README.md or PROJECT_STATUS.md.

---

**WitchcraftStudiesDB** — Historical Witchcraft Studies Knowledge Portal
*Version 1.0 | Built on frameworks of Clark, Hutton, and Ginzburg*
