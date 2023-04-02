print("Hola Irving - Compilare para jacer un ejecutable(binario), ocupa un paquete llamado 'pyinstaller' externo el proceso")
print("Ahora puedo hacer el binario, compilo usando 'pyinstaller programa.py'")
print("Todos los paquetes instalados en mi computadora se meten en el binario creado, por eso es tan pesada la carpeta")

print("Lo anterior puede generar una carpeta demasiado pesada, asi que disminuiremos ese tamaño usando otro paquete")
print("Llamado 'pipenv', ahora puedo trabajar con un entorno virtual y reducir el peso")
print("Utilizo 'pipenv install pyinstaller', este comando creara un entorno virtual en el directorio e instala el pypinstaller")
print("Ahora puedo ejecutar comando dentro del entorno virtual como 'pipenv run pip list' - Tendra menos paquetes instalados")
print("Puedo generar el nuevo binario con 'pipenv run pyinstaller programa.py'")
print("Puedo ejecutar TODOS los comandos de python pero dentro del entorno aislado 'pipenv run'")

from tkinter import *
import sys
import os

#Para poder cargar los recursos(este caso la imagen) necesito de esta función y ahora donde ocupe los recursos debo usar la función
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()

print("Ademas del ejecutable cargare recursos externos como una imagen")
print("Creo la carpeta 'res' para poner los recursos a usar como la imagen, fuentes o lo que quiera")
print("Necesito de la función para poder cargar los recursos, asi indica la documentación para que sirva el ejecutable")
print("También necesito ahora el comando con mas cosas 'pipenv run pyinstaller programa.py --windowed --onefile --clean --add-data res;res'")
imagen = PhotoImage(file=resource_path("res/Yin_yang.svg.png"))
Label(image=imagen).pack()

Label(text="Hola Irving, ahora sabes el proceso para hacer binarios(ejecutables)").pack(padx=30, pady=20)
Label(text="Con 'pipenv run pyinstaller programa.py --windowed --onefile --clean' Indico que es de escritorio y que haga un único fichero").pack(padx=10, pady=10)

print("También puedo personalizar el ICONO del ejecutable")
print("Uso un nuevo parametro 'pipenv run pyinstaller programa.py --windowed --onefile --clean --add-data res;res --ico res/gato.ico'")
print("Si da error puede ser porque necesita de una libreria 'pipenv install Pillow'")

root.mainloop()