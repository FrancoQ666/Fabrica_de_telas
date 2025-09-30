import sqlite3
import funciones

DB_NAME = "gym.db"

def buscar_producto():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    try:
        clave = input("Ingrese nombre clave en su búsqueda: ").strip()
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
    except sqlite3.Error as e:
        print(f"Error al buscar producto: {e}")
    finally:
        conexion.close()


def crear_tabla_productos():
    """Esta función ya no es necesaria, pero la mantenemos por compatibilidad"""
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               categoria TEXT NOT NULL,
               precio REAL NOT NULL,
               stock INTEGER NOT NULL,
               stock_minimo INTEGER NOT NULL
               )
        """)
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al crear tabla de productos: {e}")
    finally:
        conexion.close()


def agregar_productos(nombre, categoria, precio, stock, stock_minimo):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO productos (nombre, categoria, precio, stock, stock_minimo) VALUES (?, ?, ?, ?, ?)", 
                      (nombre, categoria, precio, stock, stock_minimo))
        conexion.commit()
        print(f"El producto '{nombre}' se ha agregado correctamente")
    except sqlite3.Error as e:
        print(f"Error al agregar producto: {e}")
    finally:
        conexion.close()

def mostrar_productos():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id, nombre, categoria, precio, stock FROM productos ORDER BY nombre ASC")
        productos = cursor.fetchall()
        if productos:
            print("\n=== PRODUCTOS DISPONIBLES ===")
            for prod in productos:
                print(f"ID: {prod[0]} || Nombre: {prod[1]} || {prod[2]} || ${prod[3]} || Stock: {prod[4]}")
        else:
            print("No hay productos registrados.")
    except sqlite3.Error as e:
        print(f"Error al mostrar productos: {e}")
    finally:
        conexion.close()


def productos_escasos():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT nombre, stock, stock_minimo FROM productos WHERE stock <= stock_minimo")
        productos = cursor.fetchall()

        if productos:
            print("PRODUCTOS EN ESCASEZ:")
            print("-" * 40)
            for prod_es in productos:
                funciones.print_colored(f"• {prod_es[0]} - Stock actual: {prod_es[1]} (Mínimo: {prod_es[2]})", color='yellow', delay=0)
            print("-" * 40)
        else:
            print("No hay productos en escasez.")
    except sqlite3.Error as e:
        print(f"Error al verificar productos escasos: {e}")
    finally:
        conexion.close()


def actualizar_stock(producto_id, nuevo_stock):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    try:
        # Verificar que el producto existe
        cursor.execute("SELECT nombre FROM productos WHERE id = ?", (producto_id,))
        producto = cursor.fetchone()
        
        if not producto:
            print(f"Error: No existe un producto con ID {producto_id}")
            return
        
        cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (nuevo_stock, producto_id))
        conexion.commit()
        print(f"El stock del producto '{producto[0]}' (ID: {producto_id}) ha sido actualizado a {nuevo_stock}")
    except sqlite3.Error as e:
        print(f"Error al actualizar stock: {e}")
    finally:
        conexion.close()