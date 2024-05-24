#formula: peso(kg) / altura(m) 

peso = int(input("dame tu peso"))
altura = int(input("dame tu altura"))

imc = peso / (altura ** 2)
print("tu IMC es: ", imc)
