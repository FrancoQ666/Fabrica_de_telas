print("es hora de iniciar secion")
i = 3
c = 0
while(i < 3):
    c =* 0
    Usuario_Name_Attempt = input("Ponga su Nombre de Usario: ").strip() #aqui usaria el usuario
    Usuario_Contrasenia_Attempt = input("Ponga su Contraseña: ").strip() #aqui usaria la contraseña del usuario

    if Usuario_Name_Attempt == Usuario_Name:
        c += 1
    if Usuario_Contrasenia_Attempt == Usuario_Contrasenia:
        c += 1
    if c == 2:
        print("Iniciando secion. . .")
        break
    print("ERROR, INTENTE DE NUEVO")

if i = 0:
    print("de le acabaron las oportunidades, sesion no iniciada")
    print("*imagen del emoji triste*")
    print("salir: 1")
    perdedor = input("Elija su opcion: ").strip()
    #aqui lleva al menu de inicio
else:
    print("Secion Iniciada!")
    #aqui lleva al menu principal