
# PUNTOS A DESARROLLAR – LAB #2

> Versión 2 (01/11/2026): se integraron los requisitos de la "Rubrica Lab #2" que no estaban en el enunciado.
> Cada punto indica el criterio de la rúbrica (R#) que lo evalúa y su peso.
> Las dudas abiertas están en `docs/pendientes_profesor.md` (se citan como **[P#]**). Las decisiones del estudiante quedan en `docs/bitacora_decisiones.md`.

## MAPA PUNTO ↔ RÚBRICA

| Punto | Rúbrica | Criterio | Peso total | Aplicación | Análisis |
|---|---|---|---|---|---|
| 0 (transversal) | R4 | Calidad de datos, fuentes y trazabilidad | 3 % | 1 % | 2 % |
| 1 | R1 | Selección de acciones y análisis fundamental | 5 % | 2 % | 3 % |
| 2 | R2 | Retornos, volatilidad anualizada y matrices de riesgo | 5 % | 2 % | 3 % |
| 3 | R3 | Optimización media-varianza y asignación de capital | 7 % | 3 % | 4 % |
| 4 | R5 | VaR mensual 1 % y 5 % como base de cobertura | 8 % | 3 % | 5 % |
| 5 | R6 | Betas CAPM individuales y del portafolio | 8 % | 3 % | 5 % |
| 6 | R8 | Número óptimo de contratos | 7 % | 3 % | 4 % |
| 7 | R7 + R9 | Parámetros del contrato (6 %) + posición corta/larga (10 %) | 16 % | 5 % | 11 % |
| 8 | R10 | Flujos mensuales, mark-to-market y margin call usando ticks | 12 % | 5 % | 7 % |
| 9 | R11 | Roll-over trimestral y rentabilidad de la cobertura | 10 % | 4 % | 6 % |
| 10 | R12 | Valor esperado de la cobertura trimestral y tasa libre de riesgo | 7 % | 3 % | 4 % |
| 11 | R13 | Rendimiento esperado mensual, valor de cartera, VaR y dividendos | 6 % | 2 % | 4 % |
| 12 | R14 | Sensibilidad con β = 0,6 y β = 1,5 | 6 % | 3 % | 3 % |
| | | **Total** | **100 %** | **39 %** | **61 %** |

Proceso de creación del portafolio (Puntos 0–3): 20 %. Derivados y cobertura (Puntos 4–12): 80 %.
El análisis pesa 61 %; la hoja "Instrucciones" de la rúbrica dice lo contrario (61 % aplicación), pero las columnas suman 39 % aplicación y 61 % análisis.

---

## 0. Calidad de datos, fuentes y trazabilidad (R4 – 3 %) — NUEVO, exigido por la rúbrica
Va en `notebooks/00_datos.ipynb` y se resume en el README. Documentar:
- Fuente de precios (Yahoo Finance vía yfinance) y **fecha de descarga**.
- Ventana histórica (6 a 10 años, medida hasta el 30/10/2026; PYPL cotiza desde julio de 2015).
- Frecuencia de datos y procedimiento de anualización.
- Tipo de precio (Close vs. Adj Close) y **tratamiento de dividendos** (evitar contarlos dos veces en el Punto 11) — decisión del estudiante.
- **Limpieza de datos**: valores faltantes, fechas no coincidentes entre acciones e índice, días festivos.
- **Coherencia temporal** de los insumos: precios, ^TNX y especificaciones del futuro con la misma fecha de corte (30/10/2026).

## 1. Análisis fundamental de las 3 acciones (CSCO, ADI, PYPL) (R1 – 5 %)
Fuente de componentes del índice indicada por el docente: https://www.investing.com/indices/nq-100-components (verificar que las 3 acciones pertenezcan al Nasdaq-100 y citarla).
Para cada acción incluir:
- Descripción general de la empresa
- Sector económico
- Principales fuentes de ingresos
- Evolución reciente del precio de mercado
- Situación financiera general
- Expectativas de precio para al menos el siguiente año
- Justificación de inclusión en el portafolio
El análisis debe CONECTAR la información fundamental con la decisión de inversión, no ser una simple descripción de la empresa.
Rúbrica: "identifica acciones válidas del mismo índice; sustenta la selección con sector, negocio, evolución, fundamentos y **expectativa de precio a un año**".
No proponer otras acciones.

## 2. Estadística descriptiva (R2 – 5 %)
Retornos periódicos, retorno anual promedio, desviación estándar anualizada, matriz de varianzas-covarianzas y matriz de correlaciones. Indicar la frecuencia de datos y explicar el procedimiento de anualización.
Rúbrica: series históricas de **6 a 10 años hasta el 30/10/2026** (la rúbrica dice 30/04/2026 por error) con **anualización coherente**.

## 3. Portafolio óptimo de Markowitz (dos enfoques) (R3 – 7 %)
Con los retornos esperados, volatilidades y covarianzas de las 3 acciones:
- (a) Portafolio de Mínima Varianza (GMV): minimiza la desviación estándar sin importar el retorno.
- (b) Portafolio de Máximo Sharpe (tangente): maximiza el exceso de retorno por unidad de riesgo, con la tasa libre de riesgo del Punto 10 (^TNX).
Para cada uno: pesos óptimos, monto invertido por acción (sobre **USD 35.000.000**; la rúbrica dice USD 20 millones por error), retorno esperado, desviación estándar y Sharpe Ratio.
Restricciones: suma de pesos = 1 y sin ventas en corto (pesos ≥ 0). Cotas mínimas/máximas por acción (el Excel de ejemplo usa 10 %–40 %): decisión del estudiante.
Graficar la frontera eficiente señalando ambos portafolios.
Decisión: comparar ambos en una tabla y justificar cuál es el portafolio definitivo (decisión del estudiante). Considerar el objetivo del gerente (inversión a 4 años con cobertura), el perfil riesgo-retorno, la concentración de los pesos y el efecto sobre la beta y la cobertura. El portafolio escogido se usa en los puntos 4 a 12.

## 4. VaR mensual del portafolio (R5 – 8 %)
VaR al 99 % y al 95 % (VaR 1 % y 5 %), en porcentaje y en dólares. Interpretar como escenarios de pérdida potencial y relacionarlo con el monto a cubrir con futuros.
Rúbrica: el VaR es la **base de la cobertura**; explicar cómo justifica la necesidad de cubrir. (Prevalece el enunciado: VaR mensual del portafolio total; el método de cálculo es decisión del estudiante.)

## 5. Betas (CAPM) (R6 – 8 %)
Beta de cada acción usando el Nasdaq-100 (^NDX) como mercado, y beta del portafolio como promedio ponderado con los pesos óptimos.
Rúbrica: además, **explicar la exposición sistemática** que representa βp.

## 6. Número óptimo de contratos de futuros (R8 – 7 %)
N* = βp · Vp / (F₀ · Q_F), con Vp = valor del portafolio, F₀ = precio del futuro y Q_F = multiplicador del contrato. Redondear a entero y justificar si se redondea hacia arriba o hacia abajo (discretización).

## 7. Especificaciones del contrato y posición en futuros (R7 – 6 % y R9 – 10 %)
**R7.** Identificar: subyacente, vencimientos, tamaño, multiplicador, tick, precio inicial, margen inicial, margen de mantenimiento, mecanismo de liquidación, frecuencia de mark-to-market y **la plataforma bursátil usada (CME Group), con fecha de consulta**. Márgenes: valores reales de CME en USD por contrato (enunciado: "según la información disponible del contrato utilizado").
**R9.** Explicar con los ticks de mercado: cuándo se usa posición corta vs. larga, qué riesgo se cubre (sistemático) y qué pasa si el mercado sube o baja. Énfasis en el inversionista que ya posee acciones y quiere protegerse de una caída: **justificar los futuros cortos para cubrir una cartera larga en acciones**.

## 8. Flujos de la posición en futuros y cuenta de margen (R10 – 12 %)
Como el horizonte (30/10/2026 – 30/10/2030) es futuro, la trayectoria del precio del futuro debe SIMULARSE (p. ej. Monte Carlo / movimiento browniano geométrico), y la simulación se usa en los Puntos 8 y 9.
Con base en el número de contratos calculado, evaluar los flujos de la posición en futuros. Para cada mes: precio inicial del futuro, precio final mensual, variación del precio, P&G de la posición larga, P&G de la posición corta, saldo de la cuenta de margen, identificación de llamados al margen y reposición requerida para volver al margen inicial (agrupados por trimestre) **[P2 pendiente: ¿mensual o trimestral?]**.
**Exigido por la rúbrica — USANDO TICKS** (criterio de la Clase 19: los precios del futuro se redondean al tick mínimo para contar ticks enteros):
- N.º de ticks = ΔF / tick
- Valor del tick = multiplicador × tick
- P&G = N.º de ticks × valor del tick × N.º de contratos (el corto invierte el signo)
Considerar margen inicial, margen de mantenimiento y mecanismo de liquidación según la información real del contrato utilizado (CME Group).

## 9. Roll-over trimestral (R11 – 10 %)
Suponer cobertura en corto absoluto, con roll-over basado en las simulaciones del horizonte de inversión y renovación trimestral de los contratos **[P1 pendiente: ¿siempre corto o cambio largo/corto por trimestre?]**. Explicar y calcular: cierre de la posición al final de cada trimestre, apertura en el siguiente contrato disponible, ganancias/pérdidas realizadas y efecto del roll-over sobre la rentabilidad del portafolio cubierto.
**Exigido por la rúbrica (no está en el enunciado)** — el modelado es decisión del estudiante:
- **Riesgo de base**: bₜ = Sₜ − Fₜ en cada fecha de roll (notación de la Clase 20) y su efecto en el resultado de la cobertura.
- **Costos** del roll-over (comisiones / costos de transacción por contrato cerrado y abierto).

## 10. Valor esperado de la cobertura trimestral (R12 – 7 %)
Tasa libre de riesgo: ^TNX (CBOE 10-Year Treasury Note Yield) observada al 30/10/2026.
Incluir explícitamente esta observación: aunque el enunciado describe ^TNX como el índice de Treasuries de 1 a 3 años, en realidad corresponde al rendimiento del bono del Tesoro a 10 años. Aun así se prefiere frente a una tasa de muy corto plazo y alta liquidez (como ^IRX, T-Bill a 13 semanas), porque:
- el horizonte de inversión es de 4 años, y una tasa de mayor plazo refleja mejor el costo de oportunidad del capital durante ese periodo;
- es la referencia indicada por el docente y una tasa de mercado ampliamente usada como libre de riesgo.
^TNX cotiza en puntos porcentuales (4,25 = 4,25 % anual). Convertirla a tasa mensual y trimestral, explicando el método (efectiva vs. nominal).
Luego: calcular el valor esperado de la posición cubierta, comparar el portafolio sin cobertura con el cubierto e interpretar si la cobertura reduce el riesgo, la rentabilidad esperada o ambos.

## 11. Rendimiento y valor esperado mensual bajo 3 enfoques (R13 – 6 %)
(a) sin cobertura, (b) cubierto con futuros, (c) ajustado por escenarios de VaR (la construcción de este enfoque es decisión del estudiante; referencia: hoja "cobertura corta trimestral" del Excel de ejemplo).
Verificar si las empresas pagan dividendos y explicar su efecto en el rendimiento total y en el valor esperado del portafolio. Si el dato de dividendos es anual, convertirlo a la periodicidad usada (mensual/trimestral).

## 12. Sensibilidad a la beta (β = 0,6 y β = 1,5) (R14 – 6 %)
Para cada caso: nuevo número de contratos, exposición sistemática, sensibilidad ante movimientos del índice, efecto en la cobertura e interpretación. Según el enunciado (prevalece), 0,6 y 1,5 son valores hipotéticos de la **beta del portafolio**: N* = β · Vp / (F₀ · Q_F). Explicar por qué una beta mayor exige una cobertura más intensa.

## SUPUESTOS PROPIOS (no están en el enunciado; documentar en el README)
- Punto 3: se construyen dos portafolios (GMV y Máximo Sharpe) porque el enunciado menciona tanto "mínima varianza" como "media-varianza con Sharpe Ratio"; se elige uno con justificación.
- Sin ventas en corto (pesos ≥ 0) y suma de pesos = 1.
- Tasa libre de riesgo: ^TNX (el enunciado permite ^TNX o una tasa equivalente de mercado).
- Mercado para betas: ^NDX.
- Punto 0: sección de calidad de datos agregada para cumplir el criterio R4 de la rúbrica.
- Punto 9: riesgo de base y costos de roll-over agregados para cumplir el criterio R11 de la rúbrica.
