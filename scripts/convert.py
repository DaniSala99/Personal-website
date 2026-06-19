#!/usr/bin/env python3
"""
Convert raw source files from raw/ into structured Markdown in input/.

Supported formats: .pdf  .docx  .txt  .md  .mdx
Supported sections: projects  work  education  portfolio

Usage:
  python scripts/convert.py                           # all raw files
  python scripts/convert.py --section projects        # one section only
  python scripts/convert.py --file 01-po-river.pdf   # single file
  python scripts/convert.py --dry-run                 # list without converting

Requires:
  ANTHROPIC_API_KEY environment variable
  pip install -r scripts/requirements.txt
"""

import argparse
import os
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
RAW_DIR = ROOT / "raw"
INPUT_DIR = ROOT / "input"
WIKI_DIR = ROOT / "wiki"

SECTIONS = ["projects", "work", "education", "portfolio"]

# ── Section-specific system prompts ──────────────────────────────────────────

SYSTEM_PROMPTS = {
    "projects": """\
You are converting a raw technical document (thesis, report, course project notes, freeform notes)
into a structured Markdown case study for a professional engineering portfolio website.

Output a single .md file with:

1. YAML frontmatter (between --- delimiters) with exactly these fields:
     title: Full descriptive project title
     subtitle: One sentence (max 15 words) used as the card preview
     client: "Institution · Course or context"  e.g. "Politecnico di Milano · M.Sc. Thesis"
     year: "YYYY"
     duration: "X months" or "Course-integrated project"
     tools: [list of software, languages, frameworks used]

2. Markdown body with exactly these sections in order:
     ## ▸ The Challenge
     ## ▸ My Approach
     ## ▸ The Solution
     ## ▸ Key Results
     ## ▸ Business Impact
     ## ▸ Tech Stack

Writing rules:
- Write in English
- Be specific and quantitative — extract every number, metric, method and result from the raw content
- The Challenge: explain the problem context and who cares about solving it
- My Approach: numbered list of methodological steps taken
- The Solution: what was actually built or delivered
- Key Results: bullet points, each with a specific number or measurable outcome
- Business Impact: who would buy or use this work (insurers, municipalities, engineering firms, etc.) and why
- Tech Stack: short inline code list like `Python` · `QGIS` · `HEC-RAS`
- Do NOT invent data that is not present in the source material
- Output ONLY the markdown file content, starting with ---
""",

    "work": """\
You are converting raw notes or a job description into a structured Markdown file
for a professional portfolio website.

Output a single .md file with:

1. YAML frontmatter (between --- delimiters):
     title: "Job Title"
     company: "Company Name"
     start: "YYYY"
     end: "YYYY"  or null if this is a current role
     skills: [array of 4-6 concise skill strings]

2. Markdown body: 2-3 focused paragraphs describing the role.
   - Use **bold** for key achievements or quantified results
   - Use *italic* for NDA or confidentiality notices
   - Be specific about tools, methods, deliverables

Rules:
- Write in English
- Do NOT invent data not present in the source
- Output ONLY the markdown file content, starting with ---
""",

    "education": """\
You are converting raw notes about an academic degree or exchange programme into a structured
Markdown file for a professional portfolio website.

Output a single .md file with YAML frontmatter only (between --- delimiters):
     degree: "M.Sc. / B.Sc. / Exchange — Full Programme Name"
     institution: "University Name"
     location: "City, Country"
     start: YYYY   (integer, no quotes)
     end: YYYY     (integer, no quotes) or null if ongoing
     grade: "XX/110"  or null if not applicable
     description: "One-line summary of coursework focus or specialisation"

Add a markdown body only if there is significant extra context worth preserving.

Rules:
- Write in English
- Output ONLY the markdown file content, starting with ---
""",

    "portfolio": """\
You are converting raw notes about a side project, personal tool, or experiment into a structured
Markdown file for a professional portfolio website.

Output a single .md file with YAML frontmatter only (between --- delimiters):
     title: "Project Name"
     year: "YYYY"
     type: "Side Project"  or "Open Source"  or "Research Tool"  etc.
     description: "2-3 sentences: what it does, why it was built, what makes it interesting"
     tools: [list of technologies used]
     repo: "https://..."   (omit line entirely if not applicable)
     url: "https://..."    (omit line entirely if not applicable)

No markdown body needed.

Rules:
- Write in English
- Output ONLY the markdown file content, starting with ---
""",
}

# ── Text extraction ───────────────────────────────────────────────────────────

def extract_text(filepath: Path) -> str:
    suffix = filepath.suffix.lower()
    if suffix == ".pdf":
        try:
            import pdfplumber
        except ImportError:
            sys.exit("Missing dependency: pip install pdfplumber")
        with pdfplumber.open(filepath) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif suffix == ".docx":
        try:
            from docx import Document
        except ImportError:
            sys.exit("Missing dependency: pip install python-docx")
        doc = Document(filepath)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    elif suffix in (".txt", ".md", ".mdx"):
        return filepath.read_text(encoding="utf-8")
    else:
        sys.exit(
            f"Unsupported format: {suffix}\n"
            "Supported formats: .pdf  .docx  .txt  .md  .mdx"
        )

# ── Conversion ────────────────────────────────────────────────────────────────

def convert(section: str, raw_file: Path, client) -> str:
    text = extract_text(raw_file)
    user_message = f"Source file: {raw_file.name}\n\nRaw content:\n---\n{text}\n---"
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPTS[section],
        messages=[{"role": "user", "content": user_message}],
    )
    return message.content[0].text.strip()

# ── Wiki entry ────────────────────────────────────────────────────────────────

def write_wiki_entry(section: str, slug: str, raw_file: Path) -> Path:
    wiki_dir = WIKI_DIR / section
    wiki_dir.mkdir(parents=True, exist_ok=True)
    entry = wiki_dir / f"{slug}.md"
    today = date.today().isoformat()
    entry.write_text(
        f"# {slug}\n\n"
        f"**Source:** `{raw_file.relative_to(ROOT)}`  \n"
        f"**Converted:** {today}  \n"
        f"**Output:** `input/{section}/{slug}.md`\n\n"
        "## Notes\n\n"
        "_Add notes here: what was synthesised, what needs manual review, "
        "which images are still missing._\n",
        encoding="utf-8",
    )
    return entry

# ── Main processing ───────────────────────────────────────────────────────────

def process_file(section: str, raw_file: Path, client, dry_run: bool, force: bool):
    slug = raw_file.stem
    output = INPUT_DIR / section / f"{slug}.md"

    if output.exists() and not force:
        print(f"  SKIP  {raw_file.name}  (output exists — use --force to overwrite)")
        return

    print(f"  →  [{section}] {raw_file.name}")

    if dry_run:
        return

    markdown = convert(section, raw_file, client)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown + "\n", encoding="utf-8")

    wiki_path = write_wiki_entry(section, slug, raw_file)
    print(f"     ✓ input/{section}/{slug}.md")
    print(f"     ✓ {wiki_path.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert raw source files to structured Markdown"
    )
    parser.add_argument(
        "--section", choices=SECTIONS,
        help="Process only this section (default: all)"
    )
    parser.add_argument(
        "--file",
        help="Process a single file by name, e.g. 01-po-river.pdf"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Overwrite existing output files in input/"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be processed without calling the API"
    )
    args = parser.parse_args()

    if not args.dry_run:
        try:
            import anthropic
        except ImportError:
            sys.exit("Missing dependency: pip install anthropic")
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            sys.exit("ANTHROPIC_API_KEY environment variable is not set.")
        client = anthropic.Anthropic(api_key=api_key)
    else:
        client = None

    if args.file:
        matches = list(RAW_DIR.rglob(args.file))
        if not matches:
            sys.exit(f"File not found in raw/: {args.file}")
        for f in matches:
            section = f.parent.name
            if section in SECTIONS:
                process_file(section, f, client, args.dry_run, args.force)
        return

    sections = [args.section] if args.section else SECTIONS
    total = 0
    for section in sections:
        section_dir = RAW_DIR / section
        if not section_dir.exists():
            continue
        files = sorted(
            f for f in section_dir.iterdir()
            if not f.name.startswith(".") and f.is_file()
        )
        for f in files:
            process_file(section, f, client, args.dry_run, args.force)
            total += 1

    if total == 0:
        print("No files found in raw/. Add source files to raw/projects/, raw/work/, etc.")
    elif not args.dry_run:
        print(f"\nDone — {total} file(s) converted.")


if __name__ == "__main__":
    main()
