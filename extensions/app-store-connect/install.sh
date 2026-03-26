#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$HOME/.claude/skills"
AGENT_DIR="$HOME/.claude/agents"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Installing App Store Connect Extension ==="

if [ ! -d "$SKILL_DIR/aso" ]; then
    echo "Error: claude-aso must be installed first."
    exit 1
fi

read -rp "App Store Connect Key ID: " KEY_ID
read -rp "App Store Connect Issuer ID: " ISSUER_ID
read -rp "Path to .p8 private key file: " KEY_PATH

if [ ! -f "$KEY_PATH" ]; then
    echo "Error: Key file not found at $KEY_PATH"
    exit 1
fi

cat >> "$SKILL_DIR/aso/.env" << EOF
ASC_KEY_ID=$KEY_ID
ASC_ISSUER_ID=$ISSUER_ID
ASC_KEY_PATH=$KEY_PATH
EOF
echo "Credentials saved to $SKILL_DIR/aso/.env"

mkdir -p "$SKILL_DIR/aso-asc"
cp "$SCRIPT_DIR/skills/aso-asc/SKILL.md" "$SKILL_DIR/aso-asc/"

cp "$SCRIPT_DIR/agents/aso-asc.md" "$AGENT_DIR/"

cp "$SCRIPT_DIR/scripts/asc_client.py" "$SKILL_DIR/aso/scripts/"

if command -v uv >/dev/null 2>&1 && [ -d "$SKILL_DIR/aso/.venv" ]; then
    uv pip install PyJWT --python "$SKILL_DIR/aso/.venv/bin/python"
else
    pip3 install --user PyJWT
fi

echo "=== App Store Connect Extension installed ==="
echo "Test with: /aso asc metadata <your-app-id>"
