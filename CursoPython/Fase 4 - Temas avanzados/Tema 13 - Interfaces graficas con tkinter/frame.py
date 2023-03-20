from tkinter import *

#Configuración de la raíz
root = Tk()
root.title("Hola Irving")
root.iconbitmap("hola.ico")
root.resizable(True, True)

root.config(cursor="arrow")
root.config(bg="lightgray")
root.config(bd="15")
root.config(relief="ridge")

#Creación de un marco(frame) 
frame = Frame(root, width=480, height=320)
#frame.pack(side="top", anchor="w")    #pack() por defecto alinea los widgets arriba y en medio, podemos también indicarle
frame.pack(fill="both", expand=1) #fill tambien puede ser en "x" o "y" como ejes
frame.config(cursor="pirate")
frame.config(bg="lightgreen")
frame.config(bd="25")
frame.config(relief="sunken")



#Bucle de la aplicación
root.mainloop()