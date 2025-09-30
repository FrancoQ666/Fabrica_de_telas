import registrer
import login
import os
import time





def main():
    while True:
        print("Bienvenido al sistema de registro del gimnasio.")
        print("(1) Registrar nuevo usuario  || (2) Iniciar sesión")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            registrer.registrar()
        elif choice == '2':
            login.inicio_sesion()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        time.sleep(2)
        os.system('clear')

if __name__ == "__main__":
    main()
    registrer.cursor.close()
    registrer.Conexion.close()
else:
        print("Por favor, corrija los errores e intente de nuevo.")