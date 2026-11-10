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
  GMV preliminar del screening (diario, cotas 15–45 %): CSCO 40 / ADI 15 / AMGN 45 · σ ≈ 20,86 %. Reemplazado por el GMV mensual del Punto 3 v2.
  Riesgo identificado: deuda alta (compra de Horizon, 2023) y liquidez corriente ajustada → analizar en el P1 con deuda neta/EBITDA, cobertura de intereses y FCF.
- Finalistas descartadas: COST (mejor Sharpe en el GMV, pero P/E ~50×) y PANW (+98,6 % en 2026, pero P/E ~85× y sin dividendo).

Resultados INVALIDADOS por el cambio: todo lo de la v1 (PYPL, diario, Máx. Sharpe). Ya rehechos: P0 a P5 (10/11/2026; 01_portafolio completo) y P6–P12 (10/11/2026; 02_futuros_cobertura completo). No quedan puntos pendientes. Los resultados v1 quedan al final como referencia.

Decisiones del grupo (10/11/2026, después de la asesoría):
- Frecuencia MENSUAL (k = 12) en todo el laboratorio: estadística, Markowitz, VaR, betas y simulación. Lo diario solo como referencia. Razón: el VaR, la simulación y la liquidación de la cuenta de margen son mensuales; así no se mezclan unidades.
- Regla de pesos: las tres acciones participan con peso > 0 % y la suma es 100 % (sin ventas en corto y sin techo). Reemplaza las cotas 15–45 % de la v1. En el GMV mensual no cambia el resultado: los pesos ya quedaban entre 15 y 45 %.
- Coherencia temporal: toda la información (precios, fundamentales, EPS) con corte al 30/10/2026. Lo publicado después (p. ej. el T3-2026 de AMGN, 03/11/2026) no se usa.
- Lectura de datos: 00_datos guarda close_v2.csv, adj_v2.csv y divs_v2.csv en data/processed; 01 y 02 leen esos archivos.

## Organización del proyecto (01/11/2026)

- Repositorio con 3 notebooks: `00_datos` (Punto 0 / R4), `01_portafolio` (Puntos 1–5), `02_futuros_cobertura` (Puntos 6–12).
- Entrega: repositorio de GitHub + informe PDF en normas APA ubicado en la raíz, junto al README.md (resuelto).
- Entorno: Anaconda, environment `lab2-derivados` (Python 3.11) definido en `environment.yml`; `requirements.txt` se mantiene para quien use pip.
- La rúbrica (Excel) tiene erratas (S&P 500, 30/04/2026, USD 20M); las corrige el estudiante. Valen Nasdaq-100, 30/10/2026 y USD 35.000.000 (Clase 23).
- Las 3 acciones (CSCO, ADI, AMGN) pertenecen al Nasdaq-100 (lista de investing.com del 10/11/2026; citada en el Punto 1).
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
- Punto 9 (resuelto 10/11/2026): roll ALINEADO A CME, al cierre del mes anterior a cada vencimiento (nov/feb/may/ago).
  Con roll en fechas del trimestre de inversión no se podría arrancar con el NQZ6 (vence 18/12/2026, antes del cierre de T1).

## Dudas cerradas con el propio proyecto (01/11/2026)

- Tasa libre de riesgo: ^TNX (bono a 10 años), justificada en el Punto 10 (el enunciado la describe como 1–3 años, pero es el bono a 10 años).
- Márgenes: valores reales de CME en USD por contrato (el enunciado exige la información del contrato utilizado).
- Ticks: los precios del futuro se redondean al tick mínimo para contar ticks enteros (criterio del profesor, Clase 19).
- Punto 12: según el enunciado (prevalece), 0,6 y 1,5 son la beta del portafolio → N* = β · Vp / (F₀ · Q_F).
- VaR del Punto 4: VaR mensual del portafolio total (lo dice el enunciado).
- Decisiones del estudiante (no se le preguntan al profesor; se deciden en su punto): regla de los pesos (resuelto: > 0 % y suma 100 %), portafolio definitivo (resuelto en la asesoría: GMV), tratamiento de dividendos (Close vs. Adj Close), modelado del riesgo de base y costos del roll-over, construcción del enfoque "ajustado por VaR".

## Datos

- Ventana de estimación: 10 años (31/10/2016 → 30/10/2026). Mensual: 120 retornos (nov-2016 → oct-2026), precio del último día de bolsa de cada mes.
- Frecuencia: MENSUAL (k = 12) en todo el lab (decisión del 10/11/2026). Diaria solo como referencia. Retornos logarítmicos.
- Tipo de precio: Adj Close (retorno total). En el P11 se descompone: μ_total ≈ μ_precio (Close) + q (dividend yield), para no contar los dividendos dos veces.
- Anualización (solo para mostrar): μ = e^(r̄_m·12) − 1; σ = σ_m · √12. En los cálculos se usan los valores mensuales.

## Punto 0 – Calidad de datos (v2, cerrado 10/11/2026)

- Opción B (decisión del estudiante): se conserva la descarga del 01/11/2026 para CSCO, ADI, ^NDX y ^TNX; AMGN se baja aparte el 10/11/2026 → data/raw/amgn_diario.csv (Close, Adj Close, Dividends, Stock Splits) + amgn_fecha_descarga.txt. Los CSV viejos no se modifican; PYPL se excluye al leerlos. Interruptores: ACTUALIZAR = False, BAJAR_AMGN = False. Al final guarda close_v2, adj_v2 y divs_v2 en data/processed.
- Justificación de las dos fechas: el ajuste del Adj Close es multiplicativo sobre toda la historia → no cambia los retornos de la ventana. Comprobado: CSCO y ADI dan idéntico a v1.
- Ventana 31/10/2016 → 30/10/2026: 2.514 días, 0 NaN (unión outer, sin desfases), 0 duplicados, 0 precios ≤ 0, mayor hueco 4 días. AMGN sin splits.
- Extremos conservados: ADI y ^NDX 16/03/2020 (COVID), CSCO 19/05/2022, AMGN 03/05/2024 (+11,17 % log; resultados del 1T-2024 y datos de MariTide; fuente: BioWorld, 03/05/2024).
- Dividendos (40 pagos en 10 años cada una; 4 en los últimos 12 m): q CSCO 1,60 % | ADI 1,03 % | AMGN 2,13 % (AMGN: USD 9,94 en 12 m).
- Retorno anual precio / total / aporte de dividendos (mensual, k = 12): CSCO 13,04 / 16,40 / 3,36 pp | ADI 20,60 / 22,84 / 2,25 pp | AMGN 12,69 / 16,10 / 3,41 pp. (Con diarios era CSCO 13,08/16,44 · ADI 20,66/22,91 · AMGN 12,72/16,14.)
- Control nuevo: factor de ajuste de Yahoo vs. 1 − D/Close(t−1) en cada ex-dividendo → diferencia máxima < 0,01 pb en las tres.
- ^NDX: Adj Close = Close (índice de precio). ^TNX al 30/10/2026 = 4,929 % (sin cambio).

## Tasa libre de riesgo

- ^TNX al 30/10/2026: 4,929 % anual → r_f = 0,04929 (Yahoo Finance, cierre del 30/10/2026)
- Tasa mensual efectiva: (1,04929)^(1/12) − 1 = 0,4018 % (usada desde el P3) | Tasa trimestral: 1,2101 % | Justificación completa: Punto 10

## Punto 1 – Análisis fundamental (v2, cerrado 10/11/2026)

- Fuentes: precios Yahoo Finance; estados financieros trimestrales de Yahoo (10-Q/10-K ante la SEC), descargados el 10/11/2026 → data/raw/estados_trimestrales_v2.csv y fechas_resultados_v2.csv; consenso de EPS → data/raw/consenso_eps_v2.csv.
- Corte al 30/10/2026: últimos 4 trimestres PUBLICADOS antes del corte (CSCO y ADI hasta el trimestre publicado en ago-2026; AMGN hasta jun-2026, se excluye el T3-2026 publicado el 03/11). Limitación: el consenso de EPS es el del día de descarga (no hay histórico gratis).
- Evolución (retorno total 1 año): ADI +81,3 % | AMGN +64,0 % | CSCO +46,0 % | ^NDX +10,3 %. AMGN cerró en su máximo de 52 semanas (USD 466,01); peor caída del año: AMGN −16,6 % | CSCO −19,0 % | ADI −20,7 %. CSCO 19,6 % por debajo de su máximo.
- Deuda: deuda neta/EBITDA CSCO 0,68x | ADI 0,97x | AMGN 2,46x. Cobertura de intereses 11,89x | 14,41x | 4,86x. FCF/deuda neta 93,8 % | 72,6 % | 23,5 %. FCF/dividendos 1,95x | 2,42x | 1,93x. Razón corriente 0,93 | 1,25 | 1,37.
  AMGN: deuda neta USD 43.315 M, FCF USD 10.175 M, margen operativo 34,0 % → deuda alta pero pagable con su propia caja.
- Expectativa a 1 año (P/E constante × EPS esperado): CSCO 24,2x → USD 124,49 (+19,1 %) | ADI 37,0x → USD 611,25 (+46,5 %) | AMGN 20,8x → USD 520,66 (+11,7 %), rango 489,97–553,30. CSCO y ADI idénticos a v1.
- Rol: CSCO = estabilidad y renta | ADI = crecimiento | AMGN = defensa (salud, ρ baja, mayor dividendo 2,1 %).
- Archivos: fundamentales_v2.csv, expectativa_PE_v2.csv

## Punto 2 – Estadística descriptiva (v2, mensual)

- 120 retornos log mensuales (nov-2016 → oct-2026), Adj Close.
- Retorno anual: CSCO 16,40 % | ADI 22,84 % | AMGN 16,10 % | ^NDX 19,45 %
- Volatilidad anual: CSCO 24,14 % | ADI 27,99 % | AMGN 23,28 % | ^NDX 19,02 % (con diarios: 26,67 / 33,33 / 25,09 / 22,89)
- σ mensual: CSCO 6,97 % | ADI 8,08 % | AMGN 6,72 % | ^NDX 5,49 %
- Asimetría/curtosis cercanas a 0, salvo CSCO (curtosis 1,24 por may-2026 +27,5 %).
- ρ mensual: CSCO-ADI 0,37 | CSCO-AMGN 0,22 | ADI-AMGN 0,26 | con ^NDX: CSCO 0,57, ADI 0,60, AMGN 0,20
- Alerta: AMGN casi no se mueve con el índice → β baja (~0,24) → menor parte del riesgo cubrible con futuros del NDX.
- Archivos: retornos_mensuales_v2.csv, cov_mensual_v2.csv, corr_mensual_v2.csv

## Punto 3 – Markowitz (v2, GMV mensual)

- Σ mensual, μ_m = e^(r̄_m) − 1, r_f mensual 0,4018 %. Regla: pesos > 0 %, suma 100 %, sin cortos.
- **PORTAFOLIO DEFINITIVO: GMV** (asesoría 09/11/2026): CSCO 36,71 % | ADI 19,37 % | AMGN 43,92 %
  Montos: CSCO USD 12.849.261,83 | ADI USD 6.777.977,89 | AMGN USD 15.372.760,28
  μ_m 1,35 % (17,49 % anual) · σ_m 5,14 % (17,81 % anual) · Sharpe mensual 0,1848 (0,64 anual)
- Máx. Sharpe (solo comparación): CSCO 25,09 % | ADI 41,38 % | AMGN 33,53 % · μ_m 1,45 % · σ_m 5,41 % · Sharpe 0,1945
- Las tres participan sin forzar mínimos; con las cotas 15–45 % de la v1 daría lo mismo.
- β preliminar del GMV ≈ 0,54 (se confirma en el P5).
- Archivos: portafolios_markowitz_v2.csv · outputs/figures/frontera_eficiente_v2.png

## Punto 4 – VaR mensual (v2, GMV)

- Método: paramétrico normal con los 120 retornos log mensuales del GMV. r* = μp − z·σp; VaR % = 1 − e^(r*); VaR USD = V0 · VaR %. Comparado con VaR histórico y backtesting (binomial).
- μp mensual 1,3428 % (≈ USD 473.152 al mes) · σp mensual 5,1423 % · asimetría 0,03 · curtosis exceso −0,21.
- VaR 95 % (al 5 %): 6,87 % / USD 2.403.871,07 | VaR 99 % (al 1 %): 10,08 % / USD 3.526.392,10
- Histórico: 95 % 7,16 % (USD 2.504.910) | 99 % 8,50 % (poco confiable con 120 datos).
- Backtesting: 10 de 120 meses pasaron el VaR 95 % (esperados 6; p = 0,08, no se rechaza) y 0 el VaR 99 %. Peor mes: oct-2020 (−9,73 % log).
- Descomposición (modelo de mercado mensual): β = 0,5401, ρ = 0,58, R² = 0,3327 → 33 % sistemático (cubrible), 67 % específico. σ sistemática 2,97 % | σ específica 4,20 %.
- VaR con cobertura ideal: 95 % USD 1.895.079,46 (−21,2 %) | 99 % USD 2.829.339,33 (−19,8 %). Exposición a cubrir β × V0 ≈ USD 18.905.160.
- Lectura: el GMV arriesga menos sin cubrir (VaR 95 % 2,40 M vs. 2,88 M en v1), pero menos riesgo es cubrible (33 % vs. 56 %); cubierto queda parecido a la v1 (1,90 M vs. 1,79 M).
- Archivos: var_mensual_v2.csv, var_cubierto_vs_sin_v2.csv · outputs/figures/var_mensual_v2.png

## Punto 5 – Betas (v2, mensual)

- Método: regresión MCO de retornos log mensuales de cada acción contra el ^NDX (120 meses); βp = Σ wi·βi con los pesos del GMV (verificada por regresión directa: igual).
- β: CSCO 0,7173 (t 7,44; R² 32,0 %) | ADI 0,8774 (t 8,07; R² 35,6 %) | AMGN 0,2434 (t 2,21; R² 4,0 %)
- **β portafolio = 0,5401** (aportes: CSCO 48,7 % | ADI 31,5 % | AMGN 19,8 %).
- CAPM mensual (rf 0,4018 %, E(rm) 1,49 %): E(r) CAPM anual CSCO 15,17 % | ADI 17,57 % | AMGN 8,31 % | portafolio 12,56 % vs. histórico 16,40 / 22,84 / 16,10 / 17,49 %. α positivo en las tres.
- Exposición sistemática: βp × V0 = USD 18.905.159,95. ^NDX −10 % en un mes → portafolio ≈ −5,40 % (−USD 1,89 M); −20 % → −USD 3,78 M.
- Comparación v1: βp 0,82 (mensual, Máx. Sharpe con PYPL) → ahora 0,54: menos contratos, pero solo 33 % del riesgo es cubrible (R² del P4).
- Archivo: betas_capm_v2.csv

## Puntos 6–12 (v2)

### Punto 6 – Número óptimo de contratos (v2, cerrado 10/11/2026)

- Insumos leídos de los `_v2` (nada a mano): βp de betas_capm_v2.csv; pesos y montos de portafolios_markowitz_v2.csv (se verifica suma = V0 y pesos > 0); F₀ y Q_F de src/futuros.py.
- N* = βp·Vp / (F₀·Q_F) = 0,5401 × 35.000.000 / (28.534 × 20) = 18.905.159,98 / 570.680 = **33,1274**.
- **Decisión: 33 contratos CORTOS NQZ6 (redondeo hacia abajo).** Razón de cobertura 99,62 %; exposición cubierta USD 18.832.440; sin cubrir USD 72.719,98 (0,13 contratos). Con 34: 102,63 %, sobrecubre USD 497.960 → apuesta neta bajista (especular).
- Incertidumbre de β (regresión mensual del GMV vs. ^NDX, 120 m): EE 0,0704, IC 95 % [0,40; 0,68] → N* entre 24,7 y 41,6. Un contrato = 0,016 de β → el 0,13 del redondeo es despreciable frente al error de β.
- R² = 0,3327: los 33 contratos solo quitan la parte sistemática (1/3 de la varianza); el 67 % específico no se cubre con futuros del índice.
- v1 → v2: 50 → 33 contratos (β 0,82 → 0,54, por el peso de AMGN, β 0,24).
- Archivo: data/processed/contratos_optimos_v2.csv (insumo de P7–P12).

### Punto 7 – Contrato y posición (v2, cerrado 10/11/2026)

- Se mantienen del v1 las especificaciones (src/futuros.py, CME Group, consulta 05/11/2026): NQZ6, Q_F USD 20, tick 0,25 = USD 5, F₀ 28.534,00, VGM USD 39.407 (corto), VGI₀ = 1,10 × VGM = USD 43.347,70, liquidación en efectivo, MtM diario (mensual en el lab). docs/especificaciones_contrato.md diligenciado.
- NQ vs. MNQ (Q_F = 2): MNQ daría 331 contratos (99,92 % vs. 99,62 %) y 10.592 negociados en 16 rolls vs. 1.056 con NQ → se queda el NQ.
- Posición con N = 33: exposición cubierta USD 18.832.440 · VGI₀ total USD 1.430.474,10 · VGM total USD 1.300.431 · apalancamiento 13,17× · USD 165 por tick · franja 788,14 ticks (197 pts = 0,69 % de F₀). La franja en % es igual a la v1 (solo depende de VGI₀/VGM).
- En 120 meses de historia, el ^NDX subió más de 0,69 % en el 61 % de los meses → llamados al margen frecuentes; hay que tener caja aparte (P8).
- R9, escenarios con ticks (sin ruido específico): −10 % → ΔF −2.853,50 pts (−11.414 ticks) → corto +USD 1.883.310 vs. acciones −USD 1.890.516 → neto −USD 7.206 (redondeo). −20 % → neto −USD 14.577. Largo con −10 % → −USD 3.773.826 (duplica la exposición).
- R² 0,33: riesgo propio del portafolio 1σ mensual 4,22 % ≈ USD 1.476.437, no cubrible con el índice.
- Meses reales (escalados a V0 y F0): abr-2022 (^NDX −13,4 %) neto +USD 40.707; sep-2022 (−10,6 %) acciones −2,85 M, corto +2,00 M, neto −USD 858.475 (riesgo específico; pérdida −70 %); dic-2022 neto −USD 388.015. Alzas: jul-2022 +45.182; abr-2020 +2,55 M; abr-2026 +0,99 M.
- Archivos: posicion_futuros_v2.csv, escenarios_ticks_R9_v2.csv, meses_reales_cobertura_v2.csv.

### Punto 8 – Simulación y cuenta de margen (v2, cerrado 10/11/2026)

- Calibración del MBG (decisión del estudiante, opción C "como analista"): μ del mercado = r_f + ERP = 4,929 % + 4,41 % = 9,339 % anual (ERP implícito de Damodaran, NYU Stern, al 01/11/2026; usa el T-bond a 10 años como r_f, igual que ^TNX). El ^NDX es índice de precio → se resta q = 0,46 % (dividend yield del ETF QQQM, 2026). σ histórica mensual 5,4912 % (19,02 % anual). Δt = 1/12, 48 pasos, 10.000 trayectorias, semilla 20261030. Deriva log del índice 0,5550 % mensual.
  Por qué no A (histórica, ≈ 19,5 %): supone que se repite 2016–2026 con el NDX caro (P/E fwd ≈ 23, CAPE ≈ 59 a sep-2026, Siblis Research); gestoras esperan 4–6 % (Vanguard, Capital Group). Por qué no B (neutral al riesgo): sirve para valorar, no para proyectar (sin prima).
- Extremos S48/S0 (C): P5 0,70 · mediana 1,30 · P95 2,45 · máx. 5,42 · prob. < S0 23,7 %. (A: 1,10 / 2,03 / 3,82 / 8,45 / 3,2 %; B: 0,59 / 1,09 / 2,04 / 4,52 / 41,2 %) → calibracion_mbg_v2.csv.
- Futuro: F = S·e^{c(T−t)}, c = ln(F₀/S₀)/T₀ = 3,9039 %, redondeo al tick. Roll alineado a CME (al cierre de nov/feb/may/ago): NQZ6 → … → NQZ0 (17 contratos).
- Portafolio (opción 2b): r_p = r_f + β(r_m − r_f) + ε, r_m = retorno total (precio + q), β = 0,5401, σ_ε = 4,2184 % mensual, α = 0.
- **N = 33 fijo los 4 años (decisión del estudiante).** Se evaluó recalcular N en cada roll (bajaba la vol. mensual del cubierto de 6,86 % a 4,51 %; sin cobertura 5,20 %); se descartó.
- Peor escenario (decisión del estudiante): por el lado del MERCADO, para mostrar para qué sirven los futuros. Grupo de trayectorias con el ^NDX final entre P4 y P6 (principal, VaR 95 %) y entre P0,5 y P1,5 (sensibilidad, VaR 99 %); dentro del grupo, la de valor sin cobertura mediano.
  P5: trayectoria #835, ^NDX −27,2 % → sin cobertura USD 32,11 M (−2,89 M) · P&G corto +7,90 M · cubierto USD 40,01 M. Grupo (200 tray.): sin 33,45 M vs. cubierto 41,56 M.
  P1: #4659, ^NDX −45,8 % → sin 27,18 M (−7,82 M) · corto +11,00 M · cubierto 38,18 M. Grupo (100): 27,81 M vs. 38,74 M.
  Desempate (verificación del 10/11/2026): los grupos tienen 200 y 100 trayectorias (número par) y las dos del medio quedaban empatadas; según los decimales de cada computador salía #4659 o #9190 en el P1. Se fija con quantile(.5, interpolation="higher") en el 8.3 y el 8.8 → siempre #835 (P5) y #4659 (P1), los mismos de esta bitácora.
  El corto gana más que la pérdida de las acciones: β = 0,54 (parte r_f del portafolio no depende del mercado) + el corto se gana el costo de llevar (F > S). El cubierto queda cerca de r_f (35 M × 1,04929⁴ ≈ 42,43 M) → se retoma en el P10.
- Cuenta de margen (lógica del Excel de ejemplo y Clase 18; sin retiros, sin intereses, sin costos): escenario P5 → 1 llamado (mes 2, ^NDX +7,2 %, reposición USD 1.122.660), saldo final USD 10.454.489. P1 → 2 llamados, USD 770.385.
- Liquidez en las 10.000 trayectorias: llamados promedio 7,6 (mediana 7, P95 18); reposición total promedio USD 9,08 M (mediana 6,84 M, P95 26,16 M); mayor reposición en un mes promedio 2,22 M (P95 4,63 M). Costo real de la cobertura = liquidez cuando el mercado sube.
- Limitación (R² 0,33): si la pérdida viene de las propias acciones y no del mercado, el futuro no ayuda (ver 7.4).
- Archivos: calibracion_mbg_v2.csv, peor_escenario_v2.csv, cuenta_margen_mensual_v2.csv, cuenta_margen_mensual_p1_v2.csv, cuenta_margen_trimestral_v2.csv, liquidez_margen_v2.csv, simulacion_v2.npz · figuras simulacion_ndx_bandas_v2.png, peor_escenario_cubierto_v2.png.
- Presentación de la simulación (decisión del estudiante, 10/11/2026): se lee con la BANDA P5–P95 (≈ 19.958 – 69.517 puntos en oct-2030; mediana 37.031); P99 y máximo se reportan como colas con su probabilidad. No se recorta la cola de arriba (es la que genera los llamados al margen del corto).
  Validación: prob. de terminar por encima de S0 + 10.000 pts 46,5 % · 50.000 20,9 % · 70.000 4,8 % · 90.000 1,0 % · 100.000 0,4 %. Múltiplos a 4 años históricos 2016–2026 (73 ventanas de 48 m): mín. 1,41 · P5 1,53 · mediana 1,91 · P95 2,59 · máx. 2,77 vs. simulado: 0,28 · 0,70 · 1,30 · 2,45 · 5,42. Último cambio a 4 años del ^NDX: +16.979 puntos. → probabilidad_niveles_ndx_v2.csv, multiplos_4a_hist_vs_sim_v2.csv.
- 8.8 Comparativa C vs. B (mismo azar). **Se queda C.** B (μ = c): retorno total del mercado 4,44 % < r_f 4,929 % (prima −0,49 %, incoherente con el lab). E[V] a 4 años: C sin 47,69 M / cubierto 43,61 M (E[P&G corto] −4,09 M = prima a la que se renuncia); B sin 43,21 M / cubierto 43,23 M (E[P&G] ≈ 0). Prob. pérdida sin/cubierto: C 24,4 % / 29,2 %; B 33,9 % / 28,4 %. Peor escenario (P5 índice): C ^NDX −27,2 % → 32,11 / 40,01 M; B −39,4 % → 29,10 / 39,06 M. Llamados prom.: C 7,6 / B 5,6; reposición prom. 9,08 / 6,13 M (P95 26,16 / 19,12 M). → comparativa_B_vs_C_v2.csv.
- 8.3 sin notación científica (tabla formateada); se quitó la columna "% de la pérdida que compensa el futuro" (daba > 100 % y confundía).

### Punto 9 – Roll-over, base y costos (v2, cerrado 10/11/2026)

- Corto absoluto, N = 33 fijo, roll alineado a CME (cierre de nov/feb/may/ago): 17 contratos (NQZ6 → NQZ0), 16 rolls; NQZ6 dura 1 mes y NQZ0 2 meses. Se agrupa en trimestres de inversión T1–T16.
- P&G_k = (F_ap − F_ci)·Q_F·N = spot −Q_F·N·(S_ci − S_ap) + base Q_F·N·(b_ci − b_ap), b = S − F (Clase 20).
- Escenario principal (mercado en el P5, tray. #835): P&G realizado +7.901.355 (= suma mensual del P8) = spot +5.104.527 + base +2.796.828. Base al abrir ≈ −260 a −362 pts, al cerrar ≈ −40 a −65 (NQZ6 −149 → −54; NQZ0 cierra en −111). Spread promedio por roll 262,45 pts ≈ USD 173.219 (33 contratos).
- Costos: USD 7,247 por contrato y por lado (IBKR 0,85 + CME 1,386 + NFA 0,011 + 1 tick de deslizamiento, fuentes IBKR) × 1.122 lados = USD 8.131 (≈ 0,006 % anual).
- Rentabilidad en el escenario principal: sin cobertura −2,13 % anual (USD 32,11 M; vol. mensual 4,71 %; peor mes −11,99 %) vs. cubierto neto de costos +3,40 % anual (USD 40,01 M; vol. 4,24 %; peor mes −7,47 %).
- 10.000 trayectorias: E[P&G corto] −4,09 M = E[spot] −7,54 M + E[base] +3,46 M (P5–P95: 2,41–4,85 M) ≈ roll yield 2,38 % anual de V0; costos −8.131.
- Riesgo de base (sensibilidad a c): c 2,90 % → E[roll yield] 2,57 M, E[V cub neto] 42,71 M | c 3,90 % → 3,46 M, 43,60 M | c 4,90 % → 4,35 M, 44,49 M. ≈ USD 0,9 M por punto de c en 4 años.
- Archivos: rollover_contratos_v2.csv, resumen_rollover_v2.csv, rentabilidad_roll_escenario_v2.csv, aporte_roll_10000_v2.csv, sensibilidad_base_c_v2.csv · figura rollover_base_v2.png.

### Punto 10 – Valor esperado y r_f (v2, cerrado 10/11/2026)

- r_f = ^TNX 4,929 % (bono a 10 años, aunque el enunciado lo llame "1 to 3 Year"); se prefiere a ^IRX por horizonte de 4 años, indicación del profe y coherencia con el ERP de Damodaran. Efectiva mensual 0,4018 %, trimestral 1,2101 % (nominales capitalizadas darían 5,04 % anual).
- Valor esperado trimestral (10.000 tray., neto de costos): E[cobertura del trimestre] entre −0,20 M y −0,32 M; VP a r_f trimestral de los 16 trimestres = −USD 3.678.644 (precio esperado del seguro = prima de mercado a la que se renuncia; con B sería ≈ 0).
- A 4 años: E[V] sin 47,70 M (8,04 % anual) · cubierto 43,60 M (5,65 %) · r_f 42,43 M (4,929 %). Mediana cubierto 41,59 M (< r_f; la media > r_f por la dispersión del riesgo propio). σ final 17,45 → 14,57 M (−17 %). P5 24,91 vs. 23,65 M; P95 80,37 vs. 70,09 M. Prob. < 35 M: 24,4 % vs. 29,2 %. Prob. < r_f: 43,8 % vs. 52,4 %.
- Por quintiles del ^NDX a 4 años: Q1 (−21,7 %) sin 35,07 M vs. cub 41,80 M (+6,73 M) · Q2 (+7,2 %) 42,83 vs. 44,55 · Q3 (+30,8 %) 46,55 vs. 44,14 · Q4 (+59,5 %) 51,70 vs. 44,28 · Q5 (+125,5 %) 62,32 vs. 43,23 (−19,09 M). El cubierto queda en 41,8–44,6 M en todos.
- Conclusión: reduce la rentabilidad esperada (−4,1 M, 8,0 % → 5,6 %) y elimina casi todo el riesgo de MERCADO, pero la dispersión total baja solo 17 % y la prob. de pérdida no mejora: R² 0,33 (riesgo propio) + se entrega la prima. Liquidez: ver 8.7.
- Archivos: valor_esperado_trimestral_v2.csv, resumen_valor_esperado_v2.csv, valor_esperado_por_quintil_v2.csv · figura valor_esperado_cobertura_v2.png.

### Punto 11 – Tres enfoques y dividendos (v2, cerrado 10/11/2026)

- Dividendos 12 m (31/10/2025–30/10/2026) / precio 30/10/2026: CSCO 1,67 USD → 1,60 % · ADI 4,29 → 1,03 % · AMGN 9,94 → 2,13 %. Portafolio (pesos GMV) q = 1,7227 % anual → 0,1424 % mensual efectiva (≈ USD 49.852 el 1.er mes).
- Sin doble conteo: la simulación ya es retorno total (betas y VaR con Adj Close; mercado rinde r_f + ERP total) → los dividendos se separan, no se suman. r_total ≈ r_precio + q_m; D_t = E[V_{t−1}]·q_m. El corto en futuros no quita los dividendos.
- (a) Sin cobertura: rend. mensual 0,65 % (precio 0,50 % + div. 0,14 %) ≈ 8,04 % anual; E[V48] 47,69 M; dividendos cobrados 2,79 M.
- (b) Cubierto: 0,46 % mensual (precio 0,32 % + div. 0,14 %) ≈ 5,65 % anual (> r_f 4,93 %); E[V48] 43,60 M; dividendos 2,66 M.
- (c) Ajustado por VaR (decisión del estudiante: E[V_{t−1}]·(1 − VaR) con los VaR mensuales del P4): mes malo 95 % → pérdida 2,40 M sin vs. 1,90 M cubierto (−21 %); 99 % → 3,53 vs. 2,83 M. Valor a 4 años si el último mes es malo (95 %): 44,14 vs. 41,05 M.
- Chequeo: VaR 95 % del 1.er mes en la simulación 7,54 % sin / 6,24 % cubierto vs. P4 6,87 % / 5,41 % (el P4 usa la media histórica, más alta).
- Archivos: dividendos_v2.csv, tres_enfoques_mensual_v2.csv, resumen_tres_enfoques_v2.csv · figura tres_enfoques_mensual_v2.png.

### Punto 12 – Sensibilidad a la beta (v2, cerrado 10/11/2026)

- Misma fórmula, contrato, márgenes, roll y simulación (mismo índice y mismo ε, solo cambia β). Redondeo hacia abajo (criterio del P6).
- β 0,6: N* 36,80 → 36 (97,8 %) · exposición 21,0 M · VGI₀ 1,56 M · USD 180/tick · índice −10 %: acciones −2,10 M, corto +2,05 M, neto −45.480.
- β 0,5401: 33 (99,6 %) · 18,9 M · 1,43 M · USD 165/tick · neto −7.206.
- β 1,5: N* 91,997 → 91 (98,9 %; con 92 sobrecubriría solo USD 2.560, también defendible) · 52,5 M · VGI₀ 3,94 M · USD 455/tick · −10 %: −5,25 M vs. +5,19 M, neto −56.630.
- 10.000 tray.: E[V] sin/cub: β 0,6 48,19/43,73 M · β 0,54 47,69/43,60 · β 1,5 59,90/48,62. Reducción de σ: 19 % / 17 % / 45 %. Mercado muy malo (Q1): 34,21→41,55 · 35,07→41,80 · 23,79→42,35 M. Llamados prom. 7,6 en los tres; reposición prom. 9,91 / 9,08 / 25,04 M (P95 28,54 / 26,16 / 72,15 M).
- Lectura: β alta exige más contratos, garantía y caja, pero la cobertura sirve más (más riesgo es de mercado). Con N fijo y β 1,5 el cubierto aún rinde 8,6 % (la exposición crece con el mercado y la cobertura queda atrás).
- Archivos: sensibilidad_beta_v2.csv, sensibilidad_beta_montecarlo_v2.csv · figura sensibilidad_beta_v2.png.

### Cierre del notebook 02 (10/11/2026)

- 02_futuros_cobertura completo en v2 (P6–P12 + conclusión general reescrita). Run All sin errores en la ejecución de verificación.
- README actualizado con los supuestos de la simulación, la cobertura y las fuentes (Damodaran, IBKR).

---

# RESULTADOS v1 (CSCO, ADI, PYPL · diario · Máx. Sharpe) – INVALIDADOS, SOLO REFERENCIA

### v1 – Punto 1 – Análisis fundamental (cerrado 01/11/2026)

- Fuentes: precios de Yahoo Finance (Tabla 1.1); fundamentales de Yahoo Finance, últimos 12 meses, consultados el 01/11/2026 (`data/processed/fundamentales_yahoo.csv`); hechos de 2026 tomados de los comunicados de resultados (SEC 8-K) y de prensa.
- Evolución al 30/10/2026 (retorno total a 1 año): ADI +81.3 % | CSCO +46.0 % | PYPL −15.1 % | ^NDX +10.3 %.
- Decisión del estudiante: expectativa a 1 año por el método C, P/E constante × EPS ajustado esperado (consenso de Yahoo; año fiscal más cercano al 30/10/2027) (`data/processed/expectativa_precio_PE.csv`).
  - CSCO: P/E 24.2× → objetivo USD 124.49 (+19.1 %), rango 122.17–135.72
  - ADI: P/E 37.0× → objetivo USD 611.25 (+46.5 %), rango 531.33–666.78
  - PYPL: P/E 10.6× → objetivo USD 62.14 (+9.0 %), rango 56.06–64.19
- Rol en el portafolio: CSCO = estabilidad y renta | ADI = crecimiento | PYPL = valor y recuperación (candidata a peso menor).
- Las tres pagan dividendo: CSCO 1.6 % | ADI 1.1 % | PYPL 1.0 % (relevante para el Punto 11).
- Las tres tienen más deuda que caja (caja neta negativa, según Yahoo).

### v1 – Punto 2 – Estadística descriptiva

- Retornos log, Adj Close, ventana 01/11/2016 → 30/10/2026. Diaria: 2,513 obs. | Mensual: 120 obs.
- Retorno anual (diaria): CSCO 16.44 % | ADI 22.91 % | PYPL 3.31 % | ^NDX 19.51 %
- Volatilidad anual (diaria): CSCO 26.67 % | ADI 33.33 % | PYPL 39.73 % | ^NDX 22.89 %
- Volatilidad anual (mensual): CSCO 24.14 % | ADI 27.99 % | PYPL 36.23 % | ^NDX 19.02 %
- PYPL rinde por debajo de r_f (3.31 % < 4.929 %) → exceso de retorno negativo.
- Correlaciones diarias: CSCO-ADI 0.49 | CSCO-PYPL 0.35 | ADI-PYPL 0.45 | con ^NDX: CSCO 0.61, ADI 0.74, PYPL 0.62
- Correlaciones mensuales (más bajas): CSCO-ADI 0.37 | CSCO-PYPL 0.24 | ADI-PYPL 0.29
- Matriz Σ para Markowitz (P3): diaria × 252 (más precisa y más conservadora). Σ mensual × 12 para el VaR (P4).
- Archivos: retornos_diarios.csv, retornos_mensuales.csv, cov_anual_diaria.csv, cov_anual_mensual.csv, corr_diaria.csv

### v1 – Punto 3 – Markowitz

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

### v1 – Punto 4 – VaR mensual

- Método (decisión del estudiante): paramétrico normal con retornos log mensuales del portafolio Máx. Sharpe (120 meses). r* = μm − z·σm; VaR % = 1 − e^(r*); VaR USD = V0 · VaR %.
- μ mensual = 1.3182 % · σ mensual = 6.0200 % · ganancia esperada del mes ≈ USD 464,433
- VaR 95 % (al 5 %): 8.23 % / USD 2,878,978.61 | VaR 99 % (al 1 %): 11.91 % / USD 4,170,100.79
- Validación: 7 de 120 meses superaron el VaR 95 % (se esperaban 6); 0 superaron el VaR 99 %. Peor mes: abr-2022 (−12.07 % log). Asimetría 0.09, curtosis en exceso 0.25.
- Descomposición (modelo de mercado, mensual): β = 0.8206, R² = 0.5603 → 56 % sistemático (cubrible), 44 % específico. σ específica mensual = 3.99 %.
- VaR con cobertura ideal del riesgo sistemático: 95 % USD 1,789,466.95 (−37.84 %) | 99 % USD 2,680,797.33 (−35.71 %). Exposición a cubrir (β mensual × V0) ≈ USD 28,720,153.
- Archivos: var_mensual.csv, var_cubierto_vs_sin.csv · outputs/figures/var_mensual.png

### v1 – Punto 5 – Betas

- Método: regresión MCO de retornos log diarios de cada acción contra el ^NDX (01/11/2016 – 30/10/2026, 2,513 obs.); βp = Σ wi·βi con los pesos del Máx. Sharpe.
- β diaria: CSCO 0.7149 (t 38.9; R² 37.6 %) | ADI 1.0707 (t 54.4; R² 54.1 %) | PYPL 1.0839 (t 40.1; R² 39.0 %)
- **β portafolio = 0.9304** (verificada por regresión directa del portafolio contra el índice).
- β mensual (comparación): CSCO 0.7173 | ADI 0.8774 | PYPL 0.9258 | βp 0.8206 → la decisión de qué beta usar para N* se toma en el Punto 6.
- α anual: CSCO +2.49 % | ADI +1.55 % | PYPL −16.06 %. CAPM con E(rm) = 19.51 % y rf = 4.929 %: E(r) CAPM portafolio 18.49 % vs. histórico 17.39 %.
- Exposición sistemática: βp × V0 = 0.9304 × 35,000,000 ≈ USD 32,564,000 equivalentes en el índice; una caída de 10 % del ^NDX implica ≈ −9.30 % (≈ −USD 3.26 M).
- Archivo: data/processed/betas_capm.csv

### v1 – Puntos 6–7 – Contrato (decisiones del 05/11/2026)

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

### v1 – Puntos 8–12 (06/11/2026)

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
