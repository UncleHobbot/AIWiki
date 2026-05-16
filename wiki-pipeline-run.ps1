# wiki-pipeline-run.ps1
# Wrapper called by Windows Task Scheduler to run the LLM Wiki daily pipeline.
# Logs all output to .state\pipeline.log (append mode).
# Safe to run manually: .\wiki-pipeline-run.ps1

$ErrorActionPreference = "Continue"

$repo    = "C:\Shared\OneDrive\AIProjects\AIWiki"
$logFile = Join-Path $repo ".state\pipeline.log"
$claude  = "C:\Users\uncle\.local\bin\claude.exe"

Set-Location $repo

function Log {
    param([string]$msg)
    $ts = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $line = "[$ts] $msg"
    Add-Content -Path $logFile -Value $line -Encoding UTF8
    Write-Host $line
}

# Rotate log if it exceeds 5 MB
if ((Test-Path $logFile) -and (Get-Item $logFile).Length -gt 5MB) {
    $archive = $logFile -replace '\.log$', ("-" + (Get-Date -Format "yyyyMMdd") + ".log")
    Move-Item $logFile $archive -Force
    Log "Log rotated to $archive"
}

Log "=== Wiki Pipeline START ==="

# Check network connectivity (Reddit + GitHub must be reachable)
$online = Test-Connection -ComputerName "reddit.com" -Count 1 -Quiet -ErrorAction SilentlyContinue
if (-not $online) {
    Log "ERROR: No network connectivity. Aborting pipeline."
    exit 1
}

# Verify claude.exe exists
if (-not (Test-Path $claude)) {
    Log "ERROR: claude.exe not found at $claude. Aborting."
    exit 1
}

# Run the pipeline headlessly.
# --print        non-interactive mode (exits after one response)
# --dangerously-skip-permissions  trusts the CLAUDE.md allowlist for tool use
# Redirect stderr into stdout so everything lands in the log.
$prompt = "/wiki-pipeline"

Log "Running: claude --print `"$prompt`""

try {
    $output = & $claude --print $prompt 2>&1
    $exitCode = $LASTEXITCODE
} catch {
    Log "ERROR launching claude.exe: $_"
    exit 1
}

# Write claude output to log, prefixed with pipe symbol for easy grep
$output | ForEach-Object { Log "| $_" }

if ($exitCode -eq 0) {
    Log "=== Wiki Pipeline COMPLETE (exit 0) ==="
} else {
    Log "=== Wiki Pipeline FAILED (exit $exitCode) ==="
}

exit $exitCode
