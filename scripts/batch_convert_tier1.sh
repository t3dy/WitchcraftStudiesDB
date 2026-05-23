#!/bin/bash
# Batch conversion script for Tier 1 priority PDFs
# Converts foundational sources to Markdown

cd "$(dirname "$0")/.."

PDF_SOURCE="E:/pdf/witchcraft studies Hutton"
OUTPUT_DIR="corpus"
LOGFILE="output/conversion_log.txt"

echo "==================================================================="
echo "WitchcraftStudiesDB Tier 1 PDF Conversion Batch"
echo "Start time: $(date)"
echo "==================================================================="
echo ""

# Create output directory
mkdir -p "$OUTPUT_DIR"
mkdir -p output

# List of Tier 1 PDFs to convert
declare -a TIER1_PDFS=(
    "Stuart Clark Thinking with Demons.pdf"
    "[Witchcraft and magic in Europe] Bengt Ankarloo, Stuart Clark - Witchcraft and Magic in Europe, Volume 2_ ancient Greece and Rome (1999, University of Pennsylvania Press) - libgen.li.pdf"
    "Witchcraft and magic in Europe VOL 3 The Middle Ages_"
    "[History of Witchcraft and Magic in Europe 4] Bengt Ankarloo, William Monter, Stuart Clark - Witchcraft and Magic in Europe_ The Period of the Witch Trials (2001, The Athlone Press) - libgen.li.pdf"
    "Ronald Hutton The Witch_ A History of Fear from Ancient Times to the Present 10 12987_9780300231243 libgen li.pdf"
    "Ronald Hutton Pagan Britain.pdf"
    "Ecstasies_ Deciphering the Witches' Sabbath_"
)

echo "Converting Tier 1 PDFs..."
echo ""

# Convert each PDF
for pdf in "${TIER1_PDFS[@]}"; do
    pdf_path="$PDF_SOURCE/$pdf"

    if [ -f "$pdf_path" ]; then
        echo "[$(date '+%H:%M:%S')] Converting: $pdf"
        python scripts/pdf_to_markdown.py "$PDF_SOURCE" \
            -o "$OUTPUT_DIR" \
            --pattern "$(basename "$pdf")" \
            >> "$LOGFILE" 2>&1

        if [ $? -eq 0 ]; then
            echo "  ✓ SUCCESS"
        else
            echo "  ✗ FAILED"
        fi
    else
        echo "[$(date '+%H:%M:%S')] SKIPPED (not found): $pdf"
    fi
    echo ""
done

echo "==================================================================="
echo "Tier 1 Conversion Complete"
echo "End time: $(date)"
echo "Output directory: $OUTPUT_DIR"
echo "Log file: $LOGFILE"
echo "==================================================================="
