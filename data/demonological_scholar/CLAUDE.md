# Demonological Scholar Entries — Working Instructions

This entity type covers both **historical figures** (demonologists, theologians, judges, sceptics active before 1800) and **modern historians** (scholars whose work shapes the field's analytical framework). Both sub-types share the same JSON schema but with different field emphases.

**Read `WRITING_STYLE_GUIDE.md` (in `accused_person/`) before writing narrative fields** — the attribution standards, confidence registers, and actor/analyst discipline apply to ALL entry types.

---

## ID Pattern

`surname-firstname-bYYYY` — birth year, four digits. If birth year is uncertain but approximate: `b1380` (use best estimate). If birth year is unknown: use the decade of peak activity: `fl1420`.

Examples:
- `ginzburg-carlo-b1939`
- `nider-johannes-b1380`
- `weyer-johann-b1516`
- `kramer-heinrich-b1430`

For scholars known only by one name or title (medieval): use the most distinctive name form: `bernardino-of-siena-b1380`, `peter-of-berne-fl1430`.

---

## Schema

Every entry must have all of these fields (use `null` for unavailable data, never omit):

```json
{
  "id": "surname-firstname-bYYYY",
  "name": "Full Display Name",
  "birth_year": 1939,
  "death_year": null,
  "birth_place": "City, Country",
  "academic_discipline": "Microhistory / Social History / Theology / Law / Medicine",
  "primary_institution": "University or institution name",
  "major_works": [
    {
      "title": "Full Title",
      "year": 1983,
      "publisher": "Publisher name",
      "significance": "One sentence on why this work matters"
    }
  ],
  "historiographical_position": "SCEPTIC | ADVOCATE | SYSTEMATIZER | PROCEDURAL | MICROHISTORIAN | SOCIAL_HISTORIAN | INTELLECTUAL_HISTORIAN | COMPARATIVE",
  "core_argument": "2-3 sentences stating the central intellectual contribution",
  "methodological_approach": {
    "primary_method": "Archival microhistory / Quantitative social history / Intellectual history / etc.",
    "source_types": "What kinds of sources they work with",
    "interpretive_framework": "The analytical lens they apply"
  },
  "key_contributions": [
    {
      "concept": "Name of contribution",
      "description": "2-3 sentences on what they contributed and why it matters"
    }
  ],
  "scholarly_relationships": {
    "alignment_with": ["scholar-slug-1", "scholar-slug-2"],
    "creative_tension_with": ["scholar-slug-1"]
  },
  "database_engagement": "How this scholar's work is used in the database entries (1-2 paragraphs)",
  "historiographical_significance": "200-400 word assessment of their place in the field",
  "scholarly_disagreement": "Named scholars on each side of contested interpretations of this figure's work",
  "scholarly_sources": ["slug-1", "slug-2"],
  "source_method": "Specific source: published biography, DNB, ODNB, scholar's own prefaces, etc.",
  "review_status": "DRAFT | REVIEWED | VERIFIED",
  "confidence": "HIGH | MEDIUM | LOW",
  "created_date": "2026-06-03",
  "last_modified": "2026-06-03"
}
```

---

## Two Sub-Types: Historical vs. Modern

### Historical Demonologists / Figures (pre-1800)

These are contemporaries of the witch trials: theologians, inquisitors, judges, critics, physicians, preachers.

**Field emphasis**:
- `academic_discipline`: Use the early modern field (Theology, Canon Law, Civil Law, Medicine, Natural Philosophy)
- `major_works`: List their actual writings, not works ABOUT them
- `historiographical_position`: How they positioned themselves toward witch prosecution (ADVOCATE = supported prosecution; SCEPTIC = questioned it; SYSTEMATIZER = organized the demonological framework; PROCEDURAL = concerned with procedural reform)
- `methodological_approach.interpretive_framework`: Their theological or philosophical framework (scholastic demonology, empirical medicine, Calvinist theology, etc.)
- `key_contributions`: Specific arguments or doctrines they introduced or systematized
- `database_engagement`: How this figure appears in the database — in `scholarly_sources` arrays of concept and trial entries, or as the subject of historiographical analysis

**What NOT to do for historical figures**:
- Do not use `scholarly_relationships` to link them to modern historians as if they were contemporaries
- Do not impose modern methodological categories on their intellectual framework
- Do not list works BY modern historians about them as their `major_works` — those go in `scholarly_sources`

**Example entry structure (Nider)**:
```
major_works: Formicarius (c.1437), Praeceptorium divinae legis (1431)
historiographical_position: SYSTEMATIZER
key_contributions: [
  "First comprehensive academic treatment of the new composite witch stereotype",
  "Key figure in transmission of Alpine trial material into learned demonological tradition",
  "Formicarius Book V as founding document for the cumulative concept"
]
scholarly_sources: [
  "clark-thinking-with-demons-2001",  -- Clark analyzes Nider extensively
  "cohn-europes-inner-demons-1975",   -- Cohn uses Nider as evidence
  "kieckhefer-magic-middle-ages-1989" -- Kieckhefer on Nider's sources
]
```

---

### Modern Historians (post-1800)

Scholars who have contributed to the historiography of witch prosecution: social historians, microhistorians, intellectual historians, feminist scholars, legal historians.

**Field emphasis**:
- `academic_discipline`: The academic field (History, Anthropology, Religious Studies, Gender Studies, etc.)
- `methodological_approach`: Their analytical method and interpretive stance
- `key_contributions`: Specific methodological or interpretive innovations they introduced to the field
- `scholarly_relationships`: How their work relates to other modern historians
- `database_engagement`: Which specific fields in the database their work is used in, and HOW

**The three primary framework scholars (Clark/Hutton/Ginzburg)** have longer, more detailed entries that serve as the database's analytical anchors. All other modern historian entries should explicitly position themselves relative to these three.

**Positioning relative to the three frameworks**:

In `core_argument`, explicitly note:
- Whether this scholar aligns with, challenges, or synthesizes the Clark/Hutton/Ginzburg approaches
- Which of the three frameworks they most extend or critique

In `scholarly_relationships`, use the slugs of scholars whose positions theirs engages:
```json
"alignment_with": ["hutton-ronald-b1953", "briggs-robin-b1942"],
"creative_tension_with": ["barstow-anne-b1940", "cohn-norman-b1915"]
```

---

## `historiographical_position` Controlled Vocabulary

| Value | Meaning | Examples |
|-------|---------|---------|
| `SCEPTIC` | Historically or contemporarily questioned the reality/extent of witch prosecution | Weyer, Scot, Spee, Bekker |
| `ADVOCATE` | Supported the reality of witchcraft and the necessity of prosecution | Bodin, Kramer, Binsfeld, De Lancre |
| `SYSTEMATIZER` | Organized demonological theory into systematic form | Nider, Del Rio, Guazzo |
| `PROCEDURAL` | Concerned primarily with procedural reform rather than the theological question | Thomasius, Spee (also SCEPTIC) |
| `MICROHISTORIAN` | Uses individual cases to illuminate broad patterns (Ginzburg's method) | Ginzburg, Briggs |
| `SOCIAL_HISTORIAN` | Quantitative and sociological approach to trial demographics | Hutton, Macfarlane, Levack |
| `INTELLECTUAL_HISTORIAN` | Studies the history of ideas in demonological thought | Clark, Kieckhefer |
| `COMPARATIVE` | Cross-regional or cross-cultural comparative approach | Ankarloo, Behringer, Monter |
| `FEMINIST` | Foregrounds gender as the primary analytical variable | Barstow, Karlsen, Purkiss |
| `ANTHROPOLOGICAL` | Uses ethnographic or anthropological methods | Evans-Pritchard's influence, Briggs |
| `LEGAL` | Emphasizes legal procedure and institutional framework | Levack, Peters |

---

## `core_argument` Writing Standard

This is the most important narrative field. It must:

1. State the scholar's central intellectual claim in 2-3 sentences (not a description of their topic)
2. Name the methodological innovation or interpretive lens they introduced
3. Distinguish their position from the baseline before they wrote

**Good examples**:
- Clark: "Demonological ideas were not symptoms of superstition or pathology but intellectually coherent arguments within their own framework — specifically, a sophisticated application of scholastic natural philosophy to the question of demonic agency. Clark's *Thinking with Demons* (1997) demonstrates that early modern demonologists thought carefully and seriously about magic, and that their conclusions flowed from premises shared by educated contemporaries across religious divides."
- Ginzburg: "Beneath the inquisitorially imposed diabolical framework of confessions, careful reading can recover traces of genuine pre-existing folk beliefs — specifically, a Eurasian shamanistic tradition of ecstatic nocturnal journeys for fertility and protection. The benandanti of Friuli provide the paradigm case: practitioners who insisted, across multiple tortured sessions, that their nocturnal battles were good and Christian, not diabolical."

**Poor examples** (too descriptive, not argumentative):
- "Clark wrote about demonological ideas in early modern Europe and showed how they were part of intellectual culture." [describes, doesn't argue]
- "Ginzburg is a microhistorian who studies witch trials in Italy." [biographical, not intellectual]

---

## `key_contributions` Writing Standard

Each contribution entry must name a **specific** intellectual innovation, not a general theme:

**Good**:
```json
{
  "concept": "Interrogation analysis as historical method",
  "description": "Ginzburg developed a method for identifying pre-inquisitorial folk beliefs beneath tortured confessions by looking for elements that do not fit the inquisitorial template — details the interrogator would not have supplied, descriptions with positive emotional valence, geographically specific content. This method, first deployed in the benandanti case, has become a standard tool in the field."
}
```

**Poor**:
```json
{
  "concept": "Microhistory",
  "description": "Ginzburg used microhistory to study witchcraft, looking at small cases in detail."
}
```

---

## `database_engagement` Writing Standard

This field connects the scholar to specific parts of the database. It should:

1. Name specific entity types where their work is used
2. Explain HOW (not just that) their work is used there
3. Note any tensions or complications in applying their framework

**Template**:
"[Scholar]'s [work] is used in [specific ways] in [specific entity types]. The [concept/argument] appears in [specific field names] of [entry types]. A tension arises in applying [their framework] to [specific entries] because [reason]."

---

## `historiographical_significance` Writing Standard

This is the encyclopedia-facing field. Structure:

1. **Their contribution** (2 sentences): What they added to the field that wasn't there before
2. **Their reception** (2-3 sentences): How the field responded — who endorsed, who challenged, how the debate evolved
3. **Their current status** (1-2 sentences): Where their work stands today, what has been superseded vs. what endures
4. **Their relation to the three frameworks** (1-2 sentences): How they fit in the Clark/Hutton/Ginzburg analytical structure

Total: 150-400 words.

---

## Checklist Before Finalizing

- [ ] `id` follows `surname-firstname-bYYYY` pattern
- [ ] `core_argument` states a specific intellectual claim, not a topic description
- [ ] `major_works` contains the works they WROTE, not works about them
- [ ] `scholarly_sources` lists works ABOUT this scholar or that they are discussed in
- [ ] `key_contributions` are specific innovations, not general themes
- [ ] `database_engagement` names specific entity types and field names
- [ ] `historiographical_position` is one of the controlled vocabulary values
- [ ] For historical figures: no modern methodological anachronism in the framing
- [ ] For modern historians: explicitly positioned relative to Clark/Hutton/Ginzburg
- [ ] `scholarly_disagreement` names specific scholars and specific disagreements
- [ ] All provenance fields present and non-null
