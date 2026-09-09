def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad: "))
    nota = float(input("Ingrese la nota: "))

    estudiante = {
        'nombre': nombre,
        'edad': edad,
        'nota': nota,
    }
    estudiantes.append(estudiante)
    return estudiante
def promedio_notas(estudiantes):
    if not estudiantes:
        return 0
    return sum(estudiante['nota'] for estudiante in estudiantes) / len(estudiantes)
def mejor_estudiante(estudiantes):
    if not estudiantes:
        return None
    return max(estudiantes, key=lambda e: e['nota'])
def mostrar_reporte(estudiantes):
    print(f"Total estudiantes: {len(estudiantes)}")
    print(f"Promedio general: {promedio_notas(estudiantes):.2f}")
    mejor = mejor_estudiante(estudiantes)
    if mejor:
        print(f"Mejor estudiante: {mejor['nombre']} - Nota: {mejor['nota']} - Edad: {mejor['edad']}")
    else:
        print("Mejor estudiante: Ninguno")
if __name__ == '__main__':
    estudiantes = []
    cantidad = int(input("Cantidad de estudiantes a registrar: "))
    for _ in range(cantidad):
        agregar_estudiante(estudiantes)
    mostrar_reporte(estudiantes)
