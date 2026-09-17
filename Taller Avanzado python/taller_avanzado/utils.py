import random


def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True


def obtener_divisores(numero: int) -> list[int]:
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


def clasificar_triangulo(lado1: float, lado2: float, lado3: float) -> str:
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return 'Los lados deben ser positivos.'
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return 'No forman un triángulo.'
    if lado1 == lado2 == lado3:
        return 'Equilátero'
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'Isósceles'
    return 'Escaleno'


def promedio_calificaciones(calificaciones: list[float]) -> float:
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def clasificar_promedio(promedio: float) -> str:
    if 0.0 <= promedio <= 2.9:
        return 'Reprobado'
    if 3.0 <= promedio <= 3.9:
        return 'Aprobado'
    if 4.0 <= promedio <= 4.5:
        return 'Sobresaliente'
    if 4.6 <= promedio <= 5.0:
        return 'Excelente'
    return 'Fuera de rango'


def decimal_a_binario(numero: int) -> str:
    if numero <= 0:
        raise ValueError('Debe ingresar un número entero positivo.')
    residuos = []
    n = numero
    while n > 0:
        residuos.append(str(n % 2))
        n //= 2
    return ''.join(reversed(residuos))


def generar_fibonacci(cantidad: int) -> list[int]:
    if cantidad <= 0:
        return []
    serie = []
    a, b = 0, 1
    for _ in range(cantidad):
        serie.append(a)
        a, b = b, a + b
    return serie


def calcular_descuento(tipo: str, cantidad: int, precio: float) -> float:
    subtotal = precio * cantidad
    if tipo.lower() == 'alimento':
        return subtotal * 0.05
    if tipo.lower() == 'aseo' and cantidad >= 3:
        return subtotal * 0.10
    return 0.0


def convertir_numero(valor: str) -> float:
    try:
        return float(valor)
    except ValueError as exc:
        raise ValueError('Debe ingresar un número válido.') from exc


def generar_patron(n: int) -> list[str]:
    if not 3 <= n <= 10:
        raise ValueError('El valor de n debe estar entre 3 y 10.')
    filas = []
    for fila in range(n - 1, 1, -1):
        valores = ' '.join(str(i) for i in range(2, fila + 1))
        filas.append(valores)
    return filas


def controlar_acceso(usuario: str, password: str) -> bool:
    return usuario == 'administrador' and password == 'Python2026'


def registrar_venta(
    cliente: str,
    cantidad_productos: int,
    precios: list[float],
    metodo_pago: str,
    descuento: float = 0.0,
) -> dict:
    subtotal = sum(precios)
    if cantidad_productos <= 0:
        raise ValueError('La cantidad de productos debe ser mayor que cero.')
    if any(precio <= 0 for precio in precios):
        raise ValueError('Los precios deben ser positivos.')

    total_bruto = subtotal
    valor_descuento = total_bruto * descuento
    cargo = 0.0
    if metodo_pago.lower() == 'tarjeta':
        cargo = total_bruto * 0.02
    elif metodo_pago.lower() == 'transferencia':
        cargo = 0.0
    elif metodo_pago.lower() == 'efectivo':
        cargo = 0.0
    else:
        raise ValueError('Medio de pago no válido.')

    total_recibido = total_bruto - valor_descuento + cargo
    return {
        'cliente': cliente,
        'cantidad_productos': cantidad_productos,
        'subtotal': total_bruto,
        'descuento': valor_descuento,
        'cargo': cargo,
        'total_recibido': total_recibido,
        'metodo_pago': metodo_pago,
    }
