import unittest
from Calculadora import Calculadora

#Ejecutar UnitTest con "python -m unittest TDDCalculadora.py"
class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calculadora = Calculadora()

    def test_valor_inicial(self):
        self.assertEqual(self.calculadora.value, 0)

    def test_sumar(self):
        self.assertEqual(self.calculadora.add(1, 3), 4)