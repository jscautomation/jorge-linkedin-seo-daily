# Mejora nº23: Redirecciones por JavaScript en migraciones — Google no las ve a tiempo (25/09/2026)

**Contexto / diagnóstico**

Es un fallo muy habitual en migraciones de plataforma (Prestashop/WooCommerce → Shopify, o cualquier cambio de dominio): el equipo que ejecuta la migración implementa las redirecciones de las URLs antiguas a las nuevas con JavaScript (`window.location.href = "..."` o un `meta refresh`) en vez de con una redirección 301 real a nivel de servidor. Al probarlo en el navegador "funciona" — el usuario acaba en la página correcta — así que nadie lo detecta como un problema hasta semanas después, cuando el tráfico orgánico no remonta.

**Por qué importa en términos de negocio**

Una redirección de servidor (301) transfiere el posicionamiento acumulado de la URL antigua a la nueva en el siguiente rastreo de Google. Una redirección hecha solo con JavaScript depende de que Googlebot ejecute ese JavaScript, lo cual ocurre en una segunda fase de rastreo, mucho más lenta e irregular que el procesado de HTML — puede tardar semanas en producirse, o no llegar a ocurrir en absoluto en el primer rastreo tras la migración. Mientras tanto: la URL antigua pierde posiciones porque ya no existe o devuelve error, la URL nueva no hereda ese posicionamiento porque Google no ha "visto" todavía la redirección, y ese hueco en el SERP lo ocupa la competencia. El resultado es tráfico orgánico y ventas que se quedan parados durante semanas o meses después de un lanzamiento que, sobre el papel, ya estaba "migrado".

**Solución paso a paso**

1. **Verifica cómo responde realmente cada URL antigua**, sin ejecutar JavaScript: usa `curl -I` (o Screaming Frog en modo "solo texto/HTML", sin renderizado JS) contra una muestra de URLs antiguas conocidas. Si el código de respuesta HTTP no es `301` (o `308`) apuntando directamente a la URL nueva, la redirección no es válida para SEO, aunque en el navegador parezca funcionar.
2. **Identifica dónde vive la redirección por JavaScript** — normalmente en el propio HTML de una página "puente" que el servidor sigue sirviendo con código 200, con un script que hace `window.location` o un `<meta http-equiv="refresh">`. Localiza el punto exacto (tema/plantilla, plugin, regla del CDN) donde se generó así en vez de a nivel de servidor.
3. **Sustitúyela por una redirección 301 real**, implementada en el nivel más bajo posible de la pila: reglas del servidor web (Nginx/Apache), configuración de la plataforma (por ejemplo, el gestor de redirecciones nativo de Shopify/WooCommerce), o el CDN/proxy (Cloudflare, etc.) — nunca en el HTML/JavaScript de la propia página.
4. **Mapea 1:1, nunca por patrón genérico**: cada URL antigua debe apuntar a su equivalente real en la web nueva (mismo producto/categoría), no a la home ni a una regla comodín — un 301 a una página no equivalente lo trata Google más como un "soft 404" que como un traspaso de autoridad real.
5. **Confirma el rastreo real en Search Console**: usa la Inspección de URLs sobre una muestra de URLs antiguas para comprobar que Google ya ve el 301 de servidor (no la versión JavaScript), y vigila la cobertura/indexación de las URLs nuevas en las semanas siguientes.
6. **Añade esta comprobación al checklist de QA de cualquier migración futura** — probarlo "a mano" en el navegador no es suficiente, porque ahí el JavaScript sí se ejecuta; solo una comprobación del código de respuesta HTTP real (sin JS) detecta el problema.

**Herramientas usadas para detectarlo/arreglarlo**

- `curl -I` (o cualquier cliente HTTP) para ver el código de respuesta real de cada URL, sin ejecutar JavaScript
- Screaming Frog en modo de rastreo solo-HTML (sin renderizado JS) para auditar en volumen
- Google Search Console → Inspección de URLs, para confirmar qué ve realmente Googlebot
- Reglas de redirección a nivel de servidor/CDN (Nginx, Apache, o el gestor nativo de la plataforma de ecommerce) para implementar el 301 real

---
