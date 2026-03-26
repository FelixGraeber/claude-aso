$ErrorActionPreference = "Stop"

$SkillName = "claude-aso"
$SkillDir = "$env:USERPROFILE\.claude\skills"
$AgentDir = "$env:USERPROFILE\.claude\agents"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "=== Installing $SkillName ==="

# Check prerequisites
$pythonVersion = python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>$null
if (-not $pythonVersion) {
    Write-Error "Python 3.12+ required"
    exit 1
}

# Create directories
New-Item -ItemType Directory -Force -Path $SkillDir | Out-Null
New-Item -ItemType Directory -Force -Path $AgentDir | Out-Null

# Copy main skill
Write-Host "Installing main skill..."
New-Item -ItemType Directory -Force -Path "$SkillDir\aso" | Out-Null
Copy-Item "$ScriptDir\aso\SKILL.md" "$SkillDir\aso\"

# Copy sub-skills
Write-Host "Installing sub-skills..."
Get-ChildItem "$ScriptDir\skills\aso-*" -Directory | ForEach-Object {
    $dest = "$SkillDir\$($_.Name)"
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item "$($_.FullName)\*" $dest -Recurse -Force
}

# Copy agents
Write-Host "Installing agents..."
Copy-Item "$ScriptDir\agents\aso-*.md" $AgentDir

# Copy references
Write-Host "Installing references..."
New-Item -ItemType Directory -Force -Path "$SkillDir\aso\references" | Out-Null
Copy-Item "$ScriptDir\references\*.md" "$SkillDir\aso\references\"

# Copy scripts
Write-Host "Installing scripts..."
New-Item -ItemType Directory -Force -Path "$SkillDir\aso\scripts" | Out-Null
Copy-Item "$ScriptDir\scripts\*.py" "$SkillDir\aso\scripts\"

# Install Python dependencies
Write-Host "Installing Python dependencies..."
pip3 install --user -r "$ScriptDir\requirements.txt"

Write-Host ""
Write-Host "=== $SkillName installed successfully ==="
Write-Host ""
Write-Host "Usage: Type /aso in Claude Code to get started"
