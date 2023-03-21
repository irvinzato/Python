from tkinter import *
from tkinter import messagebox as MessageBox 

root = Tk()

#Ventanas emergentes(popups) ocupa la importación explicita "messagebox"
def test():
    #MessageBox.showinfo("Tipo show info", "Popup de información")
    #MessageBox.showwarning("Tipo show warning", "Popup de alerta")
    #MessageBox.showerror("Tipo show error", "Popup de error")
    resultado = MessageBox.askquestion("Tipo de pregunta", "¿Estas seguro de querer salir?") #Devuelve "yes" o "no"
    if(resultado == "yes"):
        root.destroy()

def test2():               #askyesno tambien regresa boleanos
    resultado = MessageBox.askokcancel("Tipo ask o cancel", "¿Sobre escribir el fichero actual?") #Devuelve "true" o "false"
    if(resultado):
        root.destroy()
    resultado = MessageBox.askretrycancel("Tipo askretrycancel(Reintentar)", "No se puede conectar") #Devuelve boleano
    if(resultado):
        root.destroy


Button(root, text="Haz click", command=test2).pack()


root.mainloop()