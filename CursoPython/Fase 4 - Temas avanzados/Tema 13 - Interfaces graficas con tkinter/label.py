from tkinter import *

root = Tk()

#Variables dinamicas
texto = StringVar()
texto.set("Texto hecho dinamicamente")

frame = Frame(root, width=480, height=320)
frame.pack() #pack() empaqueta y distribuye uniformemente a su manera el tamaño del contenido(el tamaño lo reinicia)

label = Label(frame, text="Hola Irving, estas utilizando label")
label.place(x=0, y=0) #place() respeta el tamaño y colocamos donde querramos
label.config(bg="lightblue", fg="red", font=("Verdana", 24))
label.config(textvariable=texto)

Label(frame, text="Otra etiqueta, añadida de forma diferente").place(x=0, y=50) #Si no ocupare la variable, puedo definirlo todo en una linea
Label(frame, text="Siempre adelante Irving !").place(x=0, y=80)

#Puedo poner imagenes en labels pero "PhotoImage" solo acepta formatos .gif y uno mas
imagen = PhotoImage(file="imagen.gif")
Label(frame, image=imagen, bd=0).place(x=0, y=110)


root.mainloop()