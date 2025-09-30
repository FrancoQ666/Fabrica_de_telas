import sqlite3
import funciones
import Products
import hashlib

DB_NAME = "gym.db"  

def buscar_productos():
        Products.buscar_producto()
        input("Enter para continuar...")


def comprar_productos():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    Products.mostrar_productos()
    try:
        prod_id = int(input("Ingrese la ID del producto deseado: "))
        cursor.execute("SELECT nombre, stock FROM productos WHERE id = ?", (prod_id,))
        prod = cursor.fetchone()
        if not prod:
            print("Producto no encontrado")
            return

        if prod[1] <= 0:
            print("No hay stock disponible para este producto")
            return
        
        cantidad = int(input("¿Cuantas unidades desea comprar?: "))
        if cantidad > prod[1]:
            print("No es posible superar las unidades con la disponibilidad")
            return
        nuevo_stock = prod[1] - cantidad
        Products.actualizar_stock(prod_id, nuevo_stock)
        print(f"¡Compra realizada! {cantidad} unidad(es) de '{prod[0]}'")
    except Exception as e:
        print(f"Error en la compra {e}")
    finally:
        conexion.close()


def ver_perfil(usuario):
    funciones.limpiar_pantalla()
    print("\n=== Mi Perfil ===")
    print(f"Nombre: {usuario['nombre']} {usuario['apellido']}")
    print(f"Correo: {usuario['correo']}")
    print(f"Telefono: {usuario['telefono']}")
    print(f"Edad: {usuario['edad']}")
    print(f"Suscripcion: {usuario['suscripcion']} (Dias restantes: {usuario['tiempo']})")
    input("Enter para continuar...")


def cambiar_contrasena(usuario):
    funciones.limpiar_pantalla()
    conexion = sqlite3.connect(DB_NAME)  # Usar gym.db
    cursor = conexion.cursor()
    nueva = input("Ingrese su nueva contraseña: ").strip()
    confirmar = input("Repita la nueva contraseña: ").strip()
    if nueva != confirmar:
        print("Las contraseñas no coinciden :/")
        return
    hashed = hashlib.sha256(nueva.encode()).hexdigest()
    cursor.execute("UPDATE usuarios SET contrasenia = ? WHERE correo = ?", (hashed, usuario["correo"],))
    conexion.commit()
    conexion.close()
    print("Contraseña actualizada correctamente")
    input("Enter para continuar")

def cambiar_telefono(usuario):
    conexion = sqlite3.connect(DB_NAME)  # Usar gym.db
    cursor = conexion.cursor()
    nuevo = input("Ingrese su nuevo numero de telefono: ")
    cursor.execute("UPDATE usuarios SET telefono = ? WHERE correo = ?", (nuevo, usuario["correo"],))
    conexion.commit()
    conexion.close()
    print("Telefono actualizado")
    input("Enter para continuar")


def renovar_suscripcion(usuario):
    conexion = sqlite3.connect(DB_NAME)  # Usar gym.db
    cursor = conexion.cursor()
    try:
        # Verificar que el usuario existe en la tabla
        cursor.execute("SELECT correo FROM usuarios WHERE correo = ?", (usuario["correo"],))
        if not cursor.fetchone():
            print("Error: Usuario no encontrado en la base de datos")
            return
        
        # Renovar suscripción
        cursor.execute("UPDATE usuarios SET Tiempo = Tiempo + 30 WHERE correo = ?", (usuario["correo"],))
        conexion.commit()
        print("Suscripcion renovada por 30 dias mas")
    except sqlite3.Error as e:
        print(f"Error al renovar suscripción: {e}")
    finally:
        conexion.close()
    
def cancelar_suscripcion(usuario):
    conexion = sqlite3.connect(DB_NAME)  # Usar gym.db
    cursor = conexion.cursor()
    try:
        cursor.execute("UPDATE usuarios SET Suscripcion = 'Cancelada', Tiempo = 0 WHERE correo = ?", (usuario["correo"],))
        conexion.commit()
        print("Suscripcion cancelada")
    except sqlite3.Error as e:
        print(f"Error al cancelar suscripción: {e}")
    finally:
        conexion.close()