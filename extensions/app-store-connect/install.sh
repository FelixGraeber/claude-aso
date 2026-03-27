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

echo "=== Installing App Store Connect Extension ==="

if [ ! -d "$SKILL_DIR/aso" ]; then
    echo "Error: claude-aso-audit-skill must be installed first."
    exit 1
fi

read -rp "App Store Connect Key ID: " KEY_ID
read -rp "App Store Connect Issuer ID: " ISSUER_ID
read -rp "Path to .p8 private key file: " KEY_PATH

if [ ! -f "$KEY_PATH" ]; then
    echo "Error: Key file not found at $KEY_PATH"
    exit 1
fi

mkdir -p "$(dirname "$ENV_FILE")"
upsert_env_var "ASC_KEY_ID" "$KEY_ID"
upsert_env_var "ASC_ISSUER_ID" "$ISSUER_ID"
upsert_env_var "ASC_KEY_PATH" "$KEY_PATH"
echo "Credentials saved to $ENV_FILE"

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
