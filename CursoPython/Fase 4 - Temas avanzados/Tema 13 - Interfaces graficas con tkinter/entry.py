from tkinter import *

root = Tk()
#Ademas de "pack()", "place()", también tenemos "grid()" para posicionar en cuadricula

label = Label(root, text="Nombre(Puede ser muy largo):")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5) #sticky para justificar texto este, oeste, etc

#Campo de entrada(entry)
entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="center")

label2 = Label(root, text="Apellido:")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5) #paddings

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(state="disabled")

label3 = Label(root, text="Contraseña")
label3.grid(row=2, column=0, sticky="w", padx=5, pady=5)

entry3 = Entry(root)
entry3.grid(row=2, column=1, padx=5, pady=5)
entry3.config(show="°")

root.mainloop()