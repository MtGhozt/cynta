@echo off
setlocal
cd /d "%~dp0"
title Cynta
echo.
echo  Cynta — doble clic / launcher
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run.ps1" %*
if errorlevel 1 (
  echo.
  echo  Algo falló. Leé el mensaje de arriba.
  pause
)
endlocal
