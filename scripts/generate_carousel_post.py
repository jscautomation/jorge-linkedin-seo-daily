# -*- coding: utf-8 -*-
"""
Genera el carrusel/documento del post de LinkedIn — formato "tech oscuro"
(1440x1440), vigente desde el 03/09/2026 (segundo cambio de estilo el mismo
día: sustituye a la versión "documento crema" de esa misma mañana). Jorge
pidió acercar el diseño al de un perfil de referencia (Pablo Rodríguez /
GoToMarket) — tipografía de alto impacto, fondo oscuro, una pieza visual
fuerte (su foto) en portada — pero manteniendo los colores corporativos
propios (negro + naranja de marca, no los colores del perfil de referencia)
y corrigiendo el pixelado que se veía en el logo y el avatar del formato
anterior.

Cómo funciona (leer también AUTOMATION_BRIEF.md sección 3 — guía de estilo
completa):

- El MOTOR DE RENDER (todo lo de arriba de "CONTENIDO DE HOY") es FIJO.
  No tocar tamaños, colores, posiciones ni límites salvo que Jorge pida
  explícitamente un cambio de estilo.
- El CONTENIDO (CONFIG al final del archivo) SÍ se edita cada día: lista de
  slides, cada una un diccionario con un "type" de entre
  cover | statement | bullets | card | closing. La forma de cada tipo NO
  cambió respecto al formato anterior (mismos campos) — solo cambió el
  render. Edita CONFIG, ejecuta el script, mueve el resultado a
  `content/<carpeta-del-día>/`, y revierte el archivo con
  `git checkout -- scripts/generate_carousel_post.py`.

Qué corrige este cambio de versión respecto al anterior (mismo día,
03/09/2026), a petición expresa de Jorge tras ver el primer resultado:

- **Pixelado de logo/avatar**: el logo de marca (`assets/branding/logo.png`,
  300x213px) es un archivo de origen de baja resolución — ampliarlo o
  reducirlo con cualquier filtro no lo arregla, así que se ha sustituido
  por un LOGOTIPO DE TEXTO ("JORGE SEGOVIA" en las dos tipografías de
  marca) dibujado directamente con PIL: es vectorial en el sentido de que
  se renderiza nítido a cualquier tamaño, nunca pixelado. Si Jorge sube un
  archivo de logo de mayor resolución (>=1200px de ancho) o un SVG,
  se puede volver a pegar como imagen — mientras tanto, texto.
- El avatar (`assets/branding/foto-jorge-circle.png`) SÍ es una foto (no se
  puede "vectorizar"), así que aquí se aplica (a) remuestreo LANCZOS al
  reducir (nunca ampliar más allá del tamaño nativo) y (b) un
  UnsharpMask moderado tras el resize para compensar la suavidad de origen
  del archivo. Sigue sin ser un archivo perfecto — si Jorge sube una foto
  de mayor nitidez en el futuro, quitar el UnsharpMask o bajar su
  intensidad (`PHOTO_SHARPEN`).
- **Resolución del lienzo**: sube de 1080x1080 a 1440x1440 (misma relación
  de aspecto 1:1, todas las proporciones internas escaladas en la misma
  medida — ver `S` más abajo). El PDF sigue maquetado al mismo tamaño
  físico (28.575 cm) que antes, así que el cambio real es más densidad de
  píxel por cm — se ve más nítido al hacer zoom en LinkedIn sin cambiar el
  formato de publicación (sigue siendo un documento PDF deslizable).

Salida: `carrusel-1.png` ... `carrusel-N.png` (una por slide) +
`carrusel-post.pdf` (empaquetado SIN pérdida vía img2pdf). Sube el PDF a
LinkedIn como publicación de tipo Documento.

Uso: python3 scripts/generate_carousel_post.py content/<carpeta-del-día>
(si se omite la carpeta, usa una ruta por defecto — ver OUT_DIR).
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import img2pdf

REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = REPO_ROOT / "assets" / "fonts"
PHOTO_PATH = REPO_ROOT / "assets" / "branding" / "foto-jorge-circle.png"
OUT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "carrusel-hoy"

# ============================================================
# MOTOR DE RENDER — fijo, no tocar sin instrucción expresa de Jorge.
# Ver AUTOMATION_BRIEF.md sección 3 para la guía de estilo completa.
# ============================================================

S = 4 / 3  # factor de escala respecto al lienzo anterior (1080 -> 1440);
# se deja explícito en vez de re-fijar cada número a mano, para que si en
# el futuro hace falta otro salto de resolución, sea un único cambio.
W = H = 1440
MARGIN_X = 76

# Paleta "tech oscuro" (hex de referencia entre paréntesis). Colores
# corporativos de Jorge sin cambios (negro + naranja de marca) — lo que
# cambia es que el negro pasa a ser el fondo (antes era el crema) y el
# naranja gana peso como acento sobre oscuro, más parecido al contraste de
# alto impacto del perfil de referencia que Jorge señaló.
BG = (10, 11, 13)          # #0A0B0D — negro azulado, no negro puro (más "tech" que plano)
GRID = (26, 28, 32)        # #1A1C20 — puntos de la rejilla decorativa, apenas visibles
TEXT = (245, 244, 240)     # #F5F4F0 — texto principal, blanco roto sobre oscuro
ORANGE = (255, 90, 31)     # #FF5A1F — color de marca; resaltados, acentos, anillo de foto
INK = (17, 17, 17)         # #111111 — texto sobre fondo naranja (contraste, sin cambios)
GRAY = (139, 141, 147)     # #8B8D93 — texto secundario/kicker sobre oscuro
GUIDE_BADGE_BG = (32, 35, 41)  # #202329 — recuadro de la guía en portada; gris
# oscuro DISTINTO del fondo (para que resalte) y del naranja (para no competir
# visualmente con el CTA) — ver AUTOMATION_BRIEF.md sección 3.3.

TITLE = "ArchivoBlack-Regular.ttf"
BOLD = "Barlow-Bold.ttf"


def F(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


# Tamaños de fuente por ROL — todos escalados x S respecto al formato
# anterior de 1080px, para conservar exactamente las mismas proporciones
# ya validadas visualmente, solo que con más densidad de píxel.
TITLE_XL = 112
LINE_H_XL = 176
TITLE_L = 90
LINE_H_L = 138
TITLE_MED = 82
HEADLINE = 66
LINE_H_HEADLINE = 132
BODY = 37
LINE_H_BODY = 50
BULLET_SIZE = 34
SMALL = 26

TITLE_SAFE_TOP = 200
FOOTER_SAFE_BOTTOM = 1306
COVER_SUBTITLE_MAX_W = 1060

# Foto: nitidez de compensación (ver nota de cabecera del archivo — el
# archivo de origen es algo blando; esto no lo arregla del todo, solo lo
# disimula). Bajar `PHOTO_SHARPEN_PCT` si Jorge sube una foto ya nítida.
PHOTO_SHARPEN_PCT = 160
PHOTO_SHARPEN_RADIUS = 2.4


def rr(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def canvas():
    """Fondo oscuro + rejilla de puntos (en vez de líneas continuas) — más
    "blueprint técnico" que "libreta", a juego con el resto de motivos
    tech (esquinas tipo visor) de este formato."""
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    step = 96
    for x in range(step, W, step):
        for y in range(step, H, step):
            d.ellipse((x - 2, y - 2, x + 2, y + 2), fill=GRID)
    return img, d


def corner_brackets(d, inset=40, arm=44, width=3, color=ORANGE):
    """Marcas de esquina tipo visor/HUD en las 4 esquinas — motivo "tech"
    discreto, presente en todas las slides."""
    corners = [
        (inset, inset, 1, 1),                    # arriba-izq: brazos hacia +x/+y
        (W - inset, inset, -1, 1),                # arriba-dcha
        (inset, H - inset, 1, -1),                # abajo-izq
        (W - inset, H - inset, -1, -1),           # abajo-dcha
    ]
    for x, y, sx, sy in corners:
        d.line((x, y, x + arm * sx, y), fill=color, width=width)
        d.line((x, y, x, y + arm * sy), fill=color, width=width)


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


def draw_tracked(draw, xy, text, font, fill, tracking=6):
    """Dibuja texto con espaciado entre letras (letter-spacing) — PIL no lo
    soporta de forma nativa, así que se dibuja carácter a carácter. Se usa
    SOLO para etiquetas cortas en mayúsculas (kicker) — a este tamaño de
    texto normal sería ilegible."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        w = draw.textbbox((0, 0), ch, font=font)[2]
        x += w + tracking
    return x


def draw_mixed_line(draw, x, y, parts, font, pad=12, radius=13, plain_fill=TEXT, measure_only=False):
    """parts: lista de (texto, es_resaltado). Dibuja en una sola línea, con
    caja naranja redondeada detrás de los fragmentos resaltados (texto en
    negro sobre naranja). Usa textbbox ya anclado en la posición real de
    dibujo (no en (0,0)) para que la caja quede pegada al texto de verdad.

    `measure_only=True` no dibuja nada, solo devuelve la coordenada x
    final — así `assert_line_fits()` comprueba el ancho real con
    exactamente la misma lógica que el dibujado de verdad."""
    cx = x
    for text, hl in parts:
        bbox = draw.textbbox((cx, y), text, font=font)
        if hl:
            box = (bbox[0] - pad, bbox[1] - 8, bbox[2] + pad, bbox[3] + 8)
            if not measure_only:
                rr(draw, box, radius, fill=ORANGE)
                draw.text((cx, y), text, font=font, fill=INK)
            cx = box[2] + 16
        else:
            if not measure_only:
                draw.text((cx, y), text, font=font, fill=plain_fill)
            cx = bbox[2] + 19
    return cx


def assert_line_fits(d, parts, font, context="", limit=None):
    """Comprueba, ANTES de dibujar, que una línea de título no se sale del
    lienzo (o de la columna de texto, en portada, si hay foto grande
    debajo) por la derecha. Falla alto y claro en vez de dejar un PNG con
    el texto cortado."""
    end_x = draw_mixed_line(d, MARGIN_X, 0, parts, font, measure_only=True)
    lim = W - 32 if limit is None else limit
    assert end_x <= lim, (
        f"Línea demasiado ancha ({end_x}px, máximo {lim}px) en {context or parts!r} "
        "— acorta el texto o pártelo en más líneas."
    )


def highlighted_wrapped(draw, x, y, text, font, max_w, line_h):
    """Como draw_wrapped pero cada línea resultante se dibuja entera
    resaltada — para un titular largo que no cabe en una sola línea."""
    for ln in wrap(draw, text, font, max_w):
        draw_mixed_line(draw, x, y, [(ln, True)], font)
        y += line_h
    return y


def _sharpened_photo():
    im = Image.open(PHOTO_PATH).convert("RGB")
    return im


PHOTO_SRC = _sharpened_photo()


def circular_photo(diam, ring_width, centering=(0.5, 0.22)):
    """Foto de Jorge recortada en círculo + anillo naranja de marca. Se usa
    tanto para la insignia pequeña de cabecera (todas las slides) como para
    la foto grande de portada — mismo tratamiento, solo cambia el tamaño.
    LANCZOS al reducir + UnsharpMask moderado (ver nota de cabecera del
    archivo: compensa que el archivo de origen es algo blando; no lo
    arregla del todo)."""
    photo = ImageOps.fit(PHOTO_SRC, (diam, diam), centering=centering, method=Image.LANCZOS)
    photo = photo.filter(ImageFilter.UnsharpMask(radius=PHOTO_SHARPEN_RADIUS, percent=PHOTO_SHARPEN_PCT, threshold=2))
    mask = Image.new("L", (diam, diam), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diam, diam), fill=255)
    ring_d = diam + ring_width * 2
    ring = Image.new("RGBA", (ring_d, ring_d), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, ring_d, ring_d), fill=ORANGE + (255,))
    ring.paste(photo, (ring_width, ring_width), mask)
    return ring, ring_d


BADGE_RING, BADGE_RING_D = circular_photo(diam=118, ring_width=6)
HERO_RING, HERO_RING_D = circular_photo(diam=410, ring_width=14, centering=(0.5, 0.18))


def wordmark(d, x, y):
    """Logotipo de marca dibujado como TEXTO (no imagen) — el archivo de
    logo real (`assets/branding/logo.png`) es de baja resolución
    (300x213px); cualquier redimensionado se ve pixelado. El texto,
    dibujado directamente con las fuentes de marca, es nítido a cualquier
    tamaño. Si Jorge sube un logo de mayor resolución (>=1200px de ancho o
    SVG), se puede reemplazar esto por una imagen otra vez."""
    f_main = F(BOLD, 34)
    x2 = d.textbbox((x, y), "JORGE ", font=f_main)[2]
    d.text((x, y), "JORGE ", font=f_main, fill=TEXT)
    d.text((x2, y), "SEGOVIA", font=f_main, fill=ORANGE)


def header(img, d):
    """Logotipo de texto arriba a la izquierda + insignia circular de foto
    arriba a la derecha — mismo sitio en TODAS las slides, incluida la de
    cierre."""
    wordmark(d, MARGIN_X, 54)
    img.paste(BADGE_RING, (W - BADGE_RING_D - MARGIN_X, 40), BADGE_RING)


def kicker(d, text):
    """Etiqueta pequeña bajo la cabecera — el tema del día en mayúsculas,
    con tracking (letter-spacing) y un punto de estado delante, para un
    aire más "panel técnico" que texto suelto."""
    y = 141
    d.ellipse((MARGIN_X, y + 6, MARGIN_X + 12, y + 18), fill=ORANGE)
    draw_tracked(d, (MARGIN_X + 26, y), text, F(BOLD, SMALL), GRAY, tracking=3)


GUIDE_BADGE_TOP = 196  # y donde empieza el recuadro, debajo del kicker
GUIDE_BADGE_H = 84


GUIDE_BADGE_TEMPLATE = "Mejora nº{n}: GUÍA DE VENTAS CON SEO ACTUALIZADA CADA DÍA."
# Texto FIJO (vigente desde el 04/09/2026, a petición expresa de Jorge —
# sustituye al patrón anterior "MEJORA Nº<N> · Te doy acceso a..."). Solo
# cambia `{n}`; no se edita por día salvo instrucción expresa de Jorge.


def guide_badge(d, spec):
    """Recuadro de la guía en la portada (AUTOMATION_BRIEF.md sección 3.3):
    gris oscuro (ni el fondo ni el naranja del CTA, para no competir con
    ninguno de los dos), texto en blanco, patrón fijo `GUIDE_BADGE_TEMPLATE`.
    `spec` es el diccionario `guide_badge` del slide `cover`: {"number": N}.
    Devuelve la y donde puede empezar lo siguiente (el título) — SIEMPRE se
    llama antes de dibujar el título en `render_cover`, nunca al revés."""
    box = (MARGIN_X, GUIDE_BADGE_TOP, W - MARGIN_X, GUIDE_BADGE_TOP + GUIDE_BADGE_H)
    rr(d, box, radius=GUIDE_BADGE_H // 2, fill=GUIDE_BADGE_BG)
    text = GUIDE_BADGE_TEMPLATE.format(n=spec["number"])
    font = F(BOLD, 27)
    max_w = box[2] - box[0] - 56
    lines = wrap(d, text, font, max_w)
    assert len(lines) <= 2, (
        f"guide_badge: el texto no cabe en 2 líneas dentro del recuadro ({text!r}) "
        "— sube GUIDE_BADGE_H (el texto es fijo, GUIDE_BADGE_TEMPLATE)."
    )
    line_h = 32
    y0 = box[1] + GUIDE_BADGE_H // 2 - (len(lines) * line_h) // 2 + 4
    for ln in lines:
        d.text((box[0] + 28, y0), ln, font=font, fill=TEXT)
        y0 += line_h
    return box[3]


DEFAULT_FOOTER_NOTE = 'COMENTA "<PALABRA>" Y TE LO ENVÍO'  # sustituye <PALABRA> en CONFIG cada día
FOOTER_NOTE_FONT_SIZE = 34  # FIJO — nunca variar entre slides ni auto-ajustar al ancho del texto


def footer_gate_note(img, d, text=DEFAULT_FOOTER_NOTE):
    """Recordatorio de la regla no negociable (brief sección 2, punto 4): la
    solución completa vive solo en la guía de Notion, nunca en el carrusel.
    Va en TODAS las slides menos la de cierre (que ya lleva su propio CTA
    grande con el mismo mensaje). Caja naranja + texto blanco + flecha
    blanca dibujada a mano, todo dentro de la caja."""
    font = F(TITLE, FOOTER_NOTE_FONT_SIZE)
    pad_x, pad_y = 29, 21
    arrow_w = 45

    bbox = d.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    box_h = text_h + pad_y * 2
    box_w = arrow_w + text_w + pad_x * 2
    x0, y0 = MARGIN_X, H - 53 - box_h
    x1, y1 = x0 + box_w, y0 + box_h

    rr(d, (x0, y0, x1, y1), radius=box_h // 2, fill=ORANGE)

    ax, ay = x0 + pad_x + 12, y0 + box_h // 2 - 15
    d.line((ax, ay, ax, ay + 29), fill=(255, 255, 255), width=6)
    d.line((ax - 12, ay + 15, ax, ay + 29), fill=(255, 255, 255), width=6)
    d.line((ax + 12, ay + 15, ax, ay + 29), fill=(255, 255, 255), width=6)

    tx = x0 + pad_x + arrow_w
    ty = y0 + box_h // 2 - text_h // 2 - bbox[1]
    d.text((tx, ty), text, font=font, fill=(255, 255, 255))


def scroll_hint(img, last=False):
    """Barra degradada + flecha circular abajo a la derecha, indicando que
    hay más slides — en la última slide de contenido (justo antes del
    cierre) la flecha se convierte en un check."""
    bw, bh = 83, 253
    grad = Image.new("RGB", (1, bh), BG)
    for y in range(bh):
        t = y / (bh - 1)
        col = tuple(int(ORANGE[i] * (1 - t) + BG[i] * t) for i in range(3))
        grad.putpixel((0, y), col)
    grad = grad.resize((bw, bh))
    mask = Image.new("L", (bw, bh), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, bw, bh), radius=bw // 2)
    bx, by = W - bw - 99, 915
    img.paste(grad, (bx, by), mask)

    cx, cy, r = bx + bw // 2, by + bh + 61, 56
    d = ImageDraw.Draw(img)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=ORANGE)
    if last:
        d.line((cx - 20, cy, cx - 5, cy + 17), fill=INK, width=9)
        d.line((cx - 5, cy + 17, cx + 21, cy - 16), fill=INK, width=9)
    else:
        d.line((cx - 19, cy, cx + 19, cy), fill=INK, width=9)
        d.line((cx + 5, cy - 15, cx + 20, cy), fill=INK, width=9)
        d.line((cx + 5, cy + 15, cx + 20, cy), fill=INK, width=9)


def arrow_bullets(d, x, y, items, gap=82):
    """Lista con flecha dibujada a mano — para el tipo "bullets"."""
    for line in items:
        ay = y + 21
        d.line((x, ay, x + 27, ay), fill=ORANGE, width=7)
        d.line((x + 16, ay - 9, x + 29, ay), fill=ORANGE, width=7)
        d.line((x + 16, ay + 9, x + 29, ay), fill=ORANGE, width=7)
        y = draw_wrapped(d, (x + 56, y), line, F(BOLD, BULLET_SIZE), TEXT, W - x - 56 - 144, 42)
        y += gap - 42
    return y


def ring_checks(d, x, y, items, gap=106):
    """Lista de preguntas de autocomprobación con un pequeño anillo — para
    el campo `checks` del tipo "card"."""
    for c in items:
        d.ellipse((x, y + 13, x + 16, y + 29), outline=ORANGE, width=4)
        draw_wrapped(d, (x + 48, y), c, F(BOLD, BULLET_SIZE), TEXT, W - x - 48 - 144, 45)
        y += gap
    return y


# ------------------------------------------------------------------
# Un renderer por cada "type" de slide soportado. Todos comparten firma
# (img, d, spec, index, total) aunque no usen index/total.
# ------------------------------------------------------------------

def render_cover(img, d, spec, index, total):
    """Portada: recuadro de la guía (`guide_badge`, opcional pero estándar
    desde el 03/09/2026 — sección 3.3), título (máx. 3 líneas — deja hueco
    para la foto grande de abajo), subtítulo opcional, y la foto de Jorge en
    grande, tipo "medallón" con anillo naranja, ALINEADA A LA DERECHA (a
    petición expresa de Jorge, 04/09/2026 — antes centrada) — la pieza
    visual fuerte que pidió Jorge, en la línea de las publicaciones de
    referencia (una prueba/cara real grande, no solo texto).

    Presupuesto vertical ajustado: con `guide_badge` Y `subtitle` a la vez,
    más 3 líneas de título, el contenido puede empujar la foto grande fuera
    del lienzo — por eso, si usas `guide_badge`, omite `subtitle` salvo que
    el título ocupe menos de 3 líneas (el assert de abajo avisa si no cabe,
    en vez de recortar la foto en silencio)."""
    title_lines = spec["title_lines"]
    has_badge = bool(spec.get("guide_badge"))
    assert len(title_lines) <= 3, "cover: máximo 3 líneas de título — deja hueco a la foto grande"
    y = TITLE_SAFE_TOP
    if has_badge:
        badge_bottom = guide_badge(d, spec["guide_badge"])
        y = badge_bottom + 24
    for line in title_lines:
        assert_line_fits(d, line, F(TITLE, TITLE_XL), context=f"cover: {line}")
        draw_mixed_line(d, MARGIN_X, y, line, F(TITLE, TITLE_XL))
        y += LINE_H_XL
    if spec.get("subtitle"):
        y = draw_wrapped(d, (MARGIN_X, y + 20), spec["subtitle"], F(BOLD, BODY), GRAY,
                          COVER_SUBTITLE_MAX_W, LINE_H_BODY)
    top = max(y + 20, 780)
    assert top + HERO_RING_D <= H - 150, (
        f"cover: la foto grande no cabe (empezaría en y={top}, el lienzo mide "
        f"{H}px y hay que dejar sitio al recuadro naranja de abajo) — quita el "
        "`subtitle`, acorta el título a menos líneas, o prescinde del "
        "`guide_badge` en este slide."
    )
    img.paste(HERO_RING, (W - MARGIN_X - HERO_RING_D, top), HERO_RING)


def render_statement(img, d, spec, index, total):
    """Slide de "declaración" grande: 1-3 líneas de título, más
    opcionalmente un párrafo de cuerpo y/o una línea de cierre resaltada."""
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
        y += 45
        y = draw_wrapped(d, (MARGIN_X, y), spec["body"], F(BOLD, 40), TEXT, W - 2 * MARGIN_X, 53)
    if spec.get("closing"):
        y += 53
        draw_mixed_line(d, MARGIN_X, y, spec["closing"], F(TITLE, TITLE_MED))


def render_bullets(img, d, spec, index, total):
    """Título grande + intro + lista de 2-4 items con flecha + cierre
    (gris, opcional). Para "por qué importa esto"."""
    title_lines = spec["title_lines"]
    assert len(title_lines) <= 3, "bullets: máximo 3 líneas de título"
    assert 2 <= len(spec["items"]) <= 4, "bullets: entre 2 y 4 items"
    y = TITLE_SAFE_TOP
    for line in title_lines:
        assert_line_fits(d, line, F(TITLE, TITLE_XL), context=f"bullets: {line}")
        draw_mixed_line(d, MARGIN_X, y, line, F(TITLE, TITLE_XL))
        y += LINE_H_XL
    y += 53
    if spec.get("intro"):
        y = draw_wrapped(d, (MARGIN_X, y), spec["intro"], F(BOLD, BODY), TEXT, W - 2 * MARGIN_X, 48)
        y += 45
    y = arrow_bullets(d, MARGIN_X, y, spec["items"])
    if spec.get("closing"):
        y += 27
        draw_wrapped(d, (MARGIN_X, y), spec["closing"], F(BOLD, BODY), GRAY, W - 2 * MARGIN_X, 48)


def render_card(img, d, spec, index, total):
    """Una tarjeta = un hallazgo/paso/dato por slide: etiqueta + titular
    resaltado (envuelto automáticamente) + cuerpo corto + hasta 2 preguntas
    de autocomprobación, dentro de un panel con borde fino (efecto "panel
    técnico / salida de terminal")."""
    checks = spec.get("checks") or []
    assert len(checks) <= 2, "card: máximo 2 items en `checks`"
    y = 200
    label_line = [(spec["label"] + ":", False)]
    assert_line_fits(d, label_line, F(TITLE, TITLE_MED), context=f"card label: {spec['label']}")
    draw_mixed_line(d, MARGIN_X, y, label_line, F(TITLE, TITLE_MED))
    y += 149
    y = highlighted_wrapped(d, MARGIN_X, y, spec["headline"].upper(), F(TITLE, HEADLINE),
                             W - MARGIN_X - 74, LINE_H_HEADLINE)
    y += 53
    panel_top = y - 20
    if spec.get("body"):
        y = draw_wrapped(d, (MARGIN_X, y), spec["body"], F(BOLD, BODY), TEXT, W - 2 * MARGIN_X, LINE_H_BODY)
        y += 147
    if checks:
        d.text((MARGIN_X, y), "Comprueba tú mismo:", font=F(BOLD, 32), fill=GRAY)
        y += 75
        y = ring_checks(d, MARGIN_X, y, checks)
    rr(d, (MARGIN_X - 24, panel_top, W - MARGIN_X + 24, y + 4), radius=20, outline=GRID, width=2)


def render_closing(img, d, spec, index, total):
    """Última slide: título de 2 líneas + hasta 3 CTAs numerados + el ÚNICO
    bloque fuerte con el CTA de comentario."""
    title_lines = spec["title_lines"]
    assert len(title_lines) == 2, "closing: exactamente 2 líneas de título"
    ctas = spec["ctas"]
    assert len(ctas) <= 3, "closing: máximo 3 CTAs"

    y = 200
    for line in title_lines:
        assert_line_fits(d, line, F(TITLE, TITLE_L), context=f"closing: {line}")
        draw_mixed_line(d, MARGIN_X, y, line, F(TITLE, TITLE_L))
        y += LINE_H_L
    y += 59

    for i, (title, sub) in enumerate(ctas, start=1):
        d.ellipse((MARGIN_X, y, MARGIN_X + 53, y + 53), fill=ORANGE)
        d.text((MARGIN_X + 27, y + 27), str(i), font=F(TITLE, 27), fill=INK, anchor="mm")
        draw_mixed_line(d, MARGIN_X + 80, y + 3, [(title, False)], F(TITLE, 33))
        draw_wrapped(d, (MARGIN_X + 80, y + 59), sub, F(BOLD, 25), GRAY, W - MARGIN_X - 80 - 74, 32)
        y += 133

    box = (MARGIN_X, y + 27, W - MARGIN_X, y + 293)
    rr(d, box, 29, fill=ORANGE)
    draw_wrapped(d, (box[0] + 43, box[1] + 35), spec["box_title"], F(TITLE, 33), INK,
                 box[2] - box[0] - 85, 42)
    d.text((box[0] + 43, box[3] - 80), spec["box_link"], font=F(TITLE, 29), fill=INK)


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
        corner_brackets(d)
        header(img, d)
        kicker(d, config["kicker"])
        RENDERERS[spec["type"]](img, d, spec, i, total)
        if spec["type"] != "closing":
            footer_gate_note(img, d, config.get("footer_note", DEFAULT_FOOTER_NOTE))
            # La portada no lleva flecha de scroll: la foto grande, alineada
            # a la derecha (04/09/2026), ocupa esa misma esquina.
            if spec["type"] != "cover":
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
# ============================================================

CONFIG = {
    "kicker": "MEJORA SEO · ECOMMERCE",
    "footer_note": 'COMENTA "INDEXACION" Y TE LO ENVÍO',  # editar cada día — misma palabra que en post-linkedin.txt
    "slides": [
        {
            "type": "cover",
            # guide_badge: recuadro gris de la portada (sección 3.3) — solo
            # `number`, que sube +1 cada día publicado desde el 03/09/2026
            # (día 1). El texto es fijo (GUIDE_BADGE_TEMPLATE en el motor),
            # no se edita por día.
            "guide_badge": {
                "number": 1,
            },
            # Titular SIEMPRE en clave de ventas (sección 0 y 3.3) — nunca abrir
            # con un término SEO como "indexación"; el mecanismo técnico va en
            # el subtitle o en las slides siguientes, nunca en el título.
            # Máximo 3 líneas — el assert de render_cover avisa si no cabe
            # (la foto grande, alineada a la derecha, va debajo del título).
            "title_lines": [
                [("ESTAS PERDIENDO", False)],
                [("VENTAS", True)],
                [("EN TU ECOMMERCE", False)],
            ],
            # Sin `subtitle`: con `guide_badge` ya no queda presupuesto
            # vertical para él sin sacar la foto del lienzo (ver assert de
            # render_cover).
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
