# MESH.5 Ringtones

**Author:** SECT0101
**Version:** 1.0.0

Eight ringtones to go with the MESH.5 theme, built from LoRa radio sounds: rising chirps like a LoRa transmission, packets repeating as they hop across the mesh, and packet collisions. Most of them end with the same three-hit **MESH . 5** sting (two low hits and a fifth), and two send Morse code like a radio operator.

| Slot | File | What you hear |
|---|---|---|
| Boot | `MESH5_Boot.rtttl` | LoRa chirp, Morse **M-E-S-H**, the riff, the sting |
| Alert | `MESH5_Alert.rtttl` | Two packet chirps, the hop echo, the sting |
| Payload Complete | `MESH5_Payload_Complete.rtttl` | Chirp up, the sting resolving up |
| Error | `MESH5_Error.rtttl` | Packet collision, then a chirp falling to the floor |
| Battery Low | `MESH5_Battery_Low.rtttl` | Slow beacon pings stepping down |
| Battery Critical | `MESH5_Battery_Critical.rtttl` | Collision buzz, Morse **SOS**, the sting |
| Power Connected | `MESH5_Power_Connected.rtttl` | Quick chirp up to a high lock tone |
| Power Disconnected | `MESH5_Power_Disconnected.rtttl` | Chirp down, link lost |

## Install

1. Copy the `.rtttl` files to `/root/ringtones/` on the Pager. In the Pager web UI that is **Files > /mmc/root > ringtones > Upload**, or from a terminal:
   `scp MESH5_*.rtttl root@172.16.52.1:/root/ringtones/`
2. On the Pager, assign each file to its slot in the ringtone settings.

Each file holds only the RTTTL line, with no trailing newline, as Hak5's ringtone repo expects.

## Credits

All melodies are original.

Unofficial community ringtones. Not affiliated with Hak5 LLC or Meshtastic LLC.
