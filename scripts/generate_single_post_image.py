# -*- coding: utf-8 -*-
"""
Genera la imagen unica del post de LinkedIn — formato vigente desde el
28/08/2026 (sustituye tanto al antiguo "stat hero" de imagen unica
(`generate_post_image.py`) como al carrusel-documento negro con resaltados
naranja (`generate_carousel_post.py`), ninguno de los dos en uso desde esta
fecha). Jorge diseño el formato el mismo a mano y pidio replicarlo tal cual:
fondo crema, titular naranja enorme, foto+firma, cuadricula de logos reales
de las herramientas/marcas mencionadas en el post, y una barra inferior
negra con el CTA de comentario.

Ver AUTOMATION_BRIEF.md seccion 3 para la guia de estilo completa.

Ajuste de motor 29/08/2026 (instruccion expresa de Jorge sobre la primera
imagen generada con este formato, la del 28/08): titular con un poco mas
de aire respecto al borde superior, gap firma->logos mas ajustado (menos
hueco en blanco en el centro), y logos bastante mas grandes -- para los
favicon sueltos de tool-logos/ (que no llevan texto integrado en el PNG)
el motor ahora escribe tambien el nombre real de la herramienta debajo del
icono, ver paste_logo_grid().

Como con el resto de scripts del proyecto, el archivo tiene dos partes:
- MOTOR DE RENDER (todo lo que hay antes de "CONTENIDO DE HOY"): fijo, no
  tocar salvo que Jorge pida explicitamente un cambio de estilo.
- CONFIG ("CONTENIDO DE HOY", al final): esto SI se edita cada dia. Edita
  CONFIG, ejecuta el script, mueve el resultado a content/<carpeta-del-dia>/,
  y revierte el archivo con `git checkout -- scripts/generate_single_post_image.py`
  antes de terminar.

Uso: python3 scripts/generate_single_post_image.py content/<carpeta-del-dia>/imagen-post.png
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = REPO_ROOT / "assets" / "fonts"
PHOTO_PATH = REPO_ROOT / "assets" / "branding" / "foto-jorge.jpg"
AI_LOGO_DIR = REPO_ROOT / "assets" / "branding" / "ai-logos"
TOOL_LOGO_DIR = REPO_ROOT / "assets" / "branding" / "tool-logos"

# ============================================================
# MOTOR DE RENDER — fijo, no tocar sin instruccion expresa de Jorge.
# ============================================================

W = H = 1080

BG = (255, 252, 244)        # #FFFCF4 — fondo
ORANGE = (255, 145, 77)     # #FF914D — titular, resaltado del CTA
BAND = (40, 40, 40)         # #282828 — barra inferior
INK = (17, 17, 17)          # texto principal sobre fondo crema/blanco
GRAY = (168, 168, 162)      # subtexto de la barra (mas claro, sobre negro)

# League Spartan (Google Fonts, licencia OFL) — NO Arial/Windows, igual que
# el resto de fuentes bundleadas del proyecto. Bold para texto secundario
# (firma), ExtraBold para titular y CTA.
BOLD = FONT_DIR / "LeagueSpartan-Bold.ttf"
XBOLD = FONT_DIR / "LeagueSpartan-ExtraBold.ttf"


def F(path, size):
    return ImageFont.truetype(str(path), size)


def center_text(d, cy, text, font, fill, cx=W / 2):
    """Centra una linea de texto horizontalmente en cx, verticalmente en cy."""
    bbox = d.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    d.text((cx - w / 2, cy - (bbox[3] - bbox[1]) / 2 - bbox[1]), text, font=font, fill=fill)
    return w


def assert_line_fits(d, text, font, margin=30, context=""):
    w = d.textbbox((0, 0), text, font=font)[2]
    limit = W - 2 * margin
    assert w <= limit, (
        f'Linea demasiado ancha ({w}px, maximo {limit}px) en "{context}: {text}" '
        f"— acorta el texto o baja el tamano de fuente del titular."
    )


def mixed_center(d, cy, parts, font, cx=W / 2):
    """parts: lista de (texto, color). Centra el conjunto como una sola linea,
    cada fragmento con su propio color (para resaltar la palabra del CTA)."""
    widths = [d.textbbox((0, 0), t, font=font)[2] for t, _ in parts]
    total = sum(widths)
    x = cx - total / 2
    for (t, color), w in zip(parts, widths):
        bbox = d.textbbox((0, 0), t, font=font)
        d.text((x, cy - (bbox[3] - bbox[1]) / 2 - bbox[1]), t, font=font, fill=color)
        x += w
    return total


def circular_photo(diam=66, border=8):
    photo = Image.open(PHOTO_PATH).convert("RGB")
    photo = ImageOps.fit(photo, (diam, diam), centering=(0.5, 0.25))
    mask = Image.new("L", (diam, diam), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diam, diam), fill=255)
    ring_d = diam + border
    ring = Image.new("RGBA", (ring_d, ring_d), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, ring_d, ring_d), fill=ORANGE + (255,))
    ring.paste(photo, (border // 2, border // 2), mask)
    return ring, ring_d


def paste_logo_grid(img, tools, top_y, box_w=460, box_h=200, row_gap=290, label_gap=16):
    """Cuadricula de hasta 4 logos reales (nunca reconstruidos a mano si
    Jorge ya subio el archivo oficial a assets/branding/). Cada logo se
    escala SIN deformar (misma proporcion real) para que quepa dentro de un
    cuadro box_w x box_h — grande, pensado para que un icono cuadrado
    (favicon) salga a tamano completo box_h x box_h, y un wordmark ancho
    (icono+texto ya integrados en el propio archivo) salga limitado por el
    ancho. Debajo de cada icono, si el tool trae "name", se escribe el
    nombre real de la herramienta/app (para los favicon sueltos que no
    llevan el texto ya integrado en el PNG) — se omite si "name" es None,
    para no duplicar el texto en los logos que ya son wordmark. Con 1-2
    logos se usa una sola fila; con 3-4, dos filas de 2. Nunca mas de 4 (si
    hace falta mencionar mas herramientas, elige las 4 mas relevantes para
    el tema del dia)."""
    assert 1 <= len(tools) <= 4, "paste_logo_grid: usa entre 1 y 4 logos"
    d = ImageDraw.Draw(img)
    f_label = F(BOLD, 34)
    n = len(tools)
    cols = 1 if n == 1 else 2
    col_cx = [W / 2] if cols == 1 else [W * 0.27, W * 0.73]
    rows_needed = (n + cols - 1) // cols
    row_top = [top_y + r * row_gap for r in range(rows_needed)]
    bottom = top_y
    for i, tool in enumerate(tools):
        cx = col_cx[i % cols]
        icon_top = row_top[i // cols]
        logo = Image.open(tool["path"]).convert("RGBA")
        ratio = min(box_w / logo.width, box_h / logo.height)
        new_w, new_h = max(1, int(logo.width * ratio)), max(1, int(logo.height * ratio))
        logo = logo.resize((new_w, new_h), Image.LANCZOS)
        img.paste(logo, (int(cx - new_w / 2), int(icon_top)), logo)
        cell_bottom = icon_top + new_h
        name = tool.get("name")
        if name:
            assert_line_fits(d, name, f_label, margin=(W - box_w) / 2 + 10, context="tools.name")
            label_cy = cell_bottom + label_gap + 22
            center_text(d, label_cy, name, f_label, INK, cx=cx)
            cell_bottom = label_cy + 22
        bottom = max(bottom, cell_bottom)
    return bottom


def render(config, out_path):
    title_lines = config["title_lines"]
    assert len(title_lines) == 2, "title_lines: exactamente 2 lineas (formato validado con Jorge)"

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- Titular (2 lineas, naranja, ExtraBold, grande) ----
    # Un poco de aire respecto al borde superior (antes pegado casi al
    # borde) para que el titular respire, sin llegar a bajarlo al centro.
    f_title = F(XBOLD, 88)
    for line in title_lines:
        assert_line_fits(d, line, f_title, context="title_lines")
    y = 100
    for line in title_lines:
        center_text(d, y, line, f_title, ORANGE)
        y += 92

    # ---- Firma: foto circular + "by Jorge Segovia" ----
    ring, ring_d = circular_photo()
    f_byline = F(BOLD, 36)
    byline_w = d.textbbox((0, 0), config["byline"], font=f_byline)[2]
    gap = 20
    total_w = ring_d + gap + byline_w
    bx = (W - total_w) / 2
    by = y + 8
    img.paste(ring, (int(bx), int(by)), ring)
    d.text((bx + ring_d + gap, by + ring_d / 2), config["byline"], font=f_byline, fill=INK, anchor="lm")

    # ---- Cuadricula de logos reales ----
    # Gap reducido (antes 96) para que los bloques queden mas juntos y no
    # sobre tanto hueco en blanco entre la firma y los logos.
    logos_bottom = paste_logo_grid(img, config["tools"], top_y=by + ring_d + 32)

    # ---- Barra inferior negra: CTA de comentario ----
    # Antes 750 -> con los logos mas grandes eso dejaba un hueco en blanco
    # innecesario entre los logos y la banda; se baja a 705 para que quede
    # todo mas junto (deja justo el margen minimo de 40px del assert de abajo).
    band_top = config.get("band_top", 705)
    assert logos_bottom + 40 <= band_top, (
        f"Los logos (hasta y={logos_bottom:.0f}) invaden la banda inferior "
        f"(band_top={band_top}) — sube band_top en CONFIG o usa menos logos/mas pequenos."
    )
    d.rectangle((0, band_top, W, H), fill=BAND)

    f_cta = F(XBOLD, 50)
    cta_line = config["cta_line"]  # lista de (texto, resaltado bool)
    parts = [(t, ORANGE if hl else (255, 255, 255)) for t, hl in cta_line]
    mixed_center(d, band_top + 92, parts, f_cta)

    f_sub = F(XBOLD, 48)
    center_text(d, band_top + 192, config["cta_sub"], f_sub, GRAY)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path)
    print(f"Imagen generada: {out_path} ({W}x{H})")


# ============================================================
# CONTENIDO DE HOY — esto SI se edita cada dia. El ejemplo de abajo
# (tema del 27/08/2026, bots de IA / robots.txt) es la plantilla de
# referencia validada visualmente con Jorge el 28/08/2026 — parte de esta
# misma estructura y sustituye los textos/logos, no la reinventes.
# ============================================================

CONFIG = {
    # Titulo = el mismo que el punto 0 del post (seccion 2 del brief) y el
    # mismo que la portada del recurso descargable (seccion 4).
    "title_lines": ["GUÍA PDF PARA", "REVISAR TU ROBOTS.TXT"],

    "byline": "by Jorge Segovia",

    # 1 a 4 logos REALES (nunca reconstruidos a mano si el archivo real ya
    # existe en el repo) de las herramientas/marcas que protagonizan el
    # tema de hoy. Cada entrada es {"path": ruta, "name": nombre o None}:
    # - "name": None para los de ai-logos/ (ya llevan el wordmark de texto
    #   integrado en el propio PNG — poner el nombre otra vez lo duplicaria).
    # - "name": "Nombre real" para los de tool-logos/ (son solo el icono
    #   favicon, sin texto) — el motor escribe el nombre debajo del icono.
    # Fuentes ya disponibles:
    #   assets/branding/ai-logos/    -> claude.png, chatgpt.png,
    #                                    google-ai.png, perplexity.png
    #   assets/branding/tool-logos/  -> google-search-console.png,
    #                                    screamingfrog.png, wordpress.png,
    #                                    yoast-seo.png
    # Si el tema del dia necesita un logo que no esta en ninguna de las dos
    # carpetas, pidele a Jorge que lo suba al repo (mismo metodo que ya usa
    # para pasar capturas: subir el archivo a una carpeta de `assets/` en
    # GitHub) — no inventes ni reconstruyas un logo de marca a mano salvo
    # que de verdad no haya otra opción y Jorge lo apruebe antes de usarlo.
    "tools": [
        {"path": str(AI_LOGO_DIR / "claude.png"), "name": None},
        {"path": str(AI_LOGO_DIR / "google-ai.png"), "name": None},
        {"path": str(AI_LOGO_DIR / "perplexity.png"), "name": None},
        {"path": str(AI_LOGO_DIR / "chatgpt.png"), "name": None},
    ],

    # CTA de la barra inferior — debe coincidir con el CTA del post
    # (seccion 2, punto 6): "Comenta "<PALABRA>" y te escribo por privado
    # con el enlace." Aqui se parte en fragmentos (texto, es_resaltado) —
    # solo la palabra clave entre comillas va resaltada en naranja.
    "cta_line": [("Comenta ", False), ('"ROBOTS"', True), (" y te escribo", False)],
    "cta_sub": "debemos estar conectados =)",
}


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "_ejemplo-imagen-post.png"
    render(CONFIG, out)
