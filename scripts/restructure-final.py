#!/usr/bin/env python3
"""restructure-final.py — one-shot script to:
  1. Merge 4 sets of related policies into 4 consolidated files
  2. Rename remaining files with category prefixes (01a, 01b, 02a, ...)

Each merged file gets a brief blended intro at the top and preserves the
underlying source policies verbatim as ## sub-sections so an auditor can still
Ctrl-F to specific policy names.

Run once: `python3 scripts/restructure-final.py`
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROOT = REPO / "3. Final Word" / "3.a Final Markdown"

_ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
_LETTERS = "abcdefghijklmnopqrstuvwxyz"


def strip_artifacts(text: str) -> str:
    """Strip base64 image lines and the metadata table from a source file."""
    text = re.sub(
        r"^\| \*\*!\[\]\(data:image[^)]*\)\*\* \| \|\n\| --- \| --- \|\n",
        "",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^\| !\[\]\(data:image[^)]*\) \| \|\n\| --- \| --- \|\n",
        "",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(r"!\[\]\(data:image[^)]*\)", "", text)
    text = text.replace("Companypersonnel", "Company personnel")
    # Strip the metadata-table rows (Title/Policy# and Effective/Last Revised)
    lines = text.split("\n")
    keep = []
    skipping_meta = 0
    for i, line in enumerate(lines):
        if skipping_meta > 0:
            skipping_meta -= 1
            continue
        # Skip top-of-file metadata table
        if i < 15 and "**Title**:" in line and "**Policy #**:" in line:
            if i + 1 < len(lines) and "**Effective Date**:" in lines[i + 1]:
                skipping_meta = 1
            continue
        keep.append(line)
    return "\n".join(keep).lstrip("\n")


def demote_to_subsection(text: str) -> str:
    """Rebuild flat-numbered headings as ### / #### so they nest under a ## merge section."""
    lines = text.split("\n")
    # Files that already use # heading markdown (e.g., Framework) — demote those by 2 levels
    has_flat = any(re.match(r"^\d+\. \*\*[^*]+\*\*\s*$", ln) for ln in lines)
    if not has_flat:
        out = []
        for line in lines:
            if line.startswith("# "):
                out.append("###" + line[1:])
            elif line.startswith("## "):
                out.append("###" + line[2:])
            elif line.startswith("### "):
                out.append("####" + line[3:])
            else:
                out.append(line)
        return "\n".join(out)
    out = []
    h_counter = 0
    sub_counter = 0
    for line in lines:
        m = re.match(r"^\d+\. \*\*([^*]+)\*\*\s*$", line)
        if m:
            h_counter += 1
            sub_counter = 0
            num = _ROMAN[h_counter] if h_counter < len(_ROMAN) else str(h_counter)
            out.append(f"### {num}. {m.group(1).strip()}")
            continue
        m = re.match(r"^\d+\. \*([^*]+)\*\.?\s*$", line)
        if m:
            sub_counter += 1
            letter = (
                _LETTERS[sub_counter - 1]
                if sub_counter - 1 < len(_LETTERS)
                else str(sub_counter)
            )
            out.append(f"#### {letter}. {m.group(1).strip()}")
            continue
        m = re.match(r"^\d+\. (.+)$", line)
        if m and h_counter > 0:
            out.append(f"- {m.group(1).strip()}")
            continue
        out.append(line)
    return "\n".join(out)


# ---------- 1. MERGES ----------
# Each merge: output filename, title, blended intro, list of (source, sub-section title, policy#)
MERGES = [
    {
        "out": "02b. Patient Rights — Access, Amendment & Accounting of Disclosures.md",
        "title": "Patient Rights — Access, Amendment & Accounting of Disclosures",
        "merged_codes": "L-003 + L-008 + L-009",
        "intro": (
            "Patients of Millie, Inc. have three rights regarding their Protected Health "
            "Information: the right to inspect and obtain copies of their records, the "
            "right to request amendments to those records, and the right to receive an "
            "accounting of disclosures Millie has made about them. This Policy consolidates "
            "the three rights into a single document while preserving each underlying "
            "procedure verbatim as a sub-section so an auditor can still find the original "
            "policy text by name."
        ),
        "sources": [
            (
                "03k HIPAA - Individual Rights to Access Their Records Policy.md",
                "Right to Access PHI",
                "L-009",
            ),
            (
                "03j HIPAA - Individual Right to Request Amendments to PHI Policy.md",
                "Right to Request Amendments to PHI",
                "L-008",
            ),
            (
                "03a HIPAA- Accounting of Disclosures Policy.md",
                "Accounting of Disclosures",
                "L-003",
            ),
        ],
    },
    {
        "out": "02c. PHI Use, Disclosure, Minimum Necessary & De-Identification.md",
        "title": "PHI Use, Disclosure, Minimum Necessary & De-Identification",
        "merged_codes": "L-002 + L-005 + L-006 + L-010",
        "intro": (
            "These rules govern when and how Millie, Inc. may use, disclose, request, or "
            "de-identify Protected Health Information, including in marketing communications "
            "and Limited Data Set sharing. This Policy consolidates four underlying policies "
            "into a single document; each is preserved verbatim as a sub-section so an "
            "auditor running a HIPAA checklist still finds Marketing, the Minimum Necessary "
            "Rule, the Safe Harbor 18-identifier list, and the legal/public-health "
            "disclosure rules as named sections."
        ),
        "sources": [
            (
                "03v HIPAA - Use and Disclosure of PHI for Various Legal, Public Health and Regulatory Purposes Policy.md",
                "Use & Disclosure of PHI for Legal, Public Health & Regulatory Purposes",
                "L-002",
            ),
            (
                "03m HIPAA - Minimum Necessary Rule Policy.md",
                "Minimum Necessary Rule",
                "L-010",
            ),
            (
                "03e HIPAA - De-Identifying and Re-Identifying PHI and Creation of Limited Data Sets Policy.md",
                "De-Identifying & Re-Identifying PHI + Limited Data Sets",
                "L-005",
            ),
            (
                "03h HIPAA and Marketing Policy.md",
                "Marketing & Patient Communications",
                "L-006",
            ),
        ],
    },
    {
        "out": "03a. Technical Safeguards — Encryption, Passwords, Remote Access & Workstations.md",
        "title": "Technical Safeguards — Encryption, Passwords, Remote Access & Workstations",
        "merged_codes": "IT-001 + IT-002 + IT-005 + IT-006",
        "intro": (
            "These technical safeguards govern Millie's information systems and the "
            "endpoints that access them — encryption, password management, remote access, "
            "and workstation use (including BYOD and mobile device management). This Policy "
            "consolidates four underlying policies into a single document; each is preserved "
            "verbatim as a sub-section, and the Workstation Use sub-section retains the "
            "BYOD/MDM clause added in May 2026 to close SIG M.1.3 / M.1.5 / M.1.6."
        ),
        "sources": [
            (
                "03g HIPAA - Encryption Policy.md",
                "Encryption",
                "IT-005",
            ),
            (
                "03o HIPAA - Password Management Policy.md",
                "Password Management",
                "IT-001",
            ),
            (
                "03p HIPAA - Remote Access Policy.md",
                "Remote Access",
                "IT-006",
            ),
            (
                "03w HIPAA - Workstation Use Policy (1).md",
                "Workstation Use (including BYOD & Mobile Device Management)",
                "IT-002",
            ),
        ],
    },
    {
        "out": "05a. Incident & Breach Response.md",
        "title": "Incident & Breach Response",
        "merged_codes": "L-004 + IT-009 + AWS/Aptible IR",
        "intro": (
            "These rules govern Millie's response to security incidents and breaches "
            "affecting Protected Health Information — from initial reporting through "
            "investigation, containment, regulatory notification, and post-incident review. "
            "This Policy consolidates the general Security Incident Management process, the "
            "HIPAA-specific Breach Notification process, and the AWS / Aptible cloud-incident "
            "playbook into a single document; each is preserved verbatim as a sub-section."
        ),
        "sources": [
            (
                "03s HIPAA - Security Incident Management Policy (2).md",
                "Security Incident Management",
                "IT-009",
            ),
            (
                "03b HIPAA - Breach Notification Policy.md",
                "HIPAA Breach Notification",
                "L-004",
            ),
            (
                "AWS and Aptible Security Incident Management Policy.md",
                "AWS & Aptible Cloud Incident Playbook",
                "(no original Policy #)",
            ),
        ],
    },
]


# ---------- 2. RENAMES (non-merged files) ----------
# Each rename: (old name, new name with prefix)
RENAMES = [
    # 01. Foundational & Governance
    ("Millie Information Security & Data Governance Framework (1).md", "01a. Information Security Framework.md"),
    ("03i HIPAA Definitions Policy.md", "01b. HIPAA Definitions.md"),
    ("03q HIPAA - Risk Management Policy (1).md", "01c. Risk Management Policy.md"),
    ("03r HIPAA - Safeguards Policy.md", "01d. Safeguards Policy.md"),
    # 02. Privacy & Patient Rights — 02a is the misnamed bundle (keep name)
    ("Millie Privacy Policy (1).md", "02a. Privacy Policy.md"),
    # 04. Operations & Continuity
    ("03d HIPAA - Contingency Planning Policy (1).md", "04a. Contingency Planning Policy.md"),
    ("03n HIPAA - Paper Document Management Policy.md", "04b. Paper Document Management Policy.md"),
    ("Millie Clinic COVID Policy.md", "04c. COVID Policy.md"),
    ("Medical Waste Management Plan.md", "04d. Medical Waste Management Plan.md"),
    # 06. Vendor & Software
    ("03c HIPAA - Business Associate Agreement Policy.md", "06a. Business Associate Agreement Policy.md"),
    ("System Development Life Cycle (SDLC) & Asset Lifecycle Policy.md", "06b. SDLC & Asset Lifecycle Policy.md"),
    ("HIPAA - Millie_BAA (for BA Use with Subcontractor).md", "06c. BAA Template (Subcontractor).md"),
    # 07. Reference
    ("Millie Matrix of Platforms, Software Subscriptions, and Access (1).md", "07a. Platform & Subscription Matrix.md"),
    ("03u HIPAA - TEMPLATE - Insurance Authorization and Assignment of Benefits (002).md", "07b. Insurance Authorization Form Template.md"),
    ("ECH Security Assessment Questions (1).md", "07c. ECH Security Assessment Snapshot.md"),
]


def git_mv(old: Path, new: Path) -> None:
    """git mv, falling back to plain mv if old isn't tracked."""
    rel_old = old.relative_to(REPO)
    rel_new = new.relative_to(REPO)
    res = subprocess.run(
        ["git", "mv", str(rel_old), str(rel_new)],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        # Fallback: plain mv
        old.rename(new)


def git_rm(path: Path) -> None:
    rel = path.relative_to(REPO)
    res = subprocess.run(
        ["git", "rm", str(rel)],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        path.unlink(missing_ok=True)


def build_merged(merge: dict) -> None:
    out_path = ROOT / merge["out"]
    parts: list[str] = []

    # Top metadata table
    parts.append(
        f"| **Title**: {merge['title']} | **Merged from Policy #s**: {merge['merged_codes']} |\n"
    )
    parts.append("| --- | --- |\n")
    parts.append(
        "| **Last Revised**: 2026-05-28 (consolidated) | **Source policies preserved verbatim as sub-sections** |\n"
    )
    parts.append("\n")

    # Title + blended intro
    parts.append(f"# {merge['title']}\n\n")
    parts.append(f"{merge['intro']}\n\n")
    parts.append("---\n\n")

    # Each sub-section
    sub_idx = 0
    for src_name, sub_title, policy_num in merge["sources"]:
        src_path = ROOT / src_name
        if not src_path.exists():
            print(f"    MISSING source: {src_path}")
            continue
        sub_idx += 1
        roman = _ROMAN[sub_idx] if sub_idx < len(_ROMAN) else str(sub_idx)
        src_text = src_path.read_text(encoding="utf-8")
        cleaned = strip_artifacts(src_text)
        demoted = demote_to_subsection(cleaned)
        parts.append(f"## {roman}. {sub_title}\n\n")
        parts.append(
            f"*Originally: `{src_name}` (Policy # {policy_num}). Preserved verbatim below.*\n\n"
        )
        parts.append(demoted.strip())
        parts.append("\n\n---\n\n")

    out_path.write_text("".join(parts), encoding="utf-8")
    print(f"  ✓ Wrote {out_path.name} ({out_path.stat().st_size:,} bytes)")

    # Remove the source files (after successful write)
    for src_name, _, _ in merge["sources"]:
        src_path = ROOT / src_name
        if src_path.exists():
            git_rm(src_path)
            print(f"    removed source: {src_name}")


def main() -> None:
    print("=" * 60)
    print("PHASE 1 — Merge 4 consolidated files")
    print("=" * 60)
    for merge in MERGES:
        print(f"\n  Merging into: {merge['out']}")
        build_merged(merge)

    print()
    print("=" * 60)
    print("PHASE 2 — Rename remaining files with category prefixes")
    print("=" * 60)
    for old_name, new_name in RENAMES:
        old_path = ROOT / old_name
        new_path = ROOT / new_name
        if not old_path.exists():
            print(f"  SKIP (not present): {old_name}")
            continue
        if new_path.exists():
            print(f"  SKIP (target exists): {new_name}")
            continue
        git_mv(old_path, new_path)
        print(f"  ✓ {old_name}  →  {new_name}")

    # Add merged files to git
    for merge in MERGES:
        out_path = ROOT / merge["out"]
        if out_path.exists():
            subprocess.run(
                ["git", "add", str(out_path.relative_to(REPO))], cwd=REPO, check=False
            )

    print()
    print("=" * 60)
    print("DONE")
    print("=" * 60)
    final = sorted(p.name for p in ROOT.glob("*.md"))
    print(f"\n{len(final)} files now in 3. Final Word/3.a Final Markdown/:")
    for f in final:
        print(f"  {f}")


if __name__ == "__main__":
    main()
