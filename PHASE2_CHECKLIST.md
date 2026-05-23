# Phase 2 Implementation Checklist

**Phase**: Academic Corpus Ingestion  
**Status**: Initiated (Ready for bulk conversion)  
**Start Date**: May 23, 2026  
**Target Completion**: 1-2 weeks

## Pre-Conversion Verification ✅

- [x] Project folder created: `C:\Dev\WitchcraftStudiesDB\`
- [x] Directory structure established
- [x] PDF source directory confirmed: `E:\pdf\witchcraft studies Hutton\` (559MB, 30+ files)
- [x] PDF extraction pipeline implemented (`scripts/pdf_to_markdown.py`)
- [x] Batch automation created (`scripts/batch_convert_tier1.sh`)
- [x] Dependencies documented (`requirements.txt`)
- [x] Manifest and tracking structure created
- [x] Cross-reference mapping framework designed

## Tier 1 Conversion Queue (READY) 

**7 Priority PDFs** — Estimated total time: 1-2 hours

- [ ] **1. Ginzburg - Ecstasies (1991)** — 69MB, ~15 min
  - File: `Ecstasies_ Deciphering the Witches' Sabbath_`
  - Focus: Interrogation analysis, torture-shaped confessions
  - Priority: CRITICAL for microhistory framework

- [ ] **2. Hutton - The Witch (Recent)** — 9.6MB, ~5-8 min
  - File: `Ronald Hutton The Witch_ A History of Fear from Ancient Times to the Present...`
  - Focus: Comprehensive synthesis from ancient to present
  - Priority: CRITICAL for social history framework

- [ ] **3. Hutton - Pagan Britain (2013)** — 32MB, ~8-10 min
  - File: `Ronald Hutton Pagan Britain.pdf`
  - Focus: Cunning folk traditions, magical practitioners
  - Priority: CRITICAL for practitioner emphasis

- [ ] **4. Ankarloo/Clark - Vol 2: Ancient** — 25MB, ~8-10 min
  - File: `Witchcraft and magic in Europe` Vol 2 ancient Greece and Rome`
  - Focus: Classical intellectual genealogy
  - Priority: CORE for classical origins

- [ ] **5. Ankarloo/Clark - Vol 3: Medieval** — 17MB, ~6-8 min
  - File: `Witchcraft and magic in Europe VOL 3 The Middle Ages_`
  - Focus: Medieval theology and foundations
  - Priority: CORE for medieval intellectual context

- [ ] **6. Ankarloo/Clark/Monter - Vol 4: Early Modern** — 13MB, ~5-7 min
  - File: `History of Witchcraft and Magic in Europe 4] ... Witch Trials (2001)...`
  - Focus: Regional variations in early modern prosecution
  - Priority: CORE for synthesis of trials

- [ ] **7. Ginzburg - Night Battles (1983)** — 3.5MB, ~2-3 min
  - File: `Routledge Library Editions_ Witchcraft] Carlo Ginzburg - The Night Battles...`
  - Focus: Friuli benandanti case study
  - Priority: CORE for case study methodology

## Tier 2 Conversion Queue (PLANNED)

**8 Secondary PDFs** — Estimated total time: 30-45 minutes

- [ ] Science of Demons (early modern natural philosophy)
- [ ] The Damned Art (essays on witchcraft literature)
- [ ] Witch Hunting and Witch Trials (English records)
- [ ] Witchcraft & Magic Europe Vol 1 (Biblical/pagan)
- [ ] Hutton - Queens of the Wild (gendered traditions)
- [ ] Young/Killick - Analysis of Keith Thomas
- [ ] [Journal article collections]

## Tier 3 Queue (LATER)

**15+ Tertiary PDFs** — Additional contextual sources

- Hutton's other works (Triumph of the Moon, etc.)
- Journal articles and specialized studies
- Nider's Formicarius (primary source)
- Comparative and regional analyses

## Conversion Process

### Pre-Conversion
1. [ ] Verify PDF exists in `E:/pdf/witchcraft studies Hutton/`
2. [ ] Check file size and condition
3. [ ] Note estimated conversion time

### Conversion Step
```bash
# Option 1: Single file
python scripts/pdf_to_markdown.py --single "path/to/pdf" -o corpus/

# Option 2: Batch by pattern
python scripts/pdf_to_markdown.py "E:/pdf/witchcraft studies Hutton" \
  -o corpus/ \
  --pattern "*pattern*"

# Option 3: Run full Tier 1 batch
bash scripts/batch_convert_tier1.sh
```

### Post-Conversion
1. [ ] Verify output file created in `corpus/`
2. [ ] Check file size (should be ~40% of original PDF)
3. [ ] Spot-check text extraction (first 100 lines)
4. [ ] Verify metadata extracted
5. [ ] Update `corpus/MANIFEST.md` with ✅ CONVERTED status
6. [ ] Add cross-references to `corpus/SOURCE_DATABASE_MAPPING.md`

## Progress Tracking

### Conversion Log
After each conversion batch, record:
- **Date**: When conversion occurred
- **PDF**: Filename
- **Size**: Original MB → Converted MB
- **Time**: Duration in minutes
- **Status**: SUCCESS | ISSUES | FAILED
- **Notes**: Any problems or observations

### Example Entry
```markdown
## [2026-05-23] 08:35 — Clark - Thinking with Demons
- Original: 7.7M PDF
- Converted: 3.0MB Markdown
- Time: ~4.5 minutes
- Status: ✅ SUCCESS
- Issues: None
- Pages extracted: 800+
- Characters: 2,954,809
```

## Quality Assurance

### Text Extraction Verification
- [ ] Check first page of output (compare to PDF)
- [ ] Check middle section (verify content integrity)
- [ ] Check final page (confirm no truncation)
- [ ] Verify headings are preserved
- [ ] Check footnotes/endnotes extraction
- [ ] Verify page numbers in HTML comments

### Metadata Validation
- [ ] Author extracted correctly
- [ ] Title accurate
- [ ] Page count correct
- [ ] Publication date present
- [ ] Publisher information included (if available)

### Cross-Reference Accuracy
- [ ] Trial names mentioned are correct
- [ ] Scholar citations are accurate
- [ ] Concept references match database
- [ ] Page numbers align with actual PDF

## Integration Checklist

After Tier 1 conversions complete:

- [ ] All 7 Tier 1 PDFs converted to Markdown
- [ ] `corpus/MANIFEST.md` updated with all conversions
- [ ] `corpus/SOURCE_DATABASE_MAPPING.md` populated with trial-source mappings
- [ ] Spot-check sampling complete (5-10 files)
- [ ] Validation report generated
- [ ] Cross-links from database entries to corpus added
- [ ] Search index created (future)

## Timeline Estimate

### Session 1 (This week)
- **Tier 1 Conversions**: 1-2 hours
- **Quality verification**: 30 minutes
- **Manifest updates**: 30 minutes
- **Total**: 2-3 hours

### Session 2 (Next week)
- **Tier 2 Conversions**: 30-45 minutes
- **Integration testing**: 1 hour
- **Database linking**: 1-2 hours
- **Total**: 2.5-3.5 hours

### Session 3+ (Following)
- **Tier 3 conversions**: As time allows
- **Full search implementation**: 2-3 hours
- **Historiographical tools**: 3-4 hours

## Key Commands for This Phase

### Quick Conversion
```bash
cd C:/Dev/WitchcraftStudiesDB

# Single file test
python scripts/pdf_to_markdown.py --single "E:/pdf/witchcraft studies Hutton/Stuart Clark Thinking with Demons.pdf" -o corpus/

# Tier 1 batch (all 7)
bash scripts/batch_convert_tier1.sh

# Check progress
ls -lh corpus/*.md | tail -10
```

### Verification
```bash
# Check manifest
cat corpus/MANIFEST.md | grep -A2 "✅ CONVERTED"

# List corpus files
find corpus -name "*.md" -type f | wc -l

# View conversion log (after batch)
tail -50 output/conversion_log.txt
```

## Success Criteria

**Tier 1 Complete When**:
- ✅ 7 PDF files successfully converted
- ✅ All Markdown files created in `corpus/`
- ✅ Metadata extracted for each
- ✅ Cross-reference mappings documented
- ✅ Quality spot-checks passed
- ✅ Manifest updated

**Phase 2 Complete When**:
- ✅ 30+ PDFs converted (all tiers)
- ✅ Cross-references integrated with database
- ✅ Search index created
- ✅ Website updated with corpus links
- ✅ Final validation report generated

## Known Limitations

- **Large files**: 69MB Ecstasies, 107MB Triumph of the Moon take 10-15 min
- **OCR artifacts**: Some library genesis PDFs may have scan artifacts
- **Manual cross-referencing**: Mapping PDFs to trials requires human review
- **Search indexing**: TBD in Phase 3

## Resources Needed

- **Disk space**: ~200MB for full corpus (estimated)
- **RAM**: 4GB minimum, 8GB recommended for batch
- **CPU**: Multi-core recommended
- **Time**: 2-3 hours per week for conversions
- **Source PDFs**: 559MB in `E:\pdf\witchcraft studies Hutton\`

## Next Session Checklist

Before starting next session:
- [ ] Verify all files from this session are present
- [ ] Confirm Python and pdfplumber still installed
- [ ] Check disk space available
- [ ] Review this checklist
- [ ] Check `QUICKSTART.md` for quick reference

---

**Phase 2: Academic Corpus Ingestion**
Ready to begin bulk PDF conversions.

**First priority**: Queue Tier 1 conversions with `bash scripts/batch_convert_tier1.sh`
