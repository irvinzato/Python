def saludar():
    print("Hola, siempre firme Irving ! desde saludos.saludar()")

def version():
    print("Estas en el método version de saludos.tipoHola")

class Saludo:
    def __init__(self):
        print("self tiene -> ", self)
        print("Hola, te saludo desde el constructor(__init__) de 'Saludo'")

#Para evitar que se ejecute el llamado a la función solo por importar este archivo V144
#O cualquier código que tengamos en la parte inferior
print(__name__)
if __name__ == '__main__':
    saludar()

print("NO ESTA DENTRO DEL IF")