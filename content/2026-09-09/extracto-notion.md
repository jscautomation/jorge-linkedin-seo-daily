## Producto nuevo a la venta. Google no sabe. (09/09/2026)

**Contexto/diagnóstico:** En ecommerce con catálogo que rota con frecuencia
(temporada, colección, reposiciones), es habitual encontrar en auditoría que
un producto recién publicado tarda días, a veces semanas, en ser rastreado
e indexado por Google — justo la ventana en la que más gente lo busca por
su nombre, tras verlo en la web, en email o en redes. La causa casi nunca
es un bloqueo explícito (robots.txt, noindex): es que `sitemap.xml` se
genera solo una vez al día, o incluso manualmente, y además sigue lleno de
URLs de productos agotados o descatalogados desde hace meses. Google
reparte su presupuesto de rastreo revisando ese catálogo "fantasma" en vez
de descubrir cuanto antes la ficha nueva, que muchas veces tampoco recibe
ningún enlace interno (desde portada, categoría o newsletter) el mismo día
del lanzamiento — su único camino de descubrimiento queda siendo un
sitemap que no se ha actualizado todavía.

**Por qué importa (en términos de negocio):** El lanzamiento de un producto
tiene una ventana de interés muy concentrada en los primeros días — es
cuando más volumen de búsqueda directa genera (por nombre de producto,
campaña o colección). Si Google no ha indexado la ficha para entonces, ese
tráfico de mayor intención de compra no tiene dónde aterrizar por vía
orgánica, y se reparte entre lo que ya esté posicionado — la competencia
que sí tiene su versión indexada, o directamente inversión en Ads para
cubrir el hueco. La misma inversión ya hecha en fotografiar, describir y
promocionar el lanzamiento pierde su tramo de retorno más alto: la primera
semana.

**Solución paso a paso:**
1. Confirma la frecuencia real de generación del sitemap (revisa la
   cabecera `Last-Modified` del propio `sitemap.xml`, o el ajuste del
   plugin/módulo que lo genera en WordPress/Shopify) — si es una vez al día
   o manual, un producto publicado por la tarde puede no aparecer hasta el
   día siguiente como mínimo.
2. Cambia la generación a dinámica/on-demand (la mayoría de plugins de SEO
   de WordPress y el sitemap nativo de Shopify se actualizan solos al
   publicar; si el sitemap es un archivo estático generado por cron,
   reduce el intervalo o dispáralo también al publicar producto).
3. Audita el sitemap actual con un rastreador (Screaming Frog, lista de
   URLs del propio `sitemap.xml`) cruzando contra el catálogo real: elimina
   las URLs de productos agotados sin fecha de vuelta y descatalogados —
   pasándolas a 410 o excluyéndolas del sitemap, según el caso — para que
   Google no gaste presupuesto de rastreo revisándolas.
4. El día del lanzamiento, añade el producto nuevo al enlazado interno real
   (categoría correspondiente, bloque de "novedades" en portada, y
   cualquier newsletter/campaña que lo mencione con enlace directo) — no
   dependas solo del sitemap como vía de descubrimiento.
5. En Google Search Console, usa la inspección de URL para solicitar
   indexación manual de los lanzamientos más importantes el mismo día de
   publicación, como capa adicional (no sustituye los pasos anteriores,
   ayuda a acelerar el primer rastreo).
6. Mide el tiempo real hasta la primera indexación en los próximos
   lanzamientos (fecha de publicación vs. fecha de primera aparición en
   Search Console/búsqueda) para confirmar que el cambio ha reducido esa
   ventana.

**Herramientas usadas:** Screaming Frog (auditoría del sitemap y cruce con
catálogo real), el plugin/módulo de sitemap de la plataforma
(WordPress/Shopify), Google Search Console (inspección de URL e informe de
cobertura), y revisión manual del enlazado interno el día de cada
lanzamiento.

---
