#">>>" indica que es una prueba y la siguiente linea su resultado
def suma(a,b):
    """
    La función suma(a,b) recibe dos parámetros a y b.
    Devuelve la suma de ambos
    
    >>> suma(5,10)
    15
    
    >>> suma(0,0)
    0

    >>> suma(-5,7)
    2

    Cadenas de texto:

    >>> suma('aa','bb')
    'aabb'

    O listas

    >>> lista_1 = [1, 2, 3]
    >>> lista_2 = [4, 5, 6]
    >>> suma(lista_1, lista_2)
    [1, 2, 3, 4, 5, 6]

    Test para excepciones, en este caso es una excepcion "TypeError"

    >>> suma(10, "hola")
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()