# src/futuros.py — Especificaciones del contrato de cobertura: E-mini Nasdaq-100 (NQ)
# Fuentes (CME Group, consultadas el 05/11/2026):
#   - Contract Specs: https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html
#   - Margins:        https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.margins.html
#   - Settlements:    https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.settlements.html (trade date 30/10/2026)
#   - SPAN 2:         https://www.cmegroup.com/clearing/files/cme-span-2-margin-framework.pdf (regla IM = 1.1 × MM)
# Vigencia al 30/10/2026: ningún aviso de CME Clearing de márgenes de Equity entre el 29/10 y el 05/11/2026
# (avisos 26-356, 26-361 y 26-363 no incluyen Equity).

Q_F = 20                      # multiplicador: USD 20 por punto del índice
TICK = 0.25                   # variación mínima del precio, en puntos del índice
MARGEN_MANT = 39_407          # VGM por contrato: margen de mantenimiento CME, posición CORTA, NQZ6 (USD)
FACTOR_INICIAL = 1.10         # VGI₀ = 1.10 × VGM: tasa de cuenta especulativa (CME SPAN 2)
                              # Para cuentas de cobertura (hedge) CME exige VGI₀ = VGM; se usa 1.10 como
                              # supuesto conservador y para que exista franja entre VGI₀ y VGM (Clase 18).

NQ = {
    "codigo": "NQZ6",                         # contrato de diciembre 2026 (primer vencimiento después del 30/10/2026)
    "subyacente": "Nasdaq-100 (^NDX)",
    "Q_F": Q_F,
    "tick": TICK,
    "valor_tick": Q_F * TICK,                 # USD 5 por tick por contrato (Q_F × tick)
    "F0": 28_534.00,                          # settle del NQZ6 al 30/10/2026 (CME Group, Settlements)
    "margen_mant": MARGEN_MANT,               # VGM por contrato (USD), fijo durante los 4 años
    "margen_ini": FACTOR_INICIAL * MARGEN_MANT,  # VGI₀ por contrato = 43,347.70 USD
    "vencimiento": "2026-12-18",              # tercer viernes de diciembre, 8:30 a. m. CT
    "vencimientos": "mar, jun, sep, dic (tercer viernes)",
    "liquidacion": "en efectivo",
    "plataforma": "CME Globex (CME Group)",
}
