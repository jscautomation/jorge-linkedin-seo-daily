# -*- coding: utf-8 -*-
"""
Genera el recurso del día en formato WORKSHEET / AUTOEVALUACIÓN — una
checklist de casillas en blanco para que el lector la aplique él mismo
sobre su propia tienda mientras la lee (imprimible o para ir marcando
sobre el PDF). Es el tercer tipo de recurso del catálogo de
AUTOMATION_BRIEF.md sección 4 — parte de la rotación de 4 plantillas
(guía/checklist, one-pager, worksheet, swipe file) para no repetir siempre
el mismo formato de recurso día a día.

Mismo lenguaje visual que el resto de piezas (ver AUTOMATION_BRIEF.md
sección 3): fondo crema #FFFCF4, League Spartan, naranja #FF914D, foto+logo
arriba igual que en el resto.

Cuándo usarlo: cuando el tema del día se presta a que el lector se
autoevalúe con una lista de sí/no sobre su propia tienda (en vez de un
diagnóstico explicado en prosa) — encaja bien con roasts y mitos donde el
error tiene varias señales concretas y observables.

Uso: python3 scripts/generate_worksheet_pdf.py [ruta_de_salida.pdf]
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
# Misma paleta que el resto de generadores de PDF/imagen del repo.
# ============================================================
BG = colors.HexColor("#FFFCF4")
BORDER = colors.HexColor("#E8E1CE")
ORANGE = colors.HexColor("#FF914D")
INK = colors.HexColor("#111111")
GRAY = colors.HexColor("#79746A")

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
style_item = style("item", fontSize=10.8, leading=15)
style_score = style("score", fontSize=10.3, leading=15, textColor=INK)
style_solution_label = style("solution_label", fontSize=9, leading=12, textColor=ORANGE, spaceAfter=4)
style_solution_body = style("solution_body", fontSize=10, leading=15)
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


def checkbox_row(text):
    """Casilla cuadrada vacia (para marcar a mano o sobre el PDF) + el
    texto del item, en una fila con la casilla arriba-izquierda alineada
    con la primera linea del texto."""
    box = Table([[""]], colWidths=[6 * mm], rowHeights=[6 * mm])
    box.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1.2, INK),
        ("BACKGROUND", (0, 0), (-1, -1), BG),
    ]))
    row = Table([[box, Paragraph(text, style_item)]], colWidths=[10 * mm, None])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (0, 0), 1),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (1, 0), (1, 0), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return row


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
    doc.addPageTemplates([PageTemplate(id="Worksheet", frames=frame, onPage=chrome)])

    story = [Spacer(1, 4)]
    for line in config["title_lines"]:
        story.append(Paragraph(line, style_title))
    story.append(Spacer(1, 6))
    story.append(Paragraph(config["subtitle"], style_subtitle))
    story.append(Spacer(1, 14))
    story.append(Paragraph(config["intro_text"], style_intro))
    story.append(Spacer(1, 18))

    items_table_rows = []
    for item in config["check_items"]:
        items_table_rows.append([checkbox_row(item)])
        items_table_rows.append([Spacer(1, 12)])
    items_table = Table(items_table_rows, colWidths=[None])
    items_table.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 6))

    score_box = Table([[Paragraph(config["score_note"], style_score)]], colWidths=[None])
    score_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FBE4D2")),
        ("BOX", (0, 0), (-1, -1), 0.8, ORANGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 14), ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("ROUNDEDCORNERS", [8, 8, 8, 8]),
    ]))
    story.append(score_box)
    story.append(Spacer(1, 16))

    story.append(Paragraph("CÓMO ARREGLARLO", style_solution_label))
    story.append(Paragraph(config["solution_text"], style_solution_body))
    story.append(Spacer(1, 16))

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
    "title_lines": ["CADENAS DE REDIRECTS:", "AUTOEVALÚA TU ECOMMERCE"],
    "subtitle": "Marca las casillas que se apliquen a tu tienda — tarda 5 minutos",
    "tag": "WORKSHEET SEO · REDIRECCIONES",

    "intro_text": "No hace falta adivinar si tienes cadenas de redirects escondidas: la mayoría de señales "
                  "de que las tienes son observables sin herramientas, solo mirando cómo se comporta tu "
                  "sitio. Marca cada casilla que se aplique a tu ecommerce ahora mismo.",

    "check_items": [
        "Has cambiado de plantilla, de estructura de categorías o de dominio al menos una vez en los "
        "últimos 2 años.",
        "Nunca has exportado el informe \"Redirect Chains\" de Screaming Frog en tu dominio.",
        "Alguna URL antigua de tu catálogo (producto o categoría descatalogada) sigue redirigiendo a otra "
        "URL en vez de al destino final.",
        "Tu sitemap.xml no se ha revisado a mano desde la última migración o rediseño.",
        "No tienes una regla de proceso escrita sobre a dónde debe apuntar una redirección nueva cuando "
        "se lanza una migración.",
    ],

    "score_note": "Si has marcado 2 o más casillas, es muy probable que tengas cadenas de redirects "
                  "activas ahora mismo en tu ecommerce, gastando presupuesto de rastreo sin que lo sepas.",

    "solution_text": "Exporta el informe \"Redirect Chains\" de Screaming Frog (con \"Always Follow "
                      "Redirects\" activado en Configuration -&gt; Spider -&gt; Crawl). Para cada cadena, "
                      "localiza el destino FINAL real (el último salto con status 200) y repunta ahí "
                      "directamente cada redirección de la cadena, en un único salto -- nunca A -&gt; B -&gt; "
                      "C -&gt; D, siempre A -&gt; D. Revisa también el sitemap.xml y los enlaces internos "
                      "para que apunten a la URL final, nunca a una que redirige. Repite el crawl tras cada "
                      "migración futura.",

    "cta_title": "¿Quieres que lo midamos con datos reales de tu tienda?",
    "cta_body": "Lo hacemos en una auditoría SEO completa (Fase 1) + implementación (Fase 2), diseñada "
                "para ecommerce de facturación alta.",
}


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "_ejemplo-worksheet.pdf"
    build(CONFIG, out)
