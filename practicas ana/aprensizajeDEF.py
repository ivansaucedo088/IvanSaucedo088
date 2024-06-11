'''
es un bloque de codigo reutilizable que realiza una tarea especifica
ayuda a organizar el codigo, para hacerlo mas legible y evitar la  repeticion
'''
# Estructura basica #


''''
def NombreDeLaFuncion():
    # cuerpo de la funcion
nombreDeLaFuncion()
'''



# def para saludar con cualquier nombre
def saludar(nombre):
    print("hola", nombre)

saludar(input())

# def para sumar dos numeros

def sumas(a,b):
    print("la sumas de a y b es: ", a + b)
sumas(int(input()), int(input()))
print(sumas)
