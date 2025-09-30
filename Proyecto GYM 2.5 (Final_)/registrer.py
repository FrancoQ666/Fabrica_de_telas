import sqlite3
import hashlib
import Products

DB_NAME = "gym.db"

def hash_password(password):
    """Genera un hash SHA-256 de la contraseña."""
    return hashlib.sha256(password.encode()).hexdigest()

def inicializar_base_datos_completa():
    """Inicializa todas las tablas necesarias en gym.db"""
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    try:
        print("Inicializando base de datos...")
        
        # Crear tabla de usuarios
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
        
        # Crear tabla de productos
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            stock_minimo INTEGER NOT NULL
        )
        """)
        
        # Verificar si ya existe el admin antes de insertarlo
        cursor.execute("SELECT correo FROM usuarios WHERE correo = 'admin@gmail.com'")
        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO usuarios (nombre, apellido, edad, telefono, correo, dni, contrasenia, rol)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, ('Admin', 'Master', 30, '123456789', 'admin@gmail.com', 12345678, hash_password('admin123'), 'admin'))
            print("Usuario admin creado (admin@gmail.com / admin123)")
        
        # Insertar productos de ejemplo si la tabla está vacía
        cursor.execute("SELECT COUNT(*) FROM productos")
        if cursor.fetchone()[0] == 0:
            productos_ejemplo = [
                ("Mancuernas 5kg", "Equipamiento", 15000.0, 10, 2),
                ("Mancuernas 10kg", "Equipamiento", 25000.0, 8, 2),
                ("Barra Olímpica", "Equipamiento", 45000.0, 5, 1),
                ("Proteína Whey 1kg", "Suplementos", 8500.0, 15, 3),
                ("Creatina 300g", "Suplementos", 4200.0, 12, 2),
                ("BCAA 250g", "Suplementos", 6800.0, 8, 2),
                ("Remera Deportiva", "Ropa", 3500.0, 20, 5),
                ("Short de Entrenamiento", "Ropa", 4200.0, 15, 3),
                ("Zapatillas Running", "Ropa", 12000.0, 10, 2),
                ("Membresía Personal", "Servicios", 25000.0, 100, 10),
                ("Clase de Spinning", "Servicios", 1500.0, 50, 5),
                ("Entrenamiento Personalizado", "Servicios", 8000.0, 20, 3)
            ]
            
            cursor.executemany("""
                INSERT INTO productos (nombre, categoria, precio, stock, stock_minimo) 
                VALUES (?, ?, ?, ?, ?)
            """, productos_ejemplo)
            print("Productos de ejemplo agregados")
        
        conexion.commit()
        print("Base de datos inicializada correctamente")
        
    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")
    finally:
        conexion.close()

def registrar():
    # Asegurar que la base de datos esté inicializada
    inicializar_base_datos_completa()
    
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    try:
        print("\n" + "="*50)
        print("           REGISTRO DE NUEVO USUARIO")
        print("="*50)
        
        Usuario_Name = input("Nombre: ").strip()
        Usuario_Surname = input("Apellido: ").strip()
        Usuario_Age_str = input("Edad: ").strip()
        Usuario_DNI_str = input("DNI: ").strip()
        Usuario_Tel = input("Teléfono: ").strip()
        Usuario_Correo = input("Correo electrónico: ").strip()
        Usuario_Contrasenia = input("Contraseña: ").strip()

        # Validación de campos vacíos
        if not all([Usuario_Name, Usuario_Surname, Usuario_Age_str, Usuario_DNI_str, Usuario_Tel, Usuario_Correo, Usuario_Contrasenia]):
            print("ERROR: Todos los campos son obligatorios")
            return

        # Validación de tipos de datos
        try:
            Usuario_Age = int(Usuario_Age_str)
            Usuario_DNI = int(Usuario_DNI_str)
        except ValueError:
            print("ERROR: La edad y DNI deben ser números")
            return

        # Validaciones de rango
        if Usuario_DNI > 99999999 or Usuario_DNI < 10000000:
            print("ERROR: DNI debe tener entre 7 y 8 dígitos")
            return
        if Usuario_Age > 100 or Usuario_Age < 18:
            print("ERROR: La edad debe estar entre 18 y 100 años")
            return

        # Verificar duplicados
        cursor.execute("SELECT 1 FROM usuarios WHERE dni = ?", (Usuario_DNI,))
        if cursor.fetchone():
            print("ERROR: Ya existe un usuario con ese DNI")
            return
        cursor.execute("SELECT 1 FROM usuarios WHERE correo = ?", (Usuario_Correo,))
        if cursor.fetchone():
            print("ERROR: Ya existe un usuario con ese correo")
            return

        # Hash de la contraseña
        hashed_pass = hash_password(Usuario_Contrasenia)

        # Insertar usuario
        cursor.execute("""
            INSERT INTO usuarios (nombre, apellido, edad, telefono, correo, dni, contrasenia, rol)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (Usuario_Name, Usuario_Surname, Usuario_Age, Usuario_Tel, Usuario_Correo, Usuario_DNI, hashed_pass, "usuario"))

        conexion.commit()
        print(f"Usuario '{Usuario_Name} {Usuario_Surname}' registrado exitosamente")
        print(f"Email: {Usuario_Correo}")
        
    except sqlite3.Error as e:
        print(f"Error al registrar el usuario: {e}")
    finally:
        conexion.close()

# Inicializar base de datos al importar el módulo
inicializar_base_datos_completa()