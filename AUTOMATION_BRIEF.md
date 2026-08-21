# Brief de automatización diaria — Jorge Segovia (SEO para Ecommerce)

Este documento es la única fuente de verdad que necesita la ejecución programada
de cada mañana (L-V, 8:00 Europe/Madrid). Contiene todo lo acordado con Jorge:
marca, formato, estructura y qué entregar. Nada se deja publicado en vivo de
forma automática — el borrador de WordPress sí se crea solo (ver sección 9),
pero el post de LinkedIn y el clic final de "Publicar" en WordPress siempre
son de Jorge.

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
| Viernes | Pregunta abierta a la comunidad SEO (desde el 21/08/2026, **ya no** lleva resumen de la semana — ver nota abajo) |

**Nota sobre el viernes (vigente desde el 21/08/2026):** el post del viernes ya
no repasa lo publicado de lunes a jueves. Es una pregunta abierta a la
comunidad SEO, con esqueleto propio (sigue el mismo de la sección 2, pero
adaptado):
- Hook: la pregunta en sí, planteada con fuerza (no genérica tipo "¿qué
  opináis del SEO?" — un debate real y concreto del sector).
- Jorge da primero **su propia respuesta** (una postura o un caso concreto,
  a modo de ejemplo) para arrancar la conversación — nunca lanza la
  pregunta en el aire sin más.
- Desarrollo: por qué esa pregunta/postura importa y qué está en juego,
  igual que cualquier otro día — con su propio tema real de fondo (no
  inventado), sujeto a las mismas reglas de la sección 1bis (no repetir) y
  la regla crítica de la sección 4 (nunca dar la solución completa fuera
  del PDF).
- Cierre: reitera la pregunta e invita explícitamente a responder en
  comentarios.
- Sigue llevando PDF del día (sección 3bis) y artículo (sección 4) con
  normalidad — el ángulo "pregunta abierta" no exime de ninguna de las
  entregas obligatorias de la sección 6.

## 1bis. No repetir tema — registro obligatorio en `TEMAS_TRATADOS.md`

Antes de elegir el tema del día, **lee `TEMAS_TRATADOS.md`** (raíz del repo)
y revisa la tabla del ángulo que toca hoy (Lunes→Roast, Martes→Mito, etc.).

- Elige un tema que no esté ya cubierto — ni con el mismo título literal, ni
  con el mismo fondo (p. ej. "duplicación por parámetros de filtro" y
  "duplicación por versión con/sin www" son temas distintos, pero dos roasts
  sobre parámetros de filtro en tiendas distintas SÍ cuentan como repetido:
  lo que no se repite es el **error/mito/hallazgo de fondo**, no el nombre
  de la marca o el redactado).
- Si al revisar la tabla no encuentras ningún tema libre y razonable para el
  ángulo de hoy (muy improbable a corto plazo, pero puede pasar tras muchas
  semanas), no repitas uno igualmente — genera el resto del contenido normal
  pero avisa explícitamente a Jorge en la entrega de que hace falta que le
  pase un tema nuevo para ese ángulo.
- **Al terminar** de generar todo el contenido del día, añade una fila nueva
  al final de la tabla correspondiente en `TEMAS_TRATADOS.md` (fecha, tema,
  nota breve de la solución/ángulo) y haz commit+push de ese archivo junto
  con la carpeta `content/<día>/` (mismo commit o el siguiente, pero siempre
  el mismo día). Nunca lo dejes para "el próximo día" — si no se registra en
  el momento, se pierde el propósito del control.

## 2. Esqueleto del post de LinkedIn (siempre igual, cambia el contenido)

0. **Titular de apertura** (desde el 20/08/2026, obligatorio): la primera línea
   del post — sola, en su propio párrafo, antes del hook — es un titular corto
   y contundente que refleje el mismo golpe de efecto que el titular visual de
   la imagen (`TITLE_LINE1` + `TITLE_LINE2`, ver sección 3). Normalmente en
   mayúsculas y cerrado en punto, como frase autoconclusiva — p.ej. "FICHA DE
   PRODUCTO: GOOGLE YA NO TE VE." El texto y la imagen deben "decir lo mismo"
   a primer golpe de vista.
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

**Longitud** (desde el 20/08/2026): apunta a 150-200 palabras en total, no a
230+. Mismo esqueleto de 6-7 puntos, pero compacto — si un párrafo puede decir
lo mismo en menos frases, recorta antes de añadir matices extra.

## 3. Imagen del post

Todas las rutas del proyecto son **relativas al repo** (funciona igual en local
que en el sandbox Linux de la ejecución en la nube). Nunca uses rutas
absolutas tipo `C:\...`.

Usar `scripts/generate_post_image.py` como base. **Estructura vigente desde el
20/08/2026 — "stat hero"** (sustituye al antiguo estilo "workflow" de panel
gris arriba; no volver a ese estilo salvo que Jorge lo pida explícitamente):
etiqueta del tema arriba centrada, cifra de impacto gigante como titular
visual, título negro+naranja debajo, tira fina de logos de herramientas, y
barra inferior en **naranja corporativo** con la foto de Jorge + el CTA al PDF.

Antes de ejecutar, edita solo estas variables al principio del archivo:

- `PANEL_TAG`: etiqueta pequeña centrada arriba del todo — el tema/ángulo del
  día (p.ej. "TENDENCIA SEO · ECOMMERCE", "ROAST SEO · ECOMMERCE").
- `STAT_NUMBER` / `STAT_LABEL`: la cifra de impacto que hace de titular visual
  principal (p.ej. "83%" / "de las búsquedas con IA no dan ni un clic"). Usa
  un dato público real y verificable relevante al ángulo de hoy cuando exista
  (el de la tendencia, el % del mito, el hallazgo cuantificado de la
  auditoría...). Si ese día no hay una cifra pública sólida que encaje, usa en
  su lugar un número corto igual de relevante (p.ej. el nº de puntos del PDF,
  "40" de las URLs clon, etc.) — nunca lo dejes vacío, es el elemento más
  grande de toda la imagen.
- `TITLE_LINE1` / `TITLE_LINE2`: titular descriptivo del post (no genérico), 2
  líneas, en mayúsculas. La línea 2 sale resaltada en naranja automáticamente.
  Debe ser coherente con el titular de apertura del texto del post (sección 2,
  punto 0) — mismo mensaje, misma fuerza.
- `SUBTITLE`: el texto de la barra naranja inferior. **Debe dejar claro que el
  PDF gratis está en el enlace al final del post** (p.ej. "GRATIS: el PDF está
  en el enlace al final del post >>") — no un CTA genérico sin más, porque es
  el único sitio de la imagen donde se indica dónde está el enlace real que
  añade Jorge al publicar.
- `TOOL_LOGOS`: 2 herramientas realmente relevantes al tema del día. **No
  repitas siempre el mismo dúo** (antes de elegir, mira qué se usó los últimos
  2-3 días en `git log -p -- scripts/generate_post_image.py` y varía si
  aplica). Si el logo no existe ya en `assets/branding/tool-logos/`:
  1. Primero intenta el favicon de Google (rápido si el entorno lo permite):
     ```
     curl -sL -o assets/branding/tool-logos/<nombre>.png \
       "https://www.google.com/s2/favicons?domain=<dominio-de-la-herramienta>&sz=128"
     ```
  2. Si falla (en el sandbox de la nube, `www.google.com` y casi cualquier
     dominio externo salvo GitHub están bloqueados por política de red del
     entorno — error 403 de la CONNECT del proxy, confirmable con
     `curl -sS "$HTTPS_PROXY/__agentproxy/status"`), usa el logo oficial real
     de la marca desde el repo público **simple-icons** (sí accesible, vía
     `raw.githubusercontent.com`), con su color de marca correcto en vez de un
     favicon genérico:
     ```
     # 1) color de marca (busca el título en el JSON)
     curl -sS -o /tmp/icons.json \
       "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/data/simple-icons.json"
     python3 -c "import json; d=json.load(open('/tmp/icons.json')); \
       [print(i['title'], i['hex']) for i in d if '<nombre herramienta>'.lower() in i['title'].lower()]"

     # 2) SVG oficial (slug = título en minúsculas sin espacios/símbolos)
     curl -sS -o /tmp/logo.svg \
       "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/<slug>.svg"

     # 3) colorear con el hex del paso 1 y rasterizar a PNG 400x400
     python3 -c "
     import re, cairosvg
     svg = open('/tmp/logo.svg', encoding='utf-8').read()
     svg = re.sub(r'<path ', '<path fill=\"#<HEX>\" ', svg, count=1)
     open('/tmp/logo.svg', 'w', encoding='utf-8').write(svg)
     cairosvg.svg2png(url='/tmp/logo.svg',
       write_to='assets/branding/tool-logos/<nombre>.png', output_width=400, output_height=400)
     "
     ```
     (`pip install cairosvg` si no está ya instalado). Si la herramienta no
     existe en simple-icons, reutiliza el logo real más parecido que ya haya
     en `assets/branding/tool-logos/` antes que dejar un logo genérico o
     repetido sin sentido.
  3. Nunca uses una foto ni un montaje "con IA" simulando una captura de
     pantalla real — o es un logo oficial de verdad, o (si en el futuro el
     entorno permite navegar a la herramienta) una captura real hecha con el
     navegador, nunca una imagen inventada que aparente serlo.

Después ejecuta: `python3 scripts/generate_post_image.py content/<carpeta-del-día>/imagen-post.png`
(el primer argumento es la ruta de salida; si se omite, usa una ruta por defecto).

**Importante — fuentes**: el script usa fuentes libres bundleadas en
`assets/fonts/` (Archivo Black + Barlow Bold, licencia OFL), NO Arial/Windows.
Estas fuentes **no incluyen emojis ni símbolos Unicode especiales** (💡👇🚀 etc.)
— si aparecen como un cuadrado roto en la imagen, es por esto. Usa solo texto
normal y como mucho caracteres ASCII simples para flechas/marcas (`>>`, `-`,
`*`), nunca emoji, en `TITLE_LINE1`, `TITLE_LINE2`, `SUBTITLE`, `PANEL_TAG`,
`STAT_NUMBER` ni `STAT_LABEL`. (Los emojis SÍ están bien en el texto del post
de LinkedIn y en el artículo del blog — la limitación es solo para el texto
que se dibuja dentro de la imagen.)

Reglas de diseño ya validadas con Jorge — no cambiarlas sin que lo pida:
- El texto y la foto de Jorge NUNCA deben tocarse/solaparse (bandas separadas).
- Las dos líneas del título tampoco deben solaparse entre sí, ni ningún otro
  bloque de texto con otro (usa `wrap_two_lines()` para repartir frases largas
  en 2 líneas equilibradas antes de dar por bueno un layout).
- Debe quedar compacto, sin espacios en blanco grandes — si sobra hueco, añadir
  una línea de subtítulo o ajustar tamaños, no dejarlo vacío.
- Logos grandes y legibles, sin diagramas complejos de flechas salvo que
  encaje mejor para un tema muy concreto.
- La barra inferior es **naranja corporativo** (no gris) — foto con borde
  blanco (para que contraste sobre el naranja) + CTA en blanco al lado.

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

Ejecuta pasando la ruta de salida como argumento. **El nombre del archivo
debe ser un slug del título del PDF (nunca el genérico "lead-magnet.pdf")**,
porque es literalmente el nombre que le queda guardado al usuario cuando lo
descarga — un nombre genérico repetido cada día es una mala experiencia y
además pisaría descargas anteriores en su carpeta de Descargas:

```
python3 scripts/generate_lead_magnet_pdf.py content/<carpeta-del-día>/<slug-del-titulo>.pdf
```

Ejemplo: si `COVER_TITLE_HTML` es "Duplicado no es<br/>penalización<br/>(es
otra cosa)", el slug sería `duplicado-no-es-penalizacion.pdf` (minúsculas,
sin acentos ni signos, espacios → guiones, sin la parte entre paréntesis si
la hay).

**No hay emojis que evitar aquí** (reportlab usa fuentes PDF estándar,
soportan acentos y símbolos normales sin problema — la limitación de fuentes
es solo para `generate_post_image.py`).

### Cómo se aloja el PDF (automático, sin que Jorge suba nada)

Jorge no tiene forma de recibir un PDF nuevo cada día y subirlo él mismo sin
que deje de ser "automático" — así que el PDF se aloja usando el propio
repositorio de GitHub, que ya es público. En cuanto hagas commit y push (paso
8 de la sección 6), el PDF queda disponible en:

```
https://raw.githubusercontent.com/jscautomation/jorge-linkedin-seo-daily/main/content/<carpeta-del-día>/<slug-del-titulo>.pdf
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

### Botones CTA intermedios (desde el 20/08/2026, obligatorio)

Además del bloque de formulario final, el artículo lleva **2 botones CTA**
insertados en medio del texto que enlazan directamente al formulario (mismo
`id="jsc-lead-form"` de más abajo en la página, con scroll suave — nunca un
segundo formulario duplicado). Usa este bloque tal cual, solo cambia el texto
del botón y el sitio donde lo insertas:

```html
<div style="text-align:left;margin:36px 0;">
  <a href="#jsc-lead-form" onclick="var f=document.getElementById('jsc-lead-form'); if(f){f.scrollIntoView({behavior:'smooth'});} return false;" style="display:inline-block;background:#FF5A1F;color:#ffffff;font-weight:700;font-size:15px;line-height:1.3;padding:15px 30px;border-radius:999px;text-decoration:none;box-shadow:0 4px 14px rgba(255,90,31,.35);">
    📥 <texto del botón>
  </a>
</div>
```

Reglas de colocación ya validadas con Jorge — no cambiarlas sin que lo pida:
- **Alineado a la izquierda** (`text-align:left`, nunca centrado), igual que
  el resto del texto del artículo.
- **Primer botón**: justo después del segundo párrafo del artículo (antes del
  primer H2), no más tarde.
- **Segundo botón**: en otro punto natural de intención alta, típicamente
  justo después de la sección de "cómo detectarlo tú mismo" (cuando el lector
  ya sabe que tiene el problema y quiere la solución).
- Nunca más de 2 botones intermedios — el objetivo es dar salidas naturales
  al CTA sin saturar el artículo de banners.

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
- `<slug-del-título>.pdf` (nuevo cada día, nombre descriptivo — ver sección 3bis)
- Fila nueva añadida a `TEMAS_TRATADOS.md` (raíz del repo — ver sección 1bis)

**Orden importante**: genera y haz commit+push del PDF (y de toda la carpeta)
ANTES de dar el artículo por terminado, porque el HTML del artículo depende
de la URL pública del PDF ya subido (sección 3bis).

Al terminar, enviar los archivos a Jorge (vía SendUserFile) con una nota
breve indicando qué toca hacer: 1) copiar el post + subir la imagen a
LinkedIn, 2) revisar el borrador ya creado en WordPress (ver sección 9) y
darle a Publicar. Recordar que todo lo demás (leads, envío del PDF, y desde
que hay credenciales de WordPress configuradas — ver sección 9 — la subida
del borrador) es 100% automático y no requiere ninguna acción suya salvo el
clic final de Publicar.

**Nunca publicar nada automáticamente en el sentido de "dejarlo en vivo"**
(ni en LinkedIn, ni en WordPress, ni en Klaviyo) — desde que hay credenciales
de WordPress disponibles, el artículo SÍ se sube solo a WordPress, pero
siempre como BORRADOR (`status: draft`), nunca publicado directamente; la
rutina nunca pulsa "Publicar" por Jorge, eso es siempre su clic final.

## 7. Entorno de ejecución (nube)

- Instala dependencias con `pip install -r requirements.txt` si `Pillow` no
  está ya disponible.
- Intenta entregar los 3 archivos directamente al usuario (herramienta de
  envío de archivos si está disponible en la sesión).
- **Además, y siempre**, haz commit y push de la carpeta `content/<día>/`
  generada al repositorio (mismo remoto del que se clonó), como red de
  seguridad por si la entrega directa fallara. Usa un mensaje de commit tipo
  `Contenido diario: <fecha> (<ángulo del día>)`.

## 8. Segmento de Klaviyo por PDF (esto NO lo hace la rutina en la nube)

Cada PDF descargado queda perfectamente identificable en Klaviyo (evento
"Solicitó Lead Magnet" con la propiedad `pdf_titulo`). Un segmento en
Klaviyo es dinámico: una vez existe, se actualiza solo con cada nueva
descarga — pero el segmento en sí hay que crearlo una vez por título.

Herramienta recomendada: `scripts/sync_klaviyo_segments.py` — revisa TODO
el historial de descargas, saca los títulos distintos, y crea el segmento
que falte para cada uno (sin duplicar los que ya existen). Ejecutar sin
argumentos; es seguro correrlo tantas veces como se quiera (idempotente).
Alternativa puntual para un solo título nuevo: `scripts/create_klaviyo_segment.py
"Título exacto del PDF"`.

## 9. Borrador en WordPress (SÍ lo hace la rutina en la nube, desde el 18/08/2026)

A diferencia de Klaviyo (sección 8), Jorge decidió explícitamente asumir el
riesgo de exposición y configuró `WP_URL`, `WP_USERNAME` y `WP_APP_PASSWORD`
como **variables de entorno** en el entorno de Claude Code que usa esta
rutina (no en el repo, no en este brief, no en el prompt — solo en la config
del entorno). Motivo del cambio: los entornos de Claude Code en la nube NO
tienen un almacén de secretos dedicado (cualquier sesión que use ese mismo
entorno podría leer esas variables) — es una exposición mayor que la de antes
(cero), pero Jorge la consideró aceptable porque es una contraseña de
**aplicación** de WordPress: revocable en cualquier momento sin afectar al
login normal, y sin alcance fuera de la REST API de posts de ese sitio.

**Paso a ejecutar cada día, justo después del commit+push del paso 12,
ANTES de la entrega final (paso 13):**

```
python3 scripts/publish_to_wordpress.py content/<carpeta-del-día>
```

Esto crea la entrada en WordPress como **borrador** (`status: draft`, nunca
publicado directamente) usando la REST API de WP con Basic Auth + Application
Password. El script extrae el `<h1>` del HTML como título del post y sube el
resto del cuerpo envuelto en un bloque nativo de Gutenberg
(`<!-- wp:html -->...<!-- /wp:html -->`) — **imprescindible**: sin ese
envoltorio, WordPress aplica `wpautop` al contenido y mete etiquetas `<p>`
dentro del `<script>` del formulario, rompiéndolo (el síntoma es que el
formulario se queda colgado en "Cargando..." y nunca deja descargar el PDF).
Jorge revisa el borrador en el editor de WordPress y le da a Publicar cuando
esté conforme.

**Si el script falla** (credenciales que faltan o han caducado, WordPress
caído, etc.): no es un error bloqueante — continúa con el resto del proceso
con normalidad, y en la entrega final al usuario indica explícitamente que
el borrador NO se creó solo esta vez, con el motivo exacto del fallo (la
línea `FAIL (...)` o `ERROR: ...` que imprime el script), para que Jorge lo
suba él mismo con el mismo comando desde su sesión local si quiere.

Credenciales: `WP_URL`, `WP_USERNAME`, `WP_APP_PASSWORD` (contraseña de
aplicación de WordPress, generada en `Usuarios → Perfil → Contraseñas de
aplicación` — no es la contraseña de acceso normal, y es revocable en
cualquier momento sin afectar al login). Viven como variables de entorno del
entorno de Claude Code (para la rutina en la nube) y también en un `.env`
local (para cuando Jorge lo ejecuta él mismo) — nunca en el repo ni en este
brief.

**Nota de infraestructura:** en este sitio en concreto (Hostinger), la
funcionalidad de Application Passwords viene desactivada por defecto a nivel
de hosting. Se reactivó con un snippet PHP vía el plugin WPCode
(`Fragmentos de código`) con estos dos filtros a prioridad alta para ganarle
la partida al filtro que lo bloqueaba:

```php
add_filter( 'wp_is_application_passwords_available', '__return_true', 9999 );
add_filter( 'wp_is_application_passwords_available_for_user', '__return_true', 9999 );
```

Si en el futuro deja de funcionar (p. ej. tras una actualización de Hostinger
que reintroduzca el bloqueo con prioridad aún más alta), revisar primero que
ese snippet siga activo en WPCode antes de investigar nada más.

**A propósito, la rutina en la nube NO ejecuta este script ni tiene la
`KLAVIYO_API_KEY`** — esa clave da acceso de escritura a toda la cuenta de
Klaviyo y no hay forma segura de dársela al entorno en la nube ahora mismo
(la definición de la rutina no soporta secretos, solo prompt de texto plano).
Así que este paso queda pendiente de ejecutarse en una sesión local (por
Jorge pidiéndoselo a Claude, o por Claude si nota que hay un PDF nuevo sin
segmento) — no se te ocurra a ti, rutina en la nube, intentar llamar a la API
de Klaviyo con una clave puesta a mano en este prompt.
