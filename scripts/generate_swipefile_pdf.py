# -*- coding: utf-8 -*-
"""
Genera el recurso del día en formato SWIPE FILE — un banco de fragmentos
listos para copiar y pegar (reglas de robots.txt, plantillas de meta
title, prompts de auditoría...). Es el cuarto tipo de recurso del catálogo
de AUTOMATION_BRIEF.md sección 4 — completa la rotación de 4 plantillas
(guía/checklist, one-pager, worksheet, swipe file).

Mismo lenguaje visual que el resto de piezas (fondo crema, League Spartan,
naranja, foto+logo arriba), salvo por las "cajas de código" de cada
fragmento — fondo casi negro #282828 (la misma banda oscura de la imagen
del post) con texto monoespaciado, para que se lean claramente como algo
copiable, no como prosa.

Cuándo usarlo: cuando el tema del día da pie a fragmentos de texto
reutilizables tal cual (reglas concretas, plantillas con placeholders,
prompts) — no encaja si el tema es un diagnóstico sin nada literal que
copiar.

Uso: python3 scripts/generate_swipefile_pdf.py [ruta_de_salida.pdf]
"""
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, BaseDocTemplate, Frame, PageTemplate
from reportlab.pdfgen import canvas as pdfcanvas

REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = REPO_ROOT / "assets" / "fonts"
LOGO_PATH = REPO_ROOT / "assets" / "branding" / "logo.png"
PHOTO_PATH = REPO_ROOT / "assets" / "branding" / "foto-jorge-circle.png"

pdfmetrics.registerFont(TTFont("LeagueSpartanExtraBold", str(FONT_DIR / "LeagueSpartan-ExtraBold.ttf")))
pdfmetrics.registerFont(TTFont("LeagueSpartanBold", str(FONT_DIR / "LeagueSpartan-Bold.ttf")))
LOGO_IMG = ImageReader(str(LOGO_PATH))

# ============================================================
# MOTOR DE RENDER — fijo, no tocar sin instruccion expresa de Jorge.
# Misma paleta que el resto de generadores de PDF/imagen del repo. La caja
# de codigo usa Courier (base14 de reportlab, no hace falta registrarla) —
# es la unica pieza del repo con texto monoespaciado, a proposito, para que
# el fragmento se lea como "esto se copia tal cual".
# ============================================================
BG = colors.HexColor("#FFFCF4")
BAND = colors.HexColor("#282828")
ORANGE = colors.HexColor("#FF914D")
INK = colors.HexColor("#111111")
GRAY = colors.HexColor("#79746A")
CODE_TEXT = colors.HexColor("#F4EEE3")

styles_registry = {}


def style(name, **kw):
    kw.setdefault("fontName", "LeagueSpartanBold")
    kw.setdefault("textColor", INK)
    kw.setdefault("alignment", TA_LEFT)
    s = ParagraphStyle(name, **kw)
    styles_registry[name] = s
    return s


style_title = style("title", fontName="LeagueSpartanExtraBold", fontSize=28, leading=32,
                     textColor=ORANGE, alignment=TA_CENTER)
style_subtitle = style("subtitle", fontSize=12, leading=17, alignment=TA_CENTER)
style_intro = style("intro", fontSize=10.3, leading=15)
style_snippet_label = style("snippet_label", fontSize=11, leading=14, textColor=ORANGE, spaceAfter=4)
style_snippet_code = style("snippet_code", fontName="Courier", fontSize=9.3, leading=13.5, textColor=CODE_TEXT)
style_snippet_note = style("snippet_note", fontSize=9, leading=13, textColor=GRAY, spaceBefore=4)
style_footer_title = style("footer_title", fontName="LeagueSpartanExtraBold", fontSize=15, leading=19)
style_footer_body = style("footer_body", fontSize=9.7, leading=14)


def _header(c, doc, tag):
    logo_w, logo_h = 20 * mm, 14.2 * mm
    top_y = doc.pagesize[1] - 14 * mm - logo_h
    c.drawImage(LOGO_IMG, 20 * mm, top_y, width=logo_w, height=logo_h, mask="auto")
    c.setFillColor(GRAY)
    c.setFont("LeagueSpartanBold", 8)
    c.drawString(20 * mm, top_y - 10, tag)

    photo_d = 17 * mm
    photo_x = doc.pagesize[0] - photo_d - 20 * mm
    photo_y = doc.pagesize[1] - 14 * mm - photo_d
    c.setFillColor(ORANGE)
    c.circle(photo_x + photo_d / 2, photo_y + photo_d / 2, photo_d / 2 + 1.4, stroke=0, fill=1)
    c.drawImage(str(PHOTO_PATH), photo_x, photo_y, width=photo_d, height=photo_d, mask="auto")


def snippet_block(label, code_lines, note=None):
    code_paras = [Paragraph(line.replace(" ", "&nbsp;") or "&nbsp;", style_snippet_code) for line in code_lines]
    code_box = Table([[p] for p in code_paras], colWidths=[None])
    code_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BAND),
        ("LEFTPADDING", (0, 0), (-1, -1), 14), ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (0, 0), 9), ("BOTTOMPADDING", (0, -1), (0, -1), 9),
        ("TOPPADDING", (0, 1), (0, -1), 1), ("BOTTOMPADDING", (0, 0), (0, -2), 1),
        ("ROUNDEDCORNERS", [8, 8, 8, 8]),
    ]))
    rows = [[Paragraph(label, style_snippet_label)], [code_box]]
    if note:
        rows.append([Paragraph(note, style_snippet_note)])
    block = Table(rows, colWidths=[None])
    block.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return block


def build(config, out_path):
    def chrome(c: pdfcanvas.Canvas, doc):
        c.saveState()
        c.setFillColor(BG)
        c.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)
        _header(c, doc, config["tag"])
        c.setFillColor(GRAY)
        c.setFont("LeagueSpartanBold", 7.5)
        c.drawCentredString(doc.pagesize[0] / 2, 10 * mm, "jorge@jscautomation.es · jorgesegoviaciscar.com")
        c.restoreState()

    doc = BaseDocTemplate(str(out_path), pagesize=A4,
                           leftMargin=20 * mm, rightMargin=20 * mm,
                           topMargin=18 * mm, bottomMargin=18 * mm)
    frame = Frame(20 * mm, 18 * mm, doc.pagesize[0] - 40 * mm, doc.pagesize[1] - 56 * mm, id="page")
    doc.addPageTemplates([PageTemplate(id="SwipeFile", frames=frame, onPage=chrome)])

    story = [Spacer(1, 2)]
    for line in config["title_lines"]:
        story.append(Paragraph(line, style_title))
    story.append(Spacer(1, 4))
    story.append(Paragraph(config["subtitle"], style_subtitle))
    story.append(Spacer(1, 8))
    story.append(Paragraph(config["intro_text"], style_intro))
    story.append(Spacer(1, 10))

    for label, code_lines, note in config["snippets"]:
        story.append(snippet_block(label, code_lines, note))
        story.append(Spacer(1, 9))

    footer = Table([[
        Table([[Paragraph(config["cta_title"], style_footer_title)],
               [Spacer(1, 6)],
               [Paragraph(config["cta_body"], style_footer_body)]], colWidths=[None])
    ]], colWidths=[None])
    footer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ORANGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 18), ("RIGHTPADDING", (0, 0), (-1, -1), 18),
        ("TOPPADDING", (0, 0), (-1, -1), 16), ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
        ("ROUNDEDCORNERS", [12, 12, 12, 12]),
    ]))
    story.append(footer)

    doc.build(story)
    print(f"PDF generado: {out_path}")


# ============================================================
# CONTENIDO DE HOY — esto SI se edita cada dia. El ejemplo de abajo (tema
# del 28/08/2026, cadenas de redirects) es la referencia de formato.
# ============================================================
CONFIG = {
    "title_lines": ["CADENAS DE REDIRECTS:", "BANCO DE COMPROBACIONES"],
    "subtitle": "Copia y adapta estos fragmentos para auditar las redirecciones de tu ecommerce",
    "tag": "SWIPE FILE SEO · REDIRECCIONES",

    "intro_text": "Nada de esto hace falta escribirlo desde cero. Copia cada fragmento y adáptalo a tu "
                  "propio dominio/herramienta.",

    "snippets": [
        ("CONFIGURACIÓN DE SCREAMING FROG (antes de rastrear)",
         ["Configuration > Spider > Crawl",
          "  [x] Always Follow Redirects",
          "  [x] Always Follow Canonicals",
          "",
          "Tras el crawl: Reports > Redirects > Redirect Chains > Export"],
         "Sin \"Always Follow Redirects\" activado, Screaming Frog para en el primer salto y no ves la "
         "cadena completa."),

        ("BÚSQUEDA EN GOOGLE PARA DETECTAR URLS SOSPECHOSAS",
         ["site:tudominio.com \"redirigiendo\" OR \"ha cambiado\"",
          "site:tudominio.com inurl:old OR inurl:antiguo"],
         "Útil como primer barrido manual antes de meterte con Screaming Frog."),

        ("PROMPT DE AUDITORÍA (para pedirle a una IA que te ayude a priorizar)",
         ["Tengo esta lista de cadenas de redirects de mi ecommerce (URL origen ->",
          "salto 1 -> salto 2 -> ... -> destino final, con su codigo de estado):",
          "",
          "[pega aqui el export de Screaming Frog]",
          "",
          "Ordena las cadenas de mas a menos prioritarias segun: numero de",
          "saltos, si el origen recibe trafico/enlaces, y si el destino final",
          "es una pagina de producto o categoria activa."],
         "Sustituye el corchete por tu export real; la IA no adivina prioridad sin esos datos."),
    ],

    "cta_title": "¿Prefieres que lo hagamos nosotros por ti?",
    "cta_body": "Auditamos y arreglamos tus redirecciones dentro de una auditoría SEO completa (Fase 1) + "
                "implementación (Fase 2), diseñada para ecommerce de facturación alta.",
}


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "_ejemplo-swipefile.pdf"
    build(CONFIG, out)
