def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("Seleccione el tipo de conversión de temperatura:")
    print("1. De Celsius a Fahrenheit")
    print("2. De Fahrenheit a Celsius")
    print("3. Salir")
    opcion = input("Ingrese su opción (1, 2, o 3): ")

    if opcion == '1':
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.\n")
    elif opcion == '2':
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.\n")
    elif opcion == '3':
        print("Gracias por usar el programa. ¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.\n")
