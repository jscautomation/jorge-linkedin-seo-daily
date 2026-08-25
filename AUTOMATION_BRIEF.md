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
   y contundente que refleje el mismo golpe de efecto que el título de la
   portada del carrusel (slide `type: "cover"`, ver sección 3). Normalmente en
   mayúsculas y cerrado en punto, como frase autoconclusiva — p.ej. "FICHA DE
   PRODUCTO: GOOGLE YA NO TE VE." El texto y la portada del carrusel deben
   "decir lo mismo" a primer golpe de vista.
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

## 3. Carrusel/documento del post

Todas las rutas del proyecto son **relativas al repo** (funciona igual en local
que en el sandbox Linux de la ejecución en la nube). Nunca uses rutas
absolutas tipo `C:\...`.

**Formato vigente desde el 24/08/2026 — "documento negro con resaltados
naranja".** Sustituye tanto al antiguo "stat hero" de imagen única
(`generate_post_image.py`, ya no se usa salvo que Jorge pida explícitamente
volver a él) como al primer intento de carrusel "captura anotada a mano" con
garabatos. Jorge pidió copiar el lenguaje visual concreto del perfil de
referencia **Twinkle Chatterjee / ThriveCraft SEO** (detectado como uno de
los perfiles SEO de mejor rendimiento en LinkedIn tras un análisis de datos
de Apify) adaptado a la marca de Jorge: fondo negro con rejilla sutil, texto
crema, frases clave resaltadas con una caja naranja detrás (efecto
"subrayador"), foto+logo arriba en el mismo sitio siempre, indicador de
"desliza" abajo a la derecha, y mucha más densidad de texto por slide que el
formato anterior — es justo lo que más engagement genera en el dataset
analizado.

Genera 8-11 slides cuadradas (1080x1080) + un PDF sin pérdida que las
empaqueta todas. **El PDF (`carrusel-post.pdf`) es el artefacto principal:
se sube a LinkedIn como publicación de tipo "Documento" (LinkedIn lo
renderiza como un visor deslizable página a página)** — así es como funciona
el formato de referencia. Los PNG sueltos (`carrusel-1.png`...) existen para
poder revisar/editar cada slide a mano, no para subirlos como carrusel de
imágenes.

### 3.1 El motor es fijo, el contenido se edita cada día

Usar `scripts/generate_carousel_post.py`. El archivo tiene dos partes muy
diferenciadas:

- **Motor de render** (todo lo que hay antes de la sección `CONTENIDO DE HOY`
  del archivo): colores, fuentes, posiciones, tamaños y límites de texto. Es
  **fijo** — no tocar ningún número ni función salvo que Jorge pida
  explícitamente un cambio de estilo. Es lo que garantiza que el carrusel de
  hoy se vea exactamente igual que el de ayer y el de mañana.
- **`CONFIG`** (al final del archivo): un diccionario con la lista de slides
  de hoy. **Esto sí se edita cada día**, igual que con
  `generate_lead_magnet_pdf.py` — edita `CONFIG`, ejecuta el script, mueve el
  resultado a `content/<carpeta-del-día>/`, y revierte el archivo con
  `git checkout -- scripts/generate_carousel_post.py` antes de terminar (para
  que el próximo día vuelva a partir de la plantilla de referencia, no del
  contenido de hoy).

```
python3 scripts/generate_carousel_post.py content/<carpeta-del-día>
```

(el argumento es la carpeta de salida; genera `carrusel-1.png`...
`carrusel-N.png` + `carrusel-post.pdf` dentro).

**Si el script falla con un `AssertionError`**, el mensaje te dice
exactamente qué límite de la sección 3.4 se ha superado y con qué texto —
significa que el contenido de hoy no cabe de forma segura con ese rol de
fuente. Corrige el texto de `CONFIG` (acórtalo o repártelo en más líneas),
nunca "arregles" el error aflojando el límite en el motor de render ni
comentando el `assert`.

### 3.2 Paleta y tipografía (fijo)

| Elemento | Valor |
|---|---|
| Fondo | `#0C0C0C` (negro casi puro) + rejilla sutil `#222222` |
| Texto principal | `#F4EEE3` (crema) |
| Resaltados / acentos / marca | `#FF5A1F` (mismo naranja corporativo de siempre) |
| Texto sobre naranja o crema | `#111111` (negro) |
| Texto secundario (kicker, pie, subtítulos de CTA) | `#969691` (gris) |

Fuentes de siempre (`assets/fonts/`, licencia OFL, NO Arial/Windows):
**ArchivoBlack** para todos los títulos/titulares/etiquetas grandes,
**Barlow-Bold** para cuerpo de texto, bullets y letra pequeña. Igual que en
el resto del proyecto, **estas fuentes no incluyen emoji** — nunca escribas
💬🔖🔁 etc. dentro de `CONFIG`, sale como un cuadrado roto. Si hace falta un
icono, se dibuja a mano con formas (ver `arrow_bullets()`, `ring_checks()`,
los círculos numerados de `render_closing()` en el propio script como
ejemplo) — nunca un carácter emoji ni un glifo Unicode raro.

### 3.3 Elementos fijos en todas las slides

- **Header**: logo (recoloreado a crema automáticamente por
  `_recolored_logo()`) arriba a la izquierda + foto de Jorge en círculo
  naranja arriba a la derecha. Mismo sitio en las N slides, incluida la de
  cierre.
- **Kicker**: etiqueta pequeña en gris debajo del logo — el tema/ángulo del
  día en mayúsculas (p.ej. "ROAST SEO · ECOMMERCE", "MITO SEO ·
  ECOMMERCE"). Una sola cadena en `CONFIG["kicker"]`, igual en todas las
  slides.
- **Nota de pie del PDF gated** (`footer_gate_note`): en TODAS las slides de
  contenido (no en la portada ni en el cierre), en la esquina inferior
  izquierda — el recordatorio discreto de que la solución completa vive en
  el PDF gated, nunca en el carrusel (regla no negociable, sección 3bis).
  Texto por defecto ya integrado en el motor (`DESCARGA LA GUÍA PDF EN
  COMENTARIOS`, vigente desde el 25/08/2026 a petición expresa de Jorge —
  antes era "el arreglo completo, paso a paso -> guía gratis en
  comentarios"), no hace falta tocarlo cada día salvo que quieras un texto
  distinto vía `CONFIG["footer_note"]`.
- **Indicador de "desliza"** (`scroll_hint`): barra degradada + flecha
  circular abajo a la derecha, en todas las slides excepto la de cierre; en
  la última slide de contenido (justo antes del cierre) la flecha cambia a
  un check. **Nunca coloques texto propio en la zona aproximada x>930,
  y>680 de la mitad inferior de una slide** — es donde vive este elemento y
  taparlo con texto es exactamente el bug que se corrigió al validar este
  formato con Jorge.

### 3.4 Tipos de slide disponibles en `CONFIG["slides"]`

Cada slide es un diccionario con un campo `"type"`. Los cinco tipos
disponibles, con sus límites (impuestos por `assert` en el propio script —
si los superas, el script para en seco con el motivo exacto):

- **`cover`** (obligatorio, siempre la primera slide): `title_lines` (lista
  de líneas; cada línea es una lista de `(texto, es_resaltado)` — así se
  puede resaltar solo parte de una línea, como en el ejemplo de abajo) y
  `subtitle` (1-2 frases). Máximo **5 líneas** de título.
- **`statement`**: una "declaración" grande — `title_lines` (máximo **4
  líneas**), y opcionalmente `body` (1 párrafo corto) y/o `closing` (una
  única línea resaltada, tipo remate). Cubre tanto un gancho de una sola
  frase como una slide de contexto/transición con cuerpo.
- **`bullets`**: `title_lines` (máximo 3 líneas) + `intro` (opcional) +
  `items` (lista de **2 a 4** frases cortas, con flecha dibujada a mano) +
  `closing` (opcional, en gris). Para el "por qué importa esto".
- **`card`**: el bloque que más se repite — un hallazgo/paso/dato por slide.
  `label` (p.ej. "SEÑAL 1", "ERROR", "MITO", "DATO 1" — lo que tenga sentido
  para el ángulo del día), `headline` (el titular resaltado; se envuelve
  automáticamente en varias líneas si hace falta, no lo partas tú a mano),
  `body` (opcional, 1-2 líneas de contexto) y `checks` (opcional, máximo
  **2** preguntas de autocomprobación con un anillo delante).
- **`closing`** (obligatorio, siempre la última slide): `title_lines`
  (**exactamente 2** líneas), `ctas` (lista de hasta **3** tuplas
  `(título, subtítulo)` — normalmente comentar / guardar / compartir),
  `box_title` y `box_link` — el bloque naranja final, el ÚNICO sitio del
  carrusel con el CTA fuerte y el enlace real al PDF gated.

El ejemplo que queda en `CONFIG` tras cada `git checkout` (5 señales de
indexación silenciosa) es la plantilla de referencia validada visualmente
con Jorge el 24/08/2026 — para un día nuevo, parte de esa misma estructura
de tipos y sustituye los textos, no la reinventes desde cero.

### 3.5 Estructura recomendada por día

Orden típico (10 slides, el mismo conteo que la plantilla de referencia):
`cover` (1) → `statement` (1-2, gancho y/o contexto) → `bullets` (0-1, por
qué importa) → `card` × 3-6 (un hallazgo/paso/dato por slide) → `closing`
(1). Adapta el contenido de las `card` al ángulo del día sin cambiar la
mecánica:

- **Lunes (roast)**: cada `card` es un síntoma/señal del error real
  auditado (anonimizado), como en la plantilla.
- **Martes (mito)**: cada `card` puede ser "lo que se cree" vs "lo que
  dicen los datos" — usa `label` tipo "MITO" / "REALIDAD".
- **Miércoles (auditoría exprés)**: cada `card` es un hallazgo concreto de
  la marca pública auditada.
- **Jueves (tendencia/algoritmo)**: cada `card` es una implicación práctica
  del cambio para un ecommerce.
- **Viernes (pregunta abierta)**: la `statement` inicial plantea la
  pregunta con fuerza, la siguiente `statement` o `card` da la respuesta de
  Jorge (sigue las reglas de la sección 1, nota de viernes), y el `closing`
  reitera la pregunta e invita a comentar en vez de (o además de) los 3 CTAs
  estándar.

### 3.6 Regla no negociable (recordatorio — ver sección 3bis completa)

El carrusel enseña el diagnóstico (qué revisar, qué pasa, por qué importa),
**nunca la solución paso a paso completa** — eso vive solo en el PDF gated.
Por eso `footer_gate_note` aparece en cada slide de contenido y el `closing`
lleva el único CTA fuerte con el enlace real.

## 3bis. PDF del día (lead magnet) — UNO DISTINTO CADA DÍA, nunca repetido

**Importante**: Jorge no quiere que se repita el mismo PDF semana tras
semana. Cada día se genera un PDF nuevo, centrado en el tema exacto del post
de ese día (no una checklist genérica de 12 puntos salvo que el ángulo del
día lo justifique).

**Desde el 24/08/2026 usa el mismo lenguaje visual que el carrusel** (sección
3): fondo negro con rejilla sutil, ArchivoBlack + resaltado naranja tipo
"subrayador" en los titulares, Barlow-Bold en cuerpo/etiquetas, foto+logo
arriba en toda página. Antes tenía su propio estilo (portada con degradado
naranja + tarjetas claras) — se unificó para que el PDF gated y el carrusel
se sientan como el mismo documento, no como dos marcas distintas.

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
- **Resaltado naranja opcional**: en `COVER_TITLE_HTML`, `CTA_TITLE` o el
  `título` de cualquier punto, envuelve la frase clave entre `<hl>...</hl>`
  para que salga con la caja naranja de fondo (mismo efecto que
  `draw_mixed_line()` en el carrusel) — p.ej.
  `"<hl>Categorías fantasma:</hl><br/>qué hacer con..."`. Es opcional: sin
  `<hl>`, el texto sale igual, solo que sin resaltar. No abuses de esto —
  como en el carrusel, resalta una frase corta y contundente, no párrafos
  enteros.

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

**Ojo con las fuentes — misma limitación que el carrusel (sección 3.2)**:
desde que este PDF usa ArchivoBlack/Barlow-Bold en vez de las fuentes
estándar de reportlab, **ya no soporta emoji ni la flecha `→` (U+2192)** —
sale como hueco en blanco. Usa `->` en su lugar, nunca emoji, en
`COVER_TITLE_HTML`, `COVER_SUBTITLE`, `STAT_LABEL`, `POINTS`, `CTA_TITLE`
ni `CTA_BODY`. Los acentos y la `ñ` sí funcionan bien (ambas fuentes los
incluyen).

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
- `carrusel-1.png` ... `carrusel-N.png` (una por slide del carrusel, ver sección 3)
- `carrusel-post.pdf` (el mismo carrusel empaquetado en PDF — es lo que se sube a LinkedIn como Documento)
- `articulo-blog.html`
- `<slug-del-título>.pdf` (el lead magnet gated, nuevo cada día, nombre descriptivo — ver sección 3bis)
- Fila nueva añadida a `TEMAS_TRATADOS.md` (raíz del repo — ver sección 1bis)

**Orden importante**: genera y haz commit+push del PDF del lead magnet (y de
toda la carpeta) ANTES de dar el artículo por terminado, porque el HTML del
artículo depende de la URL pública de ese PDF ya subido (sección 3bis).

Al terminar, enviar los archivos a Jorge (vía SendUserFile) con una nota
breve indicando qué toca hacer: 1) copiar el post y subir `carrusel-post.pdf`
a LinkedIn como publicación de tipo Documento (no como carrusel de imágenes
sueltas — ver sección 3), 2) revisar el borrador ya creado en WordPress (ver
sección 9) y darle a Publicar. Recordar que todo lo demás (leads, envío del
PDF gated, y desde que hay credenciales de WordPress configuradas — ver
sección 9 — la subida del borrador) es 100% automático y no requiere ninguna
acción suya salvo el clic final de Publicar.

**Nunca publicar nada automáticamente en el sentido de "dejarlo en vivo"**
(ni en LinkedIn, ni en WordPress, ni en Klaviyo) — desde que hay credenciales
de WordPress disponibles, el artículo SÍ se sube solo a WordPress, pero
siempre como BORRADOR (`status: draft`), nunca publicado directamente; la
rutina nunca pulsa "Publicar" por Jorge, eso es siempre su clic final.

## 7. Entorno de ejecución (nube)

- Instala dependencias con `pip install -r requirements.txt` si `Pillow` no
  está ya disponible.
- Intenta entregar todos los archivos generados directamente al usuario
  (herramienta de envío de archivos si está disponible en la sesión).
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
