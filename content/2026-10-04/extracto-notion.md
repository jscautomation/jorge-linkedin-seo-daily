## Tus ventas desde la IA están llegando. Y no las estás viendo — 04/10/2026

**Contexto / diagnóstico**: los compradores ya llegan a las tiendas desde asistentes de IA (Gemini y otros). Hasta ahora, buena parte de esas visitas aparecían en Google Analytics 4 como tráfico "directo", porque sin referrer ni UTM el "directo" es la categoría por defecto. Google ha empezado a añadir parámetros UTM a los enlaces salientes de Gemini (noticia de Search Engine Journal), lo que permite atribuir esas visitas, pero solo si tu analítica está configurada para reconocerlas.

**Por qué importa en términos de negocio**: si no sabes cuánta facturación te trae la IA ni qué productos o categorías recomienda, no puedes decidir dónde invertir en contenido, feed o catálogo. Cada euro de ese canal sigue contando como "directo", y el canal parece menor de lo que es. Quien lo mide antes que su competencia refuerza lo que ya vende.

**Solución paso a paso**:

1. **Línea base**: en GA4, Informes > Adquisición > Adquisición de tráfico, anota las sesiones, transacciones e ingresos de "Directo" de los últimos 90 días. Será tu punto de comparación.
2. **Buscar el tráfico de IA que ya llega**: en Exploraciones, crea un informe con Origen/Medio de la sesión y filtra por `gemini`, `chatgpt`, `perplexity`, `copilot` y `claude` (coincidencia parcial). Comprueba qué valor de `utm_source` llega realmente desde Gemini en tus datos; no lo supongas.
3. **Crear un grupo de canales "IA generativa"**: en Administrador > Configuración de datos > Grupos de canales, crea un grupo personalizado con una regla de origen que coincida con esas fuentes (expresión regular), y colócalo por encima de "Referral" y "Directo".
4. **Evitar que tus propias campañas lo ensucien**: no uses `utm_source=gemini` ni similares en tus enlaces. Mantén una convención de UTM propia y documentada.
5. **Informe de landing pages de IA**: con el nuevo grupo, mira páginas de destino, ingresos y conversión. Identifica qué fichas y categorías te recomienda la IA.
6. **Reforzar lo que ya funciona**: en esas fichas, revisa Product schema completo, GTIN/marca, precio y stock sincronizados con el feed, y contenido claro de talla, envío y devoluciones.
7. **Si usas Looker Studio o Shopify**: replica la misma regla de canal en el panel o la plantilla de informe, para que todo el equipo vea el mismo dato.
8. **Revisión recurrente**: repite el informe cada 2-4 semanas y compara con la línea base del paso 1. Las plataformas de IA cambian cómo etiquetan los enlaces; si una fuente cae a "directo" otra vez, ajusta la regla.

**Herramientas usadas**: Google Analytics 4 (Exploraciones, grupos de canales), Looker Studio (opcional), Search Console, Merchant Center.

**Fuente de la noticia**: Search Engine Journal, "Google Gemini Adds UTM Parameters For Referral Attribution".

---
