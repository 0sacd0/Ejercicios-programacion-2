import unittest
from unittest.mock import patch
from src.ejercicios.ejercicio1 import agregar_estudiante, mejor_estudiante, promedio_notas
from src.ejercicios.ejercicio2 import actualizar_stock, buscar_producto, valor_total
from src.ejercicios.ejercicio3 import filtrar_ventas_altas, mejor_mes, promedio_general, total_mes
class TestEjercicios(unittest.TestCase):
    def test_ejercicio1(self):
        estudiantes = []
        with patch('builtins.input', side_effect=['Ana', '25', '9.5']):
            estudiante = agregar_estudiante(estudiantes)
        self.assertEqual(estudiante['nombre'], 'Ana')
        self.assertEqual(estudiante['edad'], 25)
        self.assertEqual(estudiante['nota'], 9.5)

        estudiantes = [
            {'nombre': 'Ana', 'edad': 25, 'nota': 9.5},
            {'nombre': 'Luis', 'edad': 22, 'nota': 8.0},
            {'nombre': 'Sofía', 'edad': 24, 'nota': 9.0},
        ]
        self.assertAlmostEqual(promedio_notas(estudiantes), 8.833333333333334)
        self.assertEqual(mejor_estudiante(estudiantes)['nombre'], 'Ana')
    def test_ejercicio2(self):
        inventario = [
            ('A01', 'Laptop', 1200, 3),
            ('B02', 'Mouse', 50, 10),
        ]
        self.assertEqual(buscar_producto(inventario, 'A01')[0], 'A01')
        self.assertEqual(valor_total(inventario), 4100)
        self.assertTrue(actualizar_stock(inventario, 'B02', 15))
        self.assertEqual(buscar_producto(inventario, 'B02')[3], 15)
    def test_ejercicio3(self):
        ventas = {
            'enero': [1200, 1500, 800, 900],
            'febrero': [1000, 1100, 1200],
            'marzo': [1800, 1700, 1600, 2000],
        }
        self.assertEqual(total_mes(ventas, 'enero'), 4400)
        self.assertAlmostEqual(promedio_general(ventas), 1345.4545454545455)
        self.assertEqual(mejor_mes(ventas), 'marzo')
        self.assertEqual(filtrar_ventas_altas(ventas, 1500), [1800, 1700, 1600, 2000])
if __name__ == '__main__':
    unittest.main()
