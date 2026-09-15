# Vas a perder las mismas ventas otra vez
**15 de septiembre de 2026 — Pilar: Indexación y rastreo**

## Diagnóstico

Patrón habitual cuando un ecommerce sufre una caída de ventas por contenido
duplicado o fichas finas compitiendo entre sí: para frenar la sangría
rápido, alguien usa la herramienta "Eliminar URLs" (Removals) de Google
Search Console para ocultar la URL problemática. La caída de tráfico se
frena en pocas horas, se da el problema por cerrado, y nadie vuelve a
tocarlo.

El problema: esa herramienta no borra nada del índice de Google, solo lo
oculta temporalmente — unos 6 meses, según la propia documentación de
Search Console — mientras se aplica un arreglo real y permanente en el
servidor (noindex, redirección 410 o un canonical correcto). Pasado ese
plazo, si el arreglo de fondo nunca se llegó a aplicar, la URL vuelve a
aparecer indexada tal cual estaba, sin ningún aviso previo por parte de
Google.

## Por qué importa en términos de negocio

Es una caída de ventas con "efecto retardado": la solución rápida da una
sensación de problema resuelto que dura meses, así que para cuando la
ocultación caduca y el tráfico/ventas vuelven a caer, ya nadie relaciona
la caída con aquella "solución" de hace medio año — se investiga desde
cero, se pierde tiempo, y mientras tanto la ficha o categoría real vuelve
a competir contra su propio duplicado en los resultados de búsqueda.
Multiplicado por cada URL "eliminada" así a lo largo de meses o años, es
una fuga de ventas recurrente e invisible en el calendario de nadie.

## Solución paso a paso

1. **Audita el histórico de solicitudes de eliminación**: en Search
   Console, ve a *Eliminaciones* → pestaña *Solicitudes temporales* y
   revisa cada URL listada — tanto las activas como las ya caducadas (se
   pueden consultar los últimos 6 meses de histórico).
2. **Para cada URL, comprueba si el arreglo de fondo se aplicó de verdad**:
   ¿tiene ahora mismo un `noindex` real en el HTML, devuelve un código 410
   (o 301 hacia la URL correcta), o tiene un canonical apuntando a la
   página buena? Compruébalo directamente sobre la URL en producción, no
   solo de memoria.
3. **Si el arreglo de fondo falta, aplícalo ya** — no esperes a que caduque
   la ocultación temporal. La vía permanente correcta depende del caso:
   `noindex` si la página debe seguir existiendo pero no indexada, 410/301
   si ya no debe existir, o canonical si es una variante de otra página
   equivalente.
4. **Verifica el resultado en Search Console** (Inspección de URLs) antes
   de dar el caso por cerrado — confirma que Google ve el `noindex`, el
   410 o el canonical, no solo que la URL sigue oculta por la solicitud
   temporal.
5. **Documenta la fecha de caducidad de cada ocultación activa** (hoy + 6
   meses) en el calendario o el gestor de tareas del equipo — para revisar
   antes de esa fecha si el arreglo de fondo ya está aplicado, en vez de
   descubrirlo cuando la URL ya ha reaparecido y las ventas ya han caído
   otra vez.

## Herramientas usadas para detectarlo/arreglarlo

- Google Search Console (informe de Eliminaciones + Inspección de URLs)
- Auditoría manual del código de estado HTTP y las etiquetas
  noindex/canonical de cada URL implicada (o Screaming Frog para revisarlo
  en bloque si son varias URLs)

---
