#!/usr/bin/env python3
"""build-word-docs.py — assemble the exec-facing bundle of Word/Excel/PDF files.

Strategy (maximum fidelity to the originals):
  * For policies that are unchanged from `1. original_docs_markdown/`, copy the
    *original* source file (`.docx`, `.xlsx`, `.pdf`) directly from
    `Policy Docs/`. This preserves all of the original Word formatting — fonts,
    headings, numbered lists, tables — exactly as drafted.
  * For policies that were modified in `3. final_policies/` (e.g., the 3 short
    ECH-required clauses appended), pandoc-convert the modified Markdown to
    `.docx`. These will not look identical to the originals, but they'll be
    readable Word docs.
  * `CHANGES.md` (and any other generated Markdown without a source) is also
    pandoc-converted.

Re-run any time the final policies change. Auto-installs pandoc via Homebrew
on first run if missing.

Output: `policy_docs_word/`
"""

from __future__ import annotations

import filecmp
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POLICY_DOCS = REPO / "Policy Docs"
FOLDER_1 = REPO / "1. original_docs_markdown"
FOLDER_3 = REPO / "3. final_policies"
FOLDER_2 = REPO / "2. gaps_for_ech"
OUT = REPO / "policy_docs_word"
OUT_GAP = OUT / "gap_analysis"


def ensure_pandoc() -> None:
    if shutil.which("pandoc") is None:
        print("Pandoc not found; installing via Homebrew…")
        if shutil.which("brew") is None:
            print(
                "ERROR: Homebrew not found. Install pandoc manually: "
                "https://pandoc.org/installing.html",
                file=sys.stderr,
            )
            sys.exit(1)
        subprocess.run(["brew", "install", "pandoc"], check=True)


def find_source(stem: str) -> Path | None:
    """Find an original file in Policy Docs/ that matches the given stem."""
    for ext in (".docx", ".pdf", ".xlsx", ".doc"):
        cand = POLICY_DOCS / f"{stem}{ext}"
        if cand.exists():
            return cand
    return None


def preprocess_md(src: Path) -> Path:
    """Strip docx→md conversion artifacts so pandoc → .docx renders cleanly."""
    text = src.read_text(encoding="utf-8")

    # Remove the 1-cell base64 logo table at the top: 2 lines like
    #   | **![](data:image/jpeg;base64...)** | |
    #   | --- | --- |
    text = re.sub(
        r"^\| \*\*!\[\]\(data:image[^)]*\)\*\* \| \|\n\| --- \| --- \|\n",
        "",
        text,
        flags=re.MULTILINE,
    )
    # Also handle png variants and the un-bolded form
    text = re.sub(
        r"^\| !\[\]\(data:image[^)]*\) \| \|\n\| --- \| --- \|\n",
        "",
        text,
        flags=re.MULTILINE,
    )

    # Remove any remaining inline base64 image placeholders
    text = re.sub(r"!\[\]\(data:image[^)]*\)", "", text)

    # Fix the very common docx→md typo ("Companypersonnel" missing a space)
    text = text.replace("Companypersonnel", "Company personnel")

    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    )
    tmp.write(text)
    tmp.close()
    return Path(tmp.name)


def pandoc_to_docx(src_md: Path, dst_docx: Path) -> None:
    cleaned = preprocess_md(src_md)
    try:
        subprocess.run(
            [
                "pandoc",
                str(cleaned),
                "--from",
                "markdown",
                "--to",
                "docx",
                "--standalone",
                "-o",
                str(dst_docx),
            ],
            check=True,
        )
    finally:
        cleaned.unlink(missing_ok=True)


def main() -> None:
    ensure_pandoc()

    if not FOLDER_3.exists():
        print(f"ERROR: {FOLDER_3} not found.", file=sys.stderr)
        sys.exit(1)

    OUT.mkdir(exist_ok=True)
    OUT_GAP.mkdir(exist_ok=True)
    # Clean rebuild — remove anything we previously wrote
    for f in OUT.iterdir():
        if f.is_file():
            f.unlink()
    for f in OUT_GAP.iterdir():
        if f.is_file():
            f.unlink()

    stats = {
        "copied_docx": 0,
        "copied_other": 0,
        "pandoc_modified": 0,
        "pandoc_generated": 0,
        "gap_docx": 0,
        "gap_xlsx": 0,
    }

    for md_file in sorted(FOLDER_3.glob("*.md")):
        stem = md_file.stem

        # CHANGES.md (and any other generated MD without a source) → pandoc
        source = find_source(stem)
        if stem == "CHANGES" or source is None:
            dst = OUT / f"{stem}.docx"
            pandoc_to_docx(md_file, dst)
            stats["pandoc_generated"] += 1
            print(f"  [pandoc, no source]  {dst.name}")
            continue

        # Is this .md modified vs the folder-1 baseline?
        folder1_md = FOLDER_1 / md_file.name
        unchanged = folder1_md.exists() and filecmp.cmp(
            md_file, folder1_md, shallow=False
        )

        if unchanged:
            dst = OUT / source.name
            shutil.copy2(source, dst)
            if source.suffix == ".docx":
                stats["copied_docx"] += 1
            else:
                stats["copied_other"] += 1
            print(f"  [copy {source.suffix:>5}]     {dst.name}")
        else:
            # Modified — pandoc the .md so the additions are reflected
            dst = OUT / f"{stem}.docx"
            pandoc_to_docx(md_file, dst)
            stats["pandoc_modified"] += 1
            print(f"  [pandoc, modified]   {dst.name}")

    # ---------- Gap analysis bundle ----------
    # Convert the markdown gap docs to .docx and the coverage CSV to a formatted .xlsx
    # so an exec can review the analysis alongside the policies.
    if FOLDER_2.exists():
        print()
        print("Gap analysis:")
        for md_file in sorted(FOLDER_2.glob("*.md")):
            dst = OUT_GAP / f"{md_file.stem}.docx"
            pandoc_to_docx(md_file, dst)
            stats["gap_docx"] += 1
            print(f"  [pandoc]   gap_analysis/{dst.name}")
        for csv_file in sorted(FOLDER_2.glob("*.csv")):
            dst = OUT_GAP / f"{csv_file.stem}.xlsx"
            try:
                import csv as _csv
                from openpyxl import Workbook
                from openpyxl.styles import Alignment, Font, PatternFill
                from openpyxl.utils import get_column_letter

                wb = Workbook()
                ws = wb.active
                ws.title = "Coverage Matrix"
                with open(csv_file, newline="", encoding="utf-8") as f:
                    rows = list(_csv.reader(f))
                for row in rows:
                    ws.append(row)
                # Header styling
                header_font = Font(bold=True, color="FFFFFF")
                header_fill = PatternFill("solid", fgColor="305496")
                for cell in ws[1]:
                    cell.font = header_font
                    cell.fill = header_fill
                    cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
                # Column widths — generous for text-heavy columns, narrower for short ones
                widths = {
                    "A": 18, "B": 28, "C": 8, "D": 50, "E": 36,
                    "F": 22, "G": 36, "H": 16, "I": 18, "J": 50,
                    "K": 36, "L": 12, "M": 36, "N": 30, "O": 50, "P": 10,
                }
                for col_letter, w in widths.items():
                    ws.column_dimensions[col_letter].width = w
                # Wrap text + top-align all data cells
                wrap_align = Alignment(wrap_text=True, vertical="top")
                for row in ws.iter_rows(min_row=2):
                    for cell in row:
                        cell.alignment = wrap_align
                # Freeze the header row
                ws.freeze_panes = "A2"
                wb.save(dst)
                stats["gap_xlsx"] += 1
                print(f"  [xlsx]     gap_analysis/{dst.name}")
            except Exception as e:
                # Fallback: plain copy of the CSV
                shutil.copy2(csv_file, OUT_GAP / csv_file.name)
                stats["gap_xlsx"] += 1
                print(f"  [copy csv (xlsx failed: {e})] gap_analysis/{csv_file.name}")

    total = sum(stats.values())
    print()
    print(f"Done. {total} files written to {OUT.relative_to(REPO)}/")
    print(f"  copied .docx originals:  {stats['copied_docx']}")
    print(f"  copied .xlsx/.pdf:       {stats['copied_other']}")
    print(f"  pandoc (modified .md):   {stats['pandoc_modified']}")
    print(f"  pandoc (generated .md):  {stats['pandoc_generated']}")
    print(f"  gap-analysis .docx:      {stats['gap_docx']}")
    print(f"  gap-analysis .xlsx:      {stats['gap_xlsx']}")
    print()
    print("Share with execs:")
    print("  • Word — open .docx files directly")
    print("  • Excel — open .xlsx files directly")
    print("  • Google Drive — drag the whole folder in; .docx/.xlsx/.pdf all")
    print("    auto-open in the matching Google app")


if __name__ == "__main__":
    main()
