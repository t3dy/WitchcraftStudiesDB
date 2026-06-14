# WitchcraftStudiesDB — Data Ontology

This document defines the complete entity-relationship model for the database, including field semantics, inter-entity relationships, and decision rules for which entity type to use.

---

## Entity Type Overview

| Entity Type | Description | Current Count | ID Pattern |
|------------|-------------|---------------|-----------|
| `trial_event` | A prosecution episode (single trial or coordinated hunt) | 37 | `trial-location-year` |
| `accused_person` | An individual prosecuted or accused | 45 | `name-location-year` |
| `healer_practitioner` | A magical practitioner (cunning folk, healer) | 33 | `name-location-tradition` |
| `demonological_scholar` | A scholar or historical figure who contributed to the field | 60 | `surname-firstname-bYYYY` |
| `scholarly_text` | A book, article collection, or primary source with its own entry | 58+ | `surname-title-word-year` |
| `demonological_concept` | An analytical or actor-term concept | 53 | `concept-name` |
| `location` | A geographic place with witchcraft significance | 41 | `location-name` |
| `inquisitorial_body` | An institutional court or investigating authority | 40 | `institution-name` |
| `persecuted_group` | A modern analytical category of socially vulnerable victims | 35 | `group-descriptor-scope` |
| `timeline` | A dated historical event or publication | 68 | `event-descriptor-year` |
| `primary_source` | An archival document, letter, pamphlet, or trial record | 10 | `slug-name-location-year` |
| `historiographical_debate` | A named scholarly controversy | 8 | `debate-keyword` |

---

## Entity Relationship Graph

```
trial_event ←──────────── accused_person (trial_id FK)
     │                         │
     │                    healer_practitioner (trial_id FK)
     │
     ├──── location (location_id FK)
     │
     ├──── demonological_concept[] (related_demonological_concepts[])
     │
     ├──── inquisitorial_body (via key_trial_events[])
     │
     └──── primary_source (linked_trial_events[])

demonological_scholar ──── scholarly_text (author_slug FK)
         │                        │
         │                        ├──── historiographical_debate (linked_scholarly_texts[])
         │                        │
         └──────────────── demonological_concept (scholarly_sources[])

historiographical_debate ──── demonological_scholar (scholarly_positions[].scholar_slug)
                         ──── demonological_concept (linked_concepts[])

primary_source ──── trial_event (linked_trial_events[])
               ──── accused_person (linked_accused_persons[])
               ──── scholarly_text (linked_scholarly_texts[])
```

---

## Entity Type Definitions and Field Semantics

### `trial_event`

**Purpose**: A temporally bounded prosecution episode — may be a single trial or an extended mass hunt. NOT individual executions (those are accused_person entries).

**Required fields**:
- `id`: Slug following `trial-location-year` or `location-witch-hunt-yearstart`
- `name`: Human-readable display name
- `location_id`: Slug of a `location` entry
- `date_range`: Free text (e.g., "1626–1631")
- `year_start` / `year_end`: Integers (year_end may be null for open-ended)
- `approximate_executions`: Integer or null (not a false precision)
- `approximate_accused`: Integer or null
- `jurisdiction`: Institutional description
- `legal_framework`: Legal system operative
- `overview`: 150–300 words
- `historiographical_analysis`: Object with clark/hutton/ginzburg subfields
- `accusation_patterns`: Object
- `key_accused_persons`: Array of accused_person slugs
- `related_demonological_concepts`: Array of concept slugs
- `scholarly_sources`: Array of scholarly_text slugs
- Standard provenance fields

**Scope rules**:
- A single assizes or court session → one entry
- A decades-long hunt in one jurisdiction → one entry (with date_range)
- A coordinated multi-jurisdictional panic → may need multiple entries with cross-reference
- Individual biographical information → goes in `accused_person`, not here

---

### `accused_person`

**Purpose**: An individual human being who was accused of witchcraft, prosecuted, or executed. For collective groups, use `persecuted_group` instead.

**Required fields**:
- `id`: `name-location-year` pattern (use most distinctive element; year = year accused)
- `name`: Contemporary name form (not Anglicized unless consistently used)
- `status`: One of: Executed | Pressed to death | Abjured | Acquitted | Imprisoned | Fled
- `trial_id`: Slug of linked `trial_event` (may be a forward reference)
- `location_id`: Slug of linked `location`
- `year_accused`: Integer
- `gender`: `"male"` | `"female"` | `"unknown"`
- `social_status`: Free text
- All narrative fields governed by WRITING_STYLE_GUIDE.md
- Standard provenance fields

**Confidence → writing register**: See `accused_person/WRITING_STYLE_GUIDE.md`. This is mandatory reading before writing narrative fields.

**Scope rules**:
- Real, historically documented individuals only
- LOW confidence: named in one source only (common for torture-cascade names)
- Do not create entries for anonymous collective groups — use `persecuted_group`

---

### `healer_practitioner`

**Purpose**: An individual who practiced folk magic, healing, or divination — the "cunning folk" type. May have been accused of witchcraft but their primary role is as a practitioner, not an accused.

**Key distinction from `accused_person`**:
- `accused_person`: Their historical significance is primarily that they were accused / prosecuted
- `healer_practitioner`: Their historical significance is primarily their practice / self-identification

A single individual may appear in BOTH entity types if they were both a documented practitioner AND a documented accused person. Cross-link them.

**Required fields**:
- `self_identification`: What the practitioner called themselves or their practice
- `claimed_abilities`: Array of what they claimed to do
- `practical_activities`: What they actually demonstrably did
- `actor_vs_analyst_terminology`: Object distinguishing their terms from modern analysis

---

### `demonological_scholar`

**Purpose**: Any scholar, theologian, lawyer, judge, or intellectual who contributed significantly to the history of witch prosecution or its historiography. Covers BOTH historical figures (Nider, Bodin, Weyer) AND modern historians (Ginzburg, Hutton, Clark).

**Two sub-types with different field emphasis**:

#### Historical Demonologists (pre-1800)
Emphasis on: `academic_discipline`, `major_works`, `intellectual_context`, `contribution_to_demonological_theory`, `relation_to_prosecution`

#### Modern Historians (post-1800)
Emphasis on: `methodological_approach`, `core_argument`, `scholarly_relationships`, `key_contributions`, `reception_and_critique`

**See `demonological_scholar/CLAUDE.md` for full writing guidance.**

---

### `scholarly_text`

**Purpose**: A book, article collection, or primary source that is cited in `scholarly_sources` arrays elsewhere in the database AND is significant enough to merit its own entry.

**Scope rules**:
- Must be cited in at least one other entity's `scholarly_sources`
- Journal articles are generally NOT entered individually (only if uniquely foundational, like Trevor-Roper's "European Witch-Craze")
- Edited volumes get one entry as a whole; individual chapters do not get separate entries unless uniquely critical
- Primary sources (Malleus, Daemonologie) belong here if they are primarily used as secondary-scholarly sources; archival documents belong in `primary_source`

**ID naming**: `[first-author-surname]-[key-title-word]-[year-of-edition-cited]`

---

### `demonological_concept`

**Purpose**: An analytical category or period-specific term that the database uses to organize intellectual content. NOT a synonym for "topic" — each concept entry should represent something that demonologists or scholars treated as a distinct category.

**`category_type` values**:
- `ACTOR_TERM`: A term contemporaries used themselves (e.g., "maleficium," "familiar spirit")
- `ANALYST_TERM`: A modern scholarly category applied retrospectively (e.g., "cumulative concept," "charity-refusal mechanism")
- `HYBRID`: A term used by both contemporaries and scholars but meaning different things to each (e.g., "witch," "sabbath")

**When to create a new concept vs. use an existing one**:
- If the concept appears in three or more different entity types' analysis → create it
- If it's a sub-variant of an existing concept (e.g., "storm-raising" vs. "weather-magic") → add to existing
- If it's primarily a biographical fact about one person → don't create a concept

---

### `location`

**Purpose**: A geographic place that appears in multiple trial events, has significant witchcraft-historical significance, or provides regional context for prosecution patterns.

**Scope rules**:
- Cities and regions that are trial sites → YES
- Countries as broad regional entries → YES (e.g., `scotland`, `germany`)
- Villages with only one minor incident → NO (mention in the trial_event entry instead)

**Required fields**: `name`, `modern_country`, `latitude`, `longitude`, `location_type`, `hover_description` (1-2 sentences for map tooltip), `panel_description` (full analysis, 200–500 words)

Note: `latitude` and `longitude` are **top-level fields**, NOT nested in a `coordinates` object.

---

### `inquisitorial_body`

**Purpose**: An institutional court or investigating authority — NOT the same as a trial event. Represents the permanent or semi-permanent institutional structure that conducted trials over time.

**Key distinction**: The Roman Inquisition is one `inquisitorial_body`; individual trials it conducted are separate `trial_event` entries.

**Critical note from CLAUDE.md**: The Roman and Spanish Inquisitions were **restraining forces** on witch prosecution, not drivers of it. Entries must not perpetuate the popular myth that they drove persecution.

---

### `persecuted_group`

**Purpose**: A modern analytical category grouping people who shared structural vulnerability to witch accusation — demographic, occupational, or social.

**These are analyst categories, not self-identifications**. Contemporaries did not think of "elderly widows" as a persecuted group; modern scholars do.

**Scope rules**:
- Group must appear in multiple trial events across multiple regions OR be the subject of significant scholarly analysis
- Do not create entries for groups smaller than "a meaningful historical pattern"

---

### `timeline`

**Purpose**: A single dated event (publication, trial start, institutional act, political event) that provides chronological structure.

**Scope rules**:
- Every major text publication → one timeline entry
- Every major trial event → one timeline entry (complementing the `trial_event` entry)
- Institutional acts (papal bulls, witchcraft statutes) → one entry each
- Deaths and births of major scholars → YES for highly significant figures

---

### `primary_source`

**Purpose**: An archival document, letter, interrogation transcript, pamphlet, or commission report produced AT THE TIME OF EVENTS. NOT modern scholarly analysis.

**Key distinction from `scholarly_text`**:
- `scholarly_text`: Published demonological treatise or modern monograph (used as scholarly authority)
- `primary_source`: Archival document, letter, court record, pamphlet — produced in or near the events

**See `primary_source/CLAUDE.md` for full schema and writing guidance.**

---

### `historiographical_debate`

**Purpose**: A named scholarly controversy with documented positions from multiple named historians, a stated consensus status, and direct relevance to how database entries should be interpreted.

**See `historiographical_debate/CLAUDE.md` for full schema.**

---

## Cross-Reference Rules

### Mandatory cross-links (must be updated when adding an entry)

| When you add... | You must update... |
|----------------|-------------------|
| `accused_person` | The `accused_persons[]` array in the linked `trial_event` |
| `trial_event` | The `key_trial_events[]` array in the linked `location` |
| `scholarly_text` | The `scholarly_sources[]` arrays in any entity that cites this work |
| `demonological_scholar` | The `scholarly_sources[]` arrays in any concept that lists this scholar |
| `healer_practitioner` | The linked `trial_event.key_accused_persons[]` if applicable |

### Slug resolution

All cross-references use ID slugs from the target entity's `id` field. Never use display names as cross-references. Before adding a slug to a cross-reference array, verify the target entry exists.

**Forward references**: Allowed for `trial_id` in `accused_person` entries (trial entry may not exist yet). Validation will flag these until the target is created.

---

## Decision Tree: Which Entity Type?

```
Is this a person?
  ├── YES: Were they primarily accused / prosecuted?
  │         ├── YES: accused_person
  │         └── NO: Did they primarily practice folk magic / healing?
  │                   ├── YES: healer_practitioner
  │                   └── NO: Did they contribute to scholarship / demonology?
  │                             └── YES: demonological_scholar
  └── NO: Is this a place?
           ├── YES: location
           └── NO: Is this an institution?
                    ├── YES: inquisitorial_body
                    └── NO: Is this a trial / prosecution episode?
                             ├── YES: trial_event
                             └── NO: Is this a concept or analytical category?
                                      ├── YES: demonological_concept
                                      └── NO: Is this a document/text?
                                               ├── YES archival/contemporary: primary_source
                                               ├── YES scholarly/published: scholarly_text
                                               ├── YES dated event: timeline
                                               ├── YES scholarly controversy: historiographical_debate
                                               └── YES demographic pattern: persecuted_group
```

---

## Confidence Level Semantics (all entity types)

| Level | Meaning | Prose register |
|-------|---------|---------------|
| `HIGH` | Archival primary source or secure scholarly consensus (multiple independent sources) | Indicative mood; state dates and names directly |
| `MEDIUM` | Scholarly reconstruction; inference required; scholars disagree on interpretation | Name scholars as interpretive authorities; hedge only inferred elements |
| `LOW` | Named in one source only; no independent corroboration | Open with what the single source says; conditional constructions throughout |

---

## Naming Conventions

| Thing | Convention | Example |
|-------|-----------|---------|
| File names | `lowercase-with-hyphens.json` | `johannes-junius-letter-bamberg-1628.json` |
| JSON keys | `lowercase_with_underscores` | `"year_composed": 1628` |
| ID slugs | `lowercase-with-hyphens` | `"id": "bamberg-interrogation-records-1626-1631"` |
| Missing values | `null` (never `""`) | `"year_end": null` |
| Cross-reference arrays | Slug arrays | `"scholarly_sources": ["clark-thinking-with-demons-2001"]` |

---

## Immutability Rule

**Once a field appears in ANY entry of an entity type, it must appear in ALL entries of that type.** Use `null` for entries that don't have that data. Never omit a field that exists in the schema.

Before adding a new field to any entry, check all existing entries of that type. If the field is genuinely needed, add it to ALL entries simultaneously.

---

## Validation

```bash
# Validate all entity types
python scripts/validate_entities.py --all --report json

# Check cross-links for specific types
python scripts/validate_entities.py trial_event --check-links
python scripts/validate_entities.py accused_person --check-links

# CSV export for gap analysis
python scripts/validate_entities.py --report csv
```

Run validation after adding any new entries. Cross-link validation errors are expected for forward references; all others should be resolved before committing.
