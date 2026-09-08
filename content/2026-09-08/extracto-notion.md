## Te quitaron tus estrellas en Google (08/09/2026)

**Contexto:** Muchas fichas de producto muestran un rich snippet de
valoraciones (las estrellas amarillas junto al resultado) gracias al marcado
`Review`/`AggregateRating`. El 24 de julio de 2026, Google revisó en
silencio los requisitos de este marcado para endurecer dos prácticas
habituales en ecommerce: (1) las reseñas "self-serving" — donde la propia
marca controla y publica las valoraciones de su propia entidad, sin que un
tercero independiente las recoja o verifique — dejan de ser elegibles para
mostrar estrellas; y (2) las reseñas falsas o incentivadas sin declarar
(seedeadas con un descuento, un producto gratis o una campaña de reseñas
post-compra) quedan explícitamente prohibidas si se presentan como
opiniones espontáneas. Es habitual encontrar ambas prácticas en ecommerce:
widgets de reseñas propios sin verificación externa, y campañas de email
post-compra que ofrecen un cupón a cambio de una valoración sin dejarlo
claro en la propia reseña.

**Por qué importa (en términos de negocio):** Cuando Google detecta una
infracción de este tipo, no penaliza el ranking de la página — directamente
ignora el marcado estructurado, y las estrellas desaparecen del resultado
de búsqueda. La consecuencia no es un cambio de posición: es competir, en
el mismo puesto del ranking de siempre, contra la competencia que sí
conserva su rich snippet. Varios estudios y casos documentados (Rotten
Tomatoes, Food Network, Nestlé, entre otros) sitúan la mejora de CTR que
aporta un rich snippet de valoraciones frente a un resultado idéntico sin
él en un rango del 20% al 35% (algunos casos puntuales, notablemente
superior). Perder ese rich snippet significa, con el mismo ranking, un
recorte directo de clics — y por tanto de ventas — sin que salte ninguna
alarma ni ningún error visible en la tienda.

**Solución paso a paso:**
1. Identifica cómo se generan hoy las estrellas que muestra tu ficha de
   producto: ¿las recoge y verifica una plataforma de reseñas de terceros
   (Trustpilot, Yotpo, Judge.me, Google Customer Reviews...) o es un
   widget/sistema propio donde tú decides qué reseña se publica y cuál no?
   Un sistema donde la propia marca controla el contenido y la selección de
   las reseñas es candidato a "self-serving" según la política actual.
2. Revisa cualquier campaña activa de captación de reseñas (email
   post-compra, cupón a cambio de opinión, sorteo entre quienes valoren el
   producto): si hay un incentivo, tiene que quedar declarado de forma
   clara en la propia reseña o en la página donde se muestra — nunca
   presentarse como una opinión espontánea.
3. Prueba una ficha de producto representativa en la Prueba de Resultados
   Enriquecidos de Google (search.google.com/test/rich-results) y comprueba
   si el marcado `Review`/`AggregateRating` se valida sin advertencias — una
   advertencia o un marcado ignorado silenciosamente es la señal de que ya
   no cumple.
4. Si el sistema actual es propio y no verificado por un tercero, valora
   migrar la recogida de reseñas a una plataforma externa reconocida por
   Google, o añadir una capa de verificación independiente (por ejemplo,
   solo reseñas de compradores confirmados, recogidas y alojadas fuera del
   control editorial directo de la marca).
5. Documenta el proceso de recogida de reseñas (quién puede reseñar, si hay
   incentivo y cómo se declara, quién modera qué se publica) para poder
   demostrar cumplimiento si Google vuelve a revisar los requisitos, y
   repite la comprobación con la Prueba de Resultados Enriquecidos cada vez
   que cambies de plataforma de reseñas o de proveedor de feeds/CRO.
6. Pasadas 2-4 semanas del cambio, compara en Google Search Console (o
   directamente en el buscador, en incógnito) si el rich snippet de
   estrellas ha vuelto a aparecer para las fichas afectadas.

**Herramientas usadas:** Prueba de Resultados Enriquecidos de Google
(search.google.com/test/rich-results), la documentación oficial de
Google sobre Review/AggregateRating structured data, el panel de la
plataforma de reseñas (propia o de terceros) usada en la tienda, y Google
Search Console para confirmar la recuperación del rich snippet.

---
