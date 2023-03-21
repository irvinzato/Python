from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = "" #Utilizada para almacenar la ruta de un fichero

def nuevo():
    global ruta #Indico que la variable es global(la que estare manejando)
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end") #Para borrar desde el carácter 1 al último y empezar uno nuevo
    root.title("Editor Irvinzato")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(initialdir=".", filetype=(("Ficheros de texto", "*.txt"), )
                                      , title="Abrir fichero de texto")
    if(ruta != ""):
        fichero   = open(ruta, "r")
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        fichero.close()
        root.title(ruta + " - Editor Irvinzato")

def guardar():
    mensaje.set("Guardar fichero")
    if(ruta != ""): #En caso que sea un fichero ABIERTO
        contenido = texto.get(1.0, "end-1c") #Parecido al end pero para recuperar en lugar de borrar
        fichero   = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se guardo correctamente")
    else:  #Es un fichero NUEVO sin ruta
        guardarComo()

def guardarComo():
    global ruta
    mensaje.set("Guardar como:")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if(fichero is not None):
        ruta      = fichero.name
        contenido = texto.get(1.0, "end-1c")
        fichero   = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se guardo correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

root = Tk()
root.title("Proyecto - Editor de texto")

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo",        command=nuevo)
filemenu.add_command(label="Abrir",        command=abrir)
filemenu.add_command(label="Guardar",      command=guardar)
filemenu.add_command(label="Guardar como", command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label="Salir",  command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

#Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

#Parte inferior
mensaje = StringVar()
mensaje.set("Bienvenido al editor de texto Irvinzato")
monitor = Label(root, textvariable=mensaje, justify="left")
monitor.pack(side="left")

root.mainloop()