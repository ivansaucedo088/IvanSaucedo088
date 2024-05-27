area = 0
x = 0
resultado = 0
opcion = str
while x == 0 :


    print("calculadora de areas, ingrese una opcion #minuscula#")
    print("cuadrado (a)")
    print("triangulo (b)")
    print("rectangulo (c)")
    opcion = input("opcion ?? ")

    if opcion == "a":
        print("cuadrado")
        area = int(input("dame la distacia de el lado"))
        resultado = area * 4
        print("el area es: ", resultado)

    elif opcion == "b":
        print("triangulo")
        area = int(input("dame la distacia de el lado"))
        resultado = area * 3
        print("el area es: ", resultado)

    elif opcion == "c":
        area_2 = 0
        print("rectangulo")
        area = int(input("dame la distacia de el lado"))
        area_2 = int(input("dame la aultura"))
        resultado = area * area_2
        print("el area es: ", resultado)