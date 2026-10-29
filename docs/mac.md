# Mac app

IC9700 Monitor also runs on a Mac (Mac mini, MacBook, iMac…), Apple silicon or Intel, macOS 11 or later. It is the same program as on Windows: display, meters, scope and waterfall, all controls, CW decoder, QSO log, and the phone page.

## Installing

1. Download the installer from the **Releases** page of this repository (right-hand side on GitHub), release **IC9700 Monitor … for Mac**:
   - `IC9700_Monitor_…_mac_arm64.dmg` for Apple silicon (M1, M2, M3, M4 – every Mac mini from late 2020 on);
   - `IC9700_Monitor_…_mac_x86_64.dmg` for older Intel Macs.
   (**Apple menu > About This Mac** shows which: "Chip Apple M…" = arm64, "Processor Intel" = x86_64.)
2. Open the `.dmg` and drag **IC9700 Monitor** onto **Applications**.
3. **First start only:** the app isn't from the App Store, so macOS asks before opening it.
   - Open it once from Applications. When macOS says it can't check it, click **Done** (or **Cancel**).
   - Go to **Apple menu > System Settings > Privacy & Security**, scroll down to *"IC9700 Monitor" was blocked…* and click **Open Anyway**, then **Open**.
   - From then on it opens normally.
4. When asked, allow **Microphone** (the radio's USB audio, for the phone page and the CW decoder) and **Local Network** (scope over Ethernet and the phone page).

## Connecting the radio

- **USB cable:** the IC-9700's USB port shows up on the Mac as two serial ports, named like `/dev/cu.usbserial-…` or `/dev/cu.SLAB_USBtoUART…`. With **Port = Auto-detect** the program asks each one and uses the port that answers as the IC-9700, so you don't need to choose.
- If no port appears, install the Silicon Labs **CP210x VCP driver for macOS** from silabs.com, allow it in **System Settings > Privacy & Security**, and plug the radio in again.
- Radio settings are the same as on Windows: **MENU > SET > Connectors > CI-V**: baud rate 19200 or 115200, address A2, Transceive ON. For audio: **USB AF/IF Output = AF**, **DATA OFF MOD = USB**.

## Differences from Windows

| | Mac |
| --- | --- |
| Settings, QSO log, HTTPS certificate | `~/Library/Application Support/IC9700 Monitor` |
| Right-click (SPAN key: step back) | Control-click, two-finger click on a trackpad, or the right mouse button |
| Copy decoded CW | Cmd-C |
| About / Settings | **IC9700 Monitor** menu at the top of the screen (Settings: Cmd-,) |
| Quit | Cmd-Q (settings are saved) |
| Phone access over HTTPS | Install **Tailscale for Mac**; the program finds it in Applications |

## Running from source, or building it yourself

- **From source:** install Python from [python.org](https://www.python.org/downloads/macos/) (it includes the Tk window toolkit), then in Terminal:
  ```
  python3 -m pip install pyserial sounddevice
  python3 IC9700.py
  ```
- **Build the app and .dmg yourself:** `./build_mac.sh` (needs the python.org Python). The result is `dist/IC9700 Monitor.app` and `IC9700_Monitor_<version>_mac_<arch>.dmg`.
- Every change to `IC9700.py` on GitHub builds the Mac app automatically (**Actions > Build Mac app**) and updates the release page.
