#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="claude-aso-audit-skill"
SKILL_DIR="${SKILLS_HOME:-$HOME/.claude/skills}"
AGENT_DIR="${AGENTS_HOME:-$HOME/.claude/agents}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Installing $SKILL_NAME ==="

# Check prerequisites
command -v python3 >/dev/null 2>&1 || { echo "Error: python3 required"; exit 1; }

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PYTHON_MAJOR=$(echo "$PYTHON_VERSION" | cut -d. -f1)
PYTHON_MINOR=$(echo "$PYTHON_VERSION" | cut -d. -f2)
if [ "$PYTHON_MAJOR" -lt 3 ] || { [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 12 ]; }; then
    echo "Error: Python 3.12+ required (found $PYTHON_VERSION)"
    exit 1
fi

# Create directories
mkdir -p "$SKILL_DIR" "$AGENT_DIR"

# Copy main skill
echo "Installing main skill..."
mkdir -p "$SKILL_DIR/aso"
cp "$SCRIPT_DIR/aso/SKILL.md" "$SKILL_DIR/aso/"

# Copy sub-skills
echo "Installing sub-skills..."
for skill_dir in "$SCRIPT_DIR"/skills/aso-*/; do
    skill_name=$(basename "$skill_dir")
    mkdir -p "$SKILL_DIR/$skill_name"
    cp -r "$skill_dir"/* "$SKILL_DIR/$skill_name/"
done

# Copy agents
echo "Installing agents..."
cp "$SCRIPT_DIR"/agents/aso-*.md "$AGENT_DIR/"

# Copy references
echo "Installing references..."
mkdir -p "$SKILL_DIR/aso/references"
cp "$SCRIPT_DIR"/references/*.md "$SKILL_DIR/aso/references/"

# Copy scripts
echo "Installing scripts..."
mkdir -p "$SKILL_DIR/aso/scripts"
cp "$SCRIPT_DIR"/scripts/*.py "$SKILL_DIR/aso/scripts/"

# Install Python dependencies
echo "Installing Python dependencies..."
if command -v uv >/dev/null 2>&1; then
    cd "$SKILL_DIR/aso"
    uv venv .venv 2>/dev/null || true
    uv pip install -r "$SCRIPT_DIR/requirements.txt" --python .venv/bin/python
else
    pip3 install --user -r "$SCRIPT_DIR/requirements.txt"
fi

echo ""
echo "=== $SKILL_NAME installed successfully ==="
echo ""
echo "Usage: Type /aso in your skill-compatible agent to get started"
echo "       /aso audit               Auto-detect local project metadata"
echo "       /aso audit <app-id>      Audit a live listing or competitor"
echo "       /aso keywords <seeds>    Keyword research"
echo "       /aso metadata             Optimize local metadata"
echo ""
echo "Optional: Install visual analysis support:"
echo "  pip install 'playwright>=1.50.0' 'Pillow>=11.0.0'"
echo "  playwright install chromium"
