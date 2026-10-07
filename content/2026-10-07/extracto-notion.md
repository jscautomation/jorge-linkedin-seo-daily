## Tus categorías no venden porque Google no entiende dónde están tus productos — 07/10/2026

**Contexto / diagnóstico**: en muchas tiendas la ficha de producto no tiene migas de pan (Inicio > Mujer > Vestidos > Vestido de lino), o están pintadas solo con CSS/JavaScript sin enlaces `<a href>` reales, o no llevan el marcado `BreadcrumbList`. Otras veces la miga cambia según desde dónde llegó el usuario (desde una oferta, desde el buscador interno...) y nunca apunta a la categoría principal. Así, la ficha no devuelve ningún enlace interno estable a su categoría, y Google entiende peor cómo se organiza el catálogo. Además, en el resultado de búsqueda muestra una URL cruda en lugar de una ruta legible.

**Por qué importa en términos de negocio**: las categorías son las páginas con más volumen de búsqueda y más intención de compra de la tienda ("vestidos de lino mujer"). Si cientos de fichas no les enlazan de vuelta, reciben menos fuerza interna, posicionan menos y venden menos. Y en el resultado, una ruta clara ("tienda.com › Mujer › Vestidos") genera más confianza que una URL con parámetros. No salta ninguna alarma: la ficha carga y el checkout funciona.

**Solución paso a paso**:

1. **Comprueba lo que ve Google**: abre 3-4 fichas de distintas categorías, mira el código fuente (Ctrl+U, no el inspector) y busca la miga. ¿Existe como lista de enlaces `<a href>` reales? ¿O solo aparece tras cargar JavaScript?
2. **Define una única ruta principal por producto**: aunque el producto esté en varias categorías (p. ej. "Mujer > Vestidos" y "Ofertas"), la miga debe seguir siempre la ruta de la categoría principal, no la ruta por la que llegó el usuario.
3. **Haz que la miga sean enlaces reales** en el HTML servido: cada nivel (menos el último, que es la propia ficha) enlaza a su categoría con URL limpia y texto descriptivo (no "Atrás" ni "Volver").
4. **Añade el marcado `BreadcrumbList` en JSON-LD** con los mismos niveles, nombres y URLs que la miga visible (`itemListElement`, `position`, `name`, `item`). Debe coincidir con lo que se ve en la página.
5. **Implántalo en la plantilla**, no ficha a ficha. En Shopify/WooCommerce, revisa si el tema ya lo trae (muchos lo traen incompleto) o añádelo con un snippet/plugin de SEO, evitando duplicar el marcado con dos fuentes distintas.
6. **Valida**: Prueba de Resultados Enriquecidos de Google con 3-4 URLs de producto y de categoría, y el informe de "Migas de pan" en Search Console (aparece cuando Google las detecta).
7. **Revisa en 3-4 semanas** impresiones y posiciones de tus categorías clave en Search Console, y añade la comprobación al QA de cualquier cambio de tema o plantilla.

**Herramientas usadas**: código fuente del navegador (Ctrl+U), Screaming Frog (modo solo HTML, extracción personalizada de la miga y enlaces internos entrantes a categorías), Prueba de Resultados Enriquecidos de Google, Search Console.

---
