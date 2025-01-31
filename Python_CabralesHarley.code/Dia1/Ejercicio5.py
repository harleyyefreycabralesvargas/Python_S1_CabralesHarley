##mostramos cual es la secuencia
print("secuencia: 1,1,2,-1,1,-2,?")
##definimos los 2 primeros numeros de la sucesion 
a=1
b=1
##hacemos un para desde 1 a 6 ya que el valor a hallar es el paso 5
##mostramos la secuencia
print("secuencia")
print("paso 1: 1")
print("paso 2: 1")
for i in range (1,100000000000000000):
    if i%2==0:
        c=a-b
        a=b
        b=c
        ##hacemos un condicional que si se cumple que el residuo de dividir i ente 2 es 0 hacemos que se reste el antepenultimo con el penultimo numero y que el resultado se guarde en c despues hacemos que b tome el valor del c y el antepenultimo numero tome el valor del penultimo numero 
    else:
        c=a+b
        a=b
        b=c
        ##hacemos un condicional que si se cumple que el residuo de dividir i ente 2 es 0 hacemos que se sume el antepenultimo con el penultimo numero y que el resultado se guarde en c despues hacemos que b tome el valor del c y el antepenultimo numero tome el valor del penultimo numero 
        ##ahora vamos a mostrar los valores de la secuencia
    print("paso ",i+2,": ",c)
##realizado por: Harley Yefrey Cabrales Vargas

