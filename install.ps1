$ErrorActionPreference = "Stop"

$SkillName = "claude-aso"
$SkillDir = if ($env:SKILLS_HOME) { $env:SKILLS_HOME } else { "$env:USERPROFILE\.claude\skills" }
$AgentDir = if ($env:AGENTS_HOME) { $env:AGENTS_HOME } else { "$env:USERPROFILE\.claude\agents" }
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "=== Installing $SkillName ==="

# Check prerequisites
$pythonVersion = python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>$null
if (-not $pythonVersion) {
    Write-Error "Python 3.12+ required"
    exit 1
}
$pythonMajor, $pythonMinor = $pythonVersion.Split(".")
if ([int]$pythonMajor -lt 3 -or ([int]$pythonMajor -eq 3 -and [int]$pythonMinor -lt 12)) {
    Write-Error "Python 3.12+ required (found $pythonVersion)"
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
python -m pip install --user -r "$ScriptDir\requirements.txt"

Write-Host ""
Write-Host "=== $SkillName installed successfully ==="
Write-Host ""
Write-Host "Usage: Type /aso in your skill-compatible agent to get started"
