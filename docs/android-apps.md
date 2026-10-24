# Android apps

Two apps open the phone pages full screen, with the microphone allowed and the screen kept on. They install side by side.

| App | Opens | Built by | Output |
| --- | --- | --- | --- |
| **IC-9700** | The full [phone page](phone-page.md) | `build_apk.bat` | `IC9700_Remote.apk` |
| **IC-9700 Lite** | The [lite page](lite-page.md) | `build_apk_lite.bat` | `IC9700_Lite.apk` |

The apps hold no radio code: they load the page from your PC, so updating IC9700 Monitor updates what the apps show.

## Building

You need a Windows PC with Python 3 and an internet connection. Java and the Android build tools are fetched automatically the first time.

1. Put `build_apk.py` and the `.bat` you want in one folder (this repository's folder works). Add `ic9700.png` to use your own icon; for the Lite app, `ic9700_lite.png` is used if present, otherwise `ic9700.png` gets a green LITE band.
2. Double-click `build_apk.bat` or `build_apk_lite.bat`.
3. The first run installs Microsoft OpenJDK 17 with winget if no Java 17 is found, and downloads Android platform 34 and build-tools 34.0.0 (about 150 MB) straight from Google into `%LOCALAPPDATA%\IC9700AndroidSDK`. Later builds take seconds.
4. When it finishes, Explorer opens with the `.apk` selected.

By building you accept the [Android SDK licence](https://developer.android.com/studio/terms).

## Installing on the phone

1. Copy the `.apk` to the phone (USB, Google Drive, email) and open it.
2. Allow **Install unknown apps** when asked.
3. Enter the PC's https address, e.g. `https://your-pc.tailnet-name.ts.net:8074/`. The Lite app adds `/lite` itself.
4. Sign in once with your phone-access password.

**Back** in the app gives Reload, Change PC address or Exit. If the PC can't be reached, the app says so and lets you fix the address.

## Signing key

The apps are signed with a key created on the first build: `%LOCALAPPDATA%\IC9700AndroidSDK\ic9700_remote.keystore`. **Keep it.** An update must be signed with the same key, or Android makes you uninstall the old app first. The key is never part of this repository.

## How the builder works

`build_apk.py` doesn't use Gradle or Android Studio. It:

1. finds or installs Java 17;
2. reads Google's package list and downloads the two Android packages it needs, checking their SHA-1;
3. writes a small WebView app (one Java file, manifest and icon);
4. compiles it with `aapt2`, `javac` and `d8`, aligns it with `zipalign` and signs it with `apksigner`.

Everything it prints is also saved in `build_apk_log.txt` next to the script.
