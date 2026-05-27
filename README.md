---
title: "Millie Policies"
last_reviewed: 2026-05-26
owner: "Privacy Officer + Security Officer (joint)"
---

# Millie Policies

This repository is the source of truth for Millie's HIPAA and information security policies. The current pass (May 2026) is structured as three numbered folders so the diff between the originals and the final policies is obvious:

| Folder | Purpose |
|---|---|
| **`1. original_docs_markdown/`** | The original Millie policies, converted from `.doc` / `.docx` / `.pdf` / `.xlsx` into Markdown **with no editorial changes**. This is the baseline. Don't edit. |
| **`2. gaps_for_ech/`** | Section-by-section gap analysis against the ECH Security Assessment. Categorizes each section of every questionnaire as **No Gap**, **N/A** (doesn't need to live in a policy), or **Gaps** (real coverage gap; needs to be added to a policy). Minimal — does not enumerate every row. |
| **`3. final_policies/`** | The final policy set. Starts as a copy of folder 1 and is edited from there: duplicate versions removed, files combined where natural, only ECH-required content added. `CHANGES.md` inside summarizes every structural move. |

**Repo-layout supporting folders:**

- **`Policy Docs/`** — the original `.doc` / `.docx` / `.pdf` / `.xlsx` source files. Don't edit; they're the immutable inputs that folder 1 was generated from.
- **`policy_docs_word/`** — exec-facing bundle. For each file in folder 3: if the policy is unchanged from the original, this folder gets the *original* `.docx` (or `.xlsx` / `.pdf`) from `Policy Docs/` — perfect Word formatting preserved. For the 3 policies that have ECH-driven clauses appended, this folder gets a pandoc-converted `.docx` (readable Word doc; styling not identical to the original). `CHANGES.docx` is pandoc-converted from `3. final_policies/CHANGES.md`. Regenerate after any policy edit with `./scripts/build-word-docs.py`. Don't edit — your changes get overwritten on the next rebuild.
- **`scripts/build-word-docs.py`** — the re-runnable build script (Python; uses pandoc for the converted files, plain copy for the unchanged ones). Auto-installs pandoc via Homebrew if missing.
- **`ECH Security Assessment Questions - Questions.csv`** — the questionnaire that drives the gap analysis.
- **`_old_attempt/`** — a previous consolidation pass that diverged too far from the originals (rewrote in a fresh template, broke Word formatting, added a lot of structure that ECH wasn't actually asking for). Preserved for reference; not authoritative.

## Working philosophy

- **Fewer documents is better.** Each policy that exists is a quarterly/yearly review obligation. Don't add a policy just because the topic could exist.
- **Add only what's required.** If ECH / SIG / OWASP / SOC / HIPAA is not asking for a thing to be in a policy, it does not need to be in a policy. The originals were written for HIPAA's required policies; we extend only where ECH explicitly asks for more.
- **Preserve the originals' voice and structure** when editing folder 3. The cleanest diff is "what we added," not "what we rewrote."

## How to use this repo

1. Treat `3. final_policies/` as authoritative for any policy question.
2. To see *why* a policy looks the way it does, diff the same filename between folder 1 and folder 3, then read `3. final_policies/CHANGES.md`.
3. When new ECH gaps are surfaced (next vendor questionnaire, new audit), update `2. gaps_for_ech/` first, then make the minimum edit to folder 3 needed to close them. Don't grow the policy count unless ECH forces it.
