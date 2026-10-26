# Changelog

## Version 3.30

### Look
- Level sliders have red LED-style knobs that glow brighter the higher the value (PBT sliders: the further from centre). They replace the silver knobs; a knob stays grey until the radio has reported its level.

### CW decoder
- Decodes CW from the radio's USB receive audio: **CW tab > CW DECODER**, or **View > CW decoder…**. Also on the phone page: **FUNC tab > CW decoder**.
- **Sensitivity:** Auto, Low, Normal, High or Max. High and Max listen through a narrower filter matched to the sending speed and accept weaker signals. Auto runs at the most sensitive level and backs off by itself while it sees static.
- Finds the CW tone by itself (300–1200 Hz), or follows the rig's CW pitch setting.
- Follows the sending speed (about 5–50 WPM) and the signal level automatically.
- Rejects static crashes, and doesn't print a lone E or T caused by one; stays quiet on plain noise.
- Shows prosigns such as <AR>, <SK> and <KN>; characters it can't read show as `*`.
