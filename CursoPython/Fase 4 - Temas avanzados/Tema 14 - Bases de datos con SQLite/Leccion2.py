import sqlite3

conexion = sqlite3.connect("usuarios_autoincrementalDB.db")
cursor   = conexion.cursor()

"""  #Primer parte(PRIMARY KEY) - Creación de tabla en DB(usuariosDB) y añadir masivamente
cursor.execute('''
    CREATE TABLE usuarios (
    dni    VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(100),
    edad   INTEGER,
    email  VARCHAR(100)
    )
 ''')

usuarios = [
    ('00000001A', 'Irving' , 51, 'irving@hotmail.com'),
    ('00000001B', 'Angeles', 51, 'angeles@hotmail.com'),
    ('00000001C', 'Elena'  , 46, 'elena@hotmail.com'),
    ('00000001D', 'Jesus'  , 34, 'jesus@hotmail.com')
]
cursor.executemany("INSERT INTO usuarios VALUES (?, ?, ?, ?)", usuarios)
"""


"""  #Campos autoincrementales(AUTOINCREMENT) - Segunda parte
cursor.execute('''
    CREATE TABLE productos (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    marca  VARCHAR(50) NOT NULL,
    precio FLOAT NOT NULL
    )
 ''')

 
productos = [
    ("Teclado" , "Logitech", 19.45),
    ("Pantalla", "LG"      , 89.45),
    ("Mouse"   , "Dragon"  , 20.45)
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos); #Se indica el valor auto incrementable como null

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
for producto in productos:
    print(producto)
"""


#Claves únicas, campos únicos no repetibles(UNIQUE) - Tercera parte
cursor.execute('''
    CREATE TABLE usuarios (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    ine    VARCHAR(9) UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    edad   INTEGER NOT NULL,
    email  VARCHAR(100)
    )
 ''')

usuarios = [
    ('00000001A', 'Irving' , 51, 'irving@hotmail.com'),
    ('00000002B', 'Angeles', 51, 'angeles@hotmail.com'),
    ('00000003C', 'Elena'  , 46, 'elena@hotmail.com'),
    ('00000004D', 'Yumiko' , 10, 'yumiko@hotmail.com'),
    ('00000005E', 'Jesus'  , 34, 'jesus@hotmail.com')
]

cursor.executemany("INSERT INTO usuarios VALUES(null, ?, ?, ?, ?)", usuarios)

conexion.commit()
conexion.close()