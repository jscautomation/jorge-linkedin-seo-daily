## Lanzaste tu tienda nueva... y Google sigue sin enterarse — 17/10/2026

**Contexto / diagnóstico**: en un rediseño o migración de tienda, el nuevo sitio se construye en un entorno de pruebas (staging) que se protege para que Google no lo indexe: etiqueta `noindex`, cabecera `X-Robots-Tag: noindex`, bloqueo total en `robots.txt` (`Disallow: /`), la casilla "Disuadir a los motores de búsqueda" de WordPress o la protección con contraseña/modo privado de Shopify. El día del lanzamiento se copia el sitio a producción y alguna de esas protecciones viaja con él. La tienda funciona perfecta para quien llega por anuncios, email o redes, pero Google deja de mostrarla en sus resultados, poco a poco y sin ningún aviso visible.

**Por qué importa en términos de negocio**: es tráfico orgánico que ya compraba y que desaparece justo en la semana en que más inviertes en promocionar el lanzamiento. Cada categoría que cae del buscador son ventas regaladas a la competencia, y recuperar las posiciones tras desindexarse tarda bastante más que perderlas. Lo descubres cuando el informe mensual sale en rojo, no antes.

**Solución paso a paso**:

1. **Comprueba el código de la página**: abre la home y una categoría en producción, pulsa "Ver código fuente" y busca `noindex`. Si aparece en `<meta name="robots">`, hay que quitarlo.
2. **Comprueba las cabeceras HTTP**: con la herramienta de inspección de URL de Search Console (o `curl -I` sobre la URL) busca `X-Robots-Tag: noindex`. Suele venir del servidor o de un plugin/CDN, no del código de la página.
3. **Revisa `robots.txt`**: abre `tutienda.com/robots.txt`. Si ves `Disallow: /` para todos los agentes, sustitúyelo por el robots.txt de producción (permite rastrear categorías y fichas; bloquea solo carrito, checkout y cuenta).
4. **Revisa los ajustes de plataforma**: en WordPress, Ajustes → Lectura → desmarca "Disuadir a los motores de búsqueda de indexar este sitio" (y revisa el plugin SEO: Yoast, Rank Math...). En Shopify, comprueba que la tienda no está protegida con contraseña (Preferencias → Protección con contraseña) y que ninguna plantilla/app añade `noindex` global.
5. **Inspecciona URLs clave en Search Console**: usa "Inspección de URLs" en la home, 2-3 categorías y 2-3 fichas top. Debe poner "La URL puede aparecer en Google". Pulsa "Solicitar indexación" en las más importantes una vez corregido.
6. **Comprueba el sitemap**: debe estar enviado en Search Console, apuntar al dominio de producción (no al de staging) y no contener URLs con noindex ni redirigidas.
7. **Protege el staging para siempre**: déjalo detrás de usuario y contraseña (no solo `noindex`), con un dominio distinto, y nunca copies archivos de configuración de robots/SEO de staging a producción. Añade a la lista de pasos de cada lanzamiento un "check de indexabilidad" firmado por alguien.
8. **Vigila las dos semanas siguientes**: informe de "Páginas" y de "Rendimiento" en Search Console cada pocos días; si las impresiones caen en picado tras el lanzamiento, vuelve a los puntos 1-4 antes que a cualquier otra hipótesis.

**Herramientas usadas**: Google Search Console (Inspección de URLs, informe de Páginas, Rendimiento, Sitemaps), código fuente del navegador, `curl -I` o la extensión de cabeceras del navegador, Screaming Frog (rastreo de producción buscando directivas noindex), ajustes de WordPress/Shopify.

---
