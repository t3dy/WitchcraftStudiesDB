# START HERE — WitchcraftStudiesDB v1.0

## Welcome!

You're looking at a comprehensive digital humanities project combining:
- **Database**: 320+ historical records (trials, accused, concepts, scholars)
- **Website**: 7 interactive HTML pages
- **Academic Corpus**: 30+ scholarly sources being converted to Markdown
- **Tools**: Python scripts for data management

Built on scholarly frameworks of Stuart Clark, Ronald Hutton, and Carlo Ginzburg.

---

## What You Can Do Right Now

### 1️⃣ **Explore the Website** (5 minutes)

Open any of these files in your browser:
- `web/index.html` — Landing page
- `web/trials.html` — Searchable trial database
- `web/timeline.html` — Chronological overview
- `web/map.html` — Geographic distribution
- `web/concepts.html` — Demonological concepts
- `web/scholars.html` — Historian profiles
- `web/about.html` — Methodology

### 2️⃣ **Read the Documentation** (10-15 minutes)

Start with one of these:
- **README.md** — Full project overview (best for understanding scope)
- **QUICKSTART.md** — 30-second setup guide (best for quick examples)
- **PROJECT_STATUS.md** — Current metrics and phase status

### 3️⃣ **Browse the Database** (10 minutes)

View actual data files:
```bash
# View a trial
cat data/trial_event/bamberg-1626-mass-prosecution.json

# View an accused person
cat data/accused_person/maria-tuba-bamberg-1626.json

# View a concept
cat data/demonological_concept/demonic-pact-early-modern.json
```

### 4️⃣ **Continue PDF Ingestion** (Phase 2)

Convert academic PDFs to Markdown:
```bash
# Check requirements
pip install -q pdfplumber PyPDF2

# Run batch conversion
bash scripts/batch_convert_tier1.sh

# Track progress
cat corpus/MANIFEST.md
```

---

## Which Path Is for You?

### 👨‍💼 **I want to understand the project** (15 min read)
→ Read **README.md** first  
→ Then browse **web/about.html** for methodology  
→ Check **PROJECT_STATUS.md** for metrics

### 🎓 **I'm a student/researcher interested in witchcraft** (20 min)
→ Open **web/index.html** in your browser  
→ Explore **Trials**, **Timeline**, and **Map** pages  
→ Read **web/about.html** for historiographical context

### 👨‍💻 **I want to work with the code/data** (30 min)
→ Read **CLAUDE.md** for development instructions  
→ Review **documents/ONTOLOGY.md** for data model  
→ Check **scripts/** directory for tools  
→ See **PHASE2_CHECKLIST.md** if continuing PDF ingestion

### 📚 **I'm interested in the scholarship** (45 min)
→ Read **documents/CONCEPTUAL_FRAMEWORK.md** (8 principles)  
→ Read **documents/SCHOLARLY_MODELS_PROFILE.md** (Clark/Hutton/Ginzburg)  
→ Explore **corpus/MANIFEST.md** for available academic sources  
→ Check **web/scholars.html** for historian profiles

### 🔄 **I'm continuing Phase 2 PDF conversion** (immediate)
→ Read **PHASE2_CHECKLIST.md** (5 min)  
→ Run **bash scripts/batch_convert_tier1.sh** (1-2 hours)  
→ Update **corpus/MANIFEST.md** with progress

---

## Key Statistics

### Database
- **40 Trials**: Northern Europe, British Isles, Mediterranean, New World (1487-1750)
- **40 Accused Persons**: With occupation, torture records, confessions
- **30 Concepts**: Demonic Pact, Sabbath, Maleficium, Female Susceptibility, etc.
- **40+ Sources**: Malleus, Bodin, Clark, Hutton, Ginzburg, trial records
- **30+ Scholars**: Contemporary historians working on witchcraft
- **40+ Locations**: Geographic entries with coordinates
- **30+ Healers**: Wise women, cunning folk, practitioners

**Total: 320+ entries**

### Corpus
- **30+ Academic PDFs**: 559MB total in source directory
- **Converted**: 1 file (Clark - Thinking with Demons, 3.0MB)
- **Queued**: 29 files (Tier 1, 2, 3 priority tiers)

**Status**: 3% complete → Phase 2 in progress

---

## How to Navigate the Project

### Main Documentation Files
| File | Purpose | Read Time |
|------|---------|-----------|
| README.md | Full overview | 5 min |
| CLAUDE.md | Development guide | 5 min |
| QUICKSTART.md | Quick examples | 5 min |
| PROJECT_STATUS.md | Metrics & phase info | 10 min |
| SESSION_SUMMARY.md | What was accomplished | 10 min |

### Specifications (If Adding Data)
| File | Purpose |
|------|---------|
| documents/ONTOLOGY.md | Data model specification |
| documents/VOCABULARY.md | Enum and field definitions |
| documents/STANDARD_TRIAL_EVENTS.md | How to write a trial entry |
| documents/STANDARD_WITCH_BIOGRAPHIES.md | How to write a person entry |
| documents/STANDARD_CONCEPT_DEFINITIONS.md | How to define a concept |

### For Corpus Work (Phase 2)
| File | Purpose |
|------|---------|
| INGEST_MANIFEST.md | Catalog of PDFs to convert |
| PHASE2_CHECKLIST.md | Bulk conversion checklist |
| corpus/MANIFEST.md | Conversion progress tracker |
| corpus/SOURCE_DATABASE_MAPPING.md | Cross-reference structure |

---

## The Three Scholarly Traditions

This project is built on three major historiographical approaches:

### 1. Stuart Clark — Intellectual History
**Thesis**: Demonology was a sophisticated intellectual tradition, not superstition.

Witchcraft prosecutions were the **rational application of theological theory** within educated magistrates' frameworks. Understanding demonology seriously (not as irrational panic) is essential.

**Key Work**: *Thinking with Demons* (2001)

### 2. Ronald Hutton — Social History
**Thesis**: Cunning folk were legitimate practitioners. Social conflict drove accusations.

Prosecution wasn't primarily about abstract demonology, but about **neighborhood disputes, reputation conflicts, and demographic factors**. Healers and wise women were recognized practitioners.

**Key Works**: *Pagan Britain* (2013), *The Witch* (recent)

### 3. Carlo Ginzburg — Microhistory
**Thesis**: Torture shaped confessions. We must carefully read trial records.

Through **intensive study of individual cases** and careful analysis of interrogation records, we can partially recover the voices of the accused despite the distorting power of torture and interrogation.

**Key Works**: *Night Battles* (1983), *Ecstasies* (1991)

---

## Quick Example: The Demonic Pact

**What Historical Actors Called It** (ACTOR_TERM):
- Latin: *Pactum Daemonicum*
- German: *Teufelspakt*  
- Italian: *Patto Demoniaco*

**What It Meant to Practitioners & Magistrates**:
A covenant between a human and the devil, sealed by blood or explicit renunciation of Christian faith. The devil grants occult power; the human becomes the devil's servant.

**Historical Fact** (Clark's Approach):
This doctrine was systematically theorized by demonologists like Bodin. Magistrates used it as a legal framework for prosecution.

**Social Reality** (Hutton's Approach):
Most accused witches never claimed pacts. The pact doctrine was **imposed by educated magistrates** seeking to make sense of neighborhood conflicts.

**Interrogation Reality** (Ginzburg's Approach):
Confessions to pacts were often **torture-shaped**. By analyzing leading questions in interrogation records, we can see how magistrates prompted accused persons to construct pact narratives.

---

## What Makes This Different?

### ✅ Historiographical Rigor
- Every claim has a named source (source_method)
- Confidence levels on all assertions (HIGH/MEDIUM/LOW)
- Explicit documentation of scholarly disagreement
- Distinction between ACTOR_TERM (what practitioners called things) and ANALYST_TERM (modern categories)

### ✅ Three Constituencies Served
- **Scholars**: Precision, historiographical nuance, complete bibliography
- **Students**: Accessible prose, visual scaffolding, clear frameworks
- **Researchers**: Depth, browsability, primary source access

### ✅ Relational Design
- Browse from trial → accused → concepts → texts → scholars
- All entities cross-linked by slug references
- Follow connections to build understanding

### ✅ Academic Corpus
- 30+ scholarly sources (PDF → Markdown conversion)
- Direct links from database entries to source citations
- Extended discussion available for deep learning

---

## Next Steps

### If You're New:
1. Open **web/index.html** in your browser (2 min)
2. Read **README.md** (5 min)
3. Read **documents/CONCEPTUAL_FRAMEWORK.md** (10 min)
4. Browse a few entries in **data/** directory (5 min)

### If You're Continuing Phase 2:
1. Read **PHASE2_CHECKLIST.md** (5 min)
2. Run **bash scripts/batch_convert_tier1.sh** (1-2 hours)
3. Update **corpus/MANIFEST.md** with progress
4. Add mappings to **corpus/SOURCE_DATABASE_MAPPING.md**

### If You're Adding Data:
1. Read appropriate **STANDARD_*.md** specification
2. Create JSON entry in **data/[entity_type]/**
3. Include all provenance fields
4. Validate: **python scripts/validate_entities.py --check-links**

---

## Questions?

- **Overview**: See README.md
- **Quick Help**: See QUICKSTART.md
- **Development**: See CLAUDE.md
- **Metrics**: See PROJECT_STATUS.md
- **Current Progress**: See SESSION_SUMMARY.md

---

**WitchcraftStudiesDB v1.0**  
Historical Witchcraft Studies Knowledge Portal

*Built on frameworks of Stuart Clark, Ronald Hutton, and Carlo Ginzburg*

Ready to explore!
