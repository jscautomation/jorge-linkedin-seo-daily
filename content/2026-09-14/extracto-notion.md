# Estás perdiendo ventas en móvil (y tu web no tiene ningún error)
**14 de septiembre de 2026 — Pilar: Velocidad y experiencia móvil**

## Diagnóstico

Un patrón muy habitual en auditorías de ecommerce: la ficha de producto (o
la portada de categoría) tiene buen contenido, buen SEO on-page, sin
errores en Search Console... y aun así tarda "un instante de más" en
mostrar la foto principal al abrir en móvil.

La causa casi siempre es la misma: la imagen principal de la página —la
que el usuario ve nada más entrar, la que decide si sigue mirando o se
va— tiene aplicada la carga diferida (`loading="lazy"`), una técnica
pensada para las imágenes que están más abajo en la página (para no
descargarlas hasta que el usuario llegue a esa zona), pero mal aplicada
también a la imagen que debería cargar la primera y más rápido.

## Por qué importa en términos de negocio

Esa imagen es, en la inmensa mayoría de plantillas de ecommerce, el
elemento LCP (Largest Contentful Paint) de la página — la métrica con la
que Google mide cuánto tarda en aparecer el contenido principal, y una de
las tres Core Web Vitals que Google usa como señal de ranking desde 2021.
El umbral que Google considera "bueno" es 2,5 segundos; superarlo empeora
la puntuación de Core Web Vitals de esa URL.

Pero el impacto real es antes de que Google entre en juego: el propio
cliente ve una foto que tarda en aparecer y, en muchos casos, se va antes
de que termine de cargar. Según datos de Akamai, un retraso de solo 100
milisegundos en el tiempo de carga puede reducir la conversión hasta un
7%. Eso es venta que se pierde en el propio momento de decisión de compra
— antes incluso de discutir tráfico o posicionamiento.

## Solución paso a paso

1. **Identifica el elemento LCP real de la página.** En Chrome DevTools
   (pestaña Performance, o Lighthouse) o en PageSpeed Insights
   (pagespeed.web.dev), analiza la URL de una ficha de producto y una de
   categoría representativas, en modo móvil. El informe señala
   explícitamente qué elemento es el LCP.
2. **Comprueba si ese elemento lleva `loading="lazy"`.** Basta con
   inspeccionar el HTML (clic derecho → Inspeccionar, o "Ver código
   fuente") y buscar el atributo en la etiqueta `<img>` correspondiente. Si
   la imagen se genera con un carrusel/slider de JS, revisa también si el
   propio slider retrasa la carga de la primera slide hasta que se
   inicializa el script.
3. **Quita `loading="lazy"` (o pon `loading="eager"`) únicamente en la
   imagen LCP** de cada plantilla afectada (ficha de producto, cabecera de
   categoría). El resto de imágenes de la página —las que sí están fuera
   de la vista inicial— deben mantener `loading="lazy"`; el objetivo no es
   eliminar el lazy loading, es dejar de aplicarlo a lo que se ve primero.
   En WordPress/WooCommerce, revisa si el propio tema o un plugin de
   optimización de imágenes está forzando `loading="lazy"` de forma
   global sin excepción para la imagen destacada; en Shopify, revisa el
   snippet de la plantilla del producto (`main-product.liquid` o
   equivalente) y del tema de la colección.
   Adicionalmente, añade `fetchpriority="high"` a esa misma imagen LCP —
   es la señal complementaria que recomienda Google para que el navegador
   la priorice también en la cola de descarga, no solo evitar el retraso
   del lazy loading.
4. **Vuelve a medir con PageSpeed Insights** (datos de laboratorio,
   inmediatos) y, pasadas 2-4 semanas, con el informe de Core Web Vitals
   de Search Console (datos de campo, de usuarios reales) para confirmar
   la mejora del LCP en móvil.
5. **Añade esta comprobación al QA de cualquier cambio de tema o
   plantilla** — es un error que reaparece fácilmente tras una
   actualización de tema, un cambio de plugin de imágenes o una migración,
   sin que nadie lo note hasta la siguiente auditoría.

## Herramientas usadas

- Chrome DevTools (pestaña Performance) / Lighthouse
- PageSpeed Insights (pagespeed.web.dev)
- Search Console → Core Web Vitals (informe de campo)
- Inspección manual del HTML servido (código fuente de la página)

---
