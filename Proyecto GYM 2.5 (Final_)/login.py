import sqlite3
import funciones
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def inicio_sesion():
    print("Inicio de sesion:")
    correo = input("Ponga su Correo: ").strip()
    contrasenia = input("Ponga su Contraseña: ").strip()

    hashed_pass = hash_password(contrasenia)

    conexion = sqlite3.connect("gym.db")  # Cambio aquí: usar gym.db
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT nombre, apellido, edad, telefono, correo, dni, Suscripcion, Tiempo, rol FROM usuarios WHERE correo = ? AND contrasenia = ?",
        (correo, hashed_pass)
    )
    usuario = cursor.fetchone()
    conexion.close()  # Cerrar conexión

    if usuario:
        rol = usuario[8]  # índice del campo 'rol'
        print(f"Bienvenido {usuario[0]} ({rol})")

        datos_usuario = {
            "nombre": usuario[0],
            "apellido": usuario[1],
            "edad": usuario[2],
            "telefono": usuario[3],
            "correo": usuario[4],
            "DNI": usuario[5],
            "suscripcion": usuario[6],
            "tiempo": usuario[7],
            "rol": rol
        }
        return datos_usuario
    else:
        print("Correo o contraseña incorrectos.")
        return None