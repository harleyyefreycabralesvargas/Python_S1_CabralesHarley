a=int(input("Dame el numero que quieres saber si es par o impar, primo o compuesto, numero cuadrado o no "))
z=0
x=0
if a==0:
    x=1
for i in range (1,a+1):
    if a%i==0:
        z=z+i
    if a/i==i:
        x=1
if a%2==0:
    print(a, " es par")
else:
    print(a, " es impar")    
if z!=a+1:
    print(a," es compuesto") 
else:
    print(a, " es primo.")
if x==1:
    print(a," es un numero cuadrado")
else:
    print(a, " no es un numero cuadrado")    