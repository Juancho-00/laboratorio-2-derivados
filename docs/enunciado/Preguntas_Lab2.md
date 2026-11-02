# LAB #2 Derivados Financieros

> **Estructura:** (1) rúbrica de evaluación en tabla; (2) enunciado del profesor **literal**. Debajo de cada punto, en un recuadro, aparece **solo lo que la rúbrica exige y el enunciado no dice**. Si la rúbrica y el enunciado piden lo mismo, no se agrega nada.
> Decisiones y resultados: `docs/bitacora_decisiones.md` · Dudas abiertas: `docs/pendientes_profesor.md`

## 1. Rúbrica de evaluación

Proceso de creación del portafolio: **20 %** · Proceso de derivados y cobertura: **80 %**. Cada criterio se califica de 0 a 5 en *aplicación* (cálculos, bases, fórmulas, simulaciones, contratos, margin call, roll-over) y en *análisis* (interpretación, justificación de supuestos, discusión de riesgos, argumentación).

| R | Componente | Criterio evaluado | Evidencia esperada | Punto del enunciado | Peso | Aplic. | Análisis |
|---|---|---|---|:---:|---:|---:|---:|
| R1 | Portafolio | Selección de tres acciones y análisis fundamental | Identifica acciones válidas del mismo índice; sustenta la selección con sector, negocio, evolución, fundamentos y expectativa de precio a un año. | 1 | 5 % | 2 % | 3 % |
| R2 | Portafolio | Retornos, volatilidad anualizada y matrices de riesgo | Construye series históricas de 6 a 10 años hasta el 30/10/2026; calcula retornos, desviaciones, varianzas, covarianzas y correlaciones con anualización coherente. | 2 | 5 % | 2 % | 3 % |
| R3 | Portafolio | Optimización media-varianza, pesos óptimos y asignación de capital | Obtiene pesos óptimos, monto invertido por acción, retorno esperado, desviación estándar y Sharpe Ratio del portafolio sobre USD 35 millones. | 3 | 7 % | 3 % | 4 % |
| R4 | Portafolio | Calidad de datos, fuentes y trazabilidad del modelo de portafolio | Documenta fuentes de precios, supuestos de frecuencia, tratamiento de dividendos, limpieza de datos y coherencia temporal de los insumos. | Transversal | 3 % | 1 % | 2 % |
| R5 | Derivados | VaR mensual del portafolio al 1 % y 5 % como base de cobertura | Calcula VaR mensual en porcentaje y dólares; interpreta escenarios de pérdida y los relaciona con la necesidad de cobertura. | 4 | 8 % | 3 % | 5 % |
| R6 | Derivados | Estimación de betas CAPM individuales y beta del portafolio | Calcula betas con el índice como mercado; estima beta del portafolio con pesos óptimos y explica exposición sistemática. | 5 | 8 % | 3 % | 5 % |
| R7 | Derivados | Selección técnica del futuro sobre índice y parámetros contractuales | Identifica contrato, vencimientos, multiplicador, precio inicial, margen inicial, margen de mantenimiento, liquidación y plataforma bursátil usada. | 7 (y especificaciones) | 6 % | 2 % | 4 % |
| R8 | Derivados | Número óptimo de contratos de futuros sobre índice | Aplica N\* = βp·Vp / (F₀·Q_F), usa valor del portafolio, precio del futuro y multiplicador; redondea de forma justificada por discretización. | 6 | 7 % | 3 % | 4 % |
| R9 | Derivados | Definición de posición corta o larga según objetivo de cobertura | Justifica el uso de futuros cortos para cubrir una cartera larga en acciones; analiza efectos si el mercado sube o baja y el riesgo que se cubre. | 7 | 10 % | 3 % | 7 % |
| R10 | Derivados | Flujos mensuales, mark-to-market y margin call usando ticks | Calcula ganancias/pérdidas mensuales de largos y cortos, saldo de margen, margen de mantenimiento y reposición al margen inicial. | 8 | 12 % | 5 % | 7 % |
| R11 | Derivados | Estrategia de roll-over trimestral y rentabilidad de la cobertura | Modela cierre y reapertura trimestral de futuros; evalúa ganancias/pérdidas realizadas, riesgo de base, costos y efecto sobre rentabilidad. | 9 | 10 % | 4 % | 6 % |
| R12 | Derivados | Valor esperado de la cobertura trimestral y tasa libre de riesgo | Usa una tasa libre de riesgo observable en la fecha inicial (^TNX o equivalente); calcula valor esperado y compara portafolio cubierto vs. no cubierto. | 10 | 7 % | 3 % | 4 % |
| R13 | Derivados | Rendimiento esperado mensual, valor de cartera, VaR y dividendos | Calcula valor esperado mensual de la cartera, ajusta por VaR, considera dividendos si aplican e interpreta su efecto sobre rendimiento total. | 11 | 6 % | 2 % | 4 % |
| R14 | Derivados | Sensibilidad de la cobertura con beta igual a 0.6 y 1.5 | Recalcula contratos, exposición sistemática e intensidad de cobertura para beta; interpreta diferencias. | 12 | 6 % | 3 % | 3 % |
| | | | | **Total** | **100 %** | **39 %** | **61 %** |

**Escala:** Deficiente (no desarrolla el criterio o tiene errores graves de concepto, sin fuentes, cálculos ni interpretación verificable) · Regular (desarrollo parcial, cálculos incompletos, supuestos débiles) · Bueno (cálculos consistentes, fuentes razonables, interpretación clara) · Excelente (integra cálculo, evidencia, supuestos, validación e interpretación financiera rigurosa, clara y trazable).

**Erratas corregidas en esta tabla** (aclaradas por el profesor, clase del 30/10/2026): la rúbrica original dice "S&P 500", "30/04/2026" y "USD 20 millones"; valen Nasdaq-100, 30/10/2026 y USD 35 millones. La hoja "Instrucciones" dice 61 % aplicación y 39 % análisis, pero las columnas suman al revés.

---

## 2. Enunciado del profesor (texto literal)

El propósito del ejercicio es construir un portafolio accionario óptimo compuesto por tres acciones del nasdaq https://www.investing.com/indices/nq-100-components y diseñar una estrategia de cobertura mediante futuros sobre el índice. El estudiante deberá integrar herramientas de análisis fundamental, optimización media-varianza, medición de riesgo mediante VaR, estimación de beta por CAPM, cálculo del número óptimo de contratos de futuros, análisis de llamados al margen y evaluación de una estrategia de roll-over trimestral.

El gerente de inversiones de la entidad solicita diseñar una estrategia de inversión en acciones con horizonte de cuatro años, iniciando el 30 de octubre de 2026. Para ello, se dispone de un capital inicial de 35 millones de dólares. El objetivo es construir un portafolio accionario compuesto por tres acciones pertenecientes al mismo índice bursátil y posteriormente evaluar una estrategia de cobertura utilizando futuros sobre dicho índice.Las acciones deberán seleccionarse a partir de los componentes del índice nasdaq disponibles en la fuente de referencia indicada por el docente. Para la construcción del portafolio óptimo de media-varianza se deberá utilizar información histórica de precios entre 6 y 10 años, medida hasta la fecha de inicio de la inversión.

Los contratos de futuros sobre el índice bursátil deberán tomarse de una plataforma bursátil oficial o reconocida. De dicha fuente se deberán identificar, como mínimo, el activo subyacente del futuro, vencimientos disponibles, tamaño del contrato, multiplicador, precio inicial del futuro, margen inicial, margen de mantenimiento, mecanismo de liquidación y frecuencia de ajuste por mark-to-market.

Para efectos académicos, la posición en futuros deberá evaluarse con liquidaciones mensuales, aunque se debe reconocer que en la práctica los futuros son ajustados diariamente mediante mark-to-market. La estrategia de cobertura deberá considerar una estructura de roll-over trimestral cuando los vencimientos de los contratos no coincidan exactamente con el horizonte de cobertura. El gerente de la entidad donde trabajan les solicita realizar inversiones en bolsa con objeto de inversión a 4 años. El objetivo es establecer un portafolio de inversión utilizando 3 acciones de preferencia del mismo índice bursátil. Se dispone de un capital de 35 millones de dólares para realizar inversiones en acciones desde el 30 de octubre de 2026. Para construir un portafolio óptimo de mínima varianza, se considerarán entre 6 y 10 años de información histórica hasta la fecha de inicio de las inversiones (30 de octubre de 2026).

> **Rúbrica R7 agrega:** dejar explícita cuál fue la plataforma bursátil usada para las especificaciones del contrato.

De lo anterior:

**1.** Seleccione tres acciones pertenecientes al mismo índice bursátil. Para cada acción, realice un análisis fundamental que incluya descripción general de la empresa, sector económico, principales fuentes de ingresos, evolución reciente del precio de mercado, situación financiera general, expectativas de precio para al menos el siguiente año y justificación de inclusión en el portafolio. El análisis debe conectar la información fundamental con la decisión de inversión, evitando una simple descripción de la empresa.

**2.** Con base en la información histórica seleccionada, calcule para cada acción los retornos periódicos, retornos anuales promedio, desviación estándar anualizada, matriz de varianzas y covarianzas y matriz de correlaciones. Indique la frecuencia de los datos utilizada y explique el procedimiento de anualización aplicado.

> **Rúbrica R4 agrega (criterio transversal, 3 %):** documentar las fuentes de precios, los supuestos de frecuencia, el tratamiento de dividendos, la limpieza de datos y la coherencia temporal de los insumos.

**3.** A partir de los retornos esperados, volatilidades y covarianzas de las tres acciones, construya un portafolio óptimo bajo el enfoque de media-varianza Calcule los pesos óptimos de cada acción, el monto invertido en cada una, el retorno esperado del portafolio, la desviación estándar del portafolio y el Sharpe Ratio. La inversión total deberá distribuirse sobre 35.000.000 USD.

**4.** Calcule el Valor en Riesgo del portafolio total para un horizonte mensual con niveles de confianza de 99% y 95%, es decir, VaR al 1% y VaR al 5%. Presente el VaR mensual en porcentaje y en dólares. Interprete los resultados como escenarios de pérdida potencial y explique su relación con el monto que se desea cubrir mediante futuros.

**5.** Calcule la beta de cada acción mediante el enfoque CAPM, usando como portafolio de mercado el índice bursátil al cual pertenecen las acciones seleccionadas. Posteriormente, calcule la beta del portafolio como el promedio ponderado de las betas individuales usando los pesos óptimos obtenidos en el proceso de optimización.

> **Rúbrica R6 agrega:** explicar la exposición sistemática del portafolio.

**6.** Calcule el número óptimo de contratos de futuros sobre el índice necesarios para cubrir el portafolio accionario. Dado que los contratos de futuros son instrumentos discretos, el resultado deberá aproximarse al número entero más adecuado y justificar si se redondea hacia arriba o hacia abajo.

> **Rúbrica R8 agrega:** usar explícitamente la fórmula N\* = βp · Vp / (F₀ · Q_F), con el valor del portafolio, el precio del futuro y el multiplicador.

**7.** Determine qué posición en futuros debe tomar el administrador del portafolio según el objetivo de cobertura usando los ticks de mercado del futuro del indice. Explique cuándo se usa una posición corta en futuros sobre índice, cuándo se usaría una posición larga, qué riesgo se está cubriendo, qué ocurre si el mercado accionario sube y qué ocurre si el mercado accionario baja. Analice especialmente el caso de un inversionista que ya posee acciones y desea protegerse frente a una caída del mercado.

**8.** Con base en el número de contratos calculado, evalúe los flujos trimestrales generados por la posición en futuros. Para cada mes, calcule precio inicial del futuro, precio final mensual, variación del precio, ganancia o pérdida de la posición larga, ganancia o pérdida de la posición corta, saldo de la cuenta de margen, identificación de llamados al margen y reposición requerida para volver al margen inicial. El análisis debe considerar margen inicial, margen de mantenimiento y mecanismo de liquidación según la información disponible del contrato utilizado.

> **Rúbrica R10 agrega:** el mark-to-market y los llamados al margen se calculan **usando ticks** (n.º de ticks = variación del precio / tick; P&G = n.º de ticks × valor del tick × n.º de contratos).

**9.** Suponga que la cobertura en corto absoluto y usando roll over basado en las simulaciones realizadas durante el horizonte de inversión, pero los contratos de futuros se renuevan trimestralmente. Explique y calcule el cierre de la posición al final de cada trimestre, la apertura de una nueva posición en el siguiente contrato disponible, las ganancias o pérdidas realizadas, el efecto del roll-over sobre la rentabilidad del portafolio cubierto.

> **Rúbrica R11 agrega:** evaluar el **riesgo de base** y los **costos** del roll-over.

**10.** Calcule el valor esperado de la cobertura trimestral del portafolio utilizando la tasa libre de riesgo observada en la fecha inicial. Como referencia para Estados Unidos, utilice ^TNX, correspondiente al CBOE Interest Rate 1 to 3 Year Treasury Index, o una tasa equivalente de mercado disponible para la fecha inicial del ejercicio. Identifique la tasa libre de riesgo aplicable, justifique su uso, calcule el valor esperado de la posición cubierta, compare el portafolio sin cobertura frente al portafolio cubierto e interprete si la cobertura reduce riesgo, rentabilidad esperada o ambos.

**11.** Calcule el rendimiento esperado mensual del portafolio y el valor esperado de la cartera bajo tres enfoques: portafolio sin cobertura, portafolio cubierto con futuros y portafolio ajustado por escenarios de VaR. Considere si las empresas seleccionadas pagan dividendos. En caso afirmativo, explique cómo los dividendos afectan el rendimiento total de la acción y el valor esperado del portafolio.

**12.** Analice cómo cambia la estrategia de cobertura si la beta del portafolio toma los valores hipotéticos beta = 0.6 y beta = 1.5. Para cada caso, calcule el nuevo número óptimo de contratos, exposición sistemática del portafolio, sensibilidad ante movimientos del índice, efecto sobre la cobertura e interpretación financiera del resultado. Explique por qué un portafolio con beta mayor requiere una cobertura más intensa frente a movimientos del índice.
