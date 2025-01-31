x=int(input("Ingrese el primer numero: "))
y=int(input("Ingrese el segundo numero: "))
##ponemos el contador de la suma del numero "x" y "y"
sumx=0
sumy=0
## pedimos los 2 numeros que queremos saber si son amigos
for i in range(1,(x+1)):
    ##hacemos un ciclo para, que vaya desde 1 hasta la mitad del primer numero que seria su ultimo divisor
    if x % i == 0:
        sumx=sumx+i
        ## si se cumple que el residuo de dividir x en i es 0 entonces sumamos sus divisores "i" y lo guardamos en sumx
for i in range(1,(y+1)):
    if y % i ==0:
        sumy=sumy+i
        ##hacemos ahora lo mismo pero con "y" y lo guardamos en sumy
if sumx==sumy:
    print("Son numeros amigos")
    ## si cumple escribir que son numeros amigos
else:
    print("No son numero amigos")
    ## si no cumple decir que no son numeros amigos

##realizado por: Harley Yefrey Cabrales Vargas
print(sumx, " ", sumy)