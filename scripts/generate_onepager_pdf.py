# -*- coding: utf-8 -*-
"""
Genera el recurso del día en formato ONE-PAGER / INFOGRAFÍA — una sola
página A4, pensado para temas que se resumen en un único hallazgo/punto
(el roast del lunes, la pregunta abierta del viernes, una tendencia con un
solo ángulo...). Es el segundo tipo de recurso del catálogo de
AUTOMATION_BRIEF.md sección 4 (antes solo existía el generador de guía/
checklist multi-punto, `generate_lead_magnet_pdf.py`) — para dar variedad
real al formato del recurso día a día, no repetir siempre "guía en PDF".

Mismo lenguaje visual que el post y que la guía/checklist (ver
AUTOMATION_BRIEF.md sección 3): fondo crema #FFFCF4, ExtraBold League
Spartan naranja para el titular (igual que la imagen del post), tarjetas
con borde suave y acento naranja para los 3 bloques (por qué / cómo
detectarlo / cómo arreglarlo), foto+logo arriba igual que en el resto de
piezas.

Cuándo usarlo en vez de la guía/checklist: cuando el tema del día es UN
solo punto (no una lista de varios) y quieres un recurso que se lea entero
de un vistazo, tipo cheat sheet — no fuerces contenido de relleno para
llenar la página.

Uso: python3 scripts/generate_onepager_pdf.py [ruta_de_salida.pdf]
"""
import re
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
# Misma paleta que generate_lead_magnet_pdf.py y generate_single_post_image.py
# — si cambia aquí, cambia también en esos dos motores.
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


style_title = style("title", fontName="LeagueSpartanExtraBold", fontSize=30, leading=34,
                     textColor=ORANGE, alignment=TA_CENTER)
style_subtitle = style("subtitle", fontSize=12, leading=17, alignment=TA_CENTER)
style_stat_num = style("stat_num", fontName="LeagueSpartanExtraBold", fontSize=40, leading=40,
                        textColor=INK, alignment=TA_CENTER)
style_stat_lbl = style("stat_lbl", fontSize=10.5, leading=14, textColor=INK, alignment=TA_CENTER)
style_section_title = style("section_title", fontName="LeagueSpartanExtraBold", fontSize=13, leading=17)
style_label = style("label", fontSize=9, leading=12, textColor=ORANGE, spaceAfter=3)
style_body = style("body", fontSize=9.6, leading=13.8)
style_footer_title = style("footer_title", fontName="LeagueSpartanExtraBold", fontSize=15, leading=19)
style_footer_body = style("footer_body", fontSize=9.7, leading=14)
style_kicker = style("kicker", fontSize=8.5, leading=11, textColor=GRAY)


def hl(text):
    """<hl>frase</hl> -> caja naranja de fondo, mismo efecto que en la
    guía/checklist y en el CTA de la imagen del post."""
    return re.sub(
        r"<hl>(.*?)</hl>",
        r'<font color="#111111" backColor="#FF914D">&#160;\1&#160;</font>',
        text,
    )


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


def badge(text, size=9 * mm, bg=ORANGE, fg=INK, fontsize=12):
    t = Table([[text]], colWidths=[size], rowHeights=[size])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("TEXTCOLOR", (0, 0), (-1, -1), fg),
        ("FONTNAME", (0, 0), (-1, -1), "LeagueSpartanExtraBold"),
        ("FONTSIZE", (0, 0), (-1, -1), fontsize),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROUNDEDCORNERS", [size / 2, size / 2, size / 2, size / 2]),
    ]))
    return t


def section_block(num, label, text):
    row = Table([[badge(f"{num:02d}", size=8 * mm, fontsize=10), Paragraph(label, style_section_title)]],
                colWidths=[12 * mm, None])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    content = Table([[row], [Spacer(1, 6)], [Paragraph(text, style_body)]], colWidths=[None])
    content.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 16), ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (0, 0), 10), ("BOTTOMPADDING", (0, 2), (0, 2), 10),
        ("TOPPADDING", (0, 1), (0, 2), 0), ("BOTTOMPADDING", (0, 0), (0, 1), 0),
        ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
        ("LINEBEFORE", (0, 0), (0, 0), 3, ORANGE),
        ("ROUNDEDCORNERS", [8, 8, 8, 8]),
    ]))
    return content


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
    doc.addPageTemplates([PageTemplate(id="OnePager", frames=frame, onPage=chrome)])

    story = [Spacer(1, 4)]
    for line in config["title_lines"]:
        story.append(Paragraph(line, style_title))
    story.append(Spacer(1, 6))
    story.append(Paragraph(config["subtitle"], style_subtitle))
    story.append(Spacer(1, 14))

    stat_cell = Table([
        [Paragraph(config["stat_number"], style_stat_num),
         Paragraph(config["stat_label"], style_stat_lbl)],
    ], colWidths=[36 * mm, None])
    stat_cell.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ORANGE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (0, 0), (0, 0), "CENTER"),
        ("LEFTPADDING", (0, 0), (0, 0), 6), ("LEFTPADDING", (1, 0), (1, 0), 4),
        ("RIGHTPADDING", (1, 0), (1, 0), 18),
        ("TOPPADDING", (0, 0), (-1, -1), 14), ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("ROUNDEDCORNERS", [10, 10, 10, 10]),
    ]))
    story.append(stat_cell)
    story.append(Spacer(1, 16))

    labels = ["POR QUÉ OCURRE", "CÓMO DETECTARLO EN 5 MINUTOS", "CÓMO ARREGLARLO"]
    for i, (label, text) in enumerate(zip(labels, config["section_texts"])):
        story.append(section_block(i + 1, label, text))
        story.append(Spacer(1, 9))

    story.append(Spacer(1, 4))
    footer = Table([[
        Table([[Paragraph(hl(config["cta_title"]), style_footer_title)],
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
    # Mismo titular que el punto 0 del post y que title_lines de la imagen.
    "title_lines": ["CADENAS DE REDIRECTS:", "EL SEO QUE NADIE MIDE"],
    "subtitle": "Cómo encontrar y arreglar los saltos de redirección acumulados en tu ecommerce, migración tras migración",
    "tag": "ONE-PAGER SEO · REDIRECCIONES",

    "stat_number": "1",
    "stat_label": "cadena de redirecciones que nadie había medido",

    # Un texto por sección — igual que un POINTS[0] de la guía/checklist,
    # pero pensado para UN solo hallazgo (no fuerces varios).
    "section_texts": [
        "Cada vez que cambias de plantilla, reestructuras categorías, cambias de dominio o haces un "
        "rebranding, la redirección nueva se apunta sobre la URL antigua que YA redirigía a otra cosa, en "
        "vez de apuntar directo al destino final. El resultado son cadenas de 2, 3 o más saltos "
        "(A -&gt; B -&gt; C -&gt; D) que nadie revisa porque, para el usuario, la página final carga igual.",

        "En Screaming Frog: Configuration -&gt; Spider -&gt; Crawl, activa \"Always Follow Redirects\" "
        "antes de rastrear tu dominio. Al terminar, ve a Reports -&gt; Redirects -&gt; \"Redirect Chains\" "
        "y exporta el informe: ahí aparece cada cadena completa, con el número de saltos y el código de "
        "estado de cada uno.",

        "1) Localiza el destino FINAL real de cada cadena (último salto, status 200). 2) Repunta cada "
        "redirección directo a ese destino, en un único salto -- nunca A -&gt; B -&gt; C -&gt; D, siempre "
        "A -&gt; D. 3) Revisa sitemap.xml y enlaces internos para que apunten a la URL final. 4) Repite el "
        "crawl tras cada migración, antes de que se acumulen cadenas nuevas.",
    ],

    "cta_title": "<hl>¿Cuántos saltos</hl> lleva tu redirección más antigua?",
    "cta_body": "Lo medimos y arreglamos en una auditoría SEO completa (Fase 1) + implementación (Fase 2), "
                "diseñada para ecommerce de facturación alta.",
}


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "content" / "_ejemplo-onepager.pdf"
    build(CONFIG, out)
