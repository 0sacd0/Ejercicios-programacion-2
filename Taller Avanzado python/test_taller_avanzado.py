import pytest

from taller_avanzado import (
    clasificar_triangulo,
    controlar_acceso,
    decimal_a_binario,
    es_primo,
    generar_fibonacci,
    generar_patron,
)


def test_clasificar_triangulo():
    assert clasificar_triangulo(3, 3, 3) == 'Equilátero'
    assert clasificar_triangulo(5, 5, 3) == 'Isósceles'
    assert clasificar_triangulo(4, 5, 6) == 'Escaleno'
    assert clasificar_triangulo(1, 1, 3) == 'No forman un triángulo.'


def test_es_primo():
    assert es_primo(2) is True
    assert es_primo(7) is True
    assert es_primo(9) is False
    assert es_primo(1) is False


def test_decimal_a_binario():
    assert decimal_a_binario(25) == '11001'
    assert decimal_a_binario(10) == '1010'


def test_generar_fibonacci():
    assert generar_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_generar_patron():
    assert generar_patron(5) == ['2 3 4', '2 3', '2']


def test_controlar_acceso():
    assert controlar_acceso('administrador', 'Python2026') is True
    assert controlar_acceso('admin', 'Python2026') is False
