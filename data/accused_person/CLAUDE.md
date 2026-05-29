# Accused Person Entries — Working Instructions

**Before writing any narrative text**, read `WRITING_STYLE_GUIDE.md` in this directory.

## Schema Summary

Core fields:
```
id, name, status, trial_id, location_id, year_accused, year_executed,
age_at_trial, social_status, gender
```

Narrative fields (governed by WRITING_STYLE_GUIDE.md):
```
biography, arrest_narrative, interrogation_and_confession,
confession_content, historiographical_analysis, execution_details,
accusations_against_her, contemporary_defense, historiographical_significance
```

Provenance fields:
```
source_method, review_status, confidence, scholarly_sources,
scholarly_disagreement (where applicable)
```

## Status Values

| Value | Meaning |
|-------|---------|
| `Executed` | Death sentence carried out |
| `Pressed to death` | Peine forte et dure (Giles Corey only in this database) |
| `Abjured` | Formally renounced heresy before inquisition; not executed |
| `Acquitted` | Formally found not guilty |
| `Imprisoned` | Imprisoned without execution |
| `Fled` | Escaped before trial completed |

## Confidence → Writing Register (summary)

| Confidence | Opening sentence | Claims | Dates/names |
|------------|-----------------|--------|-------------|
| HIGH | Direct assertion | Indicative mood | State specifically |
| MEDIUM | Named-scholar framing | Hedged where inferred | State where documented |
| LOW | Names the single source | Conditional/modal | Only if in the source |

See WRITING_STYLE_GUIDE.md for full rules and examples.

## Field Notes

**`accusations_against_her`**: Legacy field name from first entry (Binder, female). Schema is immutable — do not create a parallel field. Content should correctly use the subject's pronouns.

**`trial_id`**: If the trial event file does not yet exist, use the logical future slug (e.g., `north-berwick-1590-trials`, `salem-1692-trials`). This creates a forward-reference that validation will flag until the trial entry is created.

**`scholarly_sources`**: Use slug IDs matching entries in `data/demonological_scholar/`. Do not invent new IDs; check what exists first.

**`execution_details`**: Set to `null` for entries where the subject was not executed (benandanti abjurations, acquittals). Do not omit the field.

## Adding a New Entry

1. Use slug pattern: `accused-name-location-year.json`
2. Copy schema from an existing entry of similar confidence level
3. Fill ALL provenance fields — no exceptions
4. Read WRITING_STYLE_GUIDE.md before writing narrative fields
5. Run: `python scripts/validate_entities.py accused_person --check-links`
6. Add the slug to the `accused_persons` array of the relevant `trial_event` entry
