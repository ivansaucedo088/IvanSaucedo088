# Pedir al usuario que ingrese tres promedios
promedio1 = float(input("Ingrese el primer promedio: "))
promedio2 = float(input("Ingrese el segundo promedio: "))
promedio3 = float(input("Ingrese el tercer promedio: "))

# Comparar los promedios y encontrar el mayor
if promedio1 > promedio2 and promedio1 > promedio3:
    mayor = promedio1
elif promedio2 > promedio1 and promedio2 > promedio3:
    mayor = promedio2
else:
    mayor = promedio3

# Imprimir el mayor promedio
print("El mayor promedio es:", mayor)
