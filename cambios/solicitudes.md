# Solicitudes de Cambio e Incidencias - Comercial De La Torre

## INC-014: Corrección de cálculo de subtotal (Registrado por De La Torre)
- **Descripción:** El sistema devuelve el precio unitario como subtotal, sin considerar la cantidad solicitada.
- **Tipo de cambio:** Correctivo.
- **Justificación:** La función actual no multiplica por la cantidad según revisión de De La Torre.
- **Archivos afectados:** `codigo/pedidos.py`.
- **Riesgo:** Bajo.
- **Criterio de aceptación:** Para precio 80 y cantidad 3, el subtotal debe ser 240.
- **Decisión de aprobación:** Aprobado por De La Torre.

## CR-015: Incorporación de cálculo de envío y total (Registrado por De La Torre)
- **Descripción:** La gerencia solicita incorporar el cálculo automático del costo de envío y el total del pedido según reglas RN-02, RN-03 y RN-04.
- **Tipo de cambio:** Perfectivo / Nueva funcionalidad.
- **Justificación:** Automatizar los cobros de envío según el análisis de De La Torre.
- **Archivos afectados:** `codigo/pedidos.py`, `documentos/requisitos.md`.
- **Riesgo:** Medio.
- **Criterio de aceptación:** Envío gratuito si subtotal >= 300, S/ 20 si es inferior.
- **Decisión de aprobación:** Aprobado por De La Torre.