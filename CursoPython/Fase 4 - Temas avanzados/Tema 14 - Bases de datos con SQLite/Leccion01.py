import sqlite3

conexion = sqlite3.connect("nombreDB.db")

cursor = conexion.cursor() #Para crear tabla y ejecutar comandos SQL en la base de datos "nombreDb"

#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
#cursor.execute("INSERT INTO usuarios VALUES ('Jade', 11, 'jade@hotmail.com')")

""" #RECUPERAR REGISTROS DE LA BASE DE DATOS
cursor.execute("SELECT * FROM usuarios")
usuario1 = cursor.fetchone() #Recupera el PRIMER registro en forma de tupla(Si se vuelve a ejecutar recupera el siguiente)
print(usuario1)"""

"""" #AGREGAR DE FORMA MASIVA MUCHOS REGISTROS
usuarios = [
    ('Angeles', 51, 'angeles@hotmail.com'),
    ('Elena', 46, 'elena@hotmail.com'),
    ('Jesus', 34, 'jesus@hotmail.com')
]
cursor.executemany("INSERT INTO usuarios VALUES (?, ?, ?)", usuarios) #Insertar masivamente varios usuarios  """

#RECUPERAR VARIOS REGISTROS
cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall() #Recupera todos los registros almacenados en el cursor(es una lista de tuplas)
print(usuarios)

for usuario in usuarios:
    print("Nombre: {}, Apellido: {}, Correo: {}".format(usuario[0], usuario[1], usuario[2]))

conexion.commit() #Para confirmar todos los cambios(Queries) hechos en la base de datos(con el cursor)

conexion.close()