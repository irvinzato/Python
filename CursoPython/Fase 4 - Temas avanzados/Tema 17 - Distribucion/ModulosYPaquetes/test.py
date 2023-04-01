#Si no estuviera dentro del paquete(carpeta) basta con el nombre del archivo
import mensajes.saludos.tipoHola as tipoHola
#Para importar de manera selectiva algo del modulo, o con * para tener acceso a todas las deficiones del archivo
from mensajes.saludos.tipoHola import *
from mensajes.despedidas.tipoAdios import *

print("---- COSAS DEL SUB PAQUETE SALUDOS ----")
print("*** JUGANDO CON LOS METODOS ***")
tipoHola.saludar()
saludar()

print("*** JUGANDO CON LAS CLASES ***")
saludo = Saludo()
print(saludo)
Saludo()

print("---- COSAS DEL SUB PAQUETE DESPEDIDAS ----")
despedir()
Despedida()