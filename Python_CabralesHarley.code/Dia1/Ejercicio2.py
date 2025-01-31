##aca le pedimos al usuario cual es el paso que quiereb hallar
paso=int(input("Dame el paso quere deseas hallar"))
##le damos el valor de cero a la sumatoria
sumatoria=0
##hcamos un para desde el numero 1 hasta el numero (paso+1) con iterador i
for i in range (1,paso+1):
    ##hacemos un si
    if i%2==0 :
        sumatoria=sumatoria-1/i
        ##si el numero del para al dividirlo en 2 deja como residuo 0 se le resta (1/i) a la sumatoria 
    else:
        sumatoria=sumatoria+1/i
        ##si no a la sumatoria se le suma (1/i)
    print("paso",i,": ",sumatoria)
    ## mostramos el paso en el que vamos y su valor
    ##realizado: por Harley Yefrey Cabrales Vargas
    