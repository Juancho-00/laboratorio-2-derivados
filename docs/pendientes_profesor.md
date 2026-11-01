# PENDIENTES PARA PREGUNTAR AL PROFESOR – LAB #2

Asesoría: **miércoles 4 de noviembre de 2026**. Entrega: miércoles 11 de noviembre a medianoche.
Estado: ⬜ pendiente · ✅ resuelto (anotar la respuesta y pasarla a `bitacora_decisiones.md`).

Prioridad: 🔴 bloquea el trabajo o cambia la entrega · 🟡 cambia cálculos · 🟢 confirmación.

---

## 🔴 P1. Formato de entrega: RPubs vs. GitHub + PDF APA ⬜
- **Qué dicen las fuentes:** en la Clase 23 (30/10) el profesor dijo que el laboratorio se entrega en **RPubs**, como el Lab #1. El enunciado no dice formato.
- **Cuál es la confusión:** RPubs está pensado para documentos de R (RStudio / R Markdown). Nuestro trabajo está en **Python** y pensamos entregarlo como **repositorio de GitHub** (3 notebooks + README) con un **PDF en normas APA**.
- **Por qué preguntar:** si no lo acepta, hay que cambiar el formato antes del día 11, y la entrega tardía vale 0.
- **Pregunta:** "Profe, ¿puedo entregar el enlace a un repositorio de GitHub con los notebooks en Python y un informe PDF en normas APA? ¿O es obligatorio publicar en RPubs? Si es obligatorio, ¿sirve subir un HTML exportado desde el notebook?"
- **Respuesta:**

## 🔴 P2. Punto 9: ¿corto absoluto o cambio entre largo y corto en cada trimestre? ⬜
- **Qué dicen las fuentes:**
  - Enunciado: "Suponga que la cobertura **en corto absoluto** y usando roll over basado en las simulaciones…, pero los contratos de futuros se renuevan trimestralmente".
  - Clase 23: la novedad del lab es "un mark-to-market con rollover sobre una simulación, **cambiando entre largo y corto según la expectativa en cada trimestre**". El reto de la Clase 21 también pide "en cada liquidación cambie de posición según su expectativa de mercado".
- **Cuál es la confusión:** "corto absoluto" significa estar siempre en corto, mientras que la clase sugiere alternar la posición. Son dos estrategias distintas con resultados distintos.
- **Por qué preguntar:** es el 10 % (R11) y define toda la lógica del roll-over.
- **Pregunta:** "¿En el Punto 9 la cobertura es siempre en corto con roll-over trimestral, o en cada trimestre debemos decidir entre largo y corto según la expectativa? ¿O se esperan ambos escenarios comparados?"
- **Respuesta:**

## 🟡 P3. Periodicidad: ¿tabla mensual (48 meses) o trimestral (16 trimestres)? ⬜
- **Qué dicen las fuentes:**
  - Enunciado: "la posición en futuros deberá evaluarse con **liquidaciones mensuales**" y en el Punto 8: "evalúe los flujos **trimestrales**… **Para cada mes**, calcule…".
  - Clase 23: "horizonte **trimestral a 4 años** (unos **16 datos**), no diario".
  - El Excel de ejemplo liquida por trimestres.
- **Cuál es la confusión:** no queda claro si la cuenta de margen va mes a mes (48 filas agrupadas por trimestre) o trimestre a trimestre (16 filas).
- **Por qué preguntar:** cambia la simulación (paso mensual o trimestral), la cantidad de llamados al margen y el tamaño de las tablas de los Puntos 8 a 11.
- **Pregunta:** "¿La cuenta de margen del Punto 8 se liquida mensualmente (48 meses agrupados en 16 trimestres) o basta con 16 liquidaciones trimestrales?"
- **Respuesta:**

## 🟡 P4. Riesgo de base y costos en el roll-over (exigidos por la rúbrica, no por el enunciado) ⬜
- **Qué dicen las fuentes:** el criterio R11 pide "evalúa ganancias/pérdidas realizadas, **riesgo de base, costos** y efecto sobre rentabilidad". El enunciado y el Punto 9 no mencionan ni la base ni los costos.
- **Cuál es la confusión:** para medir la base bₜ = Sₜ − Fₜ hay que simular **por separado** el índice (spot) y el futuro, o derivar el futuro del spot (por ejemplo, costo de mantenimiento F = S·e^{(r−q)T}). Tampoco se sabe qué costo de transacción suponer.
- **Por qué preguntar:** si no se incluye, se pierde puntaje en R11 (10 %); si se modela distinto a lo esperado, también.
- **Pregunta:** "Para el riesgo de base, ¿simulamos el índice y derivamos el futuro con el modelo de costo de mantenimiento, o simulamos ambos por separado? ¿Qué costo de transacción por contrato suponemos para el roll-over?"
- **Respuesta:**

## 🟡 P5. Tasa libre de riesgo: ^TNX está mal descrito en el enunciado ⬜
- **Qué dicen las fuentes:** el enunciado describe ^TNX como el "CBOE Interest Rate **1 to 3 Year** Treasury Index"; en realidad ^TNX es el rendimiento del Tesoro a **10 años**. El enunciado permite "una tasa equivalente de mercado".
- **Cuál es la confusión:** no sabemos si el profesor quiere la tasa de 10 años (^TNX) o una de 1 a 3 años (como sugiere la descripción).
- **Por qué preguntar:** cambia el Sharpe, el portafolio de máximo Sharpe, el CAPM trimestral y el valor esperado de la cobertura (Puntos 3, 10 y 11).
- **Pregunta:** "El enunciado describe ^TNX como Treasuries de 1 a 3 años, pero es el bono a 10 años. ¿Usamos ^TNX igual, justificando que el horizonte es de 4 años, o prefiere una tasa de 1 a 3 años?"
- **Respuesta:**

## 🟡 P6. VaR: ¿del portafolio o de las pérdidas y ganancias? ¿Cómo es el enfoque "ajustado por VaR"? ⬜
- **Qué dicen las fuentes:**
  - Enunciado, Punto 4: VaR mensual **del portafolio total** al 1 % y 5 %, en % y USD.
  - Clase 23: "más el VaR al 5 % **de las pérdidas y ganancias**".
  - Enunciado, Punto 11: valor esperado bajo el enfoque "(c) **ajustado por escenarios de VaR**".
  - El Excel de ejemplo calcula una columna "Daily VaR" y la usa dentro del valor de cartera trimestral.
- **Cuál es la confusión:** (1) si el VaR del 5 % que mencionó en clase es el del Punto 4 o un VaR adicional sobre los P&G de la cobertura; (2) cómo se construye el valor "ajustado por VaR" (¿valor esperado menos la pérdida VaR? ¿escenario pesimista?).
- **Por qué preguntar:** R5 (8 %) y R13 (6 %).
- **Pregunta:** "¿El VaR al 5 % de las pérdidas y ganancias es el mismo del Punto 4 o uno adicional sobre la cobertura? ¿Cómo quiere que se construya el valor del portafolio ajustado por VaR en el Punto 11?"
- **Respuesta:**

## 🟡 P7. Punto 12: ¿N* = β·P/F o fórmula de cambio de beta? ⬜
- **Qué dicen las fuentes:**
  - Enunciado: "si la beta del portafolio **toma los valores hipotéticos** β = 0,6 y β = 1,5… calcule el **nuevo número óptimo de contratos**". Eso sugiere recalcular N* = β·P/F.
  - Diapositivas (Clase 21) y Excel de ejemplo ("cambio de betas"): usan **(β − β*)·P/F** en corto y **(β* − β)·P/F** en largo, donde β* es una beta **objetivo** (el Excel usa 0,5 en corto y 3 en largo).
- **Cuál es la confusión:** ¿0,6 y 1,5 son la **beta del portafolio** (cobertura total con N* = β·P/F) o la **beta objetivo** a la que se quiere llevar el portafolio (cambio de beta)?
- **Por qué preguntar:** con β = 1,5 los dos métodos dan número de contratos y **posiciones distintos** (en el segundo, si βp < 1,5 la posición sería larga).
- **Pregunta:** "En el Punto 12, ¿0,6 y 1,5 reemplazan la beta del portafolio para recalcular N* = β·P/F, o son betas objetivo con la fórmula (β − β*)·P/F?"
- **Respuesta:**

## 🟡 P8. Ticks en la cuenta de margen ⬜
- **Qué dicen las fuentes:** R10 dice "mark-to-market y margin call **usando ticks**"; el Punto 7 del enunciado dice "usando los ticks de mercado". En la Clase 19 el ejemplo redondea el precio del futuro al tick para contar ticks enteros.
- **Cuál es la confusión:** si los precios simulados deben **redondearse al tick** (0,25 puntos en el futuro Nasdaq-100) antes de calcular el P&G, o si basta con expresar ΔF en ticks (con decimales).
- **Por qué preguntar:** es el criterio de mayor peso (R10, 12 %).
- **Pregunta:** "¿Los precios simulados del futuro se redondean al tick mínimo (0,25) para contar ticks enteros, como en el ejemplo USD/COP, o se acepta el número de ticks con decimales?"
- **Respuesta:**

## 🟡 P9. Márgenes: ¿valor real de CME o porcentaje como en el ejemplo? ⬜
- **Qué dicen las fuentes:** el enunciado exige tomar los márgenes de la fuente oficial; el Excel de ejemplo usa una garantía del **0,5 %** del nocional (apalancamiento de 200×) y un mantenimiento del 50 % de la garantía. CME publica los márgenes **en USD por contrato**.
- **Cuál es la confusión:** con márgenes reales de CME la relación inicial/mantenimiento no es del 50 %, y no sabemos si el profesor espera la convención del ejemplo.
- **Por qué preguntar:** cambia la frecuencia de los llamados al margen (R10) y el análisis de apalancamiento (R7).
- **Pregunta:** "¿Usamos el margen inicial y de mantenimiento reales de CME en USD por contrato, aunque el mantenimiento no sea el 50 % del inicial?"
- **Respuesta:**

## 🟢 P10. Restricciones de pesos en la optimización ⬜
- **Qué dicen las fuentes:** el Excel de ejemplo pone cotas de **10 % mínimo y 40 % máximo** por acción (semillas del Solver; la Clase 21 dice "establezca un mínimo y un máximo de peso"). Nuestro supuesto es solo pesos ≥ 0 y suma 1.
- **Cuál es la confusión:** si las cotas son obligatorias o una elección del estudiante.
- **Pregunta:** "¿Las cotas de peso mínimo y máximo son obligatorias o podemos justificar nuestras propias restricciones?"
- **Respuesta:**

## 🟢 P11. Dividendos: ¿precio ajustado o dividend yield explícito? ⬜
- **Qué dicen las fuentes:** Clase 23: "incluir los dividendos en el rendimiento esperado (si el dato es anual, pasarlo a trimestral)". R4 pide documentar el "tratamiento de dividendos".
- **Cuál es la confusión:** si los retornos históricos se calculan con **Adj Close** (que ya incluye dividendos), sumar después el dividend yield en el Punto 11 los **contaría dos veces**.
- **Pregunta:** "¿Calculamos los retornos con el precio de cierre sin ajustar y sumamos el dividend yield aparte, o usamos el precio ajustado y solo explicamos el efecto de los dividendos?"
- **Respuesta:**

## 🟢 P12. ¿Portafolio de máximo Sharpe, mínima varianza o ambos? ⬜
- **Qué dicen las fuentes:** el enunciado menciona "media-varianza… Sharpe Ratio" y también "portafolio óptimo de **mínima varianza**"; en la Clase 23 el profesor habló del "portafolio óptimo de Sharpe".
- **Cuál es la confusión:** cuál es el portafolio esperado como definitivo.
- **Pregunta:** "¿Es válido construir ambos (GMV y máximo Sharpe) y escoger uno con justificación, o espera uno en particular?"
- **Respuesta:**

## 🟢 P13. Confirmar las erratas de la rúbrica ⬜
- **Qué dicen las fuentes:** la rúbrica dice **S&P 500**, **30/04/2026** y **USD 20 millones**; en la Clase 23 el profesor dijo que valen Nasdaq, 30/10/2026 y USD 35 millones.
- **Por qué preguntar:** para que la calificación se haga con la versión corregida y quede constancia.
- **Pregunta:** "¿Nos confirma que la rúbrica se aplicará con Nasdaq, fecha 30/10/2026 y USD 35 millones?"
- **Respuesta:**
