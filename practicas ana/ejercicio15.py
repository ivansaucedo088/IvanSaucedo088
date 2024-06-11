# Lista de edades
edades = [15, 20, 13, 18, 25, 17, 30, 14]

# Listas vacías para mayores y menores de edad
mayores_de_edad = []
menores_de_edad = []

# Clasificación de edades
for edad in edades:
    if edad >= 18:
        mayores_de_edad.append(edad)
    else:
        menores_de_edad.append(edad)

# Imprimir las listas resultantes
print("Mayores de edad:", mayores_de_edad)
print("Menores de edad:", menores_de_edad)
