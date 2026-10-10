## Tus ofertas no se ven en Google y tu competencia se lleva la venta — 10/10/2026

**Contexto / diagnóstico**: en muchas tiendas el descuento se aplica en la web (precio tachado, banner, código automático) pero el feed de Google Merchant Center sigue enviando solo el precio normal (`price`) y no declara el precio rebajado (`sale_price`). O lo envía con retraso, porque el feed se genera una vez al día o se sube a mano. Resultado: en Google Shopping y en los listados de producto se ve el precio de siempre, mientras el competidor que sí declara su oferta aparece con el precio rebajado.

**Por qué importa en términos de negocio**: quien compara precios decide en segundos y se queda con el que parece más barato. Tú pagas el descuento en margen y no recibes el tráfico que esa oferta debería atraer, justo en tus campañas más importantes (rebajas, Black Friday, Navidad). Además, si el precio del feed no coincide con el de la ficha, Google puede marcar el producto con una discrepancia de precio y suspenderlo, así que pierdes también la visibilidad que sí tenías.

**Solución paso a paso**:

1. **Comprueba lo que ve el comprador**: busca en Google tus 5-10 productos en oferta (en incógnito y en móvil) y compara el precio que se muestra con el de la ficha. Anota las discrepancias.
2. **Revisa el feed**: en Merchant Center > Productos, comprueba que los artículos en oferta llevan `price` (precio original) y `sale_price` (precio rebajado) con la misma moneda y formato que la ficha.
3. **Declara la vigencia**: usa `sale_price_effective_date` (fecha y hora de inicio y fin de la oferta) para que la oferta se active y se retire sola, sin depender de acordarse a mano.
4. **Automatiza la sincronización**: configura el feed (app de Shopify, plugin de WooCommerce o herramienta de feeds) para que se actualice con frecuencia suficiente en campaña, y evita subidas manuales de hojas de cálculo.
5. **Vigila los diagnósticos**: en Merchant Center > Diagnóstico revisa las advertencias de discrepancia de precio y los productos rechazados, y corrige la causa (feed desfasado, redondeos, impuestos incluidos o no).
6. **Alinea la ficha**: comprueba que el precio visible y el marcado `Product`/`Offer` de la ficha coinciden con el `sale_price` del feed.
7. **Convierte la revisión en rutina**: añade una comprobación de feed y precios a la checklist de cada campaña (24-48 h antes de empezar y el primer día) y repítela al terminar para retirar la oferta correctamente.

**Herramientas usadas**: Google Merchant Center (Productos y Diagnóstico), búsqueda en Google en incógnito, la app o plugin de feeds de la plataforma, Prueba de Resultados Enriquecidos de Google para el marcado de la ficha.

---
