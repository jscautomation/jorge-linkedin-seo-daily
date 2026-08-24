# -*- coding: utf-8 -*-
"""
RETIRADO desde el 24/08/2026 — ya no es el flujo activo. El formato de post
pasó a ser el carrusel/documento de `generate_carousel_post.py` (ver
AUTOMATION_BRIEF.md sección 3). Se deja este archivo tal cual, sin borrar,
solo por si Jorge pide explícitamente volver al formato de imagen única
"stat hero" — no lo uses por defecto ni lo referencies en entregas nuevas.

Genera la imagen del post de LinkedIn en el estilo "stat hero": dato/cifra
gigante arriba como titular de impacto, título negro+naranja debajo, tira
fina de logos de herramientas, y barra inferior en naranja corporativo con
la foto de Jorge + el CTA al PDF gratuito en línea.

Uso: edita TITLE_LINE1 / TITLE_LINE2 / STAT_NUMBER / STAT_LABEL / SUBTITLE /
TOOL_LOGOS más abajo y ejecuta.
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
OUT_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "2026-08-21-viernes-resumen" / "imagen-post.png"

# Fuentes libres (Google Fonts, licencia OFL) bundleadas en el repo — no
# dependen de que el sistema operativo tenga Arial/Windows instalado.
FONT_TITLE = "ArchivoBlack-Regular.ttf"   # titulares grandes (equivalente a Arial Black)
FONT_BOLD = "Barlow-Bold.ttf"             # etiquetas, subtítulo, tag del panel

# ------------------------------------------------------------
# 👉 CONFIG: esto cambia cada día
# ------------------------------------------------------------
PANEL_TAG = "RESUMEN SEMANAL · SEO ECOMMERCE"   # etiqueta pequeña arriba (tema del día)
STAT_NUMBER = "4"                        # cifra grande de impacto (titular visual)
STAT_LABEL = "errores SEO reales que hemos destripado esta semana"
TITLE_LINE1 = "4 ERRORES SEO,"
TITLE_LINE2 = "1 PREGUNTA PARA TI"
SUBTITLE = "GRATIS: el PDF está en el enlace al final del post >>"
TOOL_LOGOS = [
    {"path": str(TOOL_LOGO_DIR / "gsc.png"), "label": "Search Console"},
    {"path": str(TOOL_LOGO_DIR / "wordpress.png"), "label": "WordPress"},
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


def circular_photo(diameter, border, border_color=ORANGE, centering=(0.5, 0.3)):
    photo = Image.open(PHOTO_PATH).convert("RGB")
    photo = ImageOps.fit(photo, (diameter, diameter), centering=centering)
    mask = Image.new("L", (diameter, diameter), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diameter, diameter), fill=255)
    ring_d = diameter + border * 2
    ring = Image.new("RGBA", (ring_d, ring_d), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, ring_d, ring_d), fill=border_color + (255,))
    ring.paste(photo, (border, border), mask)
    return ring, ring_d


def wrap_two_lines(text):
    """Reparte un texto en 2 líneas lo más equilibradas posible (por palabras)."""
    words = text.split(" ")
    best_split, best_diff = 1, None
    for i in range(1, len(words)):
        a = " ".join(words[:i])
        b = " ".join(words[i:])
        diff = abs(len(a) - len(b))
        if best_diff is None or diff < best_diff:
            best_diff, best_split = diff, i
    return " ".join(words[:best_split]) + "\n" + " ".join(words[best_split:])


def tool_chip(img, draw, cx, cy, diameter, tool, label_size=19, label_gap=24):
    chip_box = (cx - diameter / 2, cy - diameter / 2, cx + diameter / 2, cy + diameter / 2)
    draw.ellipse(chip_box, fill=WHITE, outline=NODE_BORDER, width=1)
    logo = Image.open(tool["path"]).convert("RGBA")
    pad = int(diameter * 0.21)
    logo_d = int(diameter) - pad * 2
    logo = logo.resize((logo_d, logo_d), Image.LANCZOS)
    img.paste(logo, (int(cx - diameter / 2 + pad), int(cy - diameter / 2 + pad)), logo)
    f_label = font(FONT_BOLD, label_size)
    draw.text((cx, cy + diameter / 2 + label_gap), tool["label"], font=f_label, fill=NODE_LABEL, anchor="mm")


def build():
    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)

    # ---- Etiqueta del tema, centrada arriba ----
    f_tag = font(FONT_BOLD, 16)
    draw.text((W / 2, 56), PANEL_TAG, font=f_tag, fill=TAG_GRAY, anchor="mm")

    # ---- Cifra de impacto, gigante, como titular visual principal ----
    f_stat = font(FONT_TITLE, 210)
    draw_multiline_center(draw, (W / 2, 220), STAT_NUMBER, f_stat, ORANGE, line_spacing=0)

    f_stat_label = font(FONT_BOLD, 30)
    draw_multiline_center(draw, (W / 2, 355), wrap_two_lines(STAT_LABEL), f_stat_label, (74, 74, 74), line_spacing=6)

    # ---- Titular (negro + línea 2 resaltada tipo marcador) ----
    f_title = font(FONT_TITLE, 62)
    draw_multiline_center(draw, (W / 2, 460), TITLE_LINE1, f_title, INK, line_spacing=8)

    bbox2 = draw.textbbox((0, 0), TITLE_LINE2, font=f_title)
    text_w2 = bbox2[2] - bbox2[0]
    pad_x, pad_y = 20, 16
    line2_cy = 560
    highlight_box = (W / 2 - text_w2 / 2 - pad_x, line2_cy - 39 - pad_y, W / 2 + text_w2 / 2 + pad_x, line2_cy + 39 + pad_y)
    rounded_rect(draw, highlight_box, 10, fill=ORANGE)
    draw_multiline_center(draw, (W / 2, line2_cy), TITLE_LINE2, f_title, WHITE, line_spacing=0)

    # ---- Tira fina de herramientas ----
    n = len(TOOL_LOGOS)
    chip_d = 130
    gap = 46
    total_w = n * chip_d + (n - 1) * gap
    start_x = (W - total_w) / 2
    chips_cy = 720
    x = start_x
    for tool in TOOL_LOGOS:
        tool_chip(img, draw, x + chip_d / 2, chips_cy, chip_d, tool)
        x += chip_d + gap

    # ---- Barra inferior en naranja corporativo: foto + CTA al PDF en línea ----
    bar_top = 900
    rounded_rect(draw, (40, bar_top, W - 40, H - 40), 16, fill=ORANGE)

    bar_cy = bar_top + (H - 40 - bar_top) / 2
    ring, ring_d = circular_photo(110, 6, border_color=WHITE)
    img.paste(ring, (60, int(bar_cy - ring_d / 2)), ring)

    f_cta = font(FONT_BOLD, 27)
    cta_text = wrap_two_lines(SUBTITLE)
    cta_lines = cta_text.split("\n")
    spacing = 8
    line_h = draw.textbbox((0, 0), "Ag", font=f_cta)[3]
    total_h = len(cta_lines) * line_h + (len(cta_lines) - 1) * spacing
    draw.multiline_text((60 + ring_d + 26, bar_cy - total_h / 2), cta_text, font=f_cta, fill=WHITE, spacing=spacing)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"Imagen generada: {OUT_PATH}")


if __name__ == "__main__":
    build()
