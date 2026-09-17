from .utils import (
    clasificar_promedio,
    clasificar_triangulo,
    convertir_numero,
    es_primo,
    generar_patron,
    obtener_divisores,
    promedio_calificaciones,
)


def ejecutar_ejercicio_1():
    print('\n=== Ejercicio 1: Clasificación de triángulos ===')
    lados = []
    for i in range(1, 4):
        while True:
            valor = convertir_numero(input(f'Ingrese lado {i}: '))
            if valor > 0:
                lados.append(valor)
                break
            print('El lado debe ser positivo.')
    print('Resultado:', clasificar_triangulo(*lados))


def ejecutar_ejercicio_2():
    print('\n=== Ejercicio 2: Sistema de calificaciones ===')
    estudiantes = int(input('Cantidad de estudiantes: '))
    aprobados = 0
    reprobados = 0
    promedios = []
    for i in range(1, estudiantes + 1):
        calificaciones = []
        for j in range(1, 4):
            while True:
                nota = convertir_numero(input(f'Ingrese la nota {j} del estudiante {i}: '))
                if 0.0 <= nota <= 5.0:
                    calificaciones.append(nota)
                    break
                print('La nota debe estar entre 0.0 y 5.0.')
        promedio = promedio_calificaciones(calificaciones)
        promedios.append(promedio)
        categoria = clasificar_promedio(promedio)
        print(f'Estudiante {i}: promedio {promedio:.2f} => {categoria}')
        if categoria in ('Aprobado', 'Sobresaliente', 'Excelente'):
            aprobados += 1
        else:
            reprobados += 1
    print(f'Aprobados: {aprobados}')
    print(f'Reprobados: {reprobados}')
    print(f'Promedio general del grupo: {sum(promedios) / len(promedios):.2f}')
    print(f'Promedio más alto: {max(promedios):.2f}')
    print(f'Promedio más bajo: {min(promedios):.2f}')


def ejecutar_ejercicio_3():
    print('\n=== Ejercicio 3: Número primo ===')
    numero = int(input('Ingrese un número entero mayor que 1: '))
    if numero <= 1:
        print('El número debe ser mayor que 1.')
        return
    print('Es primo:', es_primo(numero))
    print('Divisores:', obtener_divisores(numero))


def ejecutar_ejercicio_4():
    print('\n=== Ejercicio 4: Cajero automático ===')
    saldo = 1500000.0
    depositos = 0
    retiros = 0
    historial = []

    while True:
        print('\nSALDO ACTUAL: $', saldo)
        print('1. Consultar saldo')
        print('2. Depositar dinero')
        print('3. Retirar dinero')
        print('4. Ver movimientos realizados')
        print('5. Salir')
        opcion = int(input('Seleccione una opción: '))

        if opcion == 1:
            print(f'Saldo disponible: ${saldo:,.0f}')
        elif opcion == 2:
            valor = float(input('Ingrese valor a depositar: '))
            if valor <= 0:
                print('No se permiten depósitos negativos.')
            else:
                saldo += valor
                depositos += 1
                historial.append(f'Depósito: ${valor:,.0f}')
        elif opcion == 3:
            valor = float(input('Ingrese valor a retirar: '))
            if valor < 10000:
                print('No se puede retirar una cantidad menor de $10.000.')
            elif valor > saldo:
                print('No se puede retirar más dinero del disponible.')
            else:
                saldo -= valor + 4500
                retiros += 1
                historial.append(f'Retiro: ${valor:,.0f} (costo $4.500)')
        elif opcion == 4:
            print('Movimientos realizados:')
            if not historial:
                print('No se han realizado movimientos.')
            else:
                for mov in historial:
                    print(mov)
            print(f'Depósitos: {depositos}')
            print(f'Retiros: {retiros}')
        elif opcion == 5:
            print('Gracias por usar el cajero.')
            break
        else:
            print('Opción inválida.')


def ejecutar_ejercicio_5():
    print('\n=== Ejercicio 5: Factura de supermercado ===')
    cantidad = int(input('Ingrese la cantidad de productos: '))
    subtotal_general = 0.0
    total_descuentos = 0.0
    detalles = []

    for i in range(1, cantidad + 1):
        nombre = input(f'Nombre del producto {i}: ')
        precio = float(input(f'Precio del producto {i}: '))
        unidades = int(input(f'Cantidad del producto {i}: '))
        tipo = input('Tipo de producto (alimento, aseo, otro): ').strip().lower()
        subtotal_producto = precio * unidades
        descuento = 0.0
        if tipo == 'alimento':
            descuento = subtotal_producto * 0.05
        elif tipo == 'aseo' and unidades >= 3:
            descuento = subtotal_producto * 0.10
        subtotal_general += subtotal_producto
        total_descuentos += descuento
        detalles.append((nombre, subtotal_producto, descuento))
        print(f'{nombre}: subtotal {subtotal_producto:.2f}, descuento {descuento:.2f}')

    if subtotal_general > 300000:
        descuento_general = subtotal_general * 0.05
        total_descuentos += descuento_general
        total_antes = subtotal_general
        total_definitivo = subtotal_general - total_descuentos
        print(f'Descuento adicional por compra mayor a $300.000: {descuento_general:.2f}')
    else:
        total_antes = subtotal_general
        total_definitivo = subtotal_general - total_descuentos
        print('No aplica descuento general.')

    print(f'Subtotal general: {subtotal_general:.2f}')
    print(f'Total de descuentos: {total_descuentos:.2f}')
    print(f'Total antes del descuento general: {total_antes:.2f}')
    print(f'Total definitivo: {total_definitivo:.2f}')


def ejecutar_ejercicio_6():
    print('\n=== Ejercicio 6: Estadísticas de números ===')
    numeros = []
    while True:
        valor = int(input('Ingrese un número entero (0 para terminar): '))
        if valor == 0:
            break
        numeros.append(valor)

    if not numeros:
        print('No se ingresaron números.')
        return

    if numeros[0] == 0:
        print('El primer valor ingresado es 0. No se puede calcular.')
        return

    print(f'Suma total: {sum(numeros)}')
    print(f'Promedio: {sum(numeros) / len(numeros):.2f}')
    print(f'Número mayor: {max(numeros)}')
    print(f'Número menor: {min(numeros)}')
