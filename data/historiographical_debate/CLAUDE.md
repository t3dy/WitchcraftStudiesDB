# historiographical_debate — Working Instructions

## What Belongs Here

Named scholarly controversies about the history of witchcraft prosecution — the points where historians explicitly argue against each other's interpretations. An entry should represent a debate that: (a) has multiple named scholars taking distinct positions, (b) has been active in the secondary literature, and (c) is directly relevant to how we should read the rest of the database.

**Not** minor disagreements about a single trial's details — those go in `scholarly_disagreement` fields on `trial_event` or `accused_person` entries. This entity type is for field-level debates with methodological stakes.

## ID Pattern

`debate-name-keyword` — e.g., `sabbath-origins-debate`, `gender-thesis-debate`, `torture-testimony-debate`.

## Required Fields (Immutable Schema)

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | Slug ID |
| `name` | string | Display name |
| `question_at_issue` | string | The central contested question, stated precisely |
| `date_range_of_scholarship` | string | e.g., `"1970–present"` |
| `scholarly_positions` | array | See structure below |
| `current_consensus` | string\|null | State of scholarly agreement; null if genuinely open |
| `consensus_status` | string | See controlled vocabulary below |
| `counter_arguments` | string\|null | Remaining objections to consensus, or main lines of ongoing disagreement |
| `database_relevance` | string | How this debate should shape how readers interpret database entries |
| `linked_concepts` | array | Slugs of relevant `demonological_concept` entries |
| `linked_scholarly_texts` | array | Slugs of key `scholarly_text` entries |
| `source_method` | string | Secondary scholarly synthesis |
| `review_status` | string | `DRAFT` / `REVIEWED` / `VERIFIED` |
| `confidence` | string | Confidence in the characterization of positions |
| `scholarly_disagreement` | string\|null | Meta-note if there is disagreement about how to characterize the debate itself |
| `created_date` | string | ISO date |
| `last_modified` | string | ISO date |

## `scholarly_positions` Array Structure

Each element:
```json
{
  "scholar_slug": "surname-firstname-bYYYY",
  "scholar_name": "Full Name",
  "position_label": "CONSENSUS | DISSENT | SYNTHESIS | PRECURSOR | CRITIC",
  "stance": "One or two sentences describing what this scholar argues",
  "key_work": "Title (year)",
  "key_argument": "The core claim in this scholar's own terms"
}
```

`position_label` controlled vocabulary:
- `CONSENSUS` — this scholar's position represents or closely tracks current scholarly consensus
- `DISSENT` — this scholar dissents from consensus
- `SYNTHESIS` — this scholar attempts to reconcile opposing positions
- `PRECURSOR` — earlier work that set the terms of the debate
- `CRITIC` — this scholar critiques the framing of the debate itself

## `consensus_status` Controlled Vocabulary

- `SETTLED` — strong scholarly consensus exists; the old position is no longer viable
- `EMERGING_CONSENSUS` — majority view is clear but significant dissent persists
- `CONTESTED` — no consensus; active disagreement
- `OPEN` — the question has not been adequately addressed

## Writing Principles

**State consensus honestly.** Where a scholarly consensus exists, say so directly with named scholars. Where the old position is no longer viable (e.g., that witch prosecution was straightforward religious superstition), say so. Avoid false balance — not all historiographical positions are equally well-supported.

**Name scholars.** Every claim about what "scholars think" must be attributable to at least one named historian with a key work. No anonymous scholarly positions.

**Separate the empirical from the interpretive.** Some debates are about what happened (empirical); others are about what it means (interpretive). Label this distinction in `database_relevance`.

**`database_relevance` is mandatory.** This field tells a reader how to use the database differently given this debate — which fields to read skeptically, which entity types are most affected, what confidence levels apply.
