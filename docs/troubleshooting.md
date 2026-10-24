# Troubleshooting

Most problems show up as a message in the program's status bar.

## Connection and radio

| Message or symptom | What to do |
| --- | --- |
| PORT OPEN BUT NO REPLY FROM RIG | Radio off, or the baud rate / CI-V address differs from the radio: check MENU > SET > Connectors > CI-V |
| No COM port for the radio | Install the Icom USB driver |
| RADIO SWITCHED OFF | Press **POWER** to switch it on |
| Power on does nothing | The USB cable must be connected and the radio's DC supply on |
| "Waiting for scope data…" | Set CI-V USB Baud Rate to 115200 on the radio and in Settings, or use the [scope over Ethernet](scope-over-lan.md) |
| RIG REJECTED THE SPAN SETTING | The radio refused that span; try another |
| Window the wrong size | **View > Reset window size** |

## Scope over Ethernet

| Message | What to do |
| --- | --- |
| no reply from the IP | Check the IP address and Network Control = ON |
| rejected the user name / password | Re-enter Network User1 ID and password from the radio |
| refused the stream | Close RS-BA1, wfview or any other network program |

## Phone

| Symptom | What to do |
| --- | --- |
| Page can't be reached | IC9700 Monitor running on the PC; Tailscale connected on both PC and phone |
| TALK / microphone doesn't work | Use the **https** address (port 8074), not http |
| "Access is denied" turning on HTTPS | Use version 3.12 or later (files moved to AppData) |
| Voice sounds muffled or pumping | Use the [Lite page](lite-page.md); ⚙ shows whether the phone's voice processing is off |
| Phone audio is silent | Radio: SET > Connectors > USB AF/IF Output = AF; PC: choose the radio's USB audio in Phone access |
| Nothing transmitted from the phone | Radio: SET > Connectors > MOD Input > DATA OFF MOD = USB |
| Lite page shows dropouts | A weak mobile link; the buffer grows by itself. Wi-Fi or a better signal helps. |

## Builds

| Build | If it stops |
| --- | --- |
| Windows installer | See [Windows installer](windows-installer.md#if-the-build-stops) |
| Android apps | Look in `build_apk_log.txt` next to the script |
| Connector X-Ref | Look in `build_html_apk_log.txt` |
| "aapt2 not found" / "still incomplete" | Antivirus may be removing the Android tools: allow `%LOCALAPPDATA%\IC9700AndroidSDK` and build again |
