## Estás regalando ventas a tu competencia — 30/09/2026

**Contexto / diagnóstico**: en categorías con catálogos grandes (moda, calzado, hogar), el comprador ve el catálogo completo, pero Google puede quedarse solo con la primera página. Cuatro causas habituales: (1) botón "cargar más" o scroll infinito que solo añade productos con JavaScript y sin URL propia por tramo; (2) páginas 2, 3, 4… con un canonical que apunta a la página 1; (3) páginas siguientes sin enlaces `<a href>` reales (solo botones); (4) páginas 2+ con `noindex` por miedo al contenido duplicado. El efecto común: los productos que solo cuelgan de esas páginas pierden su puerta de entrada desde la categoría.

**Por qué importa en términos de negocio**: cada producto que Google no descubre o no rastrea con facilidad es una venta de tráfico orgánico (gratis) que no ocurre, y que se lleva la competencia que sí muestra ese catálogo. Afecta sobre todo a la cola larga y a las colecciones grandes. No salta ninguna alarma: la web carga y el checkout funciona, simplemente vendes menos de lo que podrías.

**Solución paso a paso**:

1. **Medir el alcance**: en Search Console (informe de páginas) y con `site:tudominio.com/categoria/` comprueba cuántas fichas de una categoría grande están indexadas frente a las que realmente tiene. Si faltan muchas, sospecha de paginación.
2. **Comprobar qué ve Google sin JavaScript**: en Screaming Frog (modo solo HTML) rastrea una categoría grande y comprueba si llega a las fichas del fondo. Con `curl` o "Ver código fuente" mira si hay enlaces reales a la página siguiente.
3. **Dar a cada tramo su propia URL**: si usas "cargar más" o scroll infinito, mantén por debajo URLs paginadas (`?page=2` o `/page/2/`) accesibles y rastreables; Google no pulsa botones ni hace scroll, y su documentación recomienda que el contenido cargado bajo demanda tenga URL propia.
4. **Enlaces reales**: la navegación a la página siguiente debe ser un `<a href="...">`, no un botón con evento JavaScript, y las páginas profundas deben alcanzarse en pocos clics (enlaces a primera, última y rangos cercanos).
5. **Canonical a sí misma**: cada página paginada (2, 3, 4…) lleva un canonical que apunta a su propia URL, nunca a la página 1. Solo si ofreces una vista "ver todo" completa y rápida tiene sentido apuntar a ella.
6. **Sin `noindex` en las páginas 2+**: déjalas indexables para que los enlaces a las fichas se sigan y las fichas se descubran. Evita bloquearlas por robots.txt.
7. **Verificar**: Inspección de URLs en Search Console sobre una página 2 y otra profunda (canonical declarado vs. elegido por Google, indexabilidad), y revisa semanas después si aumentan las fichas indexadas de esa categoría.
8. **Automatizar el control**: añade esta revisión al QA de cualquier cambio de tema/plantilla o de los filtros.

**Herramientas usadas**: Google Search Console (informe de páginas, Inspección de URLs), Screaming Frog (modo solo HTML), operador `site:` y vista de código fuente / `curl`.

---
