edades = [11, 6, 13, 18, 25, 17, 30, 14, 65, 80]

infancia=[]
adolecencia=[]
jovenes=[]
adultos=[]
# Clasificación de edades
for edad in edades:
    if edad >= 6 and edad <= 11:
        infancia.append(edad)
    elif edad >= 12 and edad <= 17:
        adolecencia.append(edad)
    elif edad >= 18 and edad <= 26:
        jovenes.append(edad) 
    else:
        adultos.append(edad)

# Imprimir las listas resultantes
print("infancia", infancia)
print("adolecencia", adolecencia)
print("jovenes", jovenes)
print("adultos", adultos)
