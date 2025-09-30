import funciones
import Products
import sqlite3
DB_NAME = "gym.db"


def insertar_producto():
    try:
        funciones.limpiar_pantalla()
        funciones.print_centered("Ingreso del producto")

        nombre = input("Ingrese el nombre del producto: ").strip()

        funciones.lista_categoria()

        categoria_map = {
            "1": "Equipamiento",
            "2": "Ropa",
            "3": "Suplementos",
            "4": "Servicios"
        }
        categoria_str = input("Seleccione el número para la categoría: ").strip()
        categoria = categoria_map.get(categoria_str)

        if not categoria:
            print("Error: categoria invalida")
            return 


        precio_str = input("Ingrese el precio del producto (ARS): ").strip()

        print("\n 𝒊: Necesitamos la cantidad del producto para que el sistema avise ante un escasez")
        stock_str = input("Ingrese la cantidad/Stock del producto: ").strip()

        print("\n 𝒊: Cuando el stock llegue a este número, el sistema avisará para reponer")
        stock_minimo_str = input("Ingrese el stock mínimo: ").strip()

        # Validación de campos vacíos
        if not all([nombre, categoria_str, precio_str, stock_str, stock_minimo_str]):
            print("Error: hay campos vacíos.")
            return

        try:
            precio = float(precio_str)
            stock = int(stock_str)
            stock_minimo = int(stock_minimo_str)
        except ValueError:
            print("Error: la categoría, precio, stock y stock mínimo deben ser numéricos.")
            return

        if precio < 0:
            print("Error: el precio no puede ser negativo.")
            return

        Products.agregar_productos(nombre, categoria, precio, stock, stock_minimo)
        print(f"El producto '{nombre}' agregado con exito a la categoria {categoria}")
    except Exception as e:
        print(f"Ocurrió un error al insertar el producto: {e}")




def eliminar_producto():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()

    try:
        producto_id = input("Ingrese el ID del producto que desea eliminar: ")

        # Verificar si existe
        cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
        producto = cursor.fetchone()

        if producto:
            print(f"Producto encontrado: {producto[1]} (Stock: {producto[4]})")
            confirmacion = input("¿Esta seguro que desea eliminarlo? (s/n): ").lower()

            if confirmacion == "s":
                cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
                conexion.commit()
                print("Producto eliminado con éxito.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontro un producto con ese ID.")

    except Exception as e:
        print(f"Error al eliminar el producto: {e}")

    finally:
        conexion.close()



def aviso_escasez():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM productos WHERE stock <= stock_minimo")
    cantidad_escasos = cursor.fetchone()[0]
    conexion.close()
    
    if cantidad_escasos == 0:
        funciones.print_colored("No hay escasez de productos", color='green', delay=0)
    else:
        funciones.print_colored(f"Atención: hay {cantidad_escasos} productos en escasez", color='yellow', delay=0)
