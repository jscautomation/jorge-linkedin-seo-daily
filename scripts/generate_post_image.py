# -*- coding: utf-8 -*-
"""
Genera la imagen del post de LinkedIn en el estilo "workflow":
panel gris con mini-diagrama de pasos arriba, titular negro+naranja
abajo a la izquierda, foto circular con borde naranja abajo a la derecha.

Uso: edita TITLE_LINE1 / TITLE_LINE2 / STEPS más abajo y ejecuta.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1080, 1080
WHITE = (255, 255, 255)
PANEL_BG = (244, 244, 244)
INK = (13, 13, 13)
ORANGE = (255, 90, 31)
NODE_BORDER = (226, 226, 226)
NODE_LABEL = (43, 43, 43)
CONNECTOR = (207, 207, 207)
TAG_GRAY = (138, 138, 138)

# Rutas relativas al repo (funciona igual en Windows local que en el sandbox
# Linux de la ejecución en la nube — nunca usar rutas absolutas tipo C:\...).
REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = REPO_ROOT / "assets" / "fonts"
PHOTO_PATH = REPO_ROOT / "assets" / "branding" / "foto-jorge.jpg"
TOOL_LOGO_DIR = REPO_ROOT / "assets" / "branding" / "tool-logos"

# 👉 Esto también se pasa por CLI/env en la ejecución diaria; por defecto usa
# la carpeta de contenido de hoy. Ver generate_post_image.py --help.
import sys
OUT_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "2026-08-20-jueves-tendencia" / "imagen-post.png"

# Fuentes libres (Google Fonts, licencia OFL) bundleadas en el repo — no
# dependen de que el sistema operativo tenga Arial/Windows instalado.
FONT_TITLE = "ArchivoBlack-Regular.ttf"   # titulares grandes (equivalente a Arial Black)
FONT_BOLD = "Barlow-Bold.ttf"             # etiquetas, subtítulo, tag del panel

# ------------------------------------------------------------
# 👉 CONFIG: esto cambia cada día
# ------------------------------------------------------------
TITLE_LINE1 = "FICHA DE PRODUCTO"
TITLE_LINE2 = "GOOGLE YA NO TE VE"
SUBTITLE = "El 83% de las AI Overviews no dan ni un clic >>"
PANEL_TAG = "HERRAMIENTAS DE HOY"
TOOL_LOGOS = [
    {"path": str(TOOL_LOGO_DIR / "gsc.png"), "label": "Search Console"},
    {"path": str(TOOL_LOGO_DIR / "screamingfrog.png"), "label": "Screaming Frog"},
]


def font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


def rounded_rect(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_multiline_center(draw, xy, text, f, fill, line_spacing=4):
    lines = text.split("\n")
    heights = []
    widths = []
    for ln in lines:
        bbox = draw.textbbox((0, 0), ln, font=f)
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])
    total_h = sum(heights) + line_spacing * (len(lines) - 1)
    cx, cy = xy
    y = cy - total_h / 2
    for i, ln in enumerate(lines):
        w = widths[i]
        draw.text((cx - w / 2, y), ln, font=f, fill=fill)
        y += heights[i] + line_spacing


def build():
    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)

    # ---- Panel del diagrama ----
    panel_box = (40, 40, W - 40, 460)
    rounded_rect(draw, panel_box, 18, fill=PANEL_BG)

    f_tag = font(FONT_BOLD, 15)
    draw.text((64, 58), PANEL_TAG, font=f_tag, fill=TAG_GRAY)

    # ---- Panel simple: logos de herramientas centrados, sin conectores ----
    n = len(TOOL_LOGOS)
    chip_d = 220
    gap = 60
    total_w = n * chip_d + (n - 1) * gap
    start_x = (W - total_w) / 2
    panel_cy = (panel_box[1] + panel_box[3]) / 2 + 6

    f_label = font(FONT_BOLD, 24)
    x = start_x
    for tool in TOOL_LOGOS:
        cx = x + chip_d / 2
        chip_box = (x, panel_cy - chip_d / 2, x + chip_d, panel_cy + chip_d / 2)
        draw.ellipse(chip_box, fill=WHITE, outline=NODE_BORDER, width=1)
        logo = Image.open(tool["path"]).convert("RGBA")
        pad = 46
        logo_d = chip_d - pad * 2
        logo = logo.resize((logo_d, logo_d), Image.LANCZOS)
        img.paste(logo, (int(x + pad), int(panel_cy - chip_d / 2 + pad)), logo)
        draw.text((cx, panel_cy + chip_d / 2 + 36), tool["label"], font=f_label, fill=NODE_LABEL, anchor="mm")
        x += chip_d + gap

    # ---- Titular (grande, con sombra + línea 2 resaltada tipo marcador) ----
    f_title = font(FONT_TITLE, 82)

    # Línea 1: negro con sombra suave para dar profundidad y que "salte" de la página.
    shadow_offset = 4
    draw.text((40 + shadow_offset, 500 + shadow_offset), TITLE_LINE1, font=f_title, fill=(0, 0, 0, 60))
    draw.text((40, 500), TITLE_LINE1, font=f_title, fill=INK)

    # Línea 2: bloque naranja tipo "resaltador" con texto en blanco — máximo contraste.
    bbox2 = draw.textbbox((0, 0), TITLE_LINE2, font=f_title)
    text_w2 = bbox2[2] - bbox2[0]
    pad_x, pad_y = 20, 16
    line2_y = 650
    highlight_box = (40 - pad_x, line2_y - pad_y, 40 + text_w2 + pad_x, line2_y + 82 + pad_y)
    rounded_rect(draw, highlight_box, 10, fill=ORANGE)
    draw.text((40, line2_y - bbox2[1]), TITLE_LINE2, font=f_title, fill=WHITE)

    # ---- Subtítulo de apoyo (rellena el hueco bajo el título, da contexto) ----
    f_subtitle = font(FONT_BOLD, 30)
    subtitle_y = highlight_box[3] + 34
    draw.text((40, subtitle_y), SUBTITLE, font=f_subtitle, fill=(74, 74, 74))

    # ---- Foto circular con borde naranja ----
    # Banda propia, claramente separada del bloque de texto (nunca se tocan).
    photo_d = 185
    border = 8
    photo = Image.open(PHOTO_PATH).convert("RGB")
    photo = ImageOps.fit(photo, (photo_d, photo_d), centering=(0.5, 0.3))
    mask = Image.new("L", (photo_d, photo_d), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.ellipse((0, 0, photo_d, photo_d), fill=255)

    ring_d = photo_d + border * 2
    ring = Image.new("RGBA", (ring_d, ring_d), (0, 0, 0, 0))
    rdraw = ImageDraw.Draw(ring)
    rdraw.ellipse((0, 0, ring_d, ring_d), fill=ORANGE + (255,))
    ring.paste(photo, (border, border), mask)

    # Banda inferior propia (empieza claramente por debajo del bloque naranja del título).
    photo_band_top = 855
    px = W - 60 - ring_d
    py = photo_band_top
    img.paste(ring, (int(px), int(py)), ring)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"Imagen generada: {OUT_PATH}")


if __name__ == "__main__":
    build()
