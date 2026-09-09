from src.ejercicios.ejercicio1 import agregar_estudiante, mostrar_reporte
from src.ejercicios.ejercicio2 import mostrar_inventario, actualizar_stock, valor_total
from src.ejercicios.ejercicio3 import reporte_final
if __name__ == '__main__':
    print("=== Ejercicio 1 ===")
    estudiantes = []
    cantidad = int(input("Cantidad de estudiantes a registrar: "))
    for _ in range(cantidad):
        agregar_estudiante(estudiantes)
    mostrar_reporte(estudiantes)

    print("\n=== Ejercicio 2 ===")
    inventario = [
        ('A01', 'Laptop', 1200, 3),
        ('B02', 'Mouse', 50, 10),
        ('C03', 'Monitor', 300, 6),
    ]
    mostrar_inventario(inventario)
    print(f"Valor total: {valor_total(inventario)}")
    actualizar_stock(inventario, 'B02', 15)
    mostrar_inventario(inventario)

    print("\n=== Ejercicio 3 ===")
    ventas = {
        'enero': [1200, 1500, 800, 900],
        'febrero': [1000, 1100, 1200],
        'marzo': [1800, 1700, 1600, 2000],
    }
    reporte_final(ventas)
