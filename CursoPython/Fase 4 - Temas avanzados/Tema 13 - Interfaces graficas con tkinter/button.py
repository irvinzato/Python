from tkinter import *

def crear_label():
    Label(root, text="Label creada dinámicamente").pack()

def sumar():
    resultado.set( float(numero1.get()) + float(numero2.get()) )
    borrar()

def restar():
    resultado.set( float(numero1.get()) - float(numero2.get()) )
    borrar()

def multiplicar():
    resultado.set( float(numero1.get()) * float(numero2.get()) )
    borrar()

def borrar():
    numero1.set("")
    numero2.set("")

root = Tk()
root.config(bd=15)

numero1   = StringVar()
numero2   = StringVar()
resultado = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=numero1).pack()

Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=numero2).pack()

Label(root, text="").pack()
Button(root, text="Sumar",       command=sumar).pack()
Button(root, text="Restar",      command=restar).pack()
Button(root, text="Multiplicar", command=multiplicar).pack()

Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable=resultado, state="disabled").pack()



root.mainloop()