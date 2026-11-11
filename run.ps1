# Cynta — launcher local (FastAPI + UI)
param(
  [switch]$SkipInstall,
  [switch]$Install,
  [int]$Port = 8765
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

$env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" +
            [System.Environment]::GetEnvironmentVariable("Path", "User")
$env:PYTHONUNBUFFERED = "1"
$env:HF_HUB_DISABLE_SYMLINKS_WARNING = "1"

function Write-Ok($msg) { Write-Host "  OK  $msg" -ForegroundColor Green }
function Write-Warn($msg) { Write-Host "  !!  $msg" -ForegroundColor Yellow }
function Write-Fail($msg) { Write-Host "  XX  $msg" -ForegroundColor Red }

Write-Host ""
Write-Host "Cynta — chequeo local" -ForegroundColor Cyan
Write-Host ("=" * 40)

# Python 3.11
$py = $null
try {
  $ver = & py -3.11 -c "import sys; print(sys.version.split()[0])" 2>$null
  if ($LASTEXITCODE -eq 0 -and $ver) { $py = $ver.Trim() }
} catch { }
if (-not $py) {
  Write-Fail "Python 3.11 no encontrado. Instalá desde https://www.python.org/downloads/"
  Write-Host "  Tip: marcá 'Add python.exe to PATH' e instalá el launcher py." -ForegroundColor DarkGray
  exit 1
}
Write-Ok "Python $py (py -3.11)"

# ffmpeg
$ffmpeg = Get-Command ffmpeg -ErrorAction SilentlyContinue
if ($ffmpeg) {
  Write-Ok "ffmpeg en PATH ($($ffmpeg.Source))"
} else {
  Write-Warn "ffmpeg no está en PATH — videos van a fallar."
  Write-Host "  winget install Gyan.FFmpeg   (después reabrí la terminal)" -ForegroundColor DarkGray
}

# NVIDIA
$smi = Get-Command nvidia-smi -ErrorAction SilentlyContinue
if ($smi) {
  try {
    $gpu = & nvidia-smi --query-gpu=name,driver_version --format=csv,noheader 2>$null
    if ($gpu) { Write-Ok "GPU: $($gpu.Trim())" }
    else { Write-Warn "nvidia-smi no devolvió GPU" }
  } catch {
    Write-Warn "nvidia-smi falló"
  }
} else {
  Write-Warn "Sin nvidia-smi — Cynta puede correr en CPU (más lento)."
}

# Deps
$needInstall = $Install.IsPresent
if (-not $SkipInstall -and -not $needInstall) {
  $probe = & py -3.11 -c "import fastapi, faster_whisper, uvicorn; import nvidia.cublas" 2>$null
  if ($LASTEXITCODE -ne 0) { $needInstall = $true }
}
if ($needInstall) {
  Write-Host ""
  Write-Host "Instalando dependencias (requirements.txt)..." -ForegroundColor Cyan
  py -3.11 -m pip install -r requirements.txt
  if ($LASTEXITCODE -ne 0) {
    Write-Fail "pip install falló"
    exit 1
  }
  Write-Ok "Dependencias instaladas"
} else {
  Write-Ok "Dependencias Python ya presentes (usá -Install para forzar)"
}

# Free / reuse port
$existing = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
if ($existing) {
  Write-Warn "Puerto $Port ya en uso — abriendo UI existente"
  Start-Process "http://127.0.0.1:$Port"
  exit 0
}

Write-Host ""
Write-Host "Levantando http://127.0.0.1:$Port" -ForegroundColor Green
Write-Host "Ctrl+C para parar." -ForegroundColor DarkGray
Write-Host ""

# Open browser when server is up (background waiter)
$waiter = Start-Job -ScriptBlock {
  param($Port)
  for ($i = 0; $i -lt 60; $i++) {
    Start-Sleep -Milliseconds 400
    try {
      $r = Invoke-WebRequest -Uri "http://127.0.0.1:$Port/api/health" -UseBasicParsing -TimeoutSec 1
      if ($r.StatusCode -eq 200) {
        Start-Process "http://127.0.0.1:$Port"
        return
      }
    } catch { }
  }
} -ArgumentList $Port

try {
  py -3.11 -m uvicorn app.main:app --host 127.0.0.1 --port $Port
} finally {
  Stop-Job $waiter -ErrorAction SilentlyContinue
  Remove-Job $waiter -Force -ErrorAction SilentlyContinue
}
