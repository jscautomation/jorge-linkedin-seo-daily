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
| 2026-08-25 | "Cuantas más páginas indexe Google, mejor" (aplicado a las combinaciones de filtro de talla/color/precio de un ecommerce) | Falso: la propia guía de crawl budget de Google señala la navegación por facetas como la causa más habitual de rastreo desperdiciado — más páginas indexadas no mejora el posicionamiento y diluye el presupuesto de rastreo de las fichas reales. Solución: distinguir filtro simple (indexable si tiene volumen real) de combinado (noindex,follow por defecto), canonical consistente a la categoría limpia, y revisión recurrente en cada lanzamiento de colección |

## Miércoles — Auditoría exprés a marca pública

| Fecha | Marca auditada | Hallazgo |
|---|---|---|
| 2026-08-19 | Clarks (calzado, migración internacional a dominio único por carpetas de país) | Hreflang ausente (ni HTML, ni cabeceras HTTP, ni sitemap) tras la migración → según datos públicos de SISTRIX, 61% (ES), 68% (FR), 62% (IT) y 64% (DE) de las keywords posicionaban con URL de otro mercado. Solución: hreflang recíproco por URL (incl. self-referencing), x-default correcto, y canonical siempre a sí mismo (nunca contradiciendo al hreflang) |

## Jueves — Tendencia / cambio de algoritmo

| Fecha | Tendencia | Ángulo para ecommerce |
|---|---|---|
| 2026-08-20 | AI Overviews devorando el tráfico informacional (43% de búsquedas, ~83% zero-click), y por qué la ficha de producto es la excepción | La ficha de producto sigue necesitando tráfico real y Google la usa para Shopping/carrito universal/citas en AI Overviews. Solución: checklist de 5 puntos de Product schema (precio sincronizado, availability en tiempo real, aggregateRating real, un único generador de JSON-LD, gtin/mpn/brand completos) |
| 2026-08-27 | Robots.txt bloqueando por error a los bots de IA que sí importan (OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot) al confundirlos con los de solo entrenamiento (GPTBot, ClaudeBot), y precio/stock que solo se pintan con JavaScript | Nuevo canal de compra vía IA generativa (ChatGPT, Perplexity) distinto de las AI Overviews de Google. Solución: 5 puntos (distinguir bot de entrenamiento vs. de consulta en tiempo real, revisar robots.txt/WAF línea a línea, comprobar el HTML crudo de la ficha sin JS) |

## Viernes — Pregunta abierta a la comunidad SEO

Desde el 21/08/2026 el viernes ya no repasa la semana (ver
`AUTOMATION_BRIEF.md` § 1) — es una pregunta abierta con la propia
respuesta/postura de Jorge como arranque de la conversación.

| Fecha | Pregunta lanzada | Respuesta de Jorge (tema real de fondo) |
|---|---|---|
| 2026-08-21 | ¿Cuál es, para ti, el error de SEO técnico más caro que sigue repitiéndose en el ecommerce? | Canonicals que apuntan a la home "por si acaso" en vez de a sí mismos — se cuelan en migraciones y rediseños, diluyen la relevancia de categorías y productos reales. Solución en el PDF: auditoría con Screaming Frog de canonicals que no autoreferencian + corrección por plantilla |
| 2026-08-28 | ¿Cuántas redirecciones lleva puestas tu ecommerce, una encima de otra, sin que nadie las haya tocado nunca? | Cadenas de redirects (301 sobre 301) acumuladas migración tras migración, cada una apuntando a la anterior en vez de al destino final — cuesta presupuesto de rastreo, velocidad y relevancia diluida por salto. Solución en el PDF: informe Redirect Chains de Screaming Frog (con "Always Follow Redirects" activado), repuntar cada cadena a un único salto directo, corregir sitemap/enlaces internos y repetir el crawl tras cada migración |
