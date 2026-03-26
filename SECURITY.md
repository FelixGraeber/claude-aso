# Security Policy

## Supported Versions

Security fixes are applied on `main`.

## Reporting a Vulnerability

Do not open a public GitHub issue for a suspected vulnerability.

Report it privately to the maintainer with:
- a clear description of the issue
- affected files or commands
- reproduction steps or proof of concept
- impact assessment

The goal is to acknowledge reports promptly, confirm severity, and ship a fix before public disclosure when practical.

## Secret Handling

- Prefer environment variables over checked-in configuration files.
- If you use the optional ASO env file, keep it outside the repository and restrict it to the current user (`0600` on Unix-like systems).
- Never commit API keys, `.p8` files, or copied credentials into this repository.

## Security Checks

This repository uses:
- CI tests for parser and policy regressions
- dependency auditing in GitHub Actions
- Dependabot for dependency and workflow update visibility
