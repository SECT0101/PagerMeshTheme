#!/usr/bin/env python3
"""Shield outline shared by the MESH.5 logos and the menu cursor (community TAK shield template)."""
from PIL import Image, ImageDraw, ImageFilter
from character import bez

R = 2  # px per unit
W, H = 1000, 1100


def P(seq): return [(x * R, y * R) for x, y in seq]


def shield_poly():
    right = bez((890, 150), (906, 560), (770, 880), (500, 1066), 60)
    left = [(1000 - x, y) for x, y in right[::-1]]
    return [(500, 26), (890, 150)] + right[1:] + left[1:-1] + [(110, 150)]


def mask_of(poly):
    m = Image.new("L", (W * R, H * R), 0)
    ImageDraw.Draw(m).polygon(P(poly), fill=255)
    return m


def erode(m, r):
    return m.filter(ImageFilter.GaussianBlur(r * R)).point(lambda v: 255 if v > 250 else 0)
