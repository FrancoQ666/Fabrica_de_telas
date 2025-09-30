def menu_inicio():
    while True:
        print("\n--- Menú de inicio ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Opcion: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar()
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción invalida.")

def registrar():
    print("\n---- Registrarse ----")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    dni = input("DNI: ")
    correo = input("Correo: ")
    telefono = input("Teléfono: ")

    usuario = input("Usuario (para iniciar sesion): ")
    if usuario in usuarios:
        print("Ese usuario ya existe.")
        return
    contraseña = input("Contraseña: ")

    usuarios[usuario] = {
        "contraseña": contraseña,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "dni": dni,
        "correo": correo,
        "telefono": telefono
    }

    print("Registro exitoso.")

def iniciar_sesion():
    print("\n--- Iniciar sesion ---")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        print(f"Iniciaste sesion como {usuario}")
    else:
        print("Usuario o contraseña incorrectos.")

usuarios = {}
menu_inicio()


