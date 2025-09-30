import sqlite3
import hashlib

# Conexión a la base de datos SQLite (se crea el archivo si no existe)
Conexion = sqlite3.connect("Usuarios_Registrados.db")
cursor = Conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    edad INTEGER NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT NOT NULL,
    dni INTEGER NOT NULL,
    contrasenia TEXT NOT NULL
)
""")

def hashear_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar():
    try:
        print("Registro de nuevo usuario:")
        Usuario_Name = input("Ponga su Nombre (Primer nombre, segundo etc): ").strip()
        Usuario_Surname = input("Ponga su Apellido: ").strip()
        Usuario_Age_str = input("Ponga su Edad: ").strip()
        Usuario_DNI_str = input("Ponga su DNI: ").strip()
        Usuario_Tel = input("Ponga su Teléfono: ").strip()
        Usuario_Correo = input("Ponga su Correo: ").strip()
        Usuario_Contrasenia = input("Ponga su Contraseña: ").strip()

        # Validación de campos vacíos
        if not all([Usuario_Name, Usuario_Surname, Usuario_Age_str, Usuario_DNI_str, Usuario_Tel, Usuario_Correo, Usuario_Contrasenia]):
            print("ERROR, ALGUNO DE LOS CAMPOS ESTÁ VACÍO")
            return

        try:
            Usuario_Age = int(Usuario_Age_str)
            Usuario_DNI = int(Usuario_DNI_str)
        except ValueError:
            print("ERROR, Edad y DNI deben ser números.")
            return

        ERROR_count = 0
        if Usuario_DNI > 99999999 or Usuario_DNI < 10000000:
            ERROR_count += 1
        if Usuario_Age > 100 or Usuario_Age < 18:
            ERROR_count += 1
        if ERROR_count > 0:
            print(f"ERROR, SE HAN DETECTADO {ERROR_count} ERRORES, POR FAVOR INTENTE DE NUEVO")
            return

        # Chequeo de duplicados
        cursor.execute("SELECT 1 FROM usuarios WHERE dni = ?", (Usuario_DNI,))
        if cursor.fetchone():
            print("ERROR, YA EXISTE UN USUARIO CON ESE DNI")
            return
        cursor.execute("SELECT 1 FROM usuarios WHERE correo = ?", (Usuario_Correo,))
        if cursor.fetchone():
            print("ERROR, YA EXISTE UN USUARIO CON ESE CORREO")
            return

        Usuario_Contrasenia = hashear_contrasena(Usuario_Contrasenia)

        cursor.execute(
            "INSERT INTO usuarios (nombre, apellido, edad, telefono, correo, dni, contrasenia) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (Usuario_Name, Usuario_Surname, Usuario_Age, Usuario_Tel, Usuario_Correo, Usuario_DNI, Usuario_Contrasenia)
        )
        Conexion.commit()
        print("Registro guardado en la base de datos.")
    except sqlite3.Error as e:
        print(f"Error al registrar el usuario: {e}")
        print("Por favor, corrija los errores e intente de nuevo.")