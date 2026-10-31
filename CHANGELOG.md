# Changelog

## Version 3.33

### Mac
- **Turn on HTTPS** works with the Tailscale Mac app. Before, the Tailscale app tried to open its own window when the program asked it for the certificate, and the program said "Tailscale status could not be read: The Tailscale GUI failed to start". The program now tells it to act as the command-line tool.

## Version 3.32

### Mac
- Larger, clearer text in the Mac's own font (San Francisco); the whole window grows with it. **View > Text size**: Normal, Large (default) or Extra large.
- Runs on the Mac (Mac mini, MacBook, iMac; Apple silicon or Intel, macOS 11 or later). Download the `.dmg` from the Releases page; see [docs/mac.md](docs/mac.md).
- The Mac app is built by `build_mac.sh`, and automatically on GitHub whenever the program changes.
- Auto-detect finds the IC-9700's CI-V port among the Mac's USB serial ports (Bluetooth and other ports are skipped).
- Settings in `~/Library/Application Support/IC9700 Monitor`; About, Settings (Cmd-,) and Quit (Cmd-Q) in the app menu; Control-click works as right-click; Tailscale for Mac is found for the phone's HTTPS page.


### Look
- Level sliders have red LED-style knobs that glow brighter the higher the value (PBT sliders: the further from centre). They replace the silver knobs; a knob stays grey until the radio has reported its level.

### CW decoder
- Decodes CW from the radio's USB receive audio: **CW tab > CW DECODER**, or **View > CW decoder…**. Also on the phone page: **FUNC tab > CW decoder**.
- **Sensitivity:** Auto, Low, Normal, High or Max. High and Max listen through a narrower filter matched to the sending speed and accept weaker signals. Auto runs at the most sensitive level and backs off by itself while it sees static.
- Finds the CW tone by itself (300–1200 Hz), or follows the rig's CW pitch setting.
- Follows the sending speed (about 5–50 WPM) and the signal level automatically.
- Rejects static crashes, and doesn't print a lone E or T caused by one; stays quiet on plain noise.
- Shows prosigns such as <AR>, <SK> and <KN>; characters it can't read show as `*`.
