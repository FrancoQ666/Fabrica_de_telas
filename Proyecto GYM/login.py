import sqlite3

def inicio_sesion():
    print("Inicio de sesion:")
    correo = input("Ponga su Correo: ").strip()
    contrasenia = input("Ponga su Contraseña: ").strip()

    conexion = sqlite3.connect("Usuarios_Registrados.db")
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT nombre, apellido FROM usuarios WHERE correo = ? AND contrasenia = ?",
        (correo, contrasenia)
    )
    usuario = cursor.fetchone()
    if usuario:
        print(f"Bienvenido, {usuario[0]} {usuario[1]}!")
    else:
        print("Correo o contraseña incorrectos.")
    cursor.close()
    conexion.close()