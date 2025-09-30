import time
import funciones
import funciones_admin, Products


def menu_usuario(usuario):
    while True:
        funciones.limpiar_pantalla()
        print(f"Bienvenido {usuario['nombre']} {usuario['apellido']}")
        print("1. Suscripción")
        print("2. Productos")
        print("3. Ajustes")
        print("4. Perfil")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":



def menu_admin(usuario):
    while True:
        funciones.limpiar_pantalla()
        funciones.print_centered(f"=== MENÚ ADMIN - {usuario['nombre']} {usuario['apellido']} ===")
        print("1. Ver productos")
        print("2. Agregar producto")
        print("3. Modificar stock")
        print("4. Ver productos en escasez")
        print("5. Ver movimientos de compras")
        print("6. Salir")
        opcion = input("Ingrese una opción: ").strip()
        
        Opciones = {
            "1": Products.mostrar_productos(),
            "2": funciones_admin,
        }
        if not opcion:
            print("Debe ingresar una opcion")
            time.sleep(1)

