## Tu catálogo dejó de llegar a Google (03/09/2026)

**Contexto:** Muchas tiendas online no llaman ellas mismas a la API de Google Shopping — lo hace la app de la plataforma (Shopify, WooCommerce) o la herramienta de feeds contratada. El 18 de agosto de 2026 venció el plazo de Google para migrar de la antigua Content API for Shopping a la nueva Merchant API. Desde el 1 de septiembre, las peticiones que todavía usan la API antigua empiezan a fallar — y si el proveedor de feeds no migró a tiempo, el catálogo se queda congelado en la última sincronización que sí funcionó, sin que nadie lo note hasta días después.

**Por qué importa:** Un feed desincronizado no es un detalle técnico, es dinero. Google puede suspender listados por discrepancia de precio o stock respecto a lo que ve en la web, y cada día con el feed roto es tráfico y ventas de Shopping que se lleva la competencia que sí sincroniza bien. Cuanto más tarde en detectarse, más caro sale.

**Solución paso a paso:**
1. Entra en Google Merchant Center → Diagnóstico y revisa la fecha de última actualización de tus productos. Si lleva más de 24-48h sin refrescarse, el feed está roto.
2. Mientras el proveedor del feed migra, activa un plan de contingencia: sube el feed manualmente (archivo o Google Sheets programado) para no perder listados activos.
3. Antes de dar el problema por cerrado, revisa que no haya discrepancias de precio o stock entre lo que muestra Merchant Center y lo que hay realmente en la tienda — es la causa más habitual de suspensión de listados.
4. Aprovecha la revisión para completar los atributos que Google prioriza cada vez más: GTIN, MPN, marca y categoría de Google — reducen el riesgo de rechazo y mejoran la relevancia en Shopping.

**Herramientas usadas:** Google Merchant Center (Diagnóstico), el panel de la app/plugin de feeds de la plataforma (Shopify/WooCommerce), y una hoja de cálculo o export manual del catálogo como plan de contingencia.

---

**Nota de esta ejecución (backfill):** el post y el carrusel de este tema ya se publicaron el 03/09/2026 bajo el formato antiguo del brief (imagen única + PDF de recurso), antes de que Jorge reescribiera `AUTOMATION_BRIEF.md` ese mismo día para introducir el nuevo sistema (carrusel crema + guía única en Notion vía MCP, sin rotación de ángulos). Como el tema de hoy ya estaba elegido, publicado y registrado en `TEMAS_TRATADOS.md`, esta entrada de Notion completa retroactivamente el paso 3 del nuevo embudo (sección 4) para el contenido ya publicado — no se ha generado un segundo post/carrusel para la misma fecha. El primer día completo bajo el nuevo sistema (carrusel crema + Notion elegidos desde cero) será el 04/09/2026.
