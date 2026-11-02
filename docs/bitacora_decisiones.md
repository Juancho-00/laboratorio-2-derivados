# BITÁCORA DE DECISIONES – LAB #2

Última actualización: 02/11/2026

## Organización del proyecto (01/11/2026)

- Repositorio con 3 notebooks: `00_datos` (Punto 0 / R4), `01_portafolio` (Puntos 1–5), `02_futuros_cobertura` (Puntos 6–12).
- Entrega: repositorio de GitHub + informe PDF en normas APA ubicado en la raíz, junto al README.md (resuelto).
- Entorno: Anaconda, environment `lab2-derivados` (Python 3.11) definido en `environment.yml`; `requirements.txt` se mantiene para quien use pip.
- Requisitos de la rúbrica no contemplados en el enunciado: integrados en `Puntos_Lab2.md` (v2) y como anexo al final de `Enunciado_Lab2.txt` (el texto original del profesor no se modificó).
- La rúbrica (Excel) tiene erratas (S&P 500, 30/04/2026, USD 20M); las corrige el estudiante. Valen Nasdaq-100, 30/10/2026 y USD 35.000.000 (Clase 23).
- Las 3 acciones (CSCO, ADI, PYPL) pertenecen al Nasdaq-100 (verificado por el estudiante; citar la fuente de investing.com en el Punto 1).
- Referencia única: `docs/enunciado/Referencia_Lab2.md` (enunciado + rúbrica + precisiones) y `Rubrica Lab #2.xlsx`. Se retiraron `Enunciado_Lab2.txt` y `Puntos_Lab2.md` (02/11/2026).
- Reproducibilidad (02/11/2026): 00_datos y 01_portafolio leen los CSV guardados (no re-consultan Yahoo); optimizador SLSQP con ftol = 1e-12. Ejecución completa en orden (Run All) sin errores; resultados idénticos a los reportados.
- Dudas abiertas para la asesoría del 04/11/2026 (`docs/pendientes_profesor.md`): P1 (roll-over: ¿siempre corto o cambio largo/corto?) y P2 (cuenta de margen mensual o trimestral).

## Dudas cerradas con el propio proyecto (01/11/2026)

- Tasa libre de riesgo: ^TNX (bono a 10 años), justificada en Puntos_Lab2, Punto 10.
- Márgenes: valores reales de CME en USD por contrato (el enunciado exige la información del contrato utilizado).
- Ticks: los precios del futuro se redondean al tick mínimo para contar ticks enteros (criterio del profesor, Clase 19).
- Punto 12: según el enunciado (prevalece), 0,6 y 1,5 son la beta del portafolio → N* = β · Vp / (F₀ · Q_F).
- VaR del Punto 4: VaR mensual del portafolio total (lo dice el enunciado).
- Decisiones del estudiante (no se le preguntan al profesor; se deciden en su punto): cotas de los pesos, portafolio definitivo (GMV vs. Máx. Sharpe), tratamiento de dividendos (Close vs. Adj Close), modelado del riesgo de base y costos del roll-over, construcción del enfoque "ajustado por VaR".

## Datos

- Ventana de estimación: 10 años (31/10/2016 → 30/10/2026)
- Frecuencia: diaria (k = 252) como principal para P2, P3 y P5; mensual (k = 12) para P4 y P8. Retornos logarítmicos.
- Tipo de precio: Adj Close (retorno total). En el P11 se descompone: μ_total ≈ μ_precio (Close) + q (dividend yield), para no contar los dividendos dos veces.
- Anualización: μ = e^(r̄·k) − 1; σ = σ_periódica · √k.

## Punto 0 – Calidad de datos (cerrado 02/11/2026)

- 00_datos lee los CSV de data/raw/ (ACTUALIZAR = False) para que el laboratorio sea reproducible con la descarga del 01/11/2026.
- 0 fechas duplicadas, 0 precios ≤ 0, mayor salto entre fechas = 4 días (festivos). Extremos conservados (eventos reales): ADI y ^NDX 16/03/2020, CSCO 19/05/2022, PYPL 02/02/2022.
- Dividendos: CSCO y ADI 40 pagos en la ventana; PYPL inició en nov-2025 (4 pagos). q últimos 12 m: CSCO 1.60 % | ADI 1.03 % | PYPL 0.98 %.
- Aporte de dividendos al retorno anual (Adj Close − Close): CSCO ≈ 3.37 pp | ADI ≈ 2.25 pp | PYPL ≈ 0.11 pp.
- ^NDX es índice de precio (Adj Close = Close): relevante para F₀ = S₀·e^{(r−q)T} (Punto 10).

## Tasa libre de riesgo

- ^TNX al 30/10/2026: 4.929 % anual → r_f = 0.04929 (Yahoo Finance, cierre del 30/10/2026)
- Tasa mensual: (pendiente) | Tasa trimestral: (pendiente) | Método: (pendiente – Punto 10)

## Punto 1 – Análisis fundamental (cerrado 01/11/2026)

- Fuentes: precios de Yahoo Finance (Tabla 1.1); fundamentales de Yahoo Finance, últimos 12 meses, consultados el 01/11/2026 (`data/processed/fundamentales_yahoo.csv`); hechos de 2026 tomados de los comunicados de resultados (SEC 8-K) y de prensa.
- Evolución al 30/10/2026 (retorno total a 1 año): ADI +81.3 % | CSCO +46.0 % | PYPL −15.1 % | ^NDX +10.3 %.
- Decisión del estudiante: expectativa a 1 año por el método C, P/E constante × EPS ajustado esperado (consenso de Yahoo; año fiscal más cercano al 30/10/2027) (`data/processed/expectativa_precio_PE.csv`).
  - CSCO: P/E 24.2× → objetivo USD 124.49 (+19.1 %), rango 122.17–135.72
  - ADI: P/E 37.0× → objetivo USD 611.25 (+46.5 %), rango 531.33–666.78
  - PYPL: P/E 10.6× → objetivo USD 62.14 (+9.0 %), rango 56.06–64.19
- Rol en el portafolio: CSCO = estabilidad y renta | ADI = crecimiento | PYPL = valor y recuperación (candidata a peso menor).
- Las tres pagan dividendo: CSCO 1.6 % | ADI 1.1 % | PYPL 1.0 % (relevante para el Punto 11).
- Las tres tienen más deuda que caja (caja neta negativa, según Yahoo).

## Punto 2 – Estadística descriptiva

- Retornos log, Adj Close, ventana 01/11/2016 → 30/10/2026. Diaria: 2,513 obs. | Mensual: 120 obs.
- Retorno anual (diaria): CSCO 16.44 % | ADI 22.91 % | PYPL 3.31 % | ^NDX 19.51 %
- Volatilidad anual (diaria): CSCO 26.67 % | ADI 33.33 % | PYPL 39.73 % | ^NDX 22.89 %
- Volatilidad anual (mensual): CSCO 24.14 % | ADI 27.99 % | PYPL 36.23 % | ^NDX 19.02 %
- PYPL rinde por debajo de r_f (3.31 % < 4.929 %) → exceso de retorno negativo.
- Correlaciones diarias: CSCO-ADI 0.49 | CSCO-PYPL 0.35 | ADI-PYPL 0.45 | con ^NDX: CSCO 0.61, ADI 0.74, PYPL 0.62
- Correlaciones mensuales (más bajas): CSCO-ADI 0.37 | CSCO-PYPL 0.24 | ADI-PYPL 0.29
- Matriz Σ para Markowitz (P3): diaria × 252 (más precisa y más conservadora). Σ mensual × 12 para el VaR (P4).
- Archivos: retornos_diarios.csv, retornos_mensuales.csv, cov_anual_diaria.csv, cov_anual_mensual.csv, corr_diaria.csv

## Punto 3 – Markowitz

- GMV: CSCO 45.00 % | ADI 33.97 % | PYPL 21.03 % · Ret 15.88 % · Vol 25.12 % · Sharpe 0.4359
  Montos: CSCO 15,750,000 | ADI 11,889,424.90 | PYPL 7,360,575.10 (optimizador con tolerancia 1e-12; antes 11,889,583.81 / 7,360,416.19 por tolerancia por defecto)
- Máx. Sharpe: CSCO 40.00 % | ADI 45.00 % | PYPL 15.00 % · Ret 17.39 % · Vol 25.63 % · Sharpe 0.4860
  Montos: CSCO 14,000,000 | ADI 15,750,000 | PYPL 5,250,000
- Restricciones activas: GMV (CSCO en el techo); Máx. Sharpe (ADI en el techo, PYPL en el piso). Sin cotas, Máx. Sharpe = 39/61/0.
- Archivo: data/processed/portafolios_markowitz.csv
- Restricción de pesos (decisión del grupo): mínimo 15 %, máximo 45 % por acción; suma = 100 %; sin ventas en corto.
- Frontera: retorno factible entre 11.50 % y 17.39 %; el Máx. Sharpe coincide con el máximo retorno factible. ADI queda por encima de la CML restringida (Sharpe 0.54 > 0.49). Figura: outputs/figures/frontera_eficiente.png
- **PORTAFOLIO ELEGIDO: Máximo Sharpe** (CSCO 40 % | ADI 45 % | PYPL 15 %), decisión del grupo del 01/11/2026. Se usa en los Puntos 4 a 12.
  Justificación: mayor retorno por unidad de riesgo (Sharpe 0.4860 vs. 0.4359); coherente con el análisis fundamental (más ADI, mínimo en PYPL); la cobertura con futuros controla el riesgo sistemático; beta preliminar casi igual a la del GMV (≈ 0.93 vs. ≈ 0.91).

## Punto 4 – VaR mensual

- Método (decisión del estudiante): paramétrico normal con retornos log mensuales del portafolio Máx. Sharpe (120 meses). r* = μm − z·σm; VaR % = 1 − e^(r*); VaR USD = V0 · VaR %.
- μ mensual = 1.3182 % · σ mensual = 6.0200 % · ganancia esperada del mes ≈ USD 464,433
- VaR 95 % (al 5 %): 8.23 % / USD 2,878,978.61 | VaR 99 % (al 1 %): 11.91 % / USD 4,170,100.79
- Validación: 7 de 120 meses superaron el VaR 95 % (se esperaban 6); 0 superaron el VaR 99 %. Peor mes: abr-2022 (−12.07 % log). Asimetría 0.09, curtosis en exceso 0.25.
- Descomposición (modelo de mercado, mensual): β = 0.8206, R² = 0.5603 → 56 % sistemático (cubrible), 44 % específico. σ específica mensual = 3.99 %.
- VaR con cobertura ideal del riesgo sistemático: 95 % USD 1,789,466.95 (−37.84 %) | 99 % USD 2,680,797.33 (−35.71 %). Exposición a cubrir (β mensual × V0) ≈ USD 28,720,153.
- Archivos: var_mensual.csv, var_cubierto_vs_sin.csv · outputs/figures/var_mensual.png

## Punto 5 – Betas

- Método: regresión MCO de retornos log diarios de cada acción contra el ^NDX (01/11/2016 – 30/10/2026, 2,513 obs.); βp = Σ wi·βi con los pesos del Máx. Sharpe.
- β diaria: CSCO 0.7149 (t 38.9; R² 37.6 %) | ADI 1.0707 (t 54.4; R² 54.1 %) | PYPL 1.0839 (t 40.1; R² 39.0 %)
- **β portafolio = 0.9304** (verificada por regresión directa del portafolio contra el índice).
- β mensual (comparación): CSCO 0.7173 | ADI 0.8774 | PYPL 0.9258 | βp 0.8206 → la decisión de qué beta usar para N* se toma en el Punto 6.
- α anual: CSCO +2.49 % | ADI +1.55 % | PYPL −16.06 %. CAPM con E(rm) = 19.51 % y rf = 4.929 %: E(r) CAPM portafolio 18.49 % vs. histórico 17.39 %.
- Exposición sistemática: βp × V0 = 0.9304 × 35,000,000 ≈ USD 32,564,000 equivalentes en el índice; una caída de 10 % del ^NDX implica ≈ −9.30 % (≈ −USD 3.26 M).
- Archivo: data/processed/betas_capm.csv

## Puntos 6–7 – Contrato y número de contratos

- Contrato elegido: (E-mini NQ / Micro MNQ – pendiente) — Fuente: (pendiente)
- Multiplicador ___ | Tick ___ | Precio inicial ___
- Margen inicial ___ | Margen de mantenimiento ___
- N* = ___ → redondeado a ___ (criterio: ___)

## Puntos 8–12

- (pendiente)