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
4. **La solución real** — 2-4 bullets accionables, útiles aunque no seas cliente
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

## 4. Artículo de blog (HTML para WordPress)

Usar como plantilla `content/2026-08-17-lunes-roast/articulo-blog.html`
(estructura de headings + párrafos + el bloque de formulario ya integrado al
final, sin tocar el `<script>` del formulario más que las dos líneas de
`pdfTitulo` / `pdfUrl`, que de momento son siempre las mismas:

- `pdfTitulo`: "Los 12 errores SEO que más dinero cuestan a un ecommerce"
- `pdfUrl`: "https://jorgesegoviaciscar.com/wp-content/uploads/2026/08/checklist-12-errores-seo-ecommerce.pdf"

(Si en el futuro hay un PDF distinto por tema, avisar a Jorge — hoy en día se
reutiliza siempre el mismo checklist.)

Estructura del artículo: título H1 descriptivo, 3-5 secciones H2 breves que
desarrollan el ángulo del día en más profundidad que el post, ejemplos
concretos, y termina con el bloque de formulario ya montado (copiar tal cual
desde la plantilla, sin modificar el HTML/CSS/JS salvo pdfTitulo/pdfUrl si
cambiaran).

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

Al terminar, enviar los 3 archivos a Jorge (vía SendUserFile) con una nota
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
