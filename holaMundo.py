import time
print("Hola Mundo!!!")

def saludar():
    nombre = input("Hola, Cual es tu nombre")
    return "Hola", nombre

print(saludar())

def pedir_edad():
    edad = int(input("Introduce tu edad: "))

    for i in range(1, edad+1):
        print("Has cumplido " + str(i) + " años")

print(pedir_edad())

time.sleep(5)
