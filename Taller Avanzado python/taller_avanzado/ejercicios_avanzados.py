import random

from .utils import (
    controlar_acceso,
    decimal_a_binario,
    generar_fibonacci,
    generar_patron,
)


def ejecutar_ejercicio_7():
    print('\n=== Ejercicio 7: Decimal a binario ===')
    numero = int(input('Ingrese un número entero positivo: '))
    if numero <= 0:
        print('Debe ingresar un número positivo.')
        return
    print(f'Número binario: {decimal_a_binario(numero)}')


def ejecutar_ejercicio_8():
    print('\n=== Ejercicio 8: Serie de Fibonacci ===')
    cantidad = int(input('Ingrese la cantidad de términos: '))
    serie = generar_fibonacci(cantidad)
    print('Serie:', serie)
    print(f'Suma: {sum(serie)}')
    pares = sum(1 for n in serie if n % 2 == 0)
    impares = sum(1 for n in serie if n % 2 != 0)
    print(f'Términos pares: {pares}')
    print(f'Términos impares: {impares}')


def ejecutar_ejercicio_9():
    print('\n=== Ejercicio 9: Tabla de multiplicar avanzada ===')
    for tabla in range(1, 11):
        print(f'\nTABLA DEL {tabla}')
        for multiplicador in range(1, 11):
            print(f'{tabla} x {multiplicador} = {tabla * multiplicador}')


def ejecutar_ejercicio_10():
    print('\n=== Ejercicio 10: Patrón numérico ===')
    n = int(input('Ingrese un número entre 3 y 10: '))
    try:
        filas = generar_patron(n)
        for fila in filas:
            print(fila)
    except ValueError as exc:
        print(exc)


def ejecutar_ejercicio_11():
    print('\n=== Ejercicio 11: Juego de adivinanza con niveles ===')
    dificultad = input('Seleccione nivel (facil, intermedio, dificil): ').lower().strip()
    if dificultad == 'facil':
        rango_max = 20
        intentos = 6
    elif dificultad == 'intermedio':
        rango_max = 50
        intentos = 5
    elif dificultad == 'dificil':
        rango_max = 100
        intentos = 4
    else:
        print('Dificultad inválida.')
        return

    numero_secreto = random.randint(1, rango_max)
    for intento in range(1, intentos + 1):
        intento_usuario = int(input(f'Intento {intento}/{intentos}: ingrese un número: '))
        if intento_usuario == numero_secreto:
            print('Número correcto.')
            print(f'Puntaje: {((intentos - intento) * 20) + 20}')
            return
        if intento_usuario < numero_secreto:
            print('El número secreto es mayor.')
        else:
            print('El número secreto es menor.')
    print(f'No adivinaste. El número secreto era: {numero_secreto}')


def ejecutar_ejercicio_12():
    print('\n=== Ejercicio 12: Control de acceso ===')
    usuario_correcto = 'administrador'
    clave_correcta = 'Python2026'
    intentos = 3

    while intentos > 0:
        usuario = input('Usuario: ')
        clave = input('Contraseña: ')
        if usuario == usuario_correcto and clave == clave_correcta:
            print('Acceso concedido.')
            return
        intentos -= 1
        if usuario != usuario_correcto and clave != clave_correcta:
            print('Usuario y contraseña incorrectos.')
        elif usuario != usuario_correcto:
            print('Usuario incorrecto.')
        else:
            print('Contraseña incorrecta.')
        print(f'Intentos restantes: {intentos}')
    print('Sistema bloqueado. Demasiados intentos fallidos.')


def ejecutar_validacion_login():
    print('Validación rápida del acceso:')
    print(controlar_acceso('administrador', 'Python2026'))
