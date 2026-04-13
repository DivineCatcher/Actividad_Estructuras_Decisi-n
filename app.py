import os
os.system("cls")

# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

try: 
    edad = int(input("Ingrese su edad: \n"))
    if edad < 18:
        print("Usted es menor de edad")
    else: 
        print("Usted es mayor de edad.")
except:
    print("Caracter invalido")
# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

user1_correct = "pedro"
user2_correct = "angel"
pass1_correct = "1234"
pass2_correct = "a4s1"

user = input("Ingrese su nombre de Usuario: \n")
contraseña = input("ingrese su contraseña: \n")

if user == user1_correct and contraseña == pass1_correct:
    print(f"Bienvenido, {user1_correct}")
elif user == user2_correct and contraseña == pass2_correct:
    print(f"Bienvenido, {user2_correct}")
else:
    print("Usuario o contraseña invalidos.")



# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

try: 
    nota1 = float(input("ingrese la primera nota: \n"))
    nota2 = float(input("Ingrese la segunda nota: \n"))
    nota3 = float(input("Ingrese la tercera nota: \n"))
    prom = (nota1 + nota2 + nota3)/3
    if prom >= 4.0: 
        print("Aprobado")
    else: 
        print("Reprobado")
        
except: 
    print("Ingrese caracters validos.")