#!/usr/bin/env python3
"""sync-ech-sheet2.py — pull user changes from ECH Sheet2 into coverage_matrix.csv.

The user maintains `ECH Security Docs/ECH Security Assessment Questions - Sheet2.csv`
as the authoritative ECH workbook. They populate `Current Answer`, `Additional Info
Added`, and `Flags/Notes` as new info arrives, and may add new questions / sections.

This script:
  1. Reads Sheet2 as the source of truth for question text + user-populated cells.
  2. Reads the existing `2. Gaps/2.a Gaps Markdown/coverage_matrix.csv` for AI-
     generated analysis columns (Plain English, Coverage, Proposed Answer, Flag
     Risk, Gap Description, Required Fix - *).
  3. Produces an updated coverage_matrix.csv that:
       - has every Sheet2 row (including new ones)
       - preserves Sheet2's column order
       - preserves user-populated cells verbatim
       - keeps AI analysis where unchanged
       - re-generates Proposed Answer for rows where Current Answer or
         Additional Info Added changed (so user's content leads the answer)
       - has FULL analysis (incl. Plain English / Coverage / Proposed Answer
         / Flag Risk / Gap / Fix) for net-new rows
"""

from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SHEET2 = REPO / "ECH Security Docs" / "ECH Security Assessment Questions - Sheet2.csv"
MATRIX = REPO / "2. Gaps" / "2.a Gaps Markdown" / "coverage_matrix.csv"

# Column order in the OUTPUT matches Sheet2 (user's preferred layout).
OUT_COLS = [
    "Questionnaire",
    "Section",
    "Item #",
    "Question",
    "Coverage - AI Provided",
    "Current Answer",
    "Current Status",
    "Additional Info Added",
    "Flags/Notes",
    "Proposed Answer",
    "Plain English",
    "Flag Risk",
    "Gap Description",
    "Required Fix - File",
    "Required Fix - Text",
    "Required Fix - Words",
]

# Cells the user owns and should never be overwritten by AI analysis.
USER_OWNED = {"Current Answer", "Current Status", "Additional Info Added", "Flags/Notes"}

# Hand-authored analysis for the 5 net-new rows the user added.
NEW_ROW_ANALYSIS = {
    ("SIG Lite 2025", "T. Threat Management", "T.1"): {
        "Plain English": "Do you have a written, approved program for finding and fixing security weaknesses (with a named owner)?",
        "Coverage - AI Provided": "Partial",
        "Proposed Answer": "Partial. Operationally Millie is continuously monitored via Tenisi-managed ConnectSecure with scans twice monthly (Patch Tuesday + 2-week follow-up). The `01c. Risk Management Policy` describes annual risk assessments and mitigation, and `06b. SDLC & Asset Lifecycle Policy` §III(d) defines a patch-management SLA. A discretely titled Vulnerability Management Program Policy with named owner and review cadence is not yet on file — same gap as ECH OWASP A06 / SIG N.4.",
        "Flag Risk": "Medium",
        "Gap Description": "Vulnerability scanning is operational, but a stand-alone VM Program Policy with named owner is not documented.",
        "Required Fix - File": "01c. Risk Management Policy.md",
        "Required Fix - Text": "Append 1-paragraph clause: Millie operates a Vulnerability Management Program owned by the Chief Security Officer in coordination with Tenisi. Continuous scanning is performed via ConnectSecure twice monthly (post-Patch Tuesday and 2-week follow-up). Findings are triaged per the SDLC patch SLA (Critical=7d, High=30d, Medium=90d). The program is reviewed annually alongside the security risk assessment.",
    },
    ("SIG Lite 2025", "T. Threat Management", "T.2"): {
        "Plain English": "Do you have a written program for managing cybersecurity risk in your software/hardware supply chain?",
        "Coverage - AI Provided": "Partial",
        "Proposed Answer": "Partial. This duplicates the existing SIG S.32 / S.57 / S.61 / S.80 / S.100 gap — Millie's `01a. Information Security Framework` §11 covers third-party / vendor risk and Nth-party flow-down via BAA, but is not framed as a Cybersecurity Supply Chain Risk Management (C-SCRM) program with explicit strategy/objectives/owner. Same one-paragraph addition to Framework §11 closes both.",
        "Flag Risk": "Medium",
        "Gap Description": "Third-party risk mgmt exists but is not framed as C-SCRM. Same fix as SIG S.32.",
        "Required Fix - File": "01a. Information Security Framework.md",
        "Required Fix - Text": "(Same C-SCRM paragraph proposed for SIG S.32 — see that row. One addition closes T.2 + S.32 + S.57 + S.61 + S.80 + S.100.)",
    },
    ("SIG Lite 2025", "U. Server Security", "U.1"): {
        "Plain English": "Do you have any in-house servers that hold customer / patient data?",
        "Coverage - AI Provided": "Full",
        "Proposed Answer": "No on-premise servers. Millie's stack is fully cloud-native (Aptible-managed application + databases on AWS, with Cloudflare DNS/CDN and Google Workspace for staff). See `01a. Information Security Framework` §5 (Data Storage & Protection) and `04a. Contingency Planning Policy`. All in-scope data lives in vendor-managed cloud services.",
        "Flag Risk": "Low",
        "Gap Description": "—",
        "Required Fix - File": "N/A",
        "Required Fix - Text": "",
    },
    ("SIG Lite 2025", "V. Cloud Services", "V.1"): {
        "Plain English": "Do *you* offer cloud-hosting services to other companies?",
        "Coverage - AI Provided": "N/A",
        "Proposed Answer": "No. Millie does not provide cloud-hosting services to third parties. Millie is a consumer of cloud services (Aptible, AWS, Cloudflare, Google Workspace) for its own clinical and corporate systems. See `01a. Information Security Framework` §5 and the `Supporting Sources/Millie Matrix of Platforms, Software Subscriptions, and Access` for the vendor / SaaS inventory.",
        "Flag Risk": "None",
        "Gap Description": "—",
        "Required Fix - File": "N/A",
        "Required Fix - Text": "",
    },
    ("SIG Lite 2025", "V. Cloud Services", "V.2"): {
        "Plain English": "Can you share independent audit reports (like SOC 2) from your cloud hosting provider?",
        "Coverage - AI Provided": "N/A",
        "Proposed Answer": "N/A — Millie does not provide cloud-hosting services (see V.1). Millie's own upstream cloud providers (AWS, Aptible, Cloudflare, Google Workspace) maintain SOC 2 / ISO 27001 / HIPAA-compliant attestations that are referenced where required in the `06a. Business Associate Agreement Policy` vendor review.",
        "Flag Risk": "None",
        "Gap Description": "—",
        "Required Fix - File": "N/A",
        "Required Fix - Text": "",
    },
}


def main() -> None:
    # Read Sheet2 (user-authoritative source)
    with SHEET2.open(newline="", encoding="utf-8") as f:
        s_rows = list(csv.reader(f))
    s_h = {c: i for i, c in enumerate(s_rows[0])}

    # Read existing matrix (AI-generated analysis)
    with MATRIX.open(newline="", encoding="utf-8") as f:
        m_rows = list(csv.reader(f))
    m_h = {c: i for i, c in enumerate(m_rows[0])}
    m_by_key = {
        (r[m_h["Questionnaire"]], r[m_h["Section"]], r[m_h["Item #"]]): r
        for r in m_rows[1:]
    }

    out_data = []
    stats = {
        "carried_over": 0,
        "user_input_changed_proposed_regen": 0,
        "new_row_full_analysis": 0,
        "user_input_changed_no_propose_change": 0,
    }

    for s_row in s_rows[1:]:
        key = (s_row[s_h["Questionnaire"]], s_row[s_h["Section"]], s_row[s_h["Item #"]])

        # --- NET-NEW row: hand-authored analysis ---
        if key not in m_by_key:
            new_analysis = NEW_ROW_ANALYSIS.get(key)
            if not new_analysis:
                # Unknown new row — fall back to copying Sheet2 cells verbatim
                # and flagging for review.
                new_analysis = {
                    "Plain English": "",
                    "Coverage - AI Provided": "",
                    "Proposed Answer": "(NEEDS ANALYSIS — new row added in Sheet2 without a hand-authored analysis entry; re-run scripts/sync-ech-sheet2.py with this row added to NEW_ROW_ANALYSIS.)",
                    "Flag Risk": "",
                    "Gap Description": "",
                    "Required Fix - File": "",
                    "Required Fix - Text": "",
                }

            out_row = {col: "" for col in OUT_COLS}
            # Copy identity + Sheet2 user-owned cells verbatim
            out_row["Questionnaire"] = s_row[s_h["Questionnaire"]]
            out_row["Section"] = s_row[s_h["Section"]]
            out_row["Item #"] = s_row[s_h["Item #"]]
            out_row["Question"] = s_row[s_h["Question"]]
            for col in USER_OWNED:
                out_row[col] = s_row[s_h[col]]
            # Apply analysis
            for col, val in new_analysis.items():
                out_row[col] = val
            fix_text = out_row["Required Fix - Text"]
            out_row["Required Fix - Words"] = str(len(fix_text.split())) if fix_text else "0"
            out_data.append([out_row[c] for c in OUT_COLS])
            stats["new_row_full_analysis"] += 1
            continue

        # --- EXISTING row: carry analysis forward, refresh user-owned cells ---
        m_r = m_by_key[key]
        out_row = {}
        for col in OUT_COLS:
            if col in USER_OWNED:
                # User-owned: take from Sheet2 (current source of truth)
                out_row[col] = s_row[s_h[col]]
            elif col in ("Questionnaire", "Section", "Item #", "Question"):
                # Identity: take from Sheet2 (in case user edited question text)
                out_row[col] = s_row[s_h[col]]
            else:
                # AI analysis: carry from matrix
                out_row[col] = m_r[m_h[col]]

        # If Current Answer or Additional Info Added changed in a substantive way,
        # regenerate Proposed Answer so the user's new content leads.
        s_ca = s_row[s_h["Current Answer"]].strip()
        m_ca = m_r[m_h["Current Answer"]].strip()
        s_aia = s_row[s_h["Additional Info Added"]].strip()
        m_aia = m_r[m_h["Additional Info Added"]].strip()
        proposed = out_row["Proposed Answer"]

        regenerated = False
        if s_aia and s_aia != m_aia:
            # New Additional Info Added: prepend if it's not already in the proposed answer
            if s_aia[:60].lower() not in proposed.lower():
                out_row["Proposed Answer"] = f"{s_aia} {proposed}".strip()
                regenerated = True
        elif s_ca and s_ca != m_ca:
            # New Current Answer: prepend "Yes." / "No." / value if not already at the start
            ca_short = s_ca.rstrip(".")
            if not proposed.lower().startswith(ca_short.lower()[:20]):
                # Only prepend if it's a substantive lead (not just "Yes" when proposed already affirms)
                if ca_short.lower() not in ("yes", "no") or not (
                    proposed.lower().startswith("yes") or proposed.lower().startswith("no")
                ):
                    out_row["Proposed Answer"] = f"{ca_short}. {proposed}".strip()
                    regenerated = True

        out_data.append([out_row[c] for c in OUT_COLS])
        if regenerated:
            stats["user_input_changed_proposed_regen"] += 1
        elif s_ca != m_ca or s_aia != m_aia or s_row[s_h["Flags/Notes"]] != m_r[m_h["Flags/Notes"]]:
            stats["user_input_changed_no_propose_change"] += 1
        else:
            stats["carried_over"] += 1

    # Write the updated matrix
    with MATRIX.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(OUT_COLS)
        w.writerows(out_data)

    print(f"Wrote {MATRIX.relative_to(REPO)}")
    print(f"  Total rows: {len(out_data)}")
    print(f"  Carried over unchanged:                 {stats['carried_over']}")
    print(f"  User-input changed (no propose update): {stats['user_input_changed_no_propose_change']}")
    print(f"  User-input changed (propose regen):     {stats['user_input_changed_proposed_regen']}")
    print(f"  Net-new rows (full analysis):           {stats['new_row_full_analysis']}")


if __name__ == "__main__":
    main()
