from tkinter import *

root = Tk()

texto = Text(root)
texto.pack()
#En este caso width y height no son pixeles, son carácteres
texto.config(width=30, height=10, font=("Consolas", 12), padx=5, pady=5, selectforeground="blue")

root.mainloop()