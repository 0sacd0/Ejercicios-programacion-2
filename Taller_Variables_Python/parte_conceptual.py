# TALLER DE PYTHON
# PARTE CONCEPTUAL: ARITMETICA, CADENAS E INPUT
# Estudiantes: Sebastian Alessandro Carvajal Diaz y Laura Sharay Duarte Guerrero

# 1. Que funcion se utiliza en Python para pedir datos al usuario?
# Se utiliza la funcion input().
# input() muestra un mensaje y espera que el usuario escriba un dato.
# El programa continua cuando el usuario presiona Enter.
#
# Ejemplo:
# nombre = input("Ingrese su nombre: ")
# print(nombre)

# 2. Que tipo de dato devuelve input() por defecto?
# input() siempre devuelve un dato de tipo str, es decir, texto.
# Aunque el usuario escriba un numero, Python lo recibe como texto.
#
# Ejemplo:
# edad = input("Ingrese su edad: ")
# print(type(edad))
# El resultado es: <class 'str'>

# 3. Diferencia entre int() y float()
# int() convierte un texto o numero en un numero entero.
# float() convierte un texto o numero en un numero decimal.
#
# Ejemplos:
# edad = int(input("Ingrese su edad: "))
# precio = float(input("Ingrese el precio: "))
# print(type(edad))
# print(type(precio))
#
# int("20") produce 20.
# float("20.5") produce 20.5.
# int("20.5") produce un error porque 20.5 no es un entero escrito correctamente.

# 4. Para que sirve el operador + cuando se trabaja con cadenas?
# Con numeros, + realiza una suma.
# Con cadenas de texto, + une o concatena los textos.
#
# Ejemplo con numeros:
# numero1 = 10
# numero2 = 5
# resultado = numero1 + numero2
# print(resultado)
# El resultado es 15.
#
# Ejemplo con cadenas:
# nombre = "Sebastian"
# apellido = "Carvajal"
# nombre_completo = nombre + " " + apellido
# print(nombre_completo)
# El resultado es Sebastian Carvajal.
#
# No se debe sumar directamente texto con numeros.
# edad = input("Ingrese su edad: ")
# nueva_edad = edad + 5
# Ese codigo produce un error porque edad es str y 5 es int.
# La correccion es convertir el dato antes de hacer la operacion.
# edad = int(input("Ingrese su edad: "))
# nueva_edad = edad + 5

# 5. Diferencia entre / y // en Python
# El operador / realiza una division normal y puede producir decimales.
# El operador // realiza una division entera y elimina la parte decimal.
#
# Ejemplo:
# resultado1 = 7 / 2
# resultado2 = 7 // 2
# print(resultado1)
# print(resultado2)
# resultado1 vale 3.5.
# resultado2 vale 3.