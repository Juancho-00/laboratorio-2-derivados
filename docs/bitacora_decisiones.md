
# BITÁCORA DE DECISIONES – LAB #2

Última actualización: 01/11/2026

## Organización del proyecto (01/11/2026)

- Repositorio con 3 notebooks: `00_datos` (Punto 0 / R4), `01_portafolio` (Puntos 1–5), `02_futuros_cobertura` (Puntos 6–12).
- Entrega: repositorio de GitHub + informe PDF en normas APA ubicado en la raíz, junto al README.md (resuelto).
- Entorno: Anaconda, environment `lab2-derivados` (Python 3.11) definido en `environment.yml`; `requirements.txt` se mantiene para quien use pip.
- Requisitos de la rúbrica no contemplados en el enunciado: integrados en `Puntos_Lab2.md` (v2) y como anexo al final de `Enunciado_Lab2.txt` (el texto original del profesor no se modificó).
- La rúbrica (Excel) tiene erratas (S&P 500, 30/04/2026, USD 20M); las corrige el estudiante. Valen Nasdaq-100, 30/10/2026 y USD 35.000.000 (Clase 23).
- Las 3 acciones (CSCO, ADI, PYPL) pertenecen al Nasdaq-100 (verificado por el estudiante; citar la fuente de investing.com en el Punto 1).
- Dudas abiertas para la asesoría del 04/11/2026 (`docs/pendientes_profesor.md`): P1 (roll-over: ¿siempre corto o cambio largo/corto?) y P2 (cuenta de margen mensual o trimestral).

## Dudas cerradas con el propio proyecto (01/11/2026)

- Tasa libre de riesgo: ^TNX (bono a 10 años), justificada en Puntos_Lab2, Punto 10.
- Márgenes: valores reales de CME en USD por contrato (el enunciado exige la información del contrato utilizado).
- Ticks: los precios del futuro se redondean al tick mínimo para contar ticks enteros (criterio del profesor, Clase 19).
- Punto 12: según el enunciado (prevalece), 0,6 y 1,5 son la beta del portafolio → N* = β · Vp / (F₀ · Q_F).
- VaR del Punto 4: VaR mensual del portafolio total (lo dice el enunciado).
- Decisiones del estudiante (no se le preguntan al profesor; se deciden en su punto): cotas de los pesos, portafolio definitivo (GMV vs. Máx. Sharpe), tratamiento de dividendos (Close vs. Adj Close), modelado del riesgo de base y costos del roll-over, construcción del enfoque "ajustado por VaR".

## Datos

- Fuente de precios: Yahoo Finance (yfinance)
- Ventana histórica: (pendiente)
- Frecuencia de datos: (pendiente)
- Tipo de precio: (Close / Adj Close – pendiente)
- Archivos en data/: (pendiente)

## Tasa libre de riesgo

- ^TNX al 30/10/2026: (pendiente) % anual
- Tasa mensual: (pendiente) | Tasa trimestral: (pendiente) | Método: (pendiente)

## Punto 1 – Análisis fundamental

- Conclusiones clave: (pendiente)

## Punto 2 – Estadística descriptiva

- Retornos anuales promedio: CSCO ___ | ADI ___ | PYPL ___
- Volatilidades anualizadas: CSCO ___ | ADI ___ | PYPL ___

## Punto 3 – Markowitz

- GMV: pesos ___ | Ret ___ | Vol ___ | Sharpe ___
- Máx. Sharpe: pesos ___ | Ret ___ | Vol ___ | Sharpe ___
- PORTAFOLIO ELEGIDO: (pendiente) — Justificación: (pendiente)

## Punto 4 – VaR mensual

- VaR 95 %: ___ % / USD ___ | VaR 99 %: ___ % / USD ___

## Punto 5 – Betas

- CSCO ___ | ADI ___ | PYPL ___ | β portafolio ___

## Puntos 6–7 – Contrato y número de contratos

- Contrato elegido: (E-mini NQ / Micro MNQ – pendiente) — Fuente: (pendiente)
- Multiplicador ___ | Tick ___ | Precio inicial ___
- Margen inicial ___ | Margen de mantenimiento ___
- N* = ___ → redondeado a ___ (criterio: ___)

## Puntos 8–12

- (pendiente)
