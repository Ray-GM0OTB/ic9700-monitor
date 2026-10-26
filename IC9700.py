"""
IC-9700 Monitor & Control  -  by GM0OTB
=======================================

Version 3.30 - CI-V control panel for the Icom IC-9700.

New in 3.30
  * Level sliders: red LED-style knobs that glow brighter the higher the value (PBT sliders: the
    further from centre). Grey until the radio has reported the level.

New in 3.29
  * CW decoder (CW tab > CW DECODER, or View > CW decoder): decodes CW from the radio's USB
    receive audio. Finds the tone by itself (or uses the rig's CW pitch), follows the speed
    (about 5-50 WPM) and the signal level, and rejects static crashes. Sensitivity: Auto, Low,
    Normal, High, Max. Also on the phone page (FUNC tab > CW decoder). Uses the same audio set-up
    as the phone (sounddevice).

New in 3.28
  * LITE page: the phone's own voice processing (echo cancelling, noise suppression, auto gain,
    voice isolation) is always switched off for the microphone - requested when the mic opens,
    applied again to the live mic, then read back; the settings (gear) shows the result.
  * LITE phone page (https://<pc>:8074/lite, or Phone > Open the LITE phone page): only frequency
    (keypad + step), BAND, MODE, S / Po meter, RF power, SQL, RF gain, P.AMP, memories,
    memory scan, power and a
    big PTT. Built for clear audio and quick PTT:
      - one connection carries audio, display and commands (no extra web requests);
      - receive audio plays in its own audio thread with an adaptive jitter buffer
        (120 ms, grows after a dropout, shrinks again when the link is steady);
      - the microphone is opened once at start, so PTT doesn't wait for it;
      - PTT goes from the phone's connection straight to the radio (not via the window's queue),
        the radio's audio input is opened before keying and kept open between overs, and the
        last words are played out before unkeying.
  * Both phone pages use the quicker PTT path.
  * While a phone is listening, the PC's scope redraws less often so the audio comes first.

New in 3.27
  * Fixed the real cause of the window that could not be made smaller: the QSO-log and memory
    lists stretch their columns to the window, and Tk then asked for that width as the minimum,
    so every widening became permanent. The lists no longer set the window's size.

New in 3.26
  * Window can be made small again: the smallest width now comes from the radio panel itself, not
    from the title row (POWER key) or the long status text (SCOPE LAN / PHONE), which had pushed
    the minimum - and the starting size - wider. Starts once at that normal size.

New in 3.25
  * Installed copy: starts at the normal window size again (its settings folder in AppData kept
    the oversized width from older versions), never wider than the screen, and Windows display
    scaling is set the same way as when running IC9700.py. About shows the Python / Tk / scaling
    in use and where the settings are kept.

New in 3.24
  * Maximise / restore: the window goes back to its normal size when restored (it no longer
    resizes itself while maximised, which made Windows forget the normal size).

New in 3.23
  * Android app: build_apk.bat makes IC9700_Remote.apk (the phone page as a real app, with the
    microphone allowed for TALK). The page hides its "install as an app" button inside the app.

New in 3.22
  * Phone page: the "APP" button at the top right is gone (INSTALL AS AN APP stays at the bottom
    of the page, and disappears once installed).

New in 3.21
  * Phone page: POWER key (top left) switches the radio on and off remotely through the PC.
    Switching off asks for confirmation on the phone.

New in 3.20
  * POWER key top left: switches the radio on and off over CI-V (18 01 / 18 00). Green LED =
    radio on. Switching off asks first. Switching on works while the radio is off as long
    as the USB cable is connected (the program sends the wake-up preamble for the baud rate).

New in 3.19
  * The tuned (dial) frequency is now in the centre of the scope and waterfall on every mode:
    turning the scope on sets the radio's SCOPE > CENTER Type Display to "Carrier point center"
    (CI-V 1A 05 01 89 01) instead of "Filter center" (which put SSB ~1.5 kHz off centre).

New in 3.18
  * SPAN key cycles round: after +/-500 kHz the next click goes back to +/-2.5 kHz
    (right-click cycles the other way). Mouse wheel and the phone's SPAN -/+ still stop at the ends.

New in 3.17
  * SPAN key next to SCOPE: click for a wider span, right-click (or wheel down) for narrower:
    +/-2.5, 5, 10, 25, 50, 100, 250, 500 kHz (CI-V 27 15). Also on the phone page.

New in 3.16
  * Red marker sits in the centre of the scope and waterfall, where the radio centres the
    receive passband (on SSB that is ~1.5 kHz above the dial). Clicking a signal moves it
    under the marker, i.e. into the passband.
  * Window no longer grows wider when a long status message appears; it is back to its
    normal size (View > Reset window size does this at any time).

New in 3.15
  * The scope is switched to CENTRE mode when it is turned on, so the tuned frequency (red
    marker) sits in the middle of the spectrum and the waterfall, and the band moves past it.

New in 3.14
  * Click anywhere on the scope or the waterfall to tune there (hold and drag to follow a signal).
    A cursor line shows the frequency under the mouse; the tuned frequency is marked on the
    waterfall too. SSB / CW / RTTY / AM snap to 100 Hz, FM to the tuning step.

New in 3.13
  * Spectrum scope over the network (Ethernet): Settings > "Scope over the network".
    The scope data comes from the radio's LAN port (much faster than USB CI-V);
    everything else still runs over USB. Radio: SET > Network > Network Control = ON,
    and a Network User1 ID / password.

New in 3.12
  * Installed in Program Files: settings, QSO log and the https certificate are now saved in
    %LOCALAPPDATA%\\IC9700 Monitor (fixes "Access is denied" when turning on HTTPS).

New in 3.11
  * Transmit meter (Po and SWR) also blue, red past the S9 point of the scale - all bands.

New in 3.10
  * S-meter bar is blue up to S9 and red above S9 (PC window and phone page).
  * Windows installer (IC9700_Monitor_Setup.exe) build script.

New in 3.9
  * Phone TX audio: "TX tone" setting on the AUDIO tab (bass cut + presence lift) so the
    phone microphone no longer sounds bassy on air. Default: Clear.

New in 3.8
  * Phone TX audio: much clearer. The phone's call-style voice processing (noise suppression,
    echo cancelling, auto gain) is now off by default (AUDIO tab to turn it back on), and the
    microphone is resampled with a proper low-pass filter instead of a 3-sample average.

New in 3.7
  * Phone audio: never muted while the squelch is fully down; AUDIO tab shows which sound
    device is in use and when it is muting for a closed squelch.

New in 3.6
  * Phone: "APP" / "INSTALL AS AN APP" button always shown - installs straight away where the
    browser allows it, otherwise shows the steps for that phone (iPhone, Samsung, Chrome).

New in 3.5
  * New "Phone" menu: phone access, audio (RX / TX), HTTPS and opening the phone page.

New in 3.4
  * Phone page installs as an app (Android: Chrome > Install app, on the https address).
  * Sign-in page instead of the browser password pop-up; phones stay signed in.

New in 3.3
  * Phone audio follows the rig squelch (the IC-9700 USB audio ignores it by itself).
  * Built-in https page using this PC's Tailscale certificate (Phone access > Turn on HTTPS),
    so the phone microphone works. No "tailscale serve" needed.

New in 3.2
  * Phone audio: hear the radio on your phone and talk through it (TALK button).
    Uses the IC-9700 USB audio; needs:  python -m pip install sounddevice
    The phone microphone needs the https address (Phone access > Turn on HTTPS).
  * Phone page: waterfall removed (spectrum only).

New in 3.1
  * Phone access: Settings > Phone access... turns on a password-protected web page
    (built in, no extra packages). Open it on your phone over Tailscale to see the
    display, meter and scope and to tune, change mode, levels and functions.

New in 3.0
  * Display styled after the radio's own screen: icon line, MAIN band with tags,
    Icom-style bar meter (red over S9), SUB band readout, spectrum scope with
    waterfall (CI-V 27 - set CI-V USB baud to 115200 for a smooth scope; click the
    scope to tune), touch-style soft keys and rubber-style keys on a dark case.
  * Read memories from the radio (MEMORY > Read from radio, CI-V 1A 00): name,
    frequency, mode, duplex + offset and tone per band. Recalling such a channel
    also sets duplex and TONE / TSQL on the rig.
  * View > Show scope / waterfall hides the scope to save screen height.

Features
  * Large VFO readout - scroll the mouse wheel over any digit to tune that digit,
    or over the "MHz" area to tune by the selected step.  ▲/▼ keys also tune.
  * Segmented S-meter with peak hold; TX view shows Po (watts), SWR, ALC, COMP, Id.
  * Quick functions: P.AMP, ATT, AGC (F/M/S), NB, NR, ANF, LOCK and PTT
    (PTT has a transmit time-out and is always released on disconnect / exit).
  * Modes with filter FIL1/2/3, DATA mode, band buttons (remembers last frequency).
  * 15 levels: AF, RF, SQL, NR, NB, PBT in/out, CW pitch, RF power, mic, COMP,
    key speed, monitor, VOX, anti-VOX (double-click a PBT slider to centre it).
  * Main/Sub, VFO A/B, swap, equalise, dualwatch, split, simplex / DUP- / DUP+,
    repeater TONE / TSQL with CTCSS tone selection, satellite mode.
  * COMP, VOX, MON, BK-IN, RIT with offset, voice announce.
  * CW keyer: free text and 6 editable macros ({MYCALL} / {CALL} substitution).
  * Memories (with CSV import / export), scanner with a band-activity plot
    (click a bar to tune there), QSO log with dupe check, ADIF + CSV export.
  * Settings: COM port, baud, CI-V address, own callsign, TX time-out.
  * Panel state (toggles, tones, levels) is re-read continuously, so changes made
    on the radio's front panel show up here.

Requires:  python -m pip install pyserial sounddevice   (sounddevice only for phone audio)
Radio:     MENU > SET > Connectors > CI-V > CI-V USB Baud Rate / Address (A2)
"""
import base64
import csv
import hashlib
import hmac
import json
import math
import os
import queue
import re
import secrets
import select
import shutil
import socket
import struct
import ssl
import subprocess
import sys
import threading
import time
import tkinter as tk
import tkinter.font as tkfont
import urllib.parse
import webbrowser
import zlib
from array import array
from collections import deque
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from tkinter import filedialog, messagebox, ttk

# -----------------------------------------------------------------
# 1. CRASH-PROOF SERIAL ENVIRONMENT INGESTION
# -----------------------------------------------------------------
SERIAL_READY = False
try:
    import serial
    import serial.tools.list_ports
    SERIAL_READY = True
except ImportError:
    pass

AUDIO_READY = False          # phone audio needs sounddevice (PortAudio); everything else works without it
sd = None
try:
    import sounddevice as sd
    AUDIO_READY = True
except Exception:
    sd = None

# -----------------------------------------------------------------
# 2. CONSTANTS
# -----------------------------------------------------------------
START_BYTE = 0xFE
STOP_BYTE = 0xFD
ACK = 0xFB
NAK = 0xFA
DEFAULT_RADIO_ADDR = 0xA2
CONTR_ADDR = 0xE0

MODES = {
    0x00: "LSB", 0x01: "USB", 0x02: "AM", 0x03: "CW",
    0x04: "RTTY", 0x05: "FM", 0x07: "CW-R", 0x08: "RTTY-R", 0x17: "DV"
}
MODE_REVERSE = {v: k for k, v in MODES.items()}
MODE_LIST = ["LSB", "USB", "AM", "CW", "CW-R", "RTTY", "RTTY-R", "FM", "DV"]

ADIF_MODES = {
    "LSB": ("SSB", "LSB"), "USB": ("SSB", "USB"), "AM": ("AM", None),
    "CW": ("CW", None), "CW-R": ("CW", None), "RTTY": ("RTTY", None),
    "RTTY-R": ("RTTY", None), "FM": ("FM", None), "DV": ("DIGITALVOICE", "DSTAR"),
}

def _can_write(d):
    """Really try to write a file (os.access() says yes for Program Files on Windows, then writes fail)."""
    test = os.path.join(d, f".ic9700_write_test_{os.getpid()}")
    try:
        with open(test, "w") as f:
            f.write("x")
        os.remove(test)
        return True
    except OSError:
        return False


if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)  # next to the .exe (portable copy)
    if not _can_write(BASE_DIR):                # installed in Program Files: keep settings in AppData instead
        BASE_DIR = os.path.join(os.environ.get("LOCALAPPDATA") or os.path.expanduser("~"), "IC9700 Monitor")
        os.makedirs(BASE_DIR, exist_ok=True)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "ic9700_settings.json")
CERT_PATH = os.path.join(BASE_DIR, "ic9700_https.crt")      # Tailscale certificate for the phone's https page
KEY_PATH = os.path.join(BASE_DIR, "ic9700_https.key")
QSO_PATH = os.path.join(BASE_DIR, "ic9700_qso_log.json")
BAUD_RATES = [4800, 9600, 19200, 38400, 57600, 115200]
AUTO_PORT = "Auto-detect"
APP_VERSION = "3.30"
APP_AUTHOR = "GM0OTB"

# ---- Colour palette: radio body (case, keys) ----
BG = "#1b1c1f"           # case
PANEL = "#232529"        # control panels below the screen
PANEL2 = "#151618"
BORDER = "#393c42"
FIELD = "#101113"
BTN = "#33363b"          # rubber key
BTN_HOVER = "#3d4147"
BTN_DOWN = "#26282c"
KEY_HI = "#4b4f56"       # key top highlight
KEY_SHADOW = "#0b0c0d"
TEXT = "#eef1f5"
MUTED = "#9aa1ab"
DIM = "#5c616a"
GHOST = "#0b0d12"
SEG_OFF = "#17191d"
ACCENT = "#5ab8ff"
ACCENT_DIM = "#173149"
ACCENT_LO = "#2c6ea6"
GREEN = "#4ade80"
GREEN_DIM = "#143522"
AMBER = "#ffad1f"
AMBER_DIM = "#4a3410"
ORANGE = "#ff8a3d"
RED = "#ff3b30"
RED_DIM = "#4d1512"
BLUE = "#3b82f6"

# ---- Colour palette: the radio's display ----
LCD_BG = "#000000"
LCD_EDGE = "#2d3139"     # bezel line around the screen
LCD_SEP = "#1e2530"      # separator lines inside the screen
LCD_TEXT = "#ffffff"
LCD_LABEL = "#a8b3c3"
LCD_DIM = "#3b4250"
LCD_SEG_OFF = "#14171d"
LCD_MAIN = "#1f5fc4"     # MAIN band tag
LCD_SUB = "#4a5160"      # SUB band tag
LCD_RED = "#ff4a3d"
LCD_SBLUE = "#2f8bff"     # S-meter bar up to S9
LCD_GREEN = "#3ddc84"
LCD_ORANGE = "#ffa62b"
SOFTKEY = "#2a2e36"
SOFTKEY_HI = "#3a404b"
SOFTKEY_ON = "#2d63c8"

METER_MAX = 241
S9_RAW = 120
LINK_MISS_LIMIT = 8
RECONNECT_MS = 3000
SCAN_SETTLE = 0.15
MIN_DWELL = 0.3
REPLY_TIMEOUT = 0.6

S_TICKS = [("S1", 13), ("3", 40), ("5", 67), ("7", 93), ("9", 120),
           ("+20", 160), ("+40", 201), ("+60", 241)]


def _pwr_raw(pct):
    return (pct / 50) * 143 if pct <= 50 else 143 + ((pct - 50) / 50) * 70


PWR_TICKS = [("0", 0)] + [(f"{p}%", _pwr_raw(p)) for p in (25, 50, 75, 100)]
SWR_TICKS = [("1", 0), ("1.5", 48), ("2", 80), ("3", 120), ("∞", 241)]

BANDS = [
    ("2m", 144_000_000, 148_000_000, 145_500_000),
    ("70cm", 420_000_000, 450_000_000, 433_500_000),
    ("23cm", 1_240_000_000, 1_300_000_000, 1_296_500_000),
]
BAND_MAX_W = {"2m": 100, "70cm": 75, "23cm": 10}

STEPS = [("10 Hz", 10), ("100 Hz", 100), ("1 kHz", 1000), ("5 kHz", 5000), ("6.25 kHz", 6250),
         ("10 kHz", 10000), ("12.5 kHz", 12500), ("25 kHz", 25000), ("100 kHz", 100000),
         ("1 MHz", 1000000)]

CTCSS = [67.0, 69.3, 71.9, 74.4, 77.0, 79.7, 82.5, 85.4, 88.5, 91.5, 94.8, 97.4, 100.0,
         103.5, 107.2, 110.9, 114.8, 118.8, 123.0, 127.3, 131.8, 136.5, 141.3, 146.2, 151.4,
         156.7, 159.8, 162.2, 165.5, 167.9, 171.3, 173.8, 177.3, 179.9, 183.5, 186.2, 189.9,
         192.8, 196.6, 199.5, 203.5, 206.5, 210.7, 218.1, 225.7, 229.1, 233.6, 241.8, 250.3, 254.1]

# CI-V 0x14 levels: (label, sub-command, display format)
LEVELS = [
    ("AF gain", 0x01, "pct"), ("RF gain", 0x02, "pct"), ("Squelch", 0x03, "pct"),
    ("NR level", 0x06, "pct"), ("NB level", 0x12, "pct"), ("PBT inner", 0x07, "pbt"),
    ("PBT outer", 0x08, "pbt"), ("CW pitch", 0x09, "pitch"),
    ("RF power", 0x0A, "pct"), ("Mic gain", 0x0B, "pct"), ("COMP level", 0x0E, "pct"),
    ("Key speed", 0x0C, "wpm"), ("Monitor", 0x15, "pct"), ("VOX gain", 0x16, "pct"),
    ("Anti-VOX", 0x17, "pct"),
]
LEVEL_FMT = {sub: fmt for _, sub, fmt in LEVELS}
BAR_LEVELS = [(0x01, "AF", ACCENT), (0x0A, "PWR", AMBER), (0x03, "SQL", GREEN)]

# On/off (or multi-state) functions:
#   key: (label, cmd, sub, values, per-value texts or None)
TOGGLES = {
    "pamp": ("P.AMP", 0x16, 0x02, (0, 1), None),
    "att":  ("ATT",   0x11, None, (0x00, 0x10), None),
    "agc":  ("AGC",   0x16, 0x12, (1, 2, 3), ("AGC-F", "AGC-M", "AGC-S")),
    "nb":   ("NB",    0x16, 0x22, (0, 1), None),
    "nr":   ("NR",    0x16, 0x40, (0, 1), None),
    "anf":  ("ANF",   0x16, 0x41, (0, 1), None),
    "tone": ("TONE",  0x16, 0x42, (0, 1), None),
    "tsql": ("TSQL",  0x16, 0x43, (0, 1), None),
    "comp": ("COMP",  0x16, 0x44, (0, 1), None),
    "mon":  ("MON",   0x16, 0x45, (0, 1), None),
    "vox":  ("VOX",   0x16, 0x46, (0, 1), None),
    "bkin": ("BK-IN", 0x16, 0x47, (0, 1, 2), ("BK-IN", "SEMI BK", "FULL BK")),
    "lock": ("LOCK",  0x16, 0x50, (0, 1), None),
    "sat":  ("SAT",   0x16, 0x5A, (0, 1), None),
    "data": ("DATA",  0x1A, 0x06, (0, 1), None),
    "rit":  ("RIT",   0x21, 0x01, (0, 1), None),
}
ALWAYS_LIT = {"agc"}

DUPLEX_TEXT = {0x01: "SPLIT", 0x11: "DUP-", 0x12: "DUP+"}

DEFAULT_MACROS = ["CQ CQ CQ DE {MYCALL} {MYCALL} K", "{CALL} DE {MYCALL}", "TU 5NN",
                  "QRZ? DE {MYCALL}", "RR TNX 73", "{MYCALL}"]

# Radio memory banks (IC-9700 memories are kept per band) and the extra fields we keep for them
MEM_BANDS = [("2m", 0x01), ("70cm", 0x02), ("23cm", 0x03)]
MEM_EXTRA_KEYS = ("ch", "dup", "tone_mode", "tone", "tsql", "offset", "src")

SCOPE_SPANS = [2_500, 5_000, 10_000, 25_000, 50_000, 100_000, 250_000, 500_000]   # +/- Hz, centre mode


def span_text(hz):
    return f"±{hz / 1000:g}k" if hz < 1_000_000 else f"±{hz / 1e6:g}M"


TABS = ["TUNE", "LEVELS", "BANDS", "FUNC", "CW", "MEMORY", "SCAN", "LOG"]

SCALE = 1.0
F = {}


def px(v):
    return int(round(v * SCALE))


# -----------------------------------------------------------------
# 3. PURE HELPERS (no GUI / serial - easy to test)
# -----------------------------------------------------------------
LAN_DEFAULT_PORT_CFG = 50001
DEFAULT_CONFIG = {
    "port": AUTO_PORT, "baud": 19200, "ci_v": "A2", "geometry": "",
    "topmost": False, "step_hz": 12500, "memories": [], "band_last": {},
    "mycall": "", "tx_timeout": 180, "cw_macros": list(DEFAULT_MACROS), "tab": "TUNE",
    "scope_on": False, "scope_visible": True,
    "web_on": False, "web_port": 8073, "web_password": "", "web_https": "",
    "audio_in": "Auto (USB Audio CODEC)", "audio_out": "Auto (USB Audio CODEC)", "audio_sql": True,
    "web_https_port": 8074, "web_https_name": "", "web_secret": "",
    "lan_scope": False, "lan_ip": "", "lan_port": LAN_DEFAULT_PORT_CFG, "lan_user": "", "lan_pass": "",
}


def parse_ci_v(text):
    try:
        v = int(str(text).strip(), 16)
    except ValueError:
        return None
    return v if 0x01 <= v <= 0xDF else None


def load_config():
    cfg = {k: (v.copy() if isinstance(v, (dict, list)) else v) for k, v in DEFAULT_CONFIG.items()}
    try:
        with open(CONFIG_PATH, "r") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return cfg
        cfg["port"] = str(data.get("port", AUTO_PORT))
        cfg["baud"] = int(data.get("baud", 19200))
        if parse_ci_v(data.get("ci_v", "A2")) is not None:
            cfg["ci_v"] = str(data.get("ci_v", "A2")).strip().upper()
        cfg["geometry"] = str(data.get("geometry", ""))
        try:
            cfg["geom_fix"] = int(data.get("geom_fix", 0) or 0)
        except (TypeError, ValueError):
            cfg["geom_fix"] = 0
        cfg["topmost"] = bool(data.get("topmost", False))
        cfg["step_hz"] = int(data.get("step_hz", 12500))
        cfg["mycall"] = str(data.get("mycall", "")).upper()
        cfg["tx_timeout"] = max(10, min(600, int(data.get("tx_timeout", 180))))
        cfg["tab"] = data.get("tab", "TUNE") if data.get("tab") in TABS else "TUNE"
        cfg["scope_on"] = bool(data.get("scope_on", False))
        cfg["scope_visible"] = bool(data.get("scope_visible", True))
        cfg["web_on"] = bool(data.get("web_on", False))
        cfg["web_port"] = max(1024, min(65535, int(data.get("web_port", 8073))))
        cfg["web_password"] = str(data.get("web_password", ""))
        cfg["web_https"] = str(data.get("web_https", ""))
        for k in ("audio_in", "audio_out"):
            if data.get(k):
                cfg[k] = str(data[k])
        cfg["audio_sql"] = bool(data.get("audio_sql", True))
        cfg["web_https_port"] = max(1024, min(65535, int(data.get("web_https_port", 8074))))
        cfg["web_https_name"] = str(data.get("web_https_name", ""))
        cfg["web_secret"] = str(data.get("web_secret", ""))
        cfg["lan_scope"] = bool(data.get("lan_scope", False))
        cfg["lan_ip"] = str(data.get("lan_ip", "")).strip()
        cfg["lan_port"] = max(1, min(65535, int(data.get("lan_port", LAN_DEFAULT_PORT_CFG))))
        cfg["lan_user"] = str(data.get("lan_user", ""))
        cfg["lan_pass"] = str(data.get("lan_pass", ""))
        macros = data.get("cw_macros")
        if isinstance(macros, list) and macros:
            cfg["cw_macros"] = ([str(m) for m in macros] + DEFAULT_MACROS)[:len(DEFAULT_MACROS)]
        mems = []
        for m in data.get("memories", []):
            try:
                d = {"name": str(m["name"]), "hz": int(m["hz"]), "mode": m.get("mode")}
                for k in MEM_EXTRA_KEYS:
                    if m.get(k) is not None:
                        d[k] = m[k]
                mems.append(d)
            except Exception:
                pass
        cfg["memories"] = mems
        bl = data.get("band_last", {})
        if isinstance(bl, dict):
            cfg["band_last"] = {str(k): int(v) for k, v in bl.items()}
    except Exception:
        pass
    return cfg


def save_config(cfg):
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump(cfg, f, indent=1)
    except Exception:
        pass


def load_qso_log():
    try:
        with open(QSO_PATH, "r") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except Exception:
        return []


def save_qso_log(log):
    try:
        with open(QSO_PATH, "w") as f:
            json.dump(log, f, indent=1)
    except Exception:
        pass


def band_of(hz):
    for name, lo, hi, _ in BANDS:
        if lo <= hz <= hi:
            return name
    return ""


def hz_to_mhz(hz):
    return f"{hz / 1_000_000:.5f}"


def freq_to_bcd(hz):
    """5-byte little-endian BCD frequency as used by CI-V."""
    bcd = []
    temp = int(hz)
    for _ in range(5):
        pair = temp % 100
        bcd.append(((pair // 10) << 4) | (pair % 10))
        temp //= 100
    return bcd


def bcd_to_int(bs):
    """Big-endian packed BCD bytes -> int."""
    return int("".join(f"{b:02x}" for b in bs))


def le_bcd(bs):
    """Little-endian packed BCD (CI-V frequency order) -> int. Raises ValueError on non-BCD bytes."""
    return int("".join(f"{b:02x}" for b in reversed(bs)))


def _tone_hz(bs):
    if len(bs) != 3:
        return None
    try:
        v = bcd_to_int(bs) / 10
    except ValueError:
        return None
    return v if 60 <= v <= 260 else None


def parse_memory_frame(f, band_name):
    """Decode a CI-V 1A 00 memory-content reply.

    Returns a dict (hz, mode, filter, duplex, tone, name ...), "blank" for an empty channel,
    or None if the reply can't be understood. The frequency is located by searching for a
    5-byte BCD value inside the requested band, so small layout differences don't matter.
    """
    if not f or len(f) < 7 or f[4] != 0x1A or f[5] != 0x00:
        return None
    d = list(f[6:-1])
    if not d:
        return None
    if d[-1] == 0xFF and len(d) <= 5:
        return "blank"
    lo, hi = next(((b[1], b[2]) for b in BANDS if b[0] == band_name), (100_000, 2_000_000_000))
    fi = hz = None
    for i in range(1, 6):
        if i + 5 > len(d):
            break
        try:
            v = le_bcd(d[i:i + 5])
        except ValueError:
            continue
        if lo <= v <= hi:
            fi, hz = i, v
            break
    if fi is None:
        return "blank" if 0xFF in d[:6] else None

    def g(k):
        return d[fi + k] if fi + k < len(d) else None

    dt = g(8) or 0
    dup, tm = (dt >> 4) & 0x0F, dt & 0x0F
    offset = None
    if fi + 23 <= len(d):
        try:
            offset = le_bcd(d[fi + 20:fi + 23]) * 100
        except ValueError:
            offset = None
    name = ""
    if len(d) >= fi + 40:
        name = "".join(chr(b) for b in d[-16:] if 32 <= b < 127).strip()
    return {"hz": hz, "mode": MODES.get(g(5)), "filter": g(6) if g(6) in (1, 2, 3) else None,
            "dup": dup if dup in (0, 1, 2) else 0, "tone_mode": tm if tm in (0, 1, 2) else 0,
            "tone": _tone_hz(d[fi + 10:fi + 13]), "tsql": _tone_hz(d[fi + 13:fi + 16]),
            "offset": offset or None, "name": name}


def mem_info(m):
    parts = []
    dup = {1: "DUP-", 2: "DUP+"}.get(m.get("dup"))
    if dup:
        parts.append(dup + (f" {m['offset'] / 1e6:g}" if m.get("offset") else ""))
    if m.get("tone_mode") == 1 and m.get("tone"):
        parts.append(f"T {m['tone']:.1f}")
    elif m.get("tone_mode") == 2 and m.get("tsql"):
        parts.append(f"TSQL {m['tsql']:.1f}")
    return "  ".join(parts)


def parse_scope_frame(f, acc):
    """Assemble CI-V 27 00 scope waveform divisions. Returns (acc, complete) or None if invalid."""
    try:
        div, mx = bcd_to_int([f[7]]), bcd_to_int([f[8]])
    except (ValueError, IndexError):
        return None
    body = list(f[9:-1])
    if div == 1:
        if len(body) < 11:
            return None
        try:
            a, b = le_bcd(body[1:6]), le_bcd(body[6:11])
        except ValueError:
            return None
        lo, hi = (a - b, a + b) if body[0] == 0x00 else (a, b)      # centre mode: a=centre, b=span (+/-)
        acc = {"lo": lo, "hi": hi, "data": list(body[12:]) if mx == 1 else [], "next": 2,
               "centre": body[0] == 0x00}
    else:
        if acc is None or div != acc.get("next"):
            return None, False
        acc["data"].extend(body)
        acc["next"] += 1
    return acc, div == mx


def level_to_bcd(v):
    v = max(0, min(255, int(v)))
    s = f"{v:04d}"
    return [int(s[:2], 16), int(s[2:], 16)]


def tone_to_bcd(t):
    """88.5 Hz -> [0x00, 0x08, 0x85]"""
    s = f"{int(round(t * 10)):06d}"
    return [int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)]


def rit_to_bcd(hz):
    """RIT offset (+/- 9999 Hz) -> 2 BCD bytes little-endian + sign byte."""
    hz = max(-9999, min(9999, int(hz)))
    s = f"{abs(hz):04d}"
    return [int(s[2:4], 16), int(s[0:2], 16), 0x01 if hz < 0 else 0x00]


def level_text(sub, v):
    fmt = LEVEL_FMT.get(sub, "pct")
    if v is None:
        return "--"
    if fmt == "pbt":
        return f"{int(round((v - 128) / 127 * 100)):+d}"
    if fmt == "pitch":
        return f"{int(round(300 + v / 255 * 600))}Hz"
    if fmt == "wpm":
        return f"{int(round(6 + v / 255 * 42))}wpm"
    return f"{int(round(v / 255 * 100))}%"


def s_label(raw):
    s_units = int((raw / 120) * 9) if raw <= 120 else 9
    db = f"+{int(((raw - 120) / 121) * 60)}dB" if raw > 120 else ""
    return f"S{s_units}{db}"


def power_pct(p_val):
    if p_val <= 143:
        pct = (p_val / 143) * 50
    else:
        pct = 50 + ((p_val - 143) / 70) * 50
    return max(0, min(100, int(round(pct))))


def swr_from_raw(raw):
    """Icom SWR meter: 0=1.0, 48=1.5, 80=2.0, 120=3.0. Returns (text, severity 0-2)."""
    if raw <= 48:
        v = 1.0 + 0.5 * raw / 48
    elif raw <= 80:
        v = 1.5 + 0.5 * (raw - 48) / 32
    elif raw <= 120:
        v = 2.0 + 1.0 * (raw - 80) / 40
    else:
        return "SWR >3.0", 2
    return f"SWR {v:.1f}", (0 if v < 2.0 else 1)


def alc_pct(raw):
    return int(round(raw / 120 * 100))


def comp_db(raw):
    # 0 = 0 dB, 130 = 15 dB, 241 = 30 dB
    return 15 * raw / 130 if raw <= 130 else 15 + 15 * (raw - 130) / 111


def vd_volts(raw):
    # 0 = 0 V, 13 = 10 V, 241 = 16 V  (approximate)
    return 10 * raw / 13 if raw <= 13 else 10 + 6 * (raw - 13) / 228


def id_amps(raw):
    # 0 = 0 A, 97 = 10 A, 146 = 15 A, 241 = 25 A  (approximate)
    if raw <= 97:
        return 10 * raw / 97
    if raw <= 146:
        return 10 + 5 * (raw - 97) / 49
    return 15 + 10 * (raw - 146) / 95


def cw_clean(text):
    allowed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/?.,-=+@:'\"() ^")
    return "".join(ch for ch in text.upper() if ch in allowed)


def expand_macro(text, mycall, call):
    return text.replace("{MYCALL}", mycall or "").replace("{CALL}", call or "")


def adif_field(name, value):
    value = str(value).encode("ascii", "replace").decode("ascii")
    return f"<{name}:{len(value)}>{value}"


def adif_record(q, mycall=""):
    mode, sub = ADIF_MODES.get(q.get("mode", ""), (q.get("mode", ""), None))
    mhz = f"{q['hz'] / 1_000_000:.6f}"
    fields = [adif_field("QSO_DATE", q["date"]), adif_field("TIME_ON", q["time"]),
              adif_field("CALL", q["call"]), adif_field("FREQ", mhz),
              adif_field("MODE", mode)]
    if sub:
        fields.append(adif_field("SUBMODE", sub))
    if band_of(q["hz"]):
        fields.append(adif_field("BAND", band_of(q["hz"])))
    for key, tag in (("rst_s", "RST_SENT"), ("rst_r", "RST_RCVD"), ("name", "NAME"),
                     ("grid", "GRIDSQUARE"), ("notes", "COMMENT")):
        if q.get(key):
            fields.append(adif_field(tag, q[key]))
    if mycall:
        fields.append(adif_field("STATION_CALLSIGN", mycall))
    return " ".join(fields) + " <EOR>\n"


def adif_document(log, mycall=""):
    head = ("IC-9700 Monitor export\n" + adif_field("ADIF_VER", "3.1.4") + "\n"
            + adif_field("PROGRAMID", "IC9700 Monitor") + "\n"
            + adif_field("PROGRAMVERSION", APP_VERSION) + "\n<EOH>\n\n")
    return head + "".join(adif_record(q, mycall) for q in log)


def lerp_color(a, b, t):
    t = max(0.0, min(1.0, t))
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{int(round(x + (y - x) * t)):02x}" for x, y in zip(ca, cb))


def _wf_palette():
    stops = [(0.0, "#000614"), (0.22, "#061f6e"), (0.42, "#1658e8"), (0.58, "#22c8ff"),
             (0.72, "#ffe14d"), (0.86, "#ff7a1a"), (1.0, "#ff1f1f")]
    out = []
    for v in range(161):
        t = v / 160
        for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
            if t <= t1:
                out.append(lerp_color(c0, c1, (t - t0) / (t1 - t0)))
                break
    return out


WF_PALETTE = _wf_palette()


# -----------------------------------------------------------------
# 4. CUSTOM WIDGETS
# -----------------------------------------------------------------
def pick_family(candidates):
    have = {f.lower() for f in tkfont.families()}
    for c in candidates:
        if c.lower() in have:
            return c
    return candidates[-1]


def init_fonts(root):
    global SCALE
    try:
        SCALE = max(1.0, min(3.0, root.winfo_fpixels("1i") / 96.0))
    except Exception:
        SCALE = 1.0
    ui = pick_family(["Segoe UI", "Inter", "Helvetica Neue", "DejaVu Sans", "Helvetica"])
    mono = pick_family(["Cascadia Mono", "Consolas", "DejaVu Sans Mono", "Menlo", "Courier New", "Courier"])
    # The radio's display uses a clean sans-serif with tabular figures for the frequency
    lcd = pick_family(["Segoe UI Semibold", "Segoe UI", "Bahnschrift", "Inter", "Helvetica Neue",
                       "DejaVu Sans", "Helvetica"])
    lcd_w = "normal" if "semibold" in lcd.lower() else "bold"
    F.update(
        ui=tkfont.Font(family=ui, size=9),
        ui_b=tkfont.Font(family=ui, size=9, weight="bold"),
        small=tkfont.Font(family=ui, size=8),
        small_b=tkfont.Font(family=ui, size=7, weight="bold"),
        btn=tkfont.Font(family=ui, size=8, weight="bold"),
        title=tkfont.Font(family=ui, size=12, weight="bold"),
        big=tkfont.Font(family=ui, size=15, weight="bold"),
        mono=tkfont.Font(family=mono, size=10),
        mono_b=tkfont.Font(family=mono, size=10, weight="bold"),
        mono_s=tkfont.Font(family=mono, size=8, weight="bold"),
        cw=tkfont.Font(family=mono, size=14, weight="bold"),
        freq=tkfont.Font(family=lcd, size=40, weight=lcd_w),
        freq_s=tkfont.Font(family=lcd, size=24, weight=lcd_w),
        sub=tkfont.Font(family=lcd, size=19, weight=lcd_w),
        sub_s=tkfont.Font(family=lcd, size=12, weight=lcd_w),
        lcd=tkfont.Font(family=ui, size=8, weight="bold"),
        lcd_s=tkfont.Font(family=ui, size=7, weight="bold"),
        model=tkfont.Font(family=ui, size=13, weight="bold"),
    )


def rrect(c, x1, y1, x2, y2, r, **kw):
    r = max(1, min(r, (x2 - x1) / 2, (y2 - y1) / 2))
    pts = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y2 - r, x2, y2,
           x2 - r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
    return c.create_polygon(pts, smooth=True, **kw)


class RoundButton(tk.Canvas):
    """Flat rounded button / status chip drawn on a canvas. Can be a lit toggle."""
    TONES = {"accent": (ACCENT, ACCENT_DIM), "green": (GREEN, GREEN_DIM),
             "amber": (AMBER, AMBER_DIM), "red": (RED, RED_DIM)}

    def __init__(self, parent, text, command=None, width=64, height=28, tone="accent",
                 font=None, radius=6, solid=False, style="key"):
        bg = parent.cget("bg")
        super().__init__(parent, width=px(width), height=px(height), bg=bg,
                         highlightthickness=0, bd=0, cursor="hand2" if command else "")
        self.text = text
        self.command = command
        self.tone = tone
        self.font = font or F["btn"]
        self.radius = px(radius)
        self.solid = solid
        self.style = style          # "key" = rubber key on the case, "soft" = touch-screen soft key
        self.active = False
        self.dim_active = False
        self.hover = False
        self.down = False
        self.bind("<Configure>", lambda e: self.redraw())
        if command:
            self.bind("<Enter>", lambda e: self._set(hover=True))
            self.bind("<Leave>", lambda e: self._set(hover=False, down=False))
            self.bind("<ButtonPress-1>", lambda e: self._set(down=True))
            self.bind("<ButtonRelease-1>", self._release)
        self.redraw()

    def _set(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)
        self.redraw()

    def _release(self, e):
        was = self.down
        self._set(down=False)
        if was and 0 <= e.x <= self.winfo_width() and 0 <= e.y <= self.winfo_height():
            self.command()

    def set_active(self, on, text=None, tone=None, dim=False):
        on = bool(on)
        if (on, text or self.text, tone or self.tone, dim) == (self.active, self.text, self.tone, self.dim_active):
            return
        self.active, self.dim_active = on, dim
        if text is not None:
            self.text = text
        if tone is not None:
            self.tone = tone
        self.redraw()

    def set_text(self, text):
        if text != self.text:
            self.text = text
            self.redraw()

    def redraw(self):
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w < 4:
            w, h = int(self["width"]), int(self["height"])
        hi, lo = self.TONES.get(self.tone, self.TONES["accent"])
        if self.style == "soft":
            self._draw_soft(w, h, hi)
            return
        # Rubber key: drop shadow, body, top highlight, and an LED strip when switched on
        lit_solid = self.active and self.solid and not self.dim_active
        if lit_solid:
            fill, tc = hi, "#111111"
        else:
            fill = BTN_DOWN if self.down else (BTN_HOVER if self.hover else BTN)
            tc = TEXT if self.command else DIM
        off = 1 if self.down else 0
        rrect(self, 1, 2, w - 2, h - 1, self.radius, fill=KEY_SHADOW, outline="")
        rrect(self, 1, 1 + off, w - 2, h - 3 + off, self.radius, fill=fill,
              outline=lerp_color(fill, "#000000", 0.35))
        if not self.down:
            r = self.radius
            self.create_line(1 + r, 2, w - 2 - r, 2, fill=lerp_color(fill, "#ffffff", 0.14))
        if self.active and not self.solid:
            led = lo if self.dim_active else hi
            lw = max(px(14), min(px(26), w * 0.35))
            self.create_line(w / 2 - lw / 2, px(4) + off, w / 2 + lw / 2, px(4) + off, fill=led,
                             width=px(2), capstyle="round")
            tc = TEXT if not self.dim_active else MUTED
        self.create_text(w / 2, h / 2 + off + (px(1) if self.active and not self.solid else 0),
                         text=self.text, fill=tc, font=self.font)

    def _draw_soft(self, w, h, hi):
        """Touch-screen soft key, like the menu keys along the bottom of the radio's display."""
        if self.active:
            top, bot, outline, tc = "#3b78e0", SOFTKEY_ON, "#7fb0ff", "#ffffff"
        else:
            top = SOFTKEY_HI if self.hover else lerp_color(SOFTKEY, "#ffffff", 0.06)
            bot, outline, tc = SOFTKEY, "#4d5563", LCD_TEXT
        rrect(self, 1, 1, w - 2, h - 2, self.radius, fill=bot, outline=outline)
        rrect(self, 2, 2, w - 3, h / 2, max(1, self.radius - 1), fill=top, outline="")
        self.create_text(w / 2, h / 2, text=self.text, fill=tc, font=self.font)


class LcdTag:
    """Indicator drawn on the display canvas (MAIN, mode, FIL, TX, BUSY ...). Same API as a chip."""

    def __init__(self, changed, text, tone="accent", solid=False, hide_off=True):
        self.changed = changed
        self.text = text
        self.tone = tone
        self.solid = solid
        self.hide_off = hide_off
        self.active = False
        self.dim_active = False

    def set_active(self, on, text=None, tone=None, dim=False):
        new = (bool(on), text if text is not None else self.text, tone or self.tone, dim)
        if new != (self.active, self.text, self.tone, self.dim_active):
            self.active, self.text, self.tone, self.dim_active = new
            self.changed()

    def set_text(self, text):
        self.set_active(self.active, text)


class LevelSlider(tk.Canvas):
    """Slim horizontal slider (0-255): click / drag / wheel. Optional centre detent."""

    def __init__(self, parent, command=None, maxval=255, center=False, color=ACCENT):
        super().__init__(parent, width=px(110), height=px(26), bg=parent.cget("bg"), highlightthickness=0,
                         cursor="hand2")
        self.maxval = maxval
        self.value = 0
        self.known = False
        self.command = command
        self.center = center
        self.color = color
        self.bg_col = parent.cget("bg")
        self.bind("<Configure>", lambda e: self.redraw())
        self.bind("<Button-1>", self._drag)
        self.bind("<B1-Motion>", self._drag)
        self.bind("<MouseWheel>", lambda e: self._nudge(3 if e.delta > 0 else -3))
        self.bind("<Button-4>", lambda e: self._nudge(3))
        self.bind("<Button-5>", lambda e: self._nudge(-3))
        if center:
            self.bind("<Double-Button-1>", lambda e: self._apply(128))

    def set(self, v):
        self.value = max(0, min(self.maxval, float(v)))
        self.known = True
        self.redraw()

    def get(self):
        return self.value

    def _apply(self, v):
        self.value = max(0, min(self.maxval, int(round(v))))
        self.known = True
        self.redraw()
        if self.command:
            self.command(self.value)

    def _drag(self, e):
        pad = px(10)
        w = max(self.winfo_width(), 2 * pad + 20)
        self._apply((e.x - pad) / (w - 2 * pad) * self.maxval)

    def _nudge(self, d):
        self._apply(self.value + d)

    LED_OFF = "#3a0b09"          # unlit red LED
    LED_ON = "#ff2b1c"           # fully lit
    LED_HOT = "#ffd0c4"          # the hot centre of a bright LED

    def brightness(self):
        """0..1: how brightly the LED knob glows. Higher value = brighter; centre sliders glow
        brighter the further they are from the centre."""
        frac = self.value / self.maxval if self.maxval else 0
        return abs(frac - 0.5) * 2 if self.center else frac

    def redraw(self):
        self.delete("all")
        pad = px(10)
        w = max(self.winfo_width(), 2 * pad + 20)
        h = self.winfo_height() if self.winfo_height() > 4 else px(26)
        cy = h / 2
        x = pad + (self.value / self.maxval) * (w - 2 * pad)
        bg = self.bg_col
        b = self.brightness() if self.known else 0.0
        r = px(9)
        if self.known and b > 0.05:                               # glow around a lit LED, under the groove
            for i in range(4, 0, -1):
                rr = r + px(i * 1.2)
                self.create_oval(x - rr, cy - rr, x + rr, cy + rr, outline="",
                                 fill=lerp_color(bg, self.LED_ON, b * 0.16 * (5 - i) / 4))
        # recessed square groove
        gh = px(3)
        self.create_rectangle(pad, cy - gh, w - pad, cy + gh, fill="#0e0f11", outline="#050506")
        self.create_line(pad, cy + gh + 1, w - pad, cy + gh + 1, fill="#3f434a")      # lower lip highlight
        # level fill inside the groove
        if self.known:
            x0 = pad + 0.5 * (w - 2 * pad) if self.center else pad
            self.create_rectangle(min(x, x0), cy - gh + 1, max(x, x0), cy + gh - 1, fill=self.color, outline="")
        # scale ticks under the groove
        for k in range(11):
            tx = pad + k * (w - 2 * pad) / 10
            tl = px(4) if k in (0, 5, 10) else px(2)
            self.create_line(tx, cy + gh + px(3), tx, cy + gh + px(3) + tl, fill="#5c616a")
        # red LED knob in a black bezel, glowing brighter as the value rises
        lit = 0.08 + 0.92 * b                                     # never quite dark once known
        self.create_oval(x - r + 1, cy - r + 2, x + r + 2, cy + r + 3, fill="#060708", outline="")   # shadow
        self.create_oval(x - r, cy - r, x + r, cy + r, fill="#141518", outline="#4a4f57")            # bezel
        lr = r - px(2.5)
        if not self.known:
            lens = "#3a3d42"
        else:
            lens = lerp_color(self.LED_OFF, self.LED_ON, lit)
        self.create_oval(x - lr, cy - lr, x + lr, cy + lr, fill=lens, outline="#050505")
        if self.known:                                            # brighter core, hotter as it rises
            for i, f in enumerate((0.72, 0.48, 0.26)):
                cr = lr * f
                col = lerp_color(lens, self.LED_HOT, b * (0.25 + 0.25 * i))
                self.create_oval(x - cr, cy - cr, x + cr, cy + cr, fill=col, outline="")
        hr = max(1.0, lr * 0.32)                                  # glass highlight
        hx, hy = x - lr * 0.38, cy - lr * 0.42
        self.create_oval(hx - hr, hy - hr * 0.7, hx + hr, hy + hr * 0.7, outline="",
                         fill=lerp_color(lens, "#ffffff", 0.45 if self.known else 0.25))


# -----------------------------------------------------------------
# 4b. PHONE / BROWSER ACCESS (built-in web page, no extra packages)
# -----------------------------------------------------------------
WEB_DEFAULT_PORT = 8073

# ---- Audio for the phone: radio RX audio out, phone microphone in (IC-9700 "USB Audio CODEC") ----
AUDIO_RATE = 16000          # sent to / from the phone as 8-bit mu-law, 128 kbit/s each way
AUDIO_BLOCK = 640           # samples per packet = 40 ms
AUDIO_AUTO = "Auto (USB Audio CODEC)"
TX_STREAM_HOLD = 60            # s the TX audio stream stays open after an over while a phone listens
SQL_LEVEL_KEY = 0x03           # this program's squelch level (level_vals key)
WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
_ULAW = []


def _ulaw_tables():
    if not _ULAW:
        def enc(s):
            sign = 0x80 if s < 0 else 0
            s = min(abs(s), 32635) + 0x84
            e, mask = 7, 0x4000
            while e > 0 and not s & mask:
                e -= 1
                mask >>= 1
            return ~(sign | (e << 4) | ((s >> (e + 3)) & 0x0F)) & 0xFF

        def dec(u):
            u = ~u & 0xFF
            s = ((((u & 0x0F) << 3) + 0x84) << ((u >> 4) & 7)) - 0x84
            return -s if u & 0x80 else s
        # encoder table is indexed by the sample read as unsigned 16-bit
        _ULAW[:] = [bytes(enc(v - 65536 if v >= 32768 else v) for v in range(65536)),
                    array("h", (dec(u) for u in range(256)))]
    return _ULAW


def ulaw_encode(pcm):
    enc = _ulaw_tables()[0]
    a = array("H")
    a.frombytes(pcm[:len(pcm) & ~1])
    return bytes(map(enc.__getitem__, a))


def ulaw_decode(data):
    dec = _ulaw_tables()[1]
    return array("h", map(dec.__getitem__, data)).tobytes()


def _decimate3(pcm):
    """48 kHz -> 16 kHz (average of each 3 samples)."""
    a = array("h")
    a.frombytes(pcm[:len(pcm) & ~1])
    return array("h", ((a[i] + a[i + 1] + a[i + 2]) // 3 for i in range(0, len(a) - 2, 3))).tobytes()


def _upsample3(pcm):
    """16 kHz -> 48 kHz (linear interpolation)."""
    a = array("h")
    a.frombytes(pcm[:len(pcm) & ~1])
    out = array("h")
    n = len(a)
    for i, s in enumerate(a):
        nx = a[i + 1] if i + 1 < n else s
        out.extend((s, (2 * s + nx) // 3, (s + 2 * nx) // 3))
    return out.tobytes()


class AudioEngine:
    """Radio receive audio (from the rig's USB codec) to phone listeners, and phone microphone audio
    to the rig's USB codec. Streams are only open while a phone is listening / talking."""

    def __init__(self, app):
        self.app = app
        self.lock = threading.Lock()          # listeners, transmit buffer
        self.slock = threading.RLock()        # opening / closing streams
        self.listeners = set()
        self.in_stream = None
        self.in_rate = AUDIO_RATE
        self.out_stream = None
        self.out_rate = AUDIO_RATE
        self.out_fail = 0.0
        self.txbuf = bytearray()
        self.tx_primed = False
        self.tx_last = 0.0
        self.tx_owner = None
        self.error = ""
        self.sql_open_time = 0.0
        self.in_name = ""
        self.tx_ready = 0.0

    @staticmethod
    def devices(kind):
        """(index, name) of input or output devices, MME only on Windows (it converts sample rates)."""
        try:
            apis = sd.query_hostapis()
            devs = sd.query_devices()
        except Exception:
            return []
        mme = next((i for i, h in enumerate(apis) if h["name"] == "MME"), None)
        key = "max_input_channels" if kind == "input" else "max_output_channels"
        return [(i, d["name"]) for i, d in enumerate(devs) if d[key] > 0 and (mme is None or d["hostapi"] == mme)]

    def _find(self, kind):
        wanted = self.app.config.get("audio_in" if kind == "input" else "audio_out", AUDIO_AUTO)
        for attempt in (0, 1):
            devs = self.devices(kind)
            if wanted and wanted != AUDIO_AUTO:
                for i, n in devs:
                    if n == wanted:
                        return i
            for i, n in devs:
                if "usb audio codec" in " ".join(n.lower().split()):
                    return i
            if attempt == 0 and self.in_stream is None and self.out_stream is None:
                try:                    # look again, in case the radio was plugged in after start-up
                    sd._terminate()
                    sd._initialize()
                except Exception:
                    break
        what = "radio audio input" if kind == "input" else "radio audio output"
        raise RuntimeError(f"{what} not found ({wanted}) - is the IC-9700 USB cable connected?")

    def _open(self, kind, cb):
        dev = self._find(kind)
        try:
            name = sd.query_devices(dev)["name"]
        except Exception:
            name = f"device {dev}"
        if kind == "input":
            self.in_name = name
        cls = sd.RawInputStream if kind == "input" else sd.RawOutputStream
        last = None
        for rate in (AUDIO_RATE, 48000):
            try:
                s = cls(device=dev, samplerate=rate, channels=1, dtype="int16",
                        blocksize=AUDIO_BLOCK * rate // AUDIO_RATE, latency="low", callback=cb)
                s.start()
                return s, rate
            except Exception as e:
                last = e
        raise RuntimeError(str(last))

    @staticmethod
    def _close(s):
        if s is not None:
            try:
                s.stop()
                s.close()
            except Exception:
                pass

    # ---- receive
    def add_listener(self, l):
        with self.lock:
            self.listeners.add(l)
        with self.slock:
            if self.in_stream is None:
                try:
                    self.in_stream, self.in_rate = self._open("input", self._in_cb)
                    self.error = ""
                except Exception as e:
                    self.error = f"RX audio: {e}"
                    return self.error
        return ""

    def remove_listener(self, l):
        with self.lock:
            self.listeners.discard(l)
            empty = not self.listeners
            if self.tx_owner is l:
                self.tx_owner = None
        if empty:
            with self.slock:
                s, self.in_stream = self.in_stream, None
            self._close(s)

    def listener_count(self):
        with self.lock:
            return len(self.listeners)

    def status(self):
        """One line for the phone's AUDIO tab."""
        if self.in_stream is None:
            return ""
        txt = f"Listening on: {self.in_name} ({self.in_rate // 1000} kHz)"
        if self.squelched():
            txt += " \u00b7 MUTED: rig squelch is closed"
        return txt

    def squelched(self):
        """True when the phone audio should be muted because the rig's squelch is closed.
        The IC-9700 USB audio output ignores squelch unless its menu says otherwise."""
        app = self.app
        if not app.config.get("audio_sql", True) or not app.running or app.is_tx:
            return False
        if not app.sql_in_use():                          # squelch fully open (usual on HF): never mute
            return False
        lv = app.level_vals.get(SQL_LEVEL_KEY)
        if lv is not None and lv <= 0:                   # squelch turned fully down: always open
            return False
        is_open, when = app.sql_live
        now = time.time()
        if is_open is None or now - when > 2.0:          # no fresh squelch reading: don't mute
            return False
        if is_open:
            self.sql_open_time = now
            return False
        return now - self.sql_open_time > 0.25           # short hang so word endings aren't clipped

    def _in_cb(self, indata, frames, t, status):          # PortAudio thread
        if self.squelched():
            data = b"\xff" * (frames if self.in_rate == AUDIO_RATE else frames // 3)   # mu-law silence
        else:
            pcm = bytes(indata)
            if self.in_rate != AUDIO_RATE:
                pcm = _decimate3(pcm)
            data = ulaw_encode(pcm)
        with self.lock:
            ls = list(self.listeners)
        for l in ls:
            l.push(data)

    # ---- transmit
    def prepare_tx(self):
        """Open the radio's audio input (our output) before keying, so the first syllable isn't lost."""
        self.tx_ready = time.time()
        if self.out_stream is not None:
            return ""
        with self.slock:
            if self.out_stream is None:
                if time.time() - self.out_fail < 3:
                    return self.error
                try:
                    self.out_stream, self.out_rate = self._open("output", self._out_cb)
                    self.error = ""
                except Exception as e:
                    self.out_fail = time.time()
                    self.error = f"TX audio: {e}"
                    return self.error
        return ""

    def tx_pending(self):
        """Bytes of phone microphone audio still waiting to be played to the radio."""
        with self.lock:
            return len(self.txbuf)

    def feed(self, owner, ulaw):
        """Microphone audio from a phone. Returns an error text, or ''."""
        now = time.time()
        with self.lock:
            if self.tx_owner is not owner and self.tx_owner is not None and now - self.tx_last < 1.0:
                return ""                              # another phone is talking
            self.tx_owner = owner
            self.txbuf += ulaw_decode(ulaw)
            if len(self.txbuf) > AUDIO_RATE:           # more than 0.5 s queued: drop the oldest part
                del self.txbuf[:len(self.txbuf) - AUDIO_RATE // 2]
            self.tx_last = now
        if self.out_stream is None:
            with self.slock:
                if self.out_stream is None:
                    if now - self.out_fail < 3:
                        return self.error
                    try:
                        self.out_stream, self.out_rate = self._open("output", self._out_cb)
                        self.error = ""
                    except Exception as e:
                        self.out_fail = now
                        self.error = f"TX audio: {e}"
                        return self.error
        return ""

    def _out_cb(self, outdata, frames, t, status):        # PortAudio thread
        need = (frames if self.out_rate == AUDIO_RATE else frames // 3) * 2
        with self.lock:
            if not self.tx_primed and len(self.txbuf) >= 2 * AUDIO_BLOCK * 2:      # 80 ms jitter buffer
                self.tx_primed = True
            if self.tx_primed and len(self.txbuf) >= need:
                chunk = bytes(self.txbuf[:need])
                del self.txbuf[:need]
            else:
                chunk = None
                self.tx_primed = False
        size = len(outdata)
        if chunk is None:
            outdata[:] = bytes(size)
            return
        if self.out_rate != AUDIO_RATE:
            chunk = _upsample3(chunk)
        outdata[:] = chunk[:size].ljust(size, b"\0")

    def idle_check(self):
        """Close the transmit stream when no phone has talked for a while (Tk thread). It stays open
        between overs while a phone is listening, so keying again doesn't have to wait for it."""
        hold = TX_STREAM_HOLD if self.listener_count() else 3
        if self.out_stream is not None and time.time() - max(self.tx_last, self.tx_ready) > hold:
            with self.slock:
                s, self.out_stream = self.out_stream, None
            self._close(s)
            with self.lock:
                self.txbuf.clear()
                self.tx_primed = False

    def restart(self):
        """Re-open streams after the device choice changed."""
        with self.slock:
            a, self.in_stream = self.in_stream, None
            b, self.out_stream = self.out_stream, None
        self._close(a)
        self._close(b)
        self.out_fail = 0.0
        if self.listener_count():
            with self.slock:
                try:
                    self.in_stream, self.in_rate = self._open("input", self._in_cb)
                    self.error = ""
                except Exception as e:
                    self.error = f"RX audio: {e}"

    def close(self):
        with self.lock:
            self.listeners.clear()
        self.restart()


MORSE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", ".-.-.-": ".", "--..--": ",",
    "..--..": "?", "-..-.": "/", "-...-": "=", "-....-": "-", ".--.-.": "@", "---...": ":",
    ".----.": "'", "-.-.--": "!", ".-.-.": "<AR>", "...-.-": "<SK>", "-.--.": "<KN>",
    ".-...": "<AS>", "-.-.-": "<KA>", "........": "<HH>", "...-.": "<SN>",
}
CWD_RATE = 4000                     # decoder works at 4 kHz (16 kHz radio audio averaged in fours)
CWD_BLOCK = 40                      # 10 ms per detection block
CWD_TONES = list(range(300, 1201, 50))
# sensitivity: (longest window in 10 ms blocks, window per dot, signal gate, key-down level, key-up level);
# the levels are multiples of the noise. Longer windows follow the measured speed.
CWD_SENS = {"Low": (1, 0.0, 8.0, 3.5, 2.5), "Normal": (1, 0.0, 6.0, 3.0, 2.0),
            "High": (2, 0.5, 4.5, 2.4, 1.7), "Max": (4, 0.7, 3.0, 1.8, 1.4),
            "Auto": (4, 0.6, 3.0, 1.8, 1.4)}     # Auto backs off to High's levels while it sees junk
CWD_SENS_NAMES = ["Auto", "Low", "Normal", "High", "Max"]


class CwDecoder:
    """CW decoder on the radio's USB receive audio. Finds the tone (or uses the rig's CW pitch),
    follows the signal level and the sending speed by itself, and turns dots and dashes into text."""

    def __init__(self, app):
        self.app = app
        self.q = deque(maxlen=100)                  # 4 s of 40 ms audio packets
        self.ev = threading.Event()
        self.active = False
        self.error = ""
        self.text = ""                              # everything decoded since CLEAR (last 4000 characters)
        self.on_text = None                         # callbacks, run on the Tk thread
        self.tone_mode = app.config.get("cwd_tone", "Auto")
        self.sens = app.config.get("cwd_sens", "Auto")
        self.coef = {f: 2.0 * math.cos(2 * math.pi * f / CWD_RATE) for f in CWD_TONES}
        self.reset()

    def reset(self):
        self.buf = []
        self.peak_by = {f: 0.0 for f in CWD_TONES}
        self.floor_by = {f: None for f in CWD_TONES}
        self.tone = 700
        self.floor = None
        self.peak = 0.0
        self.nblk = 0                               # blocks since start: the noise level settles first
        self.hist = []                              # the last few 10 ms blocks, for the longer windows
        self.win_n = 2
        self.junk_n = 0                             # Auto: recent junk (static crashes, unreadable letters)
        self.junk_at = -10000
        self.backoff = False
        self.key = False                            # signal present now
        self.pend = False                           # a mark has ended but a short dip could still join it
        self.mark = 0                               # length of the current mark, 10 ms blocks
        self.gap = 0                                # length of the current gap
        self.unit = 6.0                             # dot length in 10 ms blocks (20 WPM to start with)
        self.marks = []                             # recent mark lengths, for telling dots from dashes
        self.sym = ""
        self.spaced = True
        self.held = ""                              # a lone E / T waiting to see what follows
        self.level = 0.0
        self.snr_ok = False

    # ---- start / stop (Tk thread)
    def start(self):
        if self.active:
            return ""
        if self.app.audio is None:
            self.error = "Audio isn't set up on the PC: run  py -m pip install sounddevice  and restart."
            return self.error
        self.reset()
        self.active = True
        threading.Thread(target=self._worker, daemon=True).start()
        err = self.app.audio.add_listener(self)
        if err:
            self.stop()
            self.error = err
            return err
        self.error = ""
        return ""

    def stop(self):
        if not self.active:
            return
        self.active = False
        self.ev.set()
        if self.app.audio is not None:
            self.app.audio.remove_listener(self)

    def clear(self):
        self.text = ""
        self.sym = ""
        self.held = ""
        self.spaced = True

    def wpm(self):
        return int(round(120.0 / max(1.0, self.unit)))

    # ---- audio in (PortAudio thread): just queue it
    def push(self, ulaw):
        self.q.append(ulaw)
        self.ev.set()

    # ---- processing thread
    def _worker(self):
        while self.active:
            self.ev.wait(0.5)
            self.ev.clear()
            while self.q and self.active:
                try:
                    data = self.q.popleft()
                except IndexError:
                    break
                pcm = array("h", map(_ulaw_tables()[1].__getitem__, data))
                b = self.buf
                for i in range(0, len(pcm) - 3, 4):
                    b.append((pcm[i] + pcm[i + 1] + pcm[i + 2] + pcm[i + 3]) * 0.25)
                while len(b) >= CWD_BLOCK:
                    self._block(b[:CWD_BLOCK])
                    del b[:CWD_BLOCK]

    @staticmethod
    def _goertzel(x, coef):
        s1 = s2 = 0.0
        for v in x:
            s1, s2 = v + coef * s1 - s2, s1
        return s1 * s1 + s2 * s2 - coef * s1 * s2

    def _rig_pitch(self):
        v = self.app.level_vals.get(0x09)                # IC-9700 CW pitch: 0-255 = 300-900 Hz
        return int(round((300 + v / 255 * 600) / 10) * 10) if isinstance(v, (int, float)) else 600

    def sens_params(self):
        """(window in 10 ms blocks, signal gate, key-down level, key-up level) for the sensitivity setting.
        A longer window is a narrower filter, so weaker signals stand out of the noise, but it smears
        fast CW, so the window follows the measured speed (about half to two-thirds of a dot)."""
        cap, per_dot, gate, on_k, off_k = CWD_SENS.get(self.sens, CWD_SENS["Auto"])
        if self.sens not in CWD_SENS or self.sens == "Auto":
            self.backoff = self.nblk - self.junk_at < 2000 and self.junk_n >= 3   # junk in the last 20 s
            if self.backoff:
                gate, on_k, off_k = CWD_SENS["High"][2:]
        m = self.marks
        known = len(m) >= 6 and max(m) >= 2 * min(m)       # speed measured from dots and dashes
        want = max(1, min(cap if known else min(cap, 3), int(self.unit * per_dot + 0.5)))
        n = self.win_n
        if want != n and not self.key and not self.pend and self.gap > 3 * self.unit:
            self.win_n = n = want                         # only change between characters
        return min(n, cap), gate, on_k, off_k

    def _block(self, x):
        self.nblk += 1
        settle = self.nblk < 40
        rate = 0.1 if settle else 0.02
        quiet = not self.key and not self.pend               # between marks: update the noise average
        n, gate, on_k, off_k = self.sens_params()
        h = self.hist
        h.append(x)
        del h[:-4]
        win = [v for blk in h[-n:] for v in blk]
        k = len(win) // CWD_BLOCK
        if self.tone_mode == "Rig pitch":
            f = self._rig_pitch()
        else:                                              # Auto: the tone standing furthest above its noise
            sw = [v for blk in h[-min(k, 2):] for v in blk]
            ks = len(sw) // CWD_BLOCK
            for f in CWD_TONES:
                m = math.sqrt(max(0.0, self._goertzel(sw, self.coef[f]))) / ks
                pk, fl = self.peak_by[f], self.floor_by[f]
                if fl is None:
                    fl = m
                self.peak_by[f] = m if m > pk else pk + (m - pk) * 0.003
                if m < 3.0 * fl or settle:
                    self.floor_by[f] = fl + (m - fl) * rate
            score = {f: self.peak_by[f] / max(1.0, self.floor_by[f]) for f in CWD_TONES}
            best = max(score, key=score.get)
            if best != self.tone and score[best] > gate + 2.0 and score[best] > 1.3 * score[self.tone] \
                    and quiet and not settle:
                self.tone = best
                self.peak = self.peak_by[best]
                self.floor = self.floor_by[best] * math.sqrt(ks / k)
                self.sym = ""
            f = self.tone
        self.tone = f
        coef = self.coef.get(f) or 2.0 * math.cos(2 * math.pi * f / CWD_RATE)
        mag = math.sqrt(max(0.0, self._goertzel(win, coef))) / k
        # a keyed tone is narrow; static crashes and clicks are wide: compare with 300 Hz either side
        ref = 0.0
        for rf in ((f - 300, f + 300) if f >= 500 else (f + 300, f + 450)):
            ref += math.sqrt(max(0.0, self._goertzel(win, 2.0 * math.cos(2 * math.pi * rf / CWD_RATE)))) / k
        narrow = mag > 2.0 * (ref / 2)
        # signal level tracking
        if self.floor is None:
            self.floor = mag
        fl, pk = self.floor, self.peak
        if (quiet and mag < 3.0 * fl) or settle:
            self.floor = fl + (mag - fl) * rate
        self.peak = (pk + (mag - pk) * 0.5) if mag > pk else (pk + (mag - pk) * 0.003)
        fl = max(1.0, self.floor)
        span = self.peak - fl
        self.snr_ok = self.peak > gate * fl and self.peak > 150 and not settle
        self.level = 0.0 if span <= 0 else max(0.0, min(1.0, (mag - fl) / span))
        if not self.snr_ok or not narrow:
            down = False
        elif self.key:
            down = mag > max(fl + 0.35 * span, off_k * fl)
        else:
            down = mag > max(fl + 0.5 * span, on_k * fl)
        self._timing(down)

    def _timing(self, down):
        """Key state per 10 ms block. A dip shorter than a fraction of a dot doesn't end a mark."""
        u = self.unit
        if down:
            if self.key:
                self.mark += 1
            elif self.pend and self.gap < max(2.0, 0.35 * u):
                self.mark += self.gap + 1                  # a short dip inside a mark
                self.key, self.pend, self.gap = True, False, 0
            else:
                self.key, self.mark, self.gap = True, 1, 0
            return
        if self.key:
            self.key, self.pend, self.gap = False, True, 1
        else:
            self.gap += 1
        if self.pend and self.gap >= max(2.0, 0.35 * u):
            self.pend = False
            self._mark_done(self.mark)
        if not self.pend:
            g = self.gap
            if self.sym and g > 2.0 * self.unit:
                self._emit(MORSE.get(self.sym, "*"))
                self.sym = ""
            elif not self.sym and not self.spaced and g > 5.0 * self.unit:
                self._emit(" ")

    def _mark_done(self, n):
        u = self.unit
        if n < max(1.5, 0.3 * u):                          # a click or a burst of noise
            return
        m = self.marks
        m.append(n)
        del m[:-12]
        lo, hi = min(m), max(m)
        if len(m) >= 3 and hi >= 2.0 * lo:                 # dots and dashes both seen: split them
            c1, c2 = float(lo), float(hi)
            for _ in range(6):
                t = (c1 + c2) / 2
                a = [x for x in m if x < t]
                b = [x for x in m if x >= t]
                if not a or not b:
                    break
                c1, c2 = sum(a) / len(a), sum(b) / len(b)
            thr = (c1 + c2) / 2
            self.unit = u + ((c1 + c2 / 3.0) / 2 - u) * 0.3
        else:
            thr = 2.0 * u
            self.unit = u + ((n if n < thr else n / 3.0) - u) * 0.2
        self.unit = max(1.5, min(30.0, self.unit))
        self.sym = (self.sym + ("." if n < thr else "-"))[-9:]

    def _junk(self):
        self.junk_n = min(6, self.junk_n + 1 if self.nblk - self.junk_at < 2000 else 1)
        self.junk_at = self.nblk

    def _emit(self, ch):
        """Pass a character on. A lone E or T standing as a whole word is nearly always a static
        crash, so it is held back until the next character shows it is part of a word."""
        if self.held:
            if ch == " ":                                  # E / T alone: drop it
                self.held = ""
                self._junk()
                return
            ch, self.held = self.held + ch, ""
        elif self.spaced and ch in ("E", "T"):
            self.held = ch
            return
        if "*" in ch:
            self._junk()
        elif ch.strip() and self.nblk - self.junk_at > 1000:
            self.junk_n = max(0, self.junk_n - 1)          # good copy: forget old junk slowly
        self.spaced = ch.endswith(" ")
        self.text = (self.text + ch)[-4000:]
        cb = self.on_text
        if cb is not None:
            self.app.ui(cb, ch)


class WsConn:
    """Minimal WebSocket (RFC 6455) on an already upgraded, blocking socket."""

    def __init__(self, sock):
        self.sock = sock
        self.wlock = threading.Lock()
        self.tls = isinstance(sock, ssl.SSLSocket)
        self.rlock = self.wlock if self.tls else threading.Lock()    # OpenSSL: never read and write at once

    def send(self, opcode, payload=b""):
        n = len(payload)
        if n < 126:
            hdr = bytes((0x80 | opcode, n))
        elif n < 65536:
            hdr = bytes((0x80 | opcode, 126)) + n.to_bytes(2, "big")
        else:
            hdr = bytes((0x80 | opcode, 127)) + n.to_bytes(8, "big")
        with self.wlock:
            self.sock.sendall(hdr + payload)

    def send_json(self, obj):
        self.send(0x1, json.dumps(obj).encode("utf-8"))

    def _read(self, n, idle_ok=False):
        buf = bytearray()
        deadline = time.time() + 10
        while len(buf) < n:
            if self.tls and self.sock.pending():
                r = True
            else:
                r, _, _ = select.select([self.sock], [], [], 1.0)
            if not r:
                if idle_ok and not buf:
                    raise socket.timeout()
                if time.time() > deadline:
                    raise ConnectionError("stalled")
                continue
            with self.rlock:
                try:
                    chunk = self.sock.recv(n - len(buf))
                except ssl.SSLWantReadError:
                    continue
            if not chunk:
                raise ConnectionError("closed")
            buf += chunk
        return bytes(buf)

    def recv(self):
        """One message as (opcode, payload). Raises socket.timeout after ~1 s with nothing received."""
        msg_op, parts, total = None, [], 0
        while True:
            b1, b2 = self._read(2, idle_ok=msg_op is None)
            op, n = b1 & 0x0F, b2 & 0x7F
            if n == 126:
                n = int.from_bytes(self._read(2), "big")
            elif n == 127:
                n = int.from_bytes(self._read(8), "big")
            total += n
            if total > 1 << 16:
                raise ConnectionError("message too big")
            mask = self._read(4) if b2 & 0x80 else None
            data = self._read(n) if n else b""
            if mask and n:
                m = (mask * (n // 4 + 1))[:n]
                data = (int.from_bytes(data, "little") ^ int.from_bytes(m, "little")).to_bytes(n, "little")
            if op >= 0x8:
                return op, data
            if op:
                msg_op = op
            parts.append(data)
            if b1 & 0x80:
                return msg_op, b"".join(parts)


class PttWorker:
    """Keys / unkeys the radio for one phone, straight from its connection (not via the window's
    queue), so PTT reaches the radio in one CI-V exchange. On release it lets the last few
    words already sent from the phone play out before unkeying."""

    def __init__(self, app, notify):
        self.app, self.notify = app, notify
        self.want = False
        self.state = False
        self.closed = False
        self.ev = threading.Event()
        threading.Thread(target=self._run, daemon=True).start()

    def set(self, on):
        self.want = bool(on)
        self.ev.set()

    def _run(self):
        app, eng = self.app, self.app.audio
        while not self.closed:
            self.ev.wait(0.5)
            self.ev.clear()
            while self.want != self.state and not self.closed:
                if self.want:
                    err = eng.prepare_tx() if eng is not None else ""
                    ok, why = app.fast_ptt(True)
                    self.state = ok
                    if not ok:
                        self.want = False
                    self.notify({"ptt_ack": ok, "why": why or err})
                else:
                    t0 = time.time()
                    while eng is not None and eng.tx_pending() > 2 * AUDIO_BLOCK // 2 and time.time() - t0 < 0.4:
                        time.sleep(0.02)
                    app.fast_ptt(False)
                    self.state = False
                    self.notify({"ptt_ack": False})
        if self.state:
            self.app.fast_ptt(False)
            self.state = False

    def close(self):
        self.closed = True
        self.want = False
        self.ev.set()


class AudioSession:
    """One phone's audio link. Receive audio is queued and sent by a small thread, dropping old
    packets rather than letting the delay grow when the network is slow."""

    def __init__(self, ws):
        self.ws = ws
        self.q = deque(maxlen=12)            # ~0.5 s
        self.ev = threading.Event()
        self.closed = False
        threading.Thread(target=self._sender, daemon=True).start()

    def push(self, data):
        self.q.append(data)
        self.ev.set()

    def _sender(self):
        while not self.closed:
            self.ev.wait(1.0)
            self.ev.clear()
            while not self.closed:
                try:
                    data = self.q.popleft()
                except IndexError:
                    break
                try:
                    self.ws.send(0x2, data)
                except OSError:
                    self.close()

    def close(self):
        self.closed = True
        self.ev.set()
        try:
            self.ws.sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass


def fetch_ts_cert(name=None):
    """Ask Tailscale for this PC's https certificate. Returns (True, dns name) or (False, reason).
    Reason "NOT_ENABLED" means HTTPS certificates are switched off for the tailnet."""
    code, out = run_tailscale(["status", "--json"], timeout=10)
    if code is None:
        return False, out
    try:
        st = json.loads(out)
    except ValueError:
        return False, "Tailscale status could not be read:\n" + out
    if st.get("BackendState") not in (None, "Running"):
        return False, f"Tailscale is not connected on this PC (state: {st.get('BackendState')}). Connect it and try again."
    me = (st.get("Self") or {}).get("DNSName", "").rstrip(".")
    domains = [d.rstrip(".") for d in (st.get("CertDomains") or [])]
    if not domains:
        return False, "NOT_ENABLED"
    name = name or (me if me in domains else domains[0])
    tmp_c, tmp_k = CERT_PATH + ".new", KEY_PATH + ".new"
    code, out = run_tailscale(["cert", "--cert-file", tmp_c, "--key-file", tmp_k, name], timeout=120)
    if code != 0 or not (os.path.exists(tmp_c) and os.path.exists(tmp_k)):
        low = (out or "").lower()
        if "not enabled" in low or "does not support" in low or "https" in low and "enable" in low:
            return False, "NOT_ENABLED"
        return False, out or "No reply from Tailscale."
    os.replace(tmp_c, CERT_PATH)
    os.replace(tmp_k, KEY_PATH)
    return True, name


def tailscale_exe():
    p = shutil.which("tailscale")
    if p:
        return p
    for c in (r"C:\Program Files\Tailscale\tailscale.exe", r"C:\Program Files (x86)\Tailscale\tailscale.exe"):
        if os.path.exists(c):
            return c
    return None


def run_tailscale(args, timeout=15):
    """Run the Tailscale CLI. Returns (exit code or None, output text)."""
    exe = tailscale_exe()
    if not exe:
        return None, "The Tailscale command-line tool was not found. Is Tailscale installed on this PC?"
    flags = 0x08000000 if sys.platform == "win32" else 0          # CREATE_NO_WINDOW
    try:
        p = subprocess.Popen([exe] + list(args), stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, creationflags=flags)
    except OSError as e:
        return None, str(e)
    try:
        out, _ = p.communicate(timeout=timeout)
        return p.returncode, (out or b"").decode("utf-8", "replace").strip()
    except subprocess.TimeoutExpired:
        p.kill()
        out, _ = p.communicate()
        return None, (out or b"").decode("utf-8", "replace").strip()


WEB_PAGE = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1b1c1f">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<title>IC-9700</title>
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icon-512.png">
<link rel="apple-touch-icon" href="icon-512.png">
<style>
:root{--bg:#1b1c1f;--panel:#232529;--text:#eef1f5;--muted:#9aa1ab;--dim:#5c616a;--accent:#5ab8ff;
--key:#33363b;--border:#393c42;--red:#ff4a3d;--green:#3ddc84;--orange:#ffa62b;--main:#1f5fc4;--lbl:#a8b3c3}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;background:var(--bg);color:var(--text);font:15px/1.3 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
body{padding:env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left)}
#app{max-width:560px;margin:0 auto;padding:8px 10px 100px}
[hidden]{display:none!important}
header{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted);padding:2px 2px 8px}
.led{width:9px;height:9px;border-radius:50%;background:var(--dim);flex:none}
.led.ok{background:var(--green)}.led.warn{background:var(--orange)}.led.off{background:var(--red)}
#status{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#vd{color:var(--green);font-weight:700}#utc{font-variant-numeric:tabular-nums}
#net{background:#4d1512;color:#ffd7d3;border-radius:8px;padding:10px 12px;margin-bottom:8px;font-size:13px}
.lcd{background:#000;border:1px solid #2d3139;border-radius:10px;padding:8px 10px 10px}
.tags{display:flex;align-items:center;gap:5px;flex-wrap:wrap;min-height:22px}
.tag{font:700 11px system-ui,sans-serif;padding:2px 7px;border:1px solid var(--lbl);border-radius:3px;color:#fff;letter-spacing:.03em}
.tag.main{background:var(--main);border-color:var(--main)}
.tag.amber{color:var(--orange);border-color:var(--orange)}
.tag.solid.green{background:var(--green);border-color:var(--green);color:#000}
.tag.solid.red{background:var(--red);border-color:var(--red);animation:blink 1s steps(2) infinite}
.tag.subtag{background:#4a5160;border-color:#4a5160}
.sp{flex:1}.lbl{color:var(--lbl);font:700 12px system-ui,sans-serif}
.freq{font-weight:600;font-variant-numeric:tabular-nums;font-size:clamp(42px,15.5vw,76px);text-align:center;
line-height:1.05;padding:6px 0 4px;touch-action:none;user-select:none;-webkit-user-select:none;cursor:ew-resize}
.freq small{font-size:.6em}.freq.dim{color:#3b4250}
.ticks{position:relative;height:14px;margin:0 6px 1px 26px;font:700 10px system-ui,sans-serif;color:#fff}
.ticks span{position:absolute;transform:translateX(-50%);white-space:nowrap}.ticks span.r{color:var(--red)}
.meter{display:flex;align-items:center;gap:8px}
.mlabel{width:18px;font-weight:700}
.bar{flex:1;height:14px;background:#14171d;position:relative;margin-right:6px}
#mfill{position:absolute;inset:0;background:linear-gradient(90deg,#2f8bff 49.8%,#ff4a3d 49.8%);clip-path:inset(0 100% 0 0)}
.bar::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,transparent 0 4px,#000 4px 6px)}
#mpeak{position:absolute;top:-2px;bottom:-2px;width:3px;background:var(--orange);z-index:1}
.mtext{display:flex;justify-content:space-between;gap:8px;font:700 13px ui-monospace,Menlo,Consolas,monospace;padding:5px 0 7px;color:#fff;min-height:28px}
#info{color:var(--lbl);text-align:right}
.sub{display:flex;align-items:center;gap:8px;border-top:1px solid #1e2530;padding-top:7px}
#subfreq{margin-left:auto;font-size:22px;font-weight:600;font-variant-numeric:tabular-nums;color:var(--lbl)}
#scope{display:block;width:100%;height:130px;margin-top:8px;border-radius:4px;cursor:crosshair}
nav{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin:10px 0}
button{font:700 13px system-ui,sans-serif;color:var(--text);background:var(--key);border:1px solid #1f2124;border-radius:8px;
min-height:44px;padding:0 4px;box-shadow:0 2px 0 #0b0c0d,inset 0 1px 0 rgba(255,255,255,.08);touch-action:manipulation;
user-select:none;-webkit-user-select:none}
button:active{transform:translateY(1px);box-shadow:0 1px 0 #0b0c0d}
button.on{background:#244a6e;color:#fff;box-shadow:inset 0 -3px 0 var(--accent),0 2px 0 #0b0c0d}
nav button{background:#2a2e36;border-color:#4d5563;min-height:38px;font-size:12px}
nav button.on{background:#2d63c8;border-color:#7fb0ff;box-shadow:none}
.grid{display:grid;gap:6px}.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}.g5{grid-template-columns:repeat(5,1fr)}
.page{display:none;background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:10px}.page.on{display:block}
h3{font:700 11px system-ui,sans-serif;letter-spacing:.08em;color:var(--muted);margin:14px 2px 6px;text-transform:uppercase}
h3:first-child{margin-top:2px}
.row{display:flex;gap:6px;align-items:center}
.big{font-size:24px;flex:1;min-height:58px}
select,input[type=text]{background:#101113;color:var(--text);border:1px solid var(--border);border-radius:8px;min-height:44px;
font:600 16px system-ui,sans-serif;padding:0 10px;min-width:0}
#step{flex:1.1;text-align:center}#fin{flex:1;font-variant-numeric:tabular-nums}
.unit{color:var(--muted)}button.go{background:#1e5a36;min-width:64px}
label.sel{display:flex;align-items:center;gap:8px}label.sel span{color:var(--muted);font:700 12px system-ui,sans-serif;width:38px}
label.sel select{flex:1}
.rit button{flex:1}#ritv{flex:1.4;text-align:center;font:700 14px ui-monospace,Menlo,monospace;color:var(--accent)}
.lv{display:grid;grid-template-columns:78px 1fr 58px;align-items:center;gap:8px;min-height:42px}
.lv span{color:var(--muted);font-size:13px}.lv b{text-align:right;font:700 13px ui-monospace,Menlo,monospace}
input[type=range]{width:100%;accent-color:var(--accent);height:32px;margin:0}
.mem{display:flex;width:100%;gap:10px;align-items:center;text-align:left;margin-bottom:6px;padding:8px 10px;min-height:52px}
.mem .mn{flex:1;min-width:0}.mem .mn div{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.mem .mi{color:var(--muted);font-weight:500;font-size:12px}
.mem .mf{font:700 15px ui-monospace,Menlo,monospace;color:var(--accent)}
.hint{color:var(--muted);font-size:13px;margin:6px 2px}
.cwdt{min-height:64px;max-height:150px;overflow-y:auto;background:#000;color:#fff;font:700 17px ui-monospace,Menlo,monospace;padding:8px 10px;border-radius:8px;margin-top:6px;white-space:pre-wrap;word-break:break-word;border:1px solid var(--border)}
.cwdt:empty:before{content:'Decoded CW appears here';color:var(--dim);font-weight:500;font-size:13px}
.foot{color:var(--dim);font-size:11px;text-align:center;margin-top:14px}
.offline .page button,.offline .page select,.offline .page input{opacity:.45}
#dock{position:fixed;left:0;right:0;bottom:0;z-index:20;background:rgba(21,22,24,.97);border-top:1px solid var(--border);
padding:8px 10px calc(8px + env(safe-area-inset-bottom))}
#dock .in{max-width:560px;margin:0 auto;display:grid;grid-template-columns:1fr 2.2fr;gap:8px}
#dock button{min-height:58px;font-size:14px}
#abtn.on{background:#1e5a36;box-shadow:inset 0 -3px 0 var(--green),0 2px 0 #0b0c0d}
#ptt{background:#4a2020;font-size:15px;letter-spacing:.04em;touch-action:none}
#ptt.tx{background:var(--red);color:#fff;box-shadow:0 0 0 3px rgba(255,74,61,.35)}
#ptt.rig{background:#7a4a10;color:#fff}
.mbar{height:10px;background:#14171d;border-radius:3px;overflow:hidden}.mbar div{height:100%;width:0;background:var(--green)}
.chk{display:flex;align-items:center;gap:10px;min-height:44px;color:var(--text);font-size:14px}
.chk input{width:22px;height:22px;flex:none;accent-color:var(--accent)}
.warn{color:var(--orange);font-size:13px;margin:6px 2px}
.instbtn{display:block;width:100%;margin-top:14px;background:#1f5fc4;color:#fff;border-color:#2d63c8}
.pwr{min-height:30px;padding:0 10px;font-size:12px;border-radius:6px;box-shadow:none;background:#33363b;flex:none}
.pwr.on{background:#1e5a36;color:#fff;box-shadow:inset 0 -3px 0 var(--green)}
.pwr.off{background:#4a2020;color:#ffd7d3}
.hbtn{min-height:30px;padding:0 10px;font-size:12px;background:#1f5fc4;border-color:#2d63c8;color:#fff;border-radius:6px;box-shadow:none}
.ov{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:40;display:flex;align-items:center;justify-content:center;padding:16px}
.ovbox{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:16px;max-width:420px;width:100%}
.ovbox h3{margin:0 0 10px;font-size:13px}.ovbox p{margin:0 0 10px;font-size:15px;line-height:1.45}
.ovbox button{width:100%;margin-top:6px}
.golink{display:flex;align-items:center;justify-content:center;min-height:48px;margin:8px 0;border-radius:8px;
background:#1e5a36;color:#fff;font-weight:800;text-decoration:none}
#toast{position:fixed;left:50%;bottom:80px;transform:translateX(-50%);background:#2d63c8;color:#fff;padding:8px 14px;border-radius:8px;
font-size:13px;opacity:0;transition:opacity .2s;pointer-events:none;z-index:30;white-space:nowrap}
#toast.show{opacity:1}
@keyframes blink{50%{opacity:.35}}
</style></head>
<body>
<div id="app">
<header><button id="pwr" class="pwr">&#9211; POWER</button><span id="led" class="led"></span><span id="status">Connecting&hellip;</span><span id="vd"></span><span id="utc"></span></header>
<div id="net" hidden>Can't reach the PC. Check that IC9700 Monitor is running and that Tailscale is connected on both the PC and this phone.</div>
<section class="lcd">
 <div class="tags"><span class="tag main">MAIN</span><span id="mode" class="tag">--</span><span id="fil" class="tag" hidden></span>
 <span id="dup" class="tag amber" hidden></span><span id="sat" class="tag" hidden>SAT</span><span id="scan" class="tag amber" hidden>SCAN</span>
 <span id="bandlbl" class="lbl"></span><span class="sp"></span>
 <span id="busy" class="tag solid green" hidden>BUSY</span><span id="txb" class="tag solid red" hidden>TX</span></div>
 <div id="freq" class="freq dim">---.---<small>.--</small></div>
 <div id="ticks" class="ticks"></div>
 <div class="meter"><span id="mlab" class="mlabel">S</span><div class="bar"><div id="mfill"></div><div id="mpeak" hidden></div></div></div>
 <div class="mtext"><span id="mtext"></span><span id="info"></span></div>
 <div class="sub"><span class="tag subtag">SUB</span><span id="submode" class="lbl"></span><span id="subfreq">---.---</span></div>
 <div id="scopewrap" hidden><canvas id="scope"></canvas></div>
</section>
<nav><button id="tTUNE">TUNE</button><button id="tFUNC">FUNC</button><button id="tLEVELS">LEVELS</button><button id="tMEM">MEMORY</button><button id="tAUDIO">AUDIO</button></nav>
<section id="pTUNE" class="page">
 <div class="row"><button id="dn" class="big" aria-label="Tune down">&#9664;</button><select id="step" aria-label="Tuning step"></select>
 <button id="up" class="big" aria-label="Tune up">&#9654;</button></div>
 <h3>Band</h3><div id="bands" class="grid g3"></div>
 <h3>Frequency</h3><div class="row"><input id="fin" type="text" inputmode="decimal" placeholder="145.500" autocomplete="off">
 <span class="unit">MHz</span><button id="setf" class="go">SET</button></div>
 <h3>Mode</h3><div id="modes" class="grid g5"></div>
 <div id="fils" class="grid g4" style="margin-top:6px"></div>
 <h3>Main / Sub &middot; Scope</h3><div class="grid g4"><button id="swap" style="grid-column:span 2">MAIN &#8644; SUB</button><button id="scopebtn">SCOPE</button><button id="spanbtn">SPAN</button></div>
 <div class="grid g2" style="margin-top:6px"><button id="spandn">SPAN &minus;</button><button id="spanup">SPAN +</button></div>
</section>
<section id="pFUNC" class="page">
 <h3>Functions</h3><div id="toggles" class="grid g4"></div>
 <h3>Duplex / split</h3><div id="dups" class="grid g4"></div>
 <h3>Repeater tone (CTCSS)</h3><div class="grid g2"><label class="sel"><span>TONE</span><select id="tone"></select></label>
 <label class="sel"><span>TSQL</span><select id="tsql"></select></label></div>
 <h3>RIT</h3><div class="row rit"><button data-rit="-50">&minus;50</button><button data-rit="-10">&minus;10</button><span id="ritv">+0 Hz</span>
 <button data-rit="10">+10</button><button data-rit="50">+50</button><button data-rit="clr">CLR</button></div>
 <h3>CW decoder</h3><div class="row"><button id="cwdb" style="flex:none;padding:0 14px">DECODER OFF</button><span id="cwdi" class="hint" style="flex:1"></span><button id="cwdc" style="flex:none;padding:0 12px">CLEAR</button></div>
 <div class="row" style="margin-top:6px"><label class="sel" style="flex:none"><span style="width:auto">Sensitivity</span><select id="cwds"><option>Auto</option><option>Low</option><option>Normal</option><option>High</option><option>Max</option></select></label><span id="cwdn" class="hint" style="flex:1"></span></div>
 <div id="cwdt" class="cwdt"></div>
</section>
<section id="pLEVELS" class="page"><div id="levels"></div><p class="hint">Double-tap a PBT slider to centre it.</p></section>
<section id="pMEM" class="page"><div id="mems"><p class="hint">Loading&hellip;</p></div></section>
<section id="pAUDIO" class="page">
 <div id="ahttps" hidden><p class="warn">Receive audio works here, but phones only allow the microphone on the secure <b>https://</b> page.</p>
 <a id="ahlink" class="golink" hidden>Open the secure page</a>
 <p id="ahnone" class="hint">To set it up, on the PC: Settings &rsaquo; Phone access&hellip; &rsaquo; <b>Turn on HTTPS</b>.</p></div>
 <p id="aerr" class="warn" hidden></p>
 <h3>Receive</h3>
 <div class="lv"><span>Volume</span><input id="vol" type="range" min="0" max="300" step="5"><b id="volv"></b></div>
 <div class="lv"><span>RX level</span><div class="mbar"><div id="rxlv"></div></div><b></b></div>
 <label class="chk"><input id="asql" type="checkbox">Mute when the rig's squelch is closed</label>
 <p id="ainfo" class="hint"></p>
 <p id="asqlnote" class="warn" hidden>Muted: the rig's squelch is closed. Turn the squelch down (LEVELS) or untick the box above.</p>
 <h3>Transmit</h3>
 <div class="lv"><span>Mic gain</span><input id="micg" type="range" min="0" max="300" step="5"><b id="micgv"></b></div>
 <label class="sel"><span style="width:78px">TX tone</span><select id="txeq"><option value="full">Full (no bass cut)</option><option value="clear">Clear (bass cut, presence lift)</option><option value="crisp">Crisp (strong bass cut, more presence)</option></select></label>
 <div class="lv"><span>Mic level</span><div class="mbar"><div id="miclv"></div></div><b></b></div>
 <label class="chk"><input id="mproc" type="checkbox">Phone voice processing (noise suppression, echo cancel, auto gain). Off = clearer TX audio</label>
 <label class="chk"><input id="latch" type="checkbox">Tap TALK to switch transmit on and off (instead of hold to talk)</label>
 <p class="hint">Tap <b>AUDIO</b> to hear the radio. Hold <b>TALK</b> to transmit with this phone's microphone.
 Transmit stops by itself if the phone's connection or microphone drops, when you leave this page, and at the PTT time-out set on the PC.</p>
 <p class="hint">Radio menu: SET &rsaquo; Connectors &rsaquo; MOD Input &rsaquo; DATA OFF MOD = <b>USB</b> (DATA MOD = USB for data modes).
 On iPhone, turn the ring/silent switch off to hear audio; headphones avoid the receive audio dropping to the earpiece once the mic is on.</p>
</section>
<button id="instbtn" class="instbtn" hidden>&#11015; INSTALL AS AN APP</button>
<div id="instov" class="ov" hidden><div class="ovbox"><h3>INSTALL AS AN APP</h3><div id="insttxt"></div><button id="instok">OK</button></div></div>
<p class="foot">IC9700 Monitor <span id="ver"></span> &middot; GM0OTB<br>Drag the frequency sideways to tune &middot; tap the scope to tune there</p>
</div>
<div id="dock"><div class="in"><button id="abtn">AUDIO OFF</button><button id="ptt">HOLD TO TALK</button></div></div>
<div id="toast"></div>
<script>
"use strict";
const CFG=__CFG__;
const $=id=>document.getElementById(id);
function el(tag,props,kids){const e=document.createElement(tag);if(props)Object.assign(e,props);if(kids)for(const k of kids)e.append(k);return e;}
const LS={get(k,d){try{const v=localStorage.getItem(k);return v===null?d:v}catch(e){return d}},set(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
let S=null;

// ---------------- commands to the PC (sent one after another, in order)
let chain=Promise.resolve(),pending=0;
function send(cmd){
  pending++;
  chain=chain.then(()=>fetch('api/cmd',{method:'POST',credentials:'same-origin',
    headers:{'Content-Type':'application/json','X-IC9700':'1'},body:JSON.stringify(cmd)}).catch(()=>{}))
    .then(()=>{pending--;kick();});
}
let toastT=null;
function toast(msg){const t=$('toast');t.textContent=msg;t.classList.add('show');clearTimeout(toastT);toastT=setTimeout(()=>t.classList.remove('show'),1600);}

// ---------------- polling
let pollT=null,inflight=false,again=false,fails=0;
async function poll(){
  if(inflight){again=true;return;}
  inflight=true;clearTimeout(pollT);
  try{
    const r=await fetch('api/state',{cache:'no-store',credentials:'same-origin'});
    if(r.status===401){location.reload();return;}
    if(!r.ok)throw new Error(r.status);
    S=await r.json();fails=0;$('net').hidden=true;render();
  }catch(e){if(++fails>2){$('net').hidden=false;$('led').className='led off';$('status').textContent='PC not reachable';}}
  inflight=false;
  pollT=setTimeout(poll,again?50:(document.hidden?2000:300));again=false;
}
function kick(){if(inflight)again=true;else{clearTimeout(pollT);pollT=setTimeout(poll,50);}}
document.addEventListener('visibilitychange',()=>{if(!document.hidden)kick();});

// ---------------- helpers
function fmtHz(hz){
  if(hz==null)return '---.---<small>.--</small>';
  const m=Math.floor(hz/1e6),k=Math.floor(hz%1e6/1000),h=Math.floor(hz%1000/10);
  return m+'.'+String(k).padStart(3,'0')+'<small>.'+String(h).padStart(2,'0')+'</small>';
}
function levelText(fmt,v){
  if(v==null)return '--';
  if(fmt==='pbt'){const n=Math.round((v-128)/127*100);return (n>=0?'+':'')+n;}
  if(fmt==='pitch')return Math.round(300+v/255*600)+'Hz';
  if(fmt==='wpm')return Math.round(6+v/255*42)+'wpm';
  return Math.round(v/255*100)+'%';
}
function stepHz(){return +$('step').value||1000;}
function stepTune(d){if(pending>2)return;send({a:'step',dir:d,step:stepHz()});}
function holdButton(b,fn){
  let t1=null,t2=null;
  const stop=()=>{clearTimeout(t1);clearInterval(t2);t1=t2=null;};
  b.addEventListener('pointerdown',e=>{e.preventDefault();stop();fn();t1=setTimeout(()=>{t2=setInterval(fn,150);},450);});
  for(const ev of ['pointerup','pointerleave','pointercancel'])b.addEventListener(ev,stop);
  b.addEventListener('contextmenu',e=>e.preventDefault());
}

// ---------------- build the pages
const TABS=['TUNE','FUNC','LEVELS','MEM','AUDIO'];
function showTab(n){
  for(const t of TABS){$('p'+t).classList.toggle('on',t===n);$('t'+t).classList.toggle('on',t===n);}
  LS.set('tab',n);if(n==='MEM')loadMem();
}
let stepFromRig=!LS.get('step',null);
function build(){
  $('ver').textContent=CFG.version;
  for(const t of TABS)$('t'+t).onclick=()=>showTab(t);
  const st=$('step');
  for(const [lab,hz] of CFG.steps)st.append(el('option',{value:String(hz),textContent:lab}));
  st.value=LS.get('step','12500');
  st.onchange=()=>{LS.set('step',st.value);stepFromRig=false;};
  holdButton($('dn'),()=>stepTune(-1));holdButton($('up'),()=>stepTune(1));
  for(const b of CFG.bands){const x=el('button',{textContent:b,onclick:()=>send({a:'band',band:b})});x.dataset.band=b;$('bands').append(x);}
  for(const m of CFG.modes){const x=el('button',{textContent:m,onclick:()=>send({a:'mode',mode:m})});x.dataset.mode=m;$('modes').append(x);}
  for(const n of [1,2,3]){const x=el('button',{textContent:'FIL'+n,onclick:()=>send({a:'filter',n})});x.dataset.fil=n;$('fils').append(x);}
  $('fils').append(toggleBtn('data'));
  $('setf').onclick=directEntry;$('fin').addEventListener('keydown',e=>{if(e.key==='Enter')directEntry();});
  $('swap').onclick=()=>send({a:'swap'});
  $('scopebtn').onclick=()=>{if(S)send({a:'scope',on:!S.scope_on});};
  $('cwdb').onclick=()=>send({a:'cwdec',on:!(S&&S.cwd&&S.cwd.on)});
  $('cwdc').onclick=()=>{send({a:'cwd_clear'});$('cwdt').textContent='';};
  $('cwds').onchange=e=>{send({a:'cwd_sens',v:e.target.value});cwdsTouched=Date.now();};
  $('pwr').onclick=()=>{
    if(!S||!S.online){toast('The PC has no USB connection to the radio');return;}
    if(S.rig_on){if(confirm('Switch the IC-9700 OFF?')){send({a:'power',on:false});toast('Switching off…');}}
    else{send({a:'power',on:true});toast('Switching on… (takes a few seconds)');}
  };
  $('spanbtn').onclick=()=>send({a:'span',dir:1,wrap:1});$('spanup').onclick=()=>send({a:'span',dir:1});
  $('spandn').onclick=()=>send({a:'span',dir:-1});
  for(const k of ['pamp','att','agc','nb','nr','anf','comp','vox','mon','bkin','tone','tsql','rit','sat','lock'])$('toggles').append(toggleBtn(k));
  for(const [lab,code] of [['SIMP',16],['DUP−',17],['DUP+',18],['SPLIT',1]]){
    const x=el('button',{textContent:lab,onclick:()=>send({a:'dup',code:(code===1&&S&&S.dup===1)?0:code})});x.dataset.dup=code;$('dups').append(x);
  }
  for(const id of ['tone','tsql']){
    const s=$(id);for(const t of CFG.ctcss)s.append(el('option',{value:t.toFixed(1),textContent:t.toFixed(1)+' Hz'}));
    s.onchange=()=>send({a:'tone',sql:id==='tsql',t:+s.value});
  }
  document.querySelectorAll('[data-rit]').forEach(b=>b.onclick=()=>{
    if(!S)return;const d=b.dataset.rit;send({a:'rit',hz:d==='clr'?0:S.rit+(+d)});});
  const lv=$('levels');
  for(const [label,sub,fmt] of CFG.levels){
    const r=el('input',{type:'range',min:0,max:255,step:1,value:fmt==='pbt'?128:0});
    const v=el('b',{textContent:'--'});
    r.dataset.sub=sub;r.dataset.fmt=fmt;
    let t=null;
    const push=()=>{t=null;send({a:'level',sub,v:+r.value});};
    r.addEventListener('input',()=>{touched[sub]=Date.now();v.textContent=levelText(fmt,+r.value);if(!t)t=setTimeout(push,120);});
    r.addEventListener('change',()=>{touched[sub]=Date.now();clearTimeout(t);push();});
    if(fmt==='pbt')r.addEventListener('dblclick',()=>{r.value=128;touched[sub]=Date.now();v.textContent=levelText(fmt,128);push();});
    lv.append(el('div',{className:'lv'},[el('span',{textContent:label}),r,v]));
    lvRows.push([sub,fmt,r,v]);
  }
  buildAudio();
  // drag the frequency sideways to tune
  const f=$('freq');let x0=null,acc=0;
  f.addEventListener('pointerdown',e=>{x0=e.clientX;acc=0;try{f.setPointerCapture(e.pointerId);}catch(_){}});
  f.addEventListener('pointermove',e=>{if(x0===null)return;acc+=e.clientX-x0;x0=e.clientX;
    while(Math.abs(acc)>=22){const d=Math.sign(acc);acc-=d*22;stepTune(d);}});
  for(const ev of ['pointerup','pointercancel'])f.addEventListener(ev,()=>{x0=null;});
  $('scope').addEventListener('click',scopeClick);
  showTab(TABS.includes(LS.get('tab','TUNE'))?LS.get('tab','TUNE'):'TUNE');
}
const touched={},lvRows=[];
function toggleBtn(k){const x=el('button',{textContent:CFG.toggles[k],onclick:()=>send({a:'toggle',key:k})});x.dataset.key=k;x.dataset.label=CFG.toggles[k];return x;}
function directEntry(){
  const v=parseFloat($('fin').value.replace(',','.'));
  if(!(v>=0.1&&v<=2000)){toast('Enter MHz, e.g. 145.500');return;}
  send({a:'tune',hz:Math.round(v*1e6)});$('fin').value='';$('fin').blur();
}

// ---------------- memories
let memRev=null;
async function loadMem(){
  try{const r=await fetch('api/memories',{cache:'no-store',credentials:'same-origin'});if(r.ok)renderMem(await r.json());}catch(e){}
}
function renderMem(list){
  const box=$('mems');box.textContent='';
  if(!list.length){box.append(el('p',{className:'hint',textContent:'No memories yet. Save some on the PC (MEMORY tab), or use "Read from radio" there.'}));return;}
  for(const m of list){
    box.append(el('button',{className:'mem',onclick:()=>{send({a:'mem',i:m.i});toast('Recalled '+m.name);}},[
      el('span',{className:'mn'},[el('div',{textContent:m.name}),el('div',{className:'mi',textContent:[m.ch,m.mode,m.info].filter(Boolean).join(' · ')})]),
      el('span',{className:'mf',textContent:m.mhz})]));
  }
}

// ---------------- render
let tickMode=null;
function setTicks(tx){
  if(tickMode===tx)return;tickMode=tx;const t=$('ticks');t.textContent='';
  for(const [l,f] of (tx?CFG.pwr_ticks:CFG.s_ticks)){const s=el('span',{textContent:l});s.style.left=(f*100)+'%';if(!tx&&f>CFG.s9)s.className='r';t.append(s);}
}
function showTag(id,text,show){const e=$(id);e.hidden=!show;if(show)e.textContent=text;}
let cwdsTouched=0;
function render(){
  const s=S,on=s.online;
  document.body.classList.toggle('offline',!on);
  const pw=$('pwr');pw.classList.toggle('on',!!s.rig_on);pw.classList.toggle('off',!s.rig_on);
  pw.innerHTML=s.rig_on?'&#9211; ON':'&#9211; OFF';
  $('led').className='led '+(!on?'off':(s.link?'ok':'warn'));
  $('status').textContent=on?((s.rig||'Rig')+(s.link?' · online':' · no reply from rig')):(s.status||'Radio offline');
  $('vd').textContent=s.vd?s.vd.toFixed(1)+' V':'';
  $('utc').textContent=s.utc?s.utc+' UTC':'';
  $('freq').innerHTML=fmtHz(s.hz);$('freq').classList.toggle('dim',s.hz==null);
  $('mode').textContent=s.mode||'--';
  showTag('fil',s.fil?'FIL'+s.fil:'',!!s.fil);
  const dupt={1:'SPLIT',17:'DUP-',18:'DUP+'}[s.dup];showTag('dup',dupt,!!dupt);
  const sat=s.toggles.sat;$('sat').hidden=!(sat&&sat[0]);
  $('scan').hidden=!s.scan;
  $('bandlbl').textContent=s.band||'';
  $('busy').hidden=!s.busy;$('txb').hidden=!s.tx;
  // meter
  const tx=s.meter==='tx';setTicks(tx);
  $('mlab').textContent=tx?'Po':'S';
  const frac=Math.max(0,Math.min(1,tx?s.pwr:s.mfrac));
  $('mfill').style.clipPath='inset(0 '+(100-frac*100).toFixed(1)+'% 0 0)';
  $('mfill').className=tx?'tx':'';
  const pk=$('mpeak');pk.hidden=tx||!(s.peak>0);pk.style.left='calc('+(s.peak*100).toFixed(1)+'% - 1px)';
  $('mtext').textContent=s.mtext||'';
  $('mtext').style.color=tx?['#3ddc84','#ffa62b','#ff4a3d'][s.swr_sev]||'#fff':(s.mfrac>CFG.s9?'#ff4a3d':'#fff');
  $('info').textContent=s.info||'';$('info').style.color=tx?'#ffa62b':'';
  // sub band
  $('submode').textContent=s.sub_hz!=null?[s.sub_mode,s.sub_band].filter(Boolean).join(' '):'';
  $('subfreq').innerHTML=s.sub_hz!=null?fmtHz(s.sub_hz):'---.---';
  // buttons
  document.querySelectorAll('[data-mode]').forEach(b=>b.classList.toggle('on',b.dataset.mode===s.mode));
  document.querySelectorAll('[data-fil]').forEach(b=>b.classList.toggle('on',+b.dataset.fil===s.fil));
  document.querySelectorAll('[data-band]').forEach(b=>b.classList.toggle('on',b.dataset.band===s.band));
  document.querySelectorAll('[data-dup]').forEach(b=>b.classList.toggle('on',+b.dataset.dup===s.dup));
  document.querySelectorAll('[data-key]').forEach(b=>{const t=s.toggles[b.dataset.key];b.classList.toggle('on',!!(t&&t[0]));
    const txt=t?t[1]:b.dataset.label;if(b.textContent!==txt)b.textContent=txt;});
  $('scopebtn').classList.toggle('on',!!s.scope_on);
  $('spanbtn').textContent=s.span?('±'+(s.span>=1e6?(s.span/1e6)+'M':(s.span/1000)+'k')):'SPAN';
  if(stepFromRig&&s.step){$('step').value=String(s.step);stepFromRig=false;}
  for(const [id,val] of [['tone',s.tone],['tsql',s.tsql]]){const e=$(id);if(document.activeElement!==e&&val)e.value=val;}
  $('ritv').textContent=(s.rit>=0?'+':'')+s.rit+' Hz';
  const now=Date.now();
  for(const [sub,fmt,r,v] of lvRows){
    if(now-(touched[sub]||0)<2500)continue;
    const val=s.levels[sub];
    if(val!=null)r.value=val;
    v.textContent=levelText(fmt,val);
  }
  {const c=s.cwd||{},b=$('cwdb'),t=$('cwdt');b.classList.toggle('on',!!c.on);b.textContent=c.on?'DECODER ON':'DECODER OFF';
   $('cwdi').textContent=c.info||'';$('cwdn').textContent=c.sens_note||'';
   if(c.sens&&Date.now()-cwdsTouched>2500&&document.activeElement!==$('cwds'))$('cwds').value=c.sens;
   if(t.textContent!==(c.text||'')){const end=t.scrollTop+t.clientHeight>=t.scrollHeight-4;t.textContent=c.text||'';if(end)t.scrollTop=t.scrollHeight;}}
  updAudioUi();
  if(s.mem_rev!==memRev){const first=memRev===null;memRev=s.mem_rev;if(!first&&$('pMEM').classList.contains('on'))loadMem();}
  drawScope();
}

// ---------------- spectrum scope (no waterfall)
let scopeGeom=null;
function mhz3(hz){return (hz/1e6).toFixed(3);}
function drawScope(){
  const s=S;$('scopewrap').hidden=!s.scope_on;
  if(!s.scope_on){scopeGeom=null;return;}
  const sc=$('scope'),sx=sc.getContext('2d'),dpr=window.devicePixelRatio||1,W=sc.clientWidth,H=sc.clientHeight;
  if(!W||!H)return;
  if(sc.width!==Math.round(W*dpr)||sc.height!==Math.round(H*dpr)){sc.width=Math.round(W*dpr);sc.height=Math.round(H*dpr);}
  sx.setTransform(dpr,0,0,dpr,0,0);
  const lab=14,sh=H-lab;
  sx.fillStyle='#00040e';sx.fillRect(0,0,W,sh);
  sx.strokeStyle='#0b1a33';sx.lineWidth=1;sx.beginPath();
  for(let k=1;k<10;k++){const x=Math.round(W*k/10)+.5;sx.moveTo(x,0);sx.lineTo(x,sh);}
  for(let k=1;k<4;k++){const y=Math.round(sh*k/4)+.5;sx.moveTo(0,y);sx.lineTo(W,y);}
  sx.stroke();
  sx.fillStyle='#000';sx.fillRect(0,sh,W,lab);
  const sp=s.scope;
  if(!sp||!sp.d.length){
    sx.fillStyle='#a8b3c3';sx.font='600 12px system-ui,sans-serif';sx.textAlign='center';
    sx.fillText(s.online?'Waiting for scope data…':'Radio offline',W/2,sh/2+4);scopeGeom=null;return;
  }
  const d=sp.d,n=d.length,pts=[];
  for(let i=0;i<n;i++)pts.push([n>1?i/(n-1)*W:W/2,sh-1-Math.min(d[i],160)/160*(sh-6)]);
  sx.beginPath();sx.moveTo(0,sh);for(const [x,y] of pts)sx.lineTo(x,y);sx.lineTo(W,sh);sx.closePath();sx.fillStyle='#123b8f';sx.fill();
  sx.beginPath();pts.forEach(([x,y],i)=>i?sx.lineTo(x,y):sx.moveTo(x,y));sx.strokeStyle='#dce9ff';sx.stroke();
  const mk=sp.mk||s.hz;
  if(mk&&sp.hi>sp.lo&&mk>=sp.lo&&mk<=sp.hi){
    const xm=(mk-sp.lo)/(sp.hi-sp.lo)*W;sx.strokeStyle='#ff4a3d';sx.beginPath();sx.moveTo(xm,0);sx.lineTo(xm,sh);sx.stroke();
    sx.fillStyle='#ff4a3d';sx.beginPath();sx.moveTo(xm-4,0);sx.lineTo(xm+4,0);sx.lineTo(xm,5);sx.fill();
  }
  sx.font='700 10px system-ui,sans-serif';sx.fillStyle='#a8b3c3';
  const span=(sp.hi-sp.lo)/2;sx.textAlign='left';sx.fillText(span<1e6?'±'+(span/1000)+'k':'±'+(span/1e6)+'M',4,12);
  const yb=H-3;sx.fillText(mhz3(sp.lo),4,yb);sx.textAlign='center';sx.fillText(mhz3((sp.lo+sp.hi)/2),W/2,yb);
  sx.textAlign='right';sx.fillText(mhz3(sp.hi),W-4,yb);
  scopeGeom={lo:sp.lo,hi:sp.hi,off:sp.off||0};
}
function scopeClick(e){
  if(!scopeGeom)return;const r=$('scope').getBoundingClientRect();
  const hz=scopeGeom.lo+(e.clientX-r.left)/r.width*(scopeGeom.hi-scopeGeom.lo)-scopeGeom.off,st=stepHz();
  send({a:'tune',hz:Math.round(hz/st)*st});
}
window.addEventListener('resize',()=>{if(S)drawScope();});

// ---------------- audio: radio receive audio to this phone, this phone's microphone to the radio
const AR=16000;
const ULAW=new Float32Array(256);
for(let u=0;u<256;u++){const x=~u&255,e=(x>>4)&7,s=((((x&15)<<3)+0x84)<<e)-0x84;ULAW[u]=((x&128)?-s:s)/32768;}
function ulawEnc(f){
  let s=Math.round(Math.max(-1,Math.min(1,f))*32767);const sign=s<0?0x80:0;if(s<0)s=-s;s=Math.min(s,32635)+0x84;
  let e=7,mask=0x4000;while(e>0&&!(s&mask)){e--;mask>>=1;}
  return (~(sign|(e<<4)|((s>>(e+3))&15)))&255;
}
const A={ctx:null,ws:null,want:false,on:false,tx:false,txWant:false,mic:null,rxq:[],rxpos:0,primed:false,
  vol:+LS.get('vol','1'),micg:+LS.get('micg','1'),latch:LS.get('latch','0')==='1',proc:LS.get('micproc','0')==='1',eq:LS.get('txeq','clear'),rxpk:0,micpk:0,err:'',retry:null};
function rxAvail(){let n=-A.rxpos;for(const c of A.rxq)n+=c.length;return n;}
function rxPush(u8){
  const f=new Float32Array(u8.length);for(let i=0;i<u8.length;i++)f[i]=ULAW[u8[i]];
  A.rxq.push(f);if(A.rxq.length>60){A.rxq.splice(0,A.rxq.length-20);A.rxpos=0;}
}
function onPlay(e){
  const out=e.outputBuffer.getChannelData(0),n=out.length,step=AR/A.ctx.sampleRate;
  let av=rxAvail();
  if(!A.primed){if(av>=AR*0.12)A.primed=true;else{out.fill(0);A.rxpk*=0.9;return;}}
  while(av>AR*0.5&&A.rxq.length>1){av-=A.rxq[0].length-A.rxpos;A.rxq.shift();A.rxpos=0;}   // fell behind: catch up
  const g=A.tx?0:A.vol;let pk=0;
  for(let i=0;i<n;i++){
    const c=A.rxq[0];
    if(!c){out.fill(0,i);A.rxpos=0;A.primed=false;break;}
    const i0=A.rxpos|0,fr=A.rxpos-i0,s0=c[i0],s1=i0+1<c.length?c[i0+1]:(A.rxq[1]?A.rxq[1][0]:s0);
    const v=s0+(s1-s0)*fr;out[i]=v*g;const av2=v<0?-v:v;if(av2>pk)pk=av2;
    A.rxpos+=step;
    while(A.rxq.length&&A.rxpos>=A.rxq[0].length){A.rxpos-=A.rxq[0].length;A.rxq.shift();}
  }
  A.rxpk=Math.max(pk,A.rxpk*0.85);
}
let micPos=0,micFir=null,micHist=null;
function makeFir(rate){                     // windowed-sinc low-pass, cut-off 7 kHz (below the 8 kHz Nyquist of 16 kHz)
  const N=rate>32000?63:41,M=N-1,fc=7000/rate,h=new Float32Array(N);let sum=0;
  for(let i=0;i<N;i++){const n=i-M/2,sn=n===0?2*fc:Math.sin(2*Math.PI*fc*n)/(Math.PI*n);
    const w=0.42-0.5*Math.cos(2*Math.PI*i/M)+0.08*Math.cos(4*Math.PI*i/M);h[i]=sn*w;sum+=h[i];}
  for(let i=0;i<N;i++)h[i]/=sum;h.rate=rate;return h;
}
// TX tone: 2nd-order high-pass (bass cut) + peaking presence lift, run at 16 kHz
const EQ_PRESETS={full:[[80,0.707]],clear:[[220,0.707],[2400,4,1.0]],crisp:[[300,0.707],[180,0.6],[2600,6,0.9]]};
let txEq=null,txEqName='';
function bq(b0,b1,b2,a0,a1,a2){return {b0:b0/a0,b1:b1/a0,b2:b2/a0,a1:a1/a0,a2:a2/a0,x1:0,x2:0,y1:0,y2:0};}
function bqHp(fc,q){const w=2*Math.PI*fc/AR,c=Math.cos(w),al=Math.sin(w)/(2*q);return bq((1+c)/2,-(1+c),(1+c)/2,1+al,-2*c,1-al);}
function bqPeak(fc,db,q){const g=Math.pow(10,db/40),w=2*Math.PI*fc/AR,c=Math.cos(w),al=Math.sin(w)/(2*q);
  return bq(1+al*g,-2*c,1-al*g,1+al/g,-2*c,1-al/g);}
function makeEq(name){return (EQ_PRESETS[name]||EQ_PRESETS.clear).map(p=>p.length===2?bqHp(p[0],p[1]):bqPeak(p[0],p[1],p[2]));}
function runEq(st,v){for(const f of st){const y=f.b0*v+f.b1*f.x1+f.b2*f.x2-f.a1*f.y1-f.a2*f.y2;f.x2=f.x1;f.x1=v;f.y2=f.y1;f.y1=y;v=y;}return v;}
function onMic(e){
  if(!txEq||txEqName!==A.eq){txEq=makeEq(A.eq);txEqName=A.eq;}
  const inp=e.inputBuffer.getChannelData(0),len=inp.length,sr=A.ctx.sampleRate,step=sr/AR;
  if(!micFir||micFir.rate!==sr){micFir=makeFir(sr);micHist=new Float32Array(micFir.length);micPos=0;}
  const h=micFir,N=h.length,x=new Float32Array(N+len);x.set(micHist);x.set(inp,N);micHist=x.slice(len);
  // y[0] = last filtered sample of the previous block, y[t] = filtered input sample t-1 of this block
  const y=new Float32Array(len+1);
  for(let t=0;t<=len;t++){let a=0;const b=N-1+t;for(let k=0;k<N;k++)a+=h[k]*x[b-k];y[t]=a;}
  const out=new Uint8Array(Math.ceil(len/step)+2);
  let p=micPos,k=0,pk=0;
  while(p<len){const i=p|0,f=p-i,v=runEq(txEq,y[i]+(y[i+1]-y[i])*f)*A.micg;out[k++]=ulawEnc(v);const av=v<0?-v:v;if(av>pk)pk=av;p+=step;}
  micPos=p-len;A.micpk=Math.max(pk,A.micpk*0.8);
  if(A.tx&&A.ws&&A.ws.readyState===1)A.ws.send(out.subarray(0,k));
}
function micRelease(){
  if(A.mic){try{A.mic.getTracks().forEach(t=>t.stop());}catch(_){}A.mic=null;}
  if(A.micNodes){for(const n of A.micNodes){try{n.disconnect();}catch(_){}}A.micNodes=null;}
}
function ensureCtx(){
  if(A.ctx)return;
  const C=window.AudioContext||window.webkitAudioContext;A.ctx=new C();
  const p=A.ctx.createScriptProcessor(2048,1,1);p.onaudioprocess=onPlay;p.connect(A.ctx.destination);A.play=p;
}
function audioConnect(){
  if(A.ws||!A.want)return;
  if(!S||!S.atok){clearTimeout(A.retry);A.retry=setTimeout(audioConnect,1000);return;}
  const ws=new WebSocket((location.protocol==='https:'?'wss://':'ws://')+location.host+'/api/audio?t='+encodeURIComponent(S.atok));
  ws.binaryType='arraybuffer';A.ws=ws;
  ws.onopen=()=>{A.on=true;A.err='';updAudioUi();};
  ws.onmessage=ev=>{
    if(typeof ev.data==='string'){
      let m={};try{m=JSON.parse(ev.data);}catch(_){}
      if(m.err){A.err=m.err;toast(m.err);}
      if(m.ptt_drop){A.tx=false;A.txWant=false;toast('Transmit stopped: microphone audio stopped arriving');}
      updAudioUi();return;
    }
    rxPush(new Uint8Array(ev.data));
  };
  ws.onclose=()=>{
    const wasTx=A.tx;A.ws=null;A.on=false;A.tx=false;A.rxq=[];A.rxpos=0;A.primed=false;updAudioUi();
    if(wasTx)toast('Audio link lost — transmit stopped');
    if(A.want){clearTimeout(A.retry);A.retry=setTimeout(audioConnect,2000);}
  };
}
setInterval(()=>{if(A.ws&&A.ws.readyState===1)A.ws.send('{}');},4000);
function audioToggle(){
  if(A.want){A.want=false;pttUp();clearTimeout(A.retry);if(A.ws)A.ws.close();updAudioUi();return;}
  ensureCtx();A.ctx.resume();A.want=true;audioConnect();updAudioUi();
}
async function ensureMic(){
  if(A.mic)return true;
  if(!window.isSecureContext||!navigator.mediaDevices||!navigator.mediaDevices.getUserMedia){
    toast(S&&S.https_url?'Talk needs the secure page \u2014 tap the green button':'The microphone needs the https:// page');showTab('AUDIO');return false;}
  try{A.mic=await navigator.mediaDevices.getUserMedia({audio:{channelCount:1,echoCancellation:A.proc,noiseSuppression:A.proc,autoGainControl:A.proc}});}
  catch(e){toast('Microphone not allowed ('+e.name+')');return false;}
  const src=A.ctx.createMediaStreamSource(A.mic),p=A.ctx.createScriptProcessor(2048,1,1),z=A.ctx.createGain();
  z.gain.value=0;p.onaudioprocess=onMic;src.connect(p);p.connect(z);z.connect(A.ctx.destination);A.micNodes=[src,p,z];
  return true;
}
async function pttDown(){
  if(S&&(S.tx||S.ptt)&&!A.tx&&!A.txWant){send({a:'unkey'});toast('Releasing PTT');return;}   // keyed from the PC: tap releases
  if(A.latch&&(A.tx||A.txWant)){pttUp();return;}
  A.txWant=true;updAudioUi();
  ensureCtx();A.ctx.resume();
  if(!A.want)audioToggle();
  if(!await ensureMic()){A.txWant=false;updAudioUi();return;}
  for(let i=0;i<30&&!(A.ws&&A.ws.readyState===1);i++)await new Promise(r=>setTimeout(r,100));
  if(!A.txWant)return;
  if(!(A.ws&&A.ws.readyState===1)){toast('No audio connection to the PC');A.txWant=false;updAudioUi();return;}
  if(S&&!S.online){toast('Radio is offline');A.txWant=false;updAudioUi();return;}
  A.tx=true;micPos=0;A.ws.send(JSON.stringify({ptt:true}));updAudioUi();
}
function pttUp(){
  A.txWant=false;
  if(A.tx){A.tx=false;if(A.ws&&A.ws.readyState===1)A.ws.send(JSON.stringify({ptt:false}));}
  updAudioUi();
}
function updAudioUi(){
  const ab=$('abtn');ab.classList.toggle('on',A.want&&A.on);
  ab.textContent=A.want?(A.on?(S&&S.sql_muted?'AUDIO ON \u00b7 SQL':'AUDIO ON'):'CONNECTING…'):'AUDIO OFF';
  $('asqlnote').hidden=!(A.on&&S&&S.sql_muted);
  const pb=$('ptt'),rig=!!(S&&(S.tx||S.ptt)&&!A.tx&&!A.txWant);
  pb.classList.toggle('tx',A.tx);pb.classList.toggle('rig',rig);
  pb.textContent=A.tx?(A.latch?'TX — TAP TO STOP':'TX — RELEASE TO STOP'):A.txWant?'STARTING TX…':
    rig?'RIG IN TX — TAP TO RELEASE':(A.latch?'TAP TO TALK':'HOLD TO TALK');
  const err=A.err||(S&&S.audio_err)||'';$('aerr').hidden=!err;$('aerr').textContent=err;
  const hu=S&&S.https_url;$('ahlink').hidden=!hu;$('ahnone').hidden=!!hu;if(hu&&$('ahlink').href!==hu)$('ahlink').href=hu;
  if(S&&document.activeElement!==$('asql'))$('asql').checked=!!S.audio_sql;
  $('ainfo').textContent=(S&&A.on&&S.audio_info)||'';
}
function buildAudio(){
  const vol=$('vol'),mg=$('micg'),la=$('latch');
  vol.value=Math.round(A.vol*100);mg.value=Math.round(A.micg*100);la.checked=A.latch;
  const upd=()=>{$('volv').textContent=vol.value+'%';$('micgv').textContent=mg.value+'%';};upd();
  vol.oninput=()=>{A.vol=vol.value/100;LS.set('vol',String(A.vol));upd();};
  mg.oninput=()=>{A.micg=mg.value/100;LS.set('micg',String(A.micg));upd();};
  la.onchange=()=>{A.latch=la.checked;LS.set('latch',la.checked?'1':'0');pttUp();};
  const te=$('txeq');te.value=EQ_PRESETS[A.eq]?A.eq:'clear';
  te.onchange=()=>{A.eq=te.value;LS.set('txeq',te.value);};
  const mp=$('mproc');mp.checked=A.proc;
  mp.onchange=()=>{A.proc=mp.checked;LS.set('micproc',mp.checked?'1':'0');pttUp();micRelease();toast(mp.checked?'Voice processing on':'Voice processing off');};
  $('ahttps').hidden=window.isSecureContext;
  $('asql').onchange=()=>{send({a:'audio_sql',on:$('asql').checked});};
  $('abtn').onclick=audioToggle;
  const pb=$('ptt');
  pb.addEventListener('pointerdown',e=>{e.preventDefault();try{pb.setPointerCapture(e.pointerId);}catch(_){}pttDown();});
  for(const ev of ['pointerup','pointercancel'])pb.addEventListener(ev,()=>{if(!A.latch)pttUp();});
  pb.addEventListener('contextmenu',e=>e.preventDefault());
  document.addEventListener('visibilitychange',()=>{if(document.hidden)pttUp();});
  window.addEventListener('pagehide',pttUp);
  (function meters(){
    $('rxlv').style.width=(A.on?Math.min(100,A.rxpk*130):0)+'%';
    $('miclv').style.width=(A.mic?Math.min(100,A.micpk*130):0)+'%';
    $('miclv').style.background=A.micpk>0.7?'var(--red)':'var(--green)';
    requestAnimationFrame(meters);
  })();
  updAudioUi();
}

// ---------------- installable app (Android: Chrome turns it into a real installed app)
let instEvt=null;
const standalone=window.matchMedia('(display-mode: standalone)').matches||navigator.standalone===true||/IC9700App/.test(navigator.userAgent);
function instShow(on){$('instbtn').hidden=!on;}
instShow(!standalone);                      // always offered unless it is already running as the app
window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();instEvt=e;});
window.addEventListener('appinstalled',()=>{instShow(false);$('instov').hidden=true;toast('Installed — open it from your home screen');});
function instHelp(){
  const ua=navigator.userAgent,box=$('insttxt');box.textContent='';
  const p=(html)=>{const e=document.createElement('p');e.innerHTML=html;box.append(e);};
  if(!window.isSecureContext){
    p('The app can only be installed from the <b>secure (https)</b> page.');
    if(S&&S.https_url){const a=el('a',{className:'golink',href:S.https_url,textContent:'Open the secure page'});box.append(a);
      p('Then tap <b>INSTALL AS AN APP</b> again there.');}
    else p('On the PC: <b>Phone &rsaquo; Turn on HTTPS</b>, then open the https address it shows.');
  }else if(/iPhone|iPad|iPod/.test(ua)){
    p('Tap the <b>Share</b> button (square with an arrow), scroll down and tap <b>Add to Home Screen</b>, then <b>Add</b>.');
    p('On iPhone use <b>Safari</b> for this.');
  }else if(/SamsungBrowser/.test(ua)){
    p('Tap the <b>&#9776; menu</b> (bottom right) &rsaquo; <b>Add page to</b> &rsaquo; <b>Home screen</b>.');
  }else if(/Firefox/.test(ua)){
    p('Tap the <b>&#8942; menu</b> &rsaquo; <b>Install</b> (or <b>Add to Home screen</b>).');
  }else if(/Android/.test(ua)){
    p('Tap Chrome’s <b>&#8942; menu</b> (top right) &rsaquo; <b>Install app</b> (or <b>Add to Home screen</b> &rsaquo; <b>Install</b>).');
    p('It then appears in your app drawer like any other app.');
  }else{
    p('Click the <b>install</b> icon at the right of the address bar, or the browser menu &rsaquo; <b>Install</b>.');
  }
  $('instov').hidden=false;
}
async function instClick(){
  if(instEvt){instEvt.prompt();let ok=false;try{ok=(await instEvt.userChoice).outcome==='accepted';}catch(_){}instEvt=null;if(ok)instShow(false);return;}
  instHelp();
}
$('instbtn').onclick=instClick;
$('instok').onclick=()=>{$('instov').hidden=true;};
$('instov').onclick=e=>{if(e.target===$('instov'))$('instov').hidden=true;};
if('serviceWorker' in navigator&&window.isSecureContext){navigator.serviceWorker.register('sw.js').catch(()=>{});}

build();poll();
</script>
</body></html>
"""


LOGIN_PAGE = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1b1c1f">
<title>IC-9700</title>
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icon-512.png">
<link rel="apple-touch-icon" href="icon-512.png">
<style>
*{box-sizing:border-box}
html,body{margin:0;background:#1b1c1f;color:#eef1f5;font:16px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:360px;margin:0 auto;padding:12vh 20px 40px;text-align:center}
img{width:88px;height:88px;border-radius:20px}
h1{font-size:22px;margin:14px 0 4px}p{color:#9aa1ab;font-size:14px;margin:0 0 22px}
input,button{width:100%;min-height:52px;border-radius:10px;font:600 17px system-ui,sans-serif}
input{background:#101113;color:#eef1f5;border:1px solid #393c42;padding:0 14px;margin-bottom:12px}
button{background:#1f5fc4;color:#fff;border:0}
.err{color:#ff8a80;font-size:14px;margin:0 0 12px;min-height:1px}
</style></head><body><main>
<img src="icon-512.png" alt="">
<h1>IC9700 Monitor</h1><p>GM0OTB &middot; enter the phone access password set on the PC</p>
<form method="post" action="login">__NEXT__
<p class="err">__ERR__</p>
<input type="password" name="password" autocomplete="current-password" placeholder="Password" autofocus required>
<button type="submit">Sign in</button>
</form></main>
<script>if('serviceWorker' in navigator&&window.isSecureContext)navigator.serviceWorker.register('sw.js').catch(()=>{});</script>
</body></html>
"""

WEB_MANIFEST = json.dumps({
    "id": "/", "name": "IC9700 Monitor", "short_name": "IC-9700", "start_url": "/", "scope": "/",
    "display": "standalone", "orientation": "portrait", "background_color": "#1b1c1f", "theme_color": "#1b1c1f",
    "description": "IC-9700 remote control by GM0OTB",
    "icons": [{"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}],
}).encode("utf-8")

# Lets Chrome install the page as an app. It deliberately caches nothing: the page is always live from the PC.
WEB_SW = b"""self.addEventListener('install',e=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{});
"""

COOKIE_NAME = "ic9700_auth"


LITE_PAGE = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#1b1c1f">
<link rel="manifest" href="lite.webmanifest">
<link rel="icon" href="icon-512.png">
<title>IC-9700 Lite</title>
<style>
:root{--bg:#1b1c1f;--panel:#25272b;--lcd:#000;--text:#eef1f5;--muted:#9aa1ab;--dim:#5c616a;--blue:#2f8bff;
  --red:#ff4a3d;--green:#2fd16b;--amber:#ffa62b;--line:#393c42}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;height:100%;background:var(--bg);color:var(--text);font:15px system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  overscroll-behavior:none;user-select:none;-webkit-user-select:none}
body{display:flex;flex-direction:column;padding:env(safe-area-inset-top) 10px calc(env(safe-area-inset-bottom) + 10px)}
button{font:700 15px system-ui,sans-serif;color:var(--text);background:#33363b;border:0;border-radius:10px;
  min-height:48px;touch-action:manipulation;box-shadow:inset 0 -3px 0 rgba(0,0,0,.35)}
button:active{filter:brightness(1.25)}
button.on{background:#1f5fc4;box-shadow:inset 0 -3px 0 var(--blue)}
header{display:flex;align-items:center;gap:8px;padding:8px 0}
#pwr{min-height:36px;padding:0 12px;font-size:13px;background:#4a2020;color:#ffd7d3}
#pwr.on{background:#1e5a36;color:#fff;box-shadow:inset 0 -3px 0 var(--green)}
#dot{width:10px;height:10px;border-radius:50%;background:var(--dim);flex:none}
#dot.ok{background:var(--green)}#dot.warn{background:var(--amber)}
#stat{flex:1;font-size:12px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#gear{min-height:36px;width:44px;font-size:18px}
.lcd{background:var(--lcd);border-radius:12px;padding:10px 12px 12px;border:1px solid #111}
.tags{display:flex;gap:6px;align-items:center;font:700 12px system-ui;color:var(--muted)}
.tag{border:1px solid #444;border-radius:4px;padding:1px 6px;color:#ddd}
.tag.hl{background:var(--blue);border-color:var(--blue);color:#fff}
.tag.busy{background:var(--green);border-color:var(--green);color:#002b12}
.tag.txt{background:var(--red);border-color:var(--red);color:#fff}
#utc{margin-left:auto;font-weight:600}
#freq{font:600 min(17vw,84px)/1.05 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;text-align:center;
  letter-spacing:-1px;padding:6px 0 4px;font-variant-numeric:tabular-nums;cursor:pointer}
#freq small{font-size:.55em;letter-spacing:0}
#meter{position:relative;height:16px;background:#14161a;border-radius:3px;overflow:hidden;margin-top:4px}
#mfill{position:absolute;inset:0;clip-path:inset(0 100% 0 0);transition:clip-path .12s linear}
#mpeak{position:absolute;top:0;bottom:0;width:2px;background:#fff;opacity:.8;left:0}
#mlab{display:flex;justify-content:space-between;font:700 13px system-ui;color:#ddd;margin-top:4px}
.tune{display:grid;grid-template-columns:1fr 1.1fr 1fr;gap:8px;margin:10px 0}
.tune button{font-size:26px;min-height:54px}
#stepb{font-size:14px;color:var(--muted)}
.lv{display:grid;grid-template-columns:42px 1fr 46px;align-items:center;gap:8px;margin:6px 0}
.lv b{font-size:13px;color:var(--muted)}.lv span{text-align:right;font:600 13px system-ui;color:#ddd}
input[type=range]{width:100%;height:36px;accent-color:var(--blue);margin:0}
.keys{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:8px 0}.keys.k2{grid-template-columns:1fr 1fr;margin-top:0}
.choice{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.choice button{min-height:56px;font-size:17px}
#pttwrap{margin-top:auto;padding-top:8px}
#ptt{width:100%;min-height:96px;font-size:22px;border-radius:16px;background:#3a3d43;letter-spacing:1px;touch-action:none}
#ptt.key{background:#a86a00}#ptt.tx{background:#c62a20;box-shadow:inset 0 -5px 0 #7a130c}
#ptt.rig{background:#7a3a00}
#ainfo{text-align:center;font-size:11px;color:var(--dim);margin-top:6px;min-height:14px}
#start{position:fixed;inset:0;background:rgba(10,11,13,.92);display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:14px;z-index:20;padding:24px;text-align:center}
#start button{min-width:240px;min-height:64px;font-size:19px;background:#1f5fc4}
#start p{color:var(--muted);max-width:320px;margin:0}
.sheet{position:fixed;left:0;right:0;bottom:0;max-height:82%;background:var(--panel);border-radius:16px 16px 0 0;
  padding:14px 14px calc(env(safe-area-inset-bottom) + 14px);z-index:10;overflow:auto;box-shadow:0 -8px 30px rgba(0,0,0,.5)}
.sheet h3{margin:0 0 10px;font-size:16px;display:flex;justify-content:space-between;align-items:center}
.sheet h3 button{min-height:36px;padding:0 14px;font-size:13px}
#kpd{font:600 40px system-ui;text-align:center;background:#000;border-radius:10px;padding:10px;min-height:64px;
  font-variant-numeric:tabular-nums}
.kp{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px}.kp button{font-size:24px;min-height:58px}
.mem{display:flex;justify-content:space-between;align-items:center;padding:12px 6px;border-bottom:1px solid var(--line)}
.mem:active{background:#30333a}.mem b{font-size:16px}.mem span{color:var(--muted);font-size:13px;text-align:right}
.row{display:flex;justify-content:space-between;align-items:center;gap:10px;margin:12px 0}
select{background:#101113;color:var(--text);border:1px solid var(--line);border-radius:8px;min-height:40px;font-size:15px;padding:0 8px}
#toast{position:fixed;left:50%;bottom:140px;transform:translateX(-50%);background:#000;color:#fff;padding:10px 16px;
  border-radius:10px;font-size:14px;z-index:30;max-width:88%;text-align:center;border:1px solid #333}
a{color:#7fb6ff}
[hidden]{display:none!important}
</style></head>
<body>
<header>
  <button id="pwr">&#9211; --</button><span id="dot"></span><span id="stat">Connecting&hellip;</span>
  <button id="gear" aria-label="Settings">&#9881;</button>
</header>
<div class="lcd">
  <div class="tags"><span class="tag hl" id="tband">--</span><span class="tag" id="tmode">--</span>
    <span class="tag busy" id="tbusy" hidden>BUSY</span><span class="tag txt" id="ttx" hidden>TX</span>
    <span class="tag" id="tscan" hidden>SCAN</span><span id="utc"></span></div>
  <div id="freq">---.---<small>.--</small></div>
  <div id="meter"><div id="mfill"></div><div id="mpeak"></div></div>
  <div id="mlab"><span id="ml1">S</span><span id="ml2"></span></div>
</div>
<div class="tune"><button id="dn">&minus;</button><button id="stepb">STEP</button><button id="up">+</button></div>
<div class="lv"><b>PWR</b><input type="range" id="rfp" min="0" max="255"><span id="rfpv">--</span></div>
<div class="lv"><b>SQL</b><input type="range" id="sql" min="0" max="255"><span id="sqlv">--</span></div>
<div class="lv"><b>RF</b><input type="range" id="rf" min="0" max="255"><span id="rfv">--</span></div>
<div class="keys"><button id="bandb">BAND</button><button id="modeb">MODE</button><button id="pamp">P.AMP</button></div>
<div class="keys k2"><button id="memb">MEMORY</button><button id="scanb">SCAN</button></div>
<div id="pttwrap"><button id="ptt">HOLD TO TALK</button><div id="ainfo"></div></div>

<div id="start"><b style="font-size:20px">IC-9700 Lite</b>
  <button id="startb">TAP TO START AUDIO</button>
  <p id="startp">Starts the radio audio and the microphone, so PTT keys straight away.</p></div>

<div class="sheet" id="kpsheet" hidden><h3>Enter frequency (MHz)<button id="kpx">Cancel</button></h3>
  <div id="kpd"></div>
  <div class="kp"><button>1</button><button>2</button><button>3</button><button>4</button><button>5</button><button>6</button>
  <button>7</button><button>8</button><button>9</button><button>.</button><button>0</button><button>&#9003;</button></div>
  <button id="kpok" style="width:100%;margin-top:10px;min-height:56px" class="on">SET FREQUENCY</button></div>

<div class="sheet" id="chsheet" hidden><h3><span id="chtitle"></span><button id="chx">Close</button></h3><div class="choice" id="chlist"></div></div>

<div class="sheet" id="memsheet" hidden><h3>Memories<button id="memx">Close</button></h3><div id="memlist"></div></div>

<div class="sheet" id="setsheet" hidden><h3>Phone settings<button id="setx">Close</button></h3>
  <div class="lv"><b>Vol</b><input type="range" id="vol" min="0" max="200"><span id="volv"></span></div>
  <div class="lv"><b>Mic</b><input type="range" id="micg" min="20" max="300"><span id="micgv"></span></div>
  <div class="row"><span>PTT</span><select id="pmode"><option value="hold">Hold to talk</option><option value="tap">Tap on / tap off</option></select></div>
  <div class="row"><span>TX tone</span><select id="eq"><option value="full">Full</option><option value="clear">Clear</option><option value="crisp">Crisp</option></select></div>
  <div class="row"><span>Mic level</span><div style="flex:1;height:10px;background:#111;border-radius:5px;overflow:hidden"><div id="miclv" style="height:100%;width:0;background:var(--green)"></div></div></div>
  <p id="pinfo" style="font-size:13px"></p>
  <p id="sinfo" style="color:var(--muted);font-size:13px"></p>
  <p style="font-size:13px"><a href="./">Open the full phone page</a></p></div>
<div id="toast" hidden></div>

<script>
const CFG=__CFG__;
const $=id=>document.getElementById(id);
const LS={get(k,d){try{const v=localStorage.getItem('lite_'+k);return v===null?d:v;}catch(_){return d;}},
  set(k,v){try{localStorage.setItem('lite_'+k,v);}catch(_){}}};
let S=null,WS=null,ATOK='',MEMS=[],lastNote='';
let tT=null;function toast(t){const e=$('toast');e.textContent=t;e.hidden=false;clearTimeout(tT);tT=setTimeout(()=>{e.hidden=true;},2600);}

// ---------------- connection: one WebSocket carries audio, state and commands
async function getTok(){
  try{const r=await fetch('api/lite',{cache:'no-store'});if(r.status===401){location.reload();return false;}
    const j=await r.json();ATOK=j.atok||'';return !!ATOK;}catch(_){return false;}
}
async function connect(){
  if(WS)return;
  if(!ATOK&&!await getTok()){setTimeout(connect,2000);return;}
  const ws=new WebSocket((location.protocol==='https:'?'wss://':'ws://')+location.host+'/api/audio?lite=1&t='+encodeURIComponent(ATOK));
  ws.binaryType='arraybuffer';WS=ws;let opened=false;
  ws.onopen=()=>{opened=true;render();};
  ws.onmessage=ev=>{
    if(typeof ev.data!=='string'){rxPush(new Uint8Array(ev.data));return;}
    let m;try{m=JSON.parse(ev.data);}catch(_){return;}
    if(m.st){S=m.st;render();}
    if(m.mems){MEMS=m.mems;renderMems();}
    if(m.err)toast(m.err);
    if('ptt_ack' in m){A.acked=m.ptt_ack;if(!m.ptt_ack&&A.tx&&m.why){toast(m.why);pttUp();}renderPtt();}
    if(m.ptt_drop&&A.tx){pttUp();toast('TX stopped: no microphone audio reached the PC');}
  };
  ws.onclose=()=>{WS=null;if(A.tx){pttUp();toast('Link lost — TX stopped');}if(!opened)ATOK='';render();setTimeout(connect,1500);};
}
setInterval(()=>{if(WS&&WS.readyState===1)WS.send('{}');},4000);
function cmd(c){if(WS&&WS.readyState===1){WS.send(JSON.stringify({c}));return true;}toast('Not connected to the PC');return false;}

// ---------------- audio
const AR=16000,ULAW=new Float32Array(256);
for(let u=0;u<256;u++){const x=~u&255,e=(x>>4)&7,s=((((x&15)<<3)+0x84)<<e)-0x84;ULAW[u]=((x&128)?-s:s)/32768;}
function ulawEnc(f){
  let s=Math.round(Math.max(-1,Math.min(1,f))*32767);const sign=s<0?0x80:0;if(s<0)s=-s;s=Math.min(s,32635)+0x84;
  let e=7,mask=0x4000;while(e>0&&!(s&mask)){e--;mask>>=1;}return (~(sign|(e<<4)|((s>>(e+3))&15)))&255;
}
// Receive player with an adaptive jitter buffer (16 kHz units): starts at 120 ms, grows after a
// dropout (up to 400 ms), creeps back down after 10 s without one, drops old audio if it lags.
const CORE=`class RxCore{constructor(sr,rep){this.sr=sr;this.rep=rep;this.step=16000/sr;this.q=[];this.qpos=0;this.av=0;
 this.primed=false;this.tgt=1920;this.vol=1;this.mute=false;this.g=0;this.last=0;this.under=0;this.clean=0;this.t=0;this.pk=0;}
 avail(){return this.av-this.qpos;}
 msg(d){if(d instanceof Float32Array){this.q.push(d);this.av+=d.length;
   if(this.avail()>this.tgt+4800){while(this.q.length>1&&this.av-this.q[0].length>=this.tgt){this.av-=this.q[0].length;this.qpos=0;this.q.shift();}}}
  else{if('vol' in d)this.vol=d.vol;if('mute' in d)this.mute=d.mute;}}
 fill(out){const n=out.length;if(!this.primed&&this.avail()>=this.tgt)this.primed=true;
  const gt=this.mute?0:this.vol;let pk=0;
  for(let i=0;i<n;i++){let v;
   if(this.primed&&this.q.length){const c=this.q[0],i0=this.qpos|0,fr=this.qpos-i0,s0=c[i0],
     s1=i0+1<c.length?c[i0+1]:(this.q.length>1?this.q[1][0]:s0);v=s0+(s1-s0)*fr;this.qpos+=this.step;
     while(this.q.length&&this.qpos>=this.q[0].length){this.qpos-=this.q[0].length;this.av-=this.q[0].length;this.q.shift();}
     if(!this.q.length){this.qpos=0;this.av=0;}this.last=v;}
   else{if(this.primed){this.primed=false;this.under++;this.clean=0;this.tgt=Math.min(6400,this.tgt+480);}v=(this.last*=0.995);}
   this.g+=(gt-this.g)*0.003;const o=v*this.g;out[i]=o;const a=o<0?-o:o;if(a>pk)pk=a;}
  this.pk=Math.max(pk,this.pk*0.9);
  this.clean+=n;if(this.clean>this.sr*10&&this.tgt>1280){this.tgt-=160;this.clean=0;}
  this.t+=n;if(this.t>=this.sr/4){this.t=0;this.rep({buf:Math.round(this.avail()/16),tgt:Math.round(this.tgt/16),under:this.under,pk:this.pk});}}}`;
const WORKLET=CORE+`
class RxPlay extends AudioWorkletProcessor{constructor(){super();this.c=new RxCore(sampleRate,m=>this.port.postMessage(m));
 this.port.onmessage=e=>this.c.msg(e.data);}process(i,o){this.c.fill(o[0][0]);return true;}}
class MicCap extends AudioWorkletProcessor{constructor(){super();this.on=false;this.port.onmessage=e=>{this.on=!!e.data.on;};}
 process(inp){const c=inp[0]&&inp[0][0];if(this.on&&c){const d=c.slice(0);this.port.postMessage(d,[d.buffer]);}return true;}}
registerProcessor('rx-play',RxPlay);registerProcessor('mic-cap',MicCap);`;
const A={ctx:null,ready:false,rxSend:null,mic:null,micNode:null,tx:false,acked:null,txAt:0,
  vol:+LS.get('vol','1'),micg:+LS.get('micg','1'),tap:LS.get('pmode','hold')==='tap',eq:LS.get('eq','clear'),
  stats:{buf:0,tgt:0,under:0,pk:0},micpk:0,wl:null};

function rxPush(u8){
  if(!A.ready)return;
  const f=new Float32Array(u8.length);for(let i=0;i<u8.length;i++)f[i]=ULAW[u8[i]];A.rxSend(f);
}
function rxMsg(m){if(A.ready)A.rxSend(m);}

async function startAudio(){
  if(A.ready||A.starting)return;A.starting=true;$('startb').textContent='STARTING…';
  try{
    const C=window.AudioContext||window.webkitAudioContext;A.ctx=new C({latencyHint:'interactive'});
    await A.ctx.resume();
    if(A.ctx.audioWorklet){
      const url=URL.createObjectURL(new Blob([WORKLET],{type:'application/javascript'}));
      await A.ctx.audioWorklet.addModule(url);
      const rx=new AudioWorkletNode(A.ctx,'rx-play',{numberOfInputs:0,outputChannelCount:[1]});
      rx.port.onmessage=e=>{A.stats=e.data;};rx.connect(A.ctx.destination);
      A.rxSend=d=>{if(d instanceof Float32Array)rx.port.postMessage(d,[d.buffer]);else rx.port.postMessage(d);};
    }else{                                  // plain http on an older browser: receive only
      const RxCore=new Function(CORE+';return RxCore;')(),core=new RxCore(A.ctx.sampleRate,m=>{A.stats=m;});
      const sp=A.ctx.createScriptProcessor(2048,1,1);sp.onaudioprocess=e=>core.fill(e.outputBuffer.getChannelData(0));
      sp.connect(A.ctx.destination);A.sp=sp;A.rxSend=d=>core.msg(d);
    }
    A.ready=true;A.procOn=[];A.procTxt='';rxMsg({vol:A.vol});
    if(A.ctx.audioWorklet&&window.isSecureContext&&navigator.mediaDevices&&navigator.mediaDevices.getUserMedia){
      try{
        A.mic=await navigator.mediaDevices.getUserMedia({audio:Object.assign({channelCount:1},NOPROC,GOOG_OFF)});
        await procOff();
        const src=A.ctx.createMediaStreamSource(A.mic),mn=new AudioWorkletNode(A.ctx,'mic-cap',{numberOfOutputs:1,outputChannelCount:[1]});
        const z=A.ctx.createGain();z.gain.value=0;src.connect(mn);mn.connect(z);z.connect(A.ctx.destination);
        mn.port.onmessage=e=>onMic(e.data);A.micNode=mn;
      }catch(e){toast('Microphone not allowed ('+e.name+') — receive only');}
    }else toast('Open the https:// address to talk — receive only');
    $('start').hidden=true;wake();
  }catch(e){toast('Audio could not start: '+(e.message||e.name));$('startb').textContent='TAP TO START AUDIO';}
  A.starting=false;renderPtt();
}
// The phone's own voice processing (echo cancelling, noise suppression, auto gain, voice isolation)
// is made for phone calls and makes a radio mic sound pumped and muffled: always switched off here.
const NOPROC={echoCancellation:false,noiseSuppression:false,autoGainControl:false,voiceIsolation:false};
const GOOG_OFF={googEchoCancellation:false,googNoiseSuppression:false,googAutoGainControl:false,googHighpassFilter:false,
  googTypingNoiseDetection:false,googAudioMirroring:false,googExperimentalNoiseSuppression:false,googExperimentalAutoGainControl:false};
async function procOff(){
  const tr=A.mic&&A.mic.getAudioTracks()[0];if(!tr)return;
  const sup=(navigator.mediaDevices.getSupportedConstraints&&navigator.mediaDevices.getSupportedConstraints())||{};
  const want={};for(const k in NOPROC)if(sup[k])want[k]=false;
  try{await tr.applyConstraints(want);}catch(_){}                       // second go, on the live microphone
  const st=tr.getSettings?tr.getSettings():{};
  const names={echoCancellation:'echo cancelling',noiseSuppression:'noise suppression',autoGainControl:'auto gain',voiceIsolation:'voice isolation'};
  A.procOn=Object.keys(names).filter(k=>st[k]===true).map(k=>names[k]);
  A.procTxt=A.procOn.length?'Phone voice processing still ON: '+A.procOn.join(', ')+' (this phone/browser would not switch it off)'
    :'Phone voice processing: OFF (echo cancelling, noise suppression, auto gain'+(sup.voiceIsolation?', voice isolation':'')+')';
  if(A.procOn.length)toast(A.procTxt);
}
async function wake(){try{if(navigator.wakeLock&&!document.hidden)A.wl=await navigator.wakeLock.request('screen');}catch(_){}}
document.addEventListener('visibilitychange',()=>{if(document.hidden){pttUp();}else{wake();if(A.ctx)A.ctx.resume();}});
window.addEventListener('pagehide',()=>pttUp());

// microphone: 7 kHz low-pass, resample to 16 kHz, TX tone, mu-law, 20 ms packets
let micFir=null,micHist=null,micPos=0,txEq=null;const txOut=new Uint8Array(2048);let txN=0;
function makeFir(rate){
  const N=rate>32000?63:41,M=N-1,fc=7000/rate,h=new Float32Array(N);let sum=0;
  for(let i=0;i<N;i++){const n=i-M/2,sn=n===0?2*fc:Math.sin(2*Math.PI*fc*n)/(Math.PI*n);
    const w=0.42-0.5*Math.cos(2*Math.PI*i/M)+0.08*Math.cos(4*Math.PI*i/M);h[i]=sn*w;sum+=h[i];}
  for(let i=0;i<N;i++)h[i]/=sum;h.rate=rate;return h;
}
const EQ_PRESETS={full:[[80,0.707]],clear:[[220,0.707],[2400,4,1.0]],crisp:[[300,0.707],[180,0.6],[2600,6,0.9]]};
function bq(b0,b1,b2,a0,a1,a2){return {b0:b0/a0,b1:b1/a0,b2:b2/a0,a1:a1/a0,a2:a2/a0,x1:0,x2:0,y1:0,y2:0};}
function bqHp(fc,q){const w=2*Math.PI*fc/AR,c=Math.cos(w),al=Math.sin(w)/(2*q);return bq((1+c)/2,-(1+c),(1+c)/2,1+al,-2*c,1-al);}
function bqPeak(fc,db,q){const g=Math.pow(10,db/40),w=2*Math.PI*fc/AR,c=Math.cos(w),al=Math.sin(w)/(2*q);
  return bq(1+al*g,-2*c,1-al*g,1+al/g,-2*c,1-al/g);}
function makeEq(name){return (EQ_PRESETS[name]||EQ_PRESETS.clear).map(p=>p.length===2?bqHp(p[0],p[1]):bqPeak(p[0],p[1],p[2]));}
function runEq(st,v){for(const f of st){const y=f.b0*v+f.b1*f.x1+f.b2*f.x2-f.a1*f.y1-f.a2*f.y2;f.x2=f.x1;f.x1=v;f.y2=f.y1;f.y1=y;v=y;}return v;}
function onMic(inp){
  const sr=A.ctx.sampleRate,step=sr/AR,len=inp.length;
  if(!micFir||micFir.rate!==sr){micFir=makeFir(sr);micHist=new Float32Array(micFir.length);micPos=0;}
  if(!txEq)txEq=makeEq(A.eq);
  const h=micFir,N=h.length,x=new Float32Array(N+len);x.set(micHist);x.set(inp,N);micHist=x.slice(len);
  const y=new Float32Array(len+1);
  for(let t=0;t<=len;t++){let a=0;const b=N-1+t;for(let k=0;k<N;k++)a+=h[k]*x[b-k];y[t]=a;}
  let p=micPos,pk=0;
  while(p<len){const i=p|0,f=p-i,v=runEq(txEq,y[i]+(y[i+1]-y[i])*f)*A.micg;txOut[txN++]=ulawEnc(v);const av=v<0?-v:v;if(av>pk)pk=av;p+=step;}
  micPos=p-len;A.micpk=Math.max(pk,A.micpk*0.8);
  if(txN>=320){if(A.tx&&WS&&WS.readyState===1)WS.send(txOut.slice(0,txN));txN=0;}
}

// ---------------- PTT: keys first, audio follows; the PC keys the radio straight away
function pttDown(){
  if(!A.ready){startAudio();return;}
  if(S&&S.tx&&!A.tx){cmd({a:'unkey'});toast('Releasing PTT');return;}
  if(A.tap&&A.tx){pttUp();return;}
  if(!A.micNode){toast(window.isSecureContext?'Microphone not available':'Open the https:// address to talk');return;}
  if(!WS||WS.readyState!==1){toast('Not connected to the PC');return;}
  if(S&&!S.rig_on){toast('The radio is off');return;}
  A.tx=true;A.acked=null;A.txAt=performance.now();txN=0;micPos=0;txEq=null;
  WS.send('{"ptt":true}');A.micNode.port.postMessage({on:true});rxMsg({mute:true});
  if(navigator.vibrate)navigator.vibrate(25);
  renderPtt();
}
function pttUp(){
  if(!A.tx)return;
  A.tx=false;if(A.micNode)A.micNode.port.postMessage({on:false});
  if(WS&&WS.readyState===1){if(txN)WS.send(txOut.slice(0,txN));WS.send('{"ptt":false}');}
  txN=0;rxMsg({mute:false});renderPtt();
}
function renderPtt(){
  const b=$('ptt'),rig=!!(S&&S.tx&&!A.tx);
  b.className=A.tx?(A.acked===null&&!(S&&S.tx)?'key':'tx'):(rig?'rig':'');
  b.textContent=!A.ready?'TAP TO START AUDIO':A.tx?(A.acked===null&&!(S&&S.tx)?'KEYING…':(A.tap?'TX — TAP TO STOP':'TX — RELEASE TO STOP')):
    rig?'RADIO IN TX — TAP TO RELEASE':(A.tap?'TAP TO TALK':'HOLD TO TALK');
}

// ---------------- display
function fmtHz(hz){
  if(hz==null)return '---.---<small>.--</small>';
  const s=String(Math.round(hz)).padStart(10,'0');
  return parseInt(s.slice(0,4),10)+'.'+s.slice(4,7)+'<small>.'+s.slice(7,9)+'</small>';
}
let localHz=null,localAt=0;
function pctOf(v){return v==null?'--':Math.round(v/255*100)+'%';}
const touched={};
function setLv(id,v){if(v==null)return;if(performance.now()-(touched[id]||0)<1500)return;$(id).value=v;$(id+'v').textContent=pctOf(v);}
function render(){
  const online=!!(WS&&WS.readyState===1&&S&&S.online);
  $('dot').className=online?(S.link&&S.rig_on?'ok':'warn'):'';
  $('stat').textContent=!WS||WS.readyState!==1?'Connecting to the PC…':!S?'Waiting…':!S.online?'PC not connected to the radio':
    S.rig_off?'Radio is off':(S.status||'');
  if(!S){renderPtt();return;}
  const p=$('pwr');p.className=S.rig_on?'on':'';p.innerHTML=S.rig_on?'&#9211; ON':'&#9211; OFF';
  const hz=(localHz!=null&&performance.now()-localAt<900)?localHz:S.hz;
  $('freq').innerHTML=fmtHz(hz);
  $('tband').textContent=(S.band||'--').toUpperCase();$('tmode').textContent=S.mode||'--';
  $('tbusy').hidden=!S.busy;$('ttx').hidden=!S.tx;$('tscan').hidden=!S.scan;$('utc').textContent=S.utc||'';
  const tx=S.meter==='tx',frac=tx?S.pwr:S.mfrac,s9=CFG.s9;
  const mf=$('mfill');mf.style.clipPath='inset(0 '+(100-Math.max(0,Math.min(1,frac||0))*100)+'% 0 0)';
  mf.style.background='linear-gradient(90deg,var(--blue) '+(s9*100)+'%,var(--red) '+(s9*100)+'%)';
  $('mpeak').style.left=(tx?0:Math.min(99.5,(S.peak||0)*100))+'%';$('mpeak').hidden=tx;
  $('ml1').textContent=tx?(S.info||'Po'):(S.mtext||'S');$('ml2').textContent=tx?(S.mtext||''):(S.sql_muted?'SQL closed':'');
  setLv('rfp',S.rfp);setLv('sql',S.sql);setLv('rf',S.rf);
  $('bandb').textContent=S.band?S.band.toUpperCase():'BAND';$('modeb').textContent=S.mode||'MODE';
  $('pamp').classList.toggle('on',!!S.pamp);$('scanb').classList.toggle('on',!!S.scan);
  $('scanb').textContent=S.scan?'STOP SCAN':'SCAN';
  if(!A.step)A.step=+LS.get('step',String(S.step||0))||S.step;
  $('stepb').textContent='STEP '+stepName(A.step);
  if(S.note&&S.note!==lastNote)toast(S.note);lastNote=S.note||'';
  if(A.tx&&!S.tx&&A.acked===false){pttUp();}
  if(A.tx&&!S.tx&&S.ptt===false&&performance.now()-A.txAt>3000){pttUp();toast('TX ended by the PC (time-out?)');}
  renderPtt();
}
function stepName(v){const s=CFG.steps.find(x=>x[1]===v);return s?s[0]:(v>=1000?(v/1000)+' kHz':v+' Hz');}
setInterval(()=>{
  const st=A.stats;
  $('ainfo').textContent=A.ready?('buffer '+st.buf+' ms · target '+st.tgt+' ms'+(st.under?' · dropouts '+st.under:'')):'';
  $('pinfo').textContent=A.procTxt||'';$('pinfo').style.color=A.procOn&&A.procOn.length?'var(--amber)':'var(--green)';
  $('sinfo').textContent=A.ready?('Audio: '+A.ctx.sampleRate+' Hz, '+(A.ctx.audioWorklet?'worklet':'basic')+' player. '+$('ainfo').textContent):'';
  $('miclv').style.width=Math.min(100,A.micpk*130)+'%';$('miclv').style.background=A.micpk>0.7?'var(--red)':'var(--green)';
  A.micpk*=0.85;
},250);

// ---------------- controls
function hold(btn,fn){let t1=null,t2=null;const stop=()=>{clearTimeout(t1);clearInterval(t2);t1=t2=null;};
  btn.addEventListener('pointerdown',e=>{e.preventDefault();stop();fn();t1=setTimeout(()=>{t2=setInterval(fn,130);},420);});
  for(const ev of ['pointerup','pointercancel','pointerleave'])btn.addEventListener(ev,stop);}
function tuneStep(dir){
  if(!S||S.hz==null)return;const st=A.step||S.step||1000;
  const base=(localHz!=null&&performance.now()-localAt<900)?localHz:S.hz;
  localHz=Math.round(base/st)*st+dir*st;localAt=performance.now();$('freq').innerHTML=fmtHz(localHz);
  cmd({a:'step',dir,step:st});
}
hold($('up'),()=>tuneStep(1));hold($('dn'),()=>tuneStep(-1));
$('stepb').onclick=()=>{const vals=CFG.steps.map(x=>x[1]);let i=vals.indexOf(A.step);A.step=vals[(i+1)%vals.length];
  LS.set('step',String(A.step));$('stepb').textContent='STEP '+stepName(A.step);};
for(const [id,sub] of [['rfp',10],['sql',3],['rf',2]]){
  const r=$(id);let last=0,tm=null;
  const go=()=>{last=performance.now();cmd({a:'level',sub,v:+r.value});};
  r.addEventListener('input',()=>{touched[id]=performance.now();$(id+'v').textContent=pctOf(+r.value);
    clearTimeout(tm);if(performance.now()-last>120)go();else tm=setTimeout(go,120);});
  r.addEventListener('change',()=>{touched[id]=performance.now();clearTimeout(tm);go();});
}
$('pamp').onclick=()=>cmd({a:'toggle',key:'pamp'});
// band / mode: a sheet of big buttons, the current one lit
function choose(title,items,cur,fn){
  $('chtitle').textContent=title;const box=$('chlist');box.textContent='';
  for(const it of items){const b=document.createElement('button');b.textContent=it.toUpperCase();
    if(cur&&it.toLowerCase()===String(cur).toLowerCase())b.className='on';
    b.onclick=()=>{fn(it);$('chsheet').hidden=true;};box.append(b);}
  $('chsheet').hidden=false;
}
const bandPick=()=>choose('Band',CFG.bands,S&&S.band,b=>cmd({a:'band',band:b}));
const modePick=()=>choose('Mode',CFG.modes,S&&S.mode,m=>cmd({a:'mode',mode:m}));
$('bandb').onclick=bandPick;$('modeb').onclick=modePick;$('tband').onclick=bandPick;$('tmode').onclick=modePick;
$('chx').onclick=()=>{$('chsheet').hidden=true;};
$('scanb').onclick=()=>{if(S)cmd({a:'scan',on:!S.scan});};
$('pwr').onclick=()=>{if(!S||!S.online){toast('The PC is not connected to the radio');return;}
  if(S.rig_on){if(confirm('Switch the IC-9700 OFF?'))cmd({a:'power',on:false});}else{cmd({a:'power',on:true});toast('Switching on… (a few seconds)');}};
// memories
function renderMems(){
  const box=$('memlist');box.textContent='';
  if(!MEMS.length){const p=document.createElement('p');p.style.color='var(--muted)';
    p.textContent='No memories yet. Save some on the PC (MEMORY tab, or "Read from radio" there).';box.append(p);return;}
  for(const m of MEMS){const d=document.createElement('div');d.className='mem';
    const b=document.createElement('b');b.textContent=m.name||m.mhz;const s=document.createElement('span');
    s.textContent=m.mhz+' '+(m.mode||'')+(m.info?' · '+m.info:'');d.append(b,s);
    d.onclick=()=>{cmd({a:'mem',i:m.i});$('memsheet').hidden=true;toast(m.name||m.mhz);};box.append(d);}
}
$('memb').onclick=()=>{renderMems();$('memsheet').hidden=false;};$('memx').onclick=()=>{$('memsheet').hidden=true;};
// frequency keypad
let kp='';
function kpShow(){$('kpd').textContent=kp||' ';}
$('freq').onclick=()=>{kp='';kpShow();$('kpsheet').hidden=false;};
$('kpx').onclick=()=>{$('kpsheet').hidden=true;};
for(const b of document.querySelectorAll('.kp button'))b.onclick=()=>{
  const k=b.textContent;if(k==='⌫')kp=kp.slice(0,-1);else if(k==='.'){if(!kp.includes('.'))kp+=(kp?'.':'0.');}
  else if(kp.replace('.','').length<10)kp+=k;kpShow();};
function kpHz(s){
  if(!s)return null;let mhz;
  if(s.includes('.'))mhz=parseFloat(s);
  else if(s.length<=3)mhz=+s;
  else if(/^1[23]/.test(s))mhz=parseFloat(s.slice(0,4)+'.'+s.slice(4));
  else mhz=parseFloat(s.slice(0,3)+'.'+s.slice(3));
  return isFinite(mhz)&&mhz>0?Math.round(mhz*1e6):null;
}
$('kpok').onclick=()=>{const hz=kpHz(kp);if(!hz){toast('Type a frequency in MHz, e.g. 145.500');return;}
  if(cmd({a:'tune',hz})){localHz=hz;localAt=performance.now();$('freq').innerHTML=fmtHz(hz);}$('kpsheet').hidden=true;};
// settings
const vol=$('vol'),mg=$('micg');vol.value=Math.round(A.vol*100);mg.value=Math.round(A.micg*100);
const updS=()=>{$('volv').textContent=vol.value+'%';$('micgv').textContent=mg.value+'%';};updS();
vol.oninput=()=>{A.vol=vol.value/100;LS.set('vol',String(A.vol));rxMsg({vol:A.vol});updS();};
mg.oninput=()=>{A.micg=mg.value/100;LS.set('micg',String(A.micg));updS();};
$('pmode').value=A.tap?'tap':'hold';$('pmode').onchange=()=>{A.tap=$('pmode').value==='tap';LS.set('pmode',$('pmode').value);pttUp();renderPtt();};
$('eq').value=EQ_PRESETS[A.eq]?A.eq:'clear';$('eq').onchange=()=>{A.eq=$('eq').value;LS.set('eq',A.eq);txEq=null;};
$('gear').onclick=()=>{$('setsheet').hidden=false;};$('setx').onclick=()=>{$('setsheet').hidden=true;};
// PTT button
const pb=$('ptt');
pb.addEventListener('pointerdown',e=>{e.preventDefault();try{pb.setPointerCapture(e.pointerId);}catch(_){}pttDown();});
for(const ev of ['pointerup','pointercancel'])pb.addEventListener(ev,()=>{if(!A.tap)pttUp();});
pb.addEventListener('contextmenu',e=>e.preventDefault());
$('startb').onclick=startAudio;
if('serviceWorker' in navigator&&window.isSecureContext){navigator.serviceWorker.register('sw.js').catch(()=>{});}
connect();renderPtt();
</script>
</body></html>
"""

WEB_MANIFEST_LITE = json.dumps({
    "id": "/lite", "name": "IC-9700 Lite", "short_name": "IC-9700 Lite", "start_url": "/lite", "scope": "/",
    "display": "standalone", "orientation": "portrait", "background_color": "#1b1c1f", "theme_color": "#1b1c1f",
    "description": "IC-9700 remote: clear audio and quick PTT (GM0OTB)",
    "icons": [{"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}],
}).encode("utf-8")


def lite_page_bytes():
    cfg = {"version": APP_VERSION, "steps": [[n, v] for n, v in STEPS], "s9": S9_RAW / METER_MAX,
           "bands": [b[0] for b in BANDS], "modes": MODE_LIST}
    return LITE_PAGE.replace("__CFG__", json.dumps(cfg)).encode("utf-8")


def _png_plain(size=512):
    """A simple app icon (used only if ic9700.png is missing)."""
    rows = []
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            bar = size * 0.2 < x < size * 0.8 and size * 0.62 < y < size * 0.7 and x < size * (0.2 + 0.45)
            row += bytes((0x2d, 0x63, 0xc8)) if bar else bytes((0x1b, 0x1c, 0x1f))
        rows.append(bytes(row))
    raw = zlib.compress(b"".join(rows), 9)

    def chunk(t, d):
        return len(d).to_bytes(4, "big") + t + d + (zlib.crc32(t + d) & 0xFFFFFFFF).to_bytes(4, "big")
    ihdr = size.to_bytes(4, "big") * 2 + bytes((8, 2, 0, 0, 0))
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", raw) + chunk(b"IEND", b"")


def app_icon_png():
    for d in (getattr(sys, "_MEIPASS", None), BASE_DIR, os.path.dirname(os.path.abspath(__file__))):
        if d:
            try:
                with open(os.path.join(d, "ic9700.png"), "rb") as f:
                    return f.read()
            except OSError:
                pass
    return _png_plain()


def web_page_bytes():
    """The phone page with this program's own mode / step / level / tone lists filled in."""
    cfg = {"version": APP_VERSION, "modes": MODE_LIST, "bands": [b[0] for b in BANDS],
           "steps": [[n, v] for n, v in STEPS], "ctcss": CTCSS,
           "levels": [[n, s, f] for n, s, f in LEVELS],
           "toggles": {k: v[0] for k, v in TOGGLES.items()},
           "s_ticks": [[label, raw / METER_MAX] for label, raw in S_TICKS],
           "pwr_ticks": [[label, raw / METER_MAX] for label, raw in PWR_TICKS],
           "s9": S9_RAW / METER_MAX}
    return WEB_PAGE.replace("__CFG__", json.dumps(cfg)).encode("utf-8")


class _WebServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = sys.platform != "win32"     # on Windows this would let two copies share the port

    def handle_error(self, request, client_address):
        pass                                            # pythonw has no console to print to


class _WebHandler(BaseHTTPRequestHandler):
    server_version = "IC9700Monitor"
    protocol_version = "HTTP/1.1"
    timeout = 60

    def log_message(self, *args):
        pass                                            # pythonw has no console to print to

    def _send(self, code, body=b"", ctype="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "same-origin")
        self.end_headers()
        if body and self.command != "HEAD":
            self.wfile.write(body)

    def _authed(self):
        """Signed in with the cookie from the sign-in page (or HTTP Basic, for older bookmarks)."""
        bridge = self.server.bridge
        for part in self.headers.get("Cookie", "").split(";"):
            k, _, v = part.strip().partition("=")
            if k == COOKIE_NAME and bridge.cookie_token and hmac.compare_digest(v.encode(), bridge.cookie_token.encode()):
                return True
        h = self.headers.get("Authorization", "")
        if h.startswith("Basic ") and bridge.password:
            try:
                pw = base64.b64decode(h[6:].strip()).decode("utf-8", "replace").split(":", 1)[1]
            except Exception:
                pw = ""
            if hmac.compare_digest(pw.encode("utf-8"), bridge.password.encode("utf-8")):
                return True
        return False

    def _login_page(self, err="", nxt=""):
        body = LOGIN_PAGE.replace("__ERR__", err).replace(
            "__NEXT__", '<input type="hidden" name="next" value="lite">' if nxt == "lite" else "").encode("utf-8")
        self._send(200, body, "text/html; charset=utf-8")

    def _do_login(self):
        bridge = self.server.bridge
        try:
            n = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            n = -1
        if not 0 < n <= 4096:
            self._login_page("Please enter the password.")
            return
        form = urllib.parse.parse_qs(self.rfile.read(n).decode("utf-8", "replace"))
        pw = (form.get("password") or [""])[0]
        nxt = "lite" if (form.get("next") or [""])[0] == "lite" else ""
        if not (bridge.password
                and hmac.compare_digest(pw.encode("utf-8"), bridge.password.encode("utf-8"))):
            time.sleep(1.0)                             # slow down password guessing
            self._login_page("Wrong password - try again.", nxt)
            return
        secure = "; Secure" if isinstance(self.connection, ssl.SSLSocket) else ""
        self.send_response(303)
        self.send_header("Location", "lite" if nxt else "./")
        self.send_header("Set-Cookie", f"{COOKIE_NAME}={bridge.cookie_token}; Path=/; Max-Age=31536000; "
                                       f"HttpOnly; SameSite=Lax{secure}")
        self.send_header("Content-Length", "0")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()

    def _origin_ok(self):
        origin = self.headers.get("Origin")
        if not origin:
            return True
        ohost = origin.split("://", 1)[-1].strip("/").lower()
        hosts = {h.strip().lower() for h in (self.headers.get("Host", ""), self.headers.get("X-Forwarded-Host", "")) if h}
        if ohost in hosts:
            return True
        # Behind "tailscale serve" the page is https://<pc>.<tailnet>.ts.net and requests arrive via loopback
        return (origin.startswith("https://") and ohost.split(":")[0].endswith(".ts.net")
                and self.client_address[0] in ("127.0.0.1", "::1"))

    def _audio_upgrade(self):
        """WebSocket for phone audio. Authorised by a token from /api/state (that one needs the password)."""
        bridge = self.server.bridge
        q = urllib.parse.parse_qs(self.path.split("?", 1)[1] if "?" in self.path else "")
        tok = (q.get("t") or [""])[0]
        if not (bridge.audio_token and hmac.compare_digest(tok.encode(), bridge.audio_token.encode())):
            time.sleep(1.0)
            self._send(403, b'{"error":"forbidden"}')
            return
        key = self.headers.get("Sec-WebSocket-Key", "")
        if not self._origin_ok() or "websocket" not in self.headers.get("Upgrade", "").lower() or not key:
            self._send(400, b'{"error":"bad request"}')
            return
        accept = base64.b64encode(hashlib.sha1((key + WS_GUID).encode()).digest()).decode()
        self.send_response(101, "Switching Protocols")
        self.send_header("Upgrade", "websocket")
        self.send_header("Connection", "Upgrade")
        self.send_header("Sec-WebSocket-Accept", accept)
        self.end_headers()
        self.wfile.flush()
        self.close_connection = True
        sock = self.connection
        sock.settimeout(None)
        try:
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except OSError:
            pass
        bridge.audio_session(WsConn(sock), lite=(q.get("lite") or [""])[0] == "1")

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/api/audio":
            self._audio_upgrade()
            return
        bridge = self.server.bridge
        # files the browser needs to install the page as an app (nothing private in them)
        if path == "/manifest.webmanifest":
            self._send(200, WEB_MANIFEST, "application/manifest+json")
            return
        if path in ("/icon-512.png", "/favicon.ico"):
            self._send(200, bridge.icon, "image/png")
            return
        if path == "/sw.js":
            self._send(200, WEB_SW, "text/javascript")
            return
        if path == "/lite.webmanifest":
            self._send(200, WEB_MANIFEST_LITE, "application/manifest+json")
            return
        if not self._authed():
            if path in ("/", "/index.html"):
                self._login_page()
            elif path in ("/lite", "/lite/"):
                self._login_page(nxt="lite")
            else:
                self._send(401, b'{"error":"sign in"}')
            return
        if path in ("/", "/index.html"):
            self._send(200, bridge.page, "text/html; charset=utf-8")
        elif path in ("/lite", "/lite/"):
            self._send(200, bridge.lite_page, "text/html; charset=utf-8")
        elif path == "/api/lite":
            body = json.dumps({"atok": bridge.audio_token, "https_url": bridge.https_url}).encode("utf-8")
            self._send(200, body)
        elif path == "/api/state":
            with bridge.lock:
                body = bridge.state_json
            self._send(200, body)
        elif path == "/api/memories":
            with bridge.lock:
                body = bridge.mem_json
            self._send(200, body)
        else:
            self._send(404, b'{"error":"not found"}')

    do_HEAD = do_GET

    def do_POST(self):
        if self.path.split("?", 1)[0] == "/login":
            self._do_login()
            return
        if not self._authed():
            self._send(401, b'{"error":"sign in"}')
            return
        if self.path.split("?", 1)[0] != "/api/cmd":
            self._send(404, b'{"error":"not found"}')
            return
        # Only our own page may send commands: other web sites can't add this header without permission
        if self.headers.get("X-IC9700") != "1" or not self._origin_ok():
            self._send(403, b'{"error":"forbidden"}')
            return
        try:
            n = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            n = -1
        if not 0 < n <= 4096:
            self._send(413, b'{"error":"bad length"}')
            return
        try:
            cmd = json.loads(self.rfile.read(n).decode("utf-8"))
        except Exception:
            cmd = None
        if not isinstance(cmd, dict) or not isinstance(cmd.get("a"), str):
            self._send(400, b'{"error":"bad command"}')
            return
        self.server.bridge.app.ui(self.server.bridge.app.web_command, cmd)   # runs on the Tk thread
        self._send(200, b'{"ok":true}')


class WebBridge:
    """Runs the phone page's web server on its own threads. It never touches Tk: it serves a snapshot
    the Tk thread publishes, and hands commands to the Tk thread through app.ui()."""

    def __init__(self, app):
        self.app = app
        self.lock = threading.Lock()
        self.state_json = b'{"online":false,"toggles":{},"levels":{}}'
        self.mem_json = b"[]"
        self.mem_rev = 0
        self.lite_json = b"{}"
        self.lite_sessions = 0
        self.page = b""
        self.lite_page = b""
        self.httpd = None
        self.thread = None
        self.port = None
        self.password = ""
        self.error = ""
        self.audio_token = ""
        self.cookie_token = ""
        self.icon = b""
        self.sessions = set()
        self.httpsd = None
        self.https_port = None
        self.https_url = ""
        self.https_error = ""

    @property
    def running(self):
        return self.httpd is not None

    def start_https(self, port, certfile, keyfile, name):
        """The same page on https, with the PC's own Tailscale certificate (phones need https for the mic)."""
        self.stop_https()
        if self.httpd is None:
            return False
        try:
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ctx.minimum_version = ssl.TLSVersion.TLSv1_2
            ctx.load_cert_chain(certfile, keyfile)
            httpsd = _WebServer(("0.0.0.0", port), _WebHandler)
            # handshake on the connection's own thread, so one slow phone can't hold up the others
            httpsd.socket = ctx.wrap_socket(httpsd.socket, server_side=True, do_handshake_on_connect=False)
        except (OSError, ssl.SSLError, ValueError) as e:
            self.https_error = str(e)
            return False
        httpsd.bridge = self
        self.httpsd, self.https_port, self.https_error = httpsd, port, ""
        self.https_url = f"https://{name}:{port}/"
        threading.Thread(target=httpsd.serve_forever, kwargs={"poll_interval": 0.5}, daemon=True).start()
        return True

    def stop_https(self):
        httpsd, self.httpsd, self.https_port, self.https_url = self.httpsd, None, None, ""
        if httpsd is not None:
            try:
                httpsd.shutdown()
                httpsd.server_close()
            except Exception:
                pass

    def start(self, port, password, secret=""):
        self.stop()
        self.password = password
        # sign-in cookie: changes when the password changes, so a new password signs every phone out
        self.cookie_token = hmac.new((secret or "ic9700").encode(), password.encode("utf-8"), hashlib.sha256).hexdigest()
        try:
            self.icon = app_icon_png()
            self.page = web_page_bytes()
            self.lite_page = lite_page_bytes()
            httpd = _WebServer(("0.0.0.0", port), _WebHandler)
        except OSError as e:
            self.error = str(e)
            return False
        httpd.bridge = self
        self.audio_token = secrets.token_urlsafe(18)
        self.httpd, self.port, self.error = httpd, port, ""
        self.thread = threading.Thread(target=httpd.serve_forever, kwargs={"poll_interval": 0.5}, daemon=True)
        self.thread.start()
        return True

    def stop(self):
        self.stop_https()
        httpd, self.httpd, self.port = self.httpd, None, None
        self.audio_token = ""
        with self.lock:
            sessions = list(self.sessions)
        for sess in sessions:
            sess.close()
        if httpd is not None:
            try:
                httpd.shutdown()
                httpd.server_close()
            except Exception:
                pass

    def audio_session(self, ws, lite=False):
        """Runs on the connection's own thread until the phone disconnects. The lite page also gets
        its display state and sends its commands over this one connection (no extra requests)."""
        app, eng = self.app, self.app.audio
        sess = AudioSession(ws)

        def notify(obj):
            try:
                ws.send_json(obj)
            except OSError:
                sess.close()
        pw = PttWorker(app, notify)
        with self.lock:
            self.sessions.add(sess)
            if lite:
                self.lite_sessions += 1
        if lite:
            threading.Thread(target=self._lite_pusher, args=(ws, sess), daemon=True).start()
        ptt = False
        now = time.time()
        last_rx = last_audio = now
        err_sent = ""
        try:
            if eng is None:
                ws.send_json({"err": "Audio isn't set up on the PC: run  py -m pip install sounddevice  there "
                                     "and restart IC9700 Monitor."})
            else:
                err = eng.add_listener(sess)
                if err:
                    ws.send_json({"err": err})
            while not sess.closed:
                try:
                    op, data = ws.recv()
                except socket.timeout:
                    op, data = None, b""
                now = time.time()
                if op == 0x8:
                    break
                if op is not None:
                    last_rx = now
                if op == 0x9:
                    ws.send(0xA, data)
                elif op == 0x2 and ptt and eng is not None:
                    last_audio = now
                    err = eng.feed(sess, data)
                    if err and err != err_sent:
                        err_sent = err
                        ws.send_json({"err": err})
                elif op == 0x1:
                    try:
                        msg = json.loads(data.decode("utf-8"))
                    except Exception:
                        msg = None
                    if not isinstance(msg, dict):
                        pass
                    elif "ptt" in msg and eng is not None:
                        if bool(msg["ptt"]) != ptt:
                            ptt, last_audio = bool(msg["ptt"]), now
                            pw.set(ptt)
                    elif isinstance(msg.get("c"), dict) and isinstance(msg["c"].get("a"), str):
                        app.ui(app.web_command, msg["c"])     # same commands as the full page
                if ptt and now - last_audio > 1.5:      # microphone audio stopped: never leave the rig keyed
                    ptt = False
                    pw.set(False)
                    ws.send_json({"ptt_drop": True})
                if now - last_rx > 12:                  # phone vanished without closing
                    break
        except (ConnectionError, OSError, ValueError):
            pass
        finally:
            pw.close()
            if eng is not None:
                eng.remove_listener(sess)
            sess.close()
            with self.lock:
                self.sessions.discard(sess)
                if lite:
                    self.lite_sessions -= 1

    def _lite_pusher(self, ws, sess):
        """Sends the lite page its small state snapshot (and the memory list when it changes)."""
        last, last_rev = None, None
        while not sess.closed:
            with self.lock:
                data, rev, mems = self.lite_json, self.mem_rev, self.mem_json
            try:
                if rev != last_rev:
                    last_rev = rev
                    ws.send(0x1, b'{"mems":' + mems + b'}')
                if data is not last:
                    last = data
                    ws.send(0x1, b'{"st":' + data + b'}')
            except OSError:
                sess.close()
                return
            time.sleep(0.1)

    def publish(self, state, mems=None):
        data = json.dumps(state, separators=(",", ":")).encode("utf-8")
        mdata = json.dumps(mems, separators=(",", ":")).encode("utf-8") if mems is not None else None
        with self.lock:
            self.state_json = data
            if mdata is not None:
                self.mem_json = mdata
                self.mem_rev += 1

    def publish_lite(self, state):
        data = json.dumps(state, separators=(",", ":")).encode("utf-8")
        with self.lock:
            self.lite_json = data


# -----------------------------------------------------------------
# 4c. ICOM NETWORK (LAN) LINK - used for the spectrum scope over Ethernet
#     Same UDP protocol as RS-BA1 / wfview: control on 50001, CI-V on 50002, audio on 50003.
# -----------------------------------------------------------------
LAN_DEFAULT_PORT = 50001

_LAN_PASSCODE = bytes([0] * 32 + [
    0x47, 0x5d, 0x4c, 0x42, 0x66, 0x20, 0x23, 0x46, 0x4e, 0x57, 0x45, 0x3d, 0x67, 0x76, 0x60, 0x41,
    0x62, 0x39, 0x59, 0x2d, 0x68, 0x7e, 0x7c, 0x65, 0x7d, 0x49, 0x29, 0x72, 0x73, 0x78, 0x21, 0x6e,
    0x5a, 0x5e, 0x4a, 0x3e, 0x71, 0x2c, 0x2a, 0x54, 0x3c, 0x3a, 0x63, 0x4f, 0x43, 0x75, 0x27, 0x79,
    0x5b, 0x35, 0x70, 0x48, 0x6b, 0x56, 0x6f, 0x34, 0x32, 0x6c, 0x30, 0x61, 0x6d, 0x7b, 0x2f, 0x4b,
    0x64, 0x38, 0x2b, 0x2e, 0x50, 0x40, 0x3f, 0x55, 0x33, 0x37, 0x25, 0x77, 0x24, 0x26, 0x74, 0x6a,
    0x28, 0x53, 0x4d, 0x69, 0x22, 0x5c, 0x44, 0x31, 0x36, 0x58, 0x3b, 0x7a, 0x51, 0x5f, 0x52, 0])


def icom_passcode(text):
    """Icom's scrambling of the network user name / password (16 bytes)."""
    out = bytearray()
    for i, ch in enumerate(str(text).encode("ascii", "replace")[:16]):
        p = ch + i
        if p > 126:
            p = 32 + p % 127
        out.append(_LAN_PASSCODE[p])
    return bytes(out).ljust(16, b"\0")


def _extract_civ(buf):
    """Split complete CI-V frames (FE FE ... FD) out of a bytearray buffer."""
    out = []
    while True:
        i = buf.find(STOP_BYTE)
        if i < 0:
            break
        frame = bytes(buf[:i + 1])
        del buf[:i + 1]
        j = frame.find(b"\xfe\xfe")
        if j >= 0:
            out.append(list(frame[j:]))
    if len(buf) > 4096:
        buf.clear()
    return out


class _LanStream:
    """One UDP stream to the radio (control, CI-V or audio): handshake, pings, idle and resends."""

    def __init__(self, sock, remote):
        self.sock, self.remote = sock, remote
        lip, lport = sock.getsockname()[:2]
        try:
            a = socket.inet_aton(lip)
        except OSError:
            a = b"\0\0\0\0"
        self.my_id = struct.pack("<I", (a[2] << 24) | (a[3] << 16) | (lport & 0xFFFF))
        self.remote_id = b"\0\0\0\0"
        self.here = self.ready = self.closed = False
        self.seq = 1
        self.ping_seq = 0
        self.sent = {}
        self.last_tx = self.last_ping = self.last_hello = 0.0
        self.last_rx = time.time()

    def _hdr(self, p, ptype, seq):
        struct.pack_into("<IHH", p, 0, len(p), ptype, seq & 0xFFFF)
        p[8:12] = self.my_id
        p[12:16] = self.remote_id

    def raw(self, p):
        try:
            self.sock.sendto(bytes(p), self.remote)
        except OSError:
            pass
        self.last_tx = time.time()

    def control(self, ptype, seq=0):
        p = bytearray(16)
        self._hdr(p, ptype, seq)
        self.raw(p)

    def tracked(self, p):
        seq = self.seq
        self.seq = (self.seq + 1) & 0xFFFF
        self._hdr(p, 0x00, seq)
        b = bytes(p)
        self.sent[seq] = b
        if len(self.sent) > 300:
            del self.sent[next(iter(self.sent))]
        self.raw(b)

    def resend(self, seq):
        b = self.sent.get(seq)
        if b is not None:
            self.raw(b)
        else:
            p = bytearray(16)
            self._hdr(p, 0x00, seq)
            self.raw(p)

    def tick(self, now):
        if self.closed:
            return
        if not (self.here and self.ready):
            if now - self.last_hello >= 0.5:
                self.last_hello = now
                self.control(0x06 if self.here else 0x03, 1 if self.here else 0)
            return
        if now - self.last_ping >= 0.5:
            self.last_ping = now
            p = bytearray(0x15)
            self._hdr(p, 0x07, self.ping_seq)
            self.ping_seq = (self.ping_seq + 1) & 0xFFFF
            struct.pack_into("<I", p, 0x11, int(time.monotonic() * 1000) & 0xFFFFFFFF)
            self.raw(p)
        if now - self.last_tx >= 0.1:
            self.tracked(bytearray(16))            # idle

    def handle(self, d):
        """Packets common to every stream. Returns True when handled here."""
        self.last_rx = time.time()
        if len(d) < 16:
            return True
        ptype, seq = struct.unpack_from("<HH", d, 4)
        if len(d) == 0x10:
            if ptype == 0x04:                      # "I am here"
                if not self.here:
                    self.remote_id = bytes(d[8:12])
                    self.here = True
                    self.last_hello = 0.0
            elif ptype == 0x06:                    # "I am ready"
                self.ready = True
            elif ptype == 0x05:                    # disconnect
                self.closed = True
            elif ptype == 0x01:
                self.resend(seq)
            return True
        if ptype == 0x07 and len(d) >= 0x15:       # ping: answer the radio's, ignore replies to ours
            if d[0x10] == 0x00:
                r = bytearray(d[:0x15])
                r[8:12] = self.my_id
                r[12:16] = self.remote_id
                r[0x10] = 0x01
                self.raw(r)
            return True
        if ptype == 0x01:                          # several packets to send again
            for i in range(0x10, len(d) - 1, 2):
                self.resend(struct.unpack_from("<H", d, i)[0])
            return True
        return False


class LanLink:
    """Logs in to the IC-9700 over the network and opens its CI-V stream.
    on_civ(bytes) gets CI-V data from the radio, on_status(text, colour, open) reports progress.
    Runs on its own thread; send_civ() can be called from any thread."""

    def __init__(self, ip, port, user, password, on_civ, on_status):
        self.ip, self.port = ip, int(port or LAN_DEFAULT_PORT)
        self.user, self.password = user, password
        self.on_civ, self.on_status = on_civ, on_status
        self.outq = queue.Queue()
        self.want = True
        self.is_open = False
        self.fatal = False                         # wrong password etc.: don't retry by itself
        self.last_civ = 0.0
        self.thread = threading.Thread(target=self._run, daemon=True)

    @property
    def alive(self):
        return self.thread.is_alive()

    def start(self):
        self.thread.start()

    def stop(self, wait=True):
        self.want = False
        if wait and self.thread.is_alive() and self.thread is not threading.current_thread():
            self.thread.join(timeout=2)

    def send_civ(self, data):
        self.outq.put(bytes(data))

    def _status(self, text, colour, opened=False):
        try:
            self.on_status(text, colour, opened)
        except Exception:
            pass

    def _run(self):
        socks = []
        try:
            self._session(socks)
        except Exception as e:
            self._status(f"LAN: {e}", RED)
        finally:
            self.is_open = False
            for s in socks:
                try:
                    s.close()
                except OSError:
                    pass

    def _session(self, socks):
        try:
            ip = socket.gethostbyname(self.ip.strip())
        except OSError:
            self.fatal = True
            self._status(f"LAN: can't find the radio address '{self.ip}'", RED)
            return

        def udp():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(("", 0))
            s.connect((ip, 9))                      # picks the local address used to reach the radio
            lip = s.getsockname()[0]
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((lip, 0))
            socks.append(s)
            return s

        ctl = _LanStream(udp(), (ip, self.port))
        csock, asock = udp(), udp()                 # local CI-V / audio ports, offered to the radio
        civ = aud = None
        tok_req = secrets.token_bytes(2)
        token = b"\0\0\0\0"
        auth_seq = [0x30]
        caps = None
        caps_time = 0.0
        login_sent = logged = requested = civ_open = False
        token_time = 0.0
        civ_seq = [0]
        start = time.time()

        def auth(size, rtype):
            p = bytearray(size)
            struct.pack_into(">H", p, 0x12, size - 0x10)
            p[0x14], p[0x15] = 0x01, rtype
            struct.pack_into(">H", p, 0x16, auth_seq[0])
            auth_seq[0] = (auth_seq[0] + 1) & 0xFFFF
            p[0x1a:0x1c] = tok_req
            p[0x1c:0x20] = token
            return p

        def send_token(rtype):
            p = auth(0x40, rtype)
            p[0x24:0x26] = b"\x07\x98"
            ctl.tracked(p)

        def civ_packet(payload):
            p = bytearray(0x15 + len(payload))
            p[0x10] = 0xC1
            struct.pack_into("<H", p, 0x11, len(payload))
            struct.pack_into(">H", p, 0x13, civ_seq[0])
            civ_seq[0] = (civ_seq[0] + 1) & 0xFFFF
            p[0x15:] = payload
            civ.tracked(p)

        def open_close(on):
            p = bytearray(0x16)
            p[0x10:0x12] = b"\xc0\x01"
            struct.pack_into(">H", p, 0x13, civ_seq[0])
            civ_seq[0] = (civ_seq[0] + 1) & 0xFFFF
            p[0x15] = 0x04 if on else 0x00
            civ.tracked(p)

        def request_stream():
            p = auth(0x90, 0x03)
            p[0x20:0x30] = caps[0x00:0x10]          # radio's GUID / MAC, as it sent it
            p[0x40:0x60] = caps[0x10:0x30]          # radio name
            p[0x60:0x70] = icom_passcode(self.user)
            p[0x70], p[0x71], p[0x72], p[0x73] = 1, 1, 0x01, 0x01     # rx/tx audio on, mu-law (not used)
            struct.pack_into(">IIIII", p, 0x74, 8000, 8000, csock.getsockname()[1], asock.getsockname()[1], 150)
            p[0x88] = 1
            ctl.tracked(p)

        self._status(f"LAN: connecting to {self.ip}:{self.port} ...", MUTED)
        while self.want:
            now = time.time()
            ready = [s for s in socks if s.fileno() >= 0]
            try:
                r, _, _ = select.select(ready, [], [], 0.05)
            except (OSError, ValueError):
                r = []
            for s in r:
                try:
                    d, addr = s.recvfrom(4096)
                except OSError:
                    continue
                if addr[0] != ip:
                    continue
                if s is ctl.sock:
                    if ctl.handle(d):
                        continue
                    n = len(d)
                    if n == 0x60:                                    # login reply
                        if d[0x30:0x34] == b"\xfe\xff\xff\xff":
                            self.fatal = True
                            self._status("LAN: the radio rejected the user name / password "
                                         "(SET > Network > Network User1)", RED)
                            self.want = False
                            break
                        token = bytes(d[0x1c:0x20])
                        logged, token_time = True, now
                        send_token(0x02)
                    elif n == 0x40:                                  # token reply
                        if d[0x15] == 0x05 and d[0x30:0x34] == b"\xff\xff\xff\xff":
                            self._status("LAN: token renewal refused - reconnecting", ORANGE)
                            self.want = False
                            break
                    elif n >= 0x42 + 0x66 and (n - 0x42) % 0x66 == 0:     # capabilities
                        caps, caps_time = bytes(d[0x42:0x42 + 0x66]), now
                    elif n == 0x90:                                  # radio's connection info
                        if caps is not None and not requested:
                            requested = True
                            request_stream()
                    elif n == 0x50:                                  # stream status
                        if d[0x30:0x34] == b"\xff\xff\xff\xff":
                            self._status("LAN: the radio refused the stream - is RS-BA1 / wfview "
                                         "or another program connected?", RED)
                            self.want = False
                            break
                        if d[0x40] == 0x01:
                            self._status("LAN: the radio closed the connection", ORANGE)
                            self.want = False
                            break
                        cport = struct.unpack_from(">H", d, 0x42)[0]
                        aport = struct.unpack_from(">H", d, 0x46)[0]
                        if civ is None and cport:
                            civ = _LanStream(csock, (ip, cport))
                            if aport:
                                aud = _LanStream(asock, (ip, aport))
                elif civ is not None and s is csock:
                    if civ.handle(d):
                        continue
                    if len(d) > 0x15 and d[4] == 0x00:
                        self.last_civ = now
                        self.on_civ(bytes(d[0x15:]))
                elif aud is not None and s is asock:
                    aud.handle(d)                                    # audio itself isn't used
            if not self.want:
                break
            now = time.time()
            ctl.tick(now)
            if ctl.here and ctl.ready and not login_sent:
                login_sent = True
                p = auth(0x80, 0x00)
                p[0x1c:0x20] = b"\0\0\0\0"
                p[0x40:0x50] = icom_passcode(self.user)
                p[0x50:0x60] = icom_passcode(self.password)
                p[0x60:0x70] = b"IC9700Monitor".ljust(16, b"\0")
                ctl.tracked(p)
            if caps is not None and not requested and now - caps_time > 1.0:
                requested = True
                request_stream()
            if logged and now - token_time > 60:
                token_time = now
                send_token(0x05)
            for st in (civ, aud):
                if st is not None:
                    st.tick(now)
            if civ is not None and civ.here and civ.ready and not civ_open:
                civ_open = True
                open_close(True)
                self.is_open = True
                self._status("LAN: connected - scope data over the network", GREEN, True)
            if civ_open:
                while True:
                    try:
                        civ_packet(self.outq.get_nowait())
                    except queue.Empty:
                        break
            if any(st is not None and st.closed for st in (ctl, civ)):
                self._status("LAN: the radio closed the connection", ORANGE)
                break
            if not ctl.here and now - start > 6:
                self._status(f"LAN: no reply from {self.ip}:{self.port} - check the IP address and "
                             "SET > Network > Network Control = ON", RED)
                break
            if ctl.here and now - ctl.last_rx > 8:
                self._status("LAN: the radio stopped answering", ORANGE)
                break
            if logged and not civ_open and now - token_time > 15 and now - start > 15:
                self._status("LAN: logged in, but the radio didn't open its CI-V stream", ORANGE)
                break
        # polite goodbye, so the radio frees the connection straight away
        try:
            if civ_open:
                open_close(False)
            if logged:
                send_token(0x01)
            for st in (civ, aud, ctl):
                if st is not None and st.here:
                    st.control(0x05)
        except Exception:
            pass
        self.is_open = False


# -----------------------------------------------------------------
# 5. MAIN APPLICATION
# -----------------------------------------------------------------
class IC9700Controller:
    def __init__(self, root):
        self.root = root
        init_fonts(root)
        self.root.title("IC-9700 Monitor : By GM0OTB")
        self.config = load_config()
        self.root.configure(bg=BG, highlightthickness=px(3), highlightbackground=BG, highlightcolor=BG)
        res_dir = getattr(sys, "_MEIPASS", BASE_DIR)
        try:
            self.root.iconbitmap(default=os.path.join(res_dir, "ic9700.ico"))
        except Exception:
            try:
                self._icon_img = tk.PhotoImage(file=os.path.join(res_dir, "ic9700.png"))
                self.root.iconphoto(True, self._icon_img)
            except Exception:
                pass

        self.ser = None
        self.running = False
        self.want_connect = True
        self.io_error = False
        self.io_lock = threading.Lock()
        self.cmdq = queue.Queue()
        self.uiq = queue.Queue()       # callbacks from the polling thread to the Tk thread
        self.poll_thread = None
        self.radio_addr = parse_ci_v(self.config["ci_v"]) or DEFAULT_RADIO_ADDR
        self.port_name = ""
        self.baud = self.config.get("baud", 19200)
        self.rig_name = ""

        self.is_tx = False
        self.flash_on = False
        self.swr_sev = 0
        self.pwr_frac = 0.0
        self.rx_busy = False
        self.busy_on = False
        self.cur_hz = None
        self.cur_mode = None
        self.cur_filter = None
        self.tune_time = 0.0
        self.mode_time = 0.0
        self.mode_refresh = False
        self.pending_hz = None
        self.freq_queued = False
        self.pending_levels = {}
        self.level_touch = {}
        self.level_vals = {sub: None for _, sub, _ in LEVELS}
        self._lvl_guard = False
        self.full_sync = True
        self.toggle_state = {k: None for k in TOGGLES}
        self.toggle_touch = {}
        self.toggle_btns = {k: [] for k in TOGGLES}
        self.dup_state = None
        self.dup_touch = 0.0
        self.rit_hz = 0
        self.vd = None
        self.ptt_on = False
        self.ptt_since = 0.0
        self.status_hold = 0.0
        self.link_ok = True
        self.rig_off = False

        self.meter_frac = 0.0
        self.meter_mode = "rx"
        self.peak_frac = 0.0
        self.peak_time = 0.0
        self.tx_text = {}
        self.scan = None
        self.sweep = None
        self._sweep_drawn = 0.0
        self.qso_log = load_qso_log()
        self.rxbuf = bytearray()
        self.hover_digit = None
        self.digit_hits = []
        self.freq_color = LCD_TEXT
        self._freq_key = None
        self._pending_draw = set()
        # SUB band readout (CI-V 25 01 / 26 01)
        self.sub_hz = None
        self.sub_mode = None
        self.sub_nak = 0
        # Spectrum scope (CI-V 27)
        self.scope_on = bool(self.config.get("scope_on", False))
        self.scope_acc = None
        self.scope_last = 0.0
        self.scope_data = None          # (lo_hz, hi_hz, [amplitudes 0-160])
        self.scope_span = None          # last known (lo_hz, hi_hz): clicks keep working between sweeps
        self.scope_hover_x = None
        self.scope_centre = False       # radio scope in centre mode (from the waveform header)
        self.scope_offset = 0           # scope centre minus dial frequency in centre mode (SSB: ~1.5 kHz)
        self.span_set = None            # span just chosen with the SPAN key (until the radio confirms it)
        self.span_time = 0.0
        self.web_span = None
        self.scope_time = 0.0
        self.scope_enable_pending = False
        self.wf_rows = deque(maxlen=200)
        self.wf_img = None
        # Memory read from the radio (CI-V 1A 00)
        self.memread = None
        self.memread_win = None
        # Spectrum scope over the network (Icom LAN protocol)
        self.lan = None
        self.lan_buf = bytearray()
        self.lan_retry = 0.0
        self.lan_text = ""
        self.lan_kick = 0.0
        self.scope_lock = threading.Lock()

        self.slow_reads = [(k, (lambda k=k: self.read_toggle(k))) for k in TOGGLES]
        self.slow_reads += [("dup", self.read_dup), ("tone_hz", lambda: self.read_tone(0x00)),
                            ("tsql_hz", lambda: self.read_tone(0x01)), ("rit_hz", self.read_rit),
                            ("vd", lambda: self.parse_level(self.send_cmd(0x15, 0x15)))]
        self.slow_idx = 0
        # Phone / browser access
        self.web = WebBridge(self)
        self.audio = AudioEngine(self) if AUDIO_READY else None
        self.cwdec = CwDecoder(self)
        self.cwd_win = None
        self.cwdec.on_text = self.cwd_append
        self.web_keyed = False
        self.web_note = None
        self.sql_live = (None, 0.0)          # (squelch open?, when) straight from the polling thread
        self.web_mem_dirty = True
        self.web_mem_rev = 0
        self.web_scope_seq = 0

        self.setup_styles()
        self.create_menu()
        self.create_widgets()
        self.fit_window()
        self.root.attributes("-topmost", bool(self.config.get("topmost")))
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self._win_state = "normal"
        self._normal_geom = None                       # last size / position while not maximised
        self.root.bind("<Configure>", self._on_root_configure, add="+")
        self.root.bind("<Up>", lambda e: self.key_step(+1))
        self.root.bind("<Down>", lambda e: self.key_step(-1))
        self.root.bind("<Prior>", lambda e: self.key_step(+1, 1_000_000))
        self.root.bind("<Next>", lambda e: self.key_step(-1, 1_000_000))

        self.flash_tx()
        self.clock_tick()
        self.ui_pump()

        if not SERIAL_READY:
            self.root.after(300, self.show_lib_error)
        else:
            self.root.after(100, lambda: self.auto_connect(quiet=False))
            self.root.after(RECONNECT_MS, self.reconnect_tick)
        self.start_web(quiet=True)
        self.root.after(500, self.web_tick)
        self.root.after(600, self.lite_tick)

    # ------------------------------------------------------------- setup
    def show_lib_error(self):
        messagebox.showerror("Error", "pyserial library missing!\nRun: python -m pip install pyserial")
        self.root.destroy()

    def setup_styles(self):
        st = ttk.Style(self.root)
        try:
            st.theme_use("clam")
        except tk.TclError:
            pass
        st.configure("TCombobox", fieldbackground=FIELD, background=BTN, foreground=TEXT,
                     arrowcolor=MUTED, bordercolor=BORDER, lightcolor=BORDER, darkcolor=BORDER,
                     padding=(4, 2))
        st.map("TCombobox", fieldbackground=[("readonly", FIELD)], foreground=[("readonly", TEXT)],
               selectbackground=[("readonly", FIELD)], selectforeground=[("readonly", TEXT)],
               bordercolor=[("focus", ACCENT_LO)], arrowcolor=[("active", ACCENT)])
        self.root.option_add("*TCombobox*Listbox.background", PANEL)
        self.root.option_add("*TCombobox*Listbox.foreground", TEXT)
        self.root.option_add("*TCombobox*Listbox.selectBackground", ACCENT_DIM)
        self.root.option_add("*TCombobox*Listbox.selectForeground", ACCENT)
        self.root.option_add("*TCombobox*Listbox.font", F["ui"])
        st.configure("Treeview", background=FIELD, fieldbackground=FIELD, foreground=TEXT,
                     rowheight=px(22), borderwidth=0, font=F["ui"])
        st.map("Treeview", background=[("selected", ACCENT_DIM)], foreground=[("selected", ACCENT)])
        st.configure("Treeview.Heading", background=PANEL, foreground=MUTED, relief="flat",
                     font=F["small_b"], borderwidth=0)
        st.map("Treeview.Heading", background=[("active", BTN)])
        st.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])
        for sname in ("TScrollbar", "Vertical.TScrollbar"):
            st.configure(sname, background=BTN, troughcolor=FIELD, arrowcolor=MUTED,
                         bordercolor=FIELD, lightcolor=BTN, darkcolor=BTN, gripcount=0)
        st.map("Vertical.TScrollbar", background=[("active", BTN_HOVER)])
        st.configure("Vertical.TScrollbar", background=BTN, troughcolor=FIELD, arrowcolor=MUTED,
                     bordercolor=FIELD, lightcolor=BTN, darkcolor=BTN, gripcount=0)

    # widget helpers
    def btn(self, parent, text, cmd, width=64, height=26, tone="accent"):
        return RoundButton(parent, text, cmd, width=width, height=height, tone=tone)

    def lbl(self, parent, text, **kw):
        kw.setdefault("bg", parent.cget("bg"))
        kw.setdefault("fg", TEXT)
        kw.setdefault("font", F["ui"])
        return tk.Label(parent, text=text, **kw)

    def caption(self, parent, text):
        return tk.Label(parent, text=text.upper(), bg=parent.cget("bg"), fg=MUTED, font=F["small_b"])

    def entry(self, parent, width=12, **kw):
        return tk.Entry(parent, width=width, font=F["ui"], bg=FIELD, fg=TEXT, insertbackground=ACCENT,
                        relief="flat", highlightthickness=1, highlightbackground=BORDER,
                        highlightcolor=ACCENT_LO, disabledbackground=FIELD, **kw)

    def spin(self, parent, lo, hi, inc, default, width=5):
        sp = tk.Spinbox(parent, from_=lo, to=hi, increment=inc, width=width, bg=FIELD, fg=TEXT,
                        insertbackground=ACCENT, buttonbackground=BTN, relief="flat",
                        highlightthickness=1, highlightbackground=BORDER, highlightcolor=ACCENT_LO,
                        font=F["ui"])
        sp.delete(0, tk.END)
        sp.insert(0, str(default))
        return sp

    def check(self, parent, text, var):
        return tk.Checkbutton(parent, text=text, variable=var, bg=parent.cget("bg"), fg=TEXT,
                              selectcolor=FIELD, activebackground=parent.cget("bg"), activeforeground=TEXT,
                              font=F["ui"], highlightthickness=0, bd=0)

    def card(self, parent, **pack):
        fr = tk.Frame(parent, bg=PANEL, highlightthickness=1, highlightbackground=BORDER)
        if pack:
            fr.pack(**pack)
        return fr

    def grid_row(self, parent, items, pady=3, padx=10, uniform="g"):
        """items: list of (text, cmd[, tone]) or ready widgets factories; returns list of buttons."""
        fr = tk.Frame(parent, bg=parent.cget("bg"))
        fr.pack(fill="x", padx=padx, pady=pady)
        out = []
        for i, it in enumerate(items):
            fr.columnconfigure(i, weight=1, uniform=uniform)
            b = self.btn(fr, it[0], it[1], width=40, tone=it[2] if len(it) > 2 else "accent")
            b.grid(row=0, column=i, padx=px(3), sticky="ew")
            out.append(b)
        return fr, out

    def toggle_button(self, parent, key, width=40, height=26):
        label = TOGGLES[key][0]
        tone = "amber" if key in ("lock", "att") else "accent"
        b = RoundButton(parent, label, lambda: self.click_toggle(key), width=width, height=height, tone=tone)
        self.toggle_btns[key].append(b)
        return b

    def create_menu(self):
        menubar = tk.Menu(self.root)
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Settings...", command=self.open_settings)
        settings_menu.add_command(label="Phone access...", command=self.open_web_settings)
        settings_menu.add_command(label="Reconnect", command=self.user_reconnect)
        settings_menu.add_command(label="Disconnect", command=lambda: self.disconnect(user=True))
        settings_menu.add_separator()
        settings_menu.add_command(label="Re-read radio state", command=self.request_full_sync)
        menubar.add_cascade(label="Settings", menu=settings_menu)

        view_menu = tk.Menu(menubar, tearoff=0)
        self.topmost_var = tk.BooleanVar(value=bool(self.config.get("topmost")))
        view_menu.add_checkbutton(label="Always on top", variable=self.topmost_var,
                                  command=self.toggle_topmost)
        self.scope_visible_var = tk.BooleanVar(value=bool(self.config.get("scope_visible", True)))
        view_menu.add_checkbutton(label="Show scope / waterfall", variable=self.scope_visible_var,
                                  command=lambda: self.show_scope_panel(self.scope_visible_var.get()))
        view_menu.add_separator()
        view_menu.add_command(label="Reset window size", command=self.reset_window_size)
        view_menu.add_command(label="CW decoder...", command=self.open_cw_decoder)
        menubar.add_cascade(label="View", menu=view_menu)
        phone_menu = tk.Menu(menubar, tearoff=0)
        phone_menu.add_command(label="Phone access, audio (RX / TX) && HTTPS...", command=self.open_web_settings)
        phone_menu.add_command(label="Turn on HTTPS (for the phone microphone)",
                               command=lambda: self.setup_https(self.root, lambda: None))
        phone_menu.add_separator()
        phone_menu.add_command(label="Open the phone page on this PC", command=self.open_phone_page)
        phone_menu.add_command(label="Open the LITE phone page on this PC (clear audio, quick PTT)",
                               command=lambda: self.open_phone_page("lite"))
        menubar.add_cascade(label="Phone", menu=phone_menu)
        menubar.add_command(label="About", command=self.show_about)
        self.root.config(menu=menubar)

    def show_about(self):
        win = tk.Toplevel(self.root)
        win.title("About")
        win.configure(bg=BG)
        win.resizable(False, False)
        win.transient(self.root)
        self.lbl(win, "IC-9700 Monitor", font=F["big"]).pack(padx=50, pady=(22, 4))
        self.lbl(win, "CI-V control panel", fg=MUTED).pack()
        self.lbl(win, f"Version {APP_VERSION}", fg=ACCENT).pack(pady=(10, 2))
        self.lbl(win, f"Author: {APP_AUTHOR}", fg=ACCENT).pack(pady=2)
        try:
            tkv = self.root.tk.call("info", "patchlevel")
            scal = float(self.root.tk.call("tk", "scaling"))
        except tk.TclError:
            tkv, scal = "?", 0.0
        diag = (f"Python {sys.version.split()[0]} · Tk {tkv} · scale {SCALE:.2f} (tk {scal:.2f}) · DPI {dpi_mode()}"
                f"\n{'Installed program' if getattr(sys, 'frozen', False) else 'Running IC9700.py'} · settings: {BASE_DIR}")
        self.lbl(win, diag, fg=DIM, font=F["small"], justify="center").pack(pady=(8, 0), padx=16)
        self.lbl(win, "Wheel over a digit tunes that digit  ·  PgUp/PgDn = 1 MHz",
                 fg=MUTED, font=F["small"]).pack(pady=(10, 0), padx=16)
        self.btn(win, "OK", win.destroy, width=90).pack(pady=(14, 18))
        win.update_idletasks()
        x = self.root.winfo_rootx() + (self.root.winfo_width() - win.winfo_width()) // 2
        y = self.root.winfo_rooty() + 80
        win.geometry(f"+{max(x, 0)}+{max(y, 0)}")
        win.grab_set()
        win.focus_set()
        win.bind("<Return>", lambda e: win.destroy())
        win.bind("<Escape>", lambda e: win.destroy())

    def design_width(self):
        """Smallest sensible window width: what the radio panel itself needs. The title row and the
        status bar are left out on purpose - their text is cut off instead of widening the window."""
        self.root.update_idletasks()
        skip = {getattr(self, "sbar", None), getattr(self, "head", None)}
        need = 0
        for w in self.root.winfo_children():
            if w in skip or w.winfo_manager() == "":
                continue
            if isinstance(w, (tk.Menu, tk.Toplevel)):
                continue
            try:
                need = max(need, int(w.winfo_reqwidth()))
            except tk.TclError:
                pass
        return max(px(540), need)

    def fit_window(self):
        self.root.update_idletasks()
        try:
            req_h = int(self.root.winfo_reqheight())
            req_w = self.design_width()
        except Exception:
            req_h, req_w = 760, 560
        m = re.match(r"(\d+)x\d+([+-]-?\d+[+-]-?\d+)?", self.config.get("geometry") or "")
        min_w = req_w
        if int(self.config.get("geom_fix") or 0) < 4:  # older versions could save an oversized window: reset once
            self.config["geom_fix"] = 4
            width = min_w
        else:
            width = max(min_w, int(m.group(1))) if m else min_w
        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        width = min(width, max(min_w, sw - px(40)))         # never wider than the screen
        pos = (m.group(2) or "") if m else ""
        pm = re.match(r"([+-])(-?\d+)([+-])(-?\d+)", pos)
        if pm and not (-px(50) < int(pm.group(2)) < sw - px(100) and 0 <= int(pm.group(4)) < sh - px(100)):
            pos = ""                                         # saved position is off screen
        self.root.minsize(min_w, req_h)
        self.root.geometry(f"{width}x{req_h}{pos}")

    def _on_root_configure(self, e):
        if e.widget is not self.root:
            return
        try:
            st = self.root.state()
        except tk.TclError:
            return
        prev, self._win_state = self._win_state, st
        if st == "normal":
            if prev == "zoomed":
                self.root.after(30, self._after_restore)        # just un-maximised
            else:
                self._normal_geom = self.root.geometry()

    def _after_restore(self):
        """Back from maximised: return to the normal size, with the digits re-fitted to it."""
        if self.root.state() != "normal":
            return
        m = re.match(r"(\d+)x(\d+)([+-]-?\d+[+-]-?\d+)?", self._normal_geom or "")
        if m:
            self.root.geometry(f"{m.group(1)}x{m.group(2)}{m.group(3) or ''}")
        self._freq_fit = None
        self.root.update_idletasks()
        self.draw_freq(force=True)
        self.root.after(60, self.refit_height)

    def reset_window_size(self):
        if self.root.state() == "zoomed":
            self.root.state("normal")
        self.root.update_idletasks()
        self._freq_fit = None
        w = self.design_width()                                # same as a fresh start
        self.root.geometry(f"{w}x{self.root.winfo_reqheight()}")
        self.root.after(50, self.refit_height)

    # ------------------------------------------------------------ power on / off
    def radio_is_on(self):
        return bool(self.running and self.link_ok and not self.rig_off)

    def refresh_power(self):
        on = self.radio_is_on()
        self.btn_power.set_active(on, "POWER" if on or not self.rig_off else "POWER OFF",
                                  tone="green" if on else "red", dim=not on and not self.running)

    def power_click(self):
        if not self.running:
            messagebox.showinfo("Power", "The program isn't connected to the radio's USB port.\n"
                                "Plug in the USB cable (the radio can be off) and wait for the port to open.")
            return
        if self.radio_is_on():
            if not messagebox.askyesno("Power", "Switch the IC-9700 OFF?"):
                return
        self.power_set(not self.radio_is_on())

    def power_set(self, on, who=""):
        """Switch the radio on / off (Tk thread). Used by the POWER key and by the phone page."""
        if not self.running:
            return
        if not on:
            if self.ptt_on or self.is_tx:
                self.ptt_on = False
                self.post_cmd(0x1C, 0x00, [0x00])

            def off():
                f = self.send_cmd(0x18, 0x00)
                if f is not None and f[4] == NAK:
                    self.ui(self.flash_status, "RIG REJECTED POWER OFF (18 00)", RED)
                    return
                self.rig_off = True
                self.ui(self.set_link, False)
            self.post(off)
            self.flash_status(f"SWITCHING THE RADIO OFF{who} ...", AMBER, 3)
        else:
            self.post(self.power_on_job)
            self.flash_status(f"SWITCHING THE RADIO ON{who} ...", AMBER, 8)

    def power_on_job(self):                      # polling thread
        """CI-V 18 01 needs a run of FE bytes first to wake the radio's CPU (more at higher baud rates)."""
        ser = self.ser
        if not ser or not ser.is_open:
            return
        n = max(7, int(round(self.baud * 25 / 19200)))           # 19200: 25, 115200: 150
        frame = bytes([START_BYTE] * n + [START_BYTE, START_BYTE, self.radio_addr, CONTR_ADDR, 0x18, 0x01, STOP_BYTE])
        try:
            with self.io_lock:
                ser.write(frame)
                ser.flush()
        except Exception:
            self.io_error = True
            return
        self.rig_off = False
        self.full_sync = True
        self.ui(self.refresh_power)

    def toggle_topmost(self):
        self.config["topmost"] = bool(self.topmost_var.get())
        self.root.attributes("-topmost", self.config["topmost"])

    # ------------------------------------------------------------ layout
    def create_widgets(self):
        # Status strip (bottom of the window)
        sbar = self.sbar = tk.Frame(self.root, bg=PANEL2, highlightthickness=1, highlightbackground=BORDER)
        sbar.pack(side=tk.BOTTOM, fill="x")
        self.lbl_led = tk.Canvas(sbar, width=px(10), height=px(10), bg=PANEL2, highlightthickness=0)
        self.lbl_led.pack(side="left", padx=(px(8), px(4)), pady=px(5))
        self.lbl_status = tk.Label(sbar, text="SYSTEM OFFLINE", bg=PANEL2, fg=MUTED, font=F["small_b"], anchor="w",
                                   width=1)           # long messages are cut off instead of widening the window
        self.lbl_status.pack(side="left", fill="x", expand=True)
        self.lbl_port = tk.Label(sbar, text="", bg=PANEL2, fg=DIM, font=F["small_b"])
        self.lbl_port.pack(side="right", padx=8)

        # Faceplate lettering
        head = self.head = tk.Frame(self.root, bg=BG)
        head.pack(fill="x", padx=px(16), pady=(px(8), px(2)))
        self.btn_power = RoundButton(head, "POWER", self.power_click, width=74, height=26, tone="green")
        self.btn_power.pack(side="left", padx=(0, px(12)))
        tk.Label(head, text="I C - 9 7 0 0", bg=BG, fg="#cfd4db", font=F["model"]).pack(side="left")
        tk.Label(head, text="  VHF/UHF ALL MODE TRANSCEIVER", bg=BG, fg=DIM,
                 font=F["small_b"]).pack(side="left", pady=(px(4), 0))
        tk.Label(head, text=f"MONITOR {APP_VERSION} · {APP_AUTHOR}", bg=BG, fg=DIM,
                 font=F["small_b"]).pack(side="right", pady=(px(4), 0))

        # Bezel + screen
        bezel = tk.Frame(self.root, bg="#0c0d0f", highlightthickness=1, highlightbackground=LCD_EDGE)
        bezel.pack(fill="x", padx=px(12), pady=(px(2), px(6)))
        scr = tk.Frame(bezel, bg=LCD_BG)
        scr.pack(fill="both", expand=True, padx=px(5), pady=px(5))
        self.screen = scr

        def sep():
            tk.Frame(scr, bg=LCD_SEP, height=1).pack(fill="x", padx=px(4))

        # 1. top icon line: active functions, Vd, UTC clock
        self.status_canvas = tk.Canvas(scr, height=px(20), bg=LCD_BG, highlightthickness=0)
        self.status_canvas.pack(fill="x")
        self.status_canvas.bind("<Configure>", lambda e: self.draw_status())
        self.clock_text = "--:--"
        sep()

        # 2. MAIN band: indicator tags, frequency, meter
        tag_row = tk.Frame(scr, bg=LCD_BG)
        tag_row.pack(fill="x", pady=(px(4), 0))
        self.tags_canvas = tk.Canvas(tag_row, height=px(20), bg=LCD_BG, highlightthickness=0)
        self.tags_canvas.pack(side="left", fill="x", expand=True)
        self.tags_canvas.bind("<Configure>", lambda e: self.draw_tags())
        self.btn_vfo = RoundButton(tag_row, "MAIN ⇄ SUB", self.swap_bands, width=84, height=20,
                                   font=F["lcd_s"], radius=4, style="soft")
        self.btn_vfo.pack(side="right", padx=px(6))

        def tag(text, tone="accent", solid=False, hide_off=True):
            return LcdTag(lambda: self.schedule("draw_tags"), text, tone, solid, hide_off)

        self.chip_main = tag("MAIN", solid=True, hide_off=False)
        self.chip_main.active = True
        self.chip_mode = tag("--", hide_off=False)
        self.chip_fil = tag("FIL")
        self.chip_band = tag("BAND")
        self.chip_dup = tag("SIMP", "amber")
        self.chip_sat = tag("SAT")
        self.chip_scan = tag("SCAN", "amber", solid=True)
        self.chip_busy = tag("BUSY", "green", solid=True)
        self.chip_tx = tag("TX", "red", solid=True)
        self.chip_vd = LcdTag(lambda: self.schedule("draw_status"), "-- V", "green")

        self.freq_canvas = tk.Canvas(scr, bg=LCD_BG, highlightthickness=0,
                                     height=F["freq"].metrics("linespace") + px(2))
        self.freq_canvas.pack(fill="x", padx=px(4), pady=(0, px(4)))
        self.freq_canvas.bind("<Configure>", lambda e: self.draw_freq(force=True))
        self.freq_canvas.bind("<MouseWheel>", lambda e: self.freq_wheel(e.x, 1 if e.delta > 0 else -1))
        self.freq_canvas.bind("<Button-4>", lambda e: self.freq_wheel(e.x, 1))
        self.freq_canvas.bind("<Button-5>", lambda e: self.freq_wheel(e.x, -1))
        self.freq_canvas.bind("<Motion>", self.freq_hover)
        self.freq_canvas.bind("<Leave>", lambda e: self.freq_hover(None))
        self.freq_canvas.bind("<Button-1>", lambda e: self.focus_freq_entry())

        self.meter_canvas = tk.Canvas(scr, height=px(56), bg=LCD_BG, highlightthickness=0)
        self.meter_canvas.pack(fill="x", padx=px(4))
        self.meter_canvas.bind("<Configure>", self.draw_meter)

        read_row = tk.Frame(scr, bg=LCD_BG)
        read_row.pack(fill="x", padx=px(12))
        self.lbl_smeter = tk.Label(read_row, text="", font=F["mono_b"], bg=LCD_BG, fg=LCD_TEXT)
        self.lbl_smeter.pack(side="left")
        self.lbl_info = tk.Label(read_row, text="", font=F["mono_b"], bg=LCD_BG, fg=LCD_LABEL)
        self.lbl_info.pack(side="right")
        sep()

        # 3. SUB band (double-click to swap)
        self.sub_canvas = tk.Canvas(scr, height=F["sub"].metrics("ascent") + px(10), bg=LCD_BG, highlightthickness=0, cursor="hand2")
        self.sub_canvas.pack(fill="x", padx=px(4))
        self.sub_canvas.bind("<Configure>", lambda e: self.draw_sub())
        self.sub_canvas.bind("<Double-Button-1>", lambda e: self.swap_bands())
        sep()

        # 4. AF / PWR / SQL bars
        self.levels_canvas = tk.Canvas(scr, height=px(20), bg=LCD_BG, highlightthickness=0)
        self.levels_canvas.pack(fill="x", padx=px(6), pady=(px(1), 0))
        self.levels_canvas.bind("<Configure>", self.draw_levels)

        # 5. spectrum scope + waterfall
        self.scope_canvas = tk.Canvas(scr, height=px(112), bg=LCD_BG, highlightthickness=0, cursor="crosshair")
        self.scope_visible = bool(self.config.get("scope_visible", True))
        if self.scope_visible:
            self.scope_canvas.pack(fill="x", padx=px(4), pady=(px(2), 0))
        self.scope_canvas.bind("<Configure>", lambda e: self.draw_scope(rebuild=True))
        self.scope_canvas.bind("<Button-1>", self.scope_click)
        self.scope_canvas.bind("<B1-Motion>", self.scope_click)
        self.scope_canvas.bind("<Motion>", self.scope_hover)
        self.scope_canvas.bind("<Leave>", lambda e: self.scope_hover(None))
        self.scope_canvas.bind("<MouseWheel>", lambda e: self.step_tune(1 if e.delta > 0 else -1))
        self.scope_canvas.bind("<Button-4>", lambda e: self.step_tune(1))
        self.scope_canvas.bind("<Button-5>", lambda e: self.step_tune(-1))

        # 6. soft keys along the bottom of the screen (select the control page)
        tabbar = tk.Frame(scr, bg=LCD_BG)
        tabbar.pack(fill="x", padx=px(3), pady=(px(4), px(3)))
        self.tab_btns = {}
        for i, name in enumerate(TABS):
            tabbar.columnconfigure(i, weight=1, uniform="t")
            b = RoundButton(tabbar, name, lambda n=name: self.show_tab(n), width=40, height=24,
                            font=F["lcd_s"], radius=4, style="soft")
            b.grid(row=0, column=i, padx=px(1), sticky="ew")
            self.tab_btns[name] = b

        # Rubber keys on the case
        qf = tk.Frame(self.root, bg=BG)
        qf.pack(fill="x", padx=px(12), pady=(0, px(6)))
        keys = ["pamp", "att", "agc", "nb", "nr", "anf", "lock"]
        for i, k in enumerate(keys):
            qf.columnconfigure(i, weight=1, uniform="q")
            self.toggle_button(qf, k, width=40, height=30).grid(row=0, column=i, padx=px(2), sticky="ew")
        qf.columnconfigure(len(keys), weight=1, uniform="q")
        self.btn_scope = RoundButton(qf, "SCOPE", self.toggle_scope, width=40, height=30)
        self.btn_scope.grid(row=0, column=len(keys), padx=px(2), sticky="ew")
        qf.columnconfigure(len(keys) + 1, weight=1, uniform="q")
        self.btn_span = RoundButton(qf, "SPAN", lambda: self.step_span(+1, wrap=True), width=40, height=30)
        self.btn_span.grid(row=0, column=len(keys) + 1, padx=px(2), sticky="ew")
        self.btn_span.bind("<Button-3>", lambda e: self.step_span(-1, wrap=True))
        self.btn_span.bind("<MouseWheel>", lambda e: self.step_span(1 if e.delta > 0 else -1))
        self.btn_span.bind("<Button-4>", lambda e: self.step_span(1))
        self.btn_span.bind("<Button-5>", lambda e: self.step_span(-1))
        qf.columnconfigure(len(keys) + 2, weight=2, uniform="q")
        self.btn_ptt = RoundButton(qf, "TRANSMIT", self.toggle_ptt, width=70, height=30, tone="red", solid=True,
                                   font=F["ui_b"])
        self.btn_ptt.grid(row=0, column=len(keys) + 2, padx=(px(6), px(2)), sticky="ew")

        # Control pages
        stack = self.card(self.root, fill="both", expand=True, padx=px(12), pady=(0, px(8)))
        stack.rowconfigure(0, weight=1)
        stack.columnconfigure(0, weight=1)
        self.pages = {}
        for name in TABS:
            f = tk.Frame(stack, bg=PANEL)
            f.grid(row=0, column=0, sticky="nsew")
            self.pages[name] = f
        self.build_tune_tab(self.pages["TUNE"])
        self.build_levels_tab(self.pages["LEVELS"])
        self.build_bands_tab(self.pages["BANDS"])
        self.build_func_tab(self.pages["FUNC"])
        self.build_cw_tab(self.pages["CW"])
        self.build_memory_tab(self.pages["MEMORY"])
        self.build_scan_tab(self.pages["SCAN"])
        self.build_log_tab(self.pages["LOG"])
        self.cur_tab = None
        self.show_tab(self.config.get("tab", "TUNE"))
        self.btn_scope.set_active(self.scope_on)
        self.update_port_label()
        self.set_led(MUTED)

    def show_tab(self, name):
        self.cur_tab = name
        self.config["tab"] = name
        self.pages[name].tkraise()
        for n, b in self.tab_btns.items():
            b.set_active(n == name)
        if name == "SCAN":
            self.draw_sweep()

    # ---------------------------------------------------------- tune tab
    def build_tune_tab(self, tab):
        self.caption(tab, "Mode").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        mf = tk.Frame(tab, bg=PANEL)
        mf.pack(fill="x", padx=px(9), pady=(px(3), 0))
        self.mode_btns = {}
        for i, m in enumerate(MODE_LIST):
            mf.columnconfigure(i, weight=1, uniform="m")
            b = self.btn(mf, m, lambda mm=m: self.set_radio_mode(mm), width=40)
            b.grid(row=0, column=i, padx=px(2), sticky="ew")
            self.mode_btns[m] = b

        ff = tk.Frame(tab, bg=PANEL)
        ff.pack(fill="x", padx=px(9), pady=(px(6), 0))
        self.fil_btns = {}
        for i in range(4):
            ff.columnconfigure(i, weight=1, uniform="f")
        for i in (1, 2, 3):
            b = self.btn(ff, f"FIL{i}", lambda n=i: self.set_filter(n), width=40)
            b.grid(row=0, column=i - 1, padx=px(2), sticky="ew")
            self.fil_btns[i] = b
        self.toggle_button(ff, "data").grid(row=0, column=3, padx=px(2), sticky="ew")

        self.caption(tab, "Tuning").pack(anchor="w", padx=px(12), pady=(px(10), 0))
        step_row = tk.Frame(tab, bg=PANEL)
        step_row.pack(fill="x", padx=px(12), pady=(px(3), 0))
        self.lbl(step_row, "Step").pack(side="left")
        self.step_var = tk.StringVar()
        step_box = ttk.Combobox(step_row, textvariable=self.step_var, state="readonly", width=9,
                                values=[s[0] for s in STEPS], font=F["ui"])
        step_box.pack(side="left", padx=px(6))
        saved = self.config.get("step_hz", 12500)
        self.step_var.set(next((n for n, v in STEPS if v == saved), "12.5 kHz"))
        step_box.bind("<<ComboboxSelected>>", lambda e: self.config.update(step_hz=self.step_hz()))
        self.btn(step_row, "▼", lambda: self.step_tune(-1), width=36).pack(side="left", padx=px(2))
        self.btn(step_row, "▲", lambda: self.step_tune(+1), width=36).pack(side="left", padx=px(2))
        for name, *_ in reversed(BANDS):
            self.btn(step_row, name, lambda n=name: self.band_click(n), width=50).pack(side="right", padx=px(2))

        entry_row = tk.Frame(tab, bg=PANEL)
        entry_row.pack(fill="x", padx=px(12), pady=(px(8), 0))
        self.lbl(entry_row, "Direct entry").pack(side="left")
        self.freq_entry = self.entry(entry_row, width=14, justify="center")
        self.freq_entry.config(font=F["mono_b"])
        self.freq_entry.pack(side="left", padx=px(6), ipady=px(3))
        self.freq_entry.bind("<Return>", lambda event: self.change_frequency())
        self.lbl(entry_row, "MHz", fg=MUTED).pack(side="left")
        self.btn(entry_row, "SET", self.change_frequency, width=60, tone="green").pack(side="left", padx=px(8))

        self.lbl(tab, "Scroll over a digit to tune it  ·  ▲/▼ keys = step  ·  PgUp/PgDn = 1 MHz",
                 fg=DIM, font=F["small"]).pack(side="bottom", pady=(0, px(6)))

    def focus_freq_entry(self):
        self.show_tab("TUNE")
        self.freq_entry.focus_set()

    # -------------------------------------------------------- levels tab
    def build_levels_tab(self, tab):
        grid = tk.Frame(tab, bg=PANEL)
        grid.pack(fill="both", expand=True, padx=px(8), pady=px(6))
        for c in (1, 4):
            grid.columnconfigure(c, weight=1)
        grid.columnconfigure(3, minsize=px(14))
        self.level_scales = {}
        self.level_labels = {}
        half = 8
        for i, (name, sub, fmt) in enumerate(LEVELS):
            col = 0 if i < half else 3
            row = i if i < half else i - half
            color = AMBER if sub in (0x0A, 0x0B, 0x0E, 0x16, 0x17) else ACCENT
            self.lbl(grid, name, fg=MUTED, font=F["small"], anchor="w", width=10).grid(
                row=row, column=col, sticky="w", padx=(px(4), 0), pady=px(1))
            sc = LevelSlider(grid, command=lambda v, s=sub: self.on_level(s, v), center=(fmt == "pbt"), color=color)
            sc.grid(row=row, column=col + 1, sticky="ew")
            lb = tk.Label(grid, text="--", width=6, anchor="e", bg=PANEL, fg=TEXT, font=F["mono_s"])
            lb.grid(row=row, column=col + 2, padx=(0, px(4)))
            self.level_scales[sub] = sc
            self.level_labels[sub] = lb
        self.lbl(tab, "Double-click a PBT slider to centre it  ·  mouse wheel fine-adjusts",
                 fg=DIM, font=F["small"]).pack(side="bottom", pady=(0, px(6)))

    # --------------------------------------------------------- bands tab
    def build_bands_tab(self, tab):
        self.caption(tab, "Main / Sub band").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        self.grid_row(tab, [("Select MAIN", lambda: self.vfo_cmd(0xD0, "MAIN SELECTED")),
                            ("Select SUB", lambda: self.vfo_cmd(0xD1, "SUB SELECTED")),
                            ("Swap M/S", self.swap_bands),
                            ("Equalize", lambda: self.vfo_cmd(0xA0, "MAIN = SUB"))])
        self.grid_row(tab, [("VFO A", lambda: self.vfo_cmd(0x00, "VFO A")),
                            ("VFO B", lambda: self.vfo_cmd(0x01, "VFO B")),
                            ("Dualwatch ON", lambda: self.vfo_cmd(0xC1, "DUALWATCH ON")),
                            ("Dualwatch OFF", lambda: self.vfo_cmd(0xC0, "DUALWATCH OFF"))])
        self.caption(tab, "Split / duplex").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        _, b = self.grid_row(tab, [("Simplex", lambda: self.set_duplex(0x10)),
                                   ("DUP-", lambda: self.set_duplex(0x11)),
                                   ("DUP+", lambda: self.set_duplex(0x12)),
                                   ("Split ON", lambda: self.set_duplex(0x01)),
                                   ("Split OFF", lambda: self.set_duplex(0x00))])
        self.dup_btns = dict(zip((0x10, 0x11, 0x12, 0x01, 0x00), b))

        self.caption(tab, "Repeater tone (CTCSS)").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        tr = tk.Frame(tab, bg=PANEL)
        tr.pack(fill="x", padx=px(12), pady=px(3))
        self.toggle_button(tr, "tone", width=70).pack(side="left", padx=(0, px(4)))
        self.toggle_button(tr, "tsql", width=70).pack(side="left", padx=px(4))
        self.lbl(tr, "Tone").pack(side="left", padx=(px(10), px(4)))
        self.tone_var = tk.StringVar(value="88.5")
        tb = ttk.Combobox(tr, textvariable=self.tone_var, state="readonly", width=6,
                          values=[f"{t:.1f}" for t in CTCSS], font=F["ui"])
        tb.pack(side="left")
        tb.bind("<<ComboboxSelected>>", lambda e: self.set_tone(0x00, self.tone_var.get()))
        self.lbl(tr, "TSQL").pack(side="left", padx=(px(10), px(4)))
        self.tsql_var = tk.StringVar(value="88.5")
        sb = ttk.Combobox(tr, textvariable=self.tsql_var, state="readonly", width=6,
                          values=[f"{t:.1f}" for t in CTCSS], font=F["ui"])
        sb.pack(side="left")
        sb.bind("<<ComboboxSelected>>", lambda e: self.set_tone(0x01, self.tsql_var.get()))
        self.lbl(tr, "Hz", fg=MUTED).pack(side="left", padx=px(4))

        self.caption(tab, "Satellite").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        sr = tk.Frame(tab, bg=PANEL)
        sr.pack(fill="x", padx=px(12), pady=px(3))
        self.toggle_button(sr, "sat", width=110).pack(side="left")
        self.lbl(sr, "Main = uplink, Sub = downlink. Use Swap M/S to exchange.",
                 fg=DIM, font=F["small"]).pack(side="left", padx=px(10))

    # ---------------------------------------------------------- func tab
    def build_func_tab(self, tab):
        self.caption(tab, "Receive").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        fr = tk.Frame(tab, bg=PANEL)
        fr.pack(fill="x", padx=px(10), pady=px(3))
        for i, k in enumerate(["pamp", "att", "agc", "nb", "nr", "anf"]):
            fr.columnconfigure(i, weight=1, uniform="fr")
            self.toggle_button(fr, k).grid(row=0, column=i, padx=px(2), sticky="ew")

        self.caption(tab, "Transmit").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        ft = tk.Frame(tab, bg=PANEL)
        ft.pack(fill="x", padx=px(10), pady=px(3))
        for i, k in enumerate(["comp", "vox", "mon", "bkin", "data", "lock"]):
            ft.columnconfigure(i, weight=1, uniform="ft")
            self.toggle_button(ft, k).grid(row=0, column=i, padx=px(2), sticky="ew")

        self.caption(tab, "RIT").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        rr = tk.Frame(tab, bg=PANEL)
        rr.pack(fill="x", padx=px(12), pady=px(3))
        self.toggle_button(rr, "rit", width=64).pack(side="left")
        self.btn(rr, "−50", lambda: self.nudge_rit(-50), width=46).pack(side="left", padx=(px(10), px(2)))
        self.btn(rr, "−10", lambda: self.nudge_rit(-10), width=46).pack(side="left", padx=px(2))
        self.lbl_rit = tk.Label(rr, text="+0 Hz", width=9, bg=FIELD, fg=ACCENT, font=F["mono_b"],
                                highlightthickness=1, highlightbackground=BORDER)
        self.lbl_rit.pack(side="left", padx=px(4), ipady=px(3))
        self.lbl_rit.bind("<MouseWheel>", lambda e: self.nudge_rit(10 if e.delta > 0 else -10))
        self.lbl_rit.bind("<Button-4>", lambda e: self.nudge_rit(10))
        self.lbl_rit.bind("<Button-5>", lambda e: self.nudge_rit(-10))
        self.btn(rr, "+10", lambda: self.nudge_rit(10), width=46).pack(side="left", padx=px(2))
        self.btn(rr, "+50", lambda: self.nudge_rit(50), width=46).pack(side="left", padx=px(2))
        self.btn(rr, "CLEAR", lambda: self.set_rit(0), width=56, tone="amber").pack(side="left", padx=px(8))

        self.caption(tab, "Other").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        orow = tk.Frame(tab, bg=PANEL)
        orow.pack(fill="x", padx=px(12), pady=px(3))
        self.btn(orow, "Voice: freq + mode", lambda: self.cmd_status(0x13, 0x00, None, "VOICE ANNOUNCE"),
                 width=130).pack(side="left")
        self.btn(orow, "Voice: S-meter", lambda: self.cmd_status(0x13, 0x01, None, "VOICE S-METER"),
                 width=110).pack(side="left", padx=px(6))
        self.btn(orow, "Re-read radio", self.request_full_sync, width=100).pack(side="right")

    # ------------------------------------------------------------ cw tab
    def build_cw_tab(self, tab):
        self.caption(tab, "Send CW (rig must be in CW mode)").pack(anchor="w", padx=px(12), pady=(px(8), 0))
        row = tk.Frame(tab, bg=PANEL)
        row.pack(fill="x", padx=px(12), pady=px(3))
        self.cw_entry = self.entry(row, width=30)
        self.cw_entry.config(font=F["mono_b"])
        self.cw_entry.pack(side="left", fill="x", expand=True, ipady=px(3))
        self.cw_entry.bind("<Return>", lambda e: self.send_cw(self.cw_entry.get(), clear=True))
        self.btn(row, "SEND", lambda: self.send_cw(self.cw_entry.get(), clear=True), width=60,
                 tone="green").pack(side="left", padx=(px(6), px(2)))
        self.btn(row, "STOP", self.stop_cw, width=60, tone="red").pack(side="left", padx=px(2))

        self.caption(tab, "Macros  ·  {MYCALL}  {CALL} = Log tab callsign").pack(anchor="w", padx=px(12),
                                                                              pady=(px(8), 0))
        mg = tk.Frame(tab, bg=PANEL)
        mg.pack(fill="x", padx=px(12), pady=px(2))
        mg.columnconfigure(1, weight=1)
        mg.columnconfigure(3, weight=1)
        self.macro_entries = []
        for i, text in enumerate(self.config["cw_macros"]):
            r, c = i % 3, (i // 3) * 2
            b = self.btn(mg, f"M{i + 1}", lambda n=i: self.send_macro(n), width=40)
            b.grid(row=r, column=c, padx=(0 if c == 0 else px(10), px(4)), pady=px(2))
            e = self.entry(mg, width=18)
            e.insert(0, text)
            e.grid(row=r, column=c + 1, sticky="ew", ipady=px(2))
            e.bind("<FocusOut>", lambda ev: self.save_macros())
            self.macro_entries.append(e)
        dr = tk.Frame(tab, bg=PANEL)
        dr.pack(fill="x", padx=px(12), pady=(px(6), px(2)))
        self.lbl(dr, "Decode CW from the radio's receive audio", fg=MUTED, font=F["small"]).pack(side="left")
        self.btn(dr, "CW DECODER", self.open_cw_decoder, width=96, tone="green").pack(side="right")
        self.lbl(tab, "Set key speed and pitch on the LEVELS tab, BK-IN on the FUNC tab.",
                 fg=DIM, font=F["small"]).pack(side="bottom", pady=(0, px(6)))

    # ------------------------------------------------------- CW decoder window
    def open_cw_decoder(self):
        if self.cwd_win is not None and self.cwd_win.winfo_exists():
            self.cwd_win.deiconify()
            self.cwd_win.lift()
            return
        win = tk.Toplevel(self.root)
        self.cwd_win = win
        win.title("CW Decoder - IC9700 Monitor")
        win.configure(bg=PANEL)
        win.geometry(self.config.get("cwd_geom") or f"{px(560)}x{px(250)}")
        win.minsize(px(380), px(160))
        if self.config.get("topmost"):
            win.attributes("-topmost", True)
        top = tk.Frame(win, bg=PANEL)
        top.pack(fill="x", padx=px(10), pady=(px(8), px(4)))
        self.cwd_onbtn = self.btn(top, "ON", self.cwd_toggle, width=52, tone="green")
        self.cwd_onbtn.pack(side="left")
        self.cwd_led = tk.Canvas(top, width=px(16), height=px(16), bg=PANEL, highlightthickness=0)
        self.cwd_led.pack(side="left", padx=(px(10), px(4)))
        self.cwd_led.create_oval(px(2), px(2), px(14), px(14), fill=FIELD, outline=BORDER, tags="led")
        self.cwd_bar = tk.Canvas(top, width=px(90), height=px(8), bg=FIELD, highlightthickness=0)
        self.cwd_bar.pack(side="left", padx=px(4))
        self.cwd_bar.create_rectangle(0, 0, 0, px(8), fill=ACCENT, width=0, tags="bar")
        self.cwd_info = self.lbl(top, "", fg=MUTED, font=F["mono_b"], width=17, anchor="w")
        self.cwd_info.pack(side="left", padx=(px(8), 0))
        self.btn(top, "CLEAR", self.cwd_clear, width=56).pack(side="right")
        row2 = tk.Frame(win, bg=PANEL)
        row2.pack(fill="x", padx=px(10), pady=(0, px(5)))
        self.lbl(row2, "Tone", fg=MUTED, font=F["small"]).pack(side="left")
        self.cwd_tone_var = tk.StringVar(value=self.cwdec.tone_mode)
        cb = ttk.Combobox(row2, textvariable=self.cwd_tone_var, values=["Auto", "Rig pitch"], width=9,
                          state="readonly")
        cb.pack(side="left", padx=(px(4), px(14)))
        cb.bind("<<ComboboxSelected>>", lambda e: self.cwd_set_tone())
        self.lbl(row2, "Sensitivity", fg=MUTED, font=F["small"]).pack(side="left")
        self.cwd_sens_var = tk.StringVar(value=self.cwdec.sens)
        cs = ttk.Combobox(row2, textvariable=self.cwd_sens_var, values=CWD_SENS_NAMES, width=8,
                          state="readonly")
        cs.pack(side="left", padx=px(4))
        cs.bind("<<ComboboxSelected>>", lambda e: self.cwd_set_sens(self.cwd_sens_var.get()))
        self.cwd_sens_note = self.lbl(row2, "", fg=MUTED, font=F["small"], anchor="w")
        self.cwd_sens_note.pack(side="left", padx=px(8), fill="x", expand=True)
        body = tk.Frame(win, bg=LCD_BG, highlightthickness=1, highlightbackground=BORDER)
        body.pack(fill="both", expand=True, padx=px(10))
        sb = ttk.Scrollbar(body, orient="vertical")
        txt = tk.Text(body, bg=LCD_BG, fg=LCD_TEXT, font=F["cw"], wrap="word", relief="flat", bd=0,
                      padx=px(8), pady=px(6), insertwidth=0, yscrollcommand=sb.set, cursor="arrow")
        sb.config(command=txt.yview)
        sb.pack(side="right", fill="y")
        txt.pack(side="left", fill="both", expand=True)
        txt.insert("end", self.cwdec.text)
        txt.see("end")
        txt.bind("<Key>", lambda e: None if (e.state & 4 and e.keysym.lower() in ("c", "a")) else "break")
        self.cwd_text = txt
        self.cwd_status = self.lbl(win, "", fg=MUTED, font=F["small"], anchor="w")
        self.cwd_status.pack(fill="x", padx=px(10), pady=(px(3), px(6)))
        win.protocol("WM_DELETE_WINDOW", self.close_cw_decoder)
        self.cwdec.on_text = self.cwd_append
        if not self.cwdec.active:
            self.cwdec.start()
        self.cwd_tick()

    def close_cw_decoder(self):
        win = self.cwd_win
        if win is not None and win.winfo_exists():
            self.config["cwd_geom"] = win.geometry()
            win.destroy()
        self.cwd_win = None
        self.cwdec.stop()

    def cwd_toggle(self):
        if self.cwdec.active:
            self.cwdec.stop()
        else:
            self.cwdec.start()
        self.cwd_tick(once=True)

    def cwd_set_tone(self):
        mode = self.cwd_tone_var.get()
        self.cwdec.tone_mode = mode
        self.config["cwd_tone"] = mode

    def cwd_set_sens(self, name):
        if name not in CWD_SENS_NAMES:
            return
        self.cwdec.sens = name
        self.config["cwd_sens"] = name
        if self.cwd_win is not None and self.cwd_win.winfo_exists():
            self.cwd_sens_var.set(name)

    def cwd_sens_text(self):
        """A few words on what the sensitivity setting is doing."""
        d = self.cwdec
        if d.sens == "Auto":
            return "backed off: static / noise" if d.backoff else "most sensitive, follows the speed"
        return {"Low": "strong signals only", "Normal": "clean signals",
                "High": "weak signals", "Max": "weakest signals; more noise errors"}.get(d.sens, "")

    def cwd_clear(self):
        self.cwdec.clear()
        if self.cwd_win is not None and self.cwd_win.winfo_exists():
            self.cwd_text.delete("1.0", "end")

    def cwd_append(self, ch):
        if self.cwd_win is None or not self.cwd_win.winfo_exists():
            return
        t = self.cwd_text
        at_end = t.yview()[1] > 0.98
        t.insert("end", ch)
        if float(t.index("end-1c").split(".")[0]) > 400:
            t.delete("1.0", "100.0")
        if at_end:
            t.see("end")

    def cwd_tick(self, once=False):
        win = self.cwd_win
        if win is None or not win.winfo_exists():
            return
        d = self.cwdec
        on = d.active
        self.cwd_onbtn.set_active(on, "ON" if on else "OFF", tone="green" if on else "red")
        sig = on and d.snr_ok
        self.cwd_led.itemconfig("led", fill=(GREEN if d.key else ACCENT_DIM) if sig else FIELD)
        w = int(px(90) * (d.level if sig else 0))
        self.cwd_bar.coords("bar", 0, 0, w, px(8))
        self.cwd_info.config(text=f"{d.tone} Hz  {d.wpm()} WPM" if sig else ("waiting for CW" if on else ""))
        if not on:
            st = d.error or "Decoder off"
        elif self.audio is not None and self.audio.in_stream is not None:
            st = f"Listening to {self.audio.in_name}"
            if self.audio.squelched():
                st += " \u00b7 muted: rig squelch is closed"
        else:
            st = (self.audio.error if self.audio is not None else "") or "Opening the radio's audio..."
        self.cwd_status.config(text=st, fg=RED if (not on and d.error) else MUTED)
        self.cwd_sens_note.config(text=self.cwd_sens_text())
        if not once:
            self.root.after(100, self.cwd_tick)


    def save_macros(self):
        self.config["cw_macros"] = [e.get() for e in self.macro_entries]

    def send_macro(self, n):
        self.save_macros()
        call = self.qso_call.get().strip().upper() if hasattr(self, "qso_call") else ""
        self.send_cw(expand_macro(self.config["cw_macros"][n], self.config.get("mycall", ""), call))

    def send_cw(self, text, clear=False):
        if not self.running:
            return
        txt = cw_clean(text).strip()
        if not txt:
            return
        if clear:
            self.cw_entry.delete(0, tk.END)
        chunks = [txt[i:i + 30] for i in range(0, len(txt), 30)]

        def job():
            for ch in chunks:
                f = self.send_cmd(0x17, None, list(ch.encode("ascii")))
                if f is not None and f[4] == NAK:
                    self.ui(self.flash_status, "CW REJECTED - IS THE RIG IN CW MODE?", RED)
                    return
            self.ui(self.flash_status, f"CW: {txt}", ACCENT)
        self.post(job)

    def stop_cw(self):
        self.post(lambda: self.send_cmd(0x17, 0xFF))

    # ------------------------------------------------------- memory tab
    def build_memory_tab(self, tab):
        cols = ("ch", "name", "mhz", "mode", "info")
        box = tk.Frame(tab, bg=FIELD, highlightthickness=1, highlightbackground=BORDER,
                       width=px(300), height=px(130))
        box.pack_propagate(False)          # the list's stretched columns must not set the window width
        box.pack(fill="both", expand=True, padx=px(10), pady=(px(10), px(4)))
        self.mem_tree = ttk.Treeview(box, columns=cols, show="headings", height=5, selectmode="browse")
        for c, text, w in (("ch", "CH", 64), ("name", "NAME", 130), ("mhz", "MHZ", 90), ("mode", "MODE", 50),
                           ("info", "DUP / TONE", 120)):
            self.mem_tree.heading(c, text=text, anchor="w")
            self.mem_tree.column(c, width=px(w), anchor="w")
        sb = ttk.Scrollbar(box, orient="vertical", command=self.mem_tree.yview)
        self.mem_tree.configure(yscrollcommand=sb.set)
        self.mem_tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        self.mem_tree.bind("<Double-1>", lambda e: self.recall_memory())

        row = tk.Frame(tab, bg=PANEL)
        row.pack(fill="x", padx=px(10), pady=px(3))
        self.lbl(row, "Name").pack(side="left")
        self.mem_name = self.entry(row, width=14)
        self.mem_name.pack(side="left", padx=px(6), ipady=px(2))
        self.mem_name.bind("<Return>", lambda e: self.add_memory())
        self.btn(row, "Save current", self.add_memory, width=92, tone="green").pack(side="left", padx=px(2))
        self.btn(row, "Overwrite", self.update_memory, width=74).pack(side="left", padx=px(2))
        self.btn(row, "Read from radio", self.open_memread, width=118, tone="accent").pack(side="right", padx=px(2))
        row2 = tk.Frame(tab, bg=PANEL)
        row2.pack(fill="x", padx=px(10), pady=(px(2), px(8)))
        self.btn(row2, "Recall", self.recall_memory, width=70).pack(side="left", padx=px(2))
        self.btn(row2, "Delete", self.delete_memory, width=70, tone="red").pack(side="left", padx=px(2))
        self.btn(row2, "Export CSV", self.export_memories, width=86).pack(side="right", padx=px(2))
        self.btn(row2, "Import CSV", self.import_memories, width=86).pack(side="right", padx=px(2))
        self.refresh_mem_tree()

    def refresh_mem_tree(self):
        self.web_mem_dirty = True
        self.web_mem_rev += 1
        self.mem_tree.delete(*self.mem_tree.get_children())
        for i, m in enumerate(self.config["memories"]):
            self.mem_tree.insert("", "end", iid=str(i), values=(
                m.get("ch", ""), m["name"], hz_to_mhz(m["hz"]), m.get("mode") or "", mem_info(m)))

    # ---- read memories from the radio (CI-V 1A 00)
    def open_memread(self):
        if self.memread_win is not None and self.memread_win.winfo_exists():
            self.memread_win.lift()
            return
        win = tk.Toplevel(self.root)
        self.memread_win = win
        win.title("Read memories from radio")
        win.configure(bg=PANEL)
        win.resizable(False, False)
        win.transient(self.root)

        self.caption(win, "Bands").grid(row=0, column=0, sticky="w", padx=px(14), pady=(px(12), px(2)))
        bf = tk.Frame(win, bg=PANEL)
        bf.grid(row=1, column=0, columnspan=2, sticky="w", padx=px(10))
        self.mr_bands = {}
        for name, _ in MEM_BANDS:
            v = tk.BooleanVar(value=True)
            self.check(bf, name, v).pack(side="left", padx=px(4))
            self.mr_bands[name] = v

        self.caption(win, "Channels").grid(row=2, column=0, sticky="w", padx=px(14), pady=(px(10), px(2)))
        cf = tk.Frame(win, bg=PANEL)
        cf.grid(row=3, column=0, columnspan=2, sticky="w", padx=px(14))
        self.mr_from = self.spin(cf, 1, 109, 1, 1, width=4)
        self.mr_from.pack(side="left")
        self.lbl(cf, "to", fg=MUTED).pack(side="left", padx=px(6))
        self.mr_to = self.spin(cf, 1, 109, 1, 99, width=4)
        self.mr_to.pack(side="left")
        self.lbl(cf, "(1-99 = memories, 100+ = scan edges)", fg=DIM, font=F["small"]).pack(side="left", padx=px(8))

        self.mr_replace = tk.BooleanVar(value=True)
        self.check(win, "Replace channels read from the radio last time", self.mr_replace).grid(
            row=4, column=0, columnspan=2, sticky="w", padx=px(10), pady=(px(10), 0))

        self.mr_bar = tk.Canvas(win, width=px(360), height=px(14), bg=FIELD, highlightthickness=1,
                                highlightbackground=BORDER)
        self.mr_bar.grid(row=5, column=0, columnspan=2, padx=px(14), pady=(px(12), px(4)), sticky="ew")
        self.mr_label = tk.Label(win, text="Ready. The display keeps updating while reading.", bg=PANEL,
                                 fg=MUTED, font=F["small"], anchor="w")
        self.mr_label.grid(row=6, column=0, columnspan=2, sticky="w", padx=px(14))

        bt = tk.Frame(win, bg=PANEL)
        bt.grid(row=7, column=0, columnspan=2, pady=(px(10), px(14)))
        self.mr_start = self.btn(bt, "Start", self.start_memread, width=90, tone="green")
        self.mr_start.pack(side="left", padx=px(4))
        self.btn(bt, "Stop", self.cancel_memread, width=80, tone="red").pack(side="left", padx=px(4))
        self.btn(bt, "Close", win.destroy, width=80).pack(side="left", padx=px(4))
        self.memread_progress(0, 1, 0)
        win.update_idletasks()
        x = self.root.winfo_rootx() + (self.root.winfo_width() - win.winfo_width()) // 2
        win.geometry(f"+{max(x, 0)}+{self.root.winfo_rooty() + px(120)}")

    def start_memread(self):
        if not self.running:
            messagebox.showinfo("Memories", "Connect to the radio first.", parent=self.memread_win)
            return
        if self.memread is not None:
            return
        try:
            lo, hi = int(self.mr_from.get()), int(self.mr_to.get())
        except ValueError:
            lo, hi = 1, 99
        lo, hi = max(1, min(lo, hi)), min(109, max(lo, hi))
        todo = deque((name, code, ch) for name, code in MEM_BANDS if self.mr_bands[name].get()
                     for ch in range(lo, hi + 1))
        if not todo:
            self.mr_label.config(text="Choose at least one band.", fg=AMBER)
            return
        if self.scan:
            self.stop_scan()
        self.memread = {"todo": todo, "total": len(todo), "done": 0, "found": [], "fmt": "band",
                        "nak": 0, "noreply": 0, "cancel": False, "replace": self.mr_replace.get(), "error": ""}
        self.mr_start.set_active(True, "Reading ...")
        self.mr_label.config(text="Reading ...", fg=MUTED)

    def cancel_memread(self):
        if self.memread is not None:
            self.memread["cancel"] = True

    def memread_step(self):            # polling thread
        mr = self.memread
        if mr is None:
            return
        for _ in range(4):
            if mr["cancel"] or not mr["todo"]:
                break
            band, code, ch = mr["todo"][0]
            payload = ([code] if mr["fmt"] == "band" else []) + [int(f"{ch // 100:02d}", 16),
                                                                 int(f"{ch % 100:02d}", 16)]
            f = self.send_cmd(0x1A, 0x00, payload)
            if f is None:
                mr["noreply"] += 1
                if mr["noreply"] >= 5 and not mr["found"]:
                    mr["error"] = "no reply from the rig"
                    mr["cancel"] = True
                    break
            elif f[4] == NAK:
                if mr["done"] == 0 and mr["fmt"] == "band":
                    mr["fmt"] = "noband"            # retry the first channel without the band byte
                    continue
                mr["nak"] += 1
            else:
                r = parse_memory_frame(f, band)
                if isinstance(r, dict):
                    r["ch"] = f"{band} {ch:02d}"
                    mr["found"].append(r)
            mr["todo"].popleft()
            mr["done"] += 1
        self.ui(self.memread_progress, mr["done"], mr["total"], len(mr["found"]))
        if mr["cancel"] or not mr["todo"]:
            self.memread = None
            self.ui(self.memread_finished, False, mr)

    def memread_progress(self, done, total, found):
        win = self.memread_win
        if win is None or not win.winfo_exists():
            return
        c = self.mr_bar
        c.delete("all")
        w, h = int(c["width"]), int(c["height"])
        c.create_rectangle(0, 0, w * done / max(1, total), h, fill=ACCENT_LO, outline="")
        if done:
            self.mr_label.config(text=f"Channel {done} of {total}  ·  {found} programmed", fg=MUTED)

    def memread_finished(self, aborted=False, mr=None):
        win_ok = self.memread_win is not None and self.memread_win.winfo_exists()
        if mr is None:                      # disconnected while reading
            if win_ok and aborted:
                self.mr_start.set_active(False, "Start")
            return
        found = mr["found"]
        if found:
            entries = []
            for r in found:
                e = {"name": r["name"] or r["ch"], "hz": r["hz"], "mode": r["mode"], "src": "radio"}
                for k in ("ch", "dup", "tone_mode", "tone", "tsql", "offset"):
                    if r.get(k) is not None:
                        e[k] = r[k]
                entries.append(e)
            mems = self.config["memories"]
            if mr["replace"]:
                mems[:] = [m for m in mems if m.get("src") != "radio"]
            mems.extend(entries)
            save_config(self.config)
            self.refresh_mem_tree()
        if mr["error"]:
            msg, col = f"Stopped: {mr['error']}.", RED
        elif not found and mr["nak"] >= mr["done"] > 0:
            msg, col = "The rig rejected every request (1A 00). Check the CI-V address.", RED
        else:
            msg = f"Done: {len(found)} programmed channel(s) imported from {mr['done']} read."
            if mr["cancel"]:
                msg = f"Stopped: {len(found)} channel(s) imported from {mr['done']} read."
            col = GREEN
        if win_ok:
            self.mr_label.config(text=msg, fg=col)
            self.mr_start.set_active(False, "Start")
        self.flash_status(msg.upper(), col, 5)

    def add_memory(self):
        if self.cur_hz is None:
            messagebox.showinfo("Memories", "No frequency yet - connect to the radio first.")
            return
        name = self.mem_name.get().strip() or hz_to_mhz(self.cur_hz)
        self.config["memories"].append({"name": name, "hz": int(self.cur_hz), "mode": self.cur_mode})
        save_config(self.config)
        self.mem_name.delete(0, tk.END)
        self.refresh_mem_tree()

    def update_memory(self):
        i, m = self.selected_memory()
        if m is None or self.cur_hz is None:
            return
        m["hz"], m["mode"] = int(self.cur_hz), self.cur_mode
        if self.mem_name.get().strip():
            m["name"] = self.mem_name.get().strip()
            self.mem_name.delete(0, tk.END)
        save_config(self.config)
        self.refresh_mem_tree()

    def selected_memory(self):
        sel = self.mem_tree.selection()
        if not sel:
            return None, None
        i = int(sel[0])
        return i, self.config["memories"][i]

    def recall_memory(self):
        i, m = self.selected_memory()
        if m is not None:
            self.recall_mem(m)

    def recall_mem(self, m):
        self.request_frequency(m["hz"])
        if m.get("mode") in MODE_REVERSE:
            self.set_radio_mode(m["mode"])
        # Channels read from the radio carry duplex / tone settings: apply them too
        if m.get("dup") in (0, 1, 2):
            self.set_duplex({0: 0x10, 1: 0x11, 2: 0x12}[m["dup"]])
        if m.get("tone_mode") in (0, 1, 2):
            self.set_toggle_value("tone", 1 if m["tone_mode"] == 1 else 0)
            self.set_toggle_value("tsql", 1 if m["tone_mode"] == 2 else 0)
        if m.get("tone"):
            self.set_tone(0x00, f"{m['tone']:.1f}")
        if m.get("tsql"):
            self.set_tone(0x01, f"{m['tsql']:.1f}")

    def delete_memory(self):
        i, m = self.selected_memory()
        if m is None:
            return
        del self.config["memories"][i]
        save_config(self.config)
        self.refresh_mem_tree()

    def export_memories(self):
        if not self.config["memories"]:
            messagebox.showinfo("Memories", "No memories to export.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile="ic9700_memories.csv",
                                            filetypes=[("CSV", "*.csv"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["name", "freq_mhz", "mode"])
                for m in self.config["memories"]:
                    w.writerow([m["name"], f"{m['hz'] / 1e6:.6f}", m.get("mode") or ""])
        except Exception as e:
            messagebox.showerror("Memories", f"Could not write file:\n{e}")

    def import_memories(self):
        path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv"), ("All files", "*.*")])
        if not path:
            return
        added = 0
        try:
            with open(path, newline="", encoding="utf-8-sig") as f:
                for row in csv.DictReader(f):
                    try:
                        hz = int(round(float(str(row.get("freq_mhz", "")).replace(",", ".")) * 1e6))
                        mode = (row.get("mode") or "").strip().upper() or None
                        self.config["memories"].append({
                            "name": (row.get("name") or hz_to_mhz(hz)).strip(), "hz": hz,
                            "mode": mode if mode in MODE_REVERSE else None})
                        added += 1
                    except (ValueError, TypeError):
                        pass
        except Exception as e:
            messagebox.showerror("Memories", f"Could not read file:\n{e}")
            return
        save_config(self.config)
        self.refresh_mem_tree()
        messagebox.showinfo("Memories", f"Imported {added} channel(s).\n(CSV columns: name, freq_mhz, mode)")

    # --------------------------------------------------------- scan tab
    def build_scan_tab(self, tab):
        self.scan_src = tk.StringVar(value="range")
        top = tk.Frame(tab, bg=PANEL)
        top.pack(fill="x", padx=px(10), pady=(px(8), px(2)))
        for text, val in (("Range", "range"), ("Memories", "mem")):
            tk.Radiobutton(top, text=text, variable=self.scan_src, value=val, bg=PANEL, fg=TEXT,
                           selectcolor=FIELD, activebackground=PANEL, activeforeground=TEXT,
                           font=F["ui"], highlightthickness=0).pack(side="left", padx=(0, px(6)))
        self.scan_from = self.entry(top, width=9)
        self.scan_from.pack(side="left", padx=(px(6), px(2)), ipady=px(2))
        self.scan_from.insert(0, "145.000")
        self.lbl(top, "–", fg=MUTED).pack(side="left")
        self.scan_to = self.entry(top, width=9)
        self.scan_to.pack(side="left", padx=px(2), ipady=px(2))
        self.scan_to.insert(0, "146.000")
        self.lbl(top, "MHz", fg=MUTED).pack(side="left", padx=px(2))
        self.scan_step_var = tk.StringVar(value="12.5 kHz")
        ttk.Combobox(top, textvariable=self.scan_step_var, state="readonly", width=8,
                     values=[s[0] for s in STEPS], font=F["ui"]).pack(side="left", padx=px(4))

        opt = tk.Frame(tab, bg=PANEL)
        opt.pack(fill="x", padx=px(10), pady=px(2))
        self.lbl(opt, "Dwell ms").pack(side="left")
        self.scan_dwell = self.spin(opt, 300, 3000, 50, 400)
        self.scan_dwell.pack(side="left", padx=px(4))
        self.lbl(opt, "Hold s").pack(side="left", padx=(px(6), 0))
        self.scan_hold = self.spin(opt, 1, 30, 1, 3, width=3)
        self.scan_hold.pack(side="left", padx=px(4))
        self.scan_sql = tk.BooleanVar(value=True)
        self.scan_use_s = tk.BooleanVar(value=False)
        self.check(opt, "Squelch", self.scan_sql).pack(side="left", padx=(px(8), 0))
        self.check(opt, "S ≥", self.scan_use_s).pack(side="left", padx=(px(4), 0))
        self.scan_s = self.spin(opt, 1, 9, 1, 3, width=2)
        self.scan_s.pack(side="left", padx=px(2))

        self.sweep_canvas = tk.Canvas(tab, height=px(92), bg=FIELD, highlightthickness=1,
                                      highlightbackground=BORDER, cursor="crosshair")
        self.sweep_canvas.pack(fill="both", expand=True, padx=px(10), pady=px(4))
        self.sweep_canvas.bind("<Configure>", lambda e: self.draw_sweep())
        self.sweep_canvas.bind("<Button-1>", self.sweep_click)

        brow = tk.Frame(tab, bg=PANEL)
        brow.pack(fill="x", padx=px(10), pady=(0, px(8)))
        self.btn_scan = RoundButton(brow, "START SCAN", self.toggle_scan, width=120, height=28, tone="amber",
                                    solid=True, font=F["ui_b"])
        self.btn_scan.pack(side="left")
        self.btn(brow, "Clear plot", self.clear_sweep, width=80).pack(side="left", padx=px(6))
        self.lbl(brow, "Click the plot to tune  ·  manual tuning stops the scan",
                 fg=DIM, font=F["small"]).pack(side="right")

    def toggle_scan(self):
        if self.scan:
            self.stop_scan()
        else:
            self.start_scan()

    def start_scan(self):
        if not self.running:
            messagebox.showinfo("Scan", "Connect to the radio first.")
            return
        try:
            if self.scan_src.get() == "mem":
                items = [(m["hz"], m.get("mode")) for m in self.config["memories"]]
                if not items:
                    messagebox.showinfo("Scan", "No memory channels saved yet (see the MEMORY tab).")
                    return
            else:
                lo = int(round(float(self.scan_from.get().replace(",", ".")) * 1_000_000))
                hi = int(round(float(self.scan_to.get().replace(",", ".")) * 1_000_000))
                step = dict(STEPS)[self.scan_step_var.get()]
                if hi <= lo:
                    raise ValueError("'To' must be higher than 'From'.")
                if (hi - lo) // step > 5000:
                    raise ValueError("Range has too many steps - use a larger step.")
                items = [(f, None) for f in range(lo, hi + 1, step)]
            dwell = max(MIN_DWELL, int(self.scan_dwell.get()) / 1000)
            hold = max(1, int(self.scan_hold.get()))
            s_thr = int(int(self.scan_s.get()) * 120 / 9)
        except (ValueError, KeyError) as e:
            messagebox.showerror("Scan", str(e) if str(e) and "invalid literal" not in str(e)
                                 and "could not convert" not in str(e) else "Check the scan settings.")
            return
        if not (self.scan_sql.get() or self.scan_use_s.get()):
            messagebox.showinfo("Scan", "Choose a stop condition (squelch and/or S-meter).")
            return
        if not (self.sweep and self.sweep["items"] == items):
            self.sweep = {"items": items, "levels": [None] * len(items), "idx": -1}
        self.scan = {"items": items, "idx": -1, "hold_until": 0.0, "last_move": 0.0, "dwell": dwell,
                     "hold": hold, "use_sql": self.scan_sql.get(), "use_s": self.scan_use_s.get(),
                     "s_thresh": s_thr, "levels": self.sweep["levels"], "sweep": self.sweep}
        self.btn_scan.set_active(True, "STOP SCAN")
        self.set_scan_badge("scan")
        self.draw_sweep()

    def stop_scan(self):
        self.scan = None
        self.btn_scan.set_active(False, "START SCAN")
        self.set_scan_badge(None)
        self.draw_sweep()

    def set_scan_badge(self, state):
        if state == "scan":
            self.chip_scan.set_active(True, "SCAN", tone="amber")
        elif state == "hold":
            self.chip_scan.set_active(True, "HOLD", tone="green")
        else:
            self.chip_scan.set_active(False, "SCAN")

    def clear_sweep(self):
        if self.sweep:
            self.sweep["levels"][:] = [None] * len(self.sweep["levels"])
        self.draw_sweep()

    def draw_sweep(self):
        c = self.sweep_canvas
        c.delete("all")
        w, h = c.winfo_width(), c.winfo_height()
        if w < 20:
            return
        pad, top, bot = px(8), px(8), h - px(16)
        sw = self.sweep
        # S9 guide line
        y9 = bot - (S9_RAW / METER_MAX) * (bot - top)
        c.create_line(pad, y9, w - pad, y9, fill=BORDER, dash=(2, 3))
        c.create_text(w - pad, y9 - 1, text="S9", anchor="se", fill=DIM, font=F["small_b"])
        c.create_line(pad, bot, w - pad, bot, fill=BORDER)
        if not sw:
            c.create_text(w / 2, (top + bot) / 2, text="Band activity appears here while scanning",
                          fill=DIM, font=F["small"])
            return
        items, levels = sw["items"], sw["levels"]
        n = len(items)
        span = w - 2 * pad
        cols = max(1, min(n, int(span)))
        colw = span / cols
        for col in range(cols):
            i0 = col * n // cols
            i1 = max(i0 + 1, (col + 1) * n // cols)
            vals = [v for v in levels[i0:i1] if v is not None]
            if not vals:
                continue
            v = max(vals)
            x = pad + (col + 0.5) * colw
            bh = max(1, (min(v, METER_MAX) / METER_MAX) * (bot - top))
            color = lerp_color(ACCENT_LO, ACCENT, v / S9_RAW) if v <= S9_RAW else lerp_color(AMBER, RED, (v - S9_RAW) / 121)
            c.create_line(x, bot, x, bot - bh, fill=color, width=max(1, colw - (1 if colw > 3 else 0)))
        if self.scan and 0 <= self.scan["idx"] < n:
            x = pad + (self.scan["idx"] + 0.5) / n * span
            c.create_line(x, top, x, bot, fill=AMBER)
        c.create_text(pad, h - px(2), text=hz_to_mhz(items[0][0]), anchor="sw", fill=MUTED, font=F["small_b"])
        c.create_text(w - pad, h - px(2), text=hz_to_mhz(items[-1][0]), anchor="se", fill=MUTED, font=F["small_b"])
        self.sweep_geom = (pad, span, n)

    def sweep_click(self, e):
        if not self.sweep or not hasattr(self, "sweep_geom"):
            return
        pad, span, n = self.sweep_geom
        idx = int((e.x - pad) / span * n)
        if 0 <= idx < n:
            hz, mode = self.sweep["items"][idx]
            self.request_frequency(hz)
            if mode in MODE_REVERSE:
                self.set_radio_mode(mode)

    # ---------------------------------------------------------- log tab
    def build_log_tab(self, tab):
        form = tk.Frame(tab, bg=PANEL)
        form.pack(fill="x", padx=px(10), pady=(px(8), px(2)))
        self.lbl(form, "Call", fg=MUTED, font=F["small"]).grid(row=0, column=0, sticky="w")
        self.qso_call = self.entry(form, width=11)
        self.qso_call.config(font=F["mono_b"])
        self.qso_call.grid(row=1, column=0, padx=(0, px(4)), ipady=px(2))
        self.qso_call.bind("<KeyRelease>", lambda e: self.check_dupe())
        self.lbl(form, "RST S / R", fg=MUTED, font=F["small"]).grid(row=0, column=1, columnspan=2, sticky="w")
        self.qso_rs = self.entry(form, width=4)
        self.qso_rs.grid(row=1, column=1, padx=(0, px(2)), ipady=px(2))
        self.qso_rs.insert(0, "59")
        self.qso_rr = self.entry(form, width=4)
        self.qso_rr.grid(row=1, column=2, padx=(0, px(4)), ipady=px(2))
        self.qso_rr.insert(0, "59")
        self.lbl(form, "Name", fg=MUTED, font=F["small"]).grid(row=0, column=3, sticky="w")
        self.qso_name = self.entry(form, width=10)
        self.qso_name.grid(row=1, column=3, padx=(0, px(4)), ipady=px(2))
        self.lbl(form, "Grid", fg=MUTED, font=F["small"]).grid(row=0, column=4, sticky="w")
        self.qso_grid = self.entry(form, width=7)
        self.qso_grid.grid(row=1, column=4, padx=(0, px(4)), ipady=px(2))
        self.lbl(form, "Notes", fg=MUTED, font=F["small"]).grid(row=0, column=5, sticky="w")
        self.qso_notes = self.entry(form, width=12)
        self.qso_notes.grid(row=1, column=5, sticky="ew", ipady=px(2))
        form.columnconfigure(5, weight=1)
        for e in (self.qso_call, self.qso_rs, self.qso_rr, self.qso_name, self.qso_grid, self.qso_notes):
            e.bind("<Return>", lambda ev: self.add_qso())

        r2 = tk.Frame(tab, bg=PANEL)
        r2.pack(fill="x", padx=px(10), pady=px(3))
        self.btn(r2, "LOG QSO", self.add_qso, width=90, tone="green").pack(side="left")
        self.lbl_dupe = tk.Label(r2, text="", bg=PANEL, fg=AMBER, font=F["small_b"])
        self.lbl_dupe.pack(side="left", padx=px(8))
        self.lbl_count = tk.Label(r2, text="", bg=PANEL, fg=MUTED, font=F["small_b"])
        self.lbl_count.pack(side="right")

        cols = ("utc", "call", "mhz", "mode", "rst", "name", "notes")
        box = tk.Frame(tab, bg=FIELD, highlightthickness=1, highlightbackground=BORDER,
                       width=px(300), height=px(110))
        box.pack_propagate(False)          # the list's stretched columns must not set the window width
        box.pack(fill="both", expand=True, padx=px(10), pady=px(2))
        self.qso_tree = ttk.Treeview(box, columns=cols, show="headings", height=4, selectmode="browse")
        for c, text, w in (("utc", "UTC", 104), ("call", "CALL", 72), ("mhz", "MHZ", 78), ("mode", "MODE", 46),
                           ("rst", "RST", 46), ("name", "NAME", 60), ("notes", "NOTES", 80)):
            self.qso_tree.heading(c, text=text, anchor="w")
            self.qso_tree.column(c, width=px(w), anchor="w")
        sb = ttk.Scrollbar(box, orient="vertical", command=self.qso_tree.yview)
        self.qso_tree.configure(yscrollcommand=sb.set)
        self.qso_tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        row = tk.Frame(tab, bg=PANEL)
        row.pack(fill="x", padx=px(10), pady=(px(3), px(8)))
        self.btn(row, "Delete", self.delete_qso, width=70, tone="red").pack(side="left", padx=px(2))
        self.btn(row, "Export CSV", self.export_csv, width=86).pack(side="right", padx=px(2))
        self.btn(row, "Export ADIF", self.export_adif, width=90).pack(side="right", padx=px(2))
        self.refresh_qso_tree()

    def refresh_qso_tree(self):
        self.qso_tree.delete(*self.qso_tree.get_children())
        for i, q in enumerate(self.qso_log):
            utc = f"{q['date'][:4]}-{q['date'][4:6]}-{q['date'][6:]} {q['time'][:2]}:{q['time'][2:4]}"
            self.qso_tree.insert("", 0, iid=str(i), values=(
                utc, q["call"], hz_to_mhz(q["hz"]), q.get("mode", ""),
                f"{q.get('rst_s', '')}/{q.get('rst_r', '')}", q.get("name", ""), q.get("notes", "")))
        self.lbl_count.config(text=f"{len(self.qso_log)} QSO{'s' if len(self.qso_log) != 1 else ''}")

    def check_dupe(self):
        call = self.qso_call.get().strip().upper()
        if not call:
            self.lbl_dupe.config(text="")
            return
        band = band_of(self.cur_hz) if self.cur_hz else ""
        prev = [q for q in self.qso_log if q["call"] == call]
        if not prev:
            self.lbl_dupe.config(text="NEW CALL", fg=GREEN)
        elif band and any(band_of(q["hz"]) == band for q in prev):
            last = max(prev, key=lambda q: q["date"] + q["time"])
            self.lbl_dupe.config(text=f"WORKED ON {band.upper()} · last {last['date'][:4]}-{last['date'][4:6]}-"
                                      f"{last['date'][6:]}", fg=AMBER)
        else:
            self.lbl_dupe.config(text=f"WORKED {len(prev)}x (new band)", fg=ACCENT)

    def add_qso(self):
        call = self.qso_call.get().strip().upper()
        if not call:
            messagebox.showinfo("Log", "Enter a callsign.")
            return
        if self.cur_hz is None:
            messagebox.showinfo("Log", "No frequency yet - connect to the radio first.")
            return
        now = datetime.now(timezone.utc)
        self.qso_log.append({
            "date": now.strftime("%Y%m%d"), "time": now.strftime("%H%M%S"), "call": call,
            "hz": int(self.cur_hz), "mode": self.cur_mode or "", "rst_s": self.qso_rs.get().strip(),
            "rst_r": self.qso_rr.get().strip(), "name": self.qso_name.get().strip(),
            "grid": self.qso_grid.get().strip().upper(), "notes": self.qso_notes.get().strip()})
        save_qso_log(self.qso_log)
        for e in (self.qso_call, self.qso_name, self.qso_grid, self.qso_notes):
            e.delete(0, tk.END)
        self.lbl_dupe.config(text="")
        self.refresh_qso_tree()
        self.flash_status(f"LOGGED {call}", GREEN)

    def delete_qso(self):
        sel = self.qso_tree.selection()
        if not sel:
            return
        if messagebox.askyesno("Log", "Delete the selected QSO?"):
            del self.qso_log[int(sel[0])]
            save_qso_log(self.qso_log)
            self.refresh_qso_tree()

    def export_adif(self):
        if not self.qso_log:
            messagebox.showinfo("Log", "The log is empty.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".adi", initialfile="ic9700_log.adi",
                                            filetypes=[("ADIF", "*.adi"), ("All files", "*.*")])
        if path:
            try:
                with open(path, "w", encoding="ascii", newline="\n") as f:
                    f.write(adif_document(self.qso_log, self.config.get("mycall", "")))
            except Exception as e:
                messagebox.showerror("Log", f"Could not write file:\n{e}")

    def export_csv(self):
        if not self.qso_log:
            messagebox.showinfo("Log", "The log is empty.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile="ic9700_log.csv",
                                            filetypes=[("CSV", "*.csv"), ("All files", "*.*")])
        if path:
            try:
                with open(path, "w", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    w.writerow(["date_utc", "time_utc", "call", "freq_mhz", "mode", "rst_sent", "rst_rcvd",
                                "name", "grid", "notes"])
                    for q in self.qso_log:
                        w.writerow([q["date"], q["time"], q["call"], hz_to_mhz(q["hz"]), q.get("mode", ""),
                                    q.get("rst_s", ""), q.get("rst_r", ""), q.get("name", ""),
                                    q.get("grid", ""), q.get("notes", "")])
            except Exception as e:
                messagebox.showerror("Log", f"Could not write file:\n{e}")

    # --------------------------------------------------- connection mgmt
    def set_led(self, color):
        c = self.lbl_led
        c.delete("all")
        s = px(10)
        c.create_oval(1, 1, s - 1, s - 1, fill=color, outline="")

    def set_status(self, text, color):
        self.lbl_status.config(text=text, fg=color)
        self.set_led(color)

    def flash_status(self, text, color, secs=4.0):
        """Temporary status message; reverts to the link status afterwards."""
        self.set_status(text, color)
        self.status_hold = time.time() + secs

        def back():
            if time.time() >= self.status_hold and self.running:
                self.set_link(self.link_ok)
        self.root.after(int(secs * 1000) + 50, back)

    def update_port_label(self):
        addr = f"CI-V {self.radio_addr:02X}"
        web = f" · PHONE :{self.web.port}" if self.web.running else ""
        if self.lan_open():
            web = " · SCOPE LAN" + web
        if self.running:
            self.lbl_port.config(text=f"{self.port_name} · {self.baud} · {addr}{web}")
        else:
            self.lbl_port.config(text=addr + web)

    def auto_connect(self, quiet=True):
        try:
            ports = [p.device for p in serial.tools.list_ports.comports()]
            saved = self.config.get("port", AUTO_PORT)
            sport = None
            if saved != AUTO_PORT:
                if saved in ports:
                    sport = saved
                else:
                    self.set_status(f"WAITING FOR {saved} ...", ORANGE)
                    return False
            elif "COM4" in ports:
                sport = "COM4"
            elif "COM3" in ports:
                sport = "COM3"
            elif ports:
                sport = ports[0]

            if not sport:
                self.set_status("NO TRANSCEIVER FOUND - WAITING (plug in / power on the rig)", ORANGE)
                return False
            return self.connect(sport, self.config.get("baud", 19200), quiet=quiet)
        except Exception as e:
            self.set_status("AUTO-CONNECT PORT FAULT", RED)
            if not quiet:
                messagebox.showerror("Error", f"Hardware connection initialization failed:\n{str(e)}")
            return False

    def connect(self, sport, baud=19200, quiet=False):
        self.disconnect()
        try:
            self.ser = serial.Serial(port=sport, baudrate=baud, timeout=0.3)
        except Exception as e:
            self.ser = None
            self.set_status(f"PORT FAULT ON {sport} - RETRYING", RED)
            if not quiet:
                messagebox.showerror("Error", f"Could not open {sport}:\n{str(e)}")
            return False
        self.want_connect = True
        self.io_error = False
        self.rxbuf.clear()
        self.port_name, self.baud = sport, baud
        self.full_sync = True
        self.rig_name = ""
        self.running = True
        self.link_ok = True
        self.rig_off = False
        self.set_status(f"ONLINE - RIG CONNECTED ON {sport} @ {baud}", GREEN)
        self.refresh_power()
        self.update_port_label()
        self.poll_thread = threading.Thread(target=self.poll_radio, daemon=True)
        self.poll_thread.start()
        return True

    def _raw_write(self, body):
        """Write a command straight to the port (used while stopping, after the poll thread has ended)."""
        ser = self.ser
        if not ser:
            return
        try:
            ser.write(bytes([START_BYTE, START_BYTE, self.radio_addr, CONTR_ADDR] + body + [STOP_BYTE]))
            ser.flush()
        except Exception:
            pass

    def _unkey_now(self):
        self._raw_write([0x1C, 0x00, 0x00])

    def disconnect(self, user=False, lost=False):
        if user:
            self.want_connect = False
        had = self.running or self.ser is not None
        self.running = False
        if self.poll_thread and self.poll_thread.is_alive() and self.poll_thread is not threading.current_thread():
            self.poll_thread.join(timeout=3)
        self.poll_thread = None
        if self.ptt_on or self.is_tx:
            self._unkey_now()
        if self.scope_on and self.ser:
            self._raw_write([0x27, 0x11, 0x00])     # stop the scope data stream
        self.ptt_on = False
        self.memread = None
        self.stop_lan()
        try:
            if self.ser and self.ser.is_open:
                self.ser.close()
        except Exception:
            pass
        self.ser = None
        self.io_error = False
        self.rxbuf.clear()
        while True:
            try:
                self.cmdq.get_nowait()
            except queue.Empty:
                break
        self.freq_queued = False
        self.pending_levels.clear()
        if not (had or user):
            return
        self.is_tx = False
        self.cur_hz = None
        self.cur_mode = None
        self.cur_filter = None
        self.scan = None
        self.btn_scan.set_active(False, "START SCAN")
        self.set_scan_badge(None)
        if not lost:
            self.set_status("SYSTEM OFFLINE", MUTED)
        self.update_port_label()
        self.draw_freq(force=True)
        self.chip_mode.set_active(False, "--")
        self.chip_fil.set_active(False, "FIL")
        self.chip_band.set_active(False, "BAND")
        self.chip_vd.set_active(False, "-- V")
        self.rx_busy = False
        self.meter_mode = "rx"
        self.meter_frac = 0.0
        self.peak_frac = 0.0
        self.lbl_smeter.config(text="", fg=LCD_TEXT)
        self.sub_hz = self.sub_mode = None
        self.sub_nak = 0
        self.scope_data = None
        self.scope_span = None
        self.scope_acc = None
        self.draw_sub()
        self.draw_scope()
        self.draw_status()
        self.memread_finished(aborted=True)
        self.lbl_info.config(text="")
        self.level_vals = {sub: None for _, sub, _ in LEVELS}
        self.toggle_state = {k: None for k in TOGGLES}
        for k in TOGGLES:
            self.refresh_toggle(k)
        self.dup_state = None
        self.refresh_duplex()
        self.refresh_mode_buttons()
        self.btn_ptt.set_active(False, "TRANSMIT")
        self.refresh_power()
        self.draw_levels()
        self.draw_meter()

    def user_reconnect(self):
        self.want_connect = True
        self.disconnect()
        self.auto_connect(quiet=False)

    def on_link_lost(self, thread):
        if thread is not self.poll_thread or not self.want_connect:
            return
        self.disconnect(lost=True)
        self.set_status("CONNECTION LOST - RETRYING ...", ORANGE)

    def reconnect_tick(self):
        try:
            if SERIAL_READY and self.want_connect and not self.running:
                self.auto_connect(quiet=True)
        finally:
            self.root.after(RECONNECT_MS, self.reconnect_tick)

    def on_close(self):
        self.config["geometry"] = (self.root.geometry() if self.root.state() == "normal"
                                   else (self._normal_geom or self.root.geometry()))
        self.config["step_hz"] = self.step_hz()
        self.save_macros()
        save_config(self.config)
        self.want_connect = False
        self.disconnect(user=True)
        self.stop_lan()
        self.web.stop()
        self.cwdec.stop()
        if self.audio is not None:
            self.audio.close()
        self.root.destroy()

    def request_full_sync(self):
        self.full_sync = True
        if self.running:
            self.flash_status("RE-READING RADIO STATE ...", ACCENT, 2)

    def open_settings(self):
        if not SERIAL_READY:
            messagebox.showerror("Error", "pyserial library missing!\nRun: python -m pip install pyserial")
            return

        win = tk.Toplevel(self.root)
        win.title("Settings")
        win.configure(bg=PANEL)
        win.resizable(False, False)
        win.transient(self.root)
        win.grab_set()

        def row(r, text):
            self.lbl(win, text, fg=MUTED).grid(row=r, column=0, padx=px(14), pady=px(5), sticky="w")

        row(0, "COM port")
        port_var = tk.StringVar()
        port_box = ttk.Combobox(win, textvariable=port_var, state="readonly", width=40, font=F["ui"])
        port_box.grid(row=0, column=1, padx=px(14), pady=(px(14), px(5)), sticky="w")

        row(1, "Baud rate")
        baud_var = tk.StringVar(value=str(self.config.get("baud", 19200)))
        ttk.Combobox(win, textvariable=baud_var, state="readonly", width=10, font=F["ui"],
                     values=[str(b) for b in BAUD_RATES]).grid(row=1, column=1, padx=px(14), pady=px(5), sticky="w")

        row(2, "CI-V address (hex)")
        civ_entry = self.entry(win, width=6)
        civ_entry.grid(row=2, column=1, padx=px(14), pady=px(5), sticky="w", ipady=px(2))
        civ_entry.insert(0, self.config.get("ci_v", "A2"))

        row(3, "My callsign")
        call_entry = self.entry(win, width=12)
        call_entry.grid(row=3, column=1, padx=px(14), pady=px(5), sticky="w", ipady=px(2))
        call_entry.insert(0, self.config.get("mycall", ""))

        row(4, "PTT time-out (s)")
        tot = self.spin(win, 10, 600, 10, self.config.get("tx_timeout", 180), width=6)
        tot.grid(row=4, column=1, padx=px(14), pady=px(5), sticky="w")

        self.caption(win, "Scope over the network (IC-9700 LAN port)").grid(
            row=5, column=0, columnspan=2, sticky="w", padx=px(14), pady=(px(12), 0))
        lan_var = tk.BooleanVar(value=bool(self.config.get("lan_scope")))
        self.check(win, "Get the spectrum scope over Ethernet (everything else stays on USB)", lan_var).grid(
            row=6, column=0, columnspan=2, sticky="w", padx=px(10), pady=px(2))
        row(7, "Radio IP address")
        lan_row = tk.Frame(win, bg=PANEL)
        lan_row.grid(row=7, column=1, padx=px(14), pady=px(5), sticky="w")
        lan_ip = self.entry(lan_row, width=18)
        lan_ip.pack(side="left", ipady=px(2))
        lan_ip.insert(0, self.config.get("lan_ip", ""))
        self.lbl(lan_row, "Port", fg=MUTED).pack(side="left", padx=(px(8), px(4)))
        lan_port = self.spin(lan_row, 1, 65535, 1, self.config.get("lan_port", LAN_DEFAULT_PORT), width=6)
        lan_port.pack(side="left")
        row(8, "Network user ID")
        lan_user = self.entry(win, width=18)
        lan_user.grid(row=8, column=1, padx=px(14), pady=px(5), sticky="w", ipady=px(2))
        lan_user.insert(0, self.config.get("lan_user", ""))
        row(9, "Network password")
        lan_pw = self.entry(win, width=18, show="•")
        lan_pw.grid(row=9, column=1, padx=px(14), pady=px(5), sticky="w", ipady=px(2))
        lan_pw.insert(0, self.config.get("lan_pass", ""))
        tk.Label(win, bg=PANEL, fg=DIM, font=F["small"], justify="left",
                 text="Radio: MENU > SET > Network > Network Control = ON, Network User1 ID / Password,\n"
                      "and the IP address under SET > Network (use a fixed address or a DHCP reservation).\n"
                      "Close RS-BA1 / wfview first: the radio takes one network user at a time.").grid(
            row=10, column=0, columnspan=2, sticky="w", padx=px(14), pady=(px(2), 0))

        def refresh_ports(select=None):
            entries = [AUTO_PORT]
            for p in sorted(serial.tools.list_ports.comports(), key=lambda x: x.device):
                entries.append(f"{p.device} - {p.description}")
            port_box["values"] = entries
            wanted = select or self.config.get("port", AUTO_PORT)
            choice = entries[0]
            for e in entries:
                if e.split(" - ")[0] == wanted:
                    choice = e
                    break
            port_var.set(choice)

        def apply_settings():
            port = port_var.get().split(" - ")[0]
            try:
                baud = int(baud_var.get())
            except ValueError:
                baud = 19200
            addr = parse_ci_v(civ_entry.get())
            if addr is None:
                messagebox.showerror("Error", "CI-V address must be hex between 01 and DF (IC-9700 default: A2).",
                                     parent=win)
                return
            try:
                timeout = max(10, min(600, int(tot.get())))
            except ValueError:
                timeout = 180
            try:
                lport = max(1, min(65535, int(lan_port.get())))
            except ValueError:
                lport = LAN_DEFAULT_PORT
            if lan_var.get() and not lan_ip.get().strip():
                messagebox.showerror("Error", "Enter the radio's IP address for the network scope.", parent=win)
                return
            self.config.update(port=port, baud=baud, ci_v=f"{addr:02X}",
                               mycall=call_entry.get().strip().upper(), tx_timeout=timeout,
                               lan_scope=bool(lan_var.get()), lan_ip=lan_ip.get().strip(), lan_port=lport,
                               lan_user=lan_user.get().strip(), lan_pass=lan_pw.get())
            self.stop_lan()
            self.lan_retry = 0.0
            self.radio_addr = addr
            save_config(self.config)
            win.destroy()
            self.want_connect = True
            if port == AUTO_PORT:
                self.disconnect()
                self.auto_connect(quiet=False)
            else:
                self.connect(port, baud)

        btns = tk.Frame(win, bg=PANEL)
        btns.grid(row=11, column=0, columnspan=2, pady=(px(10), px(14)))
        self.btn(btns, "Refresh", refresh_ports, width=80).pack(side="left", padx=px(4))
        self.btn(btns, "Save & connect", apply_settings, width=120, tone="green").pack(side="left", padx=px(4))
        self.btn(btns, "Cancel", win.destroy, width=80).pack(side="left", padx=px(4))

        refresh_ports()

    # ---------------------------------------------------------- CI-V I/O
    def _extract_frames(self):
        """Split complete CI-V frames (ending in 0xFD) out of the receive buffer."""
        out = []
        buf = self.rxbuf
        while True:
            i = buf.find(STOP_BYTE)
            if i < 0:
                break
            frame = bytes(buf[:i + 1])
            del buf[:i + 1]
            j = frame.find(b"\xfe\xfe")
            if j >= 0:
                out.append(list(frame[j:]))
        if len(buf) > 4096:
            buf.clear()
        return out

    def handle_frame(self, f):
        """Unsolicited frames. Spectrum scope waveform (27 00) is assembled here; others are ignored."""
        if len(f) < 10 or f[4] != 0x27 or f[5] != 0x00 or f[3] != self.radio_addr:
            return
        if f[2] not in (0x00, CONTR_ADDR) or f[6] != 0x00 or not self.scope_on:
            return                                  # main band only
        with self.scope_lock:                       # frames arrive from USB and from the network thread
            parsed = parse_scope_frame(f, self.scope_acc)
            if parsed is None:
                return
            self.scope_acc, done = parsed
            if not done:
                return
            acc, self.scope_acc = self.scope_acc, None
            now = time.time()
            gap = 0.06 if self.lan_open() else 0.12
            if self.audio is not None and self.audio.listener_count() and self.config.get("phone_priority", True):
                gap = 0.25                          # a phone is listening: its audio comes first
            if now - self.scope_last >= gap and acc.get("lo") is not None and acc["data"]:
                self.scope_last = now
                self.ui(self.scope_update, acc["lo"], acc["hi"], acc["data"], acc.get("centre", False))

    def _drain(self):
        ser = self.ser
        if not ser or not ser.is_open:
            return
        n = ser.in_waiting
        if n:
            self.rxbuf += ser.read(n)
        for f in self._extract_frames():
            self.handle_frame(f)

    def pump(self):
        try:
            with self.io_lock:
                self._drain()
        except Exception:
            self.io_error = True

    def send_cmd(self, cmd, sub_cmd=None, data=None):
        """Send one CI-V command and return the matching reply frame (list of ints) or None."""
        ser = self.ser
        if not ser or not ser.is_open:
            return None
        payload = [START_BYTE, START_BYTE, self.radio_addr, CONTR_ADDR, cmd]
        if sub_cmd is not None:
            payload.append(sub_cmd)
        if data:
            payload.extend(data)
        payload.append(STOP_BYTE)
        try:
            with self.io_lock:
                self._drain()
                ser.write(bytes(payload))
                deadline = time.time() + REPLY_TIMEOUT
                while time.time() < deadline:
                    chunk = ser.read(max(1, ser.in_waiting))
                    if chunk:
                        self.rxbuf += chunk
                    for f in self._extract_frames():
                        if len(f) < 6 or f[2] != CONTR_ADDR or f[3] != self.radio_addr:
                            self.handle_frame(f)        # broadcast / scope data; echoes are ignored
                            continue
                        code = f[4]
                        if code in (ACK, NAK):
                            return f
                        if code == cmd and (sub_cmd is None or cmd == 0x06 or len(f) <= 6 or f[5] == sub_cmd):
                            return f
                        self.handle_frame(f)
                    if not chunk:
                        return None
                return None
        except Exception:
            self.io_error = True
            return None

    def post(self, fn):
        if self.running:
            self.cmdq.put(fn)

    def post_cmd(self, cmd, sub=None, data=None):
        self.post(lambda: self.send_cmd(cmd, sub, data))

    def cmd_status(self, cmd, sub, data, want):
        """Send a command on the polling thread and report ACK / NAK in the status bar."""
        def job():
            f = self.send_cmd(cmd, sub, data)
            code = f"{cmd:02X}" + (f" {sub:02X}" if sub is not None else "")
            if f is None:
                self.ui(self.flash_status, f"{want}: NO REPLY FROM RIG", ORANGE)
            elif f[4] == NAK:
                self.ui(self.flash_status, f"RIG REJECTED {want} ({code} NAK)", RED)
            else:
                self.ui(self.flash_status, want, GREEN, 2.5)
        self.post(job)

    def run_queue(self):
        while True:
            try:
                fn = self.cmdq.get_nowait()
            except queue.Empty:
                break
            try:
                fn()
            except Exception:
                pass

    def ui(self, fn, *args):
        """Thread-safe: queue a call for the Tk main loop (never touch Tk from the polling thread)."""
        self.uiq.put((fn, args))

    def ui_pump(self):
        try:
            for _ in range(200):
                try:
                    fn, args = self.uiq.get_nowait()
                except queue.Empty:
                    break
                try:
                    fn(*args)
                except Exception:
                    pass
        finally:
            self.root.after(30, self.ui_pump)

    # ------------------------------------------------------------ parsers
    def parse_frequency_03(self, f):
        if not f or len(f) < 10 or f[4] != 0x03:
            return None
        try:
            return int("".join(f"{b:02x}" for b in reversed(f[5:10])))
        except Exception:
            return None

    def parse_mode_04(self, f):
        if not f or len(f) < 7 or f[4] != 0x04:
            return None, None
        fil = f[6] if len(f) >= 8 and f[6] in (1, 2, 3) else None
        return MODES.get(f[5]), fil

    def parse_level(self, f):
        if not f or len(f) < 8 or f[4] not in (0x14, 0x15):
            return None
        try:
            return int(f"{f[6]:02x}{f[7]:02x}")
        except Exception:
            return None

    def parse_tx_1c(self, f):
        if not f or len(f) < 8 or f[4] != 0x1C:
            return None
        return f[6] == 0x01

    def parse_sql(self, f):
        if not f or len(f) < 8 or f[4] != 0x15:
            return None
        return f[6] == 0x01

    def read_toggle(self, key):
        _, cmd, sub, vals, _ = TOGGLES[key]
        f = self.send_cmd(cmd, sub)
        if not f or f[4] != cmd:
            return None
        idx = 5 if sub is None else 6
        if len(f) <= idx + 1:
            return None
        return f[idx]

    def read_dup(self):
        f = self.send_cmd(0x0F)
        if not f or f[4] != 0x0F or len(f) < 7:
            return None
        return f[5]

    def read_tone(self, sub):
        f = self.send_cmd(0x1B, sub)
        if not f or f[4] != 0x1B or len(f) < 10:
            return None
        try:
            return bcd_to_int(f[6:9]) / 10
        except ValueError:
            return None

    def read_sub(self):
        """SUB band (unselected) frequency + mode: CI-V 25 01 / 26 01. Returns (hz, mode) or None."""
        f = self.send_cmd(0x25, 0x01)
        if f is None or f[4] == NAK or f[4] != 0x25 or len(f) < 12:
            if f is not None:
                self.sub_nak += 1
            return None
        try:
            hz = int("".join(f"{b:02x}" for b in reversed(f[6:11])))
        except ValueError:
            return None
        self.sub_nak = 0
        mode = None
        m = self.send_cmd(0x26, 0x01)
        if m and m[4] == 0x26 and len(m) >= 8:
            mode = MODES.get(m[6])
        return hz, mode

    def read_rit(self):
        f = self.send_cmd(0x21, 0x00)
        if not f or f[4] != 0x21 or len(f) < 10:
            return None
        try:
            hz = bcd_to_int([f[7], f[6]])
        except ValueError:
            return None
        return -hz if f[8] == 0x01 else hz

    # ------------------------------------------------------ polling thread
    def read_levels(self):
        for _, sub, _ in LEVELS:
            if not self.running:
                return
            v = self.parse_level(self.send_cmd(0x14, sub))
            if v is not None:
                self.ui(self.set_level_ui, sub, v)

    def identify(self):
        f = self.send_cmd(0x19, 0x00)
        if f and f[4] == 0x19 and len(f) >= 8:
            self.rig_name = "IC-9700" if f[6] == 0xA2 else f"RIG ID {f[6]:02X}"
            self.ui(self.set_link, True)

    def poll_radio(self):
        cycle = 0
        miss = 0
        identified = False
        me = threading.current_thread()
        while self.running:
            self.run_queue()
            st = {}
            hz = self.parse_frequency_03(self.send_cmd(0x03))
            if self.io_error:
                break
            if hz is None:
                miss += 1
                if miss == LINK_MISS_LIMIT:
                    self.ui(self.safe_update_ui, {"link": False})
                time.sleep(0.25)
                continue
            if miss >= LINK_MISS_LIMIT:
                st["link"] = True
            miss = 0
            st["hz"] = hz

            if not identified:
                identified = True
                self.identify()
                if self.scope_on:
                    self.scope_output(True)

            if self.memread is not None:
                self.memread_step()

            tx = self.parse_tx_1c(self.send_cmd(0x1C, 0x00))
            st["tx"] = tx
            if cycle % 3 == 0 or self.mode_refresh:
                self.mode_refresh = False
                st["mode"], st["filter"] = self.parse_mode_04(self.send_cmd(0x04))

            s_raw, sql_open = None, None
            if tx:
                st["p_raw"] = self.parse_level(self.send_cmd(0x15, 0x11))
                st["swr"] = self.parse_level(self.send_cmd(0x15, 0x12))
                st["alc"] = self.parse_level(self.send_cmd(0x15, 0x13))
                if cycle % 2:
                    st["comp"] = self.parse_level(self.send_cmd(0x15, 0x14))
                else:
                    st["id"] = self.parse_level(self.send_cmd(0x15, 0x16))
            elif tx is False:
                s_raw = self.parse_level(self.send_cmd(0x15, 0x02))
                sql_open = self.parse_sql(self.send_cmd(0x15, 0x01))
                st["s_raw"], st["sql"] = s_raw, sql_open
                if sql_open is not None:
                    self.sql_live = (bool(sql_open), time.time())

            if self.io_error:
                break

            if self.full_sync:
                self.full_sync = False
                slow = []
                for key, fn in self.slow_reads:
                    v = fn()
                    if v is not None:
                        slow.append((key, v))
                st["slow"] = slow
                self.read_levels()
            elif cycle % 2 == 1 and not self.scan:
                key, fn = self.slow_reads[self.slow_idx % len(self.slow_reads)]
                self.slow_idx += 1
                v = fn()
                if v is not None:
                    st["slow"] = [(key, v)]
            elif cycle % 4 == 2 and not self.scan and self.sub_nak < 3:
                st["sub"] = self.read_sub()
            elif cycle % 6 == 4 and not self.scan:
                name, sub, _ = LEVELS[(cycle // 6) % len(LEVELS)]
                v = self.parse_level(self.send_cmd(0x14, sub))
                if v is not None:
                    self.ui(self.set_level_ui, sub, v)

            st["scan"] = self.scan_step(tx, sql_open, s_raw)
            self.ui(self.safe_update_ui, st)
            cycle += 1
            time.sleep(0.02)
            self.pump()
        if self.io_error:
            self.ui(self.on_link_lost, me)

    def scan_step(self, tx, sql_open, s_raw):
        """Runs on the polling thread. Returns 'scan', 'hold' or None."""
        sc = self.scan
        if not sc:
            return None
        now = time.time()
        if tx:
            sc["hold_until"] = now + sc["hold"]
            return "hold"
        settled = now - sc["last_move"] >= SCAN_SETTLE
        if settled and s_raw is not None and 0 <= sc["idx"] < len(sc["levels"]):
            old = sc["levels"][sc["idx"]]
            sc["levels"][sc["idx"]] = s_raw if old is None else max(old, s_raw)
        signal = settled and ((sc["use_sql"] and sql_open) or
                              (sc["use_s"] and s_raw is not None and s_raw >= sc["s_thresh"]))
        if signal:
            sc["hold_until"] = now + sc["hold"]
        if now < sc["hold_until"]:
            return "hold"
        if now - sc["last_move"] >= sc["dwell"]:
            sc["idx"] = (sc["idx"] + 1) % len(sc["items"])
            hz, mode = sc["items"][sc["idx"]]
            self.send_cmd(0x05, data=freq_to_bcd(hz))
            if mode in MODE_REVERSE:
                self.send_cmd(0x06, MODE_REVERSE[mode], [0x01])
                self.mode_refresh = True
            sc["last_move"] = time.time()
        return "scan"

    # ----------------------------------------------------------- UI update
    def set_link(self, ok):
        self.link_ok = ok
        if ok:
            self.rig_off = False
        self.refresh_power()
        if time.time() < self.status_hold:
            return
        if not ok and self.rig_off:
            self.set_status("RADIO SWITCHED OFF - press POWER (top left) to switch it on", MUTED)
            return
        if ok:
            rig = f"{self.rig_name} " if self.rig_name else "RIG "
            self.set_status(f"ONLINE - {rig}CONNECTED ON {self.port_name} @ {self.baud}", GREEN)
        else:
            self.set_status("PORT OPEN BUT NO REPLY FROM RIG - CHECK POWER / CI-V ADDRESS / BAUD", ORANGE)

    def safe_update_ui(self, st):
        if not self.running:
            return
        now = time.time()
        if st.get("link") is not None:
            self.set_link(st["link"])

        hz = st.get("hz")
        if hz is not None:
            if now - self.tune_time > 0.8:
                self.cur_hz = hz
            b = band_of(self.cur_hz or hz)
            self.chip_band.set_active(bool(b), b.upper() if b else "BAND")
            if b:
                self.config["band_last"][b] = hz

        mode = st.get("mode")
        if mode and now - self.mode_time > 1.0:
            self.cur_mode = mode
            if st.get("filter"):
                self.cur_filter = st["filter"]
            self.chip_mode.set_active(True, mode)
            self.chip_fil.set_active(bool(self.cur_filter), f"FIL{self.cur_filter}" if self.cur_filter else "FIL")
            self.refresh_mode_buttons()

        tx = st.get("tx")
        if tx is not None:
            self.is_tx = tx
            if not tx and self.ptt_on and now - self.ptt_since > 1.5:
                self.ptt_on = False      # released at the rig
            new_mode = "tx" if tx else "rx"
            if new_mode != self.meter_mode:
                self.meter_mode = new_mode
                self.meter_frac = 0.0
                self.peak_frac = 0.0
                self.swr_sev = 0
                self.pwr_frac = 0.0
                self.tx_text = {}
                self.lbl_info.config(text="")
                self.lbl_smeter.config(text="")
            self.refresh_ptt()

        if tx:
            if st.get("swr") is not None:
                raw = st["swr"]
                self.meter_frac = min(raw / METER_MAX, 1.0)
                text, self.swr_sev = swr_from_raw(raw)
                self.lbl_smeter.config(text=text, fg=(LCD_GREEN, LCD_ORANGE, LCD_RED)[self.swr_sev])
            if st.get("p_raw") is not None:
                self.pwr_frac = min(st["p_raw"] / METER_MAX, 1.0)
                pct = power_pct(st["p_raw"])
                maxw = BAND_MAX_W.get(band_of(self.cur_hz or 0))
                self.tx_text["po"] = f"Po {pct * maxw / 100:.0f}W" if maxw else f"Po {pct}%"
            if st.get("alc") is not None:
                self.tx_text["alc"] = f"ALC {alc_pct(st['alc'])}%"
            if st.get("comp") is not None:
                self.tx_text["comp"] = f"COMP {comp_db(st['comp']):.0f}dB"
            if st.get("id") is not None:
                self.tx_text["id"] = f"Id {id_amps(st['id']):.1f}A"
            parts = [self.tx_text[k] for k in ("po", "alc", "comp", "id") if k in self.tx_text]
            self.lbl_info.config(text="  ".join(parts), fg=LCD_ORANGE)
        elif tx is False and st.get("s_raw") is not None:
            raw = st["s_raw"]
            self.meter_frac = min(raw / METER_MAX, 1.0)
            self.lbl_smeter.config(text=s_label(raw), fg=LCD_TEXT if raw <= S9_RAW else LCD_RED)
            if self.meter_frac >= self.peak_frac:
                self.peak_frac, self.peak_time = self.meter_frac, now
            elif now - self.peak_time > 1.5:
                self.peak_frac = max(self.meter_frac, self.peak_frac - 0.03)
            self.lbl_info.config(text=f"PEAK {s_label(self.peak_frac * METER_MAX)}", fg=LCD_LABEL)
        if tx is False and st.get("sql") is not None:
            self.rx_busy = bool(st["sql"])
        elif tx:
            self.rx_busy = False

        for key, val in st.get("slow", []):
            self.apply_remote(key, val)
        if "sub" in st:
            sub = st["sub"]
            new = (sub[0], sub[1] or self.sub_mode) if sub else (self.sub_hz, self.sub_mode)
            if new != (self.sub_hz, self.sub_mode) or (sub is None and self.sub_nak >= 3):
                self.sub_hz, self.sub_mode = new
                self.draw_sub()

        if "scan" in st and self.scan is not None:
            self.set_scan_badge(st["scan"])
            if self.cur_tab == "SCAN" and now - self._sweep_drawn > 0.35:
                self._sweep_drawn = now
                self.draw_sweep()

        self.draw_freq()
        self.draw_meter()

    def apply_remote(self, key, val):
        now = time.time()
        if key in TOGGLES:
            if now - self.toggle_touch.get(key, 0) < 1.5:
                return
            self.toggle_state[key] = val
            self.refresh_toggle(key)
        elif key == "dup":
            if now - self.dup_touch < 1.5:
                return
            self.dup_state = val
            self.refresh_duplex()
        elif key in ("tone_hz", "tsql_hz"):
            var = self.tone_var if key == "tone_hz" else self.tsql_var
            var.set(f"{val:.1f}")
        elif key == "rit_hz":
            if now - self.toggle_touch.get("rit_hz", 0) > 1.5:
                self.rit_hz = val
                self.lbl_rit.config(text=f"{val:+d} Hz")
        elif key == "vd":
            self.vd = vd_volts(val)
            self.chip_vd.set_active(True, f"{self.vd:.1f} V", tone="green" if self.vd >= 12.5 else "amber")

    # ------------------------------------------------- phone / browser access
    def start_web(self, quiet=True, parent=None):
        self.web.stop()
        if self.config.get("web_on") and self.config.get("web_password"):
            port = int(self.config.get("web_port", WEB_DEFAULT_PORT))
            if not self.config.get("web_secret"):
                self.config["web_secret"] = secrets.token_hex(16)
                save_config(self.config)
            if self.web.start(port, self.config["web_password"], self.config["web_secret"]):
                self.web_mem_dirty = True
                self.start_https(quiet=quiet)
            elif quiet:
                err = self.web.error
                self.root.after(1500, lambda: self.flash_status(f"PHONE ACCESS NOT STARTED: {err}", RED, 8))
            else:
                messagebox.showerror("Phone access", f"Could not start on port {port}:\n{self.web.error}\n\n"
                                     "Is another copy of the program already running? Try a different port.",
                                     parent=parent or self.root)
        self.update_port_label()

    def start_https(self, quiet=True):
        """Start the https page if a certificate has been fetched; renew it in the background when old."""
        name = self.config.get("web_https_name")
        if not (self.web.running and name and os.path.exists(CERT_PATH) and os.path.exists(KEY_PATH)):
            return
        port = int(self.config.get("web_https_port", 8074))
        if not self.web.start_https(port, CERT_PATH, KEY_PATH, name) and not quiet:
            messagebox.showerror("HTTPS", f"Could not start the https page on port {port}:\n{self.web.https_error}")
        try:
            age = time.time() - os.path.getmtime(CERT_PATH)
        except OSError:
            age = 0
        if age > 30 * 86400 and not getattr(self, "_cert_renewing", False):   # Tailscale certificates last 90 days
            self._cert_renewing = True

            def job():
                ok, _ = fetch_ts_cert(name)
                self._cert_renewing = False
                if ok:
                    self.ui(self.start_https)
            threading.Thread(target=job, daemon=True).start()

    def web_tick(self):
        try:
            if self.web.running:
                mems = None
                if self.web_mem_dirty:
                    self.web_mem_dirty = False
                    mems = self.web_memories()
                self.web.publish(self.web_state(), mems)
            if self.audio is not None:
                self.audio.idle_check()
        except Exception:
            pass
        finally:
            self.root.after(300, self.web_tick)

    def _web_toggle(self, key):
        label, _, _, vals, texts = TOGGLES[key]
        v = self.toggle_state.get(key)
        if v is None:
            return None
        return [bool(key in ALWAYS_LIT or v != vals[0]), texts[vals.index(v)] if (texts and v in vals) else label]

    def web_state(self):
        """Snapshot of what the window shows, for the phone page (Tk thread)."""
        on = self.running
        st = {
            "online": on, "link": self.link_ok, "status": self.lbl_status.cget("text"), "rig": self.rig_name,
            "utc": self.clock_text, "hz": self.cur_hz if on else None, "mode": self.cur_mode if on else None,
            "fil": self.cur_filter if on else None, "band": band_of(self.cur_hz) if (on and self.cur_hz) else "",
            "tx": bool(on and self.is_tx), "busy": bool(on and self.rx_busy and not self.is_tx),
            "ptt": bool(on and self.ptt_on), "meter": self.meter_mode, "mfrac": round(self.meter_frac, 3),
            "peak": round(self.peak_frac, 3), "pwr": round(self.pwr_frac, 3), "swr_sev": self.swr_sev,
            "mtext": self.lbl_smeter.cget("text"), "info": self.lbl_info.cget("text"),
            "sub_hz": self.sub_hz if on else None, "sub_mode": self.sub_mode if on else None,
            "sub_band": band_of(self.sub_hz) if (on and self.sub_hz) else "",
            "toggles": {k: self._web_toggle(k) for k in TOGGLES},
            "levels": {str(sub): v for sub, v in self.level_vals.items()},
            "dup": self.dup_state if on else None, "rit": self.rit_hz,
            "vd": round(self.vd, 1) if (on and self.vd) else None,
            "tone": self.tone_var.get(), "tsql": self.tsql_var.get(), "step": self.step_hz(),
            "scan": bool(self.scan), "scope_on": self.scope_on,
            "rig_on": self.radio_is_on(), "rig_off": bool(on and self.rig_off),
            "span": (self.span_set or self.cur_span()) if (on and self.scope_on) else None, "mem_rev": self.web_mem_rev,
            "atok": self.web.audio_token, "audio_sql": bool(self.config.get("audio_sql", True)),
            "sql_muted": bool(self.audio is not None and self.audio.listener_count() and self.audio.squelched()),
            "https_url": self.web.https_url,
            "cwd": {"on": self.cwdec.active, "text": self.cwdec.text[-240:],
                    "info": (f"{self.cwdec.tone} Hz \u00b7 {self.cwdec.wpm()} WPM" if self.cwdec.snr_ok
                             else "waiting for CW") if self.cwdec.active else (self.cwdec.error or ""),
                    "sens": self.cwdec.sens, "sens_note": self.cwd_sens_text()},
            "audio_info": self.audio.status() if self.audio is not None else "",
            "audio_err": (self.audio.error if self.audio is not None else
                          "Audio isn't set up on the PC: run  py -m pip install sounddevice  there and restart the program."),
        }
        if on and self.scope_on and self.scope_data:
            lo, hi, data = self.scope_data
            st["scope"] = {"lo": lo, "hi": hi, "seq": self.web_scope_seq, "d": self._resample(data, 240),
                           "mk": self.scope_marker_hz(), "off": self.scope_offset if self.scope_centre else 0}
        return st

    def lite_state(self):
        """Small snapshot for the lite phone page (Tk thread): only what it shows."""
        on = self.running
        lv = self.level_vals
        pamp = self._web_toggle("pamp")
        note = self.web_note[0] if (self.web_note and time.time() - self.web_note[1] < 5) else ""
        return {
            "online": on, "link": self.link_ok, "rig_on": self.radio_is_on(), "rig_off": bool(on and self.rig_off),
            "hz": self.cur_hz if on else None, "mode": self.cur_mode if on else None,
            "band": band_of(self.cur_hz) if (on and self.cur_hz) else "",
            "tx": bool(on and self.is_tx), "busy": bool(on and self.rx_busy and not self.is_tx),
            "ptt": bool(on and self.ptt_on), "meter": self.meter_mode, "mfrac": round(self.meter_frac, 3),
            "peak": round(self.peak_frac, 3), "pwr": round(self.pwr_frac, 3), "swr_sev": self.swr_sev,
            "mtext": self.lbl_smeter.cget("text"), "info": self.lbl_info.cget("text"),
            "rfp": lv.get(0x0A), "rf": lv.get(0x02), "sql": lv.get(0x03),
            "pamp": bool(pamp and pamp[0]), "scan": bool(self.scan), "step": self.step_hz(), "utc": self.clock_text,
            "sql_muted": bool(self.audio is not None and self.audio.listener_count() and self.audio.squelched()),
            "audio_err": (self.audio.error if self.audio is not None else
                          "Audio isn't set up on the PC: run  py -m pip install sounddevice  there and restart the program."),
            "note": note, "status": self.lbl_status.cget("text"),
        }

    def lite_tick(self):
        """Faster, smaller updates for lite phone pages, only while one is connected."""
        try:
            if self.web.running and self.web.lite_sessions > 0:
                self.web.publish_lite(self.lite_state())
        except Exception:
            pass
        finally:
            self.root.after(150, self.lite_tick)

    def web_scan(self, on):
        """Start / stop a memory-channel scan from the lite phone page."""
        if not on:
            if self.scan:
                self.stop_scan()
            return
        if self.scan or not self.running:
            return
        if not self.config["memories"]:
            self.web_note = ("No memory channels saved yet - add some on the PC (MEMORY tab)", time.time())
            return
        self.scan_src.set("mem")
        if not (self.scan_sql.get() or self.scan_use_s.get()):
            self.scan_sql.set(True)
        self.start_scan()

    def sql_in_use(self):
        """Squelch turned up above fully open?"""
        return (self.level_vals.get(0x03) or 0) > 0

    def web_memories(self):
        return [{"i": i, "name": m["name"], "mhz": hz_to_mhz(m["hz"]), "mode": m.get("mode") or "",
                 "ch": m.get("ch", ""), "info": mem_info(m)} for i, m in enumerate(self.config["memories"])]

    def web_command(self, c):
        """A command from the phone page (runs on the Tk thread, same as clicking in the window)."""
        a = c.get("a")
        try:
            if a == "tune":
                self.request_frequency(int(c["hz"]))
            elif a == "cwdec":
                if c.get("on"):
                    self.cwdec.on_text = self.cwd_append
                    self.cwdec.start()
                else:
                    self.cwdec.stop()
                if self.cwd_win is not None and self.cwd_win.winfo_exists():
                    self.cwd_tick(once=True)
            elif a == "cwd_clear":
                self.cwd_clear()
            elif a == "cwd_sens":
                self.cwd_set_sens(str(c.get("v")))
            elif a == "step":
                step = int(c.get("step") or 0)
                self.step_tune(1 if int(c["dir"]) > 0 else -1, step if step in dict(STEPS).values() else None)
            elif a == "mode" and c.get("mode") in MODE_REVERSE:
                self.set_radio_mode(c["mode"])
            elif a == "filter" and c.get("n") in (1, 2, 3):
                self.set_filter(int(c["n"]))
            elif a == "band" and c.get("band") in [b[0] for b in BANDS]:
                self.band_click(c["band"])
            elif a == "toggle" and c.get("key") in TOGGLES:
                self.click_toggle(c["key"])
            elif a == "level":
                sub, v = int(c["sub"]), max(0, min(255, int(c["v"])))
                if sub in self.level_scales:
                    self.level_scales[sub].set(v)
                    self.on_level(sub, v)
            elif a == "dup" and c.get("code") in (0x10, 0x11, 0x12, 0x01, 0x00):
                self.set_duplex(int(c["code"]))
            elif a == "tone":
                t = float(c["t"])
                if any(abs(t - x) < 0.05 for x in CTCSS):
                    sql = bool(c.get("sql"))
                    (self.tsql_var if sql else self.tone_var).set(f"{t:.1f}")
                    self.set_tone(0x01 if sql else 0x00, f"{t:.1f}")
            elif a == "rit":
                self.set_rit(int(c["hz"]))
            elif a == "swap":
                self.swap_bands()
            elif a == "mem":
                i = int(c["i"])
                if 0 <= i < len(self.config["memories"]):
                    self.recall_mem(self.config["memories"][i])
            elif a == "audio_sql":
                self.config["audio_sql"] = bool(c.get("on"))
                save_config(self.config)
            elif a == "power":
                self.power_set(bool(c.get("on")), " FROM PHONE")
            elif a == "span":
                self.step_span(1 if int(c.get("dir", 1)) > 0 else -1, wrap=bool(c.get("wrap")))
            elif a == "scan":
                self.web_scan(bool(c.get("on")))
            elif a == "scope":
                if bool(c.get("on")) != self.scope_on:
                    self.toggle_scope()
            elif a == "unkey":                 # release PTT, whoever keyed it
                if self.running and (self.ptt_on or self.is_tx):
                    self.ptt_on = False
                    self.web_keyed = False
                    self.post_cmd(0x1C, 0x00, [0x00])
                    self.refresh_ptt()
                    self.flash_status("PTT RELEASED FROM PHONE", AMBER)
        except (KeyError, TypeError, ValueError):
            pass

    def web_addresses(self):
        port = self.web.port or self.config.get("web_port", WEB_DEFAULT_PORT)
        host = socket.gethostname()
        ips = set()
        try:
            for info in socket.getaddrinfo(host, None, socket.AF_INET):
                ips.add(info[4][0])
        except OSError:
            pass
        # Tailscale addresses are in 100.64.0.0/10
        ts = sorted(ip for ip in ips if ip.startswith("100.") and 64 <= int(ip.split(".")[1]) <= 127)
        return [f"http://{ip}:{port}" for ip in ts] + [f"http://{host.lower()}:{port}"]

    def fast_ptt(self, on):
        """PTT from a phone, called on that phone's connection thread (not the Tk thread): the CI-V
        command goes out as soon as the serial port is free instead of waiting in the queue.
        Returns (ok, reason)."""
        if not self.running:
            return False, "The PC isn't connected to the radio"
        if on:
            if (self.ptt_on or self.is_tx) and not self.web_keyed:
                return False, "The radio is already transmitting (keyed from the PC)"
            self.ptt_on = True
            self.web_keyed = True
            self.ptt_since = time.time()
            f = self.send_cmd(0x1C, 0x00, [0x01])
            ok = not (f is not None and f[4] == NAK)
            if not ok:
                self.ptt_on = False
                self.web_keyed = False
            self.ui(self._fast_ptt_ui, True, ok)
            return ok, "" if ok else "The radio refused PTT"
        if not self.web_keyed:
            return True, ""
        self.web_keyed = False
        self.ptt_on = False
        self.send_cmd(0x1C, 0x00, [0x00])
        self.ui(self._fast_ptt_ui, False, True)
        return True, ""

    def _fast_ptt_ui(self, on, ok):
        self.refresh_ptt()
        if on and ok:
            self.flash_status("TX FROM PHONE", AMBER, 2)
        elif on:
            self.flash_status("RIG REJECTED PTT FROM PHONE", RED)

    def web_ptt(self, on):
        """PTT from a phone's TALK button (Tk thread). The audio link drops it if the phone goes quiet."""
        if not self.running:
            return
        if on:
            if self.ptt_on or self.is_tx:
                return
            self.ptt_on = True
            self.web_keyed = True
            self.ptt_since = time.time()
            self.refresh_ptt()

            def job():
                f = self.send_cmd(0x1C, 0x00, [0x01])
                if f is not None and f[4] == NAK:
                    self.ptt_on = False
                    self.ui(self.flash_status, "RIG REJECTED PTT FROM PHONE", RED)
            self.post(job)
            self.flash_status("TX FROM PHONE", AMBER, 2)
        elif self.web_keyed:
            self.web_keyed = False
            if self.ptt_on or self.is_tx:
                self.ptt_on = False
                self.post_cmd(0x1C, 0x00, [0x00])
                self.refresh_ptt()

    def open_phone_page(self, page=""):
        if not self.web.running:
            messagebox.showinfo("Phone", "Phone access is off. Turn it on in Phone > Phone access first.")
            self.open_web_settings()
            return
        webbrowser.open((self.web.https_url or f"http://127.0.0.1:{self.web.port}/") + page)

    def setup_https(self, parent, done):
        """Get this PC's https certificate from Tailscale and start the https page."""
        if not self.web.running:
            messagebox.showinfo("HTTPS", "Tick 'Allow access from my phone', set a password and click Save first.",
                                parent=parent)
            return
        busy = tk.Toplevel(parent)
        busy.title("HTTPS")
        busy.configure(bg=PANEL)
        busy.transient(parent)
        self.lbl(busy, "Getting a certificate from Tailscale...\nThis can take up to a minute.", fg=TEXT).pack(
            padx=px(24), pady=px(18))

        def finish(ok, info):
            try:
                busy.destroy()
            except tk.TclError:
                pass
            if ok:
                self.config["web_https_name"] = info
                save_config(self.config)
                self.start_https(quiet=False)
                done()
                if self.web.https_url:
                    messagebox.showinfo("HTTPS", "HTTPS is on. On your phone open:\n\n" + self.web.https_url +
                                        "\n\nThe TALK button (microphone) works on this address.", parent=parent)
                return
            if info == "NOT_ENABLED":
                if messagebox.askyesno(
                        "HTTPS",
                        "HTTPS certificates are switched off for your Tailscale network. This is a one-time "
                        "switch in your Tailscale account:\n\n"
                        "1. On the page that opens, find 'HTTPS Certificates' (MagicDNS must be on as well)\n"
                        "2. Click 'Enable HTTPS' and confirm\n"
                        "3. Come back here and click 'Turn on HTTPS' again\n\nOpen the Tailscale page now?",
                        parent=parent):
                    webbrowser.open("https://login.tailscale.com/admin/dns")
            else:
                messagebox.showerror("HTTPS", "Tailscale could not provide a certificate:\n\n" + info[-900:],
                                     parent=parent)

        def job():
            ok, info = fetch_ts_cert(None)
            self.ui(finish, ok, info)
        threading.Thread(target=job, daemon=True).start()

    def open_web_settings(self):
        win = tk.Toplevel(self.root)
        win.title("Phone access")
        win.configure(bg=PANEL)
        win.resizable(False, False)
        win.transient(self.root)
        win.grab_set()

        on_var = tk.BooleanVar(value=bool(self.config.get("web_on")))
        self.check(win, "Allow access from my phone / browser", on_var).grid(
            row=0, column=0, columnspan=3, sticky="w", padx=px(10), pady=(px(12), px(4)))
        self.lbl(win, "Port", fg=MUTED).grid(row=1, column=0, sticky="w", padx=px(14), pady=px(5))
        port_sp = self.spin(win, 1024, 65535, 1, self.config.get("web_port", WEB_DEFAULT_PORT), width=7)
        port_sp.grid(row=1, column=1, sticky="w", padx=px(4))
        self.lbl(win, "Password", fg=MUTED).grid(row=2, column=0, sticky="w", padx=px(14), pady=px(5))
        pw = self.entry(win, width=22, show="•")
        pw.insert(0, self.config.get("web_password", ""))
        pw.grid(row=2, column=1, sticky="w", padx=px(4), ipady=px(2))
        show_var = tk.BooleanVar(value=False)
        self.check(win, "Show", show_var).grid(row=2, column=2, sticky="w", padx=(px(6), px(14)))
        show_var.trace_add("write", lambda *a: pw.config(show="" if show_var.get() else "•"))

        self.caption(win, "Open on your phone").grid(row=3, column=0, columnspan=3, sticky="w",
                                                    padx=px(14), pady=(px(12), 0))
        info = tk.Label(win, text="", bg=PANEL, fg=TEXT, font=F["mono_b"], justify="left", anchor="w")
        info.grid(row=4, column=0, columnspan=3, sticky="w", padx=px(14), pady=(px(2), 0))
        hrow = tk.Frame(win, bg=PANEL)
        hrow.grid(row=5, column=0, columnspan=3, sticky="w", padx=px(14), pady=(px(6), 0))

        def refresh_info():
            if self.web.running:
                lines = self.web_addresses()
                if self.web.https_url:
                    lines = [self.web.https_url + "   <- use this one (microphone works)"] + lines
                info.config(text="\n".join(lines), fg=GREEN)
            elif self.web.error:
                info.config(text=f"Not running: {self.web.error}", fg=RED)
            else:
                info.config(text="Off", fg=MUTED)

        self.btn(hrow, "Turn on HTTPS (needed for the phone microphone)",
                 lambda: self.setup_https(win, refresh_info), width=330, tone="accent").pack(side="left")

        # ---- audio devices
        self.caption(win, "Audio - IC-9700 USB audio").grid(row=6, column=0, columnspan=3, sticky="w",
                                                             padx=px(14), pady=(px(14), 0))
        in_var = tk.StringVar(value=self.config.get("audio_in", AUDIO_AUTO))
        out_var = tk.StringVar(value=self.config.get("audio_out", AUDIO_AUTO))
        if AUDIO_READY:
            ins = [AUDIO_AUTO] + [n for _, n in AudioEngine.devices("input")]
            outs = [AUDIO_AUTO] + [n for _, n in AudioEngine.devices("output")]
        else:
            ins, outs = [AUDIO_AUTO], [AUDIO_AUTO]
        self.lbl(win, "Receive audio from", fg=MUTED).grid(row=7, column=0, sticky="w", padx=px(14), pady=px(4))
        ttk.Combobox(win, textvariable=in_var, values=ins, state="readonly" if AUDIO_READY else "disabled",
                     width=36, font=F["ui"]).grid(row=7, column=1, columnspan=2, sticky="w", padx=px(4))
        self.lbl(win, "Transmit audio to", fg=MUTED).grid(row=8, column=0, sticky="w", padx=px(14), pady=px(4))
        ttk.Combobox(win, textvariable=out_var, values=outs, state="readonly" if AUDIO_READY else "disabled",
                     width=36, font=F["ui"]).grid(row=8, column=1, columnspan=2, sticky="w", padx=px(4))
        if AUDIO_READY:
            note = ("Radio menu: SET > Connectors > MOD Input > DATA OFF MOD = USB (and DATA MOD = USB\n"
                    "for data modes). USB audio levels are under SET > Connectors as well.\n"
                    "The phone asks for the password once and remembers it. On the https address,\n"
                    "Chrome on Android offers 'Install app' to put it on your home screen as an app.\n"
                    "TX from the phone stops by itself if its connection or microphone drops,\n"
                    "and the PTT time-out in Settings still applies.")
            ncol = DIM
        else:
            note = ("Audio needs one more package on this PC. Open a command prompt and run:\n"
                    "    py -m pip install sounddevice\n"
                    "then restart IC9700 Monitor. (Reinstalling with the new setup does this for you.)")
            ncol = AMBER
        tk.Label(win, bg=PANEL, fg=ncol, font=F["small"], justify="left", text=note).grid(
            row=9, column=0, columnspan=3, sticky="w", padx=px(14), pady=(px(8), 0))

        def apply():
            try:
                port = int(port_sp.get())
                if not 1024 <= port <= 65535:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Phone access", "The port must be a number from 1024 to 65535.", parent=win)
                return
            password = pw.get()
            if on_var.get() and len(password) < 6:
                messagebox.showerror("Phone access", "Choose a password of at least 6 characters.", parent=win)
                return
            audio_changed = (in_var.get(), out_var.get()) != (self.config.get("audio_in", AUDIO_AUTO),
                                                               self.config.get("audio_out", AUDIO_AUTO))
            restart = (bool(on_var.get()), port, password) != (bool(self.config.get("web_on")),
                                                              self.config.get("web_port"),
                                                              self.config.get("web_password"))
            self.config.update(web_on=bool(on_var.get()), web_port=port, web_password=password,
                               audio_in=in_var.get(), audio_out=out_var.get())
            save_config(self.config)
            if restart or not self.web.running:
                self.start_web(quiet=False, parent=win)
            if audio_changed and self.audio is not None:
                threading.Thread(target=self.audio.restart, daemon=True).start()
            refresh_info()

        bt = tk.Frame(win, bg=PANEL)
        bt.grid(row=10, column=0, columnspan=3, pady=(px(12), px(14)))
        self.btn(bt, "Save", apply, width=90, tone="green").pack(side="left", padx=px(4))
        self.btn(bt, "Close", win.destroy, width=80).pack(side="left", padx=px(4))
        refresh_info()

    # --------------------------------------------------------- toggles
    def refresh_toggle(self, key):
        label, _, _, vals, texts = TOGGLES[key]
        v = self.toggle_state.get(key)
        text = texts[vals.index(v)] if (texts and v in vals) else label
        lit = v is not None and (key in ALWAYS_LIT or v != vals[0])
        for b in self.toggle_btns.get(key, []):
            b.set_active(lit, text)
        if key == "sat":
            self.chip_sat.set_active(lit, "SAT")
        self.schedule("draw_status")

    def click_toggle(self, key):
        if not self.running:
            return
        _, _, _, vals, _ = TOGGLES[key]
        cur = self.toggle_state.get(key)
        nxt = vals[(vals.index(cur) + 1) % len(vals)] if cur in vals else vals[1]
        self.set_toggle_value(key, nxt)

    def set_toggle_value(self, key, nxt):
        if not self.running:
            return
        label, cmd, sub, vals, _ = TOGGLES[key]
        self.toggle_state[key] = nxt
        self.toggle_touch[key] = time.time()
        self.refresh_toggle(key)
        if cmd == 0x11:
            frame = (0x11, nxt, None)
        elif cmd == 0x1A:
            frame = (0x1A, 0x06, [nxt, 0x01 if nxt else 0x00])
        else:
            frame = (cmd, sub, [nxt])

        def job():
            f = self.send_cmd(*frame)
            if f is not None and f[4] == NAK:
                self.ui(self.flash_status, f"RIG REJECTED {label} (not available in this mode?)", RED)
                self.toggle_touch[key] = 0
                v = self.read_toggle(key)
                if v is not None:
                    self.ui(self.apply_remote, key, v)
        self.post(job)

    def set_duplex(self, code):
        if not self.running:
            return
        self.dup_state = code
        self.dup_touch = time.time()
        self.refresh_duplex()
        names = {0x10: "SIMPLEX", 0x11: "DUP-", 0x12: "DUP+", 0x01: "SPLIT ON", 0x00: "SPLIT OFF"}
        self.cmd_status(0x0F, code, None, names[code])

    def refresh_duplex(self):
        d = self.dup_state
        text = DUPLEX_TEXT.get(d)
        self.chip_dup.set_active(bool(text), text or "SIMP")
        for code, b in getattr(self, "dup_btns", {}).items():
            b.set_active(d == code and code != 0x00)

    def set_tone(self, sub, text):
        try:
            t = float(text)
        except ValueError:
            return
        self.cmd_status(0x1B, sub, tone_to_bcd(t), f"{'TONE' if sub == 0 else 'TSQL'} {t:.1f} Hz")

    def nudge_rit(self, d):
        self.set_rit(self.rit_hz + d)

    def set_rit(self, hz):
        hz = max(-9999, min(9999, int(hz)))
        self.rit_hz = hz
        self.toggle_touch["rit_hz"] = time.time()
        self.lbl_rit.config(text=f"{hz:+d} Hz")
        self.post_cmd(0x21, 0x00, rit_to_bcd(hz))

    def refresh_mode_buttons(self):
        for m, b in self.mode_btns.items():
            b.set_active(m == self.cur_mode)
        for n, b in self.fil_btns.items():
            b.set_active(n == self.cur_filter)

    # ------------------------------------------------------------ PTT
    def toggle_ptt(self):
        if not self.running:
            return
        want = not (self.ptt_on or self.is_tx)
        self.ptt_on = want
        self.ptt_since = time.time()
        self.refresh_ptt()

        def job():
            f = self.send_cmd(0x1C, 0x00, [0x01 if want else 0x00])
            if f is not None and f[4] == NAK:
                self.ui(self.flash_status, "RIG REJECTED PTT", RED)
                self.ptt_on = False
        self.post(job)

    def refresh_ptt(self):
        on = self.ptt_on or self.is_tx
        if on and self.ptt_on:
            left = int(self.config.get("tx_timeout", 180) - (time.time() - self.ptt_since))
            self.btn_ptt.set_active(True, f"TX  {max(0, left)}s")
        elif on:
            self.btn_ptt.set_active(True, "TX")
        else:
            self.btn_ptt.set_active(False, "TRANSMIT")

    def ptt_watchdog(self):
        if self.ptt_on:
            if time.time() - self.ptt_since > self.config.get("tx_timeout", 180):
                self.ptt_on = False
                self.post_cmd(0x1C, 0x00, [0x00])
                self.flash_status("TX TIME-OUT - PTT RELEASED", RED, 6)
            self.refresh_ptt()

    # --------------------------------------------------------- tuning
    def step_hz(self):
        return dict(STEPS).get(self.step_var.get(), 12500)

    def step_tune(self, direction, step=None):
        if not self.running or self.cur_hz is None:
            return
        step = step or self.step_hz()
        cur = int(self.cur_hz)
        new = (cur // step + 1) * step if direction > 0 else ((cur - 1) // step) * step
        self.request_frequency(new)

    def key_step(self, direction, step=None):
        if isinstance(self.root.focus_get(), (tk.Entry, tk.Spinbox, ttk.Combobox)):
            return
        self.step_tune(direction, step)

    def freq_wheel(self, x, direction):
        if not self.running or self.cur_hz is None:
            return
        place = self.digit_at(x)
        if place:
            self.request_frequency(int(self.cur_hz) + direction * place)
        else:
            self.step_tune(direction)

    def digit_at(self, x):
        for x0, x1, place in self.digit_hits:
            if x0 <= x <= x1:
                return place
        return None

    def freq_hover(self, e):
        place = self.digit_at(e.x) if e is not None else None
        if place != self.hover_digit:
            self.hover_digit = place
            self.draw_freq(force=True)

    def request_frequency(self, hz, stop_scan=True):
        if not self.running:
            return
        hz = int(hz)
        if not (100_000 <= hz <= 2_000_000_000):
            return
        if stop_scan and self.scan:
            self.stop_scan()
        self.cur_hz = hz
        self.tune_time = time.time()
        self.draw_freq()
        b = band_of(hz)
        self.chip_band.set_active(bool(b), b.upper() if b else "BAND")
        self.pending_hz = hz
        if not self.freq_queued:
            self.freq_queued = True
            self.post(self.apply_pending_freq)

    def apply_pending_freq(self):
        self.freq_queued = False
        hz = self.pending_hz
        if hz is not None:
            self.send_cmd(0x05, data=freq_to_bcd(hz))

    def band_click(self, name):
        default = next(b[3] for b in BANDS if b[0] == name)
        self.request_frequency(self.config["band_last"].get(name, default))

    def change_frequency(self):
        if not self.running:
            return
        raw = self.freq_entry.get().strip().replace(",", ".")
        if not raw:
            return
        try:
            hz = int(round(float(raw) * 1_000_000))
            if not (100_000 <= hz <= 2_000_000_000):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid frequency.\nExamples: 145.173 or 433.200")
            return
        self.request_frequency(hz)
        self.freq_entry.delete(0, tk.END)

    def set_radio_mode(self, mode_name, fil=None):
        if not self.running:
            return
        m_byte = MODE_REVERSE.get(mode_name)
        if m_byte is not None:
            fil = fil or self.cur_filter or 1
            self.post_cmd(0x06, m_byte, [fil])
            self.mode_refresh = True
            self.mode_time = time.time()
            self.cur_mode = mode_name
            self.cur_filter = fil
            self.chip_mode.set_active(True, mode_name)
            self.chip_fil.set_active(True, f"FIL{fil}")
            self.refresh_mode_buttons()

    def set_filter(self, n):
        if self.cur_mode:
            self.set_radio_mode(self.cur_mode, n)

    def swap_bands(self):
        if not self.running:
            return
        self.vfo_cmd(0xB0, "MAIN/SUB SWAPPED")
        if self.scan:
            self.stop_scan()

    def vfo_cmd(self, sub, want):
        if not self.running:
            return
        self.cmd_status(0x07, sub, None, want)
        self.tune_time = 0.0
        self.mode_time = 0.0
        self.mode_refresh = True

    # --------------------------------------------------------- levels
    def on_level(self, sub, value):
        v = int(float(value))
        self.level_vals[sub] = v
        self.draw_levels()
        self.level_labels[sub].config(text=level_text(sub, v))
        if self._lvl_guard:
            return
        self.level_touch[sub] = time.time()
        self.pending_levels[sub] = v
        self.post(self.apply_levels)

    def apply_levels(self):
        while self.pending_levels:
            try:
                sub, v = self.pending_levels.popitem()
            except KeyError:
                break
            self.send_cmd(0x14, sub, level_to_bcd(v))

    def set_level_ui(self, sub, value):
        if time.time() - self.level_touch.get(sub, 0) < 2.0:
            return
        self.level_vals[sub] = value
        self.draw_levels()
        self._lvl_guard = True
        try:
            self.level_scales[sub].set(value)
            self.level_labels[sub].config(text=level_text(sub, value))
        finally:
            self._lvl_guard = False

    # ---------------------------------------------------------- drawing
    def schedule(self, name):
        """Coalesce redraw requests: run self.<name>() once when Tk is idle."""
        if name in self._pending_draw:
            return
        self._pending_draw.add(name)

        def run():
            self._pending_draw.discard(name)
            getattr(self, name)()
        self.root.after_idle(run)

    def flash_tx(self):
        self.flash_on = not self.flash_on
        tx = self.is_tx and self.running
        self.chip_tx.set_active(tx, dim=tx and not self.flash_on)
        busy = self.rx_busy and self.running and not tx
        self.chip_busy.set_active(busy)
        high_swr = tx and self.swr_sev == 2
        border = RED if (high_swr and self.flash_on) else BG
        self.root.config(highlightbackground=border, highlightcolor=border)
        color = LCD_RED if (high_swr and self.flash_on) else LCD_TEXT
        if color != self.freq_color:
            self.freq_color = color
            self.draw_freq(force=True)
        if self.scope_on and self.running and self.scope_data and time.time() - self.scope_time > 3:
            self.scope_data = None       # data stopped arriving
            self.draw_scope()
        self.lan_check()
        self.root.after(250, self.flash_tx)

    def clock_tick(self):
        self.clock_text = datetime.now(timezone.utc).strftime("%H:%M:%S")
        self.draw_status()
        self.ptt_watchdog()
        self.root.after(1000, self.clock_tick)

    # ---- screen: top icon line
    STATUS_ORDER = ["pamp", "att", "agc", "nb", "nr", "anf", "comp", "vox", "mon", "bkin",
                    "tone", "tsql", "data", "rit", "sat", "lock"]

    def _lcd_box(self, c, x, cy, text, font, fg=LCD_TEXT, fill="", outline=None, padx=4, h=14):
        tw = font.measure(text)
        wbox = tw + 2 * px(padx)
        rrect(c, x, cy - px(h) / 2, x + wbox, cy + px(h) / 2, px(2), fill=fill,
              outline=outline if outline is not None else fg)
        c.create_text(x + wbox / 2, cy, text=text, fill=fg, font=font)
        return wbox

    def draw_status(self):
        c = self.status_canvas
        c.delete("all")
        w, h = c.winfo_width(), c.winfo_height()
        if w < 50:
            return
        cy = h / 2
        x = px(6)
        font = F["lcd_s"]
        if not self.running:
            c.create_text(x, cy, text="CI-V OFFLINE", fill=LCD_DIM, font=font, anchor="w")
        else:
            for key in self.STATUS_ORDER:
                label, _, _, vals, texts = TOGGLES[key]
                v = self.toggle_state.get(key)
                if v is None or not (key in ALWAYS_LIT or v != vals[0]):
                    continue
                text = texts[vals.index(v)] if (texts and v in vals) else label
                fg = LCD_ORANGE if key in ("att", "lock") else LCD_TEXT
                x += self._lcd_box(c, x, cy, text, font, fg=fg, outline=LCD_DIM) + px(3)
                if x > w - px(150):
                    break
            if self.scope_on:
                self._lcd_box(c, x, cy, "SCOPE", font, fg=LCD_LABEL, outline=LCD_DIM)
        xr = w - px(6)
        c.create_text(xr, cy, text=self.clock_text, fill=LCD_TEXT, font=F["lcd"], anchor="e")
        xr -= F["lcd"].measure(self.clock_text) + px(4)
        c.create_text(xr, cy, text="UTC", fill=LCD_LABEL, font=font, anchor="e")
        xr -= font.measure("UTC") + px(10)
        if self.chip_vd.active:
            col = LCD_GREEN if self.chip_vd.tone == "green" else LCD_ORANGE
            c.create_text(xr, cy, text=self.chip_vd.text, fill=col, font=F["lcd"], anchor="e")

    # ---- screen: MAIN band indicator tags
    def draw_tags(self):
        c = self.tags_canvas
        c.delete("all")
        w, h = c.winfo_width(), c.winfo_height()
        if w < 50:
            return
        cy = h / 2
        font = F["lcd_s"]
        solid_fill = {"red": LCD_RED, "green": LCD_GREEN, "amber": LCD_ORANGE, "accent": LCD_MAIN}

        def draw(t, x, right=False):
            if not t.active and t.hide_off:
                return 0
            text = t.text
            if t.solid and t.active:
                fill = solid_fill.get(t.tone, LCD_MAIN)
                if t.dim_active:
                    fill = lerp_color(fill, LCD_BG, 0.65)
                fg = "#ffffff" if t.tone in ("accent", "red") else "#000000"
                if t.dim_active:
                    fg = LCD_LABEL
                outline = fill
            elif not t.active:
                fill, fg, outline = "", LCD_DIM, LCD_DIM
            else:
                fill = ""
                fg = LCD_ORANGE if t.tone == "amber" else LCD_TEXT
                outline = LCD_ORANGE if t.tone == "amber" else LCD_LABEL
            tw = font.measure(text) + 2 * px(6)
            x0 = x - tw if right else x
            rrect(c, x0, cy - px(8), x0 + tw, cy + px(8), px(2), fill=fill, outline=outline)
            c.create_text(x0 + tw / 2, cy, text=text, fill=fg, font=font)
            return tw + px(4)

        x = px(6)
        for t in (self.chip_main, self.chip_mode, self.chip_fil, self.chip_dup, self.chip_sat, self.chip_scan):
            x += draw(t, x)
        if self.chip_band.active:
            c.create_text(x + px(4), cy, text=self.chip_band.text, fill=LCD_LABEL, font=F["lcd"], anchor="w")
            x += F["lcd"].measure(self.chip_band.text) + px(14)
        if self.running and self.cur_hz is not None:
            c.create_text(x, cy, text="VFO", fill=LCD_LABEL, font=F["lcd"], anchor="w")
        xr = w - px(4)
        for t in (self.chip_tx, self.chip_busy):
            xr -= draw(t, xr, right=True)

    # ---- screen: MAIN frequency
    def _freq_layout(self, ndig):
        """Widths of the frequency pieces for the current fonts: (MHz digit, dot, small dot, small digit)."""
        big, small = F["freq"], F["freq_s"]
        cw, sw = big.measure("8"), small.measure("8")
        dw, sdw = big.measure("."), small.measure(".")
        return cw, dw, sdw, sw, ndig * cw + 3 * cw + dw + sdw + 2 * sw

    def fit_freq_font(self, width, ndig):
        """Scale the frequency fonts so the readout spans the full screen width."""
        avail = max(200, (width - px(16)) * 0.86)      # a little inside the screen edges
        big, small = F["freq"], F["freq_s"]
        size = 40
        for _ in range(3):                 # converge: font sizes are in points, widths in pixels
            big.configure(size=size)
            small.configure(size=max(10, int(size * 0.6)))
            total = self._freq_layout(ndig)[4]
            new = max(20, min(110, int(size * avail / max(1, total))))
            if new == size:
                break
            size = new
        big.configure(size=size)
        small.configure(size=max(10, int(size * 0.6)))
        while size > 20 and self._freq_layout(ndig)[4] > avail:      # never overflow
            size -= 1
            big.configure(size=size)
            small.configure(size=max(10, int(size * 0.6)))
        h = big.metrics("ascent") + px(14)
        if abs(int(self.freq_canvas["height"]) - h) > 1:
            self.freq_canvas.configure(height=h)
            self.schedule("refit_height")

    def draw_freq(self, force=False):
        hz = self.cur_hz if self.running else None
        s = f"{hz:010d}" if hz is not None else None
        first_sig = 0
        if s:
            while first_sig < 3 and s[first_sig] == "0":
                first_sig += 1
        else:
            first_sig = 1                  # placeholder "---.---.--"
        ndig = 4 - first_sig
        w = self.freq_canvas.winfo_width()
        # Size the digits for the widest frequency this radio can show (4 MHz digits), so the
        # readout keeps the same size on every band instead of growing on low bands
        if w != getattr(self, "_freq_fit", None) and w > 50:
            self._freq_fit = w
            self.fit_freq_font(w, 4)
            force = True
        key = (hz, self.freq_color, self.hover_digit, w)
        if not force and key == self._freq_key:
            return
        self._freq_key = key
        c = self.freq_canvas
        c.delete("all")
        h = c.winfo_height()
        if w < 50:
            return
        big, small = F["freq"], F["freq_s"]
        cw, dw, sdw, sw, total = self._freq_layout(ndig)
        x = (w - total) / 2
        base = int(c["height"]) - px(12) + big.metrics("descent")     # baseline 12 px above the meter
        self.digit_hits = []
        color = self.freq_color if hz is not None else LCD_DIM

        def digit(i, font, width):
            nonlocal x
            place = 10 ** (9 - i)
            ch = s[i] if s is not None else "-"
            c.create_text(x + width / 2, base, text=ch, fill=color, font=font, anchor="s")
            if hz is not None and self.hover_digit == place:
                c.create_line(x + px(3), base - px(1), x + width - px(3), base - px(1), fill=ACCENT, width=px(3))
            self.digit_hits.append((x, x + width, place))
            x += width

        def dot(font, width):
            nonlocal x
            c.create_text(x + width / 2, base, text=".", fill=color, font=font, anchor="s")
            x += width

        for i in range(first_sig, 4):
            digit(i, big, cw)
        dot(big, dw)
        for i in range(4, 7):
            digit(i, big, cw)
        dot(small, sdw)
        x_hz = x
        for i in range(7, 9):
            digit(i, small, sw)
        # unit sits in the free space above the small 10 Hz digits
        top_small = base - small.metrics("descent") - small.metrics("ascent") * 0.78
        c.create_text((x_hz + x) / 2, top_small - px(4), text="MHz", fill=LCD_LABEL, font=F["lcd"], anchor="s")

    # ---- screen: SUB band
    def draw_sub(self):
        c = self.sub_canvas
        c.delete("all")
        w, h = c.winfo_width(), c.winfo_height()
        if w < 50:
            return
        big, small = F["sub"], F["sub_s"]
        base = h - px(5)                                   # digit baseline, kept inside this line
        cy = base - big.metrics("ascent") * 0.36           # centre of the digits, for the tags
        font = F["lcd_s"]
        tw = font.measure("SUB") + 2 * px(6)
        rrect(c, px(6), cy - px(8), px(6) + tw, cy + px(8), px(2), fill=LCD_SUB, outline=LCD_SUB)
        c.create_text(px(6) + tw / 2, cy, text="SUB", fill="#ffffff", font=font)
        x = px(10) + tw
        hz = self.sub_hz if self.running else None
        if hz is not None and self.sub_mode:
            x += self._lcd_box(c, x, cy, self.sub_mode, font, fg=LCD_LABEL, outline=LCD_DIM, padx=6, h=16) + px(6)
            b = band_of(hz)
            if b:
                c.create_text(x, cy, text=b, fill=LCD_LABEL, font=F["lcd"], anchor="w")
        if hz is None:
            main_txt, hz_txt = ("---.---" if self.running and self.sub_nak < 3 else "  "), ""
            col = LCD_DIM
        else:
            mhz = hz // 1_000_000
            main_txt = f"{mhz}.{(hz % 1_000_000) // 1000:03d}"
            hz_txt = f".{(hz % 1000) // 10:02d}"
            col = LCD_LABEL
        xr = w - px(10) - F["lcd"].measure("MHz") - px(8)
        # anchor "s" puts the bottom of the text box (baseline + descent) at y, so add each font's descent
        c.create_text(xr + px(6), base + F["lcd_s"].metrics("descent"), text="MHz", fill=LCD_DIM,
                      font=F["lcd_s"], anchor="sw")
        c.create_text(xr, base + small.metrics("descent"), text=hz_txt, fill=col, font=small, anchor="se")
        xr -= small.measure(hz_txt)
        c.create_text(xr, base + big.metrics("descent"), text=main_txt, fill=col, font=big, anchor="se")
        if self.running and self.sub_nak >= 3:
            c.create_text(w - px(10), cy, text="sub band readout not supported by the rig", fill=LCD_DIM,
                          font=F["lcd_s"], anchor="e")

    # ---- screen: AF / PWR / SQL
    def draw_levels(self, event=None):
        c = self.levels_canvas
        c.delete("all")
        w = max(c.winfo_width(), 100)
        colw = w / len(BAR_LEVELS)
        n = 20
        colors = {0x01: LCD_TEXT, 0x0A: LCD_ORANGE, 0x03: LCD_GREEN}
        # label / value widths follow the font, so nothing overlaps at 125-150 % Windows scaling
        lab_w = F["lcd_s"].measure("PWR") + px(8)
        val_w = F["lcd_s"].measure("100W") + px(10)
        for col, (sub, short, _) in enumerate(BAR_LEVELS):
            x0 = col * colw + 4
            c.create_text(x0, 10, text=short, anchor="w", fill=LCD_LABEL, font=F["lcd_s"])
            bx0 = x0 + lab_w
            bx1 = (col + 1) * colw - val_w
            seg = (bx1 - bx0) / n
            v = self.level_vals.get(sub)
            filled = 0 if v is None else int(round(v / 255 * n))
            for k in range(n):
                fill = colors[sub] if k < filled else LCD_SEG_OFF
                c.create_rectangle(bx0 + k * seg + 1, 6, bx0 + (k + 1) * seg - 1, 14, fill=fill, outline="")
            c.create_text(bx1 + 4, 10, text=level_text(sub, v), anchor="w",
                          fill=LCD_TEXT if v is not None else LCD_DIM, font=F["lcd_s"])
        c.scale("all", 0, 0, 1, SCALE)

    # ---- screen: bar meter
    def _bar(self, c, x0, bar_w, y0, y1, frac, color_fn, n=60):
        seg_w = bar_w / n
        filled = int(round(frac * n))
        for i in range(n):
            xa, xb = x0 + i * seg_w + 1, x0 + (i + 1) * seg_w - 1
            fill = color_fn((i + 0.5) / n) if i < filled else LCD_SEG_OFF
            c.create_rectangle(xa, y0, xb, y1, fill=fill, outline="")

    def draw_meter(self, event=None):
        c = self.meter_canvas
        c.delete("all")
        w = max(c.winfo_width(), 100)
        x0, x1 = px(40), w - px(22)
        bar_w = x1 - x0
        sf = F["lcd_s"]
        if self.meter_mode == "tx":
            c.create_text(px(10), 20, text="Po", anchor="w", fill=LCD_TEXT, font=F["lcd"])
            for label, raw in PWR_TICKS:
                x = x0 + (raw / METER_MAX) * bar_w
                c.create_line(x, 11, x, 14, fill=LCD_LABEL)
                c.create_text(x, 0, text=label, anchor="n", fill=LCD_TEXT, font=sf)
            split = S9_RAW / METER_MAX
            self._bar(c, x0, bar_w, 15, 24, self.pwr_frac, lambda t: LCD_SBLUE if t <= split else LCD_RED)
            c.create_text(px(10), 38, text="SWR", anchor="w", fill=LCD_TEXT, font=F["lcd"])
            limit = 120 / METER_MAX
            self._bar(c, x0, bar_w, 33, 42, self.meter_frac,
                      lambda t: LCD_SBLUE if t <= limit else LCD_RED)
            for label, raw in SWR_TICKS:
                x = x0 + (raw / METER_MAX) * bar_w
                c.create_line(x, 43, x, 46, fill=LCD_LABEL)
                c.create_text(x, 46, text=label, anchor="n", fill=LCD_RED if raw > 120 else LCD_TEXT, font=sf)
        else:
            c.create_text(px(12), 26, text="S", anchor="w", fill=LCD_TEXT, font=F["ui_b"])
            for label, raw in S_TICKS:
                x = x0 + (raw / METER_MAX) * bar_w
                col = LCD_RED if raw > S9_RAW else LCD_TEXT
                c.create_line(x, 12, x, 16, fill=col)
                c.create_text(x, 0, text=label if raw < 241 else "+60dB", anchor="n", fill=col, font=sf)
            # red line under the over-S9 part of the scale, as on Icom meters
            xs9 = x0 + (S9_RAW / METER_MAX) * bar_w
            c.create_line(x0, 16, xs9, 16, fill=LCD_LABEL)
            c.create_line(xs9, 16, x1, 16, fill=LCD_RED, width=2)
            s9 = S9_RAW / METER_MAX
            self._bar(c, x0, bar_w, 19, 33, self.meter_frac,
                      lambda t: LCD_SBLUE if t <= s9 else LCD_RED)
            if self.peak_frac > 0:
                n = 60
                seg_w = bar_w / n
                i = min(int(self.peak_frac * n), n - 1)
                xa = x0 + i * seg_w + 1
                c.create_rectangle(xa, 18, xa + max(2, seg_w - 2), 34, fill=LCD_ORANGE, outline="")
            # Po scale underneath (dim on receive), like the radio's dual-scale meter
            for label, raw in PWR_TICKS:
                x = x0 + (raw / METER_MAX) * bar_w
                c.create_line(x, 36, x, 39, fill=LCD_DIM)
                c.create_text(x, 40, text=label, anchor="n", fill=LCD_DIM, font=sf)
            c.create_text(px(10), 45, text="Po", anchor="w", fill=LCD_DIM, font=sf)
        c.scale("all", 0, 0, 1, SCALE)

    # ---- screen: spectrum scope + waterfall
    def draw_scope(self, rebuild=False):
        c = self.scope_canvas
        if not self.scope_visible:
            return
        w, h = c.winfo_width(), c.winfo_height()
        if w < 50:
            return
        spec_h = int(h * 0.5)
        wf_h = h - spec_h - px(12)
        c.delete("all")
        c.create_rectangle(0, 0, w, spec_h, fill="#00040e", outline="")
        for k in range(1, 10):
            x = w * k / 10
            c.create_line(x, 0, x, spec_h, fill="#0b1a33" if k != 5 else "#163057")
        for k in range(1, 4):
            y = spec_h * k / 4
            c.create_line(0, y, w, y, fill="#0b1a33")
        mid = spec_h / 2
        if not self.scope_on:
            c.create_text(w / 2, mid, text="SCOPE OFF  -  press the SCOPE key", fill=LCD_DIM, font=F["lcd"])
        elif not self.running:
            c.create_text(w / 2, mid, text="SCOPE  -  not connected", fill=LCD_DIM, font=F["lcd"])
        elif not self.scope_data:
            msg = "Waiting for scope data ..."
            if self.lan_mode():
                msg = "Scope over the network  -  " + (self.lan_text or "connecting ...")
            elif self.baud < 115200:
                msg += "  (set CI-V USB baud 115200 for a smooth scope)"
            c.create_text(w / 2, mid, text=msg, fill=LCD_LABEL, font=F["lcd_s"])
        else:
            lo, hi, data = self.scope_data
            pts = [0, spec_h]
            vals = self._resample(data, int(w))
            for xi, v in enumerate(vals):
                pts += [xi, spec_h - 1 - (min(v, 160) / 160) * (spec_h - 4)]
            pts += [w, spec_h]
            c.create_polygon(pts, fill="#123b8f", outline="")
            c.create_line(pts[2:-2], fill="#dce9ff")
            mhz = self.scope_marker_hz()
            if mhz and hi > lo and lo <= mhz <= hi:
                xm = (mhz - lo) / (hi - lo) * w
                c.create_line(xm, 0, xm, spec_h, fill=LCD_RED)
                c.create_polygon(xm - px(4), 0, xm + px(4), 0, xm, px(5), fill=LCD_RED, outline="")
            span = (hi - lo) / 2
            c.create_text(px(4), px(2), text=f"±{span / 1000:g}k" if span < 1e6 else f"±{span / 1e6:g}M",
                          fill=LCD_LABEL, font=F["lcd_s"], anchor="nw")
        # waterfall
        if rebuild or self.wf_img is None or self.wf_img.width() != int(w) or self.wf_img.height() != wf_h:
            self.wf_img = tk.PhotoImage(width=int(w), height=max(1, wf_h))
            self.wf_cache = deque((self._wf_row(d, int(w)) for d in self.wf_rows), maxlen=self.wf_rows.maxlen)
            self._wf_put()
        c.create_image(0, spec_h, image=self.wf_img, anchor="nw")
        span = self.scope_span if (self.scope_on and self.running) else None
        mhz = self.scope_marker_hz()
        if span and mhz and span[1] > span[0] and span[0] <= mhz <= span[1]:
            xm = (mhz - span[0]) / (span[1] - span[0]) * w                  # receive passband on the waterfall
            c.create_line(xm, spec_h, xm, spec_h + wf_h, fill=LCD_RED, width=max(1, px(1)))
        hx = self.scope_hover_x
        if span and hx is not None and 0 <= hx <= w:                      # mouse cursor + its frequency
            c.create_line(hx, 0, hx, spec_h + wf_h, fill="#ffe14d")
            text = f"{self.scope_hz_at(hx) / 1e6:.4f}"
            tw = F["lcd_s"].measure(text) + px(8)
            tx = min(max(hx - tw / 2, 0), w - tw)
            c.create_rectangle(tx, spec_h - px(15), tx + tw, spec_h - px(1), fill="#000000", outline="#ffe14d")
            c.create_text(tx + tw / 2, spec_h - px(8), text=text, fill="#ffe14d", font=F["lcd_s"])
        # frequency labels under the waterfall
        yb = h - px(1)
        if self.scope_data and self.scope_on:
            lo, hi, _ = self.scope_data
            c.create_text(px(4), yb, text=hz_to_mhz(lo)[:-2], fill=LCD_LABEL, font=F["lcd_s"], anchor="sw")
            c.create_text(w / 2, yb, text=hz_to_mhz((lo + hi) // 2)[:-2], fill=LCD_LABEL, font=F["lcd_s"],
                          anchor="s")
            c.create_text(w - px(4), yb, text=hz_to_mhz(hi)[:-2], fill=LCD_LABEL, font=F["lcd_s"], anchor="se")

    @staticmethod
    def _resample(data, w):
        n = len(data)
        if n == 0 or w <= 0:
            return []
        if n >= w:
            return [max(data[i * n // w:max(i * n // w + 1, (i + 1) * n // w)]) for i in range(w)]
        return [data[min(n - 1, i * n // w)] for i in range(w)]

    def _wf_row(self, data, w):
        return "{" + " ".join(WF_PALETTE[min(160, v)] for v in self._resample(data, w)) + "}"

    def _wf_put(self):
        img = self.wf_img
        if img is None:
            return
        rows = list(self.wf_cache)[:img.height()]
        if rows:
            try:
                img.put(" ".join(rows), to=(0, 0))
            except tk.TclError:
                pass

    def scope_update(self, lo, hi, data, centre=False):
        if not self.scope_on or not self.running:
            return
        self.scope_data = (lo, hi, data)
        self.scope_span = (lo, hi)
        self.scope_centre = bool(centre)
        span = (hi - lo) // 2
        if self.span_set and (span == self.span_set or time.time() - self.span_time > 2):
            self.span_set = None
        if not self.span_set:
            self.btn_span.set_text(span_text(span) if centre else "SPAN")
        # In centre mode the radio centres the receive passband, not the dial frequency
        # (USB: ~1.5 kHz above it). Remember that offset once the dial has settled.
        if centre and self.cur_hz and time.time() - self.tune_time > 1.0:
            off = (lo + hi) // 2 - int(self.cur_hz)
            self.scope_offset = off if abs(off) <= 10_000 else 0
        elif not centre:
            self.scope_offset = 0
        self.scope_time = time.time()
        self.web_scope_seq += 1
        self.wf_rows.appendleft(data)
        if self.wf_img is not None and self.scope_visible:
            self.wf_cache.appendleft(self._wf_row(data, self.wf_img.width()))
            self._wf_put()
        self.draw_scope()

    def scope_hz_at(self, x):
        """Frequency under canvas x (scope and waterfall share the same span), snapped for the mode."""
        lo, hi = self.scope_span
        w = max(1, self.scope_canvas.winfo_width())
        hz = lo + max(0.0, min(1.0, x / w)) * (hi - lo)
        snap = self.step_hz() if self.cur_mode in ("FM", "DV", None) else min(self.step_hz(), 100)
        return int(round(hz / snap) * snap)

    def cur_span(self):
        """Current scope span (+/- Hz) from the radio's waveform, or None."""
        if not self.scope_span:
            return None
        return (self.scope_span[1] - self.scope_span[0]) // 2

    def step_span(self, direction, wrap=False):
        """SPAN key: next wider (+1) / narrower (-1) span; wrap=True cycles round. Turns the scope on."""
        if not self.running:
            return
        if not self.scope_on:
            self.toggle_scope()
        cur = self.span_set or self.cur_span() or SCOPE_SPANS[1]
        idx = min(range(len(SCOPE_SPANS)), key=lambda i: abs(SCOPE_SPANS[i] - cur))
        n = len(SCOPE_SPANS)
        new = SCOPE_SPANS[(idx + direction) % n if wrap else max(0, min(n - 1, idx + direction))]
        self.span_set, self.span_time = new, time.time()
        self.btn_span.set_text(span_text(new))
        self.web_span = new

        def job():
            self.send_cmd(0x27, 0x14, [0x00, 0x00])                      # span only applies in centre mode
            self.send_cmd(0x1A, 0x05, [0x01, 0x89, 0x01])                # dial frequency in the centre
            f = self.send_cmd(0x27, 0x15, [0x00] + freq_to_bcd(new))
            if f is not None and f[4] == NAK:
                self.ui(self.flash_status, "RIG REJECTED THE SPAN SETTING (27 15)", RED)
        self.post(job)
        self.flash_status(f"SCOPE SPAN {span_text(new)}", ACCENT, 2)

    def scope_marker_hz(self):
        """Where the red marker goes: the receive passband (scope centre in centre mode), else the dial."""
        if not self.cur_hz:
            return None
        return int(self.cur_hz) + (self.scope_offset if self.scope_centre else 0)

    def scope_click(self, e):
        """Click (or drag) on the spectrum or the waterfall: bring that signal under the red marker."""
        if not self.scope_span or not self.running or not self.scope_on:
            return
        if self.scope_span[1] <= self.scope_span[0]:
            return
        hz = self.scope_hz_at(e.x) - (self.scope_offset if self.scope_centre else 0)
        snap = self.step_hz() if self.cur_mode in ("FM", "DV", None) else min(self.step_hz(), 100)
        hz = int(round(hz / snap) * snap)
        if hz != self.cur_hz:
            self.request_frequency(hz)
        self.scope_hover_x = e.x
        self.draw_scope()

    def scope_hover(self, e):
        x = e.x if e is not None else None
        if x != self.scope_hover_x:
            self.scope_hover_x = x
            if self.scope_span:
                self.draw_scope()

    def toggle_scope(self):
        self.scope_on = not self.scope_on
        self.config["scope_on"] = self.scope_on
        self.btn_scope.set_active(self.scope_on)
        if self.scope_on and not self.scope_visible:
            self.show_scope_panel(True)
        self.scope_data = None
        self.scope_span = None
        self.wf_rows.clear()
        if hasattr(self, "wf_cache"):
            self.wf_cache.clear()
        if self.wf_img is not None:
            self.wf_img.blank()
        if self.running:
            self.post(lambda: self.scope_output(self.scope_on, report=True))
        self.draw_scope()
        self.draw_status()

    # ---- spectrum scope over the network (Icom LAN)
    def lan_mode(self):
        """Scope over the network chosen in Settings?"""
        return bool(self.config.get("lan_scope") and self.config.get("lan_ip"))

    def lan_open(self):
        lan = self.lan
        return lan is not None and lan.is_open

    def _civ_frame(self, cmd, sub, data=()):
        return bytes([START_BYTE, START_BYTE, self.radio_addr, CONTR_ADDR, cmd, sub] + list(data) + [STOP_BYTE])

    def lan_check(self):
        """Start / stop / watch the network scope link (Tk thread, 4x a second)."""
        want = self.lan_mode() and self.scope_on and self.running
        lan = self.lan
        if not want:
            if lan is not None:
                self.stop_lan()
            return
        now = time.time()
        if lan is None or not lan.alive:
            if lan is not None and lan.fatal:
                return                              # wrong password etc.: wait for new settings
            if now >= self.lan_retry:
                self.start_lan()
            return
        if lan.is_open and now - self.scope_time > 4 and now - self.lan_kick > 4:
            self.lan_kick = now                     # no waveform for a while: ask again
            self.lan_scope_on(lan)

    def start_lan(self):
        self.lan_retry = time.time() + 10
        self.lan_buf = bytearray()
        self.lan_text = "connecting ..."
        lan = LanLink(self.config["lan_ip"], self.config.get("lan_port", LAN_DEFAULT_PORT),
                      self.config.get("lan_user", ""), self.config.get("lan_pass", ""), None, None)
        lan.on_civ = lambda data, l=lan: self.lan_civ(l, data)
        lan.on_status = lambda t, c, o, l=lan: self.ui(self.lan_status, l, t, c, o)
        self.lan = lan
        lan.start()

    def stop_lan(self):
        lan, self.lan = self.lan, None
        if lan is None:
            return
        if lan.is_open:
            lan.send_civ(self._civ_frame(0x27, 0x11, [0x00]))      # stop the waveform before leaving
            time.sleep(0.15)
        lan.stop(wait=True)
        self.lan_text = ""
        self.update_port_label()

    def lan_scope_on(self, lan):
        lan.send_civ(self._civ_frame(0x27, 0x10, [0x01]))          # scope display on
        lan.send_civ(self._civ_frame(0x27, 0x14, [0x00, 0x00]))    # centre mode: tuned frequency in the middle
        lan.send_civ(self._civ_frame(0x1A, 0x05, [0x01, 0x89, 0x01]))  # carrier point centre
        lan.send_civ(self._civ_frame(0x27, 0x11, [0x01]))          # waveform data out (to the network)

    def lan_civ(self, lan, data):                  # network thread
        if lan is not self.lan:
            return
        self.lan_buf += data
        for f in _extract_civ(self.lan_buf):
            self.handle_frame(f)

    def lan_status(self, lan, text, colour, opened):
        if lan is not self.lan:
            return
        self.lan_text = text[5:] if text.startswith("LAN: ") else text
        if opened:
            self.lan_kick = time.time()
            self.lan_scope_on(lan)
        self.flash_status(("SCOPE " + text).upper(), colour, 6)
        self.update_port_label()
        if not self.scope_data:
            self.draw_scope()

    def scope_output(self, on, report=False):     # polling thread
        if self.lan_mode():
            # the network link carries the waveform: keep the USB CI-V port free of scope data
            if on:
                self.send_cmd(0x27, 0x10, [0x01])
                self.send_cmd(0x27, 0x14, [0x00, 0x00])     # main band: centre mode
                self.send_cmd(0x1A, 0x05, [0x01, 0x89, 0x01])  # CENTER Type Display = carrier point (dial in the middle)
            self.send_cmd(0x27, 0x11, [0x00])
            return
        if on:
            self.send_cmd(0x27, 0x10, [0x01])           # scope display ON
            self.send_cmd(0x27, 0x14, [0x00, 0x00])     # main band: centre mode (tuned frequency in the middle)
            self.send_cmd(0x1A, 0x05, [0x01, 0x89, 0x01])  # CENTER Type Display = carrier point, not filter centre
        f = self.send_cmd(0x27, 0x11, [0x01 if on else 0x00])   # waveform data output ON/OFF
        if report and on:
            if f is None:
                self.ui(self.flash_status, "SCOPE: NO REPLY FROM RIG", ORANGE)
            elif f[4] == NAK:
                self.ui(self.flash_status, "RIG REJECTED SCOPE DATA OUTPUT (27 11)", RED)
            elif self.baud < 115200:
                self.ui(self.flash_status, "SCOPE ON - for a smooth display set CI-V USB baud to 115200", AMBER, 6)

    def show_scope_panel(self, show):
        self.scope_visible = bool(show)
        self.config["scope_visible"] = self.scope_visible
        if hasattr(self, "scope_visible_var"):
            self.scope_visible_var.set(self.scope_visible)
        if show:
            self.scope_canvas.pack(fill="x", padx=px(4), pady=(px(2), 0), before=self.tab_btns[TABS[0]].master)
        else:
            self.scope_canvas.pack_forget()
        self.refit_height()

    def refit_height(self):
        if self.root.state() != "normal":
            return                    # maximised / minimised: leave the size to Windows (keeps the normal size)
        self.root.update_idletasks()
        h = self.root.winfo_reqheight()
        dw = self.design_width()
        w = self.root.winfo_width() if self.root.winfo_width() > 100 else dw
        w = max(w, dw)
        self.root.minsize(dw, h)
        self.root.geometry(f"{w}x{h}")


def set_dpi_awareness():
    """System DPI aware, the same whether run as IC9700.py or as the installed .exe."""
    if sys.platform != "win32":
        return
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)   # crisp text on high-DPI screens
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass


def dpi_mode():
    if sys.platform != "win32":
        return "n/a"
    try:
        import ctypes
        v = ctypes.c_int()
        ctypes.windll.shcore.GetProcessDpiAwareness(None, ctypes.byref(v))
        return {0: "unaware", 1: "system", 2: "per-monitor"}.get(v.value, str(v.value))
    except Exception:
        return "?"


if __name__ == "__main__":
    set_dpi_awareness()
    root = tk.Tk()
    app = IC9700Controller(root)
    root.mainloop()
