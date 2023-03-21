from tkinter import *

root = Tk()

menubar = Menu(root) #El menú no se empaqueta(tiene prioridad)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0) #"tearoff" para que no ponga el submenu por defecto
filemenu.add_command(label="Nuevo") #Añado opciones a "filemenu"
filemenu.add_command(label="Abrir") #Puedo ponerles "command" para añadir alguna función al clickear
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit) #"command" para cerrar la ventana

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Acerca de")
helpmenu.add_separator()
helpmenu.add_command(label="Comandos mas utilizados")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar",  menu=editmenu)
menubar.add_cascade(label="Ayuda",   menu=helpmenu)

root.mainloop()