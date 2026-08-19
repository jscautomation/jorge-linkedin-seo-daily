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
| — | — | (aún sin publicar) |

## Viernes — Pregunta abierta + resumen semanal

| Fecha | Pregunta lanzada | Resumen de la semana |
|---|---|---|
| — | — | (aún sin publicar) |
