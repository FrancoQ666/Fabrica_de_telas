import time
import registrer, login
import funciones
import Usuario_actual


def menu_inicio():
    
    while True:
        funciones.limpiar_pantalla()
        funciones.print_centered("--- Menú de inicio ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Opcion: ")

        if opcion == "1":
            funciones.limpiar_pantalla()
            usuario = login.inicio_sesion()
            
            if usuario is None:
                print("Error al iniciar sesión. Intente nuevamente.")
                time.sleep(2)
                continue
            else:
                
                if Usuario_actual:
                    if usuario["rol"] == "admin":
                        Usuario_actual.menu_admin(usuario)
                    else:
                        Usuario_actual.menu_usuario(usuario)
            time.sleep(1)
        elif opcion == "2":
            funciones.limpiar_pantalla()
            registrer.registrar()
            time.sleep(1)
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción invalida.")
        time.sleep(1)
menu_inicio()


