def calcular_subtotal(precio, cantidad):
    # De La Torre: Cálculo del subtotal (RN-01)
    return precio * cantidad

def calcular_envio(subtotal):
    # De La Torre: Evaluación de reglas RN-02 y RN-03 para el costo de envío
    if subtotal >= 300:
        return 0
    else:
        return 20

precio = 80
cantidad = 3
# De La Torre: Procesamiento de valores del pedido
subtotal = calcular_subtotal(precio, cantidad)
envio = calcular_envio(subtotal)
total = subtotal + envio # De La Torre: Cálculo del total de la orden (RN-04)

print(f"Subtotal: S/ {subtotal}")
print(f"Envío: S/ {envio}")
print(f"Total: S/ {total}")
