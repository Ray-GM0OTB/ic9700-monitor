# Desktop app

IC9700 Monitor controls the IC-9700 over the USB cable using CI-V. Everything you change on the radio's front panel shows up in the program too, because it re-reads the radio continuously.

![IC9700 Monitor](../screenshots/desktop.png)

## Setting up

**Radio menu** (set once):

| Menu path | Setting |
| --- | --- |
| SET > Connectors > CI-V > CI-V USB Baud Rate | 19200 or 115200 (115200 gives a smoother USB scope) |
| SET > Connectors > CI-V > CI-V Address | A2 |
| SET > Connectors > CI-V > CI-V Transceive | ON |
| SET > Connectors > USB AF/IF Output | AF, for radio audio on the phone |
| SET > Connectors > MOD Input > DATA OFF MOD | USB, so the phone microphone reaches the transmitter |

**First connection:**

1. Plug in the USB cable and start the program.
2. Open **Settings > Settings…**.
3. Choose the COM port (or **Auto**), the same baud rate as the radio, CI-V address **A2**, your callsign and a PTT time-out.
4. Click **Save & connect**. The status bar turns green and says "ONLINE".

## The window

| Part | What it shows or does |
| --- | --- |
| **POWER** (top left) | Switches the radio on and off. Green = on. Switching off asks first. Switching on works while the radio is off, as long as USB and DC power are connected. |
| Icon line | P.AMP, AGC, SCOPE and other active functions; supply voltage and UTC |
| Band tags | MAIN, mode, filter (FIL1-3), band, VFO/MEMORY; **MAIN ⇄ SUB** swaps the bands |
| Frequency | Mouse wheel over a digit tunes that digit; over "MHz" it tunes by the step; ▲/▼ keys tune; PgUp/PgDn = 1 MHz |
| S-meter | Blue up to S9, red above, with a PEAK hold reading |
| TX meter | Po (blue, red past 40 %), SWR (red above 3), plus ALC, COMP and Id text |
| SUB band | Mode, band and frequency of the sub receiver |
| AF / PWR / SQL | Main-band AF gain, RF power and squelch at a glance |
| Scope and waterfall | See below |
| Status bar | Connection and messages on the left; port, baud, address, SCOPE LAN and phone port on the right |

## Keys

| Key | Action |
| --- | --- |
| P.AMP / ATT | Preamp and attenuator |
| AGC-F/M/S | AGC speed (click to cycle) |
| NB / NR / ANF | Noise blanker, noise reduction, auto notch |
| LOCK | Dial lock |
| SCOPE | Scope and waterfall on/off |
| SPAN | Scope span (see below) |
| TRANSMIT | PTT on/off. Released after the PTT time-out, on disconnect and on exit. |

## Tabs

| Tab | Contents |
| --- | --- |
| TUNE | Mode, filter, DATA, tuning step, Main/Sub, VFO A/B, swap, equalise, split, dualwatch, simplex / DUP− / DUP+, Tone / TSQL with CTCSS tone, satellite mode |
| LEVELS | AF, RF, SQL, NR, NB, PBT inner/outer (double-click to centre), CW pitch, RF power, mic, COMP, key speed, monitor, VOX, anti-VOX |
| BANDS | 2 m, 70 cm, 23 cm; each returns to the last frequency you used on it |
| FUNC | COMP, VOX, MON, BK-IN, RIT with offset, voice announce |
| CW | Keyer: free text and 6 editable macros; {MYCALL} = your callsign, {CALL} = the call in the LOG tab |
| MEMORY | Memory channels: Save current, Overwrite, Delete, **Read from radio**, CSV import/export. Double-click to recall. |
| SCAN | Scan memories or a frequency range; stops on squelch and/or S-meter; band-activity plot (click a bar to tune there) |
| LOG | QSO log (see below) |

## Spectrum scope and waterfall

Press **SCOPE**. The program sets the radio's scope to CENTRE mode and "Carrier point center", so the frequency you are tuned to is always in the middle, under the red marker, on every mode.

- **Click** the spectrum or waterfall to tune there; **hold and drag** to follow a signal.
- A yellow cursor line shows the frequency under the mouse.
- SSB, CW, RTTY and AM land on the nearest 100 Hz; FM and DV land on the tuning step.
- The mouse wheel over the scope tunes by the step.

**SPAN** shows the current span. Click for the next wider one, cycling ±2.5k → 5k → 10k → 25k → 50k → 100k → 250k → 500k → ±2.5k; right-click cycles the other way. The wheel over SPAN goes wider/narrower and stops at the ends.

For a faster scope, see [Scope over Ethernet](scope-over-lan.md). **View > Show scope / waterfall** hides it to save space.

## Logging QSOs

1. Type the **Call**. A call already in the log is flagged as a dupe.
2. Change **RST S / R** from 59 if needed; add **Name**, **Grid**, **Notes**.
3. Click **LOG QSO**. UTC time, frequency and mode come from the radio.
4. **Export ADIF** for logbook programs, QRZ, Club Log or LoTW (via TQSL); **Export CSV** for spreadsheets.

The log saves itself after every change, to `ic9700_qso_log.json`.

## Menus

| Menu | Items |
| --- | --- |
| Settings | Settings… (port, baud, address, callsign, PTT time-out, scope over the network) · Phone access… · Reconnect · Disconnect · Re-read radio state |
| View | Always on top · Show scope / waterfall · Reset window size |
| Phone | Phone access, audio (RX / TX) & HTTPS… · Turn on HTTPS · Open the phone page on this PC · Open the LITE phone page on this PC |
| About | Version, author, and the Python / Tk / display scaling / settings folder in use |

## Window size

Drag the edge to resize; the frequency digits grow and shrink with it. Maximise and restore return to the size you had. **View > Reset window size** goes back to the normal size. The smallest width comes from the radio panel, so long status messages are cut off rather than widening the window.

## Where files are kept

| Running | Settings, QSO log, HTTPS certificate |
| --- | --- |
| `IC9700.py` | The folder that holds `IC9700.py` |
| Installed program | `%LOCALAPPDATA%\IC9700 Monitor` |

The two keep separate settings. To move them across, copy `ic9700_settings.json` and `ic9700_qso_log.json`.
