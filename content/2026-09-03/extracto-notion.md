## Estás perdiendo ventas en Google Shopping (03/09/2026)

**Contexto:** Muchas tiendas online no llaman ellas mismas a la API de Google Shopping — lo hace la app de la plataforma (Shopify, WooCommerce) o la herramienta de feeds contratada. El 18 de agosto de 2026 venció el plazo de Google para migrar de la antigua Content API for Shopping a la nueva Merchant API. Desde el 1 de septiembre, las peticiones que todavía usan la API antigua empiezan a fallar — y si el proveedor de feeds no migró a tiempo, el catálogo se queda congelado en la última sincronización que sí funcionó, sin que nadie lo note hasta días después.

**Por qué importa:** Un feed desincronizado no es un detalle técnico, es ventas que se escapan. Google puede suspender listados por discrepancia de precio o stock respecto a lo que ve en la web, y cada día con el feed roto es tráfico y ventas de Shopping que se lleva la competencia que sí sincroniza bien. Cuanto más tarde en detectarse, más factura te cuesta.

**Solución paso a paso:**
1. Entra en Google Merchant Center → Diagnóstico y revisa la fecha de última actualización de tus productos. Si lleva más de 24-48h sin refrescarse, el feed está roto.
2. Mientras el proveedor del feed migra, activa un plan de contingencia: sube el feed manualmente (archivo o Google Sheets programado) para no perder listados activos ni las ventas que traen.
3. Antes de dar el problema por cerrado, revisa que no haya discrepancias de precio o stock entre lo que muestra Merchant Center y lo que hay realmente en la tienda — es la causa más habitual de suspensión de listados.
4. Aprovecha la revisión para completar los atributos que Google prioriza cada vez más: GTIN, MPN, marca y categoría de Google — reducen el riesgo de rechazo y mejoran la relevancia (y las ventas) en Shopping.

**Herramientas usadas:** Google Merchant Center (Diagnóstico), el panel de la app/plugin de feeds de tu plataforma (Shopify/WooCommerce), y una hoja de cálculo o export manual del catálogo como plan de contingencia.

---

<!-- NOTA: esta entrada ya estaba añadida en la página de Notion antes de
ejecutarse este paso de la rutina (escrita por una ejecución anterior, ya
interrumpida, del mismo día 03/09/2026) — verificado con notion-fetch antes
de tocar nada. Este archivo es solo la copia de respaldo en el repo; no se
ha vuelto a escribir en Notion para evitar duplicar la entrada de hoy. -->
