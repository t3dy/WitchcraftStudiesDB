# primary_source — Working Instructions

## What Belongs Here

Archival and documentary material produced **at the time of events**: trial records, interrogation transcripts, confessions, letters, pamphlets, commission reports, chronicles, and indictments. **Not** modern scholarly analysis — that goes in `scholarly_text/`.

The boundary rule: if a demonological treatise (Malleus, Rémy's *Daemonolatreiae*, Binsfeld, Guazzo) already exists in `scholarly_text/`, do not duplicate it here. Primary sources in this directory are documents that were not primarily published as demonological argument — they are records, letters, reports, and pamphlets that preserve what actually happened in or around a trial.

## ID Pattern

`slug-name-location-year` — e.g., `johannes-junius-letter-bamberg-1628`, `benandanti-inquisition-transcripts-1575-1580`, `errores-gazariorum-1437`.

## Required Fields (Immutable Schema)

Every entry **must** have all of these:

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | Slug ID |
| `name` | string | Display name |
| `document_type` | string | See controlled vocabulary below |
| `author` | string | Contemporary author or `"Anonymous"` |
| `author_slug` | string\|null | Slug of linked `demonological_scholar` entry if exists |
| `year_composed` | integer\|null | Year written |
| `year_published` | integer\|null | Year first printed/published (null if manuscript only) |
| `original_language` | string | Latin, German, French, English, Swedish, Polish, etc. |
| `repository` | string | Archive holding original, or best published edition |
| `scholarly_edition` | string\|null | Most authoritative modern edition |
| `translation_available` | boolean | English translation exists |
| `jurisdiction_id` | string\|null | Slug of linked `inquisitorial_body` |
| `location_id` | string\|null | Slug of linked `location` |
| `content_summary` | string | What the document actually contains (not its historical significance) |
| `key_passages` | array | `[{"passage": "...", "significance": "..."}]` — direct quotes or paraphrases |
| `scholarly_significance` | string | Why historians use this document |
| `linked_trial_events` | array | Slugs of relevant `trial_event` entries |
| `linked_accused_persons` | array | Slugs of relevant `accused_person` entries |
| `linked_scholarly_texts` | array | Slugs of `scholarly_text` entries that analyze or edit this document |
| `clark_intellectual_analysis` | string\|null | What this document reveals about demonological ideas |
| `hutton_social_analysis` | string\|null | Social history reading of this document |
| `ginzburg_interrogation_analysis` | string\|null | What interrogation analysis reveals about this document |
| `source_method` | string | How we know about this document |
| `review_status` | string | `DRAFT` / `REVIEWED` / `VERIFIED` |
| `confidence` | string | `HIGH` / `MEDIUM` / `LOW` |
| `scholarly_disagreement` | string\|null | Named historians on each side of any contested interpretation |
| `created_date` | string | ISO date |
| `last_modified` | string | ISO date |

## Controlled Vocabulary: `document_type`

- `trial_record` — formal legal proceedings record
- `interrogation_transcript` — verbatim or paraphrased record of questioning
- `confession` — formal confession statement
- `letter` — personal correspondence
- `pamphlet` — printed popular account
- `commission_report` — official government investigation report
- `chronicle` — contemporary narrative history
- `inquisition_manual` — procedural guide (distinguish from demonological treatise)
- `indictment` — formal legal charge
- `deposition` — sworn witness testimony
- `collection` — archival collection spanning multiple document types

## Historiographical Principles Applied Here

**Ginzburg's interrogation analysis is essential.** Every primary source entry must engage with the question: what elements of this document reflect the interrogator's preconceptions vs. what the accused actually said? Use the `ginzburg_interrogation_analysis` field to address this explicitly.

**Actor/analyst distinction.** When quoting or paraphrasing the document, preserve the contemporary terminology in quotation marks. In the `scholarly_significance` and analysis fields, use modern analytical categories and mark them as such.

**Torture awareness.** For any confession document: note whether torture was used (it almost certainly was in Continental cases after 1250), and address how this shapes the evidentiary status of the content.

## Writing the `content_summary`

Write what the document physically contains — its structure, the questions asked or not asked, the specific claims made. Do not editorialize about significance in this field. Save scholarly interpretation for the analysis fields.

## Confidence Levels

- **HIGH**: Document held in a named archive or published in a named scholarly edition; contents confirmed by at least two secondary sources
- **MEDIUM**: Document referenced in scholarship but not independently verified; contents reconstructed from secondary accounts
- **LOW**: Document existence inferred; no direct access; contents unknown or very fragmentary
