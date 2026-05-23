#!/usr/bin/env python3
"""
PDF to Markdown Converter for WitchcraftStudiesDB

Converts academic PDFs to structured Markdown with:
- Heading hierarchy preserved
- Footnotes/endnotes extracted
- Page numbers preserved
- Metadata extracted (author, title, date)
- Cross-reference index generated
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging

# Try multiple PDF extraction libraries with fallback
try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

try:
    from PyPDF2 import PdfReader
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False

try:
    import pytesseract
    from PIL import Image
    HAS_OCR = True
except ImportError:
    HAS_OCR = False

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)


class PDFToMarkdown:
    """Convert PDF to Markdown with academic document structure."""

    def __init__(self, pdf_path: str, output_dir: str = None):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir) if output_dir else self.pdf_path.parent / "markdown"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.metadata = {}
        self.text_content = []
        self.footnotes = {}
        self.page_map = {}  # page_number -> text position
        self.cross_refs = []  # extracted cross-references

    def extract_with_pdfplumber(self) -> str:
        """Extract text using pdfplumber (most robust for academic PDFs)."""
        if not HAS_PDFPLUMBER:
            return None

        logger.info(f"Extracting text from {self.pdf_path.name} using pdfplumber...")

        try:
            full_text = []
            with pdfplumber.open(self.pdf_path) as pdf:
                # Extract metadata
                if pdf.metadata:
                    self.metadata = {
                        'Author': pdf.metadata.get('Author', ''),
                        'Title': pdf.metadata.get('Title', ''),
                        'Subject': pdf.metadata.get('Subject', ''),
                        'Creator': pdf.metadata.get('Creator', ''),
                        'Producer': pdf.metadata.get('Producer', ''),
                        'CreationDate': pdf.metadata.get('CreationDate', ''),
                        'ModDate': pdf.metadata.get('ModDate', ''),
                        'Pages': len(pdf.pages)
                    }

                # Extract text page by page
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    if text:
                        # Record page position for cross-referencing
                        page_position = len(''.join(full_text))
                        self.page_map[page_num] = page_position

                        # Add page marker
                        full_text.append(f"\n<!-- PAGE {page_num} -->\n")
                        full_text.append(text)

                        # Try to extract tables
                        tables = page.extract_tables()
                        if tables:
                            for table in tables:
                                full_text.append(self._table_to_markdown(table))

            return ''.join(full_text)

        except Exception as e:
            logger.error(f"pdfplumber extraction failed: {e}")
            return None

    def extract_with_pypdf2(self) -> str:
        """Fallback extraction using PyPDF2."""
        if not HAS_PYPDF2:
            return None

        logger.info(f"Extracting text from {self.pdf_path.name} using PyPDF2...")

        try:
            full_text = []
            with open(self.pdf_path, 'rb') as file:
                reader = PdfReader(file)

                # Metadata
                if reader.metadata:
                    self.metadata = dict(reader.metadata) if reader.metadata else {}

                # Extract pages
                for page_num, page in enumerate(reader.pages, 1):
                    text = page.extract_text()
                    if text:
                        page_position = len(''.join(full_text))
                        self.page_map[page_num] = page_position

                        full_text.append(f"\n<!-- PAGE {page_num} -->\n")
                        full_text.append(text)

            return ''.join(full_text)

        except Exception as e:
            logger.error(f"PyPDF2 extraction failed: {e}")
            return None

    def extract_text(self) -> str:
        """Extract text with fallback chain."""
        # Try pdfplumber first (best for academic PDFs)
        text = self.extract_with_pdfplumber()
        if text:
            logger.info(f"✓ Successfully extracted {len(text)} characters with pdfplumber")
            return text

        # Fallback to PyPDF2
        text = self.extract_with_pypdf2()
        if text:
            logger.info(f"✓ Successfully extracted {len(text)} characters with PyPDF2")
            return text

        logger.error(f"✗ Failed to extract text from {self.pdf_path.name}")
        return ""

    def parse_structure(self, text: str) -> None:
        """Parse document structure: headings, footnotes, cross-references."""
        lines = text.split('\n')

        for i, line in enumerate(lines):
            line = line.strip()

            # Detect headings (various patterns)
            if self._is_heading(line):
                level = self._detect_heading_level(line)
                self.text_content.append((level, line))

            # Detect footnote references
            footnote_match = re.search(r'\[(\d+)\]\s+(.+)', line)
            if footnote_match:
                fn_num = footnote_match.group(1)
                fn_text = footnote_match.group(2)
                self.footnotes[fn_num] = fn_text

            # Detect cross-references (author citations)
            cite_matches = re.findall(r'\(([A-Z][a-z]+\s+[12]\d{3}[a-z]?)\)', line)
            for cite in cite_matches:
                if cite not in self.cross_refs:
                    self.cross_refs.append(cite)

    def _is_heading(self, line: str) -> bool:
        """Check if line is likely a heading."""
        # Patterns for headings
        patterns = [
            r'^[A-Z][A-Z\s]{5,}$',  # ALL CAPS with 5+ chars
            r'^\d+\.\s+[A-Z]',  # Numbered like "1. Introduction"
            r'^#{1,6}\s+',  # Markdown headings
            r'^[A-Z][a-z]+(\s+[A-Z][a-z]+){0,3}$'  # Title case, short
        ]

        return any(re.match(pattern, line) for pattern in patterns)

    def _detect_heading_level(self, line: str) -> int:
        """Detect heading hierarchy level (1-6)."""
        # Markdown headings
        if match := re.match(r'^(#+)', line):
            return len(match.group(1))

        # ALL CAPS = level 1
        if line.isupper():
            return 1

        # Title case = level 2
        if line[0].isupper() and ' ' in line:
            return 2

        return 3  # Default

    def _table_to_markdown(self, table: List[List[str]]) -> str:
        """Convert extracted table to Markdown."""
        if not table:
            return ""

        md_lines = []
        for row in table:
            md_lines.append('| ' + ' | '.join(str(cell or '').strip() for cell in row) + ' |')

        # Add separator after header
        if len(table) > 0:
            md_lines.insert(1, '| ' + ' | '.join(['---'] * len(table[0])) + ' |')

        return '\n' + '\n'.join(md_lines) + '\n'

    def to_markdown(self, raw_text: str) -> str:
        """Convert extracted text to structured Markdown."""
        md_lines = []

        # Header with metadata
        md_lines.append('---')
        md_lines.append(f'title: {self.metadata.get("Title", "Unknown")}')
        md_lines.append(f'author: {self.metadata.get("Author", "Unknown")}')
        md_lines.append(f'date: {self.metadata.get("CreationDate", "Unknown")}')
        md_lines.append(f'pages: {self.metadata.get("Pages", "Unknown")}')
        md_lines.append('---')
        md_lines.append('')

        # Body text (with minimal formatting)
        # Split by page markers and preserve structure
        sections = raw_text.split('<!-- PAGE')

        for section_idx, section in enumerate(sections):
            if section_idx == 0 and not section.strip():
                continue  # Skip empty first section

            # Clean up page marker
            if '-->' in section:
                page_info, content = section.split('-->', 1)
                page_match = re.search(r'(\d+)', page_info)
                if page_match:
                    page_num = int(page_match.group(1))
                    md_lines.append(f'\n**[p. {page_num}]**\n')
            else:
                content = section

            # Normalize and add content
            content = content.strip()
            if content:
                md_lines.append(content)
                md_lines.append('')

        # Footnotes section
        if self.footnotes:
            md_lines.append('\n## References\n')
            for fn_num, fn_text in sorted(self.footnotes.items()):
                md_lines.append(f'[{fn_num}] {fn_text}')

        # Cross-references index
        if self.cross_refs:
            md_lines.append('\n## Citations Found\n')
            for cite in sorted(set(self.cross_refs)):
                md_lines.append(f'- {cite}')

        return '\n'.join(md_lines)

    def convert(self, verbose: bool = True) -> Tuple[bool, str]:
        """
        Main conversion pipeline.

        Returns:
            (success, output_path)
        """
        if not self.pdf_path.exists():
            logger.error(f"PDF not found: {self.pdf_path}")
            return (False, "")

        logger.info(f"Starting conversion of {self.pdf_path.name}...")

        # Extract text
        raw_text = self.extract_text()
        if not raw_text:
            return (False, "")

        # Parse structure
        self.parse_structure(raw_text)

        # Convert to Markdown
        markdown = self.to_markdown(raw_text)

        # Determine output filename
        title = self.metadata.get('Title', self.pdf_path.stem)
        # Slugify title
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:50]
        output_file = self.output_dir / f"{slug}.md"

        # Write output
        try:
            output_file.write_text(markdown, encoding='utf-8')
            logger.info(f"✓ Converted to: {output_file}")
            return (True, str(output_file))
        except Exception as e:
            logger.error(f"Failed to write output: {e}")
            return (False, "")


def batch_convert(pdf_dir: str, output_dir: str = None, pattern: str = "*.pdf") -> Dict:
    """
    Convert all PDFs in a directory.

    Args:
        pdf_dir: Input directory containing PDFs
        output_dir: Output directory for Markdown files (defaults to pdf_dir/markdown)
        pattern: File glob pattern (default: *.pdf)

    Returns:
        Dictionary with results: {filename: (success, output_path)}
    """
    pdf_dir = Path(pdf_dir)
    if not pdf_dir.exists():
        logger.error(f"Directory not found: {pdf_dir}")
        return {}

    output_dir = Path(output_dir) if output_dir else pdf_dir / "markdown"
    output_dir.mkdir(parents=True, exist_ok=True)

    results = {}
    pdf_files = sorted(pdf_dir.glob(pattern))

    logger.info(f"Found {len(pdf_files)} PDFs to convert")

    for idx, pdf_file in enumerate(pdf_files, 1):
        logger.info(f"\n[{idx}/{len(pdf_files)}] Processing {pdf_file.name}...")

        converter = PDFToMarkdown(pdf_file, output_dir)
        success, output_path = converter.convert()
        results[pdf_file.name] = (success, output_path)

    # Summary report
    logger.info(f"\n{'='*60}")
    successful = sum(1 for s, _ in results.values() if s)
    logger.info(f"Conversion complete: {successful}/{len(results)} successful")
    logger.info(f"Output directory: {output_dir}")

    return results


if __name__ == '__main__':
    # Command line interface
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert academic PDFs to Markdown'
    )
    parser.add_argument('pdf_dir', help='Directory containing PDFs')
    parser.add_argument(
        '-o', '--output',
        help='Output directory (default: pdf_dir/markdown)'
    )
    parser.add_argument(
        '--pattern',
        default='*.pdf',
        help='File glob pattern (default: *.pdf)'
    )
    parser.add_argument(
        '--single',
        help='Convert single PDF file'
    )

    args = parser.parse_args()

    if args.single:
        # Single file conversion
        converter = PDFToMarkdown(args.single, args.output)
        success, output = converter.convert()
        sys.exit(0 if success else 1)
    else:
        # Batch conversion
        results = batch_convert(args.pdf_dir, args.output, args.pattern)
        sys.exit(0)
