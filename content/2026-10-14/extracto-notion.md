## Tus fotos bonitas están frenando tus ventas en el móvil — 14/10/2026

**Contexto / diagnóstico**: muchas tiendas suben las fotos de producto tal como salen de la cámara o del proveedor (3000-4000 px, varios MB, JPG o PNG) y el tema las sirve igual a todos los dispositivos. En móvil, con conexión limitada, la ficha tarda en mostrar la foto principal; además, si la imagen no tiene su espacio reservado, la página "salta" al cargar. Nada da error: la web funciona, pero compra menos gente.

**Por qué importa en términos de negocio**: la velocidad móvil afecta directamente a la conversión. El estudio de Deloitte y Google "Milliseconds Make Millions" midió que mejorar 0,1 s la velocidad móvil sube la conversión de retail un 8,4%. Además, Google tiene en cuenta la experiencia de página (Core Web Vitals) al posicionar, así que una ficha lenta recibe menos tráfico orgánico y convierte peor el que llega. Son ventas que se pierden sin ninguna alerta.

**Solución paso a paso**:

1. **Mide el punto de partida**: abre en PageSpeed Insights (modo móvil) tu ficha de producto más vendida y una categoría principal. Anota el LCP y las advertencias "Ajusta el tamaño de las imágenes", "Sirve imágenes con formatos modernos" y "Codifica las imágenes de forma eficiente".
2. **Mira cuánto pesa lo que sirves**: en Chrome DevTools > Red > Img, recarga la ficha y ordena por tamaño. Como referencia práctica, una foto principal de ficha por debajo de ~150-200 KB y una de galería por debajo de ~100-150 KB suele bastar sin pérdida visible.
3. **Cambia el flujo de subida**: redimensiona antes de subir (lado largo de 1500-2000 px suele sobrar para zoom) y comprime. No hace falta rehacer el catálogo a mano: casi siempre se automatiza.
4. **Activa formatos modernos (WebP / AVIF)**: en Shopify, el CDN ya sirve WebP/AVIF automáticamente si usas las imágenes del tema con los filtros de imagen de Liquid (`image_url` con ancho); en WordPress/WooCommerce usa un plugin de optimización (p. ej. ShortPixel, Imagify, EWWW o la función nativa de tu plataforma de caché/CDN) y activa la conversión masiva del catálogo existente.
5. **Sirve tamaños distintos por dispositivo (`srcset` + `sizes`)**: comprueba en el código de la ficha que la imagen lleva `srcset` y `sizes`, de modo que el móvil descargue una versión de ~400-800 px de ancho. En WordPress, el núcleo lo genera solo si las imágenes se insertan con el sistema de medios; en Shopify, usa varios anchos con `image_url`.
6. **Reserva el espacio de cada imagen**: añade siempre `width` y `height` (o `aspect-ratio` en CSS) para evitar que la página salte al cargar (CLS).
7. **No retrases la foto principal**: la primera imagen visible de la ficha NO debe llevar `loading="lazy"` (usa `fetchpriority="high"` en ella). El lazy loading solo para las que quedan fuera de la primera pantalla.
8. **Valida y vigila**: vuelve a pasar PageSpeed Insights en móvil y, pasadas 2-4 semanas, revisa el informe de Core Web Vitals en Search Console (los datos reales tardan en actualizarse). Añade el peso de imagen al QA de cada colección o cambio de plantilla.

**Herramientas usadas**: PageSpeed Insights, Chrome DevTools (pestaña Red y Lighthouse), informe de Core Web Vitals de Search Console, y un plugin de optimización de imágenes (WordPress) o el CDN de imágenes de Shopify.

---
