# Inquisitorial Body Entries — Working Instructions

Entries in this type document the institutional bodies that prosecuted witchcraft — Church inquisitions, episcopal courts, and civil tribunals. The term "inquisitorial" is used broadly: many major prosecutions (Bamberg, Salem, North Berwick) were conducted by secular or episcopal courts using inquisitorial procedure, not by the Papal/Roman Inquisition proper. The `institutional_type` field carries the distinction.

**Important counterintuitive fact**: The Roman Inquisition and Spanish Inquisition were generally RESTRAINING forces on witch prosecution, not drivers of it. Mass executions occurred primarily in secular and episcopal courts outside effective Roman oversight. Entries must not perpetuate the popular misconception that "the Inquisition" drove witch hunts.

## Schema Summary

Core fields:
```
id, name, formal_name, institutional_type, founded, dissolved,
witch_trial_involvement_level
```

Structured fields:
```
jurisdiction_description    (1–2 paragraphs)
jurisdiction_territories    (slug array → location entries)
procedural_features         (object: see below)
```

Narrative fields:
```
role_in_witch_trials         (100–200 words)
historiographical_significance (150–300 words)
```

Cross-reference fields:
```
key_trial_events   — slug array → trial_event entries
```

Provenance fields:
```
source_method, review_status, confidence, scholarly_sources,
scholarly_disagreement (where applicable)
```

## `institutional_type` Controlled Vocabulary

| Value | Examples |
|-------|---------|
| `ecclesiastical_inquisition` | Roman Holy Office, Venetian Inquisition |
| `royal_inquisition` | Spanish Inquisition, Portuguese Inquisition |
| `episcopal_secular_court` | Bamberg (Prince-Bishop's criminal court) |
| `secular_tribunal` | Salem Court of Oyer and Terminer, Scottish Privy Council |
| `medieval_papal_inquisition` | Pre-1542 itinerant papal inquisitors |

## `witch_trial_involvement_level` Controlled Vocabulary

| Value | Meaning |
|-------|---------|
| `high` | Central institutional actor in documented mass prosecution |
| `moderate` | Prosecuted cases with notable restraint or limited scale |
| `low` | Rare prosecutions; skeptical orientation; primarily restraining |
| `peripheral` | Jurisdictional overlap but not primary prosecution mechanism |

## `procedural_features` Sub-fields

```json
{
  "torture_policy": "When and how torture was authorized; procedural constraints",
  "evidence_standards": "What counted as sufficient evidence for conviction",
  "confession_policy": "How confessions were obtained, validated, and could be recanted",
  "appeal_mechanism": "Whether and how defendants could appeal; oversight structure"
}
```

## Writing Standards

- **jurisdiction_description**: Be precise about territorial scope. For ecclesiastical inquisitions, note the relationship between central oversight (Rome, Madrid) and regional tribunals.
- **role_in_witch_trials**: State the specific relationship — was this institution a driver, a moderator, or incidental to witch prosecution? This is where counterintuitive findings (Spanish Inquisition's protectiveness) must be stated clearly.
- **historiographical_significance**: Name the specific scholars and their arguments about this institution's role. Distinguish between popular mythology about institutions and scholarly findings.

## ID Naming Pattern

`[institution-name]` or `[institution-location-type]`

Examples:
- `roman-inquisition`
- `spanish-inquisition`
- `venetian-inquisition`
- `bamberg-episcopal-court`
- `court-of-oyer-and-terminer-salem`
