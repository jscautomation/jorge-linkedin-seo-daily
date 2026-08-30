# Registro de temas ya publicados

Esto lo lee la rutina automática **cada mañana, antes de elegir el tema del
día** (ver `AUTOMATION_BRIEF.md` § 1bis) — sirve para no repetir el mismo
error de auditoría / mito / marca / tendencia en semanas distintas, aunque
cambie el título o la redacción.

Se actualiza en el mismo commit que el contenido del día: al terminar de
generar todo, se añade una fila nueva al final de la tabla correspondiente.
No editar el orden ni borrar filas antiguas — es el histórico completo.

## Rotación de plantilla de recurso (PDF)

Lee esta tabla **antes de elegir qué generador de PDF usar** (ver
`AUTOMATION_BRIEF.md` § 4) — el ciclo fijo es 1 Guía/checklist → 2
One-pager → 3 Worksheet → 4 Swipe file → vuelve a 1, independiente del
ángulo/día de la semana. Usa el tipo siguiente al de la última fila; si no
encaja con el tema de hoy, usa el próximo que sí encaje y anótalo en la
columna de nota.

| Fecha | Tipo usado | Nota |
|---|---|---|
| 2026-08-17 a 2026-08-27 | 1. Guía / checklist | Único generador que existía en ese momento (todos los días de roast/mito/auditoría/tendencia de esa fase) |
| 2026-08-28 | 2. One-pager | Primer uso del generador nuevo (regenerado a petición de Jorge sobre el recurso de cadenas de redirects, que ya se había entregado como guía) |
| 2026-08-31 | 3. Worksheet | Buscador interno indexado — encaja bien como autoevaluación |
| 2026-09-01 | 4. Swipe file | Mito del sitemap.xml — encaja bien con plantillas literales (entrada XML, línea de robots.txt) |
| 2026-09-02 | 1. Guía / checklist | Auditoría Topshop/ASOS — 1 solo punto, pero en formato guía por tocarle en el ciclo |
| 2026-09-03 | 2. One-pager | Tendencia AI Mode — 1 solo hallazgo, se lee de un vistazo |
| 2026-09-04 | 3. Worksheet | Páginas huérfanas — encaja bien como autoevaluación (repite tipo en la misma semana porque el ciclo de 4 no coincide con la semana de 5 días) |

## Lunes — Roast (error real de auditoría)

| Fecha | Tema (el error concreto) | Nota / solución en el PDF |
|---|---|---|
| 2026-08-17 | Duplicación de contenido por parámetros de filtro (talla/color) generando ~40 URLs clon de la misma categoría | Caso real ecommerce moda, +2M€/mes, posición 14→4 en 6 semanas. Solución: canonical hacia la URL limpia + NO bloquear por robots.txt + forzar recrawl en Search Console |
| 2026-08-24 | Categorías de temporada pasada que devuelven 200 OK sin productos (en vez de 410/301) y siguen indexadas — "categorías fantasma" que compiten contra la colección nueva de cada temporada | Caso real ecommerce moda por temporadas, 140 de ~780 categorías indexadas en ese estado, algunas +1 año. Solución: encontrarlas con Screaming Frog (custom extraction + status code), clasificar recurrente-estacional vs. descatalogada-para-siempre, contenido "vuelve pronto" o 301 según el caso, confirmar en Search Console |
| 2026-08-31 | Buscador interno sin protección: cada búsqueda de un visitante genera una URL nueva (?s=, /buscar?q=) que Google rastrea e indexa, compitiendo contra las categorías reales | Miles de URLs de "0 resultados" o resultados irrelevantes indexadas sin que nadie las creara a propósito. Solución: meta noindex,follow en la plantilla de resultados (nunca bloquear por robots.txt, taparía el noindex), solicitar eliminación en Search Console de las ya indexadas |

## Martes — Mito SEO desmontado con datos

| Fecha | Mito | Nota / qué dice Google realmente |
|---|---|---|
| 2026-08-18 | "Bloquear por robots.txt evita que Google indexe esa URL" | Falso: robots.txt controla rastreo, no indexación. Una URL bloqueada con enlaces puede seguir indexada (sin snippet), y bloquearla impide que Google vea un noindex/canonical puesto ahí. Solución: quitar bloqueo → noindex → confirmar en Search Console → opcionalmente rebloquear |
| 2026-08-25 | "Cuantas más páginas indexe Google, mejor" (aplicado a las combinaciones de filtro de talla/color/precio de un ecommerce) | Falso: la propia guía de crawl budget de Google señala la navegación por facetas como la causa más habitual de rastreo desperdiciado — más páginas indexadas no mejora el posicionamiento y diluye el presupuesto de rastreo de las fichas reales. Solución: distinguir filtro simple (indexable si tiene volumen real) de combinado (noindex,follow por defecto), canonical consistente a la categoría limpia, y revisión recurrente en cada lanzamiento de colección |
| 2026-09-01 | "El sitemap.xml no afecta al SEO, solo ayuda a que Google encuentre las URLs" | Medio verdad: no garantiza indexación, pero Google lo usa como señal de qué URLs importan y cuándo revisarlas (lastmod preciso ayuda a priorizar el recrawl); un sitemap autogenerado con URLs redirigidas/noindex/rotas manda ruido que diluye esa señal. Solución: entradas de sitemap solo con URLs 200 e indexables, lastmod real (no fijo), auditoría periódica con Screaming Frog en List Mode |

## Miércoles — Auditoría exprés a marca pública

| Fecha | Marca auditada | Hallazgo |
|---|---|---|
| 2026-08-19 | Clarks (calzado, migración internacional a dominio único por carpetas de país) | Hreflang ausente (ni HTML, ni cabeceras HTTP, ni sitemap) tras la migración → según datos públicos de SISTRIX, 61% (ES), 68% (FR), 62% (IT) y 64% (DE) de las keywords posicionaban con URL de otro mercado. Solución: hreflang recíproco por URL (incl. self-referencing), x-default correcto, y canonical siempre a sí mismo (nunca contradiciendo al hreflang) |
| 2026-09-02 | Topshop (moda, fusionada dentro de ASOS tras el cierre de Arcadia Group en 2021) | Redirecciones wildcard (en bloque) en vez de mapeo 1:1 por URL al migrar el catálogo → según datos públicos de SISTRIX, topshop.com perdió ~80% de su visibilidad en buscadores, y esa autoridad no pasó a ASOS. Solución: mapear cada URL antigua a su equivalente específico (nunca un catch-all genérico), verificar con Screaming Frog en modo lista tras el lanzamiento |

## Jueves — Tendencia / cambio de algoritmo

| Fecha | Tendencia | Ángulo para ecommerce |
|---|---|---|
| 2026-08-20 | AI Overviews devorando el tráfico informacional (43% de búsquedas, ~83% zero-click), y por qué la ficha de producto es la excepción | La ficha de producto sigue necesitando tráfico real y Google la usa para Shopping/carrito universal/citas en AI Overviews. Solución: checklist de 5 puntos de Product schema (precio sincronizado, availability en tiempo real, aggregateRating real, un único generador de JSON-LD, gtin/mpn/brand completos) |
| 2026-08-27 | Robots.txt bloqueando por error a los bots de IA que sí importan (OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot) al confundirlos con los de solo entrenamiento (GPTBot, ClaudeBot), y precio/stock que solo se pintan con JavaScript | Nuevo canal de compra vía IA generativa (ChatGPT, Perplexity) distinto de las AI Overviews de Google. Solución: 5 puntos (distinguir bot de entrenamiento vs. de consulta en tiempo real, revisar robots.txt/WAF línea a línea, comprobar el HTML crudo de la ficha sin JS) |
| 2026-09-03 | Google AI Mode citando fichas con datos estructurados extraíbles (FAQ, specs en texto real) en vez de solo texto de marketing — angulo distinto al post anterior de AI Overviews/Product schema: aquí el foco es la estructura del contenido (FAQ+specs), no el schema de producto en sí | Un análisis público reciente encontró que la mayoría de páginas citadas por Google AI Mode llevan datos estructurados. Solución: FAQPage schema con preguntas reales, specs en tabla HTML (nunca en imagen), combinar Product+FAQ+Review schema, verificar con Rich Results Test |

## Viernes — Pregunta abierta a la comunidad SEO

Desde el 21/08/2026 el viernes ya no repasa la semana (ver
`AUTOMATION_BRIEF.md` § 1) — es una pregunta abierta con la propia
respuesta/postura de Jorge como arranque de la conversación.

| Fecha | Pregunta lanzada | Respuesta de Jorge (tema real de fondo) |
|---|---|---|
| 2026-08-21 | ¿Cuál es, para ti, el error de SEO técnico más caro que sigue repitiéndose en el ecommerce? | Canonicals que apuntan a la home "por si acaso" en vez de a sí mismos — se cuelan en migraciones y rediseños, diluyen la relevancia de categorías y productos reales. Solución en el PDF: auditoría con Screaming Frog de canonicals que no autoreferencian + corrección por plantilla |
| 2026-08-28 | ¿Cuántas redirecciones lleva puestas tu ecommerce, una encima de otra, sin que nadie las haya tocado nunca? | Cadenas de redirects (301 sobre 301) acumuladas migración tras migración, cada una apuntando a la anterior en vez de al destino final — cuesta presupuesto de rastreo, velocidad y relevancia diluida por salto. Solución en el PDF: informe Redirect Chains de Screaming Frog (con "Always Follow Redirects" activado), repuntar cada cadena a un único salto directo, corregir sitemap/enlaces internos y repetir el crawl tras cada migración |
| 2026-09-04 | ¿Cuál es la página de tu catálogo que más venderías... si Google supiera que existe? | Páginas huérfanas: productos o categorías publicados y en el sitemap, pero sin un solo enlace interno real entrante — el sitemap ayuda a descubrirlas, pero sin enlazado interno Google no sabe cuánto importan y a veces ni terminan de indexarse. Solución en el PDF: informe de Inlinks en Screaming Frog ordenado de menor a mayor, añadir 2-3 enlaces reales desde páginas con autoridad a cada huérfana |
