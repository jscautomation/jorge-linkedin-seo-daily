# -*- coding: utf-8 -*-
"""
Genera el post de LinkedIn en formato CARRUSEL cuadrado (1080x1080), estilo
"captura anotada a mano" — 5 slides + PDF multipagina listo para subir a
LinkedIn como documento. Nace como sustituto del formato "imagen unica"
(scripts/generate_post_image.py) para los dias en los que el angulo pide
mas desarrollo (varios puntos, resumen semanal...). Los dos formatos
conviven por ahora — cual usar cada dia se decide caso a caso.

Estado actual: el contenido de cada slide se define en las funciones
slide_1..slide_5 mas abajo (no hay todavia un CONFIG de variables sueltas
como en generate_post_image.py / generate_lead_magnet_pdf.py, porque cada
carrusel tiene una estructura narrativa distinta segun el angulo del dia
— roast, mito, resumen semanal... formalizarlo del todo es trabajo futuro
si este formato se adopta como estandar).

Uso: python3 scripts/generate_carousel_post.py content/<carpeta-del-dia>
(genera carrusel-1..5.png + carrusel-post.pdf dentro de esa carpeta)
"""
import math
import random
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import img2pdf

REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = REPO_ROOT / "assets" / "fonts"
PHOTO_PATH = REPO_ROOT / "assets" / "branding" / "foto-jorge.jpg"
OUT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "2026-08-21-viernes-resumen"

W = H = 1080
PAPER = (250, 246, 237)
WHITE = (255, 255, 255)
INK = (17, 17, 17)
ORANGE = (255, 90, 31)
RED = (222, 45, 38)
YELLOW = (255, 209, 60)
GRAY = (130, 130, 122)
CHROME = (232, 228, 216)


def F(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


TITLE = "ArchivoBlack-Regular.ttf"
BOLD = "Barlow-Bold.ttf"


def rr(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def canvas():
    img = Image.new("RGB", (W, H), PAPER)
    return img, ImageDraw.Draw(img)


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


# ------------------------------------------------------------------
# Garabatos a mano
# ------------------------------------------------------------------
def _jitter_path(points, jitter, subdiv=6):
    out = []
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        for t in range(subdiv):
            tt = t / subdiv
            x = x0 + (x1 - x0) * tt + random.uniform(-jitter, jitter)
            y = y0 + (y1 - y0) * tt + random.uniform(-jitter, jitter)
            out.append((x, y))
    out.append(points[-1])
    return out


def scribble_line(draw, points, color, width=6, jitter=3, passes=2):
    for p in range(passes):
        draw.line(_jitter_path(points, jitter), fill=color, width=width, joint="curve")


def scribble_circle(draw, cx, cy, rx, ry, color, width=7, passes=2, tilt=0.0):
    for p in range(passes):
        pts = []
        start = random.uniform(-0.3, 0.3)
        for i in range(37):
            ang = start + (2 * math.pi + 0.5) * i / 36
            jr = random.uniform(-4, 4)
            pts.append((cx + (rx + jr) * math.cos(ang + tilt), cy + (ry + jr) * math.sin(ang + tilt)))
        draw.line(pts, fill=color, width=width, joint="curve")


def scribble_arrow(draw, p0, p1, color, width=8, jitter=4, head=24):
    scribble_line(draw, [p0, p1], color, width=width, jitter=jitter, passes=2)
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for side in (0.5, -0.5):
        hx = p1[0] - head * math.cos(ang + side)
        hy = p1[1] - head * math.sin(ang + side)
        draw.line((p1[0], p1[1], hx, hy), fill=color, width=width)


def tape(img, cx, cy, w=110, h=38, angle=-8, color=(255, 235, 150, 190)):
    layer = Image.new("RGBA", (w, h), color)
    layer = layer.rotate(angle, expand=True)
    img.paste(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)), layer)


def stamp_text(img, cx, cy, text, f, fill, angle=-6, stroke_fill=None, stroke_w=0):
    dummy = Image.new("RGBA", (10, 10))
    dd = ImageDraw.Draw(dummy)
    bbox = dd.textbbox((0, 0), text, font=f, stroke_width=stroke_w)
    pad = 14
    tw, th = bbox[2] - bbox[0] + pad * 2, bbox[3] - bbox[1] + pad * 2
    layer = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.text((pad - bbox[0], pad - bbox[1]), text, font=f, fill=fill, stroke_width=stroke_w, stroke_fill=stroke_fill)
    layer = layer.rotate(angle, expand=True, resample=Image.BICUBIC)
    img.paste(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)), layer)


def ribbon(img, cy, text, bg, fg, angle=-2.2, band_h=68, f=None):
    f = f or F(TITLE, 30)
    layer_w = W + 220
    layer = Image.new("RGBA", (layer_w, band_h), bg + (255,))
    ld = ImageDraw.Draw(layer)
    ld.text((layer_w / 2, band_h / 2), text, font=f, fill=fg, anchor="mm")
    rot = layer.rotate(angle, expand=True, resample=Image.BICUBIC)
    img.paste(rot, (int(W / 2 - rot.width / 2), int(cy - rot.height / 2)), rot)


def browser_chrome(draw, box, url_text):
    x0, y0, x1, y1 = box
    rr(draw, box, 16, fill=(255, 255, 255), outline=INK, width=4)
    bar_h = 50
    rr(draw, (x0, y0, x1, y0 + bar_h), 16, fill=CHROME)
    draw.rectangle((x0, y0 + bar_h - 16, x1, y0 + bar_h), fill=CHROME)
    for i, c in enumerate([RED, YELLOW, (100, 180, 100)]):
        cx = x0 + 24 + i * 24
        draw.ellipse((cx - 7, y0 + bar_h / 2 - 7, cx + 7, y0 + bar_h / 2 + 7), fill=c)
    rr(draw, (x0 + 100, y0 + 10, x1 - 18, y0 + bar_h - 10), 12, outline=GRAY, width=2)
    draw.text((x0 + 116, y0 + bar_h / 2), url_text, font=F(BOLD, 17), fill=(70, 70, 70), anchor="lm")
    return (x0, y0 + bar_h, x1, y1)


def top_row(draw, tag_text):
    draw.text((W / 2, 34), tag_text, font=F(BOLD, 22), fill=GRAY, anchor="mm")


def pdf_cta_bar(img, draw, y_top, height=92):
    """Aviso de 'PDF en el comentario fijado' — grande y llamativo por
    derecho propio (icono de comentario + flecha + texto grande), ya NO
    depende de ir pegado al nombre/foto de Jorge. Vive en su propia franja,
    a todo lo ancho, siempre en el mismo sitio en las 5 slides."""
    x0, x1 = 60, W - 60
    y1 = y_top + height
    rr(draw, (x0, y_top, x1, y1), 22, fill=ORANGE)
    cy = (y_top + y1) / 2 - 4

    # icono de comentario, grande, a la izquierda
    icx = x0 + 68
    bw, bh = 72, 46
    by0, by1 = cy - bh / 2, cy + bh / 2
    rr(draw, (icx - bw / 2, by0, icx + bw / 2, by1), 14, fill=WHITE)
    draw.polygon([(icx - 14, by1 - 2), (icx - 14, by1 + 18), (icx + 10, by1 - 2)], fill=WHITE)
    for ddx in (-17, 0, 17):
        draw.ellipse((icx + ddx - 7, cy - 7, icx + ddx + 7, cy + 7), fill=ORANGE)

    # flecha garabateada, gruesa, apuntando hacia ABAJO — hacia donde estan
    # los comentarios de verdad (debajo del post)
    ax = icx + bw / 2 + 46
    scribble_arrow(draw, (ax, y_top + 14), (ax, y1 - 14), WHITE, width=11, jitter=3, head=22)

    tx = ax + 46
    draw.text((tx, y_top + height / 2), "EL PDF ESTA EN EL\nCOMENTARIO FIJADO",
              font=F(TITLE, 33), fill=WHITE, anchor="lm", align="left")


def brand_footer(img, draw, slide_no, total=5):
    diam = 56
    photo = Image.open(PHOTO_PATH).convert("RGB")
    photo = ImageOps.fit(photo, (diam, diam), centering=(0.5, 0.25))
    mask = Image.new("L", (diam, diam), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diam, diam), fill=255)
    ring_d = diam + 6
    ring = Image.new("RGBA", (ring_d, ring_d), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, ring_d, ring_d), fill=(255, 255, 255, 255))
    ring.paste(photo, (3, 3), mask)

    block_h = 60
    fy = H - block_h - 20
    img.paste(ring, (44, fy + (block_h - ring_d) // 2), ring)
    name_x = 44 + ring_d + 16

    draw.text((name_x, fy + block_h / 2), "Jorge Segovia", font=F(BOLD, 20), fill=INK, anchor="lm")
    draw.text((W - 46, fy + block_h / 2), f"{slide_no}/{total}", font=F(BOLD, 22), fill=GRAY, anchor="rm")


def speech(draw, box, label, text, f_label, f_text, label_fill, tail="left"):
    x0, y0, x1, y1 = box
    rr(draw, box, 24, fill=(255, 255, 255), outline=INK, width=4)
    tx = x0 + 32 if tail == "left" else x0 + (x1 - x0) - 84
    draw.polygon([(tx, y1 - 3), (tx + 42, y1 - 3), (tx + 14, y1 + 26)], fill=(255, 255, 255), outline=INK, width=4)
    draw.line((tx + 2, y1 - 2, tx + 40, y1 - 2), fill=(255, 255, 255), width=8)
    draw.text((x0 + 28, y0 + 18), label, font=f_label, fill=label_fill)
    draw_wrapped(draw, (x0 + 28, y0 + 54), text, f_text, INK, (x1 - x0) - 56, int(f_text.size * 1.2))


def two_box(img, d, day1, title1, body1, day2, title2, body2, box1, box2):
    rr(d, box1, 18, fill=(255, 255, 255), outline=INK, width=4)
    d.text((box1[0] + 26, box1[1] + 18), day1, font=F(TITLE, 19), fill=RED)
    draw_wrapped(d, (box1[0] + 26, box1[1] + 56), title1, F(TITLE, 25), INK, box1[2] - box1[0] - 52, 32)
    draw_wrapped(d, (box1[0] + 26, box1[1] + 130), body1, F(BOLD, 19), GRAY, box1[2] - box1[0] - 52, 25)

    rr(d, box2, 18, fill=INK)
    d.text((box2[0] + 26, box2[1] + 18), day2, font=F(TITLE, 19), fill=YELLOW)
    draw_wrapped(d, (box2[0] + 26, box2[1] + 56), title2, F(TITLE, 25), PAPER, box2[2] - box2[0] - 52, 32)
    draw_wrapped(d, (box2[0] + 26, box2[1] + 130), body2, F(BOLD, 19), (210, 210, 205), box2[2] - box2[0] - 52, 25)

    tape(img, box1[2] - 60, box1[1] + 2, angle=-9)
    tape(img, box2[0] + 60, box2[1] + 2, angle=9)


# ------------------------------------------------------------------
# SLIDE 1 — hook
# ------------------------------------------------------------------
def slide_1():
    random.seed(1)
    img, d = canvas()
    top_row(d, "AUDITORIA EN VIVO · SEO ECOMMERCE")

    box = (60, 78, W - 60, 340)
    top = browser_chrome(d, box, "notas-de-jorge.txt")
    draw_wrapped(d, (box[0] + 32, top[1] + 34),
                 "“¿Cual es el error SEO mas caro que sigue repitiendose "
                 "en el ecommerce?”",
                 F(TITLE, 30), INK, box[2] - box[0] - 64, 40)
    d.text((box[0] + 32, top[3] - 44), "— pregunta que le hago hoy a la comunidad SEO",
           font=F(BOLD, 20), fill=GRAY)

    scribble_circle(d, W / 2, 190, 470, 82, RED, width=8, tilt=0.05)
    tape(img, box[0] + 55, box[1] + 4, angle=-10)
    tape(img, box[2] - 55, box[1] + 4, angle=8)
    d = ImageDraw.Draw(img)
    stamp_text(img, W - 150, 372, "SPOILER:\nYO YA TENGO UNO", F(TITLE, 22), RED, angle=-7,
               stroke_fill=PAPER, stroke_w=6)

    d.text((W / 2, 460), "TE LANZO UNA", font=F(TITLE, 52), fill=INK, anchor="mm")
    d.text((W / 2, 514), "PREGUNTA EN SERIO.", font=F(TITLE, 46), fill=ORANGE, anchor="mm")
    draw_wrapped(d, (100, 578), "No busco likes, busco respuestas reales. Empiezo yo "
                 "con la mia, y luego te toca a ti.",
                 F(BOLD, 30), GRAY, W - 200, 40, align="left")

    ribbon(img, 800, "DESLIZA, EMPIEZO YO >>", INK, PAPER)
    d = ImageDraw.Draw(img)
    pdf_cta_bar(img, d, 890)
    brand_footer(img, d, 1)
    img.save(OUT_DIR / "carrusel-1.png")


# ------------------------------------------------------------------
# SLIDE 2 — la respuesta de Jorge (arranca la conversacion)
# ------------------------------------------------------------------
def slide_2():
    random.seed(2)
    img, d = canvas()
    top_row(d, "AUDITORIA EN VIVO · SEO ECOMMERCE")
    d.text((W / 2, 104), "MI RESPUESTA, PARA ARRANCAR", font=F(TITLE, 30), fill=INK, anchor="mm")

    speech(d, (64, 156, W - 64, 300), "PARA MI, SIN DUDARLO:",
           "“Canonicals que apuntan a la home... por si acaso.”",
           F(TITLE, 21), F(TITLE, 30), ORANGE, tail="left")

    draw_wrapped(d, (100, 350), "Se cuelan en cada migracion, cada rediseño, cada "
                 "plugin nuevo. Diluyen la relevancia real de tus categorias y "
                 "fichas de producto — y como “no rompen nada” a simple vista, "
                 "nadie los revisa.",
                 F(BOLD, 25), GRAY, W - 200, 33)

    stamp_text(img, W - 150, 560, "ASI, TAL\nCUAL", F(TITLE, 26), INK, angle=6,
               stroke_fill=YELLOW, stroke_w=9)
    d = ImageDraw.Draw(img)

    draw_wrapped(d, (80, 660), "Un canonical mal puesto no da error 404. Solo te "
                 "resta autoridad, en silencio.",
                 F(TITLE, 32), INK, W - 160, 42)

    ribbon(img, 800, "DESLIZA, COMPRUEBALO TU >>", ORANGE, WHITE)
    d = ImageDraw.Draw(img)
    pdf_cta_bar(img, d, 890)
    brand_footer(img, d, 2)
    img.save(OUT_DIR / "carrusel-2.png")


# ------------------------------------------------------------------
# SLIDE 3 — como comprobarlo tu mismo (diagnostico, sin la solucion completa)
# ------------------------------------------------------------------
def slide_3():
    random.seed(3)
    img, d = canvas()
    top_row(d, "AUDITORIA EN VIVO · SEO ECOMMERCE")
    d.text((W / 2, 100), "SI TE SUENA, COMPRUEBALO", font=F(TITLE, 32), fill=INK, anchor="mm")

    box = (64, 150, W - 64, 470)
    top = browser_chrome(d, box, "screaming-frog.tutienda.com")
    ry = top[1] + 30
    d.text((box[0] + 26, ry), "columna Canonical Link Element — exportada",
           font=F(BOLD, 19), fill=GRAY)
    rows = [("/pantalones-vaqueros", "-> home"), ("/zapatillas-running", "-> home"),
            ("/camisetas-basicas", "-> si misma")]
    ry2 = ry + 42
    for url, dest in rows:
        col = RED if dest == "-> home" else (26, 90, 26)
        d.text((box[0] + 26, ry2), url, font=F(BOLD, 22), fill=(26, 90, 26))
        d.text((box[2] - 40, ry2), dest, font=F(TITLE, 20), fill=col, anchor="ra")
        ry2 += 46
    d.line((box[0] + 22, ry2 + 4, box[2] - 22, ry2 + 4), fill=(225, 222, 212), width=2)
    d.text((box[0] + 26, ry2 + 20), "cuenta cuantas filas dicen \"-> home\" sin serlo.",
           font=F(BOLD, 17), fill=GRAY)

    scribble_circle(d, box[2] - 90, ry + 65, 128, 48, RED, width=8)
    scribble_arrow(d, (790, 560), (895, 400), RED, width=9)
    stamp_text(img, 730, 522, "AHI ESTA\nEL FALLO", F(TITLE, 26), RED, angle=-6, stroke_fill=PAPER, stroke_w=6)
    d = ImageDraw.Draw(img)

    d.text((W / 2, 598), "SI EL NUMERO TE", font=F(TITLE, 40), fill=INK, anchor="mm")
    d.text((W / 2, 644), "SORPRENDE, AHI LO TIENES.", font=F(TITLE, 34), fill=ORANGE, anchor="mm")
    draw_wrapped(d, (90, 672), "Screaming Frog, exportar, filtrar. Cinco minutos "
                 "para saber si te esta pasando a ti tambien.",
                 F(BOLD, 28), GRAY, W - 180, 36)

    ribbon(img, 800, "DESLIZA PARA LA PREGUNTA >>", INK, PAPER)
    d = ImageDraw.Draw(img)
    pdf_cta_bar(img, d, 890)
    brand_footer(img, d, 3)
    img.save(OUT_DIR / "carrusel-3.png")


# ------------------------------------------------------------------
# SLIDE 4 — ahora te toca a ti (invitacion, insight grande)
# ------------------------------------------------------------------
def slide_4():
    random.seed(4)
    img, d = canvas()
    for i in range(0, H, 5):
        d.line((0, i, W, i), fill=(240, 234, 220))
    top_row(d, "AUDITORIA EN VIVO · SEO ECOMMERCE")

    scribble_circle(d, W / 2, 420, 420, 340, RED, width=8, passes=1)
    d.text((W / 2, 300), "AHORA TE TOCA", font=F(TITLE, 46), fill=INK, anchor="mm")
    d.text((W / 2, 356), "A TI.", font=F(TITLE, 46), fill=ORANGE, anchor="mm")
    draw_wrapped(d, (W / 2, 460), "¿Cual es el error que TU ves una y otra vez, en "
                 "auditoria tras auditoria, y que nadie llega a arreglar del todo?",
                 F(BOLD, 30), INK, W - 280, 40, align="center")

    stamp_text(img, W / 2, 700, "LOS MEJORES, LA\nSEMANA QUE VIENE", F(TITLE, 26), RED, angle=-4,
               stroke_fill=YELLOW, stroke_w=9)
    d = ImageDraw.Draw(img)

    ribbon(img, 800, "DESLIZA PARA EL CTA >>", ORANGE, WHITE)
    d = ImageDraw.Draw(img)
    pdf_cta_bar(img, d, 890)
    brand_footer(img, d, 4)
    img.save(OUT_DIR / "carrusel-4.png")


# ------------------------------------------------------------------
# SLIDE 5 — CTA
# ------------------------------------------------------------------
def slide_5():
    random.seed(5)
    img, d = canvas()
    top_row(d, "AUDITORIA EN VIVO · SEO ECOMMERCE")

    rr(d, (60, 80, W - 60, 300), 26, fill=ORANGE)
    d.text((W / 2, 138), "TE LEO EN COMENTARIOS:", font=F(TITLE, 30), fill=WHITE, anchor="mm")
    draw_wrapped(d, (W / 2, 190), "cual es tu error SEO mas repetido — y de paso, mira "
                 "si tienes canonicals fantasma.",
                 F(TITLE, 26), WHITE, W - 200, 34, align="center")
    d.text((W / 2, 262), "(los mejores comentarios, los destripo la semana que viene)",
           font=F(BOLD, 19), fill=(255, 224, 204), anchor="mm")

    scribble_arrow(d, (W / 2 - 60, 336), (W / 2 - 60, 420), INK, width=11, head=26)
    stamp_text(img, W / 2 + 190, 378, "VA EN\nSERIO", F(TITLE, 24), INK, angle=8,
               stroke_fill=YELLOW, stroke_w=7)
    d = ImageDraw.Draw(img)

    box = (60, 442, W - 60, 666)
    rr(d, box, 22, fill=(255, 255, 255), outline=INK, width=5)
    diam = 118
    photo = Image.open(PHOTO_PATH).convert("RGB")
    photo = ImageOps.fit(photo, (diam, diam), centering=(0.5, 0.25))
    mask = Image.new("L", (diam, diam), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diam, diam), fill=255)
    ring_d = diam + 10
    ring = Image.new("RGBA", (ring_d, ring_d), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, ring_d, ring_d), fill=ORANGE + (255,))
    ring.paste(photo, (5, 5), mask)
    img.paste(ring, (box[0] + 26, box[1] + (box[3] - box[1] - ring_d) // 2), ring)
    d = ImageDraw.Draw(img)
    tx = box[0] + 26 + ring_d + 26
    draw_wrapped(d, (tx, box[1] + 30), "La guia gratis para detectar Y arreglar los "
                 "canonicals fantasma,",
                 F(BOLD, 23), INK, box[2] - tx - 26, 29)
    draw_wrapped(d, (tx, box[1] + 88), "esta en el COMENTARIO FIJADO de este post.",
                 F(TITLE, 23), ORANGE, box[2] - tx - 26, 29)
    d.text((tx, box[3] - 46), "no en la bio, no en un link raro — en el comentario.",
           font=F(BOLD, 17), fill=GRAY)

    ribbon(img, 800, "COMPARTELO CON QUIEN LO NECESITE >>", INK, PAPER)
    d = ImageDraw.Draw(img)
    pdf_cta_bar(img, d, 890)
    brand_footer(img, d, 5)
    img.save(OUT_DIR / "carrusel-5.png")


def build_pdf():
    """Empaqueta los 5 PNG en un PDF SIN reprocesarlos — img2pdf incrusta el
    PNG tal cual (FlateDecode, sin pérdida). Pillow's Image.save(...,"PDF")
    NO sirve aquí: para imágenes RGB siempre las recomprime como JPEG
    (DCTDecode) aunque no se lo pidas, y eso se nota en las líneas finas de
    los garabatos y el texto — se ve peor que el PNG de origen."""
    paths = [OUT_DIR / f"carrusel-{i}.png" for i in range(1, 6)]
    pdf_path = OUT_DIR / "carrusel-post.pdf"
    layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(285.75), img2pdf.mm_to_pt(285.75)))
    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert([str(p) for p in paths], layout_fun=layout))
    return pdf_path


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    slide_1()
    slide_2()
    slide_3()
    slide_4()
    slide_5()
    p = build_pdf()
    print("Listo:", p)
