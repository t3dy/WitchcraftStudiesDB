# Corpus — Working Instructions

## Purpose

The `corpus/` directory holds Markdown conversions of academic PDFs. Source PDFs (559MB total) are in `E:/pdf/witchcraft studies Hutton/`. See `scripts/CLAUDE.md` for conversion commands.

## Workflow: Ingest a New Academic Source

1. Confirm the PDF is in the Tier 1-3 queue (`INGEST_MANIFEST.md`)
2. Convert: `python scripts/pdf_to_markdown.py --single "path/to/file.pdf" -o corpus/`
3. Add entry to `corpus/MANIFEST.md` with status ✅ CONVERTED
4. Map to database entries in `corpus/SOURCE_DATABASE_MAPPING.md`:
   - Format: `source-slug | pp. X–Y → database-entry-slug`
   - Example: `clark-thinking-with-demons-2001 | pp. 234-240 → bamberg-1626-mass-prosecution`
5. Update `PROJECT_STATUS.md`

## Manifest Format

Each converted source gets one entry in `corpus/MANIFEST.md`:
```
| slug | Title | Author | Year | Status | Pages | Notes |
```

## Cross-Reference Mapping

`SOURCE_DATABASE_MAPPING.md` links corpus passages to database entries. When a corpus source directly supports a claim in a JSON entry, add the mapping. This enables future full-text search and citation verification.

## Tier Queue

- **Tier 1** (highest priority): Ginzburg *Night Battles*, *Ecstasies*; Hutton *The Witch*; Ankarloo/Clark Vol 2-4
- **Tier 2**: Levack, Briggs, Roper, Larner
- **Tier 3**: Regional and specialist sources
