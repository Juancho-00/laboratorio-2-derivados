# BITÁCORA DE DECISIONES – LAB #2

## CAMBIOS ASESORÍA PROFESOR (09/11/2026) – PREVALECEN SOBRE LO ANTERIOR

Lo que pidió el profe:
1. Cambiar PYPL.
2. Portafolio de MÍNIMA VARIANZA (GMV), ya no Máx. Sharpe.
3. Corregir el MBG: los extremos salían desfasados (el superior daba el índice ~10 veces más alto en 4 años).
4. Trayectorias representativas: comparar el PEOR escenario sin cobertura vs. el portafolio cubierto (no mostrar el crecimiento del portafolio sin cubrir).
5. Cuidar las unidades: simulación MENSUAL y aplicarla bien en cada parte.
6. Comentarios y markdown más naturales, de estudiante, menos técnicos.

Decisiones (10/11/2026):
- Se hace una rama git `v2-asesoria`; `main` conserva la versión con PYPL + Máx. Sharpe.
- Lista de componentes copiada de investing.com el 10/11/2026 → data/raw/nasdaq100_componentes_investing.csv (101 tickers).
- Screening (notebooks/00_screening_reemplazo.ipynb → data/processed/screening_reemplazo_pypl.csv): filtro = 10 años completos, retorno 2026 > 0, ≥ 6 de 9 años en verde. Pasaron 46.
- Hallazgo: las ganadoras de 2026 (MU, AMD, MRVL, STX) son chips con ρ alta con ADI y σ de 44–57 %; en el GMV quedan en el piso del 15 % y suben la σ del portafolio a ~27 % (con PYPL era 25,12 %). Defensivas la bajan a 18–21 %.
- **ACCIÓN NUEVA: AMGN (Amgen)** en lugar de PYPL. Portafolio: CSCO, ADI, AMGN.
  Por qué: retorno 2026 +45,3 %, R² de tendencia 0,93, peor caída en 10 años −25 % (la menor de las 46), σ 25,1 %, ρ baja con CSCO (0,34) y ADI (0,31). Sector salud, diversifica frente a redes y chips.
  GMV preliminar (cotas 15–45 %): CSCO 40 / ADI 15 / AMGN 45 · σ ≈ 20,86 % · Sharpe ≈ 0,59 (se confirma en 01_portafolio).
  Riesgo identificado: deuda alta (compra de Horizon, 2023) y liquidez corriente ajustada → analizar en el P1 con deuda neta/EBITDA, cobertura de intereses y FCF.
- Finalistas descartadas: COST (mejor Sharpe en el GMV, pero P/E ~50×) y PANW (+98,6 % en 2026, pero P/E ~85× y sin dividendo).

Resultados INVALIDADOS por el cambio (hay que rehacerlos): todo lo de PYPL en P0–P2, pesos y montos del P3, VaR (P4), betas (P5), N*, cuenta de margen, simulación MBG y roll-over (P6–P12).

## Organización del proyecto (01/11/2026)

- Repositorio con 3 notebooks: `00_datos` (Punto 0 / R4), `01_portafolio` (Puntos 1–5), `02_futuros_cobertura` (Puntos 6–12).
- Entrega: repositorio de GitHub + informe PDF en normas APA ubicado en la raíz, junto al README.md (resuelto).
- Entorno: Anaconda, environment `lab2-derivados` (Python 3.11) definido en `environment.yml`; `requirements.txt` se mantiene para quien use pip.
- La rúbrica (Excel) tiene erratas (S&P 500, 30/04/2026, USD 20M); las corrige el estudiante. Valen Nasdaq-100, 30/10/2026 y USD 35.000.000 (Clase 23).
- Las 3 acciones (CSCO, ADI, PYPL) pertenecen al Nasdaq-100 (verificado por el estudiante; citar la fuente de investing.com en el Punto 1).
- Referencia única: `docs/enunciado/Preguntas_Lab2.md` (rúbrica en tabla + enunciado literal del profesor + lo que la rúbrica agrega por punto) y `Rubrica Lab #2.xlsx`. Se retiraron `Enunciado_Lab2.txt` y `Puntos_Lab2.md` (02/11/2026).
- Reproducibilidad (02/11/2026): 00_datos y 01_portafolio leen los CSV guardados (no re-consultan Yahoo); optimizador SLSQP con ftol = 1e-12. Ejecución completa en orden (Run All) sin errores; resultados idénticos a los reportados.

## Respuestas del profesor (asesoría 04/11/2026) – decisiones del 05/11/2026

- P1 (dirección de la cobertura): cobertura CORTA en todos los trimestres (corto absoluto) con roll-over
  trimestral. El profesor indicó que el inversionista espera que las acciones suban y que el corto mitiga
  las caídas fuertes. El corto es un seguro de la cartera larga, no una apuesta de dirección.
  No se modela la alternancia largo/corto.
- P2 (periodicidad): simulación del futuro con paso mensual (48 meses, 30/10/2026 → 30/10/2030);
  cuenta de margen liquidada mes a mes y agrupada en 16 trimestres (T1–T16); roll-over al cierre de
  cada trimestre.
- Pendiente para el Punto 9: roll en fechas del trimestre de inversión o alineado a los vencimientos
  CME (mar/jun/sep/dic).


## Dudas cerradas con el propio proyecto (01/11/2026)

- Tasa libre de riesgo: ^TNX (bono a 10 años), justificada en el Punto 10 (el enunciado la describe como 1–3 años, pero es el bono a 10 años).
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

## Punto 0 – Calidad de datos (v2, cerrado 10/11/2026)

- Opción B (decisión del estudiante): se conserva la descarga del 01/11/2026 para CSCO, ADI, ^NDX y ^TNX; AMGN se baja aparte el 10/11/2026 → data/raw/amgn_diario.csv (Close, Adj Close, Dividends, Stock Splits) + amgn_fecha_descarga.txt. Los CSV viejos no se modifican; PYPL se excluye al leerlos. Interruptores: ACTUALIZAR = False, BAJAR_AMGN = False.
- Justificación de las dos fechas: el ajuste del Adj Close es multiplicativo sobre toda la historia → no cambia los retornos de la ventana. Comprobado: CSCO y ADI dan idéntico a v1.
- Ventana 31/10/2016 → 30/10/2026: 2.514 días, 0 NaN (unión outer, sin desfases), 0 duplicados, 0 precios ≤ 0, mayor hueco 4 días. AMGN sin splits.
- Extremos conservados: ADI y ^NDX 16/03/2020 (COVID), CSCO 19/05/2022, AMGN 03/05/2024 (+11,17 % log; resultados del 1T-2024 y datos de MariTide; fuente: BioWorld, 03/05/2024).
- Dividendos (40 pagos en 10 años cada una; 4 en los últimos 12 m): q CSCO 1,60 % | ADI 1,03 % | AMGN 2,13 % (AMGN: USD 9,94 en 12 m).
- Retorno anual precio / total / aporte de dividendos: CSCO 13,08 / 16,44 / 3,37 pp | ADI 20,66 / 22,91 / 2,25 pp | AMGN 12,72 / 16,14 / 3,42 pp. AMGN coincide con el screening (16,14 %).
- Control nuevo: factor de ajuste de Yahoo vs. 1 − D/Close(t−1) en cada ex-dividendo → diferencia máxima < 0,01 pb en las tres.
- ^NDX: Adj Close = Close (índice de precio). ^TNX al 30/10/2026 = 4,929 % (sin cambio).

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

## Puntos 6–7 – Contrato (decisiones del 05/11/2026)

- Contrato: E-mini Nasdaq-100 (NQ), vencimiento dic-2026 (NQZ6). Fuente: CME Group (Contract Specs, Margins,
  Settlements), consulta 05/11/2026.
- Q_F = USD 20 × índice | tick = 0,25 pts = USD 5 | vencimientos mar/jun/sep/dic, 3.er viernes |
  liquidación en efectivo | NQZ6 vence el 18/12/2026.
- F₀ = 28.534,00 (settle NQZ6, 30/10/2026). Exposición por contrato = USD 570.680.
- VGM = USD 39.407 por contrato (columna corta, NQZ6). Vigente al 30/10/2026: ningún aviso de Equity de
  CME Clearing entre el 29/10 y el 05/11 (avisos 26-356, 26-361 y 26-363 no incluyen Equity).
- VGI₀ = 1,10 × VGM = USD 43.347,70 por contrato (regla de CME SPAN 2 para cuentas especulativas; supuesto
  conservador; para cuentas de cobertura CME exige VGI₀ = VGM). Estructura del curso: VGM = VGI₀ × 90,9 %.
- VGM fijo en USD durante los 4 años (no se usa la tabla de márgenes por vencimiento, porque es una foto
  actual y no un pronóstico de los márgenes futuros). Se explica en el notebook.
- Posición (R9): CORTA en 50 contratos NQZ6 (la entidad ya posee las acciones y teme una caída).
  Cubre solo el riesgo sistemático (56 % de la varianza, R² del Punto 4); el específico (44 %) no se cubre.
- Escenarios con ticks (sin riesgo de base, ΔV = βp·Δíndice·Vp): caída del 10 % → ΔF = −2,853.50 pts
  (−11,414 ticks × USD 250) → corto +USD 2,853,500 vs. acciones −USD 2,872,100 → neto −USD 18,600
  (residuo del redondeo de 0.33 contratos). Con largo, la pérdida sería −USD 5,725,600 (exposición duplicada).
  Archivo: data/processed/escenarios_ticks_R9.csv

## Puntos 8–12 (06/11/2026)

- P8: MBG mensual del ^NDX (Clase 1), 10,000 trayectorias, semilla 20261030; drift y σ = retornos log mensuales
  del ^NDX (120 m). F = S·e^{c(T−t)}, c implícito = ln(F0/S0)/T0 = 3.90 % (S0 = 28,384.85). Tabla con la
  trayectoria de precio final mediano (#849). Roll al cierre del mes anterior al vencimiento CME (nov/feb/may/ago).
  Resultado: P&G corto −USD 23.85 M; 9 llamados al margen; USD 24.72 M repuestos.
- P9: 17 contratos (NQZ6→NQZ0), 16 rolls. P&G = spot −29.36 M + base +5.51 M (roll yield por contango).
  Costos USD 7.247 por contrato y por lado (IBKR 0.85 + CME 1.386 + NFA 0.011 + 1 tick) → USD 12,320 en total.
  Portafolio cubierto: 4.43 % anual, vol 0.69 % (sin cobertura: 16.96 %, vol 14.99 %).
- P10: r_f = ^TNX 4.929 %; tasas efectivas: mensual 0.4018 %, trimestral 1.2101 %. E[V] a 4 años: cubierto
  USD 41.74 M (4.50 %) vs. libre de riesgo 42.43 M vs. sin cobertura 68.91 M (18.46 %). σ baja de 21.95 M
  a 1.81 M (−92 %). Llamados esperados 13.8; reposición esperada USD 32.0 M.
- P11: q portafolio = 1.25 % (CSCO 1.60 %, ADI 1.03 %, PYPL 0.98 %). Con dividendos: sin cobertura USD 71.38 M,
  cubierto USD 43.64 M (≈ 5.8 % anual > r_f). VaR 95 % del mes: 2.88 M sin cobertura vs. 1.79 M cubierto (−38 %).
- P12: N = 36 (β 0.6), 50 (base), 91 (β 1.5). Reducción de σ: 77 % / 92 % / 65 %. Mismos llamados esperados
  (13.8); la reposición escala con N.