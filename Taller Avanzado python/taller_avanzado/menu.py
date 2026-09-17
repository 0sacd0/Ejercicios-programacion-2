from .ejercicios_avanzados import (
    ejecutar_ejercicio_10,
    ejecutar_ejercicio_11,
    ejecutar_ejercicio_12,
    ejecutar_ejercicio_7,
    ejecutar_ejercicio_8,
    ejecutar_ejercicio_9,
)
from .ejercicios_basicos import (
    ejecutar_ejercicio_1,
    ejecutar_ejercicio_2,
    ejecutar_ejercicio_3,
    ejecutar_ejercicio_4,
    ejecutar_ejercicio_5,
    ejecutar_ejercicio_6,
)
from .reto_integrador import sistema_ventas_integrador


def ejecutar_menu_principal():
    print('Taller avanzado de Python: if, for y while')
    while True:
        print('\nMENÚ PRINCIPAL')
        print('1. Ejercicio 1')
        print('2. Ejercicio 2')
        print('3. Ejercicio 3')
        print('4. Ejercicio 4')
        print('5. Ejercicio 5')
        print('6. Ejercicio 6')
        print('7. Ejercicio 7')
        print('8. Ejercicio 8')
        print('9. Ejercicio 9')
        print('10. Ejercicio 10')
        print('11. Ejercicio 11')
        print('12. Ejercicio 12')
        print('13. Reto integrador')
        print('0. Salir')

        opcion = int(input('Seleccione un ejercicio: '))
        if opcion == 1:
            ejecutar_ejercicio_1()
        elif opcion == 2:
            ejecutar_ejercicio_2()
        elif opcion == 3:
            ejecutar_ejercicio_3()
        elif opcion == 4:
            ejecutar_ejercicio_4()
        elif opcion == 5:
            ejecutar_ejercicio_5()
        elif opcion == 6:
            ejecutar_ejercicio_6()
        elif opcion == 7:
            ejecutar_ejercicio_7()
        elif opcion == 8:
            ejecutar_ejercicio_8()
        elif opcion == 9:
            ejecutar_ejercicio_9()
        elif opcion == 10:
            ejecutar_ejercicio_10()
        elif opcion == 11:
            ejecutar_ejercicio_11()
        elif opcion == 12:
            ejecutar_ejercicio_12()
        elif opcion == 13:
            sistema_ventas_integrador()
        elif opcion == 0:
            print('Hasta luego.')
            break
        else:
            print('Opción no válida.')
