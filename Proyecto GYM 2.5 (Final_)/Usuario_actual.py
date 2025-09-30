import time
import funciones
import funciones_admin, Products, Usuario_cliente


def menu_usuario(usuario):
    while True:
        funciones.limpiar_pantalla()
        print(f"Bienvenido {usuario['nombre']} {usuario['apellido']}")
        print("1. Suscripción")
        print("2. Productos")
        print("3. Ajustes")
        print("4. Perfil")
        print("5. Salir")
        opcion = input("Ingrese una opción: ").strip()
        funciones.limpiar_pantalla()
        if opcion == "1":
            print("1. Renovar suscripción")
            print("2. Cancelar suscripción")
            print("3. Salir")
            sub = input("Elija una opción: ").strip()
            if sub == "1":
                Usuario_cliente.renovar_suscripcion(usuario)
            elif sub == "2":
                Usuario_cliente.cancelar_suscripcion(usuario)
            elif sub == "3":
                continue
            else:
                print("Opción inválida.")
        elif opcion == "2":
            print("1. Buscar productos")
            print("2. Comprar productos")
            print("3. Lista de productos disponibles")
            print("4. Salir")
            sub = input("Elija una opción: ").strip()
            if sub == "1":
                Usuario_cliente.buscar_productos()
            elif sub == "2":
                Usuario_cliente.comprar_productos()
            elif sub == "3":
                Products.mostrar_productos()
                input("Enter para continuar")
            elif sub == "4":
                continue
            else:
                print("Opción inválida.")
        elif opcion == "3":
            print("1. Cambiar contraseña")
            print("2. Cambiar teléfono")
            sub = input("Elija una opción: ").strip()
            if sub == "1":
                Usuario_cliente.cambiar_contrasena(usuario)
            elif sub == "2":
                Usuario_cliente.cambiar_telefono(usuario)
            else:
                print("Opción inválida.")
        elif opcion == "4":
            Usuario_cliente.ver_perfil(usuario)
        elif opcion == "5":
            print("Saliendo...")
            time.sleep(1)
            break
        else:
            print("Opción inválida.")
        input("Presione Enter para continuar...")
            



def menu_admin(usuario):
    while True:
        funciones.limpiar_pantalla()
        
        funciones.print_centered(f"=== MENÚ ADMIN - {usuario['nombre']} {usuario['apellido']} ===")
        Products.productos_escasos() #Esta funcion permite que en el menu principal, avise sobre una escasez
        print("1. Ver productos")
        print("2. Agregar producto")
        print("3. Modificar stock")
        print("4. Ver productos en escasez")
        print("5. Salir")
        opcion_usuario = input("Ingrese una opción: ").strip()
        funciones.limpiar_pantalla()
        
        if opcion_usuario == "1":
            Products.mostrar_productos()
        elif opcion_usuario == "2":
            funciones_admin.insertar_producto()
        elif opcion_usuario == "3":
            print("Le recomendamos que busque el producto deseado antes de usar esta función.")
            X = input("¿Desea buscar el producto? 1)Sí | 2)No: ").strip()
            if X == "1":
                Products.mostrar_productos
                Products.buscar_producto()
            try:
                prod_id = int(input("Ingrese la ID del producto deseado: ").strip())
                nuevo_stock = int(input("Ingrese el nuevo stock: ").strip())
                Products.actualizar_stock(prod_id, nuevo_stock)
            except Exception as e:
                print(f"Error: {e}") 
        elif opcion_usuario == "4":
            Products.productos_escasos()
        elif opcion_usuario == "5":
            print("Saliendo del menú Admin...")
            time.sleep(1)
            break
        else:
            print("Debe ingresar una opción válida")
        input("Presione Enter para continuar...")
        
            
                    
                
            
        

