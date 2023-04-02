from mensajes.saludos.tipoHola import *
import numpy as np
import unittest

#"python setup.py test" para correr las pruebas del setup
class PruebasSaludos(unittest.TestCase):
    def test_generar_array(self):
        np.testing.assert_array_equal(
            np.array([0, 1, 2, 3, 4, 5]),
            generar_array(6))