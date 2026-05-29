# WitchcraftStudiesDB — Accused Person Writing Style Guide

**Target standard**: Encyclopedia article at the level of a Wikipedia "Good Article" or *Oxford Dictionary of National Biography* entry — dense, attributed, honest about what the evidence does and does not support.

---

## 1. Confidence Level → Prose Register

The `confidence` metadata field governs every word of every narrative field. Match your prose to the evidence, not to how interesting you wish the case were.

### HIGH Confidence

**Use when**: Archival primary sources, published trial transcripts, named primary documents, or secure scholarly consensus from multiple independent sources.

**Prose register**: Indicative mood throughout. Specific dates, names, and quantities stated as fact. Named sources embedded naturally in the sentence. Do not weaken well-documented claims with hedges.

```
✓ "Bishop was examined before magistrates Hathorne and Corwin on April 19, 1692."
✓ "The jury initially returned a not-guilty verdict, which the judges sent back for reconsideration after a perceived non-response from Nurse."
✓ "Junius's letter to his daughter Veronica, smuggled from prison before his August 6, 1628 execution, documents the confession mechanism in his own words."

✗ "Bishop may have been examined around April 1692."
✗ "Sources suggest the jury initially found Nurse not guilty."
✗ "It is believed that Junius wrote to his daughter during his imprisonment."
```

### MEDIUM Confidence

**Use when**: Scholarly reconstruction from fragmentary records; inference is required to bridge gaps; scholars disagree on interpretation; few primary sources survive but the scholarly framework is sound.

**Prose register**: Named scholars as interpretive authorities. Interpretive framing for contested claims. Specific claims still stated directly where documented; hedging applied *only* to inferred elements, not to the documented ones. Acknowledge the source base's limits once per entry, then proceed to analysis.

```
✓ "Grioni's interrogation, like others in the Friuli proceedings, appears to have followed the inquisitorial pattern Ginzburg reconstructs from the Gasparutto-Moduco testimony."
✓ "The fragmentary record preserves enough of his testimony to confirm his basic benandante self-identification, though the full content of his confession is not known."
✓ "Tagliacarne likely described nocturnal combat in terms consistent with other benandanti testimony, though his specific account is not independently documented."

✗ "Grioni definitely attended Ember Day gatherings." [overclaims]
✗ "Grioni might possibly have perhaps been involved in something." [excessive hedging]
```

### LOW Confidence

**Use when**: Individual known only through a single mention in another person's confession, a single entry in a list, or one passing archival reference with no corroboration.

**Prose register**: The opening sentence of `biography` *must* explicitly name the evidentiary basis. Conditional and modal constructions for all inferred actions. Structural analysis of what institutional mechanisms would have produced is permitted as HIGH-confidence analytical framing even for a LOW-confidence individual.

```
✓ "Frau Hoelmann is known only through her appearance in Margaretha Binder's 1626 tortured confession, where she is identified as a widow residing in Bamberg."
✓ "Her interrogation would have followed the institutional protocol documented in the Junius and Binder cases."
✓ "No independent biographical record survives."

✗ "Hoelmann was arrested in January 1627 and confessed to sabbath attendance." [false precision]
✗ "Little is known about Hoelmann's life." [too vague — say exactly what IS known and from where]
```

---

## 2. Encyclopedia Article Structure

### `biography` (200–400 words)

- **Sentence 1**: Who, when, where, outcome — at the confidence level appropriate to the entry. For LOW confidence, sentence 1 names the evidentiary basis.
- **Body**: Contextual detail about their life before accusation. For HIGH: specific detail. For LOW: structural context about their social position.
- **Final paragraph**: Historiographical positioning — what makes this case significant to scholars.

### `arrest_narrative` (100–200 words)

- The mechanism by which they came to authority's attention (neighbor accusation, employer denunciation, cascade naming, self-identification)
- Institutional and social context of the arrest
- Connection to broader prosecution if applicable

### `historiographical_analysis` subsections

Each of the three subsections answers a specific question:
- `torture_mechanism`: What does this case tell us about *how* the confession was produced? (Ginzburg's framework)
- `plausibility`: What does the evidence actually show, stripped of the accusatory frame? (Hutton's framework)
- `social_vulnerability`: What structural position made this person susceptible? (demographic/social history framework)

### `historiographical_significance` (150–300 words)

This is the most encyclopedia-facing field. Structure:
1. The specific scholarly debate this case illuminates (1 sentence)
2. Named scholars and their specific arguments (2–4 sentences)
3. How this case differs from or extends the general pattern (1–2 sentences)
4. Broader significance for the field (1 sentence)

---

## 3. Historiographical Attribution Standards

**Always name the scholar**:
```
✓ "Ginzburg's analysis demonstrates..."
✓ "Hutton notes..."
✓ "Levack argues in The Witch-Hunt in Early Modern Europe..."
✓ "Boyer and Nissenbaum's community conflict model..."

✗ "Historians believe..."
✗ "Scholars have suggested..."
✗ "It is generally accepted that..."
✗ "Modern scholarship recognizes..."
```

**When scholars disagree, state both positions with names**:
```
✓ "Ginzburg interprets the benandanti as evidence of shamanic survivals from pre-Christian agrarian religion; Briggs accepts the folk belief reality while questioning whether the evidence supports a continuous tradition rather than convergent development."

✗ "There is scholarly debate about the origins of the benandanti."
```

**Primary sources take precedence over secondary analysis**:
```
✓ "The examination transcript preserved in the Salem Witchcraft Papers records her response verbatim: 'I am no witch. I know not what a witch is.'"

✗ "Historians have noted that Bishop denied the charges."
```

---

## 4. Actor / Analyst Distinction in Prose

The Actor/Analyst distinction is one of the project's 8 core historiographical principles. It must be visible in the prose.

**Actor terms** (the historical subject's own language, or that of their contemporaries) appear in quotation marks or with explicit framing:

```
✓ "Moduco described himself as a 'good walker' (benandante)"
✓ "The inquisitor imposed the category of 'sabbath' on what Moduco called communal spirit combat"
✓ "What contemporaries termed 'maleficium' comprised a range of alleged harmful practices"
```

**Analyst terms** (modern scholarly categories) appear without apology but are not used as if they were contemporaries' own categories:

```
✓ "The cascade mechanism — a structural feature of confession-based prosecutions — produced Hoelmann's arrest"
✓ "Social marginality, in Karlsen's formulation, was a primary risk factor at Salem"

✗ "Moduco attended sabbath gatherings" [uses inquisitorial analyst frame as uncontested fact]
✗ "Bishop practiced folk magic" [imposes a scholarly category as historical fact]
```

---

## 5. Specific Prohibitions

- **Do not fabricate specificity for LOW confidence entries**. No invented arrest dates, no assumed confession content, no imagined courtroom detail.
- **Do not hedge HIGH confidence entries**. If the primary source says April 19, 1692, say April 19, 1692.
- **Never write "according to some sources"** without naming the sources.
- **Never use "interesting," "fascinating," "remarkable"** as editorializing adjectives. Let the facts carry the weight.
- **Never begin `historiographical_significance` with "This case is important because"**. State the significance directly.
- **No passive constructions that hide the interpreter**: not "it has been argued that" — say who argued it.
- **Avoid the false balance trap**: if the scholarly consensus is clear (e.g., that Salem confessions were not evidence of actual witchcraft), state the consensus. Reserve "debate" language for genuine debates.

---

## 6. Schema Note: `accusations_against_her`

This field name is a legacy artifact from the first entry (Margaretha Binder, female). The JSON schema is immutable; do not create a parallel `accusations_against_him` field. The *content* of the field should correctly use the subject's pronouns and accurately describe the charges as recorded.

---

## 7. Review Checklist

Before finalizing any accused person entry, verify:

- [ ] Biography sentence 1 matches the confidence level (LOW: names the single source; HIGH: states facts directly)
- [ ] Every scholar named in `historiographical_significance` is making a specific identifiable argument
- [ ] Actor/Analyst distinction observed in confession and interrogation narrative
- [ ] `scholarly_disagreement` field (if present) names both sides of the debate
- [ ] No specific dates, names, or quantities in LOW confidence entries that are not in the source
- [ ] `historiographical_analysis` answers all three questions (how confession produced, what evidence shows, structural vulnerability)
