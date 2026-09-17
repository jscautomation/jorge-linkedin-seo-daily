## Mejora nº15: Estás perdiendo ventas sin que te visiten — 2026-09-17

**Pilar SEO:** Datos estructurados

**Contexto/diagnóstico:** Un comprador puede decidir si te compra o no antes de haber pisado tu tienda, solo mirando el resultado de Google. Es habitual encontrar ecommerce con buena ficha, buen precio y buenas reseñas, pero sin ni rastro de su política de devoluciones en el propio resultado de búsqueda ni en Google Shopping — mientras su competencia directa sí muestra "devoluciones gratis 30 días" junto al producto. La causa casi siempre es la misma: falta o está incompleta la marca de datos estructurados `MerchantReturnPolicy` en la ficha de producto (o no está configurada la política de devoluciones a nivel de cuenta en Merchant Center / Search Console), así que Google no tiene de dónde sacar esa información para mostrarla.

**Por qué importa en términos de negocio:** No es un problema de servicio al cliente ni de marketing — la tienda puede tener una política de devoluciones excelente y perder la venta igualmente, porque el comprador nunca llega a verla. Según UPS, hasta un 68% de los compradores online revisa la política de devoluciones antes de decidirse a comprar, y buena parte de esa revisión ocurre antes de entrar en la ficha, comparando resultados en el propio Google. Sin el dato estructurado, la tienda tampoco puede optar a la insignia de "tienda de calidad" que Google concede a comercios con condiciones de devolución claras y conformes — una señal de confianza adicional que sí exhibe la competencia. El resultado es venta que se pierde sin que salte ninguna alarma en las métricas de la propia web, porque el usuario nunca llega a entrar ni a abandonar un carrito: decide fuera, comparando.

**Solución paso a paso:**

1. **Audita en incógnito qué ve hoy un comprador.** Busca tu marca y tus productos principales en Google (modo incógnito, y por país si vendes en varios mercados) y anota si aparece algo sobre devoluciones junto al resultado o en Shopping. Compáralo con 2-3 competidores directos.
2. **Revisa si tienes marcado `MerchantReturnPolicy` en tus fichas de producto.** Comprueba el JSON-LD de una ficha con la Prueba de Resultados Enriquecidos de Google (o inspeccionando el código) y confirma si incluye plazo de devolución, método, gastos y condiciones — y si esos datos coinciden con la política real publicada en la web.
3. **Alternativa más simple si no quieres tocar el marcado ficha a ficha:** configura la política de devoluciones a nivel de cuenta directamente en Search Console (se traslada automáticamente a Merchant Center) o en el propio Merchant Center si ya tienes cuenta — cubre todo el catálogo de una vez sin depender del desarrollo.
4. **Sincroniza ambos lados.** Si usas Merchant Center para Shopping, comprueba que la política configurada ahí coincide exactamente con la de tu web (plazos, condiciones, gastos) — es habitual que cambien en un sitio y no en el otro tras una actualización de política.
5. **Si vendes en varios países o tiendas**, confirma que cada mercado tiene su propia política reflejada correctamente en sus datos estructurados — no vale una única configuración genérica si las condiciones reales varían por país.
6. **Verifica el resultado** repitiendo la búsqueda en incógnito del paso 1 tras el cambio, y revisa en Merchant Center si la cuenta pasa a ser elegible para la insignia de tienda de calidad.

**Herramientas usadas para detectarlo/arreglarlo:** Búsqueda en incógnito (por país) para auditar el SERP y Shopping, Prueba de Resultados Enriquecidos de Google para comprobar el JSON-LD de producto, Google Search Console (configuración de políticas de devolución a nivel de cuenta) y Google Merchant Center (Diagnóstico y elegibilidad para la insignia de tienda de calidad).

---
