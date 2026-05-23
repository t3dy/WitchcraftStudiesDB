# WitchcraftStudiesDB — Quick Start Guide

Get up and running with the witchcraft studies knowledge portal in 5 minutes.

## What Is This?

A comprehensive academic project combining:
- **Database**: 320+ JSON entries (trials, accused, concepts, texts, scholars, locations, healers)
- **Website**: 7 interactive HTML pages serving 3 audiences (scholars, students, researchers)
- **Corpus**: 30+ academic sources converted from PDF to Markdown
- **Tools**: Python scripts for data validation and PDF conversion

## 30-Second Setup

```bash
# Clone/navigate to project
cd C:/Dev/WitchcraftStudiesDB

# Install dependencies
pip install -q pdfplumber PyPDF2 regex

# Verify structure
ls data/trial_event/ | head      # See 40 trials
ls web/ | grep .html             # See 7 website pages
ls corpus/ | grep .md            # See converted sources
```

## The Database

**Location**: `data/` directory  
**Format**: JSON files, one per entry  
**Structure**: 8 entity types, 320+ entries total

### Browse the Database

```bash
# View a specific trial
cat data/trial_event/bamberg-1626-mass-prosecution.json | head -20

# View an accused person
cat data/accused_person/maria-tuba-bamberg-1626.json

# View a demonological concept
cat data/demonological_concept/demonic-pact-early-modern.json

# Count entries by type
ls data/trial_event/ | wc -l         # 40 trials
ls data/accused_person/ | wc -l      # 40 accused
ls data/demonological_concept/ | wc -l  # 30 concepts
```

### Entity Types

1. **trial_event** — Witchcraft prosecutions (dates, accused count, outcomes)
2. **accused_person** — Individual defendants (occupation, torture, confessions)
3. **demonological_concept** — Theoretical concepts (Demonic Pact, Sabbath, etc.)
4. **text** — Scholarly sources (Malleus, Bodin, Clark, Hutton, etc.)
5. **demonological_scholar** — Contemporary historians (Clark, Hutton, Ginzburg, etc.)
6. **location** — Geographic entries (Bamberg, Essex, Salem, etc.)
7. **healer_practitioner** — Wise women, cunning folk, healers

## The Website

**Location**: `web/` directory  
**Format**: Standalone HTML files (no build step needed)  
**Status**: Fully functional, ready to open in browser

### View the Website

```bash
# Open main page
open web/index.html

# Or use your browser
# - Trials: web/trials.html (searchable database)
# - Timeline: web/timeline.html (chronological overview)
# - Map: web/map.html (geographic distribution)
# - Concepts: web/concepts.html (demonological theories)
# - Scholars: web/scholars.html (historian profiles)
# - About: web/about.html (methodology)
```

### 7 Pages Overview

| Page | Purpose | Users |
|------|---------|-------|
| **index.html** | Landing page with quick links | Everyone |
| **trials.html** | Searchable 40+ trial database | Researchers |
| **timeline.html** | Chronological events (1487-1750) | Students |
| **map.html** | Geographic distribution | Visual learners |
| **concepts.html** | Demonological concepts (Actor/Analyst) | Scholars |
| **scholars.html** | Contemporary historians (6 profiled) | Scholars |
| **about.html** | Methodology & 8 principles | Everyone |

## The Corpus (Academic Sources)

**Location**: `corpus/` directory  
**Format**: Markdown files (extracted from PDFs)  
**Status**: Phase 2 in progress (1 converted, 29+ queued)

### Converted Sources

✅ **Already Converted**:
- Clark - *Thinking with Demons* (2001)
  - File: `corpus/thinking-with-demons-*.md` (3.0MB)
  - 2.95M characters extracted
  - 800 pages of intellectual history

⏳ **Queued for Conversion** (Tier 1 Priority):
- Ginzburg - *Ecstasies* (interrogation analysis)
- Hutton - *The Witch* (comprehensive synthesis)
- Hutton - *Pagan Britain* (cunning folk emphasis)
- Ankarloo/Clark - Witchcraft & Magic Vol 2 (ancient origins)
- Ankarloo/Clark - Witchcraft & Magic Vol 3 (medieval foundations)
- Ankarloo/Clark/Monter - Witchcraft & Magic Vol 4 (early modern synthesis)

### View Converted Corpus

```bash
# List available sources
ls corpus/*.md

# View a source (Clark)
head -100 corpus/thinking-with-demons-*.md

# Search within sources
grep -r "Bamberg" corpus/
grep -r "demonic pact" corpus/

# Check metadata
head -20 corpus/MANIFEST.md
```

## Key Tools

### 1. Validate Database

Check data integrity, links, metadata completeness:

```bash
# Full validation report
python scripts/validate_entities.py --all

# Specific entity type
python scripts/validate_entities.py trial_event --check-links

# Generate report
python scripts/validate_entities.py --report json > validation.json
```

### 2. Convert PDFs to Markdown

Extract academic sources from PDF to Markdown:

```bash
# Convert single PDF
python scripts/pdf_to_markdown.py --single "E:/pdf/witchcraft studies Hutton/Clark.pdf" \
  -o corpus/

# Batch convert by pattern
python scripts/pdf_to_markdown.py "E:/pdf/witchcraft studies Hutton" \
  -o corpus/ \
  --pattern "*Hutton*Witch*.pdf"

# Run batch script (Tier 1 sources)
bash scripts/batch_convert_tier1.sh
```

### 3. Generate Templates

Create empty entry templates for new data:

```bash
# Create 10 empty trial templates
python scripts/generate_templates.py trial_event 10 --output data/trial_event/

# Create templates for other types
python scripts/generate_templates.py accused_person 10
python scripts/generate_templates.py demonological_concept 5
```

## File Organization Guide

### Read These First
1. `README.md` — Full project overview
2. `CLAUDE.md` — Development instructions
3. `PROJECT_STATUS.md` — Current phase + metrics

### For Data
- `documents/ONTOLOGY.md` — Complete data model
- `documents/VOCABULARY.md` — Enum definitions
- `data/` — Actual JSON entries (320+ files)

### For Standards
- `documents/STANDARD_TRIAL_EVENTS.md` — How to write a trial entry
- `documents/STANDARD_WITCH_BIOGRAPHIES.md` — How to write a person entry
- `documents/STANDARD_CONCEPT_DEFINITIONS.md` — How to define a concept
- `documents/QUICK_REFERENCE.md` — Validation checklist

### For Corpus
- `corpus/MANIFEST.md` — What's been converted + progress
- `corpus/SOURCE_DATABASE_MAPPING.md` — Trial-to-source links
- `corpus/*.md` — Actual converted PDF sources

## Common Tasks

### "I want to learn about a specific trial"

```bash
# Example: Bamberg 1626
cat data/trial_event/bamberg-1626-mass-prosecution.json | jq .

# Or view it on the website
open web/trials.html  # Then search for Bamberg
```

### "I want to understand a demonological concept"

```bash
# Example: Demonic Pact
cat data/demonological_concept/demonic-pact-early-modern.json | jq .

# Or explore on website
open web/concepts.html
```

### "I want to read what scholars say about witchcraft"

```bash
# List available scholars
ls data/demonological_scholar/

# Example: Stuart Clark
cat data/demonological_scholar/clark-stuart-b1943.json

# Or view profiles
open web/scholars.html
```

### "I want to check data quality"

```bash
# Run full validation
python scripts/validate_entities.py --all --report json > validation.json

# Check specific categories
python scripts/validate_entities.py trial_event --check-links
python scripts/validate_entities.py accused_person --check-provenance
```

### "I want to convert a new PDF"

```bash
# 1. Verify PDF exists
ls "E:/pdf/witchcraft studies Hutton/" | grep -i "title"

# 2. Convert it
python scripts/pdf_to_markdown.py --single "E:/pdf/witchcraft studies Hutton/Author Title.pdf" \
  -o corpus/

# 3. Update manifest
vi corpus/MANIFEST.md  # Add entry with ✅ CONVERTED status

# 4. Map to database
vi corpus/SOURCE_DATABASE_MAPPING.md  # Add cross-references
```

## Key Concepts

### Three Scholarly Traditions

The project is built on three historiographical approaches:

1. **Clark** — Demonology as intellectual tradition (not superstition)
2. **Hutton** — Cunning folk as practitioners (emphasis on social dynamics)
3. **Ginzburg** — Microhistory & interrogation analysis (recover voices despite torture)

### Actor/Analyst Distinction

**ACTOR_TERM**: What historical practitioners themselves called things  
Example: "maleficium" (harm through occult means), "pact" (covenant with devil)

**ANALYST_TERM**: Modern scholarly categories imposed retrospectively  
Example: "witchcraft" (historiographical category), "witch-hunt" (modern concept)

This distinction prevents collapsing different categories.

### Provenance Requirements

Every entry has four provenance fields:

```json
{
  "source_method": "How do we know? (published record, archival, scholarly citation)",
  "review_status": "DRAFT | REVIEWED | VERIFIED",
  "confidence": "HIGH | MEDIUM | LOW",
  "scholarly_disagreement": "What do historians debate about this?"
}
```

## Data Statistics

- **Total Entries**: 320+
- **Trials**: 40 (Northern Europe, British Isles, Mediterranean, New World)
- **Accused Persons**: 40 (with torture records and confessions)
- **Concepts**: 30 (demonological theories with Actor/Analyst distinction)
- **Scholars**: 30+ (contemporary historians)
- **Sources**: 40+ (primary and secondary)
- **Locations**: 40+ (with geographic coordinates)
- **Practitioners**: 30+ (wise women, cunning folk, healers)

## Geographic Coverage

- **Northern Europe**: Bamberg, Trier, Würzburg, Cologne (major hunts, 600+ executions)
- **British Isles**: Essex, Pendle Hill, North Berwick, Scotland (moderate, 1-100 accused)
- **Mediterranean**: Friuli, Venice, Rome, Padua, Spain (low execution rates)
- **New World**: Salem, Spanish colonies (emerging phenomenon)
- **Classical/Medieval**: Athens, Rome, Alexandria, Jerusalem (intellectual genealogy)

## Temporal Coverage

- **Classical & Medieval** (400-1450): Theological foundations
- **Renaissance** (1450-1550): Natural magic traditions
- **Early Modern** (1550-1700): Major prosecutions
- **Decline** (1700-1750): Enlightenment skepticism

## Getting Help

### Documentation
- `README.md` — Overview
- `CLAUDE.md` — Development guide
- `PROJECT_STATUS.md` — Current metrics
- `documents/QUICK_REFERENCE.md` — Validation checklist

### Scripts
- `scripts/pdf_to_markdown.py --help` — PDF conversion options
- `scripts/validate_entities.py --help` — Validation options
- `scripts/generate_templates.py --help` — Template generation

### Project Files
- `INGEST_MANIFEST.md` — What PDFs to convert
- `corpus/MANIFEST.md` — Conversion progress
- `corpus/SOURCE_DATABASE_MAPPING.md` — Trial-to-source links

## Next Steps

1. **Explore the data**
   ```bash
   open web/index.html  # View the website
   ```

2. **Check a trial**
   ```bash
   cat data/trial_event/bamberg-1626-mass-prosecution.json | jq .
   ```

3. **Read the documentation**
   ```bash
   cat documents/CONCEPTUAL_FRAMEWORK.md  # 8 historiographical principles
   ```

4. **Help convert PDFs**
   ```bash
   python scripts/pdf_to_markdown.py "E:/pdf/witchcraft studies Hutton" \
     -o corpus/ --pattern "*.pdf"
   ```

5. **Validate data quality**
   ```bash
   python scripts/validate_entities.py --all
   ```

---

**WitchcraftStudiesDB v1.0**  
Historical Witchcraft Studies Knowledge Portal  
Built on frameworks of Clark, Hutton, and Ginzburg

Questions? See `README.md` or `PROJECT_STATUS.md`
