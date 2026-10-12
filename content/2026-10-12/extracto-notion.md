## Tu Black Friday empieza de cero cada año — 12/10/2026

**Contexto / diagnóstico**: muchas tiendas montan cada campaña estrella con una URL nueva (`/black-friday-2025`, `/black-friday-2026`...). La del año anterior se borra, se redirige a la home o se queda huérfana. Cada noviembre, Google se encuentra una página sin historial, sin enlaces entrantes y sin antigüedad, mientras la competencia que mantiene la misma dirección año tras año llega con la autoridad acumulada de todas las campañas anteriores.

**Por qué importa en términos de negocio**: Black Friday concentra las semanas de más demanda del año. Una página de campaña que parte de cero tarda en posicionar, y cuando lo hace la campaña ya ha pasado: ese tráfico orgánico (gratis) y esas ventas se las lleva quien sí tiene historial, y tú compensas con más gasto en anuncios.

**Solución paso a paso**:

1. **Decide una única URL permanente** para la campaña, sin año: `/black-friday/` (lo mismo para Navidad, rebajas, etc.). Esa dirección será la misma cada temporada.
2. **Recupera el historial**: comprueba qué responden hoy las URLs de campañas anteriores (Screaming Frog o `curl -I`). Si devuelven 404 o redirigen a la home, y tenían enlaces entrantes (Search Console > Enlaces, o una herramienta de backlinks), redirige con un 301 en un solo salto a la URL permanente.
3. **Actualiza el contenido, no la dirección**: cada año cambia ofertas, fechas, título y productos destacados sobre la misma URL. Indica la edición actual en el `title` y el H1 (p. ej. "Black Friday 2026") sin cambiar la ruta.
4. **Mantenla viva todo el año**: no la despubliques al terminar. Déjala accesible con un mensaje tipo "Próximo Black Friday: apúntate al aviso" y enlázala desde el pie o el menú para que conserve enlaces internos y rastreo.
5. **Publícala con margen**: ten la página actualizada y enlazada desde la home y las categorías clave varias semanas antes del arranque, no la semana previa, para dar tiempo a Google a recrawlear.
6. **Pide el recrawl**: tras actualizarla, usa Inspección de URLs > Solicitar indexación en Search Console y revisa que el sitemap la incluye.
7. **Mide y repite**: compara impresiones y clics de la URL por campaña en Search Console y añade esta revisión al calendario de cada campaña estacional.

**Herramientas usadas**: Screaming Frog (códigos de respuesta y enlaces internos), Google Search Console (Enlaces, Inspección de URLs, Rendimiento), `curl -I`, y una herramienta de backlinks (Ahrefs, Semrush o similar).

---
