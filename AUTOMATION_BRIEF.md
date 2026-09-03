# Brief de automatización diaria — Jorge Segovia (SEO para Ecommerce)

Este documento es la única fuente de verdad que necesita la ejecución programada
de cada día (7 días/semana, 8:00 Europe/Madrid). Contiene todo lo acordado con
Jorge: marca, formato, estructura y qué entregar.

**Reescritura a fondo vigente desde el 03/09/2026** (ver notas de migración al
final del documento): desaparece la rotación de ángulos por día de la semana,
se publica los 7 días, vuelve el formato carrusel (ahora en paleta crema) como
publicación principal, y el recurso descargable diario desaparece — se
sustituye por un extracto que la propia rutina añade cada día, vía el
conector MCP de Notion, a una única guía viva en Notion, a la que se llega
por Mailchimp.

## 0. Contexto del negocio

Jorge Segovia, consultor SEO especializado en ecommerce (WordPress y Shopify),
foco actual en moda pero abierto a cualquier sector ecommerce. Servicio en 2 fases:
Fase 1 (auditoría SEO de +100 páginas: keyword research, arquitectura SEO
transaccional, ranking actual, anexos) y Fase 2 (implementación).

**Público objetivo**: el contenido diario busca generar **engagement y
visibilidad del perfil de Jorge ante CEOs y propietarios de empresa de
cualquier industria**, con foco especial en quienes dirigen un ecommerce en
WordPress o Shopify (su ICP prioritario, pero no el único). Jorge interactúa
él mismo, manualmente, con perfiles de este tipo (comentarios, likes,
mensajes) para construir relación — esta rutina nunca comenta ni interactúa
en perfiles ajenos; lo único que hace es producir lo que esos perfiles ven
cuando entran en el suyo.

**El contenido sigue siendo SEO técnico para ecommerce**, pero cada pieza
tiene que abrirse y sostenerse en términos que le importan a quien dirige un
negocio — coste real (ingresos, margen, cuota de mercado frente a la
competencia), riesgo (qué pasa si no se arregla) y ventaja competitiva —
antes que en jerga técnica por sí misma. El detalle técnico se mantiene (da
autoridad) pero siempre subordinado a la consecuencia de negocio: nunca
como apertura ni como único argumento.

**La guía de Notion (destino final del embudo, ver sección 4)** también es
de ecommerce/marketing de tiendas online — gente ocupada que valora algo
accionable y rápido de aplicar por encima de la teoría.

Web: jorgesegoviaciscar.com · Email: jorge@jscautomation.es

## 1. Elegir la mejora SEO del día (ya no hay rotación por día de la semana)

**Se elimina la tabla de ángulos por día de la semana (Lunes-roast,
Martes-mito, etc.) vigente hasta el 03/09/2026** — ver nota de migración.
A partir de ahora hay un único criterio, todos los días:

- Es **una mejora SEO concreta y accionable** para ecommerce (del tipo que ya
  se venía tratando: errores reales de auditoría, mitos, hallazgos,
  tendencias), siempre aterrizada en "esto es lo que puedes implementar" —
  pensada para que un propietario de ecommerce la entienda y la aplique de
  principio a fin (diagnóstico → por qué importa → qué se hace).
- Se plantea en términos de negocio (coste, riesgo, ventaja competitiva)
  antes que jerga técnica — este enfoque, antes limitado a la nota "1ter",
  ahora aplica siempre, sin distinción por día.
- **No repetida**: antes de elegir, lee `TEMAS_TRATADOS.md` (raíz del repo,
  ahora una lista única cronológica) y no repitas el mismo fondo del
  hallazgo aunque cambie la marca, el título o la redacción.
- Si no hay tema libre razonable, no repitas — genera el resto del contenido
  con normalidad pero avisa explícitamente a Jorge en la entrega de que hace
  falta que pase un tema nuevo.

**Registro obligatorio**: al terminar de generar todo el contenido del día,
añade una fila nueva al final de la tabla de `TEMAS_TRATADOS.md` (fecha,
mejora SEO, nota breve de la solución) y haz commit+push de ese archivo junto
con la carpeta `content/<día>/` (mismo commit o el siguiente, pero siempre el
mismo día). Nunca lo dejes para "el próximo día".

## 2. Esqueleto del post de LinkedIn (siempre igual, cambia el contenido)

0. **Titular de apertura** (obligatorio): primera línea del post, sola, en
   su propio párrafo — corto y contundente, en términos de negocio (coste,
   riesgo, ventaja competitiva) siempre que el tema lo permita. Mismo
   titular que la portada del carrusel (sección 3) y el título de la
   entrada que se añade a la guía de Notion (sección 4) — post, carrusel y
   guía deben "decir lo mismo" a primer golpe de vista.
1. **Hook** (1-2 líneas, dato/situación sorprendente) — dirigido a quien toma
   la decisión de negocio, no solo a quien lo implementaría técnicamente.
2. **Contexto** (tipo de tienda/situación, siempre anonimizado si es un caso real)
3. **El desarrollo** (el roast / mito / hallazgo, con tono ligero pero riguroso)
4. **Por qué importa / qué está en juego** — coste de no arreglarlo en
   términos de negocio, SIN dar los pasos de la solución (regla de la
   sección 4 — la solución completa vive solo en la guía de Notion).
5. **Prueba** (cifra de mejora, cuando aplique — nunca inventada)
6. **CTA de comentario**: invita a comentar una palabra clave concreta
   relacionada con el tema del día, dejando claro que Jorge responde por
   privado. Patrón de texto (adapta la palabra entre comillas al tema de
   cada día, mantenla en mayúsculas):
   `Comenta "<PALABRA>" y te lo envío.` — nunca pongas el enlace directamente
   en el post; el envío es manual, por Jorge, vía DM, con la URL de
   Mailchimp (la persona deja su correo y es redirigida a la landing de
   Notion con la guía completa — ver sección 4). La palabra clave debe
   coincidir con la que uses en el recuadro naranja de todas las slides del
   carrusel (sección 3).

Tono: cercano, con personalidad, nunca acartonado. Nunca inventar cifras. El
lector prioritario es un CEO o propietario de empresa. El rigor técnico no se
pierde, pero nunca es el argumento de apertura.

**Longitud**: 150-200 palabras en total. Mismo esqueleto de 6-7 puntos, pero
compacto — si un párrafo puede decir lo mismo en menos frases, recorta antes
de añadir matices extra.

Guarda como `post-linkedin.txt`.

## 3. El carrusel (formato principal, paleta crema desde el 03/09/2026)

**Vuelve a ser un carrusel** (sustituye a la imagen única que estuvo vigente
del 28/08 al 02/09/2026 — ver nota de migración). Usa
`scripts/generate_carousel_post.py`, el mismo motor "documento" que ya
existía en el repo (estuvo desactivado, ahora vuelve a ser el generador
oficial), con un cambio de paleta.

### 3.1 El motor es fijo, el contenido se edita cada día

Igual que con el resto de scripts del repo: el motor de render (todo lo de
arriba de `CONTENIDO DE HOY`) es fijo — no tocar salvo instrucción expresa de
Jorge. El diccionario `CONFIG` al final sí se edita cada día. Edita `CONFIG`,
ejecuta el script, mueve el resultado a `content/<carpeta-del-día>/`, y
revierte el archivo con `git checkout -- scripts/generate_carousel_post.py`
antes de terminar.

```
python3 scripts/generate_carousel_post.py content/<carpeta-del-día>
```

Salida: `carrusel-1.png` … `carrusel-N.png` (una por slide) + `carrusel-post.pdf`
(empaquetado sin pérdida vía `img2pdf`). **Sube el PDF a LinkedIn como
publicación de tipo Documento** (LinkedIn lo renderiza como visor
deslizable) — los PNG son solo para revisar/editar cada slide a mano.

### 3.2 Paleta (fijo — cambiada el 03/09/2026, fondo crema en vez de negro)

| Elemento | Valor |
|---|---|
| Fondo (`BG`) | `#FFFCF4` (crema) |
| Texto principal (`CREAM`, nombre heredado del formato antiguo) | `#111111` (negro) |
| Rejilla decorativa (`GRID`) | `#E6E0D2` (gris claro sobre crema) |
| Resaltados / acentos (`ORANGE`) | `#FF5A1F` (naranja de marca) |
| Texto sobre cajas naranjas/crema (`INK`) | `#111111` |
| Texto secundario / kicker (`GRAY`) | `#78766E` |

Fuentes: ArchivoBlack (titulares) y Barlow-Bold (cuerpo/CTA), igual que
siempre — sin cambios respecto al formato anterior.

### 3.3 Estructura de slides

Tipos disponibles: `cover`, `statement`, `bullets`, `card`, `closing`.
Estructura recomendada: 1 `cover` + 1-2 `statement` + 1 `bullets` (por qué
importa) + 3-5 `card` (una señal/paso de diagnóstico por slide, con 1-2
preguntas de autochequeo) + 1 `closing`.

**Recuadro de la guía encima del título de portada (vigente desde el
03/09/2026, a petición expresa de Jorge — sustituye a un primer intento
el mismo día de meter el número en el `kicker` + una frase suelta en el
`subtitle`, que no se veía suficientemente destacado)**: la slide `cover`
lleva, ENCIMA del título (entre el kicker y el título grande, con más
separación respecto al logo/avatar que en el primer ajuste — ver
`GUIDE_BADGE_TOP`), un recuadro de esquinas redondeadas en **gris oscuro
casi negro** (`GUIDE_BADGE_BG`, no naranja) con **texto en blanco**
(`GUIDE_BADGE_TEXT`) para que resalte más, patrón fijo: `MEJORA Nº<N> ·
Te doy acceso a una guía SEO para ecommerce, actualizada cada día.` — es
el campo `guide_badge` (`number` + `line`) del slide `cover` en
`scripts/generate_carousel_post.py` (ver `guide_badge()`, ya forma parte
del motor de render, fijo). El `kicker` y el `subtitle` de la portada
vuelven a ser los de siempre (sin número ni frase añadida — el recuadro
ya lo dice todo).

`<N>` = número de la mejora **dentro de la guía de Notion**, no del
histórico completo de `TEMAS_TRATADOS.md`: empieza en **1** el día en que
se lanzó la guía en Notion (03/09/2026) y sube +1 cada día publicado
desde entonces. Fórmula: `N = (fecha de hoy − 03/09/2026 en días) + 1`
(03/09/2026 → 1, 04/09/2026 → 2, y así cada día). La frase `line` es fija
— cámbiala solo si Jorge pide explícitamente otro texto, nunca el número.

Con `guide_badge`, la portada admite como máximo 3 líneas de título (el
recuadro ocupa parte del espacio de arriba) — si el titular del día
necesita más líneas, acórtalo o muévelo parcialmente al `subtitle`.

**Slide de cierre (`closing`)**: mismo CTA que el post — `box_title`
describe brevemente qué se recibe, `box_link` repite la palabra clave del
día en el patrón `COMENTA "<PALABRA>" Y TE LO ENVÍO`. Nunca menciones un PDF
ni escribas la URL real — el enlace lo manda Jorge por DM.

**Recuadro naranja en TODAS las demás slides (no en `closing`, que ya lleva
su propio CTA grande)**: abajo del todo, un recuadro con esquinas
redondeadas, fondo naranja de marca, texto en **blanco** y flecha (dibujada
a mano, nunca un glifo) también en blanco, con el mismo patrón `COMENTA
"<PALABRA>" Y TE LO ENVÍO` — la misma palabra clave del día en cada slide,
para que quien vea cualquier página sepa qué comentar. El tamaño de letra de
este recuadro es **fijo** (no se auto-ajusta al contenido); lo único que
cambia de un día a otro es el ancho de la caja, según lo larga que sea la
palabra clave.

Los scripts antiguos (`generate_single_post_image.py`,
`generate_post_image.py`) se quedan en el repo sin usarse — no tocar salvo
instrucción expresa.

## 4. El recurso: guía única en Notion, ampliada por la rutina vía MCP

**Cambio de fondo desde el 03/09/2026, revisado el mismo día**: ya no se
genera un PDF/recurso distinto cada día (`scripts/generate_lead_magnet_pdf.py`
queda en el repo sin usarse). Existe **una única guía en Notion, pública,
que la propia rutina amplía cada día** — no un archivo que Jorge tenga que
pegar a mano, como se planteó en un primer momento: la rutina tiene acceso
directo a Notion vía conector MCP y escribe ahí ella misma.

**Página de la guía**: "Guía SEO Ecommerce — Jorge Segovia"
(`https://app.notion.com/p/3d050528a86481cab470f368ebfbb88c`). Es la página
exacta y única donde añadir contenido — no crear páginas nuevas ni buscar
otra.

### 4.1 El embudo completo (solo el paso 3 lo hace la rutina)

1. Alguien comenta la palabra clave del día en el post o el carrusel.
2. Jorge le escribe por DM (manual, fuera del alcance de esta rutina) con
   una URL de Mailchimp. La persona deja su correo ahí y es redirigida
   automáticamente a la página de Notion de arriba, con la guía completa.
3. **Lo único que genera la rutina**: usando el conector MCP de Notion,
   añade al final de esa página (después del contenido ya existente, sin
   borrar ni reescribir nada anterior) una entrada nueva con la mejora SEO
   del día.

### 4.2 Cómo escribir y añadir la entrada del día

A diferencia del post y el carrusel (que nunca dan la solución completa —
regla crítica de la sección 2, punto 4), **la entrada de Notion sí lleva la
solución completa, paso a paso** — es el recurso final del embudo, no un
teaser.

Estructura de cada entrada (como un bloque más de la página, con un
separador antes del siguiente):

- Encabezado con el título de la entrada (mismo o similar al titular del
  día — sección 2, punto 0) y la fecha
- Contexto/diagnóstico breve
- Por qué importa en términos de negocio
- Solución paso a paso, completa
- Herramientas usadas para detectarlo/arreglarlo
- Separador (`---`) antes de la siguiente entrada del día siguiente

Añade esta entrada a la página de Notion de arriba, al final de todo lo que
ya haya (nunca al principio, nunca sobrescribiendo entradas anteriores).
Además, guarda una copia del mismo contenido como
`content/<carpeta-del-día>/extracto-notion.md` en el repo — es solo un
respaldo por si falla la escritura en Notion, no hace falta que Jorge haga
nada con ese archivo si la escritura en Notion ha ido bien.

## 5. Entrega diaria — output

Carpeta: `content/YYYY-MM-DD/` (ya no lleva el ángulo en el nombre, al no
existir) con:

- `post-linkedin.txt`
- `carrusel-1.png` … `carrusel-N.png` + `carrusel-post.pdf`
- `extracto-notion.md` (copia de respaldo de lo que ya se añadió a Notion)
- Fila nueva añadida a `TEMAS_TRATADOS.md` (raíz del repo — sección 1)

Haz commit y push de toda la carpeta (mismo remoto del que se clonó) tan
pronto como esté lista. Mensaje de commit tipo `Contenido diario: <fecha>`.

Al terminar, envía los archivos a Jorge (vía `SendUserFile`) con una nota
breve: 1) copiar el post y subir `carrusel-post.pdf` a LinkedIn como
publicación de tipo Documento, 2) la palabra clave del día, para cuando
lleguen los comentarios (Jorge responde por DM con la URL de Mailchimp —
paso 100% manual), 3) confirmación de que la entrada de hoy ya se añadió a
la guía de Notion (o aviso si falló y hay que pegarla a mano desde el
archivo de respaldo).

**Nunca publicar nada en vivo automáticamente** — el post, el carrusel, la
respuesta a comentarios y el DM con la URL de Mailchimp son siempre acción
manual de Jorge; esta rutina entrega archivos, hace commit/push al
repositorio, y añade la entrada del día a Notion.

## 6. Entorno de ejecución (nube)

- Instala dependencias con `pip install -r requirements.txt` si `Pillow` /
  `img2pdf` no están ya disponibles.
- Intenta entregar todos los archivos generados directamente al usuario
  (herramienta de envío de archivos si está disponible en la sesión).
- **Además, y siempre**, haz commit y push de la carpeta `content/<día>/`
  generada al repositorio, como red de seguridad por si la entrega directa
  fallara.
- Usa el conector MCP de Notion para añadir la entrada del día a la página
  de la guía (sección 4). Si la escritura en Notion falla, no lo des por
  perdido en silencio: avísalo explícitamente en la entrega y confía en que
  el archivo de respaldo (`extracto-notion.md`) permite pegarlo a mano.

## 7. Fuera del alcance de la rutina en la nube

Todo esto es acción manual de Jorge, ninguna la ejecuta la rutina:

- Publicar el post/carrusel en LinkedIn y responder a comentarios.
- Escribir el DM con la URL de Mailchimp a quien comente la palabra clave.
- Todo lo que pase dentro de Mailchimp (captura del email, redirección) — la
  rutina sí escribe en Notion (ver sección 4), pero no toca Mailchimp.

(La sincronización de segmentos de Klaviyo por título de PDF, que existía
como sección 7 hasta el 03/09/2026, queda retirada — ya no hay un PDF nuevo
por día que generar un segmento. Si Jorge vuelve a necesitar segmentación
por tema en Mailchimp/Notion, habrá que documentar un mecanismo nuevo.)

---

## Nota de migración (03/09/2026) — se reescribe el brief a fondo

Resumen de lo que cambió respecto a la versión anterior (vigente desde el
31/08/2026), por si hace falta recuperar contexto:

- **Desaparece la rotación de ángulos por día de la semana** (Lunes-roast,
  Martes-mito, Miércoles-auditoría, Jueves-tendencia, Viernes-pregunta) y con
  ella la distinción entre L-V y fin de semana: **ahora se publica los 7
  días**. El criterio de "enfoque CEO" que antes vivía en la nota "1ter",
  atado a cada ángulo, ahora aplica siempre (nueva sección 1).
- **Vuelve el carrusel** como formato principal (`scripts/generate_carousel_post.py`,
  que había quedado sin usar desde el 28/08/2026 al adoptarse la imagen
  única), ahora con **fondo crema en vez de negro** (sección 3.2) y con el
  recordatorio de la palabra clave en un recuadro naranja llamativo en todas
  las slides, no solo un texto discreto (sección 3.3). `generate_single_post_image.py`
  pasa a ser el script que se queda sin usar.
- **Desaparece el PDF/recurso nuevo cada día** (`scripts/generate_lead_magnet_pdf.py`
  queda sin usar). En su lugar, una única guía viva en Notion que se amplía
  cada día con una entrada nueva (nueva sección 4).
- **Se retira la sección de Klaviyo** (antes sección 7): dependía de un
  título de PDF nuevo cada día que ya no existe.
- **`TEMAS_TRATADOS.md` cambia de estructura**: de 5 tablas por ángulo a una
  única lista cronológica (ver ese archivo para el detalle).

## Nota de migración 2 (03/09/2026, mismo día) — Notion pasa a ser automático

Unas horas después de la reescritura de arriba, Jorge conectó el conector
MCP de Notion a la cuenta que ejecuta esta rutina. Esto cambia el punto más
débil del plan anterior:

- **Antes** (nota de migración 1, mismo día): la rutina generaba
  `extracto-notion.md` y Jorge tenía que pegarlo él mismo en Notion.
- **Ahora**: la rutina usa el conector MCP de Notion para **añadir la
  entrada directamente** a la página de la guía (sección 4), sin
  intervención manual de Jorge. `extracto-notion.md` se sigue guardando en
  el repo, pero solo como copia de respaldo por si la escritura en Notion
  falla ese día.
- Se creó la página **"Guía SEO Ecommerce — Jorge Segovia"** en el Notion de
  Jorge para este propósito — es la página exacta a la que debe escribir la
  rutina (sección 4). El resto del embudo (comentar palabra clave → DM
  manual de Jorge con URL de Mailchimp → la persona deja su email → llega a
  esta página) no cambia.
