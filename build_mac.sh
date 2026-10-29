#!/bin/bash
# ============================================================
#  IC9700 Monitor - builds the Mac app and a .dmg installer
#  Run on a Mac (Apple silicon or Intel) with Python 3.10 or later
#  from python.org (it includes the Tk window toolkit):
#      ./build_mac.sh
#  Result: dist/IC9700 Monitor.app  and  IC9700_Monitor_<version>_mac_<arch>.dmg
#  The same script is used by the automatic build on GitHub.
# ============================================================
set -euo pipefail
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"
VER=$("$PY" -c "import re;print(re.search(r'APP_VERSION = \"([^\"]+)\"', open('IC9700.py').read()).group(1))")
ARCH=$(uname -m)
APP="dist/IC9700 Monitor.app"
DMG="IC9700_Monitor_${VER}_mac_${ARCH}.dmg"
echo "Building IC9700 Monitor $VER for $ARCH with $("$PY" --version)"

"$PY" -c "import tkinter; tkinter.Tcl()" 2>/dev/null || {
    echo "This Python has no Tk. Install Python from https://www.python.org/downloads/macos/ and run again."
    exit 1
}

echo "[1/5] Build tools ..."
"$PY" -m pip install --quiet --upgrade pip pyinstaller pyserial sounddevice

echo "[2/5] App icon ..."
rm -rf build_mac
mkdir -p build_mac/ic9700.iconset
for s in 16 32 128 256 512; do
    sips -z "$s" "$s" ic9700.png --out "build_mac/ic9700.iconset/icon_${s}x${s}.png" >/dev/null
    sips -z "$((s * 2))" "$((s * 2))" ic9700.png --out "build_mac/ic9700.iconset/icon_${s}x${s}@2x.png" >/dev/null
done
iconutil -c icns build_mac/ic9700.iconset -o build_mac/ic9700.icns

echo "[3/5] App ..."
"$PY" -m PyInstaller --noconfirm --clean --windowed --name "IC9700 Monitor" \
    --icon "$PWD/build_mac/ic9700.icns" --osx-bundle-identifier uk.gm0otb.ic9700monitor \
    --add-data "$PWD/ic9700.png:." --hidden-import sounddevice --hidden-import serial.tools.list_ports \
    --workpath build_mac/work --specpath build_mac IC9700.py

echo "[4/5] App settings (version, microphone and network permissions) ..."
PL="$APP/Contents/Info.plist"
pb() {   # pb KEY TYPE VALUE: set a key, replacing any existing value
    /usr/libexec/PlistBuddy -c "Delete :$1" "$PL" >/dev/null 2>&1 || true
    /usr/libexec/PlistBuddy -c "Add :$1 $2 \"$3\"" "$PL"
}
pb CFBundleShortVersionString string "$VER"
pb CFBundleVersion string "$VER"
pb CFBundleDisplayName string "IC9700 Monitor"
pb NSMicrophoneUsageDescription string "IC9700 Monitor listens to the radio USB audio for the phone page and the CW decoder."
pb NSLocalNetworkUsageDescription string "IC9700 Monitor talks to the IC-9700 on your network for the scope and serves the phone page."
pb NSHighResolutionCapable bool true
pb LSMinimumSystemVersion string 11.0
codesign --force --deep --sign - "$APP"          # ad-hoc signature (Apple silicon needs one to run)

echo "[5/5] Disk image ..."
rm -rf build_mac/dmg "$DMG"
mkdir -p build_mac/dmg
cp -R "$APP" build_mac/dmg/
ln -s /Applications build_mac/dmg/Applications
hdiutil create -quiet -volname "IC9700 Monitor $VER" -srcfolder build_mac/dmg -ov -format UDZO "$DMG"

echo
echo "Done: $APP"
echo "      $DMG  (open it and drag IC9700 Monitor to Applications)"
