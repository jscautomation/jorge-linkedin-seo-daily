## Estás regalando ventas a tu competencia — 29/09/2026

**Contexto / diagnóstico**: en una tienda de moda cada producto suele existir en muchos colores y tallas, y cada variante tiene su propia URL y ficha. Si el marcado de datos estructurados de esas fichas trata cada variante como un producto aislado (o solo marca una), Google no entiende que todas son el mismo artículo con opciones. El resultado: muestra en Shopping y en resultados enriquecidos una variante equivocada, un precio o una disponibilidad que no corresponde con lo que busca el comprador, o directamente prioriza a un competidor cuyo catálogo sí entiende bien.

El mecanismo técnico es el marcado `ProductGroup` de schema.org, que agrupa las variantes (`hasVariant`) bajo un mismo producto padre e indica por qué propiedades varían (`variesBy`: color, talla...). Google lo documenta para fichas de producto con variantes.

**Por qué importa en términos de negocio**: quien busca "vestido midi verde talla 40" está a un paso de comprar. Ese tráfico, además, es orgánico (gratis). Si Google no relaciona bien tus variantes, esa venta con alta intención se va a la tienda que sí tiene el catálogo bien explicado. Además, un precio o stock incorrecto en el resultado genera clics que no convierten y frustración justo antes de la compra.

**Solución paso a paso**:

1. **Ver qué ve hoy el comprador**: en incógnito y en móvil, buscar 3-4 de tus productos con variantes ("nombre + color + talla") y anotar qué variante, precio y disponibilidad muestra Google, y qué tiendas aparecen por delante.
2. **Auditar el marcado actual**: pasar una ficha con variantes por la Prueba de Resultados Enriquecidos de Google y por el validador de schema.org, y revisar si hay un único `Product` por URL sin relación con las demás variantes, o varios marcados contradictorios.
3. **Definir el producto padre**: asignar un identificador de grupo común a todas las variantes (`productGroupID`, normalmente el SKU padre) y declarar por qué propiedades varían (`variesBy`, por ejemplo color y talla).
4. **Marcar cada variante**: dentro del `ProductGroup`, listar cada variante en `hasVariant` con su propia URL, su `sku`, `color`/`size`, imagen, `gtin` o `mpn`, y su `offers` con el precio y la disponibilidad reales de esa variante.
5. **Generarlo desde una sola fuente**: implementarlo por plantilla, alimentado por los mismos datos que usa la tienda para el precio y el stock (nunca escrito a mano), para que no se desincronice. En Shopify o WordPress/WooCommerce, revisar antes qué genera ya el tema o el plugin de SEO, para no duplicar marcado ni entrar en contradicción con él.
6. **Alinear con el feed de Merchant Center**: comprobar que el `item_group_id` del feed de cada variante coincide con el grupo declarado en la web, y que precio y stock coinciden entre feed y ficha.
7. **Verificar y vigilar**: validar de nuevo con la Prueba de Resultados Enriquecidos, revisar en Search Console el informe de Fichas de comerciante/Datos estructurados 2-4 semanas después, y repetir la comprobación en cada lanzamiento de colección o cambio de tema.

**Herramientas usadas**: Prueba de Resultados Enriquecidos de Google, validador de schema.org, Google Search Console (mejoras de datos estructurados), Merchant Center (Diagnóstico y feed), Screaming Frog (extracción del JSON-LD por URL).

---
