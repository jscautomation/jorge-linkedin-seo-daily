## Tus mejores enlaces están apuntando a un error 404 — 15/10/2026

**Contexto / diagnóstico**: tras un rediseño, una migración de plataforma o un cambio de estructura de URLs, muchas tiendas conservan en internet enlaces de blogs, prensa, directorios y colaboraciones que apuntan a direcciones antiguas. Si esas URLs ahora devuelven un 404 (o redirigen a la home en lugar de a la página equivalente), Google no traspasa a la página nueva la autoridad de esos enlaces, y las personas que los pulsan aterrizan en un error.

**Por qué importa en términos de negocio**: pierdes dos fuentes de ventas a la vez: el tráfico de referencia (gente que llega recomendada y con intención de compra) y la autoridad que ayuda a tus categorías y fichas a posicionar en Google. Es tráfico gratuito que ya te ganaste y que se desperdicia sin ninguna alerta: la web funciona, el checkout funciona, simplemente vendes menos de lo que te corresponde.

**Solución paso a paso**:

1. **Saca la lista de URLs con enlaces externos**: en Google Search Console > Enlaces > Enlaces externos > Páginas de destino principales, y complétala con una herramienta de backlinks (Ahrefs, Semrush u otra) filtrando por URLs de tu dominio con enlaces entrantes.
2. **Comprueba qué responde cada una**: pasa la lista por Screaming Frog (modo lista) o `curl -I` y marca las que devuelven 404/410, o las que redirigen a la home o a una página sin relación.
3. **Prioriza por valor**: ordena por número de dominios que enlazan y por calidad del sitio de origen (prensa, medios del sector, blogs con tráfico). Empieza por las 20 principales: suelen concentrar la mayor parte del valor.
4. **Decide el destino de cada una**: si la página equivalente existe, redirige con un 301 en un solo salto, URL a URL. Si el producto ya no existe, redirige a la categoría más cercana o al sustituto real. No mandes todo a la home: Google lo trata como un soft 404 y no traspasa la autoridad.
5. **Implementa las redirecciones a nivel de servidor/CDN o plugin de redirecciones** (no con JavaScript), y prueba cada una con `curl -I` para confirmar el 301 real.
6. **Pide la actualización del enlace en los casos clave**: escribe a los pocos medios o socios más importantes para que apunten a la URL actual. Sigue siendo útil aunque el 301 ya funcione.
7. **Verifica y repite**: en Search Console > Inspección de URLs comprueba que Google ve el 301, y repite la revisión tras cada rediseño o migración, y cada 6 meses.

**Herramientas usadas**: Google Search Console (Enlaces, Inspección de URLs), Screaming Frog (modo lista), `curl -I`, y una herramienta de backlinks (Ahrefs, Semrush o similar).

---
