# PENDIENTES PARA PREGUNTAR AL PROFESOR – LAB #2

Asesoría: **miércoles 4 de noviembre de 2026**. Entrega: miércoles 11 de noviembre a medianoche.
Estado: ⬜ pendiente · ✅ resuelto (anotar la respuesta y pasarla a `bitacora_decisiones.md`).

Aquí solo quedan las dudas de **interpretación del enunciado** que no se resuelven con el proyecto (enunciado, apuntes, Excel de ejemplo). Las decisiones metodológicas y de inversión las toma el estudiante y se registran en la bitácora.

---

## P1. Punto 9: ¿corto absoluto o cambio entre largo y corto en cada trimestre? ✅

- **Qué dicen las fuentes:**
  - Enunciado: "Suponga que la cobertura **en corto absoluto** y usando roll over basado en las simulaciones…, pero los contratos de futuros se renuevan trimestralmente".
  - Clase 23 (30/10): la novedad del lab es "un mark-to-market con rollover sobre una simulación, **cambiando entre largo y corto según la expectativa en cada trimestre**". El reto de la Clase 21 también pide "en cada liquidación cambie de posición según su expectativa de mercado".
- **Cuál es la confusión:** "corto absoluto" significa estar siempre en corto, y en clase se habló de alternar la posición. Son dos estrategias con resultados distintos, y el enunciado y lo dicho en clase no coinciden.
- **Por qué preguntar:** es el criterio R11 (10 %) y define toda la lógica del roll-over: cuántos contratos se cierran y abren, en qué dirección y con qué P&G realizado.
- **Pregunta:** "¿En el Punto 9 la cobertura es siempre en corto con roll-over trimestral, o en cada trimestre debemos decidir entre largo y corto según la expectativa? ¿O se esperan ambos escenarios comparados?"
- **Respuesta: La respuesta que me dió el profesor, fue que pensara en lo siguiente. Tú como inversionista esperas que lacción suba, no?; a lo que respondí que esa era la idea mínima de una inversión que esté por encima del precio en que compro algo, y me dijo que el corto era para mitigar esas caídas donde el precio se iba al suelo**
- **Decisión (05/11/2026):** opción A — cobertura **corta en todos los trimestres (corto absoluto)** con roll-over trimestral. El corto es un seguro de la cartera larga, no una apuesta de dirección; alternar a largo duplicaría la exposición. Coherente con el enunciado y con R9.

## P2. Periodicidad: ¿cuenta de margen mensual (48 meses) o trimestral (16 trimestres)? ✅

- **Qué dicen las fuentes:**
  - Enunciado: "la posición en futuros deberá evaluarse con **liquidaciones mensuales**", y en el Punto 8: "evalúe los flujos **trimestrales**… **Para cada mes**, calcule…".
  - Clase 23: "horizonte **trimestral a 4 años** (unos **16 datos**), no diario".
  - El Excel de ejemplo liquida por trimestres.
- **Cuál es la confusión:** el enunciado habla de liquidaciones mensuales, pero en clase se mencionaron 16 datos trimestrales y el ejemplo es trimestral. No queda claro si la tabla va mes a mes (48 filas agrupadas por trimestre) o trimestre a trimestre (16 filas).
- **Por qué preguntar:** cambia el paso de la simulación (mensual o trimestral), la cantidad de llamados al margen y el tamaño de las tablas de los Puntos 8 a 11 (R10, R11, R12 y R13 suman el 35 %).
- **Pregunta:** "¿La cuenta de margen del Punto 8 se liquida mensualmente (48 meses agrupados en 16 trimestres) o basta con 16 liquidaciones trimestrales?"
- **Respuesta: El profesor me dijo que la cuenta del margen la podría realizar en las liquidaciones ya sea mensuales o trimestrales, pero, podríamos realizar las liquidaciones mensuales y agrupandolas por trimestres**
- **Decisión (05/11/2026):** liquidación **mensual** (48 meses, 30/10/2026 → 30/10/2030) agrupada en 16 trimestres (T1–T16); roll-over al cierre de cada trimestre.

---

## Nota para el Punto 9 (decisión del estudiante, no se pregunta al profesor) ⬜
- Los futuros Nasdaq-100 de CME vencen en mar/jun/sep/dic (tercer viernes); los trimestres de inversión van oct→ene→abr→jul. Definir al desarrollar el Punto 9: roll en las fechas del trimestre de inversión (supuesto académico) o alineado a los vencimientos de CME.
