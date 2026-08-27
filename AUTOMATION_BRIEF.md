# Brief de automatización diaria — Jorge Segovia (SEO para Ecommerce)

Este documento es la única fuente de verdad que necesita la ejecución programada
de cada mañana (L-V, 8:00 Europe/Madrid). Contiene todo lo acordado con Jorge:
marca, formato, estructura y qué entregar.

**Cambio de método vigente desde el 28/08/2026** (ver nota de migración al
final del documento): la rutina en la nube **ya no genera ninguna imagen**
(ni carrusel ni imagen única) **ni el artículo de blog en HTML**, y **ya no
sube ningún borrador a WordPress**. Jorge diseña la imagen él mismo con su
propia herramienta de diseño, a partir de un breve documento de ideas que sí
genera la rutina. La entrega diaria de esta rutina se reduce a: el recurso
descargable del día (normalmente un PDF, ver sección 4) + el texto del post
de LinkedIn + el documento de ideas para la imagen. Nada se deja publicado en
vivo automáticamente — subir la imagen y el post a LinkedIn, y responder a
quien comente, siguen siendo 100% de Jorge.

## 0. Contexto del negocio

Jorge Segovia, consultor SEO especializado en ecommerce (WordPress y Shopify),
foco actual en moda pero abierto a cualquier sector ecommerce. Servicio en 2 fases:
Fase 1 (auditoría SEO de +100 páginas: keyword research, arquitectura SEO
transaccional, ranking actual, anexos) y Fase 2 (implementación).

**ICP (perfil de cliente ideal) de los leads que capta este contenido**:
propietarios de ecommerce y responsables de marketing de tiendas online o
páginas web — perfiles ocupados, no necesariamente técnicos, que valoran algo
accionable y rápido de aplicar por encima de la teoría. Ten esto en mente al
elegir qué tipo de recurso encaja mejor con el tema del día (sección 4): un
propietario de ecommerce agradece más una plantilla o checklist que puede
usar él mismo en 10 minutos que un informe largo de lectura.

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
  del recurso descargable).
- Cierre: reitera la pregunta e invita explícitamente a responder en
  comentarios.
- Sigue llevando recurso descargable del día (sección 4) y documento de
  ideas para la imagen (sección 3) con normalidad — el ángulo "pregunta
  abierta" no exime de ninguna de las entregas obligatorias de la sección 5.

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

0. **Titular de apertura** (obligatorio): la primera línea del post — sola,
   en su propio párrafo, antes del hook — es un titular corto y contundente.
   Es el mismo titular que le des al recurso descargable del día (mismo
   título, ver sección 4) y el mismo que sugieras como elemento central en el
   documento de ideas para la imagen (sección 3) — texto, recurso e imagen
   deben "decir lo mismo" a primer golpe de vista. Normalmente en mayúsculas
   y cerrado en punto, como frase autoconclusiva — p.ej. "FICHA DE PRODUCTO:
   GOOGLE YA NO TE VE."
1. **Hook** (1-2 líneas, dato/situación sorprendente)
2. **Contexto** (tipo de tienda/situación, siempre anonimizado si es un caso real)
3. **El desarrollo** (el roast / mito / hallazgo, con tono ligero pero riguroso)
4. **Por qué importa / qué está en juego** — deja claro el coste de no arreglarlo,
   pero SIN dar los pasos de la solución (ver regla de la sección 4 —
   la solución completa vive solo en el recurso descargable, el post nunca
   debe regalarla)
5. **Prueba** (cifra de mejora, cuando aplique — nunca inventada, ver regla
   de tono más abajo)
6. **CTA de comentario** (método vigente desde el 28/08/2026 — sustituye al
   antiguo "enlace en comentario fijado"): invita a comentar una palabra
   clave concreta relacionada con el tema del día, dejando claro que Jorge
   responde por privado con el enlace. Patrón de texto a usar (adapta la
   palabra entre comillas al tema de cada día, mantenla en mayúsculas):
   `Comenta "<PALABRA>" y te escribo por privado con el enlace.` — nunca
   pongas el enlace directamente en el post ni prometas que "te lo dejo en
   comentarios" (eso era el método antiguo); el envío es manual, por Jorge,
   vía DM. La palabra clave debe coincidir con la que sugieras en el
   documento de ideas para la imagen (sección 3), para que quien vea la
   imagen sepa exactamente qué comentar.

Tono: cercano, con personalidad, nunca acartonado. Nunca inventar cifras — si no
hay un dato real verificable, no se afirma un resultado concreto.

**Longitud**: apunta a 150-200 palabras en total, no a 230+. Mismo esqueleto de
6-7 puntos, pero compacto — si un párrafo puede decir lo mismo en menos
frases, recorta antes de añadir matices extra.

## 3. Documento de ideas para la imagen (Jorge la diseña, la rutina ya no genera nada)

**Cambio vigente desde el 28/08/2026**: hasta el 27/08/2026 esta rutina
generaba ella misma la imagen del post (primero un "stat hero" de imagen
única, después un carrusel-documento de varias slides estilo Twinkle
Chatterjee/ThriveCraft SEO). Jorge ha hecho su propio diseño y quiere
encargarse él mismo de maquetar la imagen — así que **la rutina ya no
genera ningún PNG ni PDF de carrusel**. En su lugar, entrega un documento de
texto corto con ideas de qué incorporar, para que Jorge lo use como brief al
diseñar.

Los scripts antiguos (`scripts/generate_carousel_post.py`,
`scripts/generate_post_image.py` y el borrador
`scripts/generate_single_post_image_DRAFT.py`) se quedan en el repo tal cual,
sin usarse en el flujo diario — solo por si Jorge pide explícitamente
recuperar la generación automática de imagen en el futuro. No los toques ni
los borres salvo que te lo pida.

### Qué generar: `brief-imagen.md`

Un archivo Markdown corto (nunca un PNG, nunca un PDF) dentro de la carpeta
del día, con esta estructura fija:

```markdown
# Brief de imagen — <fecha> (<ángulo del día>)

**Titular / título del recurso:** <mismo titular que el punto 0 de la
sección 2 y que la portada del recurso de la sección 4>

**Palabra clave del CTA:** "<PALABRA>" (debe coincidir con el CTA del post,
sección 2 punto 6)

**Qué mostrar:**
- <elemento visual 1 — p.ej. "el fragmento real de robots.txt bloqueando
  GPTBot, en formato código">
- <elemento visual 2 — p.ej. "logos reales de las 4 herramientas
  mencionadas: Search Console, Screaming Frog, WordPress, Yoast">
- <elemento visual 3, si aplica>

**Tono/nota adicional:** <cualquier matiz relevante — p.ej. "es el ángulo
roast, mantén el tono ligeramente irónico del post">
```

3-5 bullets en "Qué mostrar" es suficiente — el objetivo es dar ideas
concretas y accionables (qué elementos, qué dato, qué herramienta
mencionar), no maquetar el diseño ni describir colores/tipografías (eso ya
lo tiene resuelto Jorge en su propia plantilla). Si el tema del día tiene un
elemento visual obvio (un fragmento de código, un logo de herramienta real,
una captura que Jorge podría aportar), dilo explícitamente — es la parte más
útil del brief.

## 4. Recurso del día (lead magnet) — UNO DISTINTO CADA DÍA, nunca repetido

**Importante**: Jorge no quiere que se repita el mismo recurso semana tras
semana. Cada día se genera un recurso nuevo, centrado en el tema exacto del
post de ese día.

**Novedad vigente desde el 28/08/2026 — variedad de formato**: antes el
recurso era siempre un PDF tipo guía/checklist. Ahora el objetivo es variar
el *tipo* de recurso según lo que mejor encaje con el tema del día y con el
ICP (sección 0: propietarios y responsables de marketing de ecommerce, gente
ocupada que valora algo accionable). Catálogo de tipos de recurso:

| Tipo | Cuándo encaja | Estado del generador |
|---|---|---|
| **Guía / checklist en PDF** | El tema tiene 1-varios puntos con diagnóstico + solución (roast, mito, tendencia) — es el formato por defecto | Listo: `scripts/generate_lead_magnet_pdf.py` |
| **Plantilla de autoevaluación (worksheet) en PDF** | El lector puede aplicarlo él mismo sobre su propia tienda mientras lo lee (espacios/casillas para rellenar) | Pendiente de construir — usar la guía PDF como base mientras tanto |
| **Banco de plantillas de texto (swipe file) en PDF** | El tema da pie a fragmentos listos para copiar (ej. reglas de robots.txt, plantillas de meta title, prompts de auditoría) | Pendiente de construir — usar la guía PDF como base mientras tanto |
| **Hoja de cálculo descargable (.xlsx)** | El tema encaja mejor como tracker/calculadora (ej. impacto de URLs duplicadas, checklist con columnas de estado) | Pendiente de construir — usar la guía PDF como base mientras tanto |
| **One-pager / cheat sheet en PDF** | Versión ultra condensada de una sola página, para temas que se resumen en pocos puntos | Pendiente de construir — usar la guía PDF como base mientras tanto |

Mientras los generadores nuevos no existan, **usa siempre
`scripts/generate_lead_magnet_pdf.py`** (el único listo) — no fuerces un
formato que no puedes generar todavía. Cuando Jorge pida construir alguno de
los tipos pendientes, créalo como script nuevo en `scripts/` siguiendo el
mismo patrón (CONFIG editable al principio, salida por CLI, revertir con
`git checkout` al terminar) y actualiza esta tabla marcándolo como listo.

*(Fuentes consultadas sobre qué formatos de lead magnet funcionan mejor para
este tipo de ICP en B2B/ecommerce en 2026: audits y checklists siguen entre
los que más convierten por ser accionables y específicos; plantillas y
swipe files funcionan bien porque ahorran tiempo directo; los formatos
interactivos (calculadoras, quizzes) convierten aún mejor pero requieren una
herramienta web que este repo no genera, así que no forman parte del
catálogo por ahora — ver
[Vida AI Agent OS](https://vida.io/blog/best-b2b-lead-magnets),
[Luniq](https://www.luniq.io/en/hub/articles/best-b2b-lead-magnet-formats-for-2026),
[ActiveCampaign](https://www.activecampaign.com/blog/lead-magnet-ideas-and-examples).)*

### Cómo generar el PDF guía/checklist (formato por defecto)

Usar `scripts/generate_lead_magnet_pdf.py` como base. Edita las variables al
principio del archivo (sección CONFIG) según el tema de hoy:

- `COVER_TITLE_HTML`: título de portada (con `<br/>` para saltos de línea),
  específico del tema del día — es el mismo titular que uses en el punto 0
  de la sección 2 y en el documento de ideas de la sección 3.
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
  para que salga con la caja naranja de fondo — p.ej.
  `"<hl>Categorías fantasma:</hl><br/>qué hacer con..."`. Es opcional: sin
  `<hl>`, el texto sale igual, solo que sin resaltar. No abuses de esto —
  resalta una frase corta y contundente, no párrafos enteros.

Ejecuta pasando la ruta de salida como argumento. **El nombre del archivo
debe ser un slug del título del recurso (nunca el genérico "lead-magnet.pdf"
ni "recurso.pdf")**, porque es literalmente el nombre que le queda guardado
al usuario cuando lo descarga:

```
python3 scripts/generate_lead_magnet_pdf.py content/<carpeta-del-día>/<slug-del-titulo>.pdf
```

Ejemplo: si `COVER_TITLE_HTML` es "Duplicado no es<br/>penalización<br/>(es
otra cosa)", el slug sería `duplicado-no-es-penalizacion.pdf` (minúsculas,
sin acentos ni signos, espacios → guiones, sin la parte entre paréntesis si
la hay).

**Ojo con las fuentes**: este PDF usa ArchivoBlack/Barlow-Bold en vez de las
fuentes estándar de reportlab, así que **no soporta emoji ni la flecha `→`
(U+2192)** — sale como hueco en blanco. Usa `->` en su lugar, nunca emoji, en
`COVER_TITLE_HTML`, `COVER_SUBTITLE`, `STAT_LABEL`, `POINTS`, `CTA_TITLE` ni
`CTA_BODY`. Los acentos y la `ñ` sí funcionan bien (ambas fuentes los
incluyen).

Después de generar y validar el resultado, **valida la sintaxis y revierte
el script a su versión original** con `git checkout --
scripts/generate_lead_magnet_pdf.py` antes de terminar (para que el próximo
día vuelva a partir de la plantilla de referencia, no del contenido de hoy).

### 🚫 Regla crítica: el post y el brief de imagen NUNCA dan la solución completa

El post de LinkedIn (y el documento de ideas para la imagen) están para
enganchar y generar la necesidad de pedir el recurso — **no para resolver el
problema por sí solos**. Si el lector se va con la solución completa sin
comentar y pedir el recurso, se rompe todo el embudo de captación de leads.

Lo que SÍ puede llevar el post (esto genera confianza y demuestra que Jorge
sabe de lo que habla, sin regalar la solución):
- El problema explicado con claridad: qué es, por qué ocurre, por qué
  importa/cuesta dinero.
- Cómo detectarlo/diagnosticarlo (esto es diagnóstico, no arreglo —
  compartirlo está bien, de hecho genera más ganas de saber cómo arreglarlo).
- El contexto o caso (anonimizado) que da pie al post.

Lo que el post NUNCA debe incluir: los pasos concretos de la
solución/arreglo (nada de listas tipo "así lo arreglas: 1... 2... 3..."), ni
nada que, si el lector lo copia, resuelva el problema sin necesitar el
recurso. La solución paso a paso vive ÚNICAMENTE dentro del recurso
descargable del día.

### Cómo se aloja el recurso (automático, sin que Jorge suba nada)

Jorge no tiene forma de recibir un recurso nuevo cada día y subirlo él mismo
sin que deje de ser "automático" — así que se aloja usando el propio
repositorio de GitHub, que ya es público. En cuanto hagas commit y push
(sección 5), el recurso queda disponible en:

```
https://raw.githubusercontent.com/jscautomation/jorge-linkedin-seo-daily/main/content/<carpeta-del-día>/<slug-del-titulo>.<ext>
```

Jorge usa esa URL él mismo al configurar el redireccionamiento de su
formulario de captura (fuera del alcance de esta rutina, ver nota en la
sección 5) — asegúrate de que el commit+push del recurso ocurra cuanto antes
en la entrega del día para que la URL esté viva quien la necesite.

## 5. Entrega diaria — output

Carpeta: `content/YYYY-MM-DD-<día-en-español>-<formato>/` con:
- `post-linkedin.txt`
- `<slug-del-recurso>.<ext>` (el recurso del día, nuevo cada día, nombre
  descriptivo — ver sección 4)
- `brief-imagen.md` (documento de ideas para que Jorge diseñe la imagen —
  ver sección 3)
- Fila nueva añadida a `TEMAS_TRATADOS.md` (raíz del repo — ver sección 1bis)

Haz commit y push de toda la carpeta (mismo remoto del que se clonó) tan
pronto como esté lista, como red de seguridad además de la entrega directa.
Usa un mensaje de commit tipo `Contenido diario: <fecha> (<ángulo del día>)`.

Al terminar, enviar los archivos a Jorge (vía `SendUserFile`) con una nota
breve indicando qué toca hacer: 1) diseñar la imagen con su propia
herramienta usando `brief-imagen.md` como guía, 2) copiar el post y subir
la imagen a LinkedIn, 3) cuando alguien comente la palabra clave del CTA,
escribirle por privado con el enlace a su formulario de captura (el recurso
ya está alojado y listo, con URL pública verificada). Recordar que la
sincronización de segmentos de Klaviyo (sección 7, si sigue aplicando a su
formulario actual) sigue siendo un paso aparte en sesión local.

**Nunca publicar nada en vivo automáticamente** — el post de LinkedIn, la
imagen y cualquier respuesta a comentarios son siempre acción manual de
Jorge; esta rutina solo entrega archivos y hace commit/push al repositorio.

## 6. Entorno de ejecución (nube)

- Instala dependencias con `pip install -r requirements.txt` si `Pillow` no
  está ya disponible (sigue haciendo falta para generar el PDF del recurso).
- Intenta entregar todos los archivos generados directamente al usuario
  (herramienta de envío de archivos si está disponible en la sesión).
- **Además, y siempre**, haz commit y push de la carpeta `content/<día>/`
  generada al repositorio, como red de seguridad por si la entrega directa
  fallara.

## 7. Segmento de Klaviyo por recurso (esto NO lo hace la rutina en la nube)

Si el formulario de captura que use Jorge (fuera del alcance de esta rutina,
ver sección 5) sigue registrando en Klaviyo un evento con la propiedad
`pdf_titulo` (o equivalente) por cada descarga, esta sección sigue
aplicando: un segmento en Klaviyo es dinámico — una vez existe, se actualiza
solo con cada nueva descarga, pero el segmento en sí hay que crearlo una vez
por título.

Herramienta recomendada: `scripts/sync_klaviyo_segments.py` — revisa TODO
el historial de descargas, saca los títulos distintos, y crea el segmento
que falte para cada uno (sin duplicar los que ya existen). Ejecutar sin
argumentos; es seguro correrlo tantas veces como se quiera (idempotente).
Alternativa puntual para un solo título nuevo:
`scripts/create_klaviyo_segment.py "Título exacto del recurso"`.

**A propósito, la rutina en la nube NO ejecuta este script ni tiene la
`KLAVIYO_API_KEY`** — esa clave da acceso de escritura a toda la cuenta de
Klaviyo y no hay forma segura de dársela al entorno en la nube (la
definición de la rutina no soporta secretos, solo prompt de texto plano).
Este paso queda pendiente de ejecutarse en una sesión local.

Si Jorge cambia de herramienta de formulario y ya no pasa por Klaviyo con
ese mismo evento, avisa para actualizar o retirar esta sección.

---

## Nota de migración (28/08/2026)

Este brief se reescribió a fondo el 28/08/2026 a petición expresa de Jorge.
Resumen de lo que cambió respecto a la versión anterior (24-27/08/2026, el
formato "documento negro con resaltados naranja" estilo Twinkle
Chatterjee/ThriveCraft SEO), por si hace falta recuperar contexto:

- **La rutina ya no genera ninguna imagen.** Antes generaba un carrusel de
  8-11 slides + PDF empaquetado (`scripts/generate_carousel_post.py`); antes
  de eso, una imagen única tipo "stat hero" (`scripts/generate_post_image.py`).
  Jorge diseña ahora la imagen él mismo con su propia plantilla. La rutina
  entrega en su lugar un documento de ideas (`brief-imagen.md`, sección 3).
  Los scripts antiguos se quedan en el repo sin usarse — no borrarlos salvo
  instrucción expresa.
- **Ya no se genera el artículo de blog en HTML** (antes `articulo-blog.html`,
  con plantilla de referencia en `content/2026-08-17-lunes-roast/`) ni se
  sube ningún borrador a WordPress (antes `scripts/publish_to_wordpress.py`,
  sección "9. Borrador en WordPress" del brief anterior). Las variables de
  entorno `WP_URL`/`WP_USERNAME`/`WP_APP_PASSWORD` pueden seguir configuradas
  en el entorno pero esta rutina ya no las usa.
- **Cambia el mecanismo de entrega del lead**: antes, quien comentaba la
  palabra clave encontraba el enlace en un comentario fijado automático que
  llevaba al formulario embebido en el artículo. Ahora, quien comenta recibe
  un DM manual de Jorge con el enlace a su formulario — por eso ya no hace
  falta ni el artículo ni el formulario embebido para este flujo (aunque
  `templates/formulario-lead-magnet.html` se queda en el repo, ya no forma
  parte del proceso diario salvo que Jorge decida reutilizarlo en su nueva
  herramienta).
- **El recurso descargable ya no es siempre un PDF checklist** — ver el
  catálogo de tipos de recurso en la sección 4. De momento solo hay
  generador construido para el formato guía/checklist; los demás se
  construirán bajo demanda.
