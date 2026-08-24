# Registro de temas ya publicados

Esto lo lee la rutina automática **cada mañana, antes de elegir el tema del
día** (ver `AUTOMATION_BRIEF.md` § 1bis) — sirve para no repetir el mismo
error de auditoría / mito / marca / tendencia en semanas distintas, aunque
cambie el título o la redacción.

Se actualiza en el mismo commit que el contenido del día: al terminar de
generar todo, se añade una fila nueva al final de la tabla correspondiente.
No editar el orden ni borrar filas antiguas — es el histórico completo.

## Lunes — Roast (error real de auditoría)

| Fecha | Tema (el error concreto) | Nota / solución en el PDF |
|---|---|---|
| 2026-08-17 | Duplicación de contenido por parámetros de filtro (talla/color) generando ~40 URLs clon de la misma categoría | Caso real ecommerce moda, +2M€/mes, posición 14→4 en 6 semanas. Solución: canonical hacia la URL limpia + NO bloquear por robots.txt + forzar recrawl en Search Console |
| 2026-08-24 | Categorías de temporada pasada que devuelven 200 OK sin productos (en vez de 410/301) y siguen indexadas — "categorías fantasma" que compiten contra la colección nueva de cada temporada | Caso real ecommerce moda por temporadas, 140 de ~780 categorías indexadas en ese estado, algunas +1 año. Solución: encontrarlas con Screaming Frog (custom extraction + status code), clasificar recurrente-estacional vs. descatalogada-para-siempre, contenido "vuelve pronto" o 301 según el caso, confirmar en Search Console |

## Martes — Mito SEO desmontado con datos

| Fecha | Mito | Nota / qué dice Google realmente |
|---|---|---|
| 2026-08-18 | "Bloquear por robots.txt evita que Google indexe esa URL" | Falso: robots.txt controla rastreo, no indexación. Una URL bloqueada con enlaces puede seguir indexada (sin snippet), y bloquearla impide que Google vea un noindex/canonical puesto ahí. Solución: quitar bloqueo → noindex → confirmar en Search Console → opcionalmente rebloquear |

## Miércoles — Auditoría exprés a marca pública

| Fecha | Marca auditada | Hallazgo |
|---|---|---|
| 2026-08-19 | Clarks (calzado, migración internacional a dominio único por carpetas de país) | Hreflang ausente (ni HTML, ni cabeceras HTTP, ni sitemap) tras la migración → según datos públicos de SISTRIX, 61% (ES), 68% (FR), 62% (IT) y 64% (DE) de las keywords posicionaban con URL de otro mercado. Solución: hreflang recíproco por URL (incl. self-referencing), x-default correcto, y canonical siempre a sí mismo (nunca contradiciendo al hreflang) |

## Jueves — Tendencia / cambio de algoritmo

| Fecha | Tendencia | Ángulo para ecommerce |
|---|---|---|
| 2026-08-20 | AI Overviews devorando el tráfico informacional (43% de búsquedas, ~83% zero-click), y por qué la ficha de producto es la excepción | La ficha de producto sigue necesitando tráfico real y Google la usa para Shopping/carrito universal/citas en AI Overviews. Solución: checklist de 5 puntos de Product schema (precio sincronizado, availability en tiempo real, aggregateRating real, un único generador de JSON-LD, gtin/mpn/brand completos) |

## Viernes — Pregunta abierta a la comunidad SEO

Desde el 21/08/2026 el viernes ya no repasa la semana (ver
`AUTOMATION_BRIEF.md` § 1) — es una pregunta abierta con la propia
respuesta/postura de Jorge como arranque de la conversación.

| Fecha | Pregunta lanzada | Respuesta de Jorge (tema real de fondo) |
|---|---|---|
| 2026-08-21 | ¿Cuál es, para ti, el error de SEO técnico más caro que sigue repitiéndose en el ecommerce? | Canonicals que apuntan a la home "por si acaso" en vez de a sí mismos — se cuelan en migraciones y rediseños, diluyen la relevancia de categorías y productos reales. Solución en el PDF: auditoría con Screaming Frog de canonicals que no autoreferencian + corrección por plantilla |
