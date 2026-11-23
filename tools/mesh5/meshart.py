#!/usr/bin/env python3
"""Shield art shared with the PagerMesh logo: Tac-Pine bust with a LoRa whip antenna,
mesh nodes and signal arcs in Meshtastic green."""
from PIL import Image, ImageDraw, ImageFilter
import character3d

GREEN, DARK = (103, 234, 148), (28, 30, 28)


def mesh_art():
    bust = character3d.render("bust", "od")
    bust = bust.crop((0, 0, bust.size[0], int(bust.size[1] * 0.80)))
    bust = bust.crop(bust.getbbox())
    W, H = 1500, 1200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # mesh network behind the character: nodes + links, glowing green
    nodes = [(120, 760), (260, 420), (230, 1000), (1380, 760), (1240, 420), (1270, 1000), (90, 200), (1410, 200)]
    links = [(0, 1), (0, 2), (1, 6), (3, 4), (3, 5), (4, 7), (1, 4), (0, 3), (2, 5)]
    net = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(net)
    for a, b in links:
        d.line([nodes[a], nodes[b]], fill=GREEN + (255,), width=16)
    glow = net.filter(ImageFilter.GaussianBlur(14))
    img.alpha_composite(glow); img.alpha_composite(glow)
    img.alpha_composite(net)
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for x, y in nodes:
        n = Image.new("L", (W, H), 0); ImageDraw.Draw(n).ellipse([x - 44, y - 44, x + 44, y + 44], fill=255)
        L.paste(Image.new("RGBA", (W, H), GREEN + (255,)), (0, 0), n)
        c = Image.new("L", (W, H), 0); ImageDraw.Draw(c).ellipse([x - 20, y - 20, x + 20, y + 20], fill=255)
        L.paste(Image.new("RGBA", (W, H), (12, 40, 22, 255)), (0, 0), c)
    from shade import shade_layer, drop_shadow
    drop_shadow(img, L, (6, 10), blur=10, alpha=0.5)
    img.alpha_composite(shade_layer(L, radius=10, depth=2.4, spec=0.7))
    # character
    h = 1120
    w = int(bust.size[0] * h / bust.size[1])
    b = bust.resize((w, h), Image.LANCZOS)
    bx = (W - w) // 2
    img.alpha_composite(b, (bx, H - h))
    # LoRa whip antenna off the right shoulder strap, with signal arcs
    ax0, ay0 = bx + int(w * 0.74), H - int(h * 0.22)
    ax1, ay1 = ax0 + 170, 120
    ant = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).line([(ax0, ay0), (ax1, ay1)], fill=255, width=30)
    ant.paste(Image.new("RGBA", (W, H), DARK + (255,)), (0, 0), m)
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([ax1 - 24, ay1 - 24, ax1 + 24, ay1 + 24], fill=255)
    ant.paste(Image.new("RGBA", (W, H), DARK + (255,)), (0, 0), m)
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).rounded_rectangle([ax0 - 34, ay0 - 50, ax0 + 34, ay0 + 40], 14, fill=255)
    ant.paste(Image.new("RGBA", (W, H), (60, 64, 60, 255)), (0, 0), m)
    drop_shadow(img, ant, (8, 12), blur=10, alpha=0.5)
    img.alpha_composite(shade_layer(ant, radius=10, depth=2.6, spec=0.7))
    arc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(arc)
    for r in (70, 130, 190):
        d.arc([ax1 - r, ay1 - r, ax1 + r, ay1 + r], 290, 380, fill=GREEN + (255,), width=22)
        d.arc([ax1 - r, ay1 - r, ax1 + r, ay1 + r], 110, 200, fill=GREEN + (255,), width=22)
    g = arc.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(g); img.alpha_composite(shade_layer(arc, radius=6, depth=2.0, spec=0.6))
    return img.crop(img.getbbox())
