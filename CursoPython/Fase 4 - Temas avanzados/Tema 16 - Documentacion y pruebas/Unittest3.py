import unittest

def doblar(a): return a * 2

class PruebaTestFixture(unittest.TestCase):

    def setUp(self): #Función especial dentro de las pruebas como el "beforeEach" en Java
        print("Preparando el contexto(ambiente)")
        self.numeros = [1, 2, 3, 4, 5]

    def test(self):
        print("Realizando una prueba")
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r, [2, 4, 6, 8, 10])

    def tearDown(self): #Funcion especial
        print("Destruyendo el contexto(ambiente)")
        del(self.numeros)

if __name__ == '__main__':
    unittest.main()