# Registro de mejoras SEO ya publicadas

Esto lo lee la rutina automática **cada día, antes de elegir la mejora SEO
del día** (ver `AUTOMATION_BRIEF.md` § 1) — sirve para no repetir el mismo
error/mito/hallazgo/tendencia en fechas distintas, aunque cambie el título,
la marca de ejemplo o la redacción.

Se actualiza en el mismo commit que el contenido del día: al terminar de
generar todo, se añade una fila nueva al final de la tabla. No editar el
orden ni borrar filas antiguas — es el histórico completo.

**Nota de formato (03/09/2026):** hasta esta fecha el registro estaba
organizado en 5 tablas separadas, una por ángulo del día de la semana
(Lunes-roast, Martes-mito, Miércoles-auditoría, Jueves-tendencia,
Viernes-pregunta) — ver `AUTOMATION_BRIEF.md` para el porqué de ese cambio.
Esa rotación por día ya no existe, así que a partir de esta fecha el
registro es **una única lista cronológica**. Las filas anteriores al
03/09/2026 se han volcado aquí en orden de fecha, indicando entre
paréntesis el ángulo original solo como referencia histórica — no como
categoría que siga aplicando.

**Nota de formato 2 (03/09/2026, mismo día):** se añade la columna
**Pilar SEO**, tras el giro a organizar el contenido por pilares en vez de
por hallazgos sueltos (`AUTOMATION_BRIEF.md` §1.1) — usa esta columna cada
día para evitar repetir el pilar de ayer y para elegir dentro del pilar un
ángulo no tratado. Las filas anteriores a esta fecha llevan el pilar
asignado retroactivamente (más orientativo que estricto, al no haberse
elegido con este criterio en su momento).

| Fecha | Pilar SEO | Mejora SEO (el hallazgo/tema concreto) | Nota / solución completa (ahora vive en el extracto de Notion) |
|---|---|---|---|
| 2026-08-17 | Arquitectura y navegación | (roast) Duplicación de contenido por parámetros de filtro (talla/color) generando ~40 URLs clon de la misma categoría | Caso real ecommerce moda, +2M€/mes, posición 14→4 en 6 semanas. Solución: canonical hacia la URL limpia + NO bloquear por robots.txt + forzar recrawl en Search Console |
| 2026-08-18 | Indexación y rastreo | (mito) "Bloquear por robots.txt evita que Google indexe esa URL" | Falso: robots.txt controla rastreo, no indexación. Una URL bloqueada con enlaces puede seguir indexada (sin snippet), y bloquearla impide que Google vea un noindex/canonical puesto ahí. Solución: quitar bloqueo → noindex → confirmar en Search Console → opcionalmente rebloquear |
| 2026-08-19 | SEO internacional / multi-tienda | (auditoría) Clarks (calzado, migración internacional a dominio único por carpetas de país) | Hreflang ausente (ni HTML, ni cabeceras HTTP, ni sitemap) tras la migración → según datos públicos de SISTRIX, 61% (ES), 68% (FR), 62% (IT) y 64% (DE) de las keywords posicionaban con URL de otro mercado. Solución: hreflang recíproco por URL (incl. self-referencing), x-default correcto, y canonical siempre a sí mismo (nunca contradiciendo al hreflang) |
| 2026-08-20 | Datos estructurados | (tendencia) AI Overviews devorando el tráfico informacional (43% de búsquedas, ~83% zero-click), y por qué la ficha de producto es la excepción | La ficha de producto sigue necesitando tráfico real y Google la usa para Shopping/carrito universal/citas en AI Overviews. Solución: checklist de 5 puntos de Product schema (precio sincronizado, availability en tiempo real, aggregateRating real, un único generador de JSON-LD, gtin/mpn/brand completos) |
| 2026-08-21 | Indexación y rastreo | (pregunta abierta) ¿Cuál es el error de SEO técnico más caro que sigue repitiéndose en el ecommerce? | Respuesta de Jorge: canonicals que apuntan a la home "por si acaso" en vez de a sí mismos — se cuelan en migraciones y rediseños, diluyen la relevancia de categorías y productos reales. Solución: auditoría con Screaming Frog de canonicals que no autoreferencian + corrección por plantilla |
| 2026-08-24 | Arquitectura y navegación | (roast) Categorías de temporada pasada que devuelven 200 OK sin productos (en vez de 410/301) y siguen indexadas — "categorías fantasma" que compiten contra la colección nueva de cada temporada | Caso real ecommerce moda por temporadas, 140 de ~780 categorías indexadas en ese estado, algunas +1 año. Solución: encontrarlas con Screaming Frog (custom extraction + status code), clasificar recurrente-estacional vs. descatalogada-para-siempre, contenido "vuelve pronto" o 301 según el caso, confirmar en Search Console |
| 2026-08-25 | Arquitectura y navegación | (mito) "Cuantas más páginas indexe Google, mejor" (aplicado a las combinaciones de filtro de talla/color/precio de un ecommerce) | Falso: la propia guía de crawl budget de Google señala la navegación por facetas como la causa más habitual de rastreo desperdiciado — más páginas indexadas no mejora el posicionamiento y diluye el presupuesto de rastreo de las fichas reales. Solución: distinguir filtro simple (indexable si tiene volumen real) de combinado (noindex,follow por defecto), canonical consistente a la categoría limpia, y revisión recurrente en cada lanzamiento de colección |
| 2026-08-27 | Indexación y rastreo | (tendencia) Robots.txt bloqueando por error a los bots de IA que sí importan (OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot) al confundirlos con los de solo entrenamiento (GPTBot, ClaudeBot), y precio/stock que solo se pintan con JavaScript | Nuevo canal de compra vía IA generativa (ChatGPT, Perplexity) distinto de las AI Overviews de Google. Solución: 5 puntos (distinguir bot de entrenamiento vs. de consulta en tiempo real, revisar robots.txt/WAF línea a línea, comprobar el HTML crudo de la ficha sin JS) |
| 2026-08-31 | Migraciones y redirecciones | (roast) Cadenas de redirecciones 301 acumuladas en migraciones sucesivas (Prestashop→WooCommerce→Shopify), cada URL antigua saltando 2-5 veces antes de llegar a la página final en vez de un único salto directo | Caso anonimizado ecommerce moda con dos migraciones de plataforma. Solución: detectar con el informe "Redirect Chains" de Screaming Frog (Always Follow Redirects activado), reescribir cada redirección de origen para que apunte en un solo salto a la URL final actual, y añadir la revisión de cadenas al QA de cualquier migración futura |
| 2026-09-01 | Contenido de producto y categoría | (mito) "El contenido generado con IA penaliza en Google" | Falso: estudio de Ahrefs (~1M páginas del top 10, junio 2026) — 86,5% de las páginas mejor posicionadas tienen algo de contenido con IA, 5,3% del top 3 es 100% IA; Google no usa un "detector de IA" para penalizar, aplica las mismas señales de calidad de siempre. Ángulo CEO: el mito lleva a dos errores de negocio — frenar la producción por miedo, o publicar en bruto sin editar (ahí sí cae la indexación, del 49% al 40%, por ser genérico, no por ser IA). Solución: proceso mínimo de edición humana antes de publicar contenido con IA |
| 2026-09-02 | Velocidad y experiencia móvil | (auditoría) Mango (moda, desplome de visibilidad documentado por SISTRIX) | -75% de visibilidad en google.es y -90,5% en google.fr (su 2º mercado), por 3 errores estructurales de manual identificados por SISTRIX, de los que se documentan 2: (1) enlaces/contenido clave ocultos tras JavaScript/CSS que Googlebot no siempre procesa, (2) redirecciones 302 (temporales) usadas para cambios permanentes de URL en vez de 301. Solución: servir la navegación crítica en el HTML crudo (SSR o enlaces reales en el DOM inicial) + forzar 301 explícito en servidor/CDN para cualquier cambio de URL permanente, auditando con Screaming Frog tras cada migración |
| 2026-09-03 | Feeds y canales | (tendencia) Cierre de la Content API for Shopping (plazo de migración a la nueva Merchant API venció el 18/08/2026, peticiones antiguas empiezan a fallar desde el 01/09/2026) — muchas tiendas dependen de una app/plugin/herramienta de feeds de terceros que puede no haber migrado a tiempo, dejando el catálogo de Google Shopping con precio/stock desactualizados | Riesgo de negocio: suspensión de listados por discrepancia de precio y pérdida de tráfico/ventas mientras el feed está roto. Solución: 4 pasos (comprobar en Merchant Center > Diagnóstico si el feed está desactualizado, plan de contingencia con subida manual del feed mientras el proveedor migra, revisar discrepancias de precio antes de darlo por cerrado, y aprovechar para completar GTIN/MPN/marca/categoría de Google) |

<!-- A partir de aquí, añade una fila nueva por cada día publicado. -->
