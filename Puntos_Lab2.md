
# PUNTOS A DESARROLLAR – LAB #2

## 1. Análisis fundamental de las 3 acciones (CSCO, ADI, PYPL)
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
No proponer otras acciones. Si alguna presenta un problema relevante (poca historia para cubrir 6 a 10 años o no pertenecer al índice), avisar antes de continuar.

## 2. Estadística descriptiva

Retornos periódicos, retorno anual promedio, desviación estándar anualizada, matriz de varianzas-covarianzas y matriz de correlaciones. Indicar la frecuencia de datos y explicar el procedimiento de anualización.

## 3. Portafolio óptimo de Markowitz (dos enfoques)

Con los retornos esperados, volatilidades y covarianzas de las 3 acciones:

- (a) Portafolio de Mínima Varianza (GMV): minimiza la desviación estándar sin importar el retorno.
- (b) Portafolio de Máximo Sharpe (tangente): maximiza el exceso de retorno por unidad de riesgo, con la tasa libre de riesgo del Punto 10 (^TNX).

Para cada uno: pesos óptimos, monto invertido por acción (sobre USD 35.000.000), retorno esperado, desviación estándar y Sharpe Ratio.
Restricciones: suma de pesos = 1 y sin ventas en corto (pesos ≥ 0), salvo que la rúbrica indique otra cosa.
Graficar la frontera eficiente señalando ambos portafolios.
Decisión: comparar ambos en una tabla y justificar cuál es el portafolio definitivo. Considerar el objetivo del gerente (inversión a 4 años con cobertura), el perfil riesgo-retorno, la concentración de los pesos y el efecto sobre la beta y la cobertura. El portafolio escogido se usa en los puntos 4 a 12.

## 4. VaR mensual del portafolio

VaR al 99 % y al 95 % (VaR 1 % y 5 %), en porcentaje y en dólares. Interpretar como escenarios de pérdida potencial y relacionarlo con el monto a cubrir con futuros.

## 5. Betas (CAPM)

Beta de cada acción usando el Nasdaq-100 (^NDX) como mercado, y beta del portafolio como promedio ponderado con los pesos óptimos.

## 6. Número óptimo de contratos de futuros

N* = β × (Valor del portafolio / Valor del contrato de futuros). Redondear a entero y justificar si se redondea hacia arriba o hacia abajo.

## 7. Posición en futuros y especificaciones del contrato

Identificar: subyacente, vencimientos, tamaño, multiplicador, tick, precio inicial, margen inicial, margen de mantenimiento, mecanismo de liquidación y frecuencia de mark-to-market.
Explicar con los ticks de mercado: cuándo se usa posición corta vs. larga, qué riesgo se cubre y qué pasa si el mercado sube o baja. Énfasis en el inversionista que ya posee acciones y quiere protegerse de una caída.

## 8. Flujos de la posición en futuros y cuenta de margen
Como el horizonte (30/10/2026 – 30/10/2030) es futuro, la trayectoria del precio del futuro debe SIMULARSE (p. ej. Monte Carlo / movimiento browniano geométrico), y la simulación se usa en los Puntos 8 y 9.
Con base en el número de contratos calculado, evaluar los flujos trimestrales de la posición en futuros. Para cada mes: precio inicial del futuro, precio final mensual, variación del precio, P&G de la posición larga, P&G de la posición corta, saldo de la cuenta de margen, identificación de llamados al margen y reposición requerida para volver al margen inicial (agrupados por trimestre).
Considerar margen inicial, margen de mantenimiento y mecanismo de liquidación según la información real del contrato utilizado (CME Group).

## 9. Roll-over trimestral (cobertura en corto absoluto)
Suponer cobertura en corto absoluto, con roll-over basado en las simulaciones del horizonte de inversión y renovación trimestral de los contratos. Explicar y calcular: cierre de la posición al final de cada trimestre, apertura en el siguiente contrato disponible, ganancias/pérdidas realizadas y efecto del roll-over sobre la rentabilidad del portafolio cubierto.

## 10. Valor esperado de la cobertura trimestral

Tasa libre de riesgo: ^TNX (CBOE 10-Year Treasury Note Yield) observada al 30/10/2026.
Incluir explícitamente esta observación: aunque el enunciado describe ^TNX como el índice de Treasuries de 1 a 3 años, en realidad corresponde al rendimiento del bono del Tesoro a 10 años. Aun así se prefiere frente a una tasa de muy corto plazo y alta liquidez (como ^IRX, T-Bill a 13 semanas), porque:

- el horizonte de inversión es de 4 años, y una tasa de mayor plazo refleja mejor el costo de oportunidad del capital durante ese periodo;
- es la referencia indicada por el docente y una tasa de mercado ampliamente usada como libre de riesgo.

^TNX cotiza en puntos porcentuales (4,25 = 4,25 % anual). Convertirla a tasa mensual y trimestral, explicando el método (efectiva vs. nominal).
Luego: calcular el valor esperado de la posición cubierta, comparar el portafolio sin cobertura con el cubierto e interpretar si la cobertura reduce el riesgo, la rentabilidad esperada o ambos.

## 11. Rendimiento y valor esperado mensual bajo 3 enfoques

(a) sin cobertura, (b) cubierto con futuros, (c) ajustado por escenarios de VaR.
Verificar si las empresas pagan dividendos y explicar su efecto en el rendimiento total y en el valor esperado del portafolio.

## 12. Sensibilidad a la beta (β = 0,6 y β = 1,5)

Para cada caso: nuevo número de contratos, exposición sistemática, sensibilidad ante movimientos del índice, efecto en la cobertura e interpretación. Explicar por qué una beta mayor exige una cobertura más intensa.

## SUPUESTOS PROPIOS (no están en el enunciado; documentar en el README)
- Punto 3: se construyen dos portafolios (GMV y Máximo Sharpe) porque el enunciado menciona tanto "mínima varianza" como "media-varianza con Sharpe Ratio"; se elige uno con justificación.
- Sin ventas en corto (pesos ≥ 0) y suma de pesos = 1.
- Tasa libre de riesgo: ^TNX (el enunciado permite ^TNX o una tasa equivalente de mercado).
- Mercado para betas: ^NDX.
