# Phone page

IC9700 Monitor has a built-in, password-protected web page. Open it on a phone to see the display and scope, tune and change settings, hear the radio and talk through it. Nothing extra needs installing on the PC except Tailscale, and `sounddevice` for audio.

For a cut-down page tuned for audio quality and fast PTT, see the [Lite page](lite-page.md).

<p>
<img src="../screenshots/phone-tune.png" width="240" alt="TUNE tab with scope">
<img src="../screenshots/phone-func.png" width="240" alt="FUNC tab">
</p>

## Setting up (once)

1. Install [Tailscale](https://tailscale.com/) on the PC and the phone, and sign both in to the same account. This lets the phone reach the PC from anywhere, privately.
2. On the PC: **Phone > Phone access, audio (RX / TX) & HTTPS…**
   - Tick **Allow access from my phone / browser**.
   - Choose a **password** (6 characters or more). The page runs on port **8073**.
   - Choose the radio's USB audio for **Receive audio from** and **Transmit audio to** (or leave on Auto).
   - **Save**.
3. Click **Turn on HTTPS**. This gets a certificate for the PC from Tailscale and starts the secure page on port **8074**, at an address like `https://your-pc.tailnet-name.ts.net:8074/`. Use this address: phones only allow the microphone on https pages.
4. On the radio: SET > Connectors > MOD Input > **DATA OFF MOD = USB** (and DATA MOD = USB if you use data modes), so the phone's voice reaches the transmitter.
5. Open the https address on the phone and sign in. The phone stays signed in.

Audio needs one Python package on the PC: `py -m pip install sounddevice`. The installed program already includes it.

## What's on the page

| Tab | Contents |
| --- | --- |
| (top) | Power ⏻ ON/OFF, connection, frequency, S/Po meter, spectrum scope (tap to tune) |
| TUNE | Band, frequency entry and step, mode and filter, Main/Sub swap, SCOPE and SPAN |
| FUNC | P.AMP, ATT, AGC, NB, NR, ANF and other functions; duplex / split; repeater tone (CTCSS); RIT; CW decoder (ON / OFF, sensitivity, decoded text, CLEAR) |
| LEVELS | The level sliders |
| MEMORY | Memory channels: tap to recall |
| AUDIO | Receive (audio on/off, volume, squelch muting) and Transmit (mic gain, TX tone, hold or tap mode, voice processing); install as an app |

**TALK** keys the radio and sends your voice. Hold it to talk, or switch to tap-on/tap-off on the AUDIO tab.

## Safety

- PTT drops if the phone's microphone audio stops for 1.5 s or the connection is lost.
- The PC's PTT time-out also applies.
- Switching the radio off from the phone asks for confirmation.
- Commands are only accepted from the page itself, after sign-in. Changing the password signs every phone out.

## Install as an app

On the https page, Chrome on Android offers **⋮ > Install app**, and iPhone Safari offers Share > **Add to Home Screen**. Or build the proper Android app: see [Android apps](android-apps.md).

## Remote power

The phone's ⏻ key switches the radio on and off through the PC. For this to work, the PC must be on with IC9700 Monitor running, the USB cable connected, and the radio's DC supply on.
