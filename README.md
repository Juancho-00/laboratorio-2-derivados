# Lab #2 – Derivados Financieros: Portafolio Nasdaq-100 + Cobertura con Futuros

**Autor:** John Zapata, Jovan Marin, Juan Pablo Quintero · Ingeniería Financiera, ITM · Derivados Financieros (Prof. David Rodríguez) · 2026-2

## Descripción

> Versión 2 (rama `v2-asesoria`), con los cambios de la asesoría del 09/11/2026: AMGN reemplaza a PYPL, portafolio de mínima varianza y todo en frecuencia mensual. La versión 1 queda en `main`.

Diseño de una estrategia de inversión de **USD 35.000.000** en tres acciones del Nasdaq-100
(**CSCO**, **ADI**, **AMGN**), iniciada el **30/10/2026** con horizonte de **4 años**, y su cobertura
con **futuros sobre el índice Nasdaq-100** (CME Group): análisis fundamental, optimización
media-varianza, VaR, betas CAPM, número óptimo de contratos, cuenta de margen por ticks,
roll-over trimestral y sensibilidad a la beta.

## Estructura del repositorio

```
├── README.md
├── Informe_Lab2_APA.pdf        # informe final en normas APA (se agrega al final)
├── environment.yml             # entorno de Anaconda
├── requirements.txt
├── data/
│   ├── raw/                    # descargas sin modificar (precios, dividendos, ^TNX)
│   └── processed/              # retornos y series derivadas
├── notebooks/
│   ├── 00_datos.ipynb          # Punto 0: descarga y calidad de datos
│   ├── 00_screening_reemplazo.ipynb  # filtro del Nasdaq-100 para reemplazar PYPL (asesoría 09/11)
│   ├── 01_portafolio.ipynb     # Puntos 1–5: fundamental, estadística, Markowitz, VaR, betas
│   └── 02_futuros_cobertura.ipynb  # Puntos 6–12: futuros, margen, roll-over, sensibilidad
├── src/
│   └── futuros.py              # funciones reutilizables
├── outputs/
│   ├── figures/
│   └── tables/
└── docs/
    ├── bitacora_decisiones.md
    ├── pendientes_profesor.md
    ├── especificaciones_contrato.md
    ├── enunciado/              # Preguntas_Lab2.md (rúbrica + enunciado literal) y rúbrica en Excel
    └── referencias/            # Excel de ejemplo del curso
```

## Ejecución

1. Crear el entorno e instalar dependencias:
   - **Anaconda (recomendado):** `conda env create -f environment.yml` y luego `conda activate lab2-derivados`
   - **pip:** `pip install -r requirements.txt`
2. Abrir la carpeta en VS Code y ejecutar los notebooks **en orden**:
   `00_datos` → `01_portafolio` → `02_futuros_cobertura`
3. Los datos de `data/raw/` (descarga del 01/11/2026; AMGN y estados financieros del 10/11/2026) se leen desde disco: los notebooks no vuelven a consultar Yahoo (`ACTUALIZAR = False` y `BAJAR_AMGN = False` en `00_datos`; los estados financieros y el consenso de EPS solo se descargan si el CSV no existe), así que los resultados son reproducibles. `00_datos` guarda `close_v2.csv`, `adj_v2.csv` y `divs_v2.csv` en `data/processed/`, que son los que leen los demás notebooks.

## Supuestos

- Liquidación de futuros **mensual** (en la práctica el mark-to-market es diario).
- **Roll-over trimestral** cuando los vencimientos no coinciden con el horizonte de cobertura.
- Datos: 10 años (31/10/2016 – 30/10/2026), precios Adj Close (retorno total), retornos logarítmicos.
- Frecuencia: **mensual** (k = 12, 120 retornos) en todo el laboratorio: estadística, Markowitz, VaR, betas y simulación. Lo diario solo como referencia.
- Optimización: las tres acciones con peso mayor a 0 %, suma = 100 %, sin ventas en corto. Portafolio elegido: **mínima varianza (GMV)** (CSCO 36,71 % · ADI 19,37 % · AMGN 43,92 %). El de máximo Sharpe se muestra solo para comparar.
- Tasa libre de riesgo: ^TNX al 30/10/2026 = 4,929 % anual (0,4018 % mensual efectiva).
- Coherencia temporal: toda la información con corte al 30/10/2026; los fundamentales usan los últimos 4 trimestres publicados antes de esa fecha.
- Expectativa de precio a 1 año: P/E constante × EPS esperado (consenso de analistas en Yahoo Finance).
- VaR mensual paramétrico (normal) al 95 % y 99 %.
- Mercado para betas: ^NDX (Nasdaq-100), coherente con el futuro utilizado; betas por regresión con datos mensuales.
- Cobertura: E-mini Nasdaq-100 (NQZ6, CME Group). N* = βp·Vp / (F₀·Q_F) = 33,13 → **33 contratos cortos** (redondeo hacia abajo: cubrir sin sobrecubrir; la diferencia es menor que el error de estimación de la β). Solo se cubre el riesgo sistemático (R² = 0,33 con el ^NDX).
- Márgenes: VGM de CME (USD 39.407 por contrato, posición corta NQZ6) fijo los 4 años; VGI₀ = 1,10 × VGM (regla CME SPAN 2).
- Simulación (Puntos 8–12): MBG mensual (Δt = 1/12, 48 meses, 10.000 trayectorias, semilla 20261030) del ^NDX con μ = r_f + ERP (ERP implícito de Damodaran al 01/11/2026 = 4,41 %) menos el dividend yield del índice (0,46 %) y σ histórica mensual. Se lee con la banda P5–P95. Futuro: F = S·e^{c(T−t)}, con c implícito en F₀/S₀.
- Portafolio simulado con el modelo de mercado: r_p = r_f + β(r_m − r_f) + ε (β = 0,54, σ_ε = 4,22 % mensual, α = 0); ya es retorno total (incluye dividendos).
- Cobertura: corto absoluto, N = 33 fijo, roll alineado a los vencimientos de CME (cierre de nov/feb/may/ago; 17 contratos, 16 rolls), liquidación mensual por ticks. Costos USD 7,247 por contrato y por lado (IBKR + CME + NFA + 1 tick).
- Peor escenario: por caída del mercado (percentil 5 del índice a 4 años; percentil 1 como sensibilidad).
- Detalle de cada decisión y resultado: `docs/bitacora_decisiones.md`.

## Fuentes

- Precios históricos: Yahoo Finance vía `yfinance` (CSCO, ADI, ^NDX y ^TNX descargados el 01/11/2026; AMGN el 10/11/2026; los CSV de `data/raw/` son la versión usada).
- Componentes del índice: https://www.investing.com/indices/nq-100-components (consultada el 10/11/2026)
- Especificaciones del futuro: CME Group (fecha de consulta: 05/11/2026).
- Prima de riesgo de mercado: ERP implícito de A. Damodaran (NYU Stern) al 01/11/2026, https://pages.stern.nyu.edu/adamodar/
- Comisiones de futuros: Interactive Brokers (comisión, tarifa CME Globex y NFA).
- Tasa libre de riesgo: ^TNX observada el 30/10/2026 (Yahoo Finance).
- Fundamentales: estados trimestrales de Yahoo Finance (reportes 10-Q/10-K ante la SEC), descargados el 10/11/2026 con corte al 30/10/2026. Consenso de EPS: Yahoo Finance, 10/11/2026.
- Hechos corporativos de 2026: comunicados de resultados de cada empresa (SEC, formularios 8-K) y prensa financiera (citados en el notebook 01).
