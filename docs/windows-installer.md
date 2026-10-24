# Windows installer

`build_installer.bat` turns `IC9700.py` into a normal Windows setup program, `IC9700_Monitor_Setup_<version>.exe`. The installed program runs without Python, includes the phone-audio library, and appears in the Start menu with an uninstaller.

## Building

1. Put `IC9700.py`, `build_installer.bat` and `IC9700_installer.iss` in one folder (this repository's folder works). Add `ic9700.ico` and `ic9700.png` for the program's icon.
2. Double-click `build_installer.bat`. It:
   1. installs PyInstaller, pyserial and sounddevice with pip;
   2. builds the program with PyInstaller into `dist\IC9700 Monitor\`;
   3. builds the setup with [Inno Setup 6](https://jrsoftware.org/isinfo.php), installing it with winget first if needed.
3. Explorer opens the `installer` folder with the setup `.exe`.

When you change `IC9700.py` to a new version, also change `AppVersion` in `IC9700_installer.iss` and the file name in `build_installer.bat`.

## Installing

Run the setup `.exe`. It installs to Program Files, adds a Start-menu entry and an optional desktop shortcut. Installing over an older version keeps your settings.

The installed program keeps its settings, QSO log and HTTPS certificate in `%LOCALAPPDATA%\IC9700 Monitor`, because Windows doesn't let programs write to Program Files. These are separate from a copy run as `IC9700.py`.

## If the build stops

The window shows which step failed. Common causes:

| Step | Cause |
| --- | --- |
| [1/3] | Python not on PATH: reinstall Python and tick **Add to PATH** |
| [2/3] | Antivirus blocking PyInstaller: allow the folder |
| [3/3] | Inno Setup missing and winget unavailable: install it from [jrsoftware.org](https://jrsoftware.org/isdl.php) |
