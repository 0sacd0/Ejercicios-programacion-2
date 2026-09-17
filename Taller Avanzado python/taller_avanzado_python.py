from taller_avanzado import (
    calcular_descuento,
    clasificar_promedio,
    clasificar_triangulo,
    controlar_acceso,
    decimal_a_binario,
    es_primo,
    generar_fibonacci,
    generar_patron,
    obtener_divisores,
    promedio_calificaciones,
    registrar_venta,
)
from taller_avanzado.menu import ejecutar_menu_principal

__all__ = [
    'es_primo',
    'obtener_divisores',
    'clasificar_triangulo',
    'promedio_calificaciones',
    'clasificar_promedio',
    'decimal_a_binario',
    'generar_fibonacci',
    'calcular_descuento',
    'generar_patron',
    'controlar_acceso',
    'registrar_venta',
    'ejecutar_menu_principal',
]


if __name__ == '__main__':
    ejecutar_menu_principal()
