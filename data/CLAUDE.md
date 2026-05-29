# Data Layer — Working Instructions

## Entity Types and Current Counts

| Type | Count | ID Pattern | Example |
|------|-------|------------|---------|
| `trial_event` | 2 | `trial-location-year` | `bamberg-1626-mass-prosecution` |
| `accused_person` | 15 | `accused-name-location-year` | `margaretha-binder-bamberg-1626` |
| `demonological_concept` | 2 | `concept-name` | `witches-sabbath-collective` |
| `demonological_scholar` | 3 | `surname-firstname-bYYYY` | `ginzburg-carlo-b1939` |
| `location` | 1 | `location-name` | `bamberg` |
| `healer_practitioner` | 1 | `name-location-tradition` | `gaspar-tagliacarne-friuli-benandante` |

## JSON Conventions

- Keys: `lowercase_with_underscores`
- IDs: `lowercase-with-hyphens`
- Cross-references: slug arrays only (no numeric IDs, no UUIDs)
- Missing data: `null` not `""` or omitted field
- Schema is **immutable**: once a field appears in an entity type, it exists in every entry

## Provenance Fields — Required on Every Entry

```json
{
  "source_method": "Specific: 'Bamberg episcopal archives, via Behringer 1997' not 'published sources'",
  "review_status": "DRAFT | REVIEWED | VERIFIED",
  "confidence": "HIGH | MEDIUM | LOW",
  "scholarly_disagreement": "Name the historians on each side; 'historians disagree' alone is not acceptable"
}
```

**confidence meanings**:
- `HIGH` — Archival or published primary source; secure scholarly consensus
- `MEDIUM` — Scholarly reconstruction from fragmentary evidence; inference required
- `LOW` — Named in one source only; no independent corroboration; identity uncertain

## Cross-Linking Requirements

| Entity | Must link to |
|--------|-------------|
| `accused_person` | `trial_event.accused_persons[]` |
| `trial_event` | `location`, `demonological_concept[]`, `accused_persons[]` |
| `healer_practitioner` | `location`, `trial_event[]` if applicable |

After adding an entry, update the cross-reference arrays in related entries.

## Validation Commands

```bash
# Full validation report
python scripts/validate_entities.py --all --report json

# Check cross-links for a specific type
python scripts/validate_entities.py trial_event --check-links
python scripts/validate_entities.py accused_person --check-links

# Generate CSV export
python scripts/validate_entities.py --report csv
```

## Naming Conventions

- Files: `lowercase-with-hyphens.json`
- JSON keys: `lowercase_with_underscores`
- Markdown headings: Title Case

## Section-Specific Guidance

For `accused_person` entries, read `accused_person/CLAUDE.md` and `accused_person/WRITING_STYLE_GUIDE.md` before writing narrative fields. Writing quality requirements are strict — see the style guide.
