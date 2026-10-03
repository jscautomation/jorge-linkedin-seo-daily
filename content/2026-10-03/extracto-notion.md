## Tu competencia te roba clientes antes del clic — 03/10/2026

**Contexto / diagnóstico**: en fichas con variantes (talla, color, capacidad), el marcado de datos estructurados suele describir solo una variante —normalmente la primera o la más barata— como si fuera el producto entero. Google lee un único precio y una única disponibilidad para toda la ficha y puede mostrarlos en el resultado de búsqueda, aunque la variante que quiere el comprador cueste más o esté agotada. Causas habituales: (1) un solo bloque `Product` con un único `offers` para todas las variantes; (2) `price` o `availability` fijados en la plantilla en vez de leerse de la variante real; (3) cada variante con su propia URL pero sin relación declarada entre ellas; (4) el marcado no coincide con lo que se ve en la página o en el feed de Merchant Center.

**Por qué importa en términos de negocio**: el clic de alguien con intención de compra que llega y descubre que el precio o la disponibilidad no coinciden es una venta que se pierde y, además, una visita de pago o de tráfico gratis desperdiciada. Si el dato del resultado no es fiable, Google tiene menos motivos para confiar en la ficha frente a la de un competidor con el dato correcto. No salta ninguna alarma: la validación del marcado puede salir en verde y el checkout funciona.

**Solución paso a paso**:

1. **Detectar el problema**: elige 10 fichas con muchas variantes (las de más facturación) y compara, para cada una, el precio y la disponibilidad del resultado en Google (o de la Prueba de resultados enriquecidos) con los de la variante real en la web.
2. **Revisar el marcado actual**: abre la ficha en la Prueba de resultados enriquecidos de Google y en validator.schema.org; comprueba cuántos bloques `Product`/`Offer` hay y de dónde sale cada `price` y `availability`.
3. **Agrupar las variantes**: usa `ProductGroup` como producto padre con un `productGroupID` único y la propiedad `variesBy` (por ejemplo `https://schema.org/size` y `https://schema.org/color`), y un `Product` por variante dentro de `hasVariant`.
4. **Dar a cada variante sus propios datos**: cada `Product` hijo lleva su `sku` (y GTIN si existe), su `color`/`size`, su `url` (si tiene una propia, con el parámetro de variante) y su propio `offers` con `price`, `priceCurrency` y `availability` reales (`InStock`/`OutOfStock`).
5. **Generarlo desde los datos, no a mano**: que el precio y el stock salgan de la variante en el momento de renderizar (Shopify: Liquid con `variant.price` y `variant.available`; WordPress/WooCommerce: el plugin de datos estructurados o un fragmento que lea las variaciones). Evita valores fijos en la plantilla.
6. **Coherencia con el feed**: asegúrate de que los mismos `sku`, precio y disponibilidad coinciden con el feed de Merchant Center y con lo que se ve en la página; una discrepancia puede acabar en advertencias o rechazos en Merchant Center.
7. **Canonical coherente**: si cada variante tiene URL propia, decide una estrategia clara (cada variante canónica a sí misma o todas al producto padre) y no dejes que el canonical contradiga el marcado.
8. **Verificar y vigilar**: valida de nuevo con la Prueba de resultados enriquecidos, revisa los informes de "Fragmentos de productos" y "Comerciantes" en Search Console y los diagnósticos de Merchant Center; añade la revisión al QA de cualquier cambio de tema o de plugin.

**Herramientas usadas**: Prueba de resultados enriquecidos de Google, validator.schema.org, Search Console (informes de fragmentos de productos y de comerciantes), Merchant Center (Diagnóstico), Screaming Frog (extracción de datos estructurados) y la vista de código fuente.

---
