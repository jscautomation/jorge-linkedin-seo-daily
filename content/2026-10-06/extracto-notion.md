## Estás regalando ventas a tu competencia — 06/10/2026

**Contexto / diagnóstico**: una ficha de producto con varios colores y tallas puede estar comunicando mal a Google qué es "un producto con variantes" y qué son productos distintos. Si cada variante tiene su URL pero nada las agrupa (ni en el marcado de la ficha ni en el feed de Merchant Center), o si todas comparten un único precio, una única imagen y una única disponibilidad, Google no sabe qué variante enseñar a quien busca "modelo + color + talla". Muestra una cualquiera, o prefiere la de otra tienda que sí lo tiene claro.

**Por qué importa en términos de negocio**: quien busca un color y una talla concretos ya quiere comprar. Si ve una foto, un precio o una talla que no es la suya, no investiga: compra donde la ficha le muestra exactamente lo que buscó. Es venta orgánica gratuita que se va a la competencia sin ningún aviso en tus métricas.

**Solución paso a paso**:

1. **Mide el problema**: en incógnito y en móvil, busca "modelo + color" y "modelo + talla" de tus 10 productos más vendidos. Anota en cuántos Google muestra la variante correcta (foto, precio, disponibilidad).
2. **Decide la estructura**: define qué es el producto "padre" (el modelo) y qué son las variantes (color, talla...). Cada variante necesita su propio identificador (SKU, y GTIN si lo tiene).
3. **Marca el grupo en la ficha**: en el JSON-LD usa `ProductGroup` para el modelo, con `productGroupID`, `variesBy` (las propiedades que varían, p. ej. color y talla) y `hasVariant` con un `Product` por variante (SKU, color/talla, imagen, `offers` con su precio y disponibilidad reales).
4. **Una imagen y un precio por variante**: cada variante debe apuntar a su imagen propia y a su precio real, no a los valores por defecto del modelo.
5. **Alinea el feed de Merchant Center**: todas las variantes de un mismo modelo deben compartir el mismo `item_group_id` en el feed, y los atributos `color`, `size` y similares deben rellenarse en cada una. Revisa que precio y disponibilidad del feed coincidan con la ficha.
6. **Genera todo desde una única fuente**: que el JSON-LD y el feed salgan de los mismos datos de producto de la tienda (plugin o tema de WordPress/Shopify bien configurado), para que no se desincronicen.
7. **Valida y repite**: comprueba el marcado con la Prueba de Resultados Enriquecidos de Google y el feed en Merchant Center > Diagnóstico. Repite la comprobación del paso 1 a las 2-4 semanas y en cada lanzamiento de colección.

**Herramientas usadas**: navegador en incógnito (escritorio y móvil), Prueba de Resultados Enriquecidos de Google, Google Search Console, Merchant Center (Diagnóstico y atributos del feed), y el inspector del navegador para revisar el JSON-LD de la ficha.

---
