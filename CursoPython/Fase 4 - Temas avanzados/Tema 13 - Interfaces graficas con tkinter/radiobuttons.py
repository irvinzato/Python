from tkinter import *

def seleccionar():
    valor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    valor.config(text="")

root = Tk()

opcion = IntVar()

Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=seleccionar).pack()

valor = Label(root)
valor.pack()

Button(root, text="Reiniciar selección", command=reset).pack()

root.mainloop()