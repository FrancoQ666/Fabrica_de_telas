import sqlite3

DB_NAME = "gym.db"

def buscar_producto():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    clave = input("Ingrese palabra clave en su búsqueda: ").strip()
    cursor.execute(
        "SELECT nombre, precio, stock FROM productos WHERE nombre LIKE ?", (f"%{clave}%",)
    )
    resultados = cursor.fetchall()
    if resultados:
        print("\nPosibles resultados:")
        for r in resultados:
            print(f"Nombre: {r[0]}, Precio: {r[1]}, Stock: {r[2]}")
    else:
        print("No se encontraron productos con esa palabra clave.")
    conexion.close()



def crear_tabla_productos():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nombre TEXT NOT NULL,
           categoria TEXT NOT NULL,
           precio REAL NOT NULL,
           stock INTEGER  NOT NULL,
           stock_minimo INTEGER NOT NULL
           )
    """)
    conexion.commit()
    conexion.close()


def agregar_productos(nombre, categoria, precio, stock, stock_minimo):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, categoria, precio, stock, stock_minimo) VALUES (?, ?, ?, ?, ?)", (nombre,categoria,precio,stock, stock_minimo))
    conexion.commit()
    conexion.close()
    print(f"El producto '{nombre}' se ha agregado correctamente")

def mostrar_productos():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, categoria, precio, stock FROM productos ORDER BY nombre ASC")
    for pod in cursor.fetchall():
        print(pod)
    conexion.close()


def productos_escasos():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, stock FROM productos WHERE stock <= stock_minimo")
    productos = cursor.fetchall()

    if productos:
        print("Productos en escasez:")
        for pod_es in productos:
            print(f"{pod_es[0]} - Stock: {pod_es[1]}")
    else:
        print("No hay productos en escasez.")

    conexion.close()



def actualizar_stock(producto_id, nuevo_stock):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (nuevo_stock, producto_id))
    conexion.commit()
    conexion.close()
    print(f"El stock del producto con ID {producto_id} ha sido actualizado a {nuevo_stock}")
