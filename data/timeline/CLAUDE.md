# Timeline Entity Type — Working Instructions

## Purpose

The `timeline/` directory holds individual JSON entries for dated historical events that provide chronological context for the database's entities. Each entry captures a single event (publication, trial, institutional action, political event) and links to related entities elsewhere in the database.

## Schema

```json
{
  "id": "event-slug-year",
  "event_name": "Short title (under 10 words)",
  "event_type": "primary_source_publication | trial_event | institutional_event | biographical | political_event",
  "date": "YYYY",
  "date_precision": "exact | approximate | circa",
  "circa_range": "YYYY-YYYY",
  "location": "Place name (text)",
  "location_slug": "slug-or-null",
  "significance": "1-2 sentence description of historical importance",
  "related_entities": ["slug1", "slug2"],
  "source_method": "...",
  "confidence": "HIGH | MEDIUM | LOW",
  "review_status": "DRAFT | REVIEWED | VERIFIED",
  "scholarly_sources": ["slug1"],
  "created_date": "YYYY-MM-DD",
  "last_modified": "YYYY-MM-DD"
}
```

## ID Pattern

`[event-descriptor]-[year]`

Examples:
- `malleus-maleficarum-published-1487`
- `north-berwick-trials-1590`
- `cautio-criminalis-published-1631`

## `event_type` Vocabulary

| Value | Examples |
|-------|---------|
| `primary_source_publication` | Malleus, Daemonologie, Cautio |
| `trial_event` | Salem 1692, Bamberg 1626, North Berwick 1590 |
| `institutional_event` | Papal bulls, Council decrees, court establishment |
| `biographical` | Birth/death of key figures |
| `political_event` | Events affecting witch prosecution context |

## Date Precision

- `exact`: date is securely documented to year
- `approximate`: plausible year range within ±5 years
- `circa`: known only within broader range; use `circa_range` field

## Relationship to Other Entities

Timeline entries link to:
- `trial_event`: via `related_entities`
- `demonological_scholar`: via `related_entities`
- `scholarly_text`: via `related_entities`
- `location`: via `location_slug`

## Validation

No validation script yet. Keep all IDs consistent with existing entity slugs.
