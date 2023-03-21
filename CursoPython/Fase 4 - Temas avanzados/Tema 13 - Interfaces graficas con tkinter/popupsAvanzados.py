from tkinter import *
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test():
    color = ColorChooser.askcolor(title="Elije un color") #Devuelve el color en una tupla((R,G,B), '#codigoHexadecimal')
    print(color)

def test2():                #Puedo decirle que solo muestre ciertas extensiones de ficheros y desde donde abrir("initialidir='C:'")
    fichero = FileDialog.askopenfilename(title="Abrir un fichero"     #Devuelve la ruta al fichero seleccionado
                                         , filetypes=(("Ficheros de texto", "*.txt"), ("ImagenesJpg", "*.jpg") ) ) 
    print(fichero)

def test3():                                                    #Recordar que se carga lo escrito
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w", defaultextension=".txt") #Equivale a open("ruta", "w")
    print(fichero)
    if(fichero is not None):
        fichero.write("Este texto se escribio desde la condición")
        fichero.close()

Button(root, text="Haz click", command=test2).pack()

root.mainloop()