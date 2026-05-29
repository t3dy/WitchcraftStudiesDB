# Scripts — Working Instructions

## Available Tools

### PDF Conversion: `pdf_to_markdown.py`

```bash
# Single file
python scripts/pdf_to_markdown.py --single "path/to/file.pdf" -o corpus/

# Batch by filename pattern
python scripts/pdf_to_markdown.py "E:/pdf/witchcraft studies Hutton" \
  -o corpus/ \
  --pattern "*Hutton*Witch*.pdf"

# Batch script for Tier 1 queue
bash scripts/batch_convert_tier1.sh
```

After conversion:
1. Add entry to `corpus/MANIFEST.md` with status ✅ CONVERTED
2. Map trials/concepts/scholars in `corpus/SOURCE_DATABASE_MAPPING.md`
3. Update `PROJECT_STATUS.md` with progress

### Data Validation: `validate_entities.py`

```bash
python scripts/validate_entities.py --all --report json
python scripts/validate_entities.py trial_event --check-links
python scripts/validate_entities.py accused_person --check-links
python scripts/validate_entities.py --report csv
```

### Template Generation: `generate_templates.py`

```bash
# Create empty trial templates
python scripts/generate_templates.py trial_event 10 --output data/trial_event/
```

## Troubleshooting

### PDF conversion fails
1. Check file exists: `ls "E:/pdf/witchcraft studies Hutton/"`
2. Check read permissions
3. Try single-file mode: `python scripts/pdf_to_markdown.py --single "path"`
4. Some PDFs from library genesis may be corrupted — check with a PDF reader first
5. Large PDFs (69MB+) may hit memory limits — run one at a time, not batch

### Link validation errors
- Run `validate_entities.py {type} --check-links` to isolate broken links
- Slugs must be exact: `lowercase-with-hyphens`, no spaces, no uppercase
- Forward references (e.g., `salem-1692-trials` before that trial file exists) will fail validation until the target entry is created

### Memory issues with large PDFs
```bash
python -Xmx4g scripts/pdf_to_markdown.py --single "large-file.pdf" -o corpus/
```

## Script Conventions

All scripts follow idempotent design — safe to re-run without side effects. Scripts do not overwrite existing output unless `--force` is specified.
