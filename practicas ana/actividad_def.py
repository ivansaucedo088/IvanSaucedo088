a = 5
b = 5
# sumas
def sumar(a,b):
    print("la suma es: ", a+b)

# restar
def restar(a,b):
    print("la resta es: ", a-b)

#multiplicacion
def multiplicar(a,b):
    print("la multiplicacion: ", a*b)

# division
def division(a,b):
    print("la multiplicacion es: ", a/b)


j = int(input(("selecciona una opcion \nsuma(1) \n resta(2) \n multiplicacion(3) \n divicion(4)\n")))

if j == 1:
    sumar(a, b)

elif j ==2:
    restar(a,b)

elif j ==  3:
    multiplicar(a, b)
else:
    division(a, b)


          
