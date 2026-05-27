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
OUT = REPO / "policy_docs_word"


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
    # Clean rebuild — remove anything we previously wrote
    for f in OUT.iterdir():
        if f.is_file():
            f.unlink()

    stats = {
        "copied_docx": 0,
        "copied_other": 0,
        "pandoc_modified": 0,
        "pandoc_generated": 0,
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

    total = sum(stats.values())
    print()
    print(f"Done. {total} files written to {OUT.relative_to(REPO)}/")
    print(f"  copied .docx originals:  {stats['copied_docx']}")
    print(f"  copied .xlsx/.pdf:       {stats['copied_other']}")
    print(f"  pandoc (modified .md):   {stats['pandoc_modified']}")
    print(f"  pandoc (generated .md):  {stats['pandoc_generated']}")
    print()
    print("Share with execs:")
    print("  • Word — open .docx files directly")
    print("  • Excel — open .xlsx files directly")
    print("  • Google Drive — drag the whole folder in; .docx/.xlsx/.pdf all")
    print("    auto-open in the matching Google app")


if __name__ == "__main__":
    main()
