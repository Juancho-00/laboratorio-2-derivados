# Lab #2 – Derivados Financieros: Portafolio Nasdaq-100 + Cobertura con Futuros

**Autor:** John Zapata, Jovan Marin, Juan Pablo Quintero · Ingeniería Financiera, ITM · Derivados Financieros (Prof. David Rodríguez) · 2026-2

## Descripción

Diseño de una estrategia de inversión de **USD 35.000.000** en tres acciones del Nasdaq-100
(**CSCO**, **ADI**, **PYPL**), iniciada el **30/10/2026** con horizonte de **4 años**, y su cobertura
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
    ├── enunciado/              # Referencia_Lab2.md (enunciado + rúbrica unificados) y rúbrica en Excel
    └── referencias/            # Excel de ejemplo del curso
```

## Ejecución

1. Crear el entorno e instalar dependencias:
   - **Anaconda (recomendado):** `conda env create -f environment.yml` y luego `conda activate lab2-derivados`
   - **pip:** `pip install -r requirements.txt`
2. Abrir la carpeta en VS Code y ejecutar los notebooks **en orden**:
   `00_datos` → `01_portafolio` → `02_futuros_cobertura`
3. Los datos de `data/raw/` (descarga del 01/11/2026) y la foto de fundamentales de `data/processed/` se leen desde disco: los notebooks no vuelven a consultar Yahoo (`ACTUALIZAR = False` en `00_datos`), así que los resultados son reproducibles.

## Supuestos

- Liquidación de futuros **mensual** (en la práctica el mark-to-market es diario).
- **Roll-over trimestral** cuando los vencimientos no coinciden con el horizonte de cobertura.
- Datos: 10 años (31/10/2016 – 30/10/2026), precios Adj Close (retorno total), retornos logarítmicos.
- Frecuencia: diaria (k = 252) para estadística, Markowitz y betas; mensual (k = 12) para VaR y simulación.
- Optimización: pesos entre 15 % y 45 % por acción, suma = 1, sin ventas en corto. Portafolio elegido: **Máximo Sharpe** (CSCO 40 % · ADI 45 % · PYPL 15 %).
- Tasa libre de riesgo: ^TNX al 30/10/2026 = 4.929 % anual.
- Expectativa de precio a 1 año: P/E constante × EPS esperado (consenso de analistas en Yahoo Finance).
- VaR mensual paramétrico (normal) al 95 % y 99 %.
- Mercado para betas: ^NDX (Nasdaq-100), coherente con el futuro utilizado; betas por regresión con datos diarios.
- Detalle de cada decisión y resultado: `docs/bitacora_decisiones.md`.

## Fuentes

- Precios históricos: Yahoo Finance vía `yfinance` (descarga del 01/11/2026; los CSV de `data/raw/` son la versión usada).
- Componentes del índice: https://www.investing.com/indices/nq-100-components
- Especificaciones del futuro: CME Group (fecha de consulta: ___).
- Tasa libre de riesgo: ^TNX observada el 30/10/2026 (Yahoo Finance).
- Fundamentales y consenso de EPS: Yahoo Finance, consultados el 01/11/2026 (`data/processed/`).
- Hechos corporativos de 2026: comunicados de resultados de cada empresa (SEC, formularios 8-K) y prensa financiera (citados en el notebook 01).
