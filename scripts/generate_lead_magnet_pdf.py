# -*- coding: utf-8 -*-
"""
Genera el PDF lead magnet (portada + intro + tarjetas de contenido + cierre
con CTA de las 2 fases). Mismo sistema visual siempre — lo que cambia cada
día es el CONFIG de abajo (título, intro, puntos).

Desde el 01/09/2026 usa el MISMO lenguaje visual que la imagen única del
post de LinkedIn (`generate_single_post_image.py` / AUTOMATION_BRIEF.md
sección 3): fondo crema `#FFFCF4`, titular en naranja `#FF914D` con
League Spartan ExtraBold, banda oscura `#282828` (footer de contenido y
CTA), foto circular con anillo naranja + firma "by Jorge Segovia" en el
mismo sitio en toda página. Antes (24/08-01/09/2026) usaba el lenguaje
visual del carrusel ya retirado (fondo negro, ArchivoBlack/Barlow-Bold,
naranja `#FF5A1F`) — se cambió para que el PDF gated y el post/imagen del
día se sientan como el mismo documento de marca, no como dos estilos
distintos.

Uso: python3 scripts/generate_lead_magnet_pdf.py [ruta_de_salida.pdf]
Todas las rutas son relativas al repo (funciona igual en Windows local que
en el sandbox Linux de la ejecución en la nube).
"""
import re
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle,
    HRFlowable, Frame, PageTemplate, BaseDocTemplate, NextPageTemplate
)
from reportlab.pdfgen import canvas as pdfcanvas

REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = REPO_ROOT / "assets" / "fonts"
LOGO_PATH = REPO_ROOT / "assets" / "branding" / "logo.png"
PHOTO_PATH = REPO_ROOT / "assets" / "branding" / "foto-jorge-circle.png"

pdfmetrics.registerFont(TTFont("LSBold", str(FONT_DIR / "LeagueSpartan-Bold.ttf")))
pdfmetrics.registerFont(TTFont("LSExtraBold", str(FONT_DIR / "LeagueSpartan-ExtraBold.ttf")))

# Misma paleta que la imagen del post (ver AUTOMATION_BRIEF.md sección 3.2)
# — no tocar sin cambiar también el motor de generate_single_post_image.py.
BG = colors.HexColor("#FFFCF4")      # crema — fondo de página
ORANGE = colors.HexColor("#FF914D")  # titular / resaltado
BAND = colors.HexColor("#282828")    # banda oscura — footer de contenido y CTA
INK = colors.HexColor("#111111")     # texto principal sobre fondo crema
GRAY = colors.HexColor("#A8A8A2")    # subtexto sobre la banda oscura (no sobre crema — ahí no da contraste)
# Tonos derivados de INK para texto secundario sobre crema (kicker, pie de
# página, recap) y para líneas/bordes sutiles — no son colores nuevos, son
# variantes de opacidad de INK sobre el fondo crema.
INK_MUTED = colors.Color(INK.red, INK.green, INK.blue, alpha=0.6)
DIVIDER = colors.Color(INK.red, INK.green, INK.blue, alpha=0.12)

# ==================================================================
# 👉 CONFIG: esto cambia cada día. El resto del archivo (estilos,
#    layout, funciones) es fijo — no tocar salvo rediseño explícito.
#
# NOVEDAD 24/08/2026: cualquier campo de texto puede envolver una frase
# clave entre <hl>...</hl> para que salga resaltada con caja naranja —
# el mismo efecto que el resaltado de los titulares de la imagen del post.
# Es opcional: si no usas <hl>, el texto sale igual, solo que sin resaltar.
# ==================================================================
COVER_TITLE_HTML = "<hl>Los 12 errores SEO</hl><br/>que más dinero cuestan<br/>a un ecommerce"
COVER_SUBTITLE = "La checklist que uso en cada auditoría SEO a tiendas online de facturación alta (WordPress y Shopify)"
COVER_TAG = "CHECKLIST SEO · ECOMMERCE"  # etiqueta pequeña arriba a la izquierda — se repite en todas las páginas

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
     "En Google Search Console -> Cobertura, busca “Excluida por etiqueta noindex” o “Bloqueada por robots.txt” y revisa si aparecen categorías importantes.",
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
     "En Search Console -> Cobertura, revisa cuántas URLs “No encontradas (404)” corresponden a productos que antes tenían tráfico o enlaces.",
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
CTA_TITLE = "<hl>¿Cuáles de estos errores</hl> tiene tu ecommerce?"
CTA_BODY = "Lo descubrimos en una auditoría SEO completa, diseñada para ecommerce de facturación alta."

# 👉 ruta de salida: por CLI (recomendado en la ejecución diaria) o por defecto
OUTPUT_PATH = sys.argv[1] if len(sys.argv) > 1 else str(
    REPO_ROOT / "assets" / "pdf" / "checklist-12-errores-seo-ecommerce.pdf"
)
# ==================================================================


def hl(text):
    """Convierte <hl>frase</hl> en el span con caja naranja de fondo que
    reportlab SÍ soporta de verdad (<font backColor>) — mismo efecto de
    resaltado que draw_mixed_line()/el titular de la imagen del post. Los
    espacios finos (&#160;) hacen de padding horizontal, ya que <font> no
    admite padding."""
    return re.sub(
        r"<hl>(.*?)</hl>",
        r'<font color="#111111" backColor="#FF914D">&#160;\1&#160;</font>',
        text,
    )


styles_registry = {}


def style(name, **kw):
    kw.setdefault("fontName", "LSBold")
    kw.setdefault("textColor", INK)
    kw.setdefault("alignment", TA_LEFT)
    s = ParagraphStyle(name, **kw)
    styles_registry[name] = s
    return s


style_h1_cover = style("h1_cover", fontName="LSExtraBold", fontSize=27, leading=35, spaceAfter=14, textColor=ORANGE)
style_sub_cover = style("sub_cover", fontSize=12.5, leading=18)
style_author_name = style("author_name", fontName="LSExtraBold", fontSize=12, leading=15, textColor=INK)
style_author_role = style("author_role", fontSize=9, leading=12, textColor=INK)
style_h2 = style("h2", fontName="LSExtraBold", fontSize=18, leading=23, spaceAfter=10)
style_body = style("body", fontSize=10, leading=15.5, spaceAfter=8)
style_intro = style("intro", fontSize=11.5, leading=18)
style_error_title = style("error_title", fontName="LSExtraBold", fontSize=13, leading=17)
style_label = style("label", fontName="LSExtraBold", fontSize=8.5, leading=12, spaceBefore=10, spaceAfter=3)
style_cta_title = style("cta_title", fontName="LSExtraBold", fontSize=22, leading=28, spaceAfter=14, textColor=ORANGE)
style_cta_body = style("cta_body", fontSize=11, leading=16)
style_cta_phase_h = style("cta_phase_h", fontName="LSExtraBold", fontSize=11.5, leading=15, textColor=INK)
style_cta_phase_b = style("cta_phase_b", fontSize=9.7, leading=14, textColor=INK)
style_recap = style("recap", fontSize=8.3, leading=13, textColor=INK_MUTED)
style_intro_stat_num = style("intro_stat_num", fontName="LSExtraBold", fontSize=48, leading=48,
                              textColor=INK, alignment=1)
style_intro_stat_lbl = style("intro_stat_lbl", fontSize=9, leading=12, textColor=INK, alignment=1)
style_kicker = style("kicker", fontSize=8.5, leading=11, textColor=INK_MUTED)


def _header(c, doc):
    """Logo arriba a la izquierda + etiqueta debajo + foto en círculo con
    anillo naranja arriba a la derecha — mismo tratamiento que la firma
    "by Jorge Segovia" de la imagen del post, en el mismo sitio en TODAS
    las páginas."""
    logo_w, logo_h = 20 * mm, 14.2 * mm
    top_y = doc.pagesize[1] - 14 * mm - logo_h
    c.drawImage(str(LOGO_PATH), 20 * mm, top_y, width=logo_w, height=logo_h, mask="auto")
    c.setFillColor(INK_MUTED)
    c.setFont("LSBold", 8)
    c.drawString(20 * mm, top_y - 10, COVER_TAG)

    photo_d = 17 * mm
    photo_x = doc.pagesize[0] - photo_d - 20 * mm
    photo_y = doc.pagesize[1] - 14 * mm - photo_d
    c.setFillColor(ORANGE)
    c.circle(photo_x + photo_d / 2, photo_y + photo_d / 2, photo_d / 2 + 1.4, stroke=0, fill=1)
    c.drawImage(str(PHOTO_PATH), photo_x, photo_y, width=photo_d, height=photo_d, mask="auto")


def page_chrome(c: pdfcanvas.Canvas, doc):
    c.saveState()
    c.setFillColor(BG)
    c.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)
    _header(c, doc)
    c.restoreState()


def content_chrome(c: pdfcanvas.Canvas, doc):
    """Chrome de las páginas de contenido/CTA: además del header, una
    banda oscura fina al pie — el mismo elemento de marca que la barra CTA
    de la imagen del post (fondo crema arriba, banda #282828 abajo)."""
    page_chrome(c, doc)
    c.saveState()
    band_h = 14 * mm
    c.setFillColor(BAND)
    c.rect(0, 0, doc.pagesize[0], band_h, fill=1, stroke=0)
    c.setFillColor(BG)
    c.setFont("LSBold", 7.5)
    c.drawString(20 * mm, band_h / 2 - 3, FOOTER_TITLE)
    c.setFillColor(ORANGE)
    c.drawRightString(doc.pagesize[0] - 20 * mm, band_h / 2 - 3, f"{doc.page - 1}")
    c.restoreState()


def badge(text, size=9 * mm, bg=ORANGE, fg=INK, font="LSExtraBold", fontsize=12):
    t = Table([[text]], colWidths=[size], rowHeights=[size])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("TEXTCOLOR", (0, 0), (-1, -1), fg),
        ("FONTNAME", (0, 0), (-1, -1), font),
        ("FONTSIZE", (0, 0), (-1, -1), fontsize),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROUNDEDCORNERS", [size / 2, size / 2, size / 2, size / 2]),
    ]))
    return t


def point_card(num, title, why, detect, fix):
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
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    header = Table([[badge(f"{num:02d}"), Paragraph(hl(title), style_error_title)]], colWidths=[13 * mm, None])
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    content = Table([[header], [Spacer(1, 8)], [inner_table]], colWidths=[None])
    content.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 16), ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (0, 0), 14), ("BOTTOMPADDING", (0, 2), (0, 2), 14),
        ("BOX", (0, 0), (-1, -1), 0.8, DIVIDER),
        ("LINEBEFORE", (0, 0), (0, 0), 3, ORANGE),
        ("ROUNDEDCORNERS", [8, 8, 8, 8]),
    ]))
    return content


def build():
    Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(OUTPUT_PATH, pagesize=A4,
                           leftMargin=20 * mm, rightMargin=20 * mm,
                           topMargin=18 * mm, bottomMargin=18 * mm)

    frame_cover = Frame(20 * mm, 18 * mm, doc.pagesize[0] - 40 * mm, doc.pagesize[1] - 60 * mm, id="cover")
    frame_content = Frame(20 * mm, 18 * mm, doc.pagesize[0] - 40 * mm, doc.pagesize[1] - 56 * mm, id="content")
    frame_cta = Frame(20 * mm, 18 * mm, doc.pagesize[0] - 40 * mm, doc.pagesize[1] - 56 * mm, id="cta")

    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=frame_cover, onPage=page_chrome),
        PageTemplate(id="Content", frames=frame_content, onPage=content_chrome),
        PageTemplate(id="CTA", frames=frame_cta, onPage=content_chrome),
    ])

    story = []

    # ---------- COVER ----------
    story.append(Spacer(1, 46 * mm))
    story.append(Paragraph(hl(COVER_TITLE_HTML), style_h1_cover))
    story.append(Spacer(1, 10))
    story.append(Paragraph(COVER_SUBTITLE, style_sub_cover))
    story.append(Spacer(1, 110))
    author_table = Table([[Paragraph("JORGE SEGOVIA", style_author_name)],
                           [Paragraph("Consultor SEO para Ecommerce", style_author_role)]],
                          colWidths=[None])
    author_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ORANGE),
        ("ROUNDEDCORNERS", [20, 20, 20, 20]),
        ("LEFTPADDING", (0, 0), (-1, -1), 16), ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (0, 0), 10), ("BOTTOMPADDING", (0, 0), (0, 0), 1),
        ("TOPPADDING", (0, 1), (0, 1), 0), ("BOTTOMPADDING", (0, 1), (0, 1), 10),
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
        ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (0, 0), 16), ("BOTTOMPADDING", (0, 0), (0, 0), 4),
        ("BOTTOMPADDING", (0, 1), (0, 1), 16),
        ("ROUNDEDCORNERS", [10, 10, 10, 10]),
    ]))
    intro_table = Table([[intro_left, stat_cell]], colWidths=[None, 46 * mm])
    intro_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (1, 0), (1, 0), 14), ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(intro_table)
    story.append(Spacer(1, 14))
    story.append(HRFlowable(width="100%", thickness=0.8, color=DIVIDER))
    story.append(PageBreak())

    # ---------- PUNTOS (2 por página) ----------
    for i in range(0, len(POINTS), 2):
        pair = POINTS[i:i + 2]
        for j, (title, why, detect, fix) in enumerate(pair):
            num = i + j + 1
            story.append(point_card(num, title, why, detect, fix))
            if j == 0 and len(pair) > 1:
                story.append(Spacer(1, 12))
        if i + 2 < len(POINTS):
            story.append(PageBreak())

    # ---------- CTA ----------
    story.append(NextPageTemplate("CTA"))
    story.append(PageBreak())
    story.append(Spacer(1, 20 * mm))
    story.append(Paragraph(hl(CTA_TITLE), style_cta_title))
    story.append(Paragraph(CTA_BODY, style_cta_body))
    story.append(Spacer(1, 22))

    def phase_badge(n):
        return badge(str(n), bg=INK, fg=BG, fontsize=11)

    phase_table = Table([
        [phase_badge(1), Paragraph("FASE 1 · AUDITORÍA SEO", style_cta_phase_h),
         Paragraph("Informe de +100 páginas con Keyword Research, arquitectura SEO transaccional, "
                    "ranking de keywords actuales y todos los anexos.", style_cta_phase_b)],
        [phase_badge(2), Paragraph("FASE 2 · IMPLEMENTACIÓN", style_cta_phase_h),
         Paragraph("Aplicamos juntos todos los cambios propuestos en la auditoría y la nueva "
                    "arquitectura SEO transaccional.", style_cta_phase_b)],
    ], colWidths=[13 * mm, 58 * mm, None])
    phase_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), ORANGE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, INK),
        ("LEFTPADDING", (0, 0), (-1, -1), 14), ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 12), ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("ROUNDEDCORNERS", [12, 12, 12, 12]),
    ]))
    story.append(phase_table)
    story.append(Spacer(1, 22))
    story.append(Paragraph("jorge@jscautomation.es · jorgesegoviaciscar.com", style_cta_body))
    if len(POINTS) > 1:
        story.append(Spacer(1, 26))
        recap = " · ".join(f"{idx + 1}. {name}" for idx, (name, *_r) in enumerate(POINTS))
        story.append(Paragraph(recap, style_recap))

    doc.build(story)
    print(f"PDF generado: {OUTPUT_PATH}")


if __name__ == "__main__":
    build()
