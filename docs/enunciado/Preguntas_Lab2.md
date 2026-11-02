# LAB #2 Derivados Financieros

> Documento único de referencia: integra el **enunciado del profesor** (texto oficial, resumido por punto), los **criterios de la rúbrica** y las **precisiones** ya resueltas. La rúbrica en Excel (`Rubrica Lab #2.xlsx`) se conserva para los porcentajes de calificación.
> Versión 3 – 02/11/2026. Decisiones y resultados: `docs/bitacora_decisiones.md`. Dudas abiertas: `docs/pendientes_profesor.md`.

## Contexto del caso (enunciado)

- El gerente de inversiones solicita una estrategia en acciones con **horizonte de 4 años**, iniciando el **30 de octubre de 2026**, con un capital de **USD 35.000.000**.
- Portafolio de **3 acciones del mismo índice** (Nasdaq-100; fuente de componentes indicada por el docente: https://www.investing.com/indices/nq-100-components). Acciones del grupo: **CSCO, ADI y PYPL**.
- Optimización media-varianza con **6 a 10 años** de precios históricos, medidos hasta la fecha de inicio.
- Cobertura con **futuros sobre el índice**, con especificaciones tomadas de una plataforma oficial o reconocida (mínimo: subyacente, vencimientos, tamaño, multiplicador, precio inicial, margen inicial, margen de mantenimiento, mecanismo de liquidación y frecuencia de mark-to-market).
- **Supuestos académicos:** la posición en futuros se evalúa con **liquidaciones mensuales** (reconociendo que en la práctica el mark-to-market es diario) y con **roll-over trimestral** cuando los vencimientos no coinciden con el horizonte.

## Escala y pesos de la rúbrica

- Niveles: **Deficiente** (no desarrolla o con errores graves, sin fuentes ni cálculos verificables) · **Regular** (desarrollo parcial, supuestos débiles) · **Bueno** (cálculos consistentes, fuentes razonables, interpretación clara) · **Excelente** (integra cálculo, evidencia, supuestos, validación e interpretación rigurosa y trazable).
- Cada criterio se califica de 0 a 5 en **aplicación** (39 % del total) y **análisis** (61 % del total). Creación del portafolio: 20 %; derivados y cobertura: 80 %. *(La hoja "Instrucciones" dice 61 % aplicación / 39 % análisis, pero las columnas suman al revés.)*
- El profesor aclaró que el análisis debe estar **redactado con palabras propias**.

| Punto | Rúbrica | Criterio | Peso | Aplic. | Análisis |
|---|---|---|---:|---:|---:|
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

---

## 0. Calidad de datos, fuentes y trazabilidad — R4 (3 %)
**Rúbrica:** documenta fuentes de precios, supuestos de frecuencia, tratamiento de dividendos, limpieza de datos y coherencia temporal de los insumos. *(No aparece en el enunciado; lo exige la rúbrica.)*
**Dónde:** `notebooks/00_datos.ipynb` (secciones 0.1–0.5) y README.

## 1. Selección y análisis fundamental — R1 (5 %)
**Enunciado:** para cada acción: descripción general, sector económico, principales fuentes de ingresos, evolución reciente del precio, situación financiera general, expectativas de precio para al menos el siguiente año y justificación de inclusión. El análisis debe **conectar la información fundamental con la decisión de inversión**, evitando una simple descripción.
**Rúbrica:** identifica acciones válidas del mismo índice; sustenta la selección con sector, negocio, evolución, fundamentos y **expectativa de precio a un año**.
**Precisión:** citar la fuente de componentes del índice (investing.com) con fecha de consulta.

## 2. Estadística descriptiva — R2 (5 %)
**Enunciado:** retornos periódicos, retornos anuales promedio, desviación estándar anualizada, matriz de varianzas-covarianzas y matriz de correlaciones; indicar la frecuencia y explicar la anualización.
**Rúbrica:** series de 6 a 10 años hasta el 30/10/2026, con **anualización coherente**.

## 3. Optimización media-varianza — R3 (7 %)
**Enunciado:** con retornos esperados, volatilidades y covarianzas, construir el portafolio óptimo de media-varianza: pesos, monto por acción, retorno esperado, desviación estándar y Sharpe Ratio, distribuyendo USD 35.000.000.
**Rúbrica:** pesos óptimos, monto invertido por acción, retorno esperado, desviación estándar y Sharpe Ratio.
**Precisiones:** se construyen dos portafolios (GMV y Máximo Sharpe, porque el enunciado menciona "mínima varianza" y "Sharpe Ratio") y se elige uno con justificación; frontera eficiente con ambos; restricciones de pesos definidas por el grupo.

## 4. VaR mensual — R5 (8 %)
**Enunciado:** VaR del portafolio total con horizonte mensual al 99 % y 95 % (VaR al 1 % y 5 %), en porcentaje y en dólares; interpretarlo como escenarios de pérdida potencial y explicar su relación con el monto a cubrir con futuros.
**Rúbrica:** VaR mensual en % y USD; interpreta escenarios de pérdida y los relaciona con la **necesidad de cobertura**.

## 5. Betas CAPM — R6 (8 %)
**Enunciado:** beta de cada acción con el índice al que pertenecen como portafolio de mercado (^NDX); beta del portafolio como promedio ponderado con los pesos óptimos.
**Rúbrica:** calcula betas con el índice; beta del portafolio con pesos óptimos y **explica la exposición sistemática**.

## 6. Número óptimo de contratos — R8 (7 %)
**Enunciado:** número óptimo de contratos sobre el índice para cubrir el portafolio; aproximar al entero más adecuado y justificar si se redondea hacia arriba o hacia abajo.
**Rúbrica:** aplica **N\* = βp · Vp / (F₀ · Q_F)** con el valor del portafolio, el precio del futuro y el multiplicador; redondeo justificado por discretización.

## 7. Contrato de futuros y posición — R7 (6 %) + R9 (10 %)
**Enunciado:** posición en futuros según el objetivo de cobertura **usando los ticks de mercado** del futuro del índice; explicar cuándo se usa corto o largo, qué riesgo se cubre y qué ocurre si el mercado sube o baja, en especial para un inversionista que ya posee acciones y quiere protegerse de una caída.
**Rúbrica R7:** identifica contrato, vencimientos, multiplicador, precio inicial, margen inicial, margen de mantenimiento, liquidación y **plataforma bursátil usada**.
**Rúbrica R9:** justifica **futuros cortos para cubrir una cartera larga** en acciones; analiza efectos si el mercado sube o baja y el riesgo que se cubre.
**Precisión:** márgenes reales de CME en USD por contrato, con fecha de consulta.

## 8. Flujos y cuenta de margen — R10 (12 %)
**Enunciado:** con el número de contratos, evaluar los flujos trimestrales de la posición; **para cada mes**: precio inicial del futuro, precio final mensual, variación, P&G de la posición larga y de la corta, saldo de la cuenta de margen, llamados al margen y reposición para volver al margen inicial; considerar margen inicial, de mantenimiento y mecanismo de liquidación del contrato.
**Rúbrica:** P&G mensual de largos y cortos, saldo de margen, margen de mantenimiento y reposición al margen inicial, **usando ticks**.
**Precisiones:** el horizonte 30/10/2026–30/10/2030 es futuro → el precio del futuro se **simula** (p. ej. movimiento browniano geométrico) y la simulación se usa en los Puntos 8 y 9. Por ticks: N.º de ticks = ΔF / tick; valor del tick = multiplicador × tick; P&G = ticks × valor del tick × contratos (el corto invierte el signo). Los precios se redondean al tick mínimo (criterio de la Clase 19). **[Pendiente P2: ¿tabla mensual o trimestral?]**

## 9. Roll-over trimestral — R11 (10 %)
**Enunciado:** cobertura **en corto absoluto** con roll-over basado en las simulaciones y renovación trimestral; explicar y calcular el cierre al final de cada trimestre, la apertura en el siguiente contrato, las ganancias/pérdidas realizadas y el efecto del roll-over sobre la rentabilidad del portafolio cubierto.
**Rúbrica:** modela cierre y reapertura trimestral; evalúa P&G realizadas, **riesgo de base, costos** y efecto sobre la rentabilidad.
**Precisiones:** riesgo de base bₜ = Sₜ − Fₜ (notación de la Clase 20) y costos de transacción del roll: modelado a decisión del estudiante. **[Pendiente P1: ¿siempre corto o cambio largo/corto por trimestre?]**

## 10. Valor esperado de la cobertura trimestral — R12 (7 %)
**Enunciado:** valor esperado de la cobertura trimestral con la tasa libre de riesgo de la fecha inicial (^TNX o una tasa equivalente); identificar y justificar la tasa, calcular el valor esperado de la posición cubierta, comparar portafolio sin cobertura vs. cubierto e interpretar si la cobertura reduce riesgo, rentabilidad esperada o ambos.
**Rúbrica:** tasa libre de riesgo observable en la fecha inicial; valor esperado; comparación cubierto vs. no cubierto.
**Precisiones:** el enunciado describe ^TNX como "Treasuries de 1 a 3 años", pero es el **bono del Tesoro a 10 años**; se usa justificando el horizonte de 4 años. ^TNX cotiza en puntos porcentuales; convertir a tasa mensual y trimestral explicando el método (efectiva vs. nominal).

## 11. Rendimiento y valor esperado mensual: 3 enfoques — R13 (6 %)
**Enunciado:** rendimiento esperado mensual y valor esperado de la cartera (a) sin cobertura, (b) cubierta con futuros y (c) ajustada por escenarios de VaR; considerar si las empresas pagan dividendos y explicar su efecto en el rendimiento total y el valor esperado.
**Rúbrica:** valor esperado mensual, ajuste por VaR, dividendos si aplican y su efecto sobre el rendimiento total.
**Precisiones:** los retornos usan Adj Close (ya incluyen dividendos): se descompone μ_total ≈ μ_precio + q para no contarlos dos veces; q anual se convierte a la periodicidad usada. La construcción del enfoque (c) es decisión del estudiante.

## 12. Sensibilidad a la beta — R14 (6 %)
**Enunciado:** cómo cambia la cobertura si la beta del portafolio toma los valores hipotéticos **β = 0,6 y β = 1,5**: nuevo número óptimo de contratos, exposición sistemática, sensibilidad ante movimientos del índice, efecto sobre la cobertura e interpretación; explicar por qué una beta mayor requiere una cobertura más intensa.
**Rúbrica:** recalcula contratos, exposición sistemática e intensidad de la cobertura; interpreta diferencias.
**Precisión:** por el enunciado, 0,6 y 1,5 reemplazan la beta del portafolio: N\* = β · Vp / (F₀ · Q_F).

## Supuestos propios (documentados en el README)

- Dos portafolios (GMV y Máximo Sharpe) y elección justificada.
- Pesos entre 15 % y 45 % por acción, suma = 1, sin ventas en corto.
- Tasa libre de riesgo: ^TNX al 30/10/2026; mercado para betas: ^NDX.
- Punto 0 (R4) y riesgo de base y costos en el Punto 9 (R11) agregados porque los exige la rúbrica.
