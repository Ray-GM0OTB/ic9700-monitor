# CI-V commands used

IC9700 Monitor talks to the radio with Icom CI-V: radio address A2 (default), controller address E0. Commands are taken from the [IC-9700 CI-V reference](https://www.rigpix.com/icom/ic9700_civ_v2.pdf).

| Command | Purpose |
| --- | --- |
| 03 / 05 | Read / set frequency |
| 04 / 06 | Read / set mode and filter |
| 0F | Duplex / split |
| 11 | Attenuator |
| 14 xx | Levels (AF 01, RF 02, SQL 03, NR 06, PBT 07/08, CW pitch 09, RF power 0A, mic 0B, key speed 0C, COMP 0E, NB 12, monitor 15, VOX 16, anti-VOX 17) |
| 15 xx | Meters (squelch 01, S 02, Po 11, SWR 12, ALC 13, COMP 14, Vd 15, Id 16) |
| 16 xx | Functions (preamp 02, AGC 12, NB 22, NR 40, ANF 41, tone 42, TSQL 43, COMP 44, MON 45, VOX 46, BK-IN 47, lock 50, satellite 5A) |
| 18 00 / 18 01 | Power off / on (on is preceded by a run of FE wake-up bytes sized to the baud rate) |
| 1A 00 | Read memory channels |
| 1A 05 01 89 01 | Scope: CENTER Type Display = carrier point center |
| 1B | CTCSS tone frequency |
| 1C 00 | PTT |
| 21 | RIT |
| 25 / 26 | SUB band frequency and mode |
| 27 00 | Scope waveform data |
| 27 10 / 27 11 | Scope on / waveform output on |
| 27 14 00 00 | Scope centre mode, main band |
| 27 15 | Scope span |

## Network (scope over Ethernet)

The [scope over Ethernet](scope-over-lan.md) uses the Icom LAN protocol, as RS-BA1 and wfview do: UDP 50001 for control and login, 50002 for the CI-V stream. Audio (50003) is opened as the protocol requires but not used.

## Phone link

The phone pages use HTTP(S) on ports 8073 / 8074 and one WebSocket (`/api/audio`) for audio. The lite page also sends its display state and commands over that WebSocket. Audio is 16 kHz, 8-bit µ-law each way.
