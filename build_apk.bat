@echo off
rem ============================================================
rem  IC9700 Remote - builds the Android app (IC9700_Remote.apk)
rem  Put this file and build_apk.py in one folder (plus ic9700.png
rem  for the app icon, if you have it), then double-click this file.
rem  First run downloads Java and the Android SDK (~300 MB).
rem ============================================================
setlocal
cd /d "%~dp0"
where py >nul 2>nul && (set PY=py) || (set PY=python)
%PY% --version >nul 2>nul || (
  echo Python was not found. Install it from https://www.python.org/downloads/ and tick "Add to PATH".
  pause & exit /b 1
)
%PY% build_apk.py
if errorlevel 1 (
  echo.
  echo Build failed - see the messages above.
  pause & exit /b 1
)
explorer /select,"%~dp0IC9700_Remote.apk"
pause
