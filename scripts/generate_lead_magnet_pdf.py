# -*- coding: utf-8 -*-
"""
Genera el PDF lead magnet (portada con degradado + foto + logo, tarjetas de
contenido, cierre con CTA de las 2 fases). Mismo sistema visual siempre —
lo que cambia cada día es el CONFIG de abajo (título, intro, puntos).

Uso: python3 scripts/generate_lead_magnet_pdf.py [ruta_de_salida.pdf]
Todas las rutas son relativas al repo (funciona igual en Windows local que
en el sandbox Linux de la ejecución en la nube).
"""
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle,
    HRFlowable, Frame, PageTemplate, BaseDocTemplate, NextPageTemplate
)
from reportlab.pdfgen import canvas as pdfcanvas

REPO_ROOT = Path(__file__).resolve().parent.parent
GRADIENT_BG_PATH = str(REPO_ROOT / "assets" / "branding" / "gradient_bg.png")
LOGO_PATH = str(REPO_ROOT / "assets" / "branding" / "logo.png")
PHOTO_PATH = str(REPO_ROOT / "assets" / "branding" / "foto-jorge-circle.png")

NAVY = colors.HexColor("#1A1A1A")
ORANGE = colors.HexColor("#FF5A1F")
CARD_BG = colors.HexColor("#F4F6FA")
GRAY = colors.HexColor("#5b6b85")
INK = colors.HexColor("#212c42")
WHITE = colors.white

# ==================================================================
# 👉 CONFIG: esto cambia cada día. El resto del archivo (estilos,
#    layout, funciones) es fijo — no tocar salvo rediseño explícito.
# ==================================================================
COVER_TITLE_HTML = "Los 12 errores SEO<br/>que más dinero cuestan<br/>a un ecommerce"
COVER_SUBTITLE = "La checklist que uso en cada auditoría SEO a tiendas online de facturación alta (WordPress y Shopify)"
COVER_TAG = "CHECKLIST SEO · ECOMMERCE"  # etiqueta pequeña arriba a la izquierda de la portada

INTRO_TITLE = "Antes de empezar"
INTRO_PARAGRAPHS = [
    "Soy Jorge Segovia, consultor SEO especializado en ecommerce. Llevo años haciendo auditorías SEO "
    "completas —de más de 100 páginas— a tiendas online de facturación alta, la mayoría en Shopify y "
    "WordPress.",
    "Cada vez que abro una cuenta nueva me encuentro los mismos errores una y otra vez: fallos que llevan "
    "meses, a veces años, frenando el tráfico orgánico y las ventas, y que casi nadie detecta porque no "
    "dan la cara a simple vista.",
    "Esta checklist reúne los que más impacto tienen en el negocio. Para cada uno te explico por qué "
    "ocurre, cómo detectarlo tú mismo en 5 minutos, y qué hacer para arreglarlo.",
]
STAT_NUMBER = "12"
STAT_LABEL = "ERRORES REALES<br/>DE AUDITORÍAS SEO<br/>A ECOMMERCE"

# Lista de puntos — 1 o varios, según el documento (este archivo trae los 12
# del checklist original como EJEMPLO por defecto; en la ejecución diaria se
# sustituyen por los puntos reales del tema de ese día — ver AUTOMATION_BRIEF.md § 3bis).
POINTS = [
    ("Categorías de producto bloqueadas o sin indexar",
     "Al crear filtros de categoría (talla, color, precio) muchas plataformas generan automáticamente reglas de robots.txt o etiquetas noindex que terminan bloqueando también categorías principales por error de configuración.",
     "En Google Search Console → Cobertura, busca “Excluida por etiqueta noindex” o “Bloqueada por robots.txt” y revisa si aparecen categorías importantes.",
     "Audita el robots.txt y las etiquetas noindex categoría por categoría, dejando indexables solo las que tengan volumen de búsqueda real."),
    ("Contenido duplicado por parámetros de filtro",
     "Los filtros de color, talla o precio generan URLs como ?color=rojo&talla=m que Google rastrea como páginas nuevas con el mismo contenido que la categoría original.",
     "Busca en Google “site:tudominio.com inurl:?” y cuenta cuántas URLs con parámetros aparecen indexadas.",
     "Usa canonical hacia la URL de categoría limpia y configura los parámetros como no indexables en Search Console."),
    ("Arquitectura SEO no transaccional",
     "La estructura de categorías se diseña copiando el catálogo interno (marca, proveedor, temporada) en vez de cómo busca la gente realmente en Google.",
     "Compara tus categorías actuales con un keyword research de intención transaccional en tu sector: si faltan categorías para búsquedas de alto volumen, ahí está el problema.",
     "Rediseña el árbol de categorías alrededor de las keywords transaccionales reales de tu sector, no de tu catálogo interno."),
    ("Paginación mal gestionada",
     "Al listar productos en varias páginas no se gestiona correctamente el canonical ni el contenido de cada página, y Google trata la categoría como contenido “delgado”.",
     "Abre la página 2 o 3 de cualquier categoría y mira el código fuente: busca la etiqueta canonical, ¿apunta a sí misma o siempre a la página 1?",
     "Cada página paginada debe ser autocanonical (canonical a sí misma) y aportar valor único, no ser un simple corta-pega de la primera."),
    ("Productos agotados devueltos como 404",
     "Cuando un producto se agota o se descataloga, la plataforma elimina la URL directamente sin gestionar la transición ni el tráfico o enlaces que recibía.",
     "En Search Console → Cobertura, revisa cuántas URLs “No encontradas (404)” corresponden a productos que antes tenían tráfico o enlaces.",
     "Mantén la página con un mensaje de “agotado” + productos similares, o redirige (301) a la categoría padre si es definitivo."),
    ("Core Web Vitals en rojo por imágenes sin optimizar",
     "Las fotos de producto se suben a resolución completa, sin comprimir y sin carga diferida (lazy load), disparando los tiempos de carga.",
     "Pasa tu URL de producto por PageSpeed Insights (gratis) y mira el LCP: si supera 2.5 segundos, tienes un problema real.",
     "Comprime las imágenes (formato WebP), activa lazy load y sirve tamaños responsive según el dispositivo."),
    ("Breadcrumbs sin datos estructurados",
     "Se implementan visualmente para el usuario, pero sin el marcado schema.org BreadcrumbList, así que Google no puede aprovecharlos en resultados de búsqueda.",
     "Pega la URL de un producto en el Rich Results Test de Google y comprueba si detecta “BreadcrumbList”.",
     "Añade el marcado JSON-LD de BreadcrumbList; la mayoría de plugins SEO de WordPress lo generan automáticamente si lo activas."),
    ("Meta titles y descriptions duplicados o autogenerados",
     "La plataforma genera el title automáticamente con el mismo patrón para todos los productos (ej. “Nombre producto | Tienda”), sin optimizar keyword ni diferenciar.",
     "Exporta el listado de title tags con Screaming Frog (gratis hasta 500 URLs) y filtra por duplicados.",
     "Personaliza el title con la keyword principal más un atributo diferenciador (color, talla, uso) en vez del patrón genérico."),
    ("Canonicals mal configurados",
     "Por error de plantilla, muchas variantes de producto o incluso categorías completas canonicalizan hacia la home del sitio.",
     "En Screaming Frog, exporta la columna “Canonical Link Element” y busca cuántas URLs apuntan a la home sin ser la home.",
     "Corrige la plantilla para que cada página canonicalice hacia sí misma, salvo casos justificados (variantes de color/talla del mismo producto)."),
    ("Categorías sin contenido único (“thin content”)",
     "La categoría solo muestra el listado de productos, sin ningún texto que le dé a Google señales claras sobre de qué trata la página.",
     "Entra en una categoría importante y comprueba si hay al menos 150-300 palabras de texto único, no solo productos.",
     "Añade un bloque de texto SEO (arriba o abajo del listado) centrado en la keyword transaccional de esa categoría."),
    ("Productos huérfanos sin enlazado interno",
     "Los productos nuevos o de baja rotación no reciben enlaces desde categorías, artículos de blog u otras páginas relevantes del sitio.",
     "En Screaming Frog, filtra por “Inlinks” y localiza productos con 0 o 1 enlace interno recibido.",
     "Enlaza esos productos desde categorías relacionadas, artículos de blog y bloques de “productos relacionados”."),
    ("Sitemap XML desactualizado",
     "El sitemap se generó una vez y no se actualiza dinámicamente, o incluye URLs descatalogadas o marcadas como noindex.",
     "Abre tu sitemap.xml y comprueba aleatoriamente 10 URLs: ¿siguen existiendo y son indexables?",
     "Usa un sitemap dinámico (la mayoría de plugins SEO lo generan automáticamente) y envíalo actualizado en Search Console."),
]

FOOTER_TITLE = "Los 12 errores SEO que más dinero cuestan a un ecommerce"  # pie de página en las páginas de contenido
CTA_TITLE = "¿Cuáles de estos errores tiene tu ecommerce?"
CTA_BODY = "Lo descubrimos en una auditoría SEO completa, diseñada para ecommerce de facturación alta."

# 👉 ruta de salida: por CLI (recomendado en la ejecución diaria) o por defecto
OUTPUT_PATH = sys.argv[1] if len(sys.argv) > 1 else str(
    REPO_ROOT / "assets" / "pdf" / "checklist-12-errores-seo-ecommerce.pdf"
)
# ==================================================================

styles = getSampleStyleSheet()

style_h1_cover = ParagraphStyle(
    "h1_cover", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=29, leading=35, textColor=WHITE, alignment=TA_LEFT, spaceAfter=14
)
style_sub_cover = ParagraphStyle(
    "sub_cover", parent=styles["Normal"], fontName="Helvetica",
    fontSize=13.5, leading=19, textColor=WHITE, alignment=TA_LEFT
)
style_author_cover = ParagraphStyle(
    "author_cover", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=11.5, leading=16, textColor=NAVY, alignment=TA_LEFT
)
style_h2 = ParagraphStyle(
    "h2", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=18, leading=22, textColor=NAVY, spaceBefore=0, spaceAfter=10
)
style_body = ParagraphStyle(
    "body", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10, leading=15.5, textColor=INK, spaceAfter=8
)
style_intro = ParagraphStyle(
    "intro", parent=styles["Normal"], fontName="Helvetica",
    fontSize=11.5, leading=18, textColor=INK
)
style_error_title = ParagraphStyle(
    "error_title", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=12.5, leading=15.5, textColor=NAVY, spaceAfter=0
)
style_label = ParagraphStyle(
    "label", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=8.5, leading=12, textColor=ORANGE, spaceBefore=10, spaceAfter=3
)
style_cta_title = ParagraphStyle(
    "cta_title", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=22, leading=27, textColor=WHITE, alignment=TA_CENTER, spaceAfter=14
)
style_cta_body = ParagraphStyle(
    "cta_body", parent=styles["Normal"], fontName="Helvetica",
    fontSize=11, leading=16, textColor=WHITE, alignment=TA_CENTER
)
style_cta_phase_h = ParagraphStyle(
    "cta_phase_h", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=11, leading=15, textColor=WHITE, alignment=TA_LEFT
)
style_cta_phase_b = ParagraphStyle(
    "cta_phase_b", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10, leading=14.5, textColor=WHITE, alignment=TA_LEFT
)
style_recap = ParagraphStyle(
    "recap", parent=styles["Normal"], fontName="Helvetica",
    fontSize=8.3, leading=13, textColor=colors.HexColor("#ffe8d9"), alignment=TA_LEFT
)
style_intro_stat_num = ParagraphStyle(
    "intro_stat_num", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=52, leading=52, textColor=WHITE, alignment=TA_CENTER
)
style_intro_stat_lbl = ParagraphStyle(
    "intro_stat_lbl", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=9, leading=12, textColor=WHITE, alignment=TA_CENTER
)


def rounded_card(c, x, y, w, h, radius=8, fill=CARD_BG, accent=ORANGE):
    c.saveState()
    c.setFillColor(fill)
    c.roundRect(x, y, w, h, radius, stroke=0, fill=1)
    c.setFillColor(accent)
    c.roundRect(x, y, 4, h, 2, stroke=0, fill=1)
    c.restoreState()


def cover_bg(c: pdfcanvas.Canvas, doc):
    c.saveState()
    c.drawImage(GRADIENT_BG_PATH, 0, 0, width=doc.pagesize[0], height=doc.pagesize[1])
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(20 * mm, doc.pagesize[1] - 18 * mm, COVER_TAG)
    logo_w, logo_h = 32 * mm, 22.7 * mm
    pad = 4 * mm
    chip_x = doc.pagesize[0] - logo_w - 16 * mm - pad
    chip_y = doc.pagesize[1] - logo_h - 10 * mm - pad
    c.setFillColor(WHITE)
    c.roundRect(chip_x, chip_y, logo_w + 2 * pad, logo_h + 2 * pad, 6, stroke=0, fill=1)
    c.drawImage(LOGO_PATH, chip_x + pad, chip_y + pad, width=logo_w, height=logo_h, mask="auto")
    photo_d = logo_h + 2 * pad
    photo_x = chip_x - photo_d - 5 * mm
    photo_y = chip_y
    c.setFillColor(WHITE)
    c.circle(photo_x + photo_d / 2, photo_y + photo_d / 2, photo_d / 2 + 1.2, stroke=0, fill=1)
    c.drawImage(PHOTO_PATH, photo_x, photo_y, width=photo_d, height=photo_d, mask="auto")
    c.restoreState()


def content_bg(c: pdfcanvas.Canvas, doc):
    c.saveState()
    c.setFillColor(WHITE)
    c.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)
    c.setFillColor(ORANGE)
    c.rect(0, doc.pagesize[1] - 6 * mm, doc.pagesize[0], 6 * mm, fill=1, stroke=0)
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8)
    c.drawString(20 * mm, 10 * mm, FOOTER_TITLE)
    c.drawRightString(doc.pagesize[0] - 20 * mm, 10 * mm, f"{doc.page - 1}")
    logo_w, logo_h = 16 * mm, 11.4 * mm
    c.drawImage(LOGO_PATH, doc.pagesize[0] - logo_w - 20 * mm, doc.pagesize[1] - logo_h - 12 * mm,
                width=logo_w, height=logo_h, mask="auto")
    c.restoreState()


def cta_bg(c: pdfcanvas.Canvas, doc):
    c.saveState()
    c.drawImage(GRADIENT_BG_PATH, 0, 0, width=doc.pagesize[0], height=doc.pagesize[1])
    logo_w, logo_h = 28 * mm, 19.9 * mm
    pad = 4 * mm
    photo_d = logo_h + 2 * pad
    group_w = photo_d + 5 * mm + (logo_w + 2 * pad)
    group_x0 = (doc.pagesize[0] - group_w) / 2
    chip_y = doc.pagesize[1] - logo_h - 14 * mm - pad
    photo_x = group_x0
    chip_x = photo_x + photo_d + 5 * mm
    c.setFillColor(WHITE)
    c.circle(photo_x + photo_d / 2, chip_y + photo_d / 2, photo_d / 2 + 1.2, stroke=0, fill=1)
    c.drawImage(PHOTO_PATH, photo_x, chip_y, width=photo_d, height=photo_d, mask="auto")
    c.setFillColor(WHITE)
    c.roundRect(chip_x, chip_y, logo_w + 2 * pad, logo_h + 2 * pad, 6, stroke=0, fill=1)
    c.drawImage(LOGO_PATH, chip_x + pad, chip_y + pad, width=logo_w, height=logo_h, mask="auto")
    c.restoreState()


def error_badge_flowable_table(num, title, why, detect, fix, card_h_mm=112):
    inner = [
        [Paragraph("POR QUÉ OCURRE", style_label)],
        [Paragraph(why, style_body)],
        [Paragraph("CÓMO DETECTARLO EN 5 MINUTOS", style_label)],
        [Paragraph(detect, style_body)],
        [Paragraph("CÓMO ARREGLARLO", style_label)],
        [Paragraph(fix, style_body)],
    ]
    inner_table = Table(inner, colWidths=[None])
    inner_table.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    badge = Table([[f"{num:02d}"]], colWidths=[9 * mm], rowHeights=[9 * mm])
    badge.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ORANGE),
        ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROUNDEDCORNERS", [9, 9, 9, 9]),
    ]))

    header = Table([[badge, Paragraph(title, style_error_title)]], colWidths=[13 * mm, None])
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    card_content = Table([[header], [Spacer(1, 6)], [inner_table]], colWidths=[None])
    card_content.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
    ]))

    outer = Table([[card_content]], colWidths=[None], rowHeights=[card_h_mm * mm])
    outer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LINEBEFORE", (0, 0), (0, 0), 4, ORANGE),
        ("ROUNDEDCORNERS", [8, 8, 8, 8]),
    ]))
    return outer


def build():
    Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(OUTPUT_PATH, pagesize=A4,
                           leftMargin=20 * mm, rightMargin=20 * mm,
                           topMargin=18 * mm, bottomMargin=18 * mm)

    frame_cover = Frame(20 * mm, 18 * mm, doc.pagesize[0] - 40 * mm, doc.pagesize[1] - 60 * mm, id="cover")
    frame_content = Frame(20 * mm, 18 * mm, doc.pagesize[0] - 40 * mm, doc.pagesize[1] - 42 * mm, id="content")
    frame_cta = Frame(20 * mm, 18 * mm, doc.pagesize[0] - 40 * mm, doc.pagesize[1] - 36 * mm, id="cta")

    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=frame_cover, onPage=cover_bg),
        PageTemplate(id="Content", frames=frame_content, onPage=content_bg),
        PageTemplate(id="CTA", frames=frame_cta, onPage=cta_bg),
    ])

    story = []

    # ---------- COVER ----------
    story.append(Spacer(1, 70 * mm))
    story.append(Paragraph(COVER_TITLE_HTML, style_h1_cover))
    story.append(Spacer(1, 10))
    story.append(Paragraph(COVER_SUBTITLE, style_sub_cover))
    story.append(Spacer(1, 60))
    author_table = Table([[Paragraph(
        "JORGE SEGOVIA<br/><font color='#5a4433' size=9>Consultor SEO para Ecommerce</font>", style_author_cover)]],
        colWidths=[None])
    author_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WHITE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROUNDEDCORNERS", [20, 20, 20, 20]),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))
    story.append(author_table)
    story.append(NextPageTemplate("Content"))
    story.append(PageBreak())

    # ---------- INTRO ----------
    story.append(Paragraph(INTRO_TITLE, style_h2))
    intro_left = []
    for i, p in enumerate(INTRO_PARAGRAPHS):
        intro_left.append(Paragraph(p, style_intro))
        if i < len(INTRO_PARAGRAPHS) - 1:
            intro_left.append(Spacer(1, 8))
    stat_cell = Table([
        [Paragraph(STAT_NUMBER, style_intro_stat_num)],
        [Paragraph(STAT_LABEL, style_intro_stat_lbl)],
    ], colWidths=[42 * mm])
    stat_cell.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ORANGE),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (0, 0), 16),
        ("BOTTOMPADDING", (0, 0), (0, 0), 4),
        ("BOTTOMPADDING", (0, 1), (0, 1), 16),
        ("ROUNDEDCORNERS", [10, 10, 10, 10]),
    ]))
    intro_table = Table([[intro_left, stat_cell]], colWidths=[None, 46 * mm])
    intro_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (1, 0), (1, 0), 14),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(intro_table)
    story.append(Spacer(1, 14))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e6ee")))
    story.append(PageBreak())

    # ---------- PUNTOS (2 por página) ----------
    for i in range(0, len(POINTS), 2):
        pair = POINTS[i:i + 2]
        for j, (title, why, detect, fix) in enumerate(pair):
            num = i + j + 1
            story.append(error_badge_flowable_table(num, title, why, detect, fix))
            if j == 0 and len(pair) > 1:
                story.append(Spacer(1, 10))
        if i + 2 < len(POINTS):
            story.append(PageBreak())

    # ---------- CTA ----------
    story.append(NextPageTemplate("CTA"))
    story.append(PageBreak())
    story.append(Spacer(1, 20 * mm))
    story.append(Paragraph(CTA_TITLE, style_cta_title))
    story.append(Paragraph(CTA_BODY, style_cta_body))
    story.append(Spacer(1, 22))

    def phase_badge(n):
        t = Table([[str(n)]], colWidths=[9 * mm], rowHeights=[9 * mm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 11),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ROUNDEDCORNERS", [9, 9, 9, 9]),
        ]))
        return t

    phase_table = Table([
        [phase_badge(1), Paragraph("FASE 1 · AUDITORÍA SEO", style_cta_phase_h),
         Paragraph("Informe de +100 páginas con Keyword Research, arquitectura SEO transaccional, "
                    "ranking de keywords actuales y todos los anexos.", style_cta_phase_b)],
        [phase_badge(2), Paragraph("FASE 2 · IMPLEMENTACIÓN", style_cta_phase_h),
         Paragraph("Aplicamos juntos todos los cambios propuestos en la auditoría y la nueva "
                    "arquitectura SEO transaccional.", style_cta_phase_b)],
    ], colWidths=[13 * mm, 45 * mm, None])
    phase_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, colors.HexColor("#ffcfa8")),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(phase_table)
    story.append(Spacer(1, 26))
    story.append(Paragraph("jorge@jscautomation.es · jorgesegoviaciscar.com", style_cta_body))
    if len(POINTS) > 1:
        story.append(Spacer(1, 30))
        recap = " · ".join(f"{idx + 1}. {name}" for idx, (name, *_r) in enumerate(POINTS))
        story.append(Paragraph(recap, style_recap))

    doc.build(story)
    print(f"PDF generado: {OUTPUT_PATH}")


if __name__ == "__main__":
    build()
