# Especificaciones del contrato de futuros (Punto 7 / R7)

Fuente oficial: CME Group (CME Globex) · Fecha de consulta: 05/11/2026 · Enlaces: [Contract Specs](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html) · [Margins](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.margins.html) · [Settlements](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.settlements.html) · [CME SPAN 2](https://www.cmegroup.com/clearing/files/cme-span-2-margin-framework.pdf). Capturas en `docs/referencias/`.

| Parámetro | E-mini Nasdaq-100 (NQ) – elegido | Micro E-mini Nasdaq-100 (MNQ) – comparación |
|---|---|---|
| Activo subyacente | Nasdaq-100 (^NDX) | Nasdaq-100 (^NDX) |
| Vencimientos disponibles | mar, jun, sep, dic (tercer viernes) | mar, jun, sep, dic (tercer viernes) |
| Contrato usado al inicio | NQZ6 (vence 18/12/2026) | – |
| Multiplicador (Q_F) | USD 20 × índice | USD 2 × índice |
| Tick mínimo | 0,25 puntos | 0,25 puntos |
| Valor del tick | USD 5,00 por contrato | USD 0,50 por contrato |
| Precio inicial del futuro (30/10/2026) | 28.534,00 (settle NQZ6) | no se usa |
| Margen de mantenimiento (VGM) | USD 39.407 por contrato (posición corta NQZ6) | no consultado |
| Margen inicial (VGI₀) | USD 43.347,70 por contrato = 1,10 × VGM (supuesto, regla SPAN 2 de cuentas especulativas) | no consultado |
| Mecanismo de liquidación | en efectivo al vencimiento | en efectivo al vencimiento |
| Frecuencia de mark-to-market | diaria en CME; mensual en el laboratorio | diaria en CME |

Contrato elegido: NQ, 33 contratos cortos (N* = 33,13). Justificación: con la exposición sistemática del portafolio (USD 18,9 M) el MNQ exigiría 331 contratos y unos 10.600 negociados en los 16 roll-overs (vs. unos 1.060 con el NQ), para ganar solo 0,3 puntos de razón de cobertura (99,9 % vs. 99,6 %). El NQ es además el contrato más líquido del Nasdaq-100. Detalle en `notebooks/02_futuros_cobertura.ipynb`, Punto 7.
