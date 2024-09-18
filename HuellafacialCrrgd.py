import random

datosBiometricos = [[], [], []]  # List of lists to store [nombreUsuario, huellaUsuario, codigo]
numPersonas = 0

print("--------SISTEMA BIOMETRICO--------------")
print("----------Bienvenidos-------------------")

while True:
    print("¿Qué acción desea realizar?")
    print("1) Login")
    print("2) Registro")
    print("3) Recuperar clave")
    print("4) Salir")
    tipo = int(input("Ingrese la opción: "))

    if tipo == 4:
        break
    
    elif tipo == 1:  # Login
        user = input("Ingrese el rostro de la persona: ")
        
        if user in datosBiometricos[1]:  # Check if the facial data exists in datosBiometricos
            index = datosBiometricos[1].index(user)
            print(f"Bienvenido, {datosBiometricos[0][index]}")
            print("---Acceso a los módulos---")
            
            while True:
                print("¿Qué acción desea realizar?")
                print("1) Cerrar sesión")
                opcion = int(input("Ingrese la opción: "))
                
                if opcion == 1:
                    break
                else:
                    print("Opción inválida.")
        
        else:
            print("No existe ese usuario.")
    
    elif tipo == 2:  # Registro
        numPersonas = int(input("Ingrese el número de personas a registrar: "))
        
        for i in range(numPersonas):
            print(f'Ingrese los datos de la persona {i + 1}')
            nombreUsuario = input("Nombre de la persona: ")
            huellaUsuario = input("Huella facial: ")
            codigo = random.randrange(1000, 9999)
            
            datosBiometricos[0].append(nombreUsuario)
            datosBiometricos[1].append(huellaUsuario)
            datosBiometricos[2].append(codigo)
 
        print("Usuarios registrados exitosamente.")
    
    elif tipo == 3:  # Recuperar clave
        nombreUsuario = input("Ingrese el nombre de usuario para recuperar clave: ")
        
        if nombreUsuario in datosBiometricos[0]:
            index = datosBiometricos[0].index(nombreUsuario)
            print(f"El código de usuario para {nombreUsuario} es: {datosBiometricos[2][index]}")
        else:
            print("No existe esa persona.")
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
    
print("----Muchas gracias por usar el sistema biometrico----")
