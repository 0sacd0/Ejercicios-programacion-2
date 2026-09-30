TASA_ANUAL = 0.15
TASA_COMISION = 0.10

def leer_numero(mensaje, permitir_negativos=False):
    while True:
        try:
            valor = float(input(mensaje))
            if not permitir_negativos and valor < 0:
                print("Ingrese un valor mayor o igual a cero.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Escriba un número.")

def calcular_interes_mensual():
    capital = leer_numero("Ingrese el capital que desea invertir: $")
    tasa_mensual = (1 + TASA_ANUAL) ** (1 / 12) - 1
    interes = capital * tasa_mensual
    print(f"Interés ganado en un mes: ${interes:,.2f}")
    print(f"Capital al finalizar el mes: ${capital + interes:,.2f}")

def calcular_salario():
    sueldo_base = leer_numero("Ingrese el sueldo base del vendedor: $")
    ventas = []

    for numero in range(1, 4):
        venta = leer_numero(f"Ingrese el valor de la venta {numero}: $")
        ventas.append(venta)

    comision = sum(ventas) * TASA_COMISION
    salario_total = sueldo_base + comision
    print(f"Comisión total: ${comision:,.2f}")
    print(f"Salario del mes: ${salario_total:,.2f}")

def convertir_pesos_a_dolares():
    pesos = leer_numero("Ingrese la cantidad en pesos: $")
    valor_dolar = leer_numero("Ingrese el valor de 1 dólar en pesos: ")
    dolares = pesos / valor_dolar
    print(f"${pesos:,.2f} pesos equivalen a ${dolares:,.2f} dólares.")

def calcular_valor_absoluto():
    numero = leer_numero("Ingrese un número: ", permitir_negativos=True)
    print(f"El valor absoluto de {numero} es: {abs(numero)}")

def calcular_masa_de_aire():
    presion = leer_numero("Ingrese la presión: ")
    volumen = leer_numero("Ingrese el volumen: ")
    temperatura = leer_numero("Ingrese la temperatura: ")
    masa = (presion * volumen) / (0.37 * (temperatura + 460))
    print(f"La masa del aire es: {masa:.2f}")

def calcular_pulsaciones():
    edad = leer_numero("Ingrese la edad de la persona: ", permitir_negativos=False)
    pulsaciones = (220 - edad) / 10
    print(f"El número de pulsaciones por cada 10 segundos de ejercicio es: {pulsaciones:.2f}")

def main():
    while True:
        print("\n--- Ejercicios de control ---")
        print("1. Calcular interés de un mes")
        print("2. Calcular salario con comisiones")
        print("3. Convertir pesos a dólares")
        print("4. Valor absoluto")
        print("5. Masa de aire")
        print("6. Pulsaciones")
        print("7. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            calcular_interes_mensual()
        elif opcion == "2":
            calcular_salario()
        elif opcion == "3":
            convertir_pesos_a_dolares()
        elif opcion == "4":
            calcular_valor_absoluto()
        elif opcion == "5":
            calcular_masa_de_aire()
        elif opcion == "6":
            calcular_pulsaciones()
        elif opcion == "7":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Seleccione una opción del menú.")

if __name__ == "__main__":
    main()