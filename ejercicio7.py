#costos de envio 

x = int(("cuantos kilos vas a enviar?"))

if x <= 1:
    print("el cobro sera $50")
elif x > 1 and  x < 5:
    print("el cobro sera $100")
elif x > 5 and  x < 10:
    print("el cobro sera $200")
else:
    print("el cobro sera $500")