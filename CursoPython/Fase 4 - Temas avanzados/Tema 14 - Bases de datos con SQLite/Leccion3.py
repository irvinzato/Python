import sqlite3

conexion = sqlite3.connect("usuarios_autoincrementalDB.db")
cursor   = conexion.cursor()

#Clausula WHERE
cursor.execute("SELECT * FROM usuarios WHERE edad = 27")
usuarios = cursor.fetchall()
print(usuarios)

#Clausula UPDATE(actualizar) SET(todos los campos a actualizar) WHERE(de quien)
cursor.execute("UPDATE usuarios SET nombre = 'Irving Rivera' WHERE ine = '00000001A'")

#Borrar registros DELETE(Si no pongo el Where y solo pongo la tabla, borra TODA la tabla)
cursor.execute("DELETE FROM usuarios WHERE ine = '00000001A'")


conexion.commit()
conexion.close()