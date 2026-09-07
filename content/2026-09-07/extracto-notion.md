## Tu tienda no existe en 3 países (07/09/2026)

**Contexto:** Un ecommerce que vende en varios mercados (España, Francia,
Italia, por ejemplo) traduce su web a cada idioma y da por hecho que ya
"está" en esos países. En bastantes auditorías internacionales aparece
siempre el mismo fallo, invisible desde dentro: la web detecta la IP del
visitante y le redirige automáticamente a la versión de "su" país (o le
fuerza a elegir antes de ver nada) — y aplica exactamente la misma lógica a
los rastreadores de buscadores. Como la inmensa mayoría del rastreo real de
Google llega desde direcciones IP de EE.UU., Googlebot entra, es
redirigido a la versión por defecto (normalmente la de origen de la marca)
y nunca llega a descubrir ni rastrear el resto de versiones — aunque estén
online, bien traducidas y enlazadas desde el propio sitio.

**Por qué importa (en términos de negocio):** El resultado no es "menos
optimización" en esos mercados: es tráfico orgánico cero en países donde el
ecommerce ya vende y ya ha invertido en traducir y adaptar el catálogo. Cada
mercado bloqueado de esta forma solo puede captar clientes vía pago (ads) o
tráfico de marca ya existente — nunca por búsqueda orgánica de producto o
categoría, que es precisamente el tráfico más barato y más escalable a
medio plazo. Cuantos más países tenga la tienda en esta situación, mayor la
dependencia de medios de pago para sostener la facturación internacional, y
menor el retorno de la inversión ya hecha en localizar el contenido.

**Solución paso a paso:**
1. Comprueba primero si la redirección es realmente automática (sin
   posibilidad de acceder directo a otra versión) o solo una sugerencia que
   el usuario puede descartar — la automática y forzada es la que bloquea
   el rastreo; una sugerencia con opción de "seguir en este país" no lo
   hace, siempre que el enlace a cada versión siga siendo accesible.
2. Verifica el comportamiento real usando un rastreador (Screaming Frog u
   otro) configurado con el user-agent de Googlebot y, si es posible,
   simulando una IP de EE.UU. (con un proxy o VPN) — así se ve exactamente
   lo que ve el bot real, no lo que ve un visitante desde España.
3. Elimina la redirección forzada del lado servidor/JavaScript: todas las
   versiones de país/idioma deben ser accesibles directamente por URL, sin
   redirect automático, tanto para usuarios como para bots. Sustitúyela,
   si Jorge quiere mantener algo de personalización, por un banner
   descartable que sugiere el cambio de país sin bloquear el acceso a la
   versión solicitada.
4. Implementa hreflang recíproco completo en todas las páginas equivalentes
   (incluyendo self-referencing y la etiqueta x-default) como la señal
   correcta para indicar a Google qué versión servir a cada
   idioma/región — es el mecanismo pensado para esto, no el redirect.
5. Añade un selector de país/idioma visible y enlazado en el pie o cabecera
   de la web, con enlaces reales (no solo JavaScript que dispare otro
   redirect) a cada versión — da a Google (y a los usuarios) una vía de
   descubrimiento adicional independiente del hreflang.
6. Pasadas 2-4 semanas del cambio, revisa en Google Search Console (una
   propiedad por dominio/subcarpeta si aplica) la cobertura de rastreo e
   impresiones por país en cada versión de idioma, para confirmar que
   Google ha empezado a rastrear e indexar los mercados antes bloqueados.

**Herramientas usadas:** Screaming Frog (con user-agent de Googlebot y,
opcionalmente, IP de EE.UU. vía proxy/VPN, para simular el rastreo real),
un validador de hreflang (para confirmar reciprocidad y x-default),
Google Search Console (cobertura e impresiones por país/idioma), y revisión
manual navegando la web con distintas IPs/ubicaciones.

---
