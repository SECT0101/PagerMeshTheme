#!/usr/bin/env bash
# Rebuild the MESH.5 theme (and optionally the logos) from scratch.
#   tools/mesh5/build.sh /path/to/wifipineapplepager-themes [--logo]
# Needs python3 + pillow + numpy, jq, a clone of hak5/wifipineapplepager-themes,
# and these SIL OFL fonts from github.com/google/fonts saved in ./fonts:
#   ofl/sharetechmono/ShareTechMono-Regular.ttf   ofl/sharetech/ShareTech-Regular.ttf
#   ofl/blackopsone/BlackOpsOne-Regular.ttf       ofl/sairacondensed/SairaCondensed-Black.ttf
#   ofl/vt323/VT323-Regular.ttf                   ofl/orbitron/Orbitron[wght].ttf (save as Orbitron%5Bwght%5D.ttf)
# Color scheme: MESH5_SCHEME=mesh (default) | cyan | nvg | coyote | white
set -euo pipefail
cd "$(dirname "$0")"
THEMES="${1:?path to wifipineapplepager-themes clone}"
OUT=../../themes/mesh5
export MESH5_FONTS=fonts MESH5_MASCOT=meshpine.png MESH5_WORDMARK=wordmark.png
python3 - <<'PY'
from brand import wordmark
import character3d
wordmark("blackops", 300, "woodland", seed=8, outline=(200, 194, 172)).save("wordmark.png")
character3d.render("helmet", "od").save("meshpine.png")
PY
KEEP=$(mktemp -d); cp -r "$OUT/README.md" "$OUT/preview" "$KEEP/" 2>/dev/null || true
python3 build_mesh5.py "$THEMES/themes/wargames" "$OUT" fonts
python3 post_json.py "$OUT"
bash "$THEMES/tools/generate_color_palette.sh" "$OUT/theme.json" > "$OUT/color_palette_preview.html"
cp -r "$KEEP"/* "$OUT/" 2>/dev/null || true
python3 selector.py "$OUT"
python3 icons.py "$OUT"
python3 validate.py "$OUT" "$THEMES/themes/wargames"
python3 preview.py "$OUT/preview"
rm -f wordmark.png meshpine.png
if [[ "${2:-}" == "--logo" ]]; then python3 logo3d.py ../../art/mesh5/mesh5_lora_mesh_edition_shield.png; python3 planet_logos.py ../../art/mesh5; fi
