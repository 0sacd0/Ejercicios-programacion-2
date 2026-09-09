def buscar_producto(inventario, codigo):
    for producto in inventario:
        if producto[0] == codigo:
            return producto
    return None
def valor_total(inventario):
    total = 0
    for codigo, nombre, precio, cantidad in inventario:
        total += precio * cantidad
    return total
def actualizar_stock(inventario, codigo, nueva_cantidad):
    producto = buscar_producto(inventario, codigo)
    if producto is None:
        return False
    indice = inventario.index(producto)
    inventario[indice] = (producto[0], producto[1], producto[2], nueva_cantidad)
    return True
def mostrar_inventario(inventario):
    print("\nInventario actual:")
    print("Codigo\tNombre\tPrecio\tCantidad\tValor Total")
    for codigo, nombre, precio, cantidad in inventario:
        print(f"{codigo}\t{nombre}\t{precio}\t{cantidad}\t{precio * cantidad}")
if __name__ == '__main__':
    inventario = [
        ('A01', 'Laptop', 1200, 3),
        ('B02', 'Mouse', 50, 10),
        ('C03', 'Monitor', 300, 6),
    ]
    mostrar_inventario(inventario)
    print(f"Valor total: {valor_total(inventario)}")
    print(f"Buscar A01: {buscar_producto(inventario, 'A01')}")
    actualizar_stock(inventario, 'B02', 15)
    mostrar_inventario(inventario)
