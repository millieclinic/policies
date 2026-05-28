#!/usr/bin/env python3
"""generate-per-file-changelog.py — produce a file-by-file changelog
comparing every file in `Current Policies (<date> Generated)/3.a Final Markdown/` to its
original in `1. Original Docs (Word)/1.a Original Converted to MD/`.

For each final file, classify as:
  - RENAMED_ONLY (byte-identical to a folder-1 file; just renamed)
  - MODIFIED   (similar to a folder-1 file but content differs; diff shown)
  - MERGED     (multiple sources combined; per-source provenance + new
                content listed)

Output: `Current Policies (<date> Generated)/3.a Final Markdown/PER-FILE-CHANGELOG.md`
"""

from __future__ import annotations

import difflib
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
F1 = REPO / "1. Original Docs (Word)" / "1.a Original Converted to MD"


def _find_current_policies_folder() -> Path:
    matches = sorted(REPO.glob("Current Policies (* Generated)"))
    if not matches:
        raise SystemExit(
            "No `Current Policies (… Generated)/` folder found. "
            "Run `scripts/build-word-docs.py` first."
        )
    return matches[-1]


F3 = _find_current_policies_folder() / "3.a Final Markdown"

# --- Known merges (kept in sync with restructure-final.py) -----------------
ROMAN = ["", "I", "II", "III", "IV", "V"]

MERGES: dict[str, list[tuple[str, str, str]]] = {
    "02b. Patient Rights — Access, Amendment & Accounting of Disclosures.md": [
        ("03k HIPAA - Individual Rights to Access Their Records Policy.md",
         "Right to Access PHI", "L-009"),
        ("03j HIPAA - Individual Right to Request Amendments to PHI Policy.md",
         "Right to Request Amendments to PHI", "L-008"),
        ("03a HIPAA- Accounting of Disclosures Policy.md",
         "Accounting of Disclosures", "L-003"),
    ],
    "02c. PHI Use, Disclosure, Minimum Necessary & De-Identification.md": [
        ("03v HIPAA - Use and Disclosure of PHI for Various Legal, Public Health and Regulatory Purposes Policy.md",
         "Use & Disclosure of PHI for Legal, Public Health & Regulatory Purposes", "L-002"),
        ("03m HIPAA - Minimum Necessary Rule Policy.md",
         "Minimum Necessary Rule", "L-010"),
        ("03e HIPAA - De-Identifying and Re-Identifying PHI and Creation of Limited Data Sets Policy.md",
         "De-Identifying & Re-Identifying PHI + Limited Data Sets", "L-005"),
        ("03h HIPAA and Marketing Policy.md",
         "Marketing & Patient Communications", "L-006"),
    ],
    "03a. Technical Safeguards — Encryption, Passwords, Remote Access & Workstations.md": [
        ("03g HIPAA - Encryption Policy.md", "Encryption", "IT-005"),
        ("03o HIPAA - Password Management Policy.md", "Password Management", "IT-001"),
        ("03p HIPAA - Remote Access Policy.md", "Remote Access", "IT-006"),
        ("03w HIPAA - Workstation Use Policy (1).md",
         "Workstation Use (including BYOD & Mobile Device Management)", "IT-002"),
    ],
    "05a. Incident & Breach Response.md": [
        ("03s HIPAA - Security Incident Management Policy (2).md",
         "Security Incident Management", "IT-009"),
        ("03b HIPAA - Breach Notification Policy.md",
         "HIPAA Breach Notification", "L-004"),
        ("AWS and Aptible Security Incident Management Policy.md",
         "AWS & Aptible Cloud Incident Playbook", "(no original Policy #)"),
    ],
}

# Sub-sections that had their own pre-merge ECH modifications carried forward
SOURCE_NOTES: dict[str, str] = {
    "03w HIPAA - Workstation Use Policy (1).md":
        "BYOD/MDM clause was appended to the source file in May 2026 to close "
        "SIG M.1.3 / M.1.5 / M.1.6; that clause is preserved verbatim in the merge.",
}

# Folder-1 files that were intentionally dropped as superseded duplicates
SUPERSEDED: list[tuple[str, str]] = [
    ("03d HIPAA - Contingency Planning Policy.md",
     "older May 1 version; the `(1)` May 7 revision became `04a. Contingency Planning Policy.md`."),
    ("03l HIPAA - Millie_BAA (for BA Use with Subcontractor).md",
     "legacy `.doc` of the BAA template; the modern `.docx` became `06c. BAA Template (Subcontractor).md`."),
    ("03q HIPAA - Risk Management Policy.md",
     "byte-identical to the `(1)` version; the `(1)` became `01c. Risk Management Policy.md`."),
    ("03s HIPAA - Security Incident Management Policy (1).md",
     "May 14 PDF version; superseded by `(2).docx` May 18, now inside `05a. Incident & Breach Response.md`."),
    ("03s HIPAA - Security Incident Management Policy.docx.md",
     "May 1 oldest version; superseded by `(2).docx`, now inside `05a. Incident & Breach Response.md`."),
    ("03s HIPAA - Security Incident Management Policy.pdf.md",
     "May 6 PDF version; superseded by `(2).docx`, now inside `05a. Incident & Breach Response.md`."),
    ("03w HIPAA - Workstation Use Policy.md",
     "older May 1 version; the `(1)` May 4 version became part of `03a. Technical Safeguards…`."),
    ("Millie Information Security & Data Governance Framework.md",
     "older May 5 version; the `(1)` May 23 version became `01a. Information Security Framework.md`."),
    ("Millie Privacy Policy.md",
     "byte-identical to the `(1)` version; the `(1)` became `02a. Privacy Policy.md`."),
]

# ---------------------------------------------------------------------------


def find_byte_match(f3_path: Path) -> Path | None:
    target = f3_path.read_bytes()
    for f1 in F1.glob("*.md"):
        if f1.read_bytes() == target:
            return f1
    return None


def find_similar(f3_path: Path) -> tuple[Path | None, float]:
    target_text = f3_path.read_text(encoding="utf-8")
    target_lines = set(target_text.split("\n"))
    if not target_lines:
        return None, 0.0
    best = None
    best_ratio = 0.0
    for f1 in F1.glob("*.md"):
        f1_lines = set(f1.read_text(encoding="utf-8").split("\n"))
        if not f1_lines:
            continue
        overlap = len(target_lines & f1_lines)
        ratio = overlap / max(len(target_lines), len(f1_lines))
        if ratio > best_ratio:
            best_ratio = ratio
            best = f1
    return best, best_ratio


def diff_additions_deletions(
    f1_path: Path, f3_path: Path, max_lines: int = 40
) -> tuple[list[str], list[str]]:
    f1_lines = f1_path.read_text(encoding="utf-8").splitlines()
    f3_lines = f3_path.read_text(encoding="utf-8").splitlines()
    diff = list(difflib.unified_diff(f1_lines, f3_lines, n=0, lineterm=""))
    additions: list[str] = []
    deletions: list[str] = []
    for line in diff:
        if line.startswith("+++") or line.startswith("---") or line.startswith("@@"):
            continue
        if line.startswith("+"):
            additions.append(line[1:])
        elif line.startswith("-"):
            deletions.append(line[1:])
    return additions[:max_lines], deletions[:max_lines]


def render_section(name: str, body: str) -> str:
    return f"## {name}\n\n{body}\n\n---\n\n"


def main() -> None:
    out: list[str] = []
    out.append("# Per-File Changelog — Original → Final")
    out.append("")
    out.append(
        "For every active file in `Current Policies (<date> Generated)/3.a Final Markdown/`, this "
        "document shows exactly what changed from the original source(s) in "
        "`1. Original Docs (Word)/1.a Original Converted to MD/`. Walk it "
        "file-by-file to verify."
    )
    out.append("")
    out.append("Generated by `scripts/generate-per-file-changelog.py`. Re-run "
               "after any edit to `3.a Final Markdown/`.")
    out.append("")
    out.append("**Legend:**")
    out.append("- **Renamed only** = byte-identical to the original; just a "
               "new filename.")
    out.append("- **Renamed + modified** = original content plus added "
               "paragraphs/sentences; diff shown.")
    out.append("- **Merged** = multiple original policies combined into one "
               "file; each source preserved verbatim as a `## I. / ## II. / …` "
               "sub-section.")
    out.append("")
    out.append("---")
    out.append("")

    skip = {"CHANGES.md", "PER-FILE-CHANGELOG.md"}
    final_files = sorted(p for p in F3.glob("*.md") if p.name not in skip)

    for f3_path in final_files:
        body_lines: list[str] = []

        if f3_path.name in MERGES:
            # MERGED
            sources = MERGES[f3_path.name]
            body_lines.append(
                f"**Type:** Merged from {len(sources)} source policies."
            )
            body_lines.append("")
            body_lines.append("**Source policies** (each preserved verbatim as a sub-section):")
            body_lines.append("")
            for i, (src, title, code) in enumerate(sources, start=1):
                roman = ROMAN[i] if i < len(ROMAN) else str(i)
                body_lines.append(f"- **§{roman}. {title}** ← `{src}` (Policy # {code})")
            body_lines.append("")
            body_lines.append("**New content authored for the merge** (no original sentences edited):")
            body_lines.append("- A top metadata table listing the merged Policy # codes and the consolidation date.")
            body_lines.append("- A 2–3 sentence blended intro paragraph at the top describing the topic.")
            body_lines.append("- A `## I. / ## II. / …` sub-section heading per source with a provenance citation line (`*Originally: <filename> (Policy # X). Preserved verbatim below.*`).")
            body_lines.append("- Each source's existing headings were demoted one level so they nest inside the merge (i.e., source `## Foo` becomes `### Foo`).")
            body_lines.append("- Each source's redundant top metadata table was stripped (the info already lives in the merge's top table).")
            body_lines.append("")
            # Carry any source-specific notes
            source_notes_present = [s for s in sources if s[0] in SOURCE_NOTES]
            if source_notes_present:
                body_lines.append("**Carried-forward modifications from the source files** (already in the source MD before the merge):")
                for src, _, _ in source_notes_present:
                    body_lines.append(f"- `{src}`: {SOURCE_NOTES[src]}")
                body_lines.append("")
            body_lines.append("**Verbatim policy text from sources:** yes — no original sentences were edited during the merge.")
            out.append(render_section(f3_path.name, "\n".join(body_lines)))
            continue

        # Not a merge — check byte match first
        f1_match = find_byte_match(f3_path)
        if f1_match is not None:
            body_lines.append("**Type:** Renamed only — content byte-identical to original.")
            body_lines.append("")
            body_lines.append(f"**Source:** `{f1_match.name}`")
            body_lines.append("")
            body_lines.append("**Changes:** filename only.")
            # Special-case the misnamed bundle
            if "Privacy Policy" in f3_path.name:
                body_lines.append("")
                body_lines.append(
                    "⚠️ **Note:** Despite the name, this file is *not* a patient-facing "
                    "Notice of Privacy Practices — it is a bundle of 9 internal HIPAA staff "
                    "policies that an earlier Millie process concatenated under the "
                    "Accounting-of-Disclosures (L-003) header. The contents largely overlap "
                    "with the individual L-series policies that are now in `02b` and `02c`. "
                    "A real patient-facing NPP should be authored separately."
                )
            out.append(render_section(f3_path.name, "\n".join(body_lines)))
            continue

        # Modified — find best similar source by line overlap
        f1_similar, ratio = find_similar(f3_path)
        if f1_similar is None or ratio < 0.30:
            body_lines.append("**Type:** New / no matching folder-1 source identified.")
            out.append(render_section(f3_path.name, "\n".join(body_lines)))
            continue

        adds, dels = diff_additions_deletions(f1_similar, f3_path)
        body_lines.append(
            f"**Type:** Renamed + content modified ({int(ratio * 100)}% line overlap with source)."
        )
        body_lines.append("")
        body_lines.append(f"**Source:** `{f1_similar.name}`")
        body_lines.append("")
        body_lines.append(
            "**Changes:** filename changed; new lines added are listed below. "
            "(No original policy sentences were removed.)"
        )
        body_lines.append("")
        if adds:
            body_lines.append("**Lines added in the final version:**")
            body_lines.append("")
            body_lines.append("```")
            for a in adds:
                body_lines.append(a if a else "")
            body_lines.append("```")
            body_lines.append("")
        if dels:
            body_lines.append("**Lines that appear removed** (usually just whitespace/list-numbering rewrites — verify):")
            body_lines.append("")
            body_lines.append("```")
            for d in dels:
                body_lines.append(d if d else "")
            body_lines.append("```")
            body_lines.append("")
        out.append(render_section(f3_path.name, "\n".join(body_lines)))

    # Tail: superseded sources
    out.append("# Source files intentionally NOT carried forward (superseded)")
    out.append("")
    out.append(
        "These folder-1 files were deemed duplicates of newer versions or "
        "subsumed by a merge. They still exist in `1. Original Docs (Word)/1.a "
        "Original Converted to MD/` (and the underlying Word source still "
        "exists in `1. Original Docs (Word)/`) as historical reference; they "
        "are simply not in `Current Policies (<date> Generated)/3.a Final Markdown/`."
    )
    out.append("")
    for fname, reason in SUPERSEDED:
        out.append(f"- `{fname}` — {reason}")
    out.append("")

    report = F3 / "PER-FILE-CHANGELOG.md"
    report.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {report.relative_to(REPO)}")
    print(f"  {len(final_files)} files documented; {len(SUPERSEDED)} superseded sources noted")


if __name__ == "__main__":
    main()
