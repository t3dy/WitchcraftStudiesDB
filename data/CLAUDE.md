# Data Layer — Working Instructions

## Entity Types and Current Counts

| Type | Count | ID Pattern | Example |
|------|-------|------------|---------|
| `trial_event` | 5 | `trial-location-year` | `bamberg-1626-mass-prosecution` |
| `accused_person` | 15 | `name-location-year` | `margaretha-binder-bamberg-1626` |
| `demonological_concept` | 15 | `concept-name` | `witches-sabbath-collective` |
| `demonological_scholar` | 22 | `surname-firstname-bYYYY` | `ginzburg-carlo-b1939` |
| `scholarly_text` | 17 | `surname-title-word-year` | `clark-thinking-with-demons-2001` |
| `location` | 5 | `location-name` | `bamberg` |
| `healer_practitioner` | 1 | `name-location-tradition` | `gaspar-tagliacarne-friuli-benandante` |
| `persecuted_group` | 4 | `group-descriptor-scope` | `widows-early-modern` |
| `inquisitorial_body` | 5 | `institution-name` | `venetian-inquisition` |
| `timeline` | 25 | `event-descriptor-year` | `malleus-maleficarum-published-1487` |

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
| `persecuted_group` | `accused_person.exemplary_accused_persons[]` (one-directional from group) |
| `inquisitorial_body` | `trial_event.key_trial_events[]` (one-directional from institution) |

After adding an entry, update the cross-reference arrays in related entries.

## Section-Specific Guidance — New Entity Types

For `persecuted_group` entries, read `persecuted_group/CLAUDE.md`. These are analytical categories (modern scholarly groupings), not self-identifications. The `persecution_rationale` field records what contemporaries believed; `structural_vulnerability` and `historiographical_significance` record modern analysis.

For `scholarly_text` entries, read `scholarly_text/CLAUDE.md`. IDs match the slugs already used in `scholarly_sources` arrays throughout the database — creating an entry here resolves the broken cross-references in those arrays. The ID year reflects the edition commonly cited, not necessarily the first-edition year.

For `inquisitorial_body` entries, read `inquisitorial_body/CLAUDE.md`. Note that many major witch trials (Bamberg, Salem, North Berwick) were conducted by secular or episcopal courts, not by the Roman/Spanish/Venetian Inquisitions. The `institutional_type` field carries this distinction. **The Roman and Spanish Inquisitions were generally restraining forces on witch prosecution**, not drivers of it — entries must not perpetuate the contrary popular myth.

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

For `timeline` entries, read `timeline/CLAUDE.md`. Timeline entries capture dated historical events (publications, trials, institutional acts) and link to related entities. They are the chronological spine of the database.

For `demonological_scholar` entries covering historical figures (Bodin, Weyer, Kramer, etc.): these follow the same schema as modern scholars but with `academic_discipline` reflecting their early modern field (Law, Theology, Medicine) and `database_engagement` rather than a personalized engagement field. The `scholarly_sources` array should reference the modern scholarly texts that analyze them.
