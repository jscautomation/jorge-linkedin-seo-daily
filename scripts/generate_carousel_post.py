# -*- coding: utf-8 -*-
"""
Genera el carrusel/documento del post de LinkedIn — 1080x1080, estilo
"documento negro con resaltados naranja". Adoptado como formato ESTANDAR
de las publicaciones desde el 24/08/2026 (sustituye tanto al antiguo
"stat hero" de `generate_post_image.py` como al primer intento de
carrusel "captura anotada a mano" con garabatos), inspirado en el perfil
de referencia Twinkle Chatterjee (ThriveCraft SEO) que Jorge señaló como
modelo tras analizar datos de Apify de varios perfiles SEO de alto
rendimiento en LinkedIn.

Cómo funciona (leer también AUTOMATION_BRIEF.md sección 3 — es la guía de
estilo completa: paleta exacta, fuentes, límites de texto por tipo de
slide y por qué existen esos límites):

- El MOTOR DE RENDER (todo lo de arriba de "CONTENIDO DE HOY") es FIJO.
  No tocar tamaños, colores, posiciones ni límites salvo que Jorge pida
  explícitamente un cambio de estilo — es lo que garantiza que el
  carrusel de hoy se vea igual que el de ayer y el de mañana.
- El CONTENIDO (CONFIG al final del archivo) SÍ se edita cada día: es una
  lista de slides, cada una un diccionario con un "type" de entre
  cover | statement | bullets | card | closing (ver la guía de estilo
  para qué lleva cada uno). Edita CONFIG, ejecuta el script, y como con
  `generate_lead_magnet_pdf.py`, revierte el archivo con
  `git checkout -- scripts/generate_carousel_post.py` después de mover el
  contenido generado a la carpeta `content/<día>/` correspondiente.
- Cada slide de tipo distinto de "cover"/"closing" lleva automáticamente
  la nota "DESCARGA LA GUÍA PDF EN COMENTARIOS" en la esquina inferior
  izquierda (vigente desde el 25/08/2026, a petición expresa de Jorge) —
  es la regla no negociable del brief (sección 3bis): el PDF con la
  respuesta completa NUNCA se da en el carrusel, solo el diagnóstico. La
  slide de cierre lleva el único CTA fuerte con el enlace al PDF.
- La portada (`cover`) lleva, si el spec trae `guide_badge`, un recuadro
  naranja ENCIMA del título con el número de la mejora dentro de la guía
  de Notion y una frase de acceso (vigente desde el 03/09/2026, a
  petición expresa de Jorge — ver `guide_badge()` y AUTOMATION_BRIEF.md
  sección 3.3 para la fórmula del número).

Salida: `carrusel-1.png` ... `carrusel-N.png` (una por slide) +
`carrusel-post.pdf` (empaquetado SIN pérdida vía img2pdf — Pillow re-
comprime a JPEG si se usa `Image.save(..., "PDF")`, se nota en las cajas
resaltadas y el texto). **Sube el PDF a LinkedIn como publicación de tipo
Documento** (así es como funciona el formato de referencia — un PDF que
LinkedIn renderiza como visor deslizable — NO como carrusel de imágenes
sueltas; los PNG existen para poder revisar/editar cada slide a mano).

Uso: python3 scripts/generate_carousel_post.py content/<carpeta-del-día>
(si se omite la carpeta, usa una ruta por defecto — ver OUT_DIR).
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import img2pdf

REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = REPO_ROOT / "assets" / "fonts"
PHOTO_PATH = REPO_ROOT / "assets" / "branding" / "foto-jorge.jpg"
LOGO_PATH = REPO_ROOT / "assets" / "branding" / "logo.png"
OUT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "carrusel-hoy"

# ============================================================
# MOTOR DE RENDER — fijo, no tocar sin instrucción expresa de Jorge.
# Ver AUTOMATION_BRIEF.md sección 3 para la guía de estilo con capturas
# de referencia y el razonamiento detrás de cada límite.
# ============================================================

W = H = 1080
MARGIN_X = 56

# Paleta (hex de referencia entre paréntesis para cuando haga falta fuera
# de Python, p.ej. en el HTML del formulario o en Figma):
BG = (255, 252, 244)       # #FFFCF4 — fondo crema (cambiado 03/09/2026, antes #0C0C0C negro)
GRID = (230, 224, 210)     # gris claro sobre crema — líneas de la rejilla decorativa
CREAM = (17, 17, 17)       # #111111 — texto principal oscuro sobre crema (nombre de variable heredado del formato negro anterior)
ORANGE = (255, 90, 31)     # #FF5A1F — color de marca; resaltados y acentos (sin cambios)
INK = (17, 17, 17)         # #111111 — texto sobre fondo naranja/crema
GRAY = (120, 118, 110)     # gris oscuro sobre crema — texto secundario/kicker

# Fuentes libres bundleadas (OFL), NO Arial/Windows. Igual que el resto
# del proyecto, NO incluyen emoji — nunca uses 💬🔖🔁 etc. dentro de una
# imagen; si necesitas un icono, dibújalo a mano (ver icon_number() o los
# iconos de pdf_cta_bar en versiones anteriores) en vez de un emoji.
TITLE = "ArchivoBlack-Regular.ttf"
BOLD = "Barlow-Bold.ttf"


def F(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


# Tamaños de fuente por ROL (no por slide) — usa siempre el que
# corresponda al rol, no un tamaño suelto, para que todos los días se
# vean con la misma jerarquía visual:
TITLE_XL = 84     # título grande multilínea: cover, statement, bullets
LINE_H_XL = 132   # interlineado para TITLE_XL (deja hueco a la caja de resaltado)
TITLE_L = 68      # título de 2 líneas de la slide de cierre
LINE_H_L = 104
TITLE_MED = 62    # etiqueta de una card ("SEÑAL 1:", "MITO:", "DATO 1:"...)
HEADLINE = 50     # titular resaltado y envuelto dentro de una card
LINE_H_HEADLINE = 100
BODY = 28         # párrafo de cuerpo normal
LINE_H_BODY = 38
BULLET_SIZE = 26  # texto de items en listas (bullets/checks)
SMALL = 20        # kicker, notas de pie, subtítulos de CTA

# Zonas de seguridad (aprendidas a base de overflows reales al maquetar
# el ejemplo — respétalas al escribir contenido nuevo):
TITLE_SAFE_TOP = 150       # ninguna línea de título debe empezar antes de aquí
FOOTER_SAFE_BOTTOM = 980   # ningún bloque de contenido debe bajar de aquí
COVER_SUBTITLE_MAX_W = 800  # ancho máximo del subtítulo de portada — deja
# libre la columna derecha (x > ~944) donde vive el indicador de deslizar
# en la mitad inferior de la slide; usar un ancho mayor ahí hace que el
# texto se meta debajo del circulo naranja y quede tapado.


def rr(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def canvas():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    step = 155
    for x in range(0, W + 1, step):
        d.line((x, 0, x, H), fill=GRID, width=1)
    for y in range(0, H + 1, step):
        d.line((0, y, W, y), fill=GRID, width=1)
    return img, d


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


def draw_mixed_line(draw, x, y, parts, font, pad=9, radius=10, plain_fill=CREAM, measure_only=False):
    """parts: lista de (texto, es_resaltado). Dibuja en una sola línea,
    con caja naranja redondeada detrás de los fragmentos resaltados
    (texto en negro sobre naranja) — el efecto "subrayador" característico
    de este formato. Usa textbbox ya anclado en la posición real de
    dibujo (no en (0,0)) para que la caja quede pegada al texto de
    verdad, sin desplazarse — NO "optimizar" esto calculando el bbox en
    (0,0) y sumando offsets a mano, así es como se rompió la primera vez.

    `measure_only=True` no dibuja nada, solo devuelve la coordenada x
    final — así `assert_line_fits()` puede comprobar el ancho real con
    exactamente la misma lógica que el dibujado de verdad, sin que las
    dos puedan desincronizarse."""
    cx = x
    for text, hl in parts:
        bbox = draw.textbbox((cx, y), text, font=font)
        if hl:
            box = (bbox[0] - pad, bbox[1] - 6, bbox[2] + pad, bbox[3] + 6)
            if not measure_only:
                rr(draw, box, radius, fill=ORANGE)
                draw.text((cx, y), text, font=font, fill=INK)
            cx = box[2] + 12
        else:
            if not measure_only:
                draw.text((cx, y), text, font=font, fill=plain_fill)
            cx = bbox[2] + 14
    return cx


def assert_line_fits(d, parts, font, context=""):
    """Comprueba, ANTES de dibujar, que una línea de título (título de
    portada, statement, bullets, closing o etiqueta de card) no se sale
    del lienzo por la derecha. Falla alto y claro en vez de dejar un PNG
    con el texto cortado — si salta esto, la línea de contenido de hoy es
    demasiado larga para el tamaño de fuente de su rol: acórtala o
    repártela en más líneas."""
    end_x = draw_mixed_line(d, MARGIN_X, 0, parts, font, measure_only=True)
    limit = W - 24
    assert end_x <= limit, (
        f"Línea demasiado ancha ({end_x}px, máximo {limit}px) en {context or parts!r} "
        "— acorta el texto o pártelo en más líneas."
    )


def highlighted_wrapped(draw, x, y, text, font, max_w, line_h):
    """Como draw_wrapped pero cada línea resultante se dibuja entera
    resaltada — para un titular largo que no cabe en una sola línea sin
    salirse del lienzo (usar SIEMPRE esto para el `headline` de una card,
    nunca draw_mixed_line con el texto entero en una sola llamada, o se
    sale del lienzo por la derecha en cuanto el texto supera ~6 palabras)."""
    for ln in wrap(draw, text, font, max_w):
        draw_mixed_line(draw, x, y, [(ln, True)], font)
        y += line_h
    return y


def _recolored_logo():
    """El logo oficial es texto negro + naranja sobre fondo transparente.
    Para fondo oscuro, el negro se recolorea a crema; el naranja se deja
    tal cual (coincide con ORANGE, no hace falta re-tocar la marca)."""
    im = Image.open(LOGO_PATH).convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a > 30 and r < 100 and g < 100 and b < 100:
                px[x, y] = (CREAM[0], CREAM[1], CREAM[2], a)
    return im


LOGO_DARK = _recolored_logo()


def header(img, d):
    """Logo arriba a la izquierda + foto de Jorge en círculo naranja
    arriba a la derecha — mismo sitio en TODAS las slides, incluida la
    de cierre."""
    logo_h = 46
    ratio = logo_h / LOGO_DARK.height
    logo = LOGO_DARK.resize((int(LOGO_DARK.width * ratio), logo_h), Image.LANCZOS)
    img.paste(logo, (56, 44), logo)

    diam = 92
    photo = Image.open(PHOTO_PATH).convert("RGB")
    photo = ImageOps.fit(photo, (diam, diam), centering=(0.5, 0.25))
    mask = Image.new("L", (diam, diam), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diam, diam), fill=255)
    ring_d = diam + 10
    ring = Image.new("RGBA", (ring_d, ring_d), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, ring_d, ring_d), fill=ORANGE + (255,))
    ring.paste(photo, (5, 5), mask)
    img.paste(ring, (W - ring_d - 46, 30), ring)


def kicker(d, text):
    """Etiqueta pequeña centrada... no, alineada a la izquierda, debajo
    del logo — el tema/ángulo del día en mayúsculas (p.ej. "ROAST SEO ·
    ECOMMERCE", "MITO SEO · ECOMMERCE"). Misma en las N slides."""
    d.text((56, 106), text, font=F(BOLD, SMALL), fill=GRAY)


GUIDE_BADGE_FONT_SIZE = 26  # FIJO, igual criterio que FOOTER_NOTE_FONT_SIZE — nunca se auto-ajusta al texto
GUIDE_BADGE_LINE_H = 34
GUIDE_BADGE_TOP = 140  # justo debajo del kicker (que vive en y=106)


def guide_badge(img, d, number, line):
    """Recuadro con el gancho de la guía SEO de Notion, ENCIMA del título de
    la portada (`cover`) — vigente desde el 03/09/2026 a petición expresa de
    Jorge (sustituye al primer intento de meter el número en el kicker + una
    frase suelta en el subtitle, que no se veía suficientemente destacado).

    Caja naranja de marca con esquinas redondeadas, texto en negro (INK),
    ancho fijo (el ancho útil del canvas) y alto variable según cuántas
    líneas ocupe el texto envuelto — mismo criterio que footer_gate_note:
    el tamaño de letra NUNCA se auto-ajusta, lo que varía es cuánto espacio
    ocupa la caja. Solo se usa en `cover`; el resto de slides ya tienen su
    propio recuadro (footer_gate_note).

    `number` es el número de la mejora dentro de la guía (arranca en 1 el
    día que se activó la guía en Notion, 03/09/2026, sube +1 cada día
    publicado — ver AUTOMATION_BRIEF.md sección 3.3 para la fórmula).
    `line` es la frase fija que invita a pedir acceso (editar solo si Jorge
    pide cambiar el texto, no el número)."""
    font = F(BOLD, GUIDE_BADGE_FONT_SIZE)
    text = f'MEJORA Nº{number} · {line}'
    pad_x, pad_y = 28, 22
    max_w = W - 2 * MARGIN_X - 2 * pad_x
    lines = wrap(d, text, font, max_w)
    box_h = pad_y * 2 + GUIDE_BADGE_LINE_H * len(lines)
    box = (MARGIN_X, GUIDE_BADGE_TOP, W - MARGIN_X, GUIDE_BADGE_TOP + box_h)
    rr(d, box, radius=20, fill=ORANGE)
    ty = GUIDE_BADGE_TOP + pad_y
    for ln in lines:
        d.text((MARGIN_X + pad_x, ty), ln, font=font, fill=INK)
        ty += GUIDE_BADGE_LINE_H
    return GUIDE_BADGE_TOP + box_h + 32  # y de arranque del título, con margen


DEFAULT_FOOTER_NOTE = 'COMENTA "<PALABRA>" Y TE LO ENVÍO'  # sustituye <PALABRA> en CONFIG cada día
FOOTER_NOTE_FONT_SIZE = 26  # FIJO — nunca variar entre slides ni auto-ajustar al ancho del texto


def footer_gate_note(img, d, text=DEFAULT_FOOTER_NOTE):
    """Recordatorio de la regla no negociable (brief sección 2, punto 4): la
    solución completa vive solo en la guía de Notion, nunca en el carrusel.
    Va en TODAS las slides menos la de cierre (que ya lleva su propio CTA
    grande con el mismo mensaje).

    Versión "recuadro naranja" vigente desde el 03/09/2026 a petición expresa
    de Jorge (antes era texto naranja suelto sobre el fondo, y antes de eso
    texto discreto en gris — ver AUTOMATION_BRIEF.md para el historial):
    caja naranja de marca con esquinas redondeadas + texto en BLANCO + flecha
    blanca dibujada a mano, todo DENTRO de la caja. El tamaño de fuente es
    fijo (FOOTER_NOTE_FONT_SIZE) — nunca se auto-ajusta al ancho del texto;
    lo que varía de un día a otro es el ancho de la caja, no el tamaño de
    letra."""
    font = F(TITLE, FOOTER_NOTE_FONT_SIZE)
    pad_x, pad_y = 22, 16
    arrow_w = 34  # espacio reservado para la flecha dentro de la caja

    bbox = d.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    box_h = text_h + pad_y * 2
    box_w = arrow_w + text_w + pad_x * 2
    x0, y0 = MARGIN_X, H - 40 - box_h
    x1, y1 = x0 + box_w, y0 + box_h

    rr(d, (x0, y0, x1, y1), radius=box_h // 2, fill=ORANGE)

    ax, ay = x0 + pad_x + 9, y0 + box_h // 2 - 11
    d.line((ax, ay, ax, ay + 22), fill=(255, 255, 255), width=5)
    d.line((ax - 9, ay + 11, ax, ay + 22), fill=(255, 255, 255), width=5)
    d.line((ax + 9, ay + 11, ax, ay + 22), fill=(255, 255, 255), width=5)

    tx = x0 + pad_x + arrow_w
    ty = y0 + box_h // 2 - text_h // 2 - bbox[1]
    d.text((tx, ty), text, font=font, fill=(255, 255, 255))


def scroll_hint(img, last=False):
    """Barra degradada + flecha circular abajo a la derecha, indicando
    que hay más slides — en la última slide de contenido (justo antes del
    cierre) la flecha se convierte en un check. NUNCA coloques texto de
    contenido en la zona aproximada x>930, y>680 de la mitad inferior de
    la slide — es donde vive este elemento."""
    bw, bh = 62, 190
    grad = Image.new("RGB", (1, bh), BG)
    for y in range(bh):
        t = y / (bh - 1)
        col = tuple(int(ORANGE[i] * (1 - t) + BG[i] * t) for i in range(3))
        grad.putpixel((0, y), col)
    grad = grad.resize((bw, bh))
    mask = Image.new("L", (bw, bh), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, bw, bh), radius=bw // 2)
    bx, by = W - bw - 74, 686
    img.paste(grad, (bx, by), mask)

    cx, cy, r = bx + bw // 2, by + bh + 46, 42
    d = ImageDraw.Draw(img)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=ORANGE)
    if last:
        d.line((cx - 15, cy, cx - 4, cy + 13), fill=INK, width=7)
        d.line((cx - 4, cy + 13, cx + 16, cy - 12), fill=INK, width=7)
    else:
        d.line((cx - 14, cy, cx + 14, cy), fill=INK, width=7)
        d.line((cx + 4, cy - 11, cx + 15, cy), fill=INK, width=7)
        d.line((cx + 4, cy + 11, cx + 15, cy), fill=INK, width=7)


def arrow_bullets(d, x, y, items, gap=62):
    """Lista con flecha dibujada a mano (no emoji/glyph — estas fuentes no
    tienen el carácter →) — para el tipo "bullets" (por qué importa)."""
    for line in items:
        ay = y + 16
        d.line((x, ay, x + 20, ay), fill=ORANGE, width=5)
        d.line((x + 12, ay - 7, x + 22, ay), fill=ORANGE, width=5)
        d.line((x + 12, ay + 7, x + 22, ay), fill=ORANGE, width=5)
        y = draw_wrapped(d, (x + 42, y), line, F(BOLD, BULLET_SIZE), CREAM, W - x - 42 - 108, 32)
        y += gap - 32
    return y


def ring_checks(d, x, y, items, gap=80):
    """Lista de preguntas de autocomprobación con un pequeño anillo — para
    el campo `checks` del tipo "card"."""
    for c in items:
        d.ellipse((x, y + 10, x + 12, y + 22), outline=ORANGE, width=3)
        draw_wrapped(d, (x + 36, y), c, F(BOLD, BULLET_SIZE), CREAM, W - x - 36 - 108, 34)
        y += gap
    return y


# ------------------------------------------------------------------
# Un renderer por cada "type" de slide soportado. Todos comparten firma
# (img, d, spec, index, total) aunque no usen index/total.
# ------------------------------------------------------------------

def render_cover(img, d, spec, index, total):
    title_lines = spec["title_lines"]
    badge = spec.get("guide_badge")
    if badge:
        assert len(title_lines) <= 3, (
            "cover: con guide_badge, máximo 3 líneas de título "
            "(el recuadro de la guía ocupa espacio arriba)"
        )
        y = guide_badge(img, d, badge["number"], badge["line"])
    else:
        assert len(title_lines) <= 5, "cover: máximo 5 líneas de título (se sale del lienzo por abajo)"
        y = TITLE_SAFE_TOP
    for line in title_lines:
        assert_line_fits(d, line, F(TITLE, TITLE_XL), context=f"cover: {line}")
        draw_mixed_line(d, MARGIN_X, y, line, F(TITLE, TITLE_XL))
        y += LINE_H_XL
    if spec.get("subtitle"):
        draw_wrapped(d, (MARGIN_X, y + 24), spec["subtitle"], F(BOLD, BODY), GRAY,
                     COVER_SUBTITLE_MAX_W, LINE_H_BODY)


def render_statement(img, d, spec, index, total):
    """Slide de "declaración" grande: 1-3 líneas de título (mezcla de
    texto plano y resaltado, igual que cover), más opcionalmente un
    párrafo de cuerpo y/o una línea de cierre resaltada. Cubre tanto el
    gancho (solo title_lines) como una slide de contexto/transición
    (title_lines + body + closing)."""
    title_lines = spec["title_lines"]
    assert len(title_lines) <= 4, "statement: máximo 4 líneas de título"
    y = TITLE_SAFE_TOP
    for line in title_lines:
        assert_line_fits(d, line, F(TITLE, TITLE_XL), context=f"statement: {line}")
        draw_mixed_line(d, MARGIN_X, y, line, F(TITLE, TITLE_XL))
        y += LINE_H_XL
    if spec.get("closing"):
        assert_line_fits(d, spec["closing"], F(TITLE, TITLE_MED), context=f"statement closing: {spec['closing']}")
    if spec.get("body"):
        y += 34
        y = draw_wrapped(d, (MARGIN_X, y), spec["body"], F(BOLD, 30), CREAM, W - 2 * MARGIN_X, 40)
    if spec.get("closing"):
        y += 40
        draw_mixed_line(d, MARGIN_X, y, spec["closing"], F(TITLE, TITLE_MED))


def render_bullets(img, d, spec, index, total):
    """Título grande + intro + lista de 2-4 items con flecha + cierre
    (gris, opcional). Para "por qué importa esto"."""
    title_lines = spec["title_lines"]
    assert len(title_lines) <= 3, "bullets: máximo 3 líneas de título"
    assert 2 <= len(spec["items"]) <= 4, "bullets: entre 2 y 4 items (más se mete en la zona del indicador)"
    y = TITLE_SAFE_TOP
    for line in title_lines:
        assert_line_fits(d, line, F(TITLE, TITLE_XL), context=f"bullets: {line}")
        draw_mixed_line(d, MARGIN_X, y, line, F(TITLE, TITLE_XL))
        y += LINE_H_XL
    y += 40
    if spec.get("intro"):
        y = draw_wrapped(d, (MARGIN_X, y), spec["intro"], F(BOLD, BODY), CREAM, W - 2 * MARGIN_X, 36)
        y += 34
    y = arrow_bullets(d, MARGIN_X, y, spec["items"])
    if spec.get("closing"):
        y += 20
        draw_wrapped(d, (MARGIN_X, y), spec["closing"], F(BOLD, BODY), GRAY, W - 2 * MARGIN_X, 36)


def render_card(img, d, spec, index, total):
    """Una tarjeta = un hallazgo/paso/dato por slide: etiqueta ("SEÑAL 1",
    "MITO", "DATO 1"...) + titular resaltado (envuelto automáticamente) +
    cuerpo corto + hasta 2 preguntas de autocomprobación. Es el bloque que
    más se repite (el "documento" real: cada card es una página)."""
    checks = spec.get("checks") or []
    assert len(checks) <= 2, "card: máximo 2 items en `checks` (3+ empuja el contenido a la nota de pie)"
    y = 150
    label_line = [(spec["label"] + ":", False)]
    assert_line_fits(d, label_line, F(TITLE, TITLE_MED), context=f"card label: {spec['label']}")
    draw_mixed_line(d, MARGIN_X, y, label_line, F(TITLE, TITLE_MED))
    y += 112
    y = highlighted_wrapped(d, MARGIN_X, y, spec["headline"].upper(), F(TITLE, HEADLINE),
                             W - MARGIN_X - 56, LINE_H_HEADLINE)
    y += 40
    if spec.get("body"):
        y = draw_wrapped(d, (MARGIN_X, y), spec["body"], F(BOLD, BODY), CREAM, W - 2 * MARGIN_X, LINE_H_BODY)
        y += 110
    if checks:
        d.text((MARGIN_X, y), "Comprueba tu mismo:", font=F(BOLD, 24), fill=GRAY)
        y += 56
        ring_checks(d, MARGIN_X, y, checks)


def render_closing(img, d, spec, index, total):
    """Última slide: título de 2 líneas + hasta 3 CTAs numerados
    (comentar / guardar / compartir) + el ÚNICO bloque fuerte con el
    enlace real al PDF gated. No lleva footer_gate_note ni scroll_hint
    (se gestiona en render_all)."""
    title_lines = spec["title_lines"]
    assert len(title_lines) == 2, "closing: exactamente 2 líneas de título (para que el bloque de abajo quepa)"
    ctas = spec["ctas"]
    assert len(ctas) <= 3, "closing: máximo 3 CTAs (comentar / guardar / compartir)"

    y = 150
    for line in title_lines:
        assert_line_fits(d, line, F(TITLE, TITLE_L), context=f"closing: {line}")
        draw_mixed_line(d, MARGIN_X, y, line, F(TITLE, TITLE_L))
        y += LINE_H_L
    y += 44  # separación fija hasta el primer CTA (validada visualmente)

    for i, (title, sub) in enumerate(ctas, start=1):
        d.ellipse((MARGIN_X, y, MARGIN_X + 40, y + 40), fill=ORANGE)
        d.text((MARGIN_X + 20, y + 20), str(i), font=F(TITLE, 20), fill=INK, anchor="mm")
        draw_mixed_line(d, MARGIN_X + 60, y + 2, [(title, False)], F(TITLE, 25))
        draw_wrapped(d, (MARGIN_X + 60, y + 44), sub, F(BOLD, 19), GRAY, W - MARGIN_X - 60 - 56, 24)
        y += 100

    box = (MARGIN_X, y + 20, W - MARGIN_X, y + 220)
    rr(d, box, 22, fill=ORANGE)
    draw_wrapped(d, (box[0] + 32, box[1] + 26), spec["box_title"], F(TITLE, 25), INK,
                 box[2] - box[0] - 64, 32)
    d.text((box[0] + 32, box[3] - 60), spec["box_link"], font=F(TITLE, 22), fill=INK)


RENDERERS = {
    "cover": render_cover,
    "statement": render_statement,
    "bullets": render_bullets,
    "card": render_card,
    "closing": render_closing,
}


def render_all(config):
    slides = config["slides"]
    assert slides[0]["type"] == "cover", "la primera slide debe ser type=cover"
    assert slides[-1]["type"] == "closing", "la última slide debe ser type=closing"
    total = len(slides)
    for i, spec in enumerate(slides, start=1):
        img, d = canvas()
        header(img, d)
        kicker(d, config["kicker"])
        RENDERERS[spec["type"]](img, d, spec, i, total)
        if spec["type"] != "closing":
            footer_gate_note(img, d, config.get("footer_note", DEFAULT_FOOTER_NOTE))
        if spec["type"] != "closing":
            is_last_before_closing = (i == total - 1)
            scroll_hint(img, last=is_last_before_closing)
        img.save(OUT_DIR / f"carrusel-{i}.png")
    return total


def build_pdf(total):
    paths = [OUT_DIR / f"carrusel-{i}.png" for i in range(1, total + 1)]
    pdf_path = OUT_DIR / "carrusel-post.pdf"
    layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(285.75), img2pdf.mm_to_pt(285.75)))
    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert([str(p) for p in paths], layout_fun=layout))
    return pdf_path


# ============================================================
# CONTENIDO DE HOY — esto SÍ se edita cada día.
# El ejemplo de abajo ("5 señales de indexación silenciosa") es la
# plantilla de referencia validada visualmente con Jorge el 24/08/2026;
# mantenla como base y sustituye textos, no la estructura de tipos salvo
# que el ángulo del día lo pida (ver AUTOMATION_BRIEF.md sección 3 para
# qué combinación de tipos usar según el día de la semana).
# ============================================================

CONFIG = {
    "kicker": "MEJORA SEO · ECOMMERCE",
    "footer_note": 'COMENTA "INDEXACION" Y TE LO ENVÍO',  # editar cada día — misma palabra que en post-linkedin.txt
    "slides": [
        {
            "type": "cover",
            "guide_badge": {
                "number": 1,  # día 1 desde el lanzamiento de la guía en Notion (03/09/2026), +1 cada día — ver AUTOMATION_BRIEF.md §3.3
                "line": "Te doy acceso a una guia SEO para ecommerce, actualizada cada dia.",
            },
            "title_lines": [
                [("5 SEÑALES", True)],
                [("DE INDEXACION", False)],
                [("SILENCIOSA", True)],
            ],
            "subtitle": "Ninguna rompe la tienda. Ninguna da error. Por eso "
                        "nadie las revisa — y por eso te cuestan trafico, mes tras mes.",
        },
        {
            "type": "statement",
            "title_lines": [
                [("Tu ecommerce", False)],
                [("puede estar", False)],
                [("perdiendo trafico", False)],
                [("ahora mismo.", False)],
            ],
            "closing": [("Y no te vas a enterar", True)],
        },
        {
            "type": "statement",
            "title_lines": [
                [("TU TIENDA", False)],
                [("FUNCIONA BIEN.", False)],
                [("¿SEGURO?", True)],
            ],
            "body": "Ninguna de estas 5 señales da un error visible. Ninguna "
                    "rompe el checkout. Por eso nadie las revisa.",
            "closing": [("Vamos a auditarlo.", True)],
        },
        {
            "type": "bullets",
            "title_lines": [
                [("¿POR QUÉ", False), ("IMPORTA", True)],
                [("ESTO EN TU", False)],
                [("ECOMMERCE?", True)],
            ],
            "intro": "La indexacion silenciosa no es un \"nice to have\". Es:",
            "items": [
                "Categorias que dejan de posicionar",
                "Fichas de producto compitiendo con su propio filtro",
                "Trafico que se va sin que salte ninguna alarma",
            ],
            "closing": "Los ecommerce que lo revisan a tiempo, escalan sin sorpresas.",
        },
        {
            "type": "card",
            "label": "SEÑAL 1",
            "headline": "Tus filtros de categoria generan URLs infinitas",
            "body": "(?color=, ?talla=...) y todas indexadas.",
            "checks": [
                "¿Los filtros tienen volumen de busqueda real?",
                "¿O generan miles de combinaciones sin sentido?",
            ],
        },
        {
            "type": "card",
            "label": "SEÑAL 2",
            "headline": "Tu paginacion no recibe ni un enlace interno",
            "body": "(pagina 2, 3, 4...).",
            "checks": [
                "¿Cada pagina se alcanza en 2 clics desde la categoria?",
                "¿O solo existe la pagina 1 para Google?",
            ],
        },
        {
            "type": "card",
            "label": "SEÑAL 3",
            "headline": "Productos agotados siguen indexados meses despues",
            "body": "sin stock ni fecha de vuelta.",
            "checks": [
                "¿Sabes cuantos agotados llevas indexados ahora?",
                "¿Devuelven 410 o siguen como si nada?",
            ],
        },
        {
            "type": "card",
            "label": "SEÑAL 4",
            "headline": "Tienes dos URLs para la misma ficha",
            "body": "(con/sin barra final, con/sin mayusculas).",
            "checks": [
                "¿Cada producto tiene una unica URL canonica?",
                "¿O Google ve 3-4 versiones del mismo producto?",
            ],
        },
        {
            "type": "card",
            "label": "SEÑAL 5",
            "headline": "El sitemap.xml lleva URLs que dan 404",
            "body": "o que estan marcadas noindex.",
            "checks": [
                "¿Cuando revisaste tu sitemap por ultima vez?",
                "¿Sabes si Google confia todavia en el?",
            ],
        },
        {
            "type": "closing",
            "title_lines": [
                [("SI HAS LLEGADO", False)],
                [("HASTA AQUI...", True)],
            ],
            "ctas": [
                ("Comenta tu numero", "0 a 5 — cuantas señales tienes ahora mismo"),
                ("Guarda este post", "lo vas a necesitar cuando audites tu tienda"),
                ("Compartelo", "con quien lleve el SEO de un ecommerce"),
            ],
            "box_title": "El paso a paso completo para corregir las 5 señales:",
            "box_link": 'COMENTA "INDEXACION" Y TE LO ENVÍO',
        },
    ],
}


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    n = render_all(CONFIG)
    p = build_pdf(n)
    print(f"Listo: {n} slides ->", p)
