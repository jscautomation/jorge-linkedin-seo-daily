# -*- coding: utf-8 -*-
"""
BORRADOR DE EJEMPLO — formato nuevo propuesto (26/08 conversación con Jorge):
imagen única (no carrusel), mismo lenguaje visual de marca (ArchivoBlack +
Barlow-Bold, resaltado naranja tipo "subrayador", header logo+foto en el
mismo sitio) pero:

- Fondo BLANCO en vez de negro.
- Titular = el nombre del recurso gratis que se está regalando.
- Tono coloquial, con una broma/expresión del día a día.
- Fila de logos de herramientas relacionadas con el recurso.
- Bloque de beneficios ("qué te llevas").
- CTA tipo "Comenta X y te lo mando" (en vez de "enlace en comentarios").

NO es parte del flujo automático todavía — es un ejemplo para que Jorge dé
el visto bueno o pida cambios antes de integrarlo en la rutina diaria.

Uso: python3 scripts/generate_single_post_image_DRAFT.py [ruta_salida.png]
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = REPO_ROOT / "assets" / "fonts"
PHOTO_PATH = REPO_ROOT / "assets" / "branding" / "foto-jorge.jpg"
LOGO_PATH = REPO_ROOT / "assets" / "branding" / "logo.png"
TOOL_LOGO_DIR = REPO_ROOT / "assets" / "branding" / "tool-logos"
OUT_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "_ejemplo-formato-imagen-unica.png"

W, H = 1080, 1400
MARGIN_X = 64

# Paleta — misma marca, versión "fondo blanco"
WHITE = (255, 255, 255)
GRID = (237, 235, 231)      # rejilla decorativa — misma idea que el carrusel negro, muy sutil sobre blanco
INK = (17, 17, 17)          # texto principal sobre blanco (antes era crema sobre negro)
ORANGE = (255, 90, 31)
GRAY = (110, 110, 104)      # texto secundario — más oscuro que el gris de la versión negra, para contraste en blanco
CHIP_BG = (246, 244, 240)
CHIP_BORDER = (226, 224, 218)

TITLE_FONT = "ArchivoBlack-Regular.ttf"
BOLD_FONT = "Barlow-Bold.ttf"


def F(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


def rr(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textbbox((0, 0), trial, font=f)[2] <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, xy, text, f, fill, max_w, line_h, align="left"):
    x, y = xy
    for ln in wrap(draw, text, f, max_w):
        if align == "center":
            w = draw.textbbox((0, 0), ln, font=f)[2]
            draw.text((x - w / 2, y), ln, font=f, fill=fill)
        else:
            draw.text((x, y), ln, font=f, fill=fill)
        y += line_h
    return y


def draw_mixed_line(draw, x, y, parts, font, pad=9, radius=10):
    """parts: lista de (texto, es_resaltado). Caja naranja detrás del
    fragmento resaltado (texto en negro sobre naranja), igual que el
    carrusel — el efecto funciona igual de bien sobre fondo blanco."""
    cx = x
    for text, hl in parts:
        w = draw.textbbox((0, 0), text, font=font)[2]
        if hl:
            bbox = draw.textbbox((cx, y), text, font=font)
            box = (bbox[0] - pad, bbox[1] - pad * 0.6, bbox[2] + pad, bbox[3] + pad * 0.6)
            rr(draw, box, radius, fill=ORANGE)
            draw.text((cx, y), text, font=font, fill=INK)
        else:
            draw.text((cx, y), text, font=font, fill=INK)
        cx += w + draw.textbbox((0, 0), " ", font=font)[2]


def recolor_logo_for_white_bg():
    """El logo original ya es negro+naranja — sobre fondo blanco no hace
    falta recolorear nada (al contrario que en el carrusel, donde el negro
    se convertía en crema para que se viera sobre fondo oscuro)."""
    return Image.open(LOGO_PATH).convert("RGBA")


def circular_photo(diameter, border, border_color=ORANGE):
    photo = Image.open(PHOTO_PATH).convert("RGB")
    photo = ImageOps.fit(photo, (diameter, diameter), centering=(0.5, 0.3))
    mask = Image.new("L", (diameter, diameter), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diameter, diameter), fill=255)
    ring_d = diameter + border * 2
    ring = Image.new("RGBA", (ring_d, ring_d), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, ring_d, ring_d), fill=border_color + (255,))
    ring.paste(photo, (border, border), mask)
    return ring, ring_d


def tool_chip(img, draw, cx, cy, diameter, logo_path, label, label_size=21):
    box = (cx - diameter / 2, cy - diameter / 2, cx + diameter / 2, cy + diameter / 2)
    draw.ellipse(box, fill=CHIP_BG, outline=CHIP_BORDER, width=2)
    logo = Image.open(logo_path).convert("RGBA")
    pad = int(diameter * 0.24)
    logo_d = int(diameter) - pad * 2
    logo = logo.resize((logo_d, logo_d), Image.LANCZOS)
    img.paste(logo, (int(cx - diameter / 2 + pad), int(cy - diameter / 2 + pad)), logo)
    f_label = F(BOLD_FONT, label_size)
    draw.text((cx, cy + diameter / 2 + 22), label, font=f_label, fill=GRAY, anchor="mm")


def arrow_bullet(draw, x, y, size, color=ORANGE):
    draw.polygon([(x, y - size / 2), (x, y + size / 2), (x + size * 0.9, y)], fill=color)


# ==================================================================
# CONTENIDO DE EJEMPLO (recurso: chuleta/checklist SEO evergreen —
# solo para ilustrar el formato, se sustituye por el tema real del día)
# ==================================================================
KICKER = "RECURSO GRATIS · SEO ECOMMERCE"
TITLE_LINES = [
    [("LA ", False), ("CHULETA SEO", True)],
    [("QUE USO EN", False)],
    [("CADA AUDITORÍA", False)],
]
SUBTITLE = ("Sin rollos ni tecnicismos raros: los fallos que le hacen perder "
            "pasta a un ecommerce, contados como se los explicaría a mi cuñado.")

TOOLS = [
    (str(TOOL_LOGO_DIR / "google-search-console.png"), "Search Console"),
    (str(TOOL_LOGO_DIR / "screamingfrog.png"), "Screaming Frog"),
    (str(TOOL_LOGO_DIR / "wordpress.png"), "WordPress"),
    (str(TOOL_LOGO_DIR / "yoast-seo.png"), "Yoast SEO"),
]

BENEFITS_TITLE = "¿QUÉ TE LLEVAS?"
BENEFITS = [
    "Encuentra en 5 minutos lo que a otros les cuesta semanas ver",
    "Explicado en cristiano, cero jerga imposible",
    "Se aplica hoy mismo, sin tocar una línea de código",
]

CTA_LINE1 = "COMENTA \"CHULETA\""
CTA_LINE2 = "Y TE LO MANDO"
CTA_SUB = "Directo a tu bandeja de entrada, sin vueltas."

FOOTER_NOTE = "Guía gratuita para ecommerce en WordPress y Shopify"
# ==================================================================


def build():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # ---- Rejilla decorativa sutil (misma idea que el carrusel negro) ----
    step = 155
    for gx in range(0, W + 1, step):
        d.line((gx, 0, gx, H), fill=GRID, width=1)
    for gy in range(0, H + 1, step):
        d.line((0, gy, W, gy), fill=GRID, width=1)

    # ---- Header: logo + foto, mismo sitio que el carrusel ----
    logo = recolor_logo_for_white_bg()
    logo_h = 42
    logo_w = int(logo.width * logo_h / logo.height)
    logo_resized = logo.resize((logo_w, logo_h), Image.LANCZOS)
    img.paste(logo_resized, (MARGIN_X, 56), logo_resized)

    ring, ring_d = circular_photo(74, 4)
    img.paste(ring, (W - MARGIN_X - ring_d, 46), ring)

    d.text((MARGIN_X, 56 + logo_h + 18), KICKER, font=F(BOLD_FONT, 20), fill=GRAY)

    # ---- Titular grande (nombre del recurso) ----
    f_title = F(TITLE_FONT, 76)
    line_h = 96
    y = 218
    for line in TITLE_LINES:
        draw_mixed_line(d, MARGIN_X, y, line, f_title)
        y += line_h

    # ---- Subtítulo coloquial ----
    y += 22
    y = draw_wrapped(d, (MARGIN_X, y), SUBTITLE, F(BOLD_FONT, 28), GRAY, W - MARGIN_X * 2, 38)

    # ---- Fila de herramientas ----
    y += 44
    n = len(TOOLS)
    chip_d = 128
    gap = 40
    total_w = n * chip_d + (n - 1) * gap
    start_x = (W - total_w) / 2
    chips_cy = y + chip_d / 2
    x = start_x
    for logo_path, label in TOOLS:
        tool_chip(img, d, x + chip_d / 2, chips_cy, chip_d, logo_path, label)
        x += chip_d + gap
    y = chips_cy + chip_d / 2 + 60

    # ---- Separador ----
    d.line((MARGIN_X, y, W - MARGIN_X, y), fill=CHIP_BORDER, width=2)
    y += 40

    # ---- Beneficios ----
    d.text((MARGIN_X, y), BENEFITS_TITLE, font=F(TITLE_FONT, 30), fill=INK)
    y += 56
    f_benefit = F(BOLD_FONT, 27)
    for b in BENEFITS:
        arrow_bullet(d, MARGIN_X + 6, y + 14, 22)
        y = draw_wrapped(d, (MARGIN_X + 46, y), b, f_benefit, INK, W - MARGIN_X * 2 - 46, 34)
        y += 18

    # ---- CTA: caja naranja "Comenta X y te lo mando" ----
    y += 20
    box_top = y
    box_h = 190
    rr(d, (MARGIN_X, box_top, W - MARGIN_X, box_top + box_h), 22, fill=ORANGE)

    f_cta = F(TITLE_FONT, 46)
    cta_cy = box_top + 72
    w1 = d.textbbox((0, 0), CTA_LINE1, font=f_cta)[2]
    d.text((W / 2 - w1 / 2, cta_cy - 30), CTA_LINE1, font=f_cta, fill=WHITE)
    w2 = d.textbbox((0, 0), CTA_LINE2, font=f_cta)[2]
    d.text((W / 2 - w2 / 2, cta_cy + 34), CTA_LINE2, font=f_cta, fill=WHITE)

    f_ctasub = F(BOLD_FONT, 22)
    wsub = d.textbbox((0, 0), CTA_SUB, font=f_ctasub)[2]
    d.text((W / 2 - wsub / 2, box_top + box_h - 40), CTA_SUB, font=f_ctasub, fill=(255, 224, 209))

    # ---- Footer ----
    footer_y = box_top + box_h + 26
    fw = d.textbbox((0, 0), FOOTER_NOTE, font=F(BOLD_FONT, 20))[2]
    d.text((W / 2 - fw / 2, footer_y), FOOTER_NOTE, font=F(BOLD_FONT, 20), fill=GRAY)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH)
    print(f"Imagen generada: {OUT_PATH} ({W}x{H}, altura de contenido usada hasta y={footer_y + 30})")


if __name__ == "__main__":
    build()
