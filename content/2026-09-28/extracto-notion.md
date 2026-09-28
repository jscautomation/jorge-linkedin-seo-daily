## Estás perdiendo ventas en móvil — 28/09/2026

**Contexto / diagnóstico**: en fichas de producto de varios ecommerce de moda, elementos que se cargan después del contenido principal — el aviso de "quedan pocas unidades", el banner de cookies, el widget de chat en vivo — no tienen su espacio reservado de antemano. Cuando terminan de cargar, empujan el resto de la página hacia abajo. Si ese salto coincide con el instante en que el comprador, en móvil, va a pulsar "añadir al carrito", el dedo aterriza sobre otro elemento: cambia de producto, cierra el aviso, abre el chat, o simplemente pierde el hilo y abandona.

Esto tiene nombre técnico: **Cumulative Layout Shift (CLS)**, uno de los tres Core Web Vitals de Google (junto a LCP e INP), que mide precisamente cuánto se mueve el contenido visible de una página mientras carga.

**Por qué importa en términos de negocio**: la mayoría del tráfico de un ecommerce entra por móvil, así que un CLS alto no es un detalle de estilo — es fricción justo en el paso de mayor intención de compra (añadir al carrito, cambiar talla/color, confirmar checkout). Cada toque accidental es, en la práctica, una venta que se cae sin que salte ninguna alarma en ningún informe: no es un error 500, no rompe el checkout, simplemente el comprador se frustra y se va. Google, además, lo mide como señal de Page Experience — su propia investigación indica que las páginas que cumplen el umbral recomendado de CLS (por debajo de 0,1) registran un 24% menos de abandono de carga por parte de los usuarios.

**Solución paso a paso**:

1. **Medir el problema real**: abrir PageSpeed Insights (o el informe de Core Web Vitals de Search Console) para las plantillas de ficha de producto y categoría, filtrando por móvil, y anotar la puntuación de CLS actual (objetivo: por debajo de 0,1).
2. **Reproducir el salto con las herramientas de desarrollador de Chrome**: en la pestaña "Performance", grabar la carga de una ficha de producto en emulación móvil y activar la superposición de "Layout Shift Regions" — Chrome resalta en la propia pantalla qué elemento se movió y en qué instante.
3. **Identificar el elemento culpable** entre los sospechosos habituales de ecommerce: avisos de stock/urgencia inyectados por JavaScript, banners de cookies o consentimiento, widgets de chat de terceros, carruseles de "productos recomendados" y anuncios/píxeles de marketing que se cargan de forma asíncrona.
4. **Reservar el espacio de cada elemento antes de que cargue**: fijar un `min-height` (o un tamaño explícito) en el contenedor del banner/aviso/widget igual al que ocupará una vez cargado, para que su aparición no desplace nada a su alrededor. Para imágenes de producto, fijar siempre los atributos `width`/`height` (o `aspect-ratio` en CSS) en el HTML.
5. **Cargar los elementos no críticos sin bloquear ni desplazar el contenido principal**: usar `font-display: optional` o precargar las fuentes de marca (para evitar el salto al sustituir la fuente por defecto), y cargar chat/banners de forma diferida pero dentro de un contenedor ya reservado, nunca insertándolos "a la fuerza" en el flujo del documento.
6. **Revalidar**: volver a medir con PageSpeed Insights/Search Console 2-4 semanas después del cambio, confirmando que el CLS de las plantillas afectadas baja de 0,1, y comprobar en analítica si baja la tasa de abandono de carrito en móvil en ese mismo periodo.

**Herramientas usadas**: PageSpeed Insights, Google Search Console (informe de Core Web Vitals), Chrome DevTools (pestaña Performance con "Layout Shift Regions").

---
