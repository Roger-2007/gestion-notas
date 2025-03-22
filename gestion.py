users = []
user_type_active = ""
subjects = []

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

def loginUser():
    emailLogin = input("Ingrese su email")
    passwordLogin = input("Ingrese su contraseña")
    for user in users:
        if(user[4]==emailLogin and user[5]==passwordLogin):
            print("Usted ha inciado sesion correctamente")
            user_type_active=user[6]
        else:
           print("Correo o contraseña incorrectos")

def createSubject():
    if user_type_active=="Admin":
        subject = []
        subjectName = input("Ingrese el nombre del curso ")
        subject.append(subjectName)
        subjects.append(subject)
    else:
        print("Usted no tiene permisos para crear cursos")

    