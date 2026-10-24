@echo off
rem ============================================================
rem  IC-9700 Lite - builds the separate Lite Android app
rem  (IC9700_Lite.apk): minimal controls, clear audio, quick PTT.
rem  Put this file and build_apk.py in one folder (plus ic9700.png
rem  or ic9700_lite.png for the icon), then double-click this file.
rem  It installs beside the full IC-9700 app on the phone.
rem ============================================================
setlocal
cd /d "%~dp0"
where py >nul 2>nul && (set PY=py) || (set PY=python)
%PY% --version >nul 2>nul || (
  echo Python was not found. Install it from https://www.python.org/downloads/ and tick "Add to PATH".
  pause & exit /b 1
)
%PY% build_apk.py --lite
if errorlevel 1 (
  echo.
  echo Build failed - see the messages above.
  pause & exit /b 1
)
explorer /select,"%~dp0IC9700_Lite.apk"
pause
