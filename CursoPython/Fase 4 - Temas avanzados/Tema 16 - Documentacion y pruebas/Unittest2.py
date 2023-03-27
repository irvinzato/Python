import unittest

class PruebasMetodosCadenas(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('Hola'.upper(), 'HOLA')

    def test_isupper(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('hola'.isupper())

    def test_split(self):
        cadena = "Hola Irving"
        self.assertEqual(cadena.split(" "), ['Hola', 'Irving'])

if __name__ == "__main__":
    unittest.main()