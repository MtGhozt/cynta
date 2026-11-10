# Launch local transcription product (FastAPI + UI)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
            [System.Environment]::GetEnvironmentVariable("Path","User")
$env:PYTHONUNBUFFERED = "1"
$env:HF_HUB_DISABLE_SYMLINKS_WARNING = "1"

if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    Write-Host "WARNING: ffmpeg not found in PATH. Video uploads will fail until installed." -ForegroundColor Yellow
}

Write-Host "Installing/updating Python deps (py -3.11)..." -ForegroundColor Cyan
py -3.11 -m pip install -r requirements.txt

Write-Host ""
Write-Host "Opening http://127.0.0.1:8765" -ForegroundColor Green
Write-Host "Ctrl+C to stop." -ForegroundColor DarkGray
Write-Host ""

Start-Process "http://127.0.0.1:8765"
py -3.11 -m uvicorn app.main:app --host 127.0.0.1 --port 8765
