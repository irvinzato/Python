def doblar(lista):
    """
    Dobla el valor de los elementos de una lista.
    En los tests hago diferentes maneras, como anidar código para bucles y tratar excepciones(En el Script donde sumo)

    >>> lista = [1, 2, 3, 4, 5]
    >>> doblar(lista)
    [2, 4, 6, 8, 10]

    >>> lista = []
    >>> for i in range(10):
    ...     lista.append(i)
    >>> doblar(lista)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    return [numero * 2 for numero in lista]

if __name__ == "__main__":
    import doctest
    doctest.testmod()