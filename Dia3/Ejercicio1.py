print("Los numeros divisibles ente 7 pero no divisibles entre 5 en el rango de 2000 a 3200 son")
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        print(i)