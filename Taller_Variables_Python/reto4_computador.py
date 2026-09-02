nombre_cliente = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el producto: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))

subtotal = precio * cantidad
iva = subtotal * 0.19
total = subtotal + iva

print("-------- FACTURA --------")
print("Cliente:", nombre_cliente)
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Precio unitario: $", precio)
print("Subtotal: $", subtotal)
print("IVA: $", iva)
print("TOTAL: $", total)
