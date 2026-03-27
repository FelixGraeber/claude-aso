#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="${SKILLS_HOME:-$HOME/.claude/skills}"
AGENT_DIR="${AGENTS_HOME:-$HOME/.claude/agents}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ENV_FILE="${ASO_ENV_FILE:-$SKILL_DIR/aso/.env}"

upsert_env_var() {
    local key="$1"
    local value="$2"
    touch "$ENV_FILE"
    chmod 600 "$ENV_FILE"
    if grep -q "^${key}=" "$ENV_FILE"; then
        python3 - "$ENV_FILE" "$key" "$value" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
key = sys.argv[2]
value = sys.argv[3]
lines = path.read_text().splitlines()
updated = []
replaced = False
for line in lines:
    if line.startswith(f"{key}="):
        updated.append(f"{key}={value}")
        replaced = True
    else:
        updated.append(line)
if not replaced:
    updated.append(f"{key}={value}")
path.write_text("\n".join(updated) + "\n")
PY
    else
        printf '%s=%s\n' "$key" "$value" >> "$ENV_FILE"
    fi
}

echo "=== Installing AppTweak Extension ==="

if [ ! -d "$SKILL_DIR/aso" ]; then
    echo "Error: claude-aso-audit-skill must be installed first. Run install.sh from the root directory."
    exit 1
fi

read -rsp "Enter your AppTweak API key: " API_KEY
echo
if [ -z "$API_KEY" ]; then
    echo "Error: API key is required"
    exit 1
fi

mkdir -p "$(dirname "$ENV_FILE")"
upsert_env_var "APPTWEAK_API_KEY" "$API_KEY"
echo "API key saved to $ENV_FILE"

mkdir -p "$SKILL_DIR/aso-apptweak"
cp "$SCRIPT_DIR/skills/aso-apptweak/SKILL.md" "$SKILL_DIR/aso-apptweak/"

cp "$SCRIPT_DIR/agents/aso-apptweak.md" "$AGENT_DIR/"

cp "$SCRIPT_DIR/scripts/apptweak_client.py" "$SKILL_DIR/aso/scripts/"

echo "=== AppTweak Extension installed ==="
echo "Test with: /aso apptweak keywords 'fitness tracker'"
