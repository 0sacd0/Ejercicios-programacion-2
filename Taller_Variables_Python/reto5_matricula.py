nombre_vendedor = input("Ingrese el nombre del vendedor: ")
nombre_cliente = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el producto: ")
cantidad = int(input("Ingrese la cantidad: "))
precio_unitario = float(input("Ingrese el precio unitario: "))

subtotal = cantidad * precio_unitario
descuento = subtotal * 0.10
base = subtotal - descuento
iva = base * 0.19
total = base + iva

print("========== VENTA ==========")
print("Vendedor:", nombre_vendedor)
print("Cliente:", nombre_cliente)
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", descuento)
print("IVA: $", iva)
print("TOTAL A PAGAR: $", total)
