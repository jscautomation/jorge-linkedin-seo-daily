## Te buscan por foto y no te encuentran — 11/10/2026

**Contexto / diagnóstico**: cada vez más compradores buscan con una imagen (Google Lens, Google Imágenes, la pestaña "Imágenes" del buscador) en lugar de con palabras, sobre todo en moda y producto muy visual. Muchas tiendas suben sus fotos con nombres de cámara o de proveedor (`IMG_4532.jpg`), con el texto alternativo (`alt`) vacío o repetido en todas las fotos de la ficha, con galerías que cargan las imágenes solo mediante JavaScript, o con archivos de varios MB que ralentizan la página. Para Google, la foto es entonces un archivo sin contexto.

**Por qué importa en términos de negocio**: es tráfico con intención de compra que no pagas por clic: la persona llega con el producto ya en la cabeza. Si tus fotos no se pueden entender ni encontrar, esas visitas y esas ventas las capta la competencia que sí ha trabajado sus imágenes, y tus informes lo mezclan con el resto de tráfico, así que no se nota que falta.

**Solución paso a paso**:

1. **Mide el punto de partida**: en Search Console > Rendimiento > Resultados de búsqueda, filtra por tipo de búsqueda "Imagen" y mira cuántos clics e impresiones recibes. Haz también una búsqueda en Google Imágenes de tus 5-10 productos más vendidos (marca + modelo y descripción genérica) y anota si aparecen tus fotos.
2. **Prioriza**: empieza por los 20 productos más vendidos o con más margen, y por las fotos principales de cada ficha. No hace falta tocar todo el catálogo de golpe.
3. **Nombra bien los archivos**: descriptivos, en minúsculas, separados por guiones y con el idioma del mercado: `vestido-lino-mujer-azul-marino-frontal.jpg`, no `IMG_4532.jpg` ni `foto-final-2.jpg`. Hazlo al subir y, en catálogos grandes, con un renombrado masivo o la función de tu plataforma.
4. **Escribe un `alt` útil y distinto por foto**: describe lo que se ve (producto, color, ángulo o detalle) en una frase corta natural. Evita rellenar con palabras clave y evita repetir el mismo texto en todas las fotos de la ficha. Las imágenes puramente decorativas pueden llevar `alt=""`.
5. **Comprueba que Google ve las imágenes**: abre la ficha con "Ver código fuente" y confirma que las fotos están en el HTML como `<img>` (o `<picture>`) con su `src`. Si una galería las carga solo al hacer clic o con JavaScript, pide a desarrollo que las incluya en el HTML inicial. Verifícalo también con "Inspección de URL > Probar URL publicada" en Search Console.
6. **Optimiza peso y formato**: exporta en WebP (o AVIF) con compresión razonable, ajusta las dimensiones al tamaño real de uso y mantén ligeras las imágenes principales (como referencia, del orden de 200-300 KB). La imagen principal de la ficha no debe llevar `loading="lazy"`; sí las de más abajo.
7. **Refuerza el contexto**: coloca las fotos cerca del título y del texto del producto, añade la imagen principal en el marcado `Product` (`image`) y, si usas Merchant Center, comprueba que la `image_link` del feed sea una imagen nítida de producto sin textos ni marcas de agua.
8. **Incluye las imágenes en el rastreo**: asegúrate de que `robots.txt` no bloquea las carpetas de imágenes y valora añadirlas al sitemap (o usar un sitemap de imágenes si tu plataforma no las incluye).
9. **Vuelve a medir**: pasadas 4-8 semanas, repite el paso 1 y compara clics e impresiones de búsqueda de imagen de esas fichas.

**Herramientas usadas**: Search Console (Rendimiento por tipo de búsqueda "Imagen", Inspección de URL), búsqueda en Google Imágenes y Google Lens, "Ver código fuente" del navegador, PageSpeed Insights, y una herramienta de compresión/conversión de imágenes (Squoosh o el plugin/app de tu plataforma). Con un rastreador tipo Screaming Frog se puede auditar de golpe qué imágenes carecen de `alt` o pesan demasiado.

---
