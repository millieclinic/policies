#!/usr/bin/env bash
# build-word-docs.sh — convert all Millie policy markdown files into .docx for exec viewing.
#
# Output: policy_docs_word/  — one .docx per source .md.
# Execs can open these directly in Word, or drag the folder into Google Drive
# and Drive will auto-convert each .docx into a native Google Doc.
#
# Re-run any time policies change.

set -euo pipefail

cd "$(dirname "$0")/.."  # repo root

# ---------- 1. Ensure pandoc is available ----------
if ! command -v pandoc >/dev/null 2>&1; then
  echo "Pandoc not found; attempting to install via Homebrew..."
  if ! command -v brew >/dev/null 2>&1; then
    echo "ERROR: Homebrew not found. Install pandoc manually:" >&2
    echo "  https://pandoc.org/installing.html" >&2
    exit 1
  fi
  brew install pandoc
fi

# ---------- 2. Prepare output folder ----------
OUT_DIR="policy_docs_word"
mkdir -p "$OUT_DIR"
rm -f "$OUT_DIR"/*.docx  # always clean rebuild — keeps the folder authoritative

# ---------- 3. Files to convert ----------
# 13 active policies + 4 root summary docs = 17 files.
# Intentional skips: New Policy Docs/_archive/ (historical), New Policy Docs/forms/
# (templates), New Policy Docs/PATIENT-NOTICE-TODO.md (placeholder TODO).
FILES=(
  "README.md"
  "TODO.md"
  "POLICY-VS-QUESTIONNAIRE-MAPPING.md"
  "CONSOLIDATION-PROPOSAL.md"
  "New Policy Docs/governance-and-risk-management.md"
  "New Policy Docs/phi-use-and-disclosure.md"
  "New Policy Docs/patient-rights.md"
  "New Policy Docs/technical-safeguards.md"
  "New Policy Docs/operational-safeguards.md"
  "New Policy Docs/incident-and-breach-response.md"
  "New Policy Docs/vendor-and-business-associates.md"
  "New Policy Docs/acceptable-use-and-byod.md"
  "New Policy Docs/network-and-cloud-security.md"
  "New Policy Docs/ai-and-ml-governance.md"
  "New Policy Docs/sdlc-and-asset-lifecycle.md"
  "New Policy Docs/hipaa-definitions.md"
  "New Policy Docs/platform-and-access-matrix.md"
)

# ---------- 4. Convert each file ----------
count=0
for src in "${FILES[@]}"; do
  if [[ ! -f "$src" ]]; then
    echo "  SKIP (missing): $src" >&2
    continue
  fi

  base="$(basename "$src" .md)"
  dst="$OUT_DIR/${base}.docx"

  # Pre-process: rewrite intra-repo .md links to .docx so cross-references
  # survive when execs read the converted docs.
  pre_processed="$(mktemp -t policy-md.XXXXXX)"
  trap 'rm -f "$pre_processed"' EXIT
  sed -E 's|\]\(([^)]+)\.md([)#])|](\1.docx\2|g' "$src" > "$pre_processed"

  pandoc "$pre_processed" \
    --from markdown \
    --to docx \
    --standalone \
    --toc --toc-depth=3 \
    --metadata title="$base" \
    -o "$dst"

  size=$(wc -c < "$dst" | tr -d ' ')
  printf "  ✓ %-55s %s bytes\n" "$dst" "$size"
  rm -f "$pre_processed"
  count=$((count + 1))
done

echo ""
echo "Done. ${count} .docx files written to ${OUT_DIR}/"
echo ""
echo "Share with execs:"
echo "  • Email / Slack — attach individual .docx files; open in Word."
echo "  • Google Drive — drag the entire ${OUT_DIR}/ folder into Drive;"
echo "    each .docx auto-converts to a native Google Doc on first open."
