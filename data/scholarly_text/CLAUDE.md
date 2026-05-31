# Scholarly Text Entries — Working Instructions

This entity type covers academic works (monographs, edited volumes, article collections) and primary sources (trial records, demonological treatises) that are cited in the database's `scholarly_sources` fields. An entry here means the work is significant enough to merit its own entry and is cross-referenced by at least one entity elsewhere in the database.

## Schema Summary

Core fields:
```
id, title, author, year_published, original_year (if translation/reprint),
publisher, text_type
```

Narrative fields:
```
subject_focus          (1 sentence)
summary                (100–200 words)
scholarly_significance (150–300 words)
key_arguments          (array: concept + claim)
relation_to_database   (how this work is used in existing entries)
```

Provenance fields:
```
source_method, review_status, confidence, scholarly_disagreement
```

## `text_type` Controlled Vocabulary

| Value | Examples |
|-------|---------|
| `monograph` | Ginzburg's Night Battles, Clark's Thinking with Demons |
| `edited_volume` | Ankarloo/Clark series |
| `article_collection` | Essays assembled under one volume |
| `primary_source` | Malleus Maleficarum, Daemonologie, court records |
| `primary_source_edition` | Modern critical edition of a primary source (e.g., Salem Witchcraft Papers) |

## ID Naming Pattern

`[first-author-surname]-[key-title-word(s)]-[year-of-edition-referenced]`

The year in the ID corresponds to the edition most commonly cited in this database, which may differ from the first edition year. If the work is a translation, the English translation year is used (because most citations in English-language scholarship use the translation).

Examples:
- `clark-thinking-with-demons-2001` — Clark (1997), OUP paperback 2001
- `ginzburg-night-battles-1983` — Ginzburg (Italian 1966, English 1983)
- `ankarloo-clark-vol4-witch-trials-2001` — vol. 4 of the series

## Writing Standards

- **summary**: What the work argues, not just what it covers. State the central thesis in 2-3 sentences, then give methodological and evidentiary scope.
- **scholarly_significance**: Place the work in the historiographical landscape. Name the debates it opened or settled; note its reception by the three anchor scholars (Clark/Hutton/Ginzburg) where relevant. State specifically what the database's entries draw from it.
- **scholarly_disagreement**: For well-established works, name specific critiques and critics. Do not write "scholars have debated" — name them.
- **key_arguments**: Each entry should have 3-5 specific claims from the text that are drawn on in the database. Keep each claim to 1-2 sentences.

## Connection to Database Entries

The `scholarly_sources` array in every entity uses IDs from this type. When a new scholarly text is created:
1. Verify the ID matches exactly what's already used in `scholarly_sources` arrays across the database
2. Update `data/CLAUDE.md` entry count
