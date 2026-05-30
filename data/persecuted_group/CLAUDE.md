# Persecuted Group Entries — Working Instructions

Entries in this type document social categories disproportionately targeted in witch prosecutions. These are analytical categories, not self-identifications: the `persecution_rationale` field records how contemporaries theorized the targeting; the `structural_vulnerability` and `historiographical_significance` fields record modern scholarly analysis of why it occurred.

## Schema Summary

Core fields:
```
id, name, category, temporal_scope, primary_regions
```

Narrative fields:
```
group_profile           (200–400 words)
persecution_rationale   (100–200 words)
structural_vulnerability (100–200 words)
historiographical_significance (150–300 words)
```

Cross-reference fields:
```
exemplary_accused_persons   — slug array → accused_person entries
related_demonological_concepts — slug array → demonological_concept entries
```

Provenance fields:
```
source_method, review_status, confidence, scholarly_sources,
scholarly_disagreement (where applicable)
```

## `category` Controlled Vocabulary

| Value | Use for |
|-------|---------|
| `demographic` | Age, marital status, sex — widows, elderly women |
| `occupational` | Professional roles — midwives, cunning folk, healers |
| `social_class` | Economic position — the destitute, property-owning women |
| `religious_minority` | Religious or ethnic minorities — Jews, Waldensians |

## Writing Standards

Apply the same confidence-level register used for `accused_person` entries:

- **group_profile**: Opens with the defining characteristics of the group in early modern social terms, not modern categories. Name the specific scholars whose demographic or sociological work establishes the pattern as documented (not just asserted). Acknowledge regional variation — no monolithic "witch hunt."
- **persecution_rationale**: This is the ACTOR-LEVEL account — what contemporaries believed. Use actor/analyst framing: "Demonological theory held that…" not "Witches were believed to…"
- **structural_vulnerability**: This is the ANALYST-LEVEL account — why the modern historiography explains the targeting. Named scholars with named arguments.
- **historiographical_significance**: Follow the four-part structure from the accused_person style guide: specific debate → named scholars and their arguments → how this group case extends or complicates the pattern → broader significance.

## ID Naming Pattern

`[group-descriptor]-[scope]`

Examples:
- `widows-early-modern`
- `cunning-folk-wise-women`
- `midwives-obstetric-healers`
- `socially-marginal-destitute`

## Prohibited Patterns

- Do not write "women were persecuted because of misogyny" as an unattributed claim. State Karlsen's argument, or Hutton's argument, with the specific claim each makes.
- Do not collapse regional variation into a single pattern. Note where a group was especially targeted and where it was not.
- Do not assert statistical proportions without citing the source (Hutton's demographic analysis, Levack's quantitative work, etc.).
