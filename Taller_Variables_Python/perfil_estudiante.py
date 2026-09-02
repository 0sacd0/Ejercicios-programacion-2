estudiantes = "Sebastian Alessandro Carvajal Diaz y Laura Sharay Duarte Guerrero"
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = int(input("Ingrese la edad: "))
ciudad = input("Ingrese la ciudad: ")
universidad = input("Ingrese la universidad: ")
carrera = input("Ingrese la carrera: ")
semestre = int(input("Ingrese el semestre: "))
promedio = float(input("Ingrese el promedio: "))

nombre_completo = nombre + " " + apellido

print("========== PERFIL DEL ESTUDIANTE ==========")
print("Estudiantes:", estudiantes)
print("Nombre completo:", nombre_completo)
print("Edad:", edad)
print("Ciudad:", ciudad)
print("Universidad:", universidad)
print("Carrera:", carrera)
print("Semestre:", semestre)
print("Promedio:", promedio)
print("===========================================")
