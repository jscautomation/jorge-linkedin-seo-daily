# -*- coding: utf-8 -*-
"""Generates the brand gradient background PNG (135°, orange) used by the PDF."""
import math
from PIL import Image

GRAD_START = (255, 161, 53)   # #FFA135
GRAD_END = (255, 90, 31)      # #FF5A1F
OUT_PATH = r"C:\Users\Usuario\Desktop\Youtube_Auto\linkedin-seo-automation\assets\branding\gradient_bg.png"

W, H = 1240, 1754  # A4 @ ~150dpi


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def build(angle_deg=135, w=W, h=H, c1=GRAD_START, c2=GRAD_END, out=OUT_PATH):
    angle = math.radians(angle_deg)
    dx, dy = math.cos(angle), math.sin(angle)
    img = Image.new("RGB", (w, h))
    px = img.load()
    # projection range along gradient direction
    corners = [(0, 0), (w, 0), (0, h), (w, h)]
    projs = [x * dx + y * dy for x, y in corners]
    pmin, pmax = min(projs), max(projs)
    for y in range(h):
        for x in range(0, w, 2):  # step 2 for speed, then fill neighbor
            p = x * dx + y * dy
            t = (p - pmin) / (pmax - pmin)
            color = lerp(c1, c2, t)
            px[x, y] = color
            if x + 1 < w:
                px[x + 1, y] = color
    img.save(out)
    print(f"Gradiente generado: {out}")


if __name__ == "__main__":
    build()
