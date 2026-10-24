# Scope over Ethernet

The spectrum scope can come from the IC-9700's LAN port, which carries waveform data much faster than USB CI-V. Tuning, meters, PTT and everything else stay on USB.

## Radio

MENU > SET > Network:

1. **Network Control**: ON.
2. **Network User1**: set an ID and password.
3. Note the **IP address**. A fixed address, or a reservation on your router, stops it changing.

## Program

**Settings > Settings…**, section "Scope over the network":

1. Tick **Get the spectrum scope over Ethernet**.
2. Enter the radio's **IP address**. Leave the port at **50001**.
3. Enter the **network user ID** and **password** from the radio.
4. **Save & connect**, then press **SCOPE**.

When it connects, the status bar shows "SCOPE LAN: CONNECTED" and the bottom bar shows "SCOPE LAN". Untick the box to go back to the USB scope.

The radio accepts one network user at a time, so close RS-BA1, wfview or any other network program first.

## How it works

The program uses the same UDP protocol as RS-BA1 and wfview: it logs in on the control port (50001), opens the radio's CI-V stream (50002), asks for scope waveform data on that stream and draws it. Audio over the network is not used.

## Messages

| Message | Meaning |
| --- | --- |
| SCOPE LAN: CONNECTED | Working |
| no reply from <ip>:50001 | Wrong IP, radio off the network, or Network Control is off |
| the radio rejected the user name / password | Check Network User1 ID and password on the radio |
| the radio refused the stream | Another program (RS-BA1, wfview) is connected |
| logged in, but the radio didn't open its CI-V stream | Restart the radio's network: Network Control off and on |
