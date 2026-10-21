# Pruebas y mediciones · H3–H5

La infraestructura que arranca no equivale a una práctica completa. Los once casos de aceptación de la plantilla están omitidos hasta que los implementéis.

## Matriz de aceptación

| Caso | Requisito | Caso pequeño propio / cálculo independiente | Test y evidencia | Estado |
|---|---|---|---|---|
| P01 | Arranque completo desde clon limpio | | | Pendiente |
| P02 | Repetición sin duplicados | | | Pendiente |
| P03 | Reconciliación de recepciones | | | Pendiente |
| P04 | Integración sin pérdidas ni multiplicación | | | Pendiente |
| P05 | Escenarios y periodos normales | | | Pendiente |
| P06 | Lote tardío | | | Pendiente |
| P07 | Energía y huecos | | | Pendiente |
| P08 | Denominadores y no evaluable | | | Pendiente |
| P09 | Persistencia | | | Pendiente |
| P10 | Formatos y motores equivalentes | | | Pendiente |
| P11 | Fallo controlado y publicación | | | Pendiente |

Los resultados esperados deben derivarse de un razonamiento independiente, no de ejecutar la misma función que se está probando. Añadid casos límite de cadencia, intervalos, unidades y ausencias.

## Registro de experimentos

| Fecha / commit | Entorno y versiones | Parámetros / filas | Operación | Formato / motor | Repetición | Tiempo | Memoria máxima y método | Bytes | Equivalencia |
|---|---|---|---|---|---|---|---|---|---|
| Por medir | | | | | | | | | |

- Diferenciad generación, arranque del motor y operación medida.
- Indicad condiciones, caché, procesos concurrentes y límites de recursos.
- Comparad la misma operación y los mismos datos; verificad claves, conteos y tolerancia antes de interpretar tiempos.
- Haced tres repeticiones de formatos y presentad medianas, sin ocultar las observaciones individuales.
- Comprobad perfiles funcional, 100k y 1m, o documentad la alternativa acordada.
- Identificad Spark local como local. Medid lista/conjunto incluyendo la preparación.
- Separad datos medidos de hipótesis para estimaciones de almacenamiento o electricidad.

## Persistencia y fallos

Definid qué contaréis o compararéis antes y después de una parada. No regeneréis datos entre ambas capturas. Probad un fallo sobre una copia de trabajo: no alteréis la única copia de los originales.
