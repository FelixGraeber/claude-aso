#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$HOME/.claude/skills"
AGENT_DIR="$HOME/.claude/agents"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Installing AppTweak Extension ==="

if [ ! -d "$SKILL_DIR/aso" ]; then
    echo "Error: claude-aso must be installed first. Run install.sh from the root directory."
    exit 1
fi

read -rp "Enter your AppTweak API key: " API_KEY
if [ -z "$API_KEY" ]; then
    echo "Error: API key is required"
    exit 1
fi

echo "APPTWEAK_API_KEY=$API_KEY" >> "$SKILL_DIR/aso/.env"
echo "API key saved to $SKILL_DIR/aso/.env"

mkdir -p "$SKILL_DIR/aso-apptweak"
cp "$SCRIPT_DIR/skills/aso-apptweak/SKILL.md" "$SKILL_DIR/aso-apptweak/"

cp "$SCRIPT_DIR/agents/aso-apptweak.md" "$AGENT_DIR/"

cp "$SCRIPT_DIR/scripts/apptweak_client.py" "$SKILL_DIR/aso/scripts/"

echo "=== AppTweak Extension installed ==="
echo "Test with: /aso apptweak keywords 'fitness tracker'"
