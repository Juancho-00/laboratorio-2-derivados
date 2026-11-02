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
    ├── enunciado/              # enunciado, puntos y rúbrica
    └── referencias/            # Excel de ejemplo del curso
```

## Ejecución

1. Crear el entorno e instalar dependencias:
   - **Anaconda (recomendado):** `conda env create -f environment.yml` y luego `conda activate lab2-derivados`
   - **pip:** `pip install -r requirements.txt`
2. Abrir la carpeta en VS Code y ejecutar los notebooks **en orden**:
   `00_datos` → `01_portafolio` → `02_futuros_cobertura`
3. Los datos descargados quedan en `data/raw/` para reproducibilidad.

## Supuestos

- Liquidación de futuros **mensual** (en la práctica el mark-to-market es diario).
- **Roll-over trimestral** cuando los vencimientos no coinciden con el horizonte de cobertura.
- Sin ventas en corto (pesos ≥ 0) y suma de pesos = 1.
- Mercado para betas: ^NDX (Nasdaq-100), coherente con el futuro utilizado.
- *(se completa a medida que se toman decisiones; ver `docs/bitacora_decisiones.md`)*

## Fuentes

- Precios históricos: Yahoo Finance vía `yfinance` (fecha de descarga: ___).
- Componentes del índice: https://www.investing.com/indices/nq-100-components
- Especificaciones del futuro: CME Group (fecha de consulta: ___).
- Tasa libre de riesgo: ^TNX observada el 30/10/2026.
