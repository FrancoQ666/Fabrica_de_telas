import sqlite3
import hashlib
import Products
# Conexión a la base de datos SQLite (se crea el archivo si no existe)
Conexion = sqlite3.connect("Usuarios_Registrados.db")
cursor = Conexion.cursor()


def hash_password(password):
    """Genera un hash SHA-256 de la contraseña."""
    return hashlib.sha256(password.encode()).hexdigest()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    edad INTEGER NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT NOT NULL,
    dni INTEGER NOT NULL,
    contrasenia TEXT NOT NULL,
    Suscripcion TEXT DEFAULT 'Basico',
    Tiempo INTEGER DEFAULT 30,
    rol TEXT DEFAULT 'usuario'
)
""")



cursor.execute("""
    INSERT INTO usuarios (nombre, apellido, edad, telefono, correo, dni, contrasenia, rol)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ('Admin', 'Master', 30, '123456789', 'admin@gmail.com', 12345678, hash_password('admin123'), 'admin'))
Conexion.commit()


def registrar():
    try:
        print("Registro de nuevo usuario:")
        Usuario_Name = input("Ponga su Nombre: ").strip()
        Usuario_Surname = input("Ponga su Apellido: ").strip()
        Usuario_Age_str = input("Ponga su Edad: ").strip()
        Usuario_DNI_str = input("Ponga su DNI: ").strip()
        Usuario_Tel = input("Ponga su Teléfono: ").strip()
        Usuario_Correo = input("Ponga su Correo: ").strip()
        Usuario_Contrasenia = input("Ponga su Contraseña: ").strip()

        if not all([Usuario_Name, Usuario_Surname, Usuario_Age_str, Usuario_DNI_str, Usuario_Tel, Usuario_Correo, Usuario_Contrasenia]):
            print("ERROR, ALGUNO DE LOS CAMPOS ESTÁ VACÍO")
            return

        try:
            Usuario_Age = int(Usuario_Age_str)
            Usuario_DNI = int(Usuario_DNI_str)
        except ValueError:
            print("ERROR, Edad y DNI deben ser números.")
            return

        if Usuario_DNI > 99999999 or Usuario_DNI < 1:
            print("ERROR, DNI no válido")
            return
        if Usuario_Age > 100 or Usuario_Age < 18:
            print("ERROR, Edad no válida")
            return

        # Duplicados
        cursor.execute("SELECT 1 FROM usuarios WHERE dni = ?", (Usuario_DNI,))
        if cursor.fetchone():
            print("ERROR, YA EXISTE UN USUARIO CON ESE DNI")
            return
        cursor.execute("SELECT 1 FROM usuarios WHERE correo = ?", (Usuario_Correo,))
        if cursor.fetchone():
            print("ERROR, YA EXISTE UN USUARIO CON ESE CORREO")
            return



        # Hash de la contraseña
        hashed_pass = hashlib.sha256(Usuario_Contrasenia.encode()).hexdigest()

        cursor.execute("""
            INSERT INTO usuarios (nombre, apellido, edad, telefono, correo, dni, contrasenia, rol)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (Usuario_Name, Usuario_Surname, Usuario_Age, Usuario_Tel, Usuario_Correo, Usuario_DNI, hashed_pass, "Usuario"))

        Conexion.commit()
        print(f"Registro guardado. Usuario {Usuario_Name}")
    except sqlite3.Error as e:
        print(f"Error al registrar el usuario: {e}")
