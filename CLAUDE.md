# Claude ASO — App Store Optimization for Claude Code

## Overview

Comprehensive ASO skill for iOS App Store and Google Play. 13 sub-skills, 9 parallel subagents, extensible API integrations. Follows the claude-seo 3-layer architecture (directive → orchestration → execution).

## Architecture

```
aso/SKILL.md          → Main orchestrator (entry point, routing, scoring)
skills/aso-*/SKILL.md → 13 specialized sub-skills (independently invocable)
agents/aso-*.md       → 9 parallel subagents (spawned during audits)
references/*.md       → On-demand knowledge (metadata specs, quality gates)
scripts/*.py          → Python utilities (fetch, parse, validate, analyze)
extensions/           → Optional API integrations (AppTweak, App Store Connect)
```

## Commands

All commands start with `/aso`. Run `/aso` for the full command table.

## Development Rules

- SKILL.md files: <500 lines, <5000 tokens
- Reference files: focused, <200 lines
- Scripts: CLI interface with `--json` output, docstrings
- Naming: kebab-case for directories, snake_case for Python
- Agents: invoked via Agent tool, never via Bash
- Python: use uv, deps in pyproject.toml
- Platform detection: auto-detect iOS vs Android from app ID format

## Key Principles

1. **Platform-aware**: Every analysis distinguishes iOS vs Android rules
2. **Parallel execution**: Full audits spawn 7-9 subagents simultaneously
3. **Progressive disclosure**: Metadata always loaded, references on demand
4. **Quality gates**: Hard rules prevent bad recommendations (no keyword stuffing, respect char limits)
