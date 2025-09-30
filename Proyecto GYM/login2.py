import sqlite3


i = 3
def inicio_sesion():
    print("Inicio Sesion:")
    while i < 0:
        correo = input("Ponga su Correo: ").strip()
        contrasenia = input("Ponga su Contraseña: ").strip()
        conexion = sqlite3.connect("Usuarios_Registrados.db")