@echo off
rem ============================================================
rem  Connector X-Ref - builds an offline Android app from
rem  connector-xref\Connector Cross-Reference.html
rem  Result: connector-xref\Connector_X-Ref.apk
rem  Needs build_html_apk.py and build_apk.py in this folder.
rem ============================================================
setlocal
cd /d "%~dp0"
where py >nul 2>nul && (set PY=py) || (set PY=python)
%PY% --version >nul 2>nul || (
  echo Python was not found. Install it from https://www.python.org/downloads/ and tick "Add to PATH".
  pause & exit /b 1
)
set PAGE=connector-xref\Connector Cross-Reference.html
if not exist "%PAGE%" set PAGE=Connector Cross-Reference.html
if not exist "%PAGE%" (
  echo Connector Cross-Reference.html was not found.
  pause & exit /b 1
)
%PY% build_html_apk.py "%PAGE%" "Connector X-Ref"
if errorlevel 1 (
  echo.
  echo Build failed - see the messages above, or send build_html_apk_log.txt
  pause & exit /b 1
)
for %%F in ("%PAGE%") do explorer /select,"%%~dpFConnector_X-Ref.apk"
pause
