# MESH.5 build tools

Scripts that draw every MESH.5 image on top of Hak5's `wargames` reference theme: the theme art, the MESH.5 wordmark, the 3D Tac-Pine mesh operator and the LoRa Mesh Edition shield.

```
git clone https://github.com/hak5/wifipineapplepager-themes
tools/mesh5/build.sh /path/to/wifipineapplepager-themes          # rebuild themes/mesh5
tools/mesh5/build.sh /path/to/wifipineapplepager-themes --logo   # also rebuild the art/mesh5 logos
```

Needs python3 with pillow and numpy, jq, and the SIL OFL fonts listed at the top of `build.sh` saved in `tools/mesh5/fonts/`.
`MESH5_SCHEME` picks the color scheme: `mesh` (default, Meshtastic green), `cyan`, `nvg`, `coyote` or `white`.

| Script | What it does |
|---|---|
| `build_mesh5.py` | Draws the theme images (same names and sizes as `wargames`) |
| `post_json.py` | Palette, dashboard and boot-frame JSON changes |
| `brand.py` | Camo patterns and the MESH.5 wordmark |
| `character.py`, `character3d.py`, `shade.py` | Tac-Pine geometry and 3D lighting |
| `meshart.py` | The shield art: Tac-Pine bust with a LoRa whip, mesh nodes and signal arcs |
| `logo.py`, `logo3d.py` | The shield outline and the MESH.5 LoRa Mesh Edition shield |
| `selector.py` | The small shield menu cursors (`payloads_dashboard/arrow.png`, `alerts_dashboard/sub.png`) |
| `icons.py` | Repaints the home-menu icons Meshtastic green (the stock files are magenta) |
| `planet.py` | MESH THE PLANET! slogan, glitch color split and the meshed globe (Natural Earth coastlines in `data/`) |
| `planet_logos.py` | The MESH THE PLANET! tab, shield and patch (`art/mesh5/`) |
| `validate.py` | Checks JSON, referenced assets and image sizes |
| `preview.py` | Renders the README preview screenshots |
