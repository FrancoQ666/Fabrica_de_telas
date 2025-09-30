"""
Nuevo Suscripto: Suscripto.py
tiempo: 2023-10-30 20:00:00
"""

def tiempo():
    print("\nTiempo restante: 30 dias\n")

def Renovar():
    opcion = input("\nDesea renovar la suscripcion? (si/no): ").lower()
    if opcion == "si":
        print("Suscripcion renovada por 30 dias.")
    else:
        print("No se renovó la suscripcion.")

def ajustar():
    print("\n--- Ajustar ---")
    print("1. Tamaño")
    print("2. Cuenta")
    print("3. Volver")
    input("Seleccione una opcion: ")
    print("⚙ Ajuste realizado.")

def Cancelar():
    opcion = input("\nEsta seguro que desea cancelar la suscripcion? (si/no): ").lower()
    if opcion == "si":
        print("Suscripción cancelada.")
    else:
        print("Se mantiene la suscripcion activa.")

def informacion():
    print("\nInformacion: En el Papu Gimnasio podes acceder a todos los servicios que ofrecemos por el mismo precio: sala cardiovascular, musculación, peso libre con equipamiento de primera línea\n")
    print("\nclases grupales con mucha onda (Entrenamiento funcional, Ritmos, Yoga, Aero Local, Aero Combat, Abdominales y Estiramiento)\n")
    print("\nvestuarios modernos y planes de entrenamiento prediseñados.\n")
    
def perfil():
    print("\n--- Crear Perfil ---")
    nombre = input("Nombre: ")
    user_id = input("ID: ")
    fecha_registro = input("Fecha de registro (YYYY-MM-DD): ")
    fecha_suscripcion = input("Fecha de suscripción (YYYY-MM-DD): ")
    
    print("\nPerfil creado con exito:")
    print(f"Nombre: {nombre}")
    print(f"ID: {user_id}")
    print(f"Fecha de registro: {fecha_registro}")
    print(f"Fecha de suscripcion: {fecha_suscripcion}\n")

