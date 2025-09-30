import time
import registrer, login
import funciones

def menu_inicio():
    
    while True:
        funciones.limpiar_pantalla()
        print("\n--- Menú de inicio ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Opcion: ")

        if opcion == "1":
            funciones.limpiar_pantalla()
            
            login.inicio_sesion()
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


