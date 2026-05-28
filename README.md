---
title: "Millie Policies"
last_reviewed: 2026-05-28
owner: "Privacy Officer + Security Officer (joint)"
---

# Millie Policies

This repository is the source of truth for Millie's HIPAA and information security policies. Three numbered folders, each with a Word-friendly top level for non-technical reviewers and a Markdown sub-folder for the underlying source.

## What's where

| Folder | What's in it (top level) | What's in the sub-folder |
|---|---|---|
| **`1. Original Docs (Word)/`** | The original Millie policies as `.doc` / `.docx` / `.pdf` / `.xlsx` files — exactly as authored. **Don't edit.** | `1.a Original Converted to MD/` — automatic Markdown conversions of the originals with no editorial changes. The baseline against which folder 3 is diffed. |
| **`2. Gaps/`** | The ECH gap analysis as Word docs (`SUMMARY.docx`, `GAPS.docx`, `ROW-LEVEL-VERIFICATION.docx`, `NA-justifications.docx`, `COVERAGE-CSV-SUMMARY.docx`) plus the row-by-row matrix as Excel (`coverage_matrix.xlsx`). **Open in Word / Excel.** | `2.a Gaps Markdown/` — the editable Markdown / CSV source the Word/Excel files are generated from. |
| **`Current Policies (MM-DD-YYYY Generated)/`** | The **final policy set** as Word / Excel / PDF — what an exec or reviewer should download. Starts as a copy of folder 1 and is edited from there: duplicate versions removed, files combined where natural, only ECH-required content added. **Don't edit these directly; regenerate via the build script.** | `3.a Final Markdown/` — the editable Markdown source for the final policies. This is what you actually edit when a policy changes; `CHANGES.md` inside summarizes every structural move vs the originals. |

After editing anything in a Markdown sub-folder, run `./scripts/build-word-docs.py` to regenerate the Word/Excel files at the top level of folder 2 and folder 3.

## Other repo contents

- **`scripts/build-word-docs.py`** — the re-runnable build script. Auto-installs pandoc via Homebrew on first run.
- **`ECH Security Assessment Questions - Questions.csv`** — the original 182-row ECH questionnaire (immutable input).
- **`ECH Security Assessment Questions - Sheet2.csv`** — your expanded 212-row workbook with your own answers in the "Current Answer" and "Additional Info Added" columns; the gap analysis is generated from this.
- **`_old_attempt/`** — a previous consolidation pass that diverged too far from the originals (rewrote in a fresh template, broke Word formatting, added a lot of structure that ECH wasn't actually asking for). Preserved for reference only; not authoritative.

## Working philosophy

- **Fewer documents is better.** Each policy that exists is a quarterly/yearly review obligation. Don't add a policy just because the topic could exist.
- **Add only what's required.** If ECH / SIG / OWASP / SOC / HIPAA is not asking for a thing to be in a policy, it does not need to be in a policy. The originals were written for HIPAA's required policies; we extend only where ECH explicitly asks for more.
- **Preserve the originals' voice and structure** when editing folder 3. The cleanest diff is "what we added," not "what we rewrote."

## How to use this repo

**If you're a reviewer / exec:** open the Word files in `Current Policies (MM-DD-YYYY Generated)/` and the Word/Excel files in `2. Gaps/`. You can ignore everything else.

**If you're maintaining the policies:**

1. Treat `Current Policies (MM-DD-YYYY Generated)/3.a Final Markdown/` as the authoritative source for any policy edit.
2. To see *why* a policy looks the way it does, diff the same filename between `1. Original Docs (Word)/1.a Original Converted to MD/` and `Current Policies (MM-DD-YYYY Generated)/3.a Final Markdown/`, then read the `CHANGES.md` next to the final markdown.
3. When new ECH gaps are surfaced (next vendor questionnaire, new audit), update `2. Gaps/2.a Gaps Markdown/` first, then make the minimum edit to `Current Policies (MM-DD-YYYY Generated)/3.a Final Markdown/` needed to close them. Don't grow the policy count unless ECH forces it.
4. After any edit, run `./scripts/build-word-docs.py` to regenerate the Word/Excel files. Commit the markdown changes and the regenerated Word output together.

## Quick-start for execs

Drag `2. Gaps/` and `Current Policies (MM-DD-YYYY Generated)/` into Google Drive — each `.docx` will open as a Google Doc, each `.xlsx` as a Google Sheet. Or just open the files directly in Word / Excel.
