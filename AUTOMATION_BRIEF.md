# Brief de automatización diaria — Jorge Segovia (SEO para Ecommerce)

Este documento es la única fuente de verdad que necesita la ejecución programada
de cada mañana (L-V, 8:00 Europe/Madrid). Contiene todo lo acordado con Jorge:
marca, formato, estructura y qué entregar. No se publica nada automáticamente —
solo se prepara el contenido y se envía a Jorge para que él publique.

## 0. Contexto del negocio

Jorge Segovia, consultor SEO especializado en ecommerce (WordPress y Shopify),
foco actual en moda pero abierto a cualquier sector ecommerce. Servicio en 2 fases:
Fase 1 (auditoría SEO de +100 páginas: keyword research, arquitectura SEO
transaccional, ranking actual, anexos) y Fase 2 (implementación).

Web: jorgesegoviaciscar.com · Email: jorge@jscautomation.es

## 1. Rotación semanal (mismo esqueleto de post, ángulo distinto cada día)

| Día | Ángulo |
|---|---|
| Lunes | Roast: error real de auditoría (anonimizado) |
| Martes | Mito SEO desmontado con datos |
| Miércoles | Auditoría exprés a una marca ecommerce grande y pública (nunca cliente de Jorge, dato 100% verificable) |
| Jueves | Cambio de algoritmo / tendencia SEO reciente explicada para ecommerce |
| Viernes | Pregunta abierta a la comunidad + resumen rápido de la semana |

## 2. Esqueleto del post de LinkedIn (siempre igual, cambia el contenido)

1. **Hook** (1-2 líneas, dato/situación sorprendente)
2. **Contexto** (tipo de tienda/situación, siempre anonimizado si es un caso real)
3. **El desarrollo** (el roast / mito / hallazgo, con tono ligero pero riguroso)
4. **Por qué importa / qué está en juego** — deja claro el coste de no arreglarlo,
   pero SIN dar los pasos de la solución (ver regla de la sección 4 — aplica
   igual aquí: la solución completa vive solo en el PDF, ni el post ni el
   artículo deben regalarla)
5. **Prueba** (cifra de mejora, cuando aplique)
6. **CTA** al PDF: enlace al artículo del blog (el enlace real lo añade Jorge al publicar)

Tono: cercano, con personalidad, nunca acartonado. Nunca inventar cifras — si no
hay un dato real verificable, no se afirma un resultado concreto.

## 3. Imagen del post

Todas las rutas del proyecto son **relativas al repo** (funciona igual en local
que en el sandbox Linux de la ejecución en la nube). Nunca uses rutas
absolutas tipo `C:\...`.

Usar `scripts/generate_post_image.py` como base. Antes de ejecutar, edita solo
estas variables al principio del archivo:

- `TITLE_LINE1` / `TITLE_LINE2`: titular descriptivo del post (no genérico), 2
  líneas, en mayúsculas. La línea 2 sale resaltada en naranja automáticamente.
- `SUBTITLE`: una frase corta de apoyo/CTA (p.ej. "Cómo detectarlo en 5 minutos >>").
- `PANEL_TAG`: normalmente "HERRAMIENTAS DE HOY".
- `TOOL_LOGOS`: 2-3 herramientas realmente relevantes al tema del día. Si el logo
  no existe ya en `assets/branding/tool-logos/`, descárgalo así (con `-L` para
  seguir redirecciones):
  ```
  curl -sL -o assets/branding/tool-logos/<nombre>.png \
    "https://www.google.com/s2/favicons?domain=<dominio-de-la-herramienta>&sz=128"
  ```

Después ejecuta: `python3 scripts/generate_post_image.py content/<carpeta-del-día>/imagen-post.png`
(el primer argumento es la ruta de salida; si se omite, usa una ruta por defecto).

**Importante — fuentes**: el script usa fuentes libres bundleadas en
`assets/fonts/` (Archivo Black + Barlow Bold, licencia OFL), NO Arial/Windows.
Estas fuentes **no incluyen emojis ni símbolos Unicode especiales** (💡👇🚀 etc.)
— si aparecen como un cuadrado roto en la imagen, es por esto. Usa solo texto
normal y como mucho caracteres ASCII simples para flechas/marcas (`>>`, `-`,
`*`), nunca emoji, en `TITLE_LINE1`, `TITLE_LINE2`, `SUBTITLE` ni `PANEL_TAG`.
(Los emojis SÍ están bien en el texto del post de LinkedIn y en el artículo del
blog — la limitación es solo para el texto que se dibuja dentro de la imagen.)

Reglas de diseño ya validadas con Jorge — no cambiarlas sin que lo pida:
- El texto y la foto de Jorge NUNCA deben tocarse/solaparse (bandas separadas).
- Las dos líneas del título tampoco deben solaparse entre sí.
- Debe quedar compacto, sin espacios en blanco grandes — si sobra hueco, añadir
  una línea de subtítulo o ajustar tamaños, no dejarlo vacío.
- Logos grandes y legibles, panel simple (sin diagramas complejos de flechas
  salvo que encaje mejor para un tema muy concreto).

## 3bis. PDF del día (lead magnet) — UNO DISTINTO CADA DÍA, nunca repetido

**Importante**: Jorge no quiere que se repita el mismo PDF semana tras
semana. Cada día se genera un PDF nuevo, centrado en el tema exacto del post
de ese día (no una checklist genérica de 12 puntos salvo que el ángulo del
día lo justifique).

Usar `scripts/generate_lead_magnet_pdf.py` como base. Edita las variables al
principio del archivo (sección CONFIG) según el tema de hoy:

- `COVER_TITLE_HTML`: título de portada (con `<br/>` para saltos de línea),
  específico del tema del día — no reutilices el título del checklist salvo
  que el ángulo de hoy sea literalmente ese.
- `COVER_SUBTITLE`, `COVER_TAG`, `STAT_NUMBER`, `STAT_LABEL`: ajusta al
  contenido — si el documento trata sobre un único hallazgo/mito/tendencia,
  `STAT_NUMBER` puede ser "1" (o el número de puntos reales que tenga) y
  `STAT_LABEL` describir de qué es ese número.
- `POINTS`: lista de 1 a varios puntos `(título, por qué ocurre, cómo
  detectarlo, cómo arreglarlo)`. Para el roast del lunes, normalmente 1 punto
  (desarrollo en profundidad del error del día). Para otros formatos, usa el
  número de puntos que tenga sentido con el contenido real del post (nunca
  inventes puntos de relleno solo por completar una lista).
- `FOOTER_TITLE`, `CTA_TITLE`, `CTA_BODY`: ajusta el texto, mantén el CTA de
  las 2 fases (Fase 1 / Fase 2) tal cual, es fijo.

Ejecuta pasando la ruta de salida como argumento:
```
python3 scripts/generate_lead_magnet_pdf.py content/<carpeta-del-día>/lead-magnet.pdf
```

**No hay emojis que evitar aquí** (reportlab usa fuentes PDF estándar,
soportan acentos y símbolos normales sin problema — la limitación de fuentes
es solo para `generate_post_image.py`).

### Cómo se aloja el PDF (automático, sin que Jorge suba nada)

Jorge no tiene forma de recibir un PDF nuevo cada día y subirlo él mismo sin
que deje de ser "automático" — así que el PDF se aloja usando el propio
repositorio de GitHub, que ya es público. En cuanto hagas commit y push (paso
8 de la sección 6), el PDF queda disponible en:

```
https://raw.githubusercontent.com/jscautomation/jorge-linkedin-seo-daily/main/content/<carpeta-del-día>/lead-magnet.pdf
```

Usa exactamente esa URL (con la carpeta del día correcta) como `pdfUrl` en el
formulario del artículo (ver sección 4). Como el commit+push ocurre en el
mismo run antes de que Jorge publique nada, la URL ya estará viva cuando
alguien la use.

## 4. Artículo de blog (HTML para WordPress)

Usar como plantilla `content/2026-08-17-lunes-roast/articulo-blog.html`
(estructura de headings + párrafos + el bloque de formulario ya integrado al
final, sin tocar el `<script>` del formulario más que estas dos líneas, que
**sí cambian cada día**:

- `pdfTitulo`: el mismo texto que uses en `COVER_TITLE_HTML` del PDF de hoy
  (versión en texto plano, sin `<br/>`).
- `pdfUrl`: la URL de raw.githubusercontent.com del PDF de hoy (ver sección
  3bis) — nunca reutilices la URL de un día anterior.

### 🚫 Regla crítica: el artículo NUNCA da la solución completa

El artículo (y el post de LinkedIn) están para enganchar y generar la
necesidad de descargar el PDF — **no para resolver el problema por sí
solos**. Si el lector se va con la solución completa sin rellenar el
formulario, no hay ningún motivo para que descargue el PDF ni deje su email,
y se rompe todo el embudo de captación de leads.

Lo que SÍ puede llevar el artículo (esto genera confianza y demuestra que
Jorge sabe de lo que habla, sin regalar la solución):
- El problema explicado en profundidad: qué es, por qué ocurre, por qué
  importa/cuesta dinero.
- Cómo detectarlo/diagnosticarlo tú mismo (esto es diagnóstico, no arreglo —
  compartirlo está bien, de hecho genera más ganas de saber cómo arreglarlo).
- El contexto o caso (anonimizado) que da pie al post.

Lo que el artículo NUNCA debe incluir:
- Los pasos concretos de la solución/arreglo (nada de listas tipo "así lo
  arreglas: 1... 2... 3...").
- Cualquier cosa que, si el lector la copia, resuelva el problema sin
  necesitar el PDF.

En su lugar, cierra el artículo con un párrafo que teasee la solución sin
darla (p.ej. "La solución tiene 3 pasos muy concretos que explico con
capturas de pantalla y ejemplos reales en la guía gratuita — te la dejo
abajo, tarda 30 segundos en llegarte por email") y el bloque del formulario
justo después. La solución paso a paso vive ÚNICAMENTE dentro del PDF
(sección `POINTS` → campo "cómo arreglarlo" de `generate_lead_magnet_pdf.py`).

Estructura del artículo: título H1 descriptivo, 3-5 secciones H2 breves que
desarrollan el ángulo del día en más profundidad que el post, ejemplos
concretos, y termina con el bloque de formulario ya montado (copiar tal cual
desde la plantilla, solo cambiando pdfTitulo/pdfUrl).

## 5. Formulario de captura (fijo, no tocar salvo instrucción expresa)

Plantilla maestra: `templates/formulario-lead-magnet.html`. Ya incluye:
- Degradado de marca (135°, #FFA135 → #FF5A1F), foto + logo de Jorge.
- Doble llamada a Klaviyo (subscribe a la lista Y8MmeF + evento "Solicitó Lead
  Magnet" que dispara el flow "Lead prueba"). Esto ya está probado y funciona.
- No modificar esta lógica salvo que Jorge lo pida explícitamente.

## 6. Entrega diaria — output

Carpeta: `content/YYYY-MM-DD-<día-en-español>-<formato>/` con:
- `post-linkedin.txt`
- `imagen-post.png`
- `articulo-blog.html`
- `lead-magnet.pdf` (nuevo cada día — ver sección 3bis)

**Orden importante**: genera y haz commit+push del PDF (y de toda la carpeta)
ANTES de dar el artículo por terminado, porque el HTML del artículo depende
de la URL pública del PDF ya subido (sección 3bis).

Al terminar, enviar los archivos a Jorge (vía SendUserFile) con una nota
breve indicando qué toca hacer: 1) copiar el post + subir la imagen a
LinkedIn, 2) pegar el HTML del artículo en WordPress y publicar. Recordar que
todo lo demás (leads, envío del PDF) es 100% automático y no requiere ninguna
acción suya.

**Nunca publicar nada automáticamente** (ni en LinkedIn ni en WordPress ni en
Klaviyo) — el output es siempre para que Jorge revise y publique él mismo.

## 7. Entorno de ejecución (nube)

- Instala dependencias con `pip install -r requirements.txt` si `Pillow` no
  está ya disponible.
- Intenta entregar los 3 archivos directamente al usuario (herramienta de
  envío de archivos si está disponible en la sesión).
- **Además, y siempre**, haz commit y push de la carpeta `content/<día>/`
  generada al repositorio (mismo remoto del que se clonó), como red de
  seguridad por si la entrega directa fallara. Usa un mensaje de commit tipo
  `Contenido diario: <fecha> (<ángulo del día>)`.
