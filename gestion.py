users = []

def createUser():
    user = []
    id = int(input("Ingrese su documento de identidad "))
    user.append(id)
    user_name = input("Ingrese su nombre ")
    user.append(user_name)
    user_last_name = input("Ingrese su apellido ")
    user.append(user_last_name)
    phone = input("Ingrese su numero de telefono ")    
    user.append(phone)      
    user_email = input("Ingrese su correo electronico ")
    user.append(user_email)
    user_password = input("Ingrese su contraseña ")
    user.append(user_password)
    user_type=""
    option = int(input("\nIngrese su rol\n1.Profesor\n2.Estudiante\n3.Admin"))
    match option:
        case 1: user_type="Profesor"
        case 2: user_type="Estudiante"
        case 3: user_type="Admin"
    user.append(user_type)
    users.append(user)
    print(users)

    