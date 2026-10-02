## Tu Shopify puede perder ventas el 1 de marzo — 02/10/2026

**Contexto / diagnóstico**: muchas apps de Shopify (reseñas, recomendados, píxeles de marketing, widgets de datos estructurados) añaden su código a la tienda mediante los llamados *script tags* (ScriptTag API), un método antiguo. Shopify ha fijado dos fechas: desde el **1 de octubre de 2026** las mutaciones `scriptTagCreate` y `scriptTagUpdate` dejan de funcionar (no se pueden crear ni actualizar script tags), y desde el **1 de marzo de 2027** Shopify deja de inyectar en la tienda los script tags existentes. Hasta entonces los ya instalados siguen funcionando, por lo que no salta ningún error. Los sustitutos oficiales son los *Web Pixels* (analítica y conversión) y los *app embed blocks* de las *theme app extensions* (comportamiento o interfaz en la tienda).

**Por qué importa en términos de negocio**: lo que una app pinta hoy en la ficha o mide en el checkout puede desaparecer en marzo si la app no ha migrado: estrellas de reseñas y datos de producto que alimentan el aspecto del resultado en Google, píxeles de conversión que alimentan tus campañas, bloques de recomendados que empujan el ticket medio. Resultado: menos clics, menos conversión y campañas optimizando a ciegas, sin una alerta que te avise. Quien lo revisa ahora lo arregla con calma; quien espera a marzo lo arregla con las ventas ya cayendo.

**Solución paso a paso**:

1. **Inventario de apps**: en el admin de Shopify (Ajustes → Apps) lista todas las apps instaladas y apunta qué hace cada una en la tienda (reseñas, píxeles, recomendados, datos estructurados, chat, etc.).
2. **Detectar quién inyecta con script tags**: abre una ficha de producto, "Ver código fuente" o DevTools → Red/Elements, y localiza los scripts de terceros cargados desde el dominio de cada app. Pregunta además a cada proveedor (o consulta su documentación/changelog) si su app ya usa app embed blocks o Web Pixels. Sospecha en especial de apps antiguas o sin actualizaciones recientes.
3. **Priorizar por impacto en ventas**: primero lo que toca ingresos (píxeles de conversión de Google/Meta, reseñas con estrellas, recomendados), después lo cosmético.
4. **Exigir o ejecutar la migración**: escribe a cada proveedor pidiendo confirmación escrita de que migran antes del 1 de marzo de 2027. Si es una app a medida o código propio: analítica → Web Pixel; interfaz/comportamiento → theme app extension con app embed block.
5. **Probar tras actualizar**: tras cada actualización de app, comprueba en una ficha real que el elemento sigue apareciendo y que las conversiones se registran (Vista previa de Tag Assistant / Pixel Helper, y la Prueba de Resultados Enriquecidos de Google para estrellas y datos de producto).
6. **Plan B**: si una app clave no migra, busca alternativa antes de enero y deja margen para probarla; evita descubrirlo el 1 de marzo.
7. **Revisar el efecto semanas después**: compara en Search Console (CTR y resultados enriquecidos) y en tus informes de conversión que no hay caída tras los cambios; repite el inventario cada trimestre.

**Herramientas usadas**: admin de Shopify (apps y pixels), DevTools del navegador, Prueba de Resultados Enriquecidos de Google, Tag Assistant / Meta Pixel Helper, Search Console.

---
