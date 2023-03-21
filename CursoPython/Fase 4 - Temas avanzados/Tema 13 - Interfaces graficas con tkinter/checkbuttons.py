from tkinter import *

def seleccionar():
    cadena = ""
    if(leche.get()): #Si tiene 1 entra
        cadena += "Con leche"
    else:
        cadena += "Sin leche"
    if(azucar.get()): #Si tiene 1 entra
        cadena += " Con azucar"
    else:
        cadena += " Sin azucar"
    cadenaLabel.config(text=cadena)

root = Tk()
root.title("Cafetería")
root.config(bd=15)

leche  = IntVar() #1 si - 0 no
azucar = IntVar()

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root).pack(side="left")
#frame.pack(side="right")

Label(frame, text="¿Como quieres el café?").pack(anchor="w")
Checkbutton(frame, text="Con leche",  variable=leche,  onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

cadenaLabel = Label(frame)
cadenaLabel.pack()

root.mainloop()