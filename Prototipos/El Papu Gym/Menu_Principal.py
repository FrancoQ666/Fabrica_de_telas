def mostrar_menu():
    print('\nBienvenido Usuario, al PAPU GIMNASIO')
    print("Selecciona una opción:")
    print("1. Suscripcion")
    print("2. Productos")
    print("3. Ajustes")
    print("4. Perfil")
    print("5. Salir")

def suscripcion():
    print(">> Mostrando opciones de subscripcion")

def productos():
    print(">> Mostrando productos disponibles")

def ajustes():
    print(">> Abriendo configuracion")

def perfil():
    print(">> Mostrando perfil del usuario")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion (1-5): ")

    if opcion == "1":
        subscripcion()
    elif opcion == "2":
        productos()
    elif opcion == "3":
        ajustes()
    elif opcion == "4":
        perfil()
    elif opcion == "5":
        print("Chau papu bro master HD")
        break
    else:
        print("Opcion invalida Intenta de nuevo.")
