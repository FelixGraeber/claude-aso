# Installation

## Prerequisites

- Python 3.12+
- A skill-compatible agent runtime
- Git

## Quick Install (Unix/macOS)

```bash
git clone https://github.com/felixgraeber/claude-aso-audit-skill.git
cd claude-aso-audit-skill
bash install.sh
```

By default the installer uses `~/.claude/skills` and `~/.claude/agents`. Override them if your runtime uses different directories:

```bash
SKILLS_HOME="$HOME/.codex/skills" AGENTS_HOME="$HOME/.codex/agents" bash install.sh
```

## Quick Install (Windows)

```powershell
git clone https://github.com/felixgraeber/claude-aso-audit-skill.git
cd claude-aso-audit-skill
.\install.ps1
```

## What the installer does

1. Checks Python 3.12+ is available
2. Creates the configured skills and agents directories
3. Copies main skill, sub-skills, agents, references, and scripts
4. Installs Python dependencies (beautifulsoup4, requests, lxml, urllib3)
5. Optionally installs Playwright for screenshot analysis

## Verify Installation

In your agent runtime, invoke:
```
/aso
```

You should see the command table.

## Optional: Visual Analysis

For screenshot capture and analysis:
```bash
pip install 'playwright>=1.50.0' 'Pillow>=11.0.0'
playwright install chromium
```

## Optional: Extensions

### AppTweak (live keyword data)
```bash
bash extensions/apptweak/install.sh
```
Requires AppTweak API key (Pro plan, $69+/month).

### App Store Connect (Apple API)
```bash
bash extensions/app-store-connect/install.sh
```
Requires Apple Developer Program membership and API key.

## Directory Structure After Install

```
<skills-home parent>/
├── skills/
│   ├── aso/              # Main skill + references + scripts
│   ├── aso-audit/        # Sub-skills
│   ├── aso-keywords/
│   ├── aso-metadata/
│   └── ...
└── agents/
    ├── aso-keywords.md   # Agents
    ├── aso-metadata.md
    └── ...
```

## Troubleshooting

- **Skills not appearing**: Verify files are in your configured skills and agents directories
- **Python errors**: Ensure Python 3.12+ is installed and dependencies are available
- **Fetch errors**: Check network connectivity and app ID format
