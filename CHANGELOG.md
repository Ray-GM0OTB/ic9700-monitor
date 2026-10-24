# Changelog

## Version 3.28 – first public release

### Desktop program
- Display modelled on the IC-9700's screen: large frequency readout (mouse wheel over a digit tunes that digit), MAIN and SUB bands, band / mode / filter tags.
- S-meter blue up to S9 and red above, with peak hold; TX meter with Po, SWR, ALC, COMP and Id, also blue then red.
- POWER key switches the radio on and off over CI-V, including switching on from standby.
- Spectrum scope and waterfall with the tuned frequency in the centre; click or drag to tune; SPAN key cycling ±2.5 kHz to ±500 kHz.
- Optional scope over Ethernet from the radio's LAN port, with everything else on USB.
- Modes, filters, 15 level sliders, P.AMP, ATT, AGC, NB, NR, ANF, lock, split, duplex, CTCSS, satellite mode, RIT, CW keyer with macros.
- Memories read from the radio, CSV import / export, scanner with a band-activity plot.
- QSO log with dupe check, ADIF and CSV export.
- Window keeps its size through maximise / restore; View > Reset window size.

### Phone
- Password-protected phone page over Tailscale with HTTPS: display, scope, all controls, radio audio and TALK.
- Lite phone page for clear audio and quick PTT: one connection for audio, display and commands; adaptive jitter buffer; PTT keyed straight from the phone's connection; phone voice processing switched off and checked.
- Lite page controls: power, frequency keypad and step, BAND, MODE, S / Po meter, RF power, SQL, RF gain, P.AMP, memories, memory scan.
- Remote power on / off from the phone.

### Apps and builds
- Windows setup program built with `build_installer.bat`.
- Android apps *IC-9700* and *IC-9700 Lite*, built with `build_apk.bat` and `build_apk_lite.bat`.
- *Connector X-Ref*, an offline Android app for circular connector part numbers, built with `build_connector_apk.bat`.
