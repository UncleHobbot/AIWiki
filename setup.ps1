#Requires -Version 5.1
<#
.SYNOPSIS
    LLM Wiki — first-time setup script for Windows.

.DESCRIPTION
    Creates the full project directory tree, checks prerequisites,
    installs Python dependencies, and scaffolds the .env file.
    Run from the llm-wiki project root.

.EXAMPLE
    # Allow script execution if needed (run once as Administrator):
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

    # Then run setup:
    .\setup.ps1

.EXAMPLE
    # Skip Python dependency install (directories + .env only):
    .\setup.ps1 -SkipPip

.EXAMPLE
    # Force recreate .env even if one already exists:
    .\setup.ps1 -ForceEnv
#>

[CmdletBinding()]
param(
    [switch] $SkipPip,
    [switch] $ForceEnv,
    [switch] $SkipChecks
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# ── Colour helpers ─────────────────────────────────────────────────────────────

function Write-Header([string]$Text) {
    Write-Host ""
    Write-Host "  $Text" -ForegroundColor Cyan
    Write-Host "  $('─' * $Text.Length)" -ForegroundColor DarkCyan
}

function Write-Ok([string]$Text)   { Write-Host "  ✓  $Text" -ForegroundColor Green }
function Write-Warn([string]$Text) { Write-Host "  ⚠  $Text" -ForegroundColor Yellow }
function Write-Fail([string]$Text) { Write-Host "  ✗  $Text" -ForegroundColor Red }
function Write-Info([string]$Text) { Write-Host "  ·  $Text" -ForegroundColor Gray }
function Write-Step([string]$Text) { Write-Host "  »  $Text" -ForegroundColor White }

# ── Banner ─────────────────────────────────────────────────────────────────────

Write-Host ""
Write-Host " ╔══════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host " ║          LLM Wiki  —  Setup  (Windows)          ║" -ForegroundColor Cyan
Write-Host " ║   Personal AI knowledge base · Claude Code       ║" -ForegroundColor DarkCyan
Write-Host " ╚══════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# ── Confirm working directory ──────────────────────────────────────────────────

Write-Header "Working directory"
$ProjectRoot = $PSScriptRoot   # folder where setup.ps1 lives

if (-not (Test-Path (Join-Path $ProjectRoot 'CLAUDE.md'))) {
    Write-Fail "CLAUDE.md not found in: $ProjectRoot"
    Write-Info "Run this script from the llm-wiki project root."
    exit 1
}
Write-Ok $ProjectRoot
Set-Location $ProjectRoot

# ── Prerequisite checks ────────────────────────────────────────────────────────

if (-not $SkipChecks) {
    Write-Header "Checking prerequisites"

    # PowerShell version
    $psVer = $PSVersionTable.PSVersion
    if ($psVer.Major -ge 7) {
        Write-Ok "PowerShell $psVer (pwsh)"
    } elseif ($psVer.Major -eq 5) {
        Write-Ok "PowerShell $psVer (Windows PowerShell)"
        Write-Info "PowerShell 7+ recommended: https://aka.ms/powershell"
    } else {
        Write-Warn "PowerShell $psVer is very old — some features may not work"
    }

    # Python
    $pythonCmd = $null
    foreach ($cmd in @('python', 'python3', 'py')) {
        try {
            $ver = & $cmd --version 2>&1
            if ($ver -match 'Python (\d+\.\d+)') {
                $pyVer = [version]$Matches[1]
                if ($pyVer -ge [version]'3.9') {
                    $pythonCmd = $cmd
                    Write-Ok "Python $($pyVer.ToString()) — $cmd"
                    break
                } else {
                    Write-Warn "Python $($pyVer.ToString()) found but 3.9+ is required"
                }
            }
        } catch { }
    }

    if (-not $pythonCmd) {
        Write-Fail "Python 3.9+ not found in PATH."
        Write-Info "Download from: https://www.python.org/downloads/"
        Write-Info "Make sure 'Add Python to PATH' is checked during install."
        exit 1
    }

    # pip
    try {
        $pipVer = & $pythonCmd -m pip --version 2>&1
        Write-Ok "pip — $($pipVer -replace '\s+', ' ')"
    } catch {
        Write-Fail "pip not available for $pythonCmd"
        Write-Info "Fix with: $pythonCmd -m ensurepip --upgrade"
        exit 1
    }

    # claude (Claude Code CLI) — optional, just warn
    $claudeFound = $false
    try {
        $null = Get-Command 'claude' -ErrorAction Stop
        $claudeFound = $true
        Write-Ok "Claude Code CLI found"
    } catch {
        Write-Warn "Claude Code CLI not found in PATH"
        Write-Info "Install with: npm install -g @anthropic-ai/claude-code"
    }

    # node/npm — only warn if Claude not found
    if (-not $claudeFound) {
        try {
            $nodeVer = node --version 2>&1
            $npmVer  = npm  --version 2>&1
            Write-Ok "Node $nodeVer / npm $npmVer"
            Write-Info "Run:  npm install -g @anthropic-ai/claude-code"
        } catch {
            Write-Warn "Node.js not found — needed to install Claude Code"
            Write-Info "Download from: https://nodejs.org/"
        }
    }
}

# ── Directory tree ─────────────────────────────────────────────────────────────

Write-Header "Creating directory structure"

$Directories = @(
    'inbox\clippings',
    'sources\reddit',
    'sources\web',
    'sources\transcripts',
    'wiki\concepts',
    'wiki\tools',
    'wiki\agents',
    'wiki\models',
    'wiki\news',
    'wiki\tips',
    'wiki\people',
    'digests',
    'scripts',
    '.state'
)

$Created = 0
$Existed = 0

foreach ($Dir in $Directories) {
    $FullPath = Join-Path $ProjectRoot $Dir
    if (Test-Path $FullPath) {
        $Existed++
    } else {
        New-Item -ItemType Directory -Path $FullPath -Force | Out-Null
        $Created++
    }
}

if ($Created -gt 0) { Write-Ok "$Created directories created" }
if ($Existed -gt 0) { Write-Info "$Existed directories already existed (skipped)" }

# ── .env scaffold ──────────────────────────────────────────────────────────────

Write-Header "Environment file (.env)"

$EnvFile    = Join-Path $ProjectRoot '.env'
$EnvExample = Join-Path $ProjectRoot '.env.example'

if ((Test-Path $EnvFile) -and -not $ForceEnv) {
    Write-Ok ".env already exists — skipping (use -ForceEnv to overwrite)"
} elseif (Test-Path $EnvExample) {
    Copy-Item $EnvExample $EnvFile -Force
    Write-Ok ".env created from .env.example"
    Write-Warn "Edit .env and add your Reddit + RapidAPI credentials before first run"
} else {
    # Write a minimal .env directly
    @'
# LLM Wiki — credentials
# Reddit API  →  https://www.reddit.com/prefs/apps
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=llm-wiki-bot/1.0 (by /u/your_username)

# Twitter/X via RapidAPI  →  https://rapidapi.com  (search: twitter241)
# Optional — tweet URL lookup only; dump files work without this
RAPIDAPI_KEY=your_rapidapi_key_here
'@ | Set-Content -Encoding UTF8 $EnvFile
    Write-Ok ".env created from built-in template"
    Write-Warn "Edit .env and add your Reddit + RapidAPI credentials before first run"
}

# ── Python dependencies ────────────────────────────────────────────────────────

if (-not $SkipPip) {
    Write-Header "Installing Python dependencies"

    $ReqFile = Join-Path $ProjectRoot 'requirements.txt'

    if (Test-Path $ReqFile) {
        Write-Step "pip install -r requirements.txt"
        try {
            & $pythonCmd -m pip install -r $ReqFile --quiet --disable-pip-version-check
            Write-Ok "All packages installed"
        } catch {
            Write-Fail "pip install failed: $_"
            Write-Info "Try manually:  $pythonCmd -m pip install -r requirements.txt"
        }
    } else {
        Write-Step "requirements.txt not found — installing core packages directly"
        $Packages = @(
            'requests',
            'python-dotenv',
            'yt-dlp',
            'youtube-transcript-api',
            'rich',
            'readability-lxml'
        )
        try {
            & $pythonCmd -m pip install @Packages --quiet --disable-pip-version-check
            Write-Ok "Core packages installed"
        } catch {
            Write-Fail "pip install failed: $_"
        }
    }
} else {
    Write-Header "Python dependencies"
    Write-Info "Skipped (--SkipPip). Install manually:"
    Write-Info "  $pythonCmd -m pip install -r requirements.txt"
}

# ── Validate scripts ───────────────────────────────────────────────────────────

Write-Header "Checking helper scripts"

$Scripts = @(
    'scripts\utils.py',
    'scripts\fetch_reddit.py',
    'scripts\fetch_youtube.py',
    'scripts\fetch_url.py',
    'scripts\fetch_twitter.py'
)

$MissingScripts = @()
foreach ($Script in $Scripts) {
    $FullPath = Join-Path $ProjectRoot $Script
    if (Test-Path $FullPath) {
        Write-Ok $Script
    } else {
        Write-Warn "Missing: $Script"
        $MissingScripts += $Script
    }
}

if ($MissingScripts.Count -gt 0) {
    Write-Warn "$($MissingScripts.Count) script(s) not found — copy them from the project template."
}

# ── State file initialisation ──────────────────────────────────────────────────

Write-Header "Initialising state files"

$StateFiles = @{
    '.state\processed_urls.json' = '[]'
    '.state\reddit_cursor.json'  = '{}'
    '.state\last_run.json'       = '[]'
}

foreach ($Entry in $StateFiles.GetEnumerator()) {
    $FullPath = Join-Path $ProjectRoot $Entry.Key
    if (-not (Test-Path $FullPath)) {
        $Entry.Value | Set-Content -Encoding UTF8 $FullPath
        Write-Ok "Created $($Entry.Key)"
    } else {
        Write-Info "$($Entry.Key) already exists (skipped)"
    }
}

# ── Quick-smoke test ───────────────────────────────────────────────────────────

Write-Header "Smoke test"

try {
    $TestOutput = & $pythonCmd -c "import requests, dotenv; print('imports ok')" 2>&1
    if ($TestOutput -match 'imports ok') {
        Write-Ok "Core Python imports (requests, dotenv)"
    } else {
        Write-Warn "Import check returned: $TestOutput"
    }
} catch {
    Write-Warn "Could not verify Python imports — check pip install output above"
}

try {
    $YtOutput = & $pythonCmd -c "from youtube_transcript_api import YouTubeTranscriptApi; print('ok')" 2>&1
    if ($YtOutput -match 'ok') { Write-Ok "youtube-transcript-api" }
    else                       { Write-Warn "youtube-transcript-api not importable — transcripts may fail" }
} catch {
    Write-Warn "youtube-transcript-api import failed"
}

# ── Summary ────────────────────────────────────────────────────────────────────

Write-Host ""
Write-Host " ╔══════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host " ║                Setup complete! 🎉                ║" -ForegroundColor Green
Write-Host " ╚══════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
Write-Host "  Next steps:" -ForegroundColor White
Write-Host ""
Write-Host "  1. Edit .env and fill in your Reddit credentials" -ForegroundColor Gray
Write-Host "     https://www.reddit.com/prefs/apps" -ForegroundColor DarkGray
Write-Host ""
Write-Host "  2. Add content to the inbox:" -ForegroundColor Gray
Write-Host "     inbox\links.md       ← paste article URLs" -ForegroundColor DarkGray
Write-Host "     inbox\youtube.md     ← paste YouTube URLs" -ForegroundColor DarkGray
Write-Host "     inbox\twitter.md     ← paste tweet URLs" -ForegroundColor DarkGray
Write-Host "     inbox\posts.md       ← paste social media text posts" -ForegroundColor DarkGray
Write-Host "     inbox\clippings\     ← drop Obsidian Web Clipper .md files" -ForegroundColor DarkGray
Write-Host ""
Write-Host "  3. Start Claude Code from this folder:" -ForegroundColor Gray
Write-Host "     claude" -ForegroundColor Yellow
Write-Host ""
Write-Host "  4. Try your first command in Claude Code:" -ForegroundColor Gray
Write-Host "     /wiki-reddit" -ForegroundColor Yellow
Write-Host "     /wiki-inbox" -ForegroundColor Yellow
Write-Host ""
