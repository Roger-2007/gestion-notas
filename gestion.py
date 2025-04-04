users = []
user_type_active = []
name_active=[]
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
            user_type_active.clear()
            user_type_active.append(user[6]) 
            name_active.clear()       
            name_active.append(user[4])    
            print("Usted ha inciado sesion correctamente")
        else:
           print("Correo o contraseña incorrectos")

def createSubject():
    if user_type_active[0]=="Admin":
        subject = []
        subjectName = input("Ingrese el nombre del curso ")
        subject.append(subjectName)
        subjects.append(subject)
    else:
        print("Usted no tiene permisos para crear cursos")

def updateGrades():
    if user_type_active[0]=="Profesor":
        i = 0
        print("Ingrese el estudiante que quiere calificar")
        for user in users:
            if user[6]=="Estudiante":
                print(f"{i}. {user[1]}")
            i+=1
        u = int(input("numero"))
        user_selected = users[u]
        name_user_selected = user_selected[1]
        j=1
        for subject in subjects:
            print(f"{j}. {subject[0]}") 
            j+=1  
        s = int(input("numero"))-1
        subject_selected = subjects[s] 
        grade = float(input("Ingrese la nota del estudiante"))
        userGrades = []
        userGrades.append(name_user_selected)
        userGrades.append(grade)
        subject_selected.append(userGrades)
        print("Nota registrada con exito")
    else:
        print("Usted no puede subir notas")   

def viewGrades():
    if user_type_active[0]=="Estudiante":    
        i = 1
        for subject in subjects:
            print(f"{i} {subject[0]}")
        s = int(input("Ingrese que materia quiere consultar"))-1
        subject_selected = subjects[s]
        for grade in subject_selected:
            if name_active[0]==grade[0]:
                print(f"Su nota es: {grade[1]}")    
    else:
        print("Usted no puede ver las notas")            
        
#Menu
option = option = int(input("Ingrese una opcion\n1. Crear usuario"))
match option:
    case 1:createUser()
    case _:print("Opcion invalida")

option = int(input("Ingrese una opcion\n1. Crear usuario\n2. Iniciar sesion\n3. Subir notas\n4. Consultar notas\n5. Crear materia\n6. Salir")) 
while option!=6:
    match option:        
        case 1: createUser()
        case 2: loginUser()
        case 3: updateGrades()
        case 4: viewGrades()
        case 5: createSubject()
        case 6: print("Cerraste el sistema con exito")
        case _: print("Opcion no valida")
    option = int(input("\nIngrese una opcion\n1. Crear usuario\n2. Iniciar sesion\n3. Subir notas\n4. Consultar notas\n5. Crear materia\n6. Salir"))     