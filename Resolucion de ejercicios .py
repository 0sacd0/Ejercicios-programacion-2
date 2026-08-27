#Hecho por: Sebastian Alessandro Carvajal Diaz y Luara Sharay Duarte
#CODIGO EN FORMATO SPAGHETTI, ejecutar 1 por 1, no ejecutar todo el codigo a la vez, ya que se repiten variables y se sobreescriben



#Ejercicio 1 y 3 aplicados 
nombre = input("ingrese su nombre: ")
edad = int(input("Ingrese edad:"))
semestre = int(input("Ingrese semestre:"))
programa = input("ingrese Nombre de carrera:")
promedio = float(input("Ingrese promedio:"))
print("Hola", nombre , "Tienes",edad,"Años","estudias", programa , "en el semestre", semestre, "con un promedio de:",promedio)

#Ejercicio 2
print("-----------------------------------------")
print(type(nombre))
print(type(edad))
print(type(semestre))
print(type(programa))
print(type(promedio))

#ejercicio 4
print("-----------------------------------------")
print("Calculadora")
N1 = float(input("Ingrese Numero 1:"))
N2 = float(input("Ingrese Numero 2:"))
suma= N1+N2
resta=N1-N2
Mult = N1*N2
div = N1/N2
print ( "El Resuldatado de su suma es:", suma , ";El de la resta es: ", resta , "EL de la multiplicacion es:", Mult , "El resultadp de la division es: ", div)

#Ejercicio 5
print("-----------------------------------------")
A = 25
B = 15
print("Valor de A:", A , "Valor de B:", B)
A,B = B,A
print(" Nuevo Valor de A:", A , " Nuevo Valor de B:", B)

#Ejercicio 6
print("-----------------------------------------")
nombre = input("ingrese su nombre: ")
AN1 = int(input("Año de Nacimiento : "))
AN2 = int(input("Año Actual : "))
Edad2 = AN2 - AN1
print("Hola", nombre ,"tienes:", Edad2 , "Años")

#Ejercicio 7
print("-----------------------------------------")
nombreP = input("Nombre del producto: ")
CANT= int(input("Ingrese Cantidad del Producto:"))
PRE= int(input("Ingrese Precio del Producto Por Unidad:"))
TOTALP= CANT * PRE

print("Producto:", nombreP)
print("Cantidad:", CANT)
print("Precio Unitario:", PRE)
print("Pago total:", TOTALP)

#Ejercicio 8
print("-----------------------------------------")
print("Calculado de Notas")
NT1 = float(input("Ingrese nota 1: "))
NT2 = float(input("Ingrese nota 2: "))
NT3 = float(input("Ingrese nota 3: "))
NTC = (NT1+NT2+NT3)/3
print("Tu Promedio es:", NTC)

#Ejercicio 8 
print("-----------------------------------------")
print("Conversión de temperatura")
C = float(input("Ingrese Grados Celcios: "))
F = (C * 9/5) + 32
print(C, "Grados Celcios Equivalen a", F , "Grados Fahrenheit")

#Ejercicio 9

print("-----------------------------------------")
print("Conversor de Moneda")
MD = float(input("Ingrese Cantidad de dolares: "))
MDC = float(input("Ingrese valor de peso colombiano Actual: "))
CAM= MD * MDC
print("Tienes", MD , " DOlares que al cambio en peso colombiano que esta a ", MDC , "Te daria a un total de: ", CAM)

#RETOS PRACTICOS

#RETO 1
print("-----------------------------------------")
print("Nomina basica")
NOM = input("Ingrese su nombre: ")
VHOR= float(input("Ingrese el Valor de la hora: "))
CANTDH = int(input("ingrese cantidad de horas trabajadas: "))
NOMI = VHOR * CANTDH
print("Hola", NOM , "haz Trabajado", CANTDH , "Horas , se paga a", VHOR, "La hora por ende su nomina corresponde a: ", NOMI)

# RETO 2: FACTURA DE RESTAURANTE
print("-----------------------------------------")
print("Factura de restaurante")
cliente = input("Nombre del cliente: ")
valor_comida = float(input("Valor de la comida: "))
valor_bebidas = float(input("Valor de las bebidas: "))
subtotal = valor_comida + valor_bebidas
propina = subtotal * 0.10
total_pagar = subtotal + propina
print("Cliente:", cliente)
print("Subtotal: $", subtotal)
print("Propina (10%): $", propina)
print("Total a pagar: $", total_pagar)

# RETO 3: INDICE DE MASA CORPORAL
print("-----------------------------------------")
print("Indice de masa corporal")
nombre_imc = input("Nombre: ")
peso = float(input("Peso en kilogramos: "))
estatura = float(input("Estatura en metros: "))
imc = peso / (estatura ** 2)
print("Nombre:", nombre_imc)
print("IMC:", round(imc, 2))

# RETO 4: DATOS DE UN COMPUTADOR
print("-----------------------------------------")
print("Ficha del computador")
codigo_equipo = input("Codigo del equipo: ")
marca = input("Marca: ")
procesador = input("Procesador: ")
memoria_ram = input("Memoria RAM: ")
capacidad_disco = input("Capacidad del disco: ")
sistema_operativo = input("Sistema operativo: ")
estado_equipo = input("Estado del equipo: ")
print("\nCodigo:", codigo_equipo)
print("Marca:", marca)
print("Procesador:", procesador)
print("Memoria RAM:", memoria_ram)
print("Capacidad del disco:", capacidad_disco)
print("Sistema operativo:", sistema_operativo)
print("Estado:", estado_equipo)

# RETO INTEGRADOR: SISTEMA BASICO DE MATRICULA
print("-----------------------------------------")
codigo_estudiante = input("Codigo del estudiante: ")
nombre_estudiante = input("Nombre completo: ")
edad_estudiante = int(input("Edad: "))
programa_academico = input("Programa academico: ")
semestre_estudiante = int(input("Semestre: "))
materias_matriculadas = int(input("Numero de materias matriculadas: "))
valor_materia = float(input("Valor de cada materia: "))
total_matricula = materias_matriculadas * valor_materia
print("=================================")
print(" REGISTRO DE MATRICULA")
print("=================================")
print("Codigo:", codigo_estudiante)
print("Estudiante:", nombre_estudiante)
print("Edad:", edad_estudiante)
print("Programa:", programa_academico)
print("Semestre:", semestre_estudiante)
print("Materias:", materias_matriculadas)
print("Valor por materia: $", valor_materia)
print("Total matricula: $", total_matricula)
print("=================================")

# ACTIVIDAD DE ANALISIS
# input() devuelve texto; edad debe convertirse a int antes de sumar.
# nombre_analisis = input("Ingrese su nombre: ")
# edad_analisis = int(input("Ingrese su edad: "))
# nueva_edad = edad_analisis + 5
# print(nombre_analisis)
# print(nueva_edad)

# MINI DESAFIO: PERFIL DEL ESTUDIANTE
print("-----------------------------------------")
apellido = input("Apellido: ")
ciudad = input("Ciudad: ")
universidad = input("Universidad: ")
semestre_perfil = int(input("Semestre: "))
promedio_perfil = float(input("Promedio: "))
print("========== PERFIL DEL ESTUDIANTE ==========")
print("Nombre completo:", nombre, apellido)
print("Edad:", edad)
print("Ciudad:", ciudad)
print("Universidad:", universidad)
print("Carrera:", programa)
print("Semestre:", semestre_perfil)
print("Promedio:", promedio_perfil)
print("===========================================")






