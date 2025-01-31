##escribimos la condicion que se tiene que cumplir
print("condicion:p*p*p+q*q*q*q-2*p*p menor a 680")
##vamos a mostrar los numeros que cumplen con la condicion dada
print("las numeros que cumplen la condicion son:")
##hacemos un para, para p 
for p in range(1,21):
    ##hacemos un para, para q
    for q in range(1,21):
     if ((p**3)+(q**4)-(2*p**2))<680:
        ##hacemos una condicion con los numeros p y q de los paras
        print("cumplen la condicion p=",p,"q=",q)
        ##mostramos los numeros que cumplen esta condicion
##realizado por: Harley Yefrey Cabrales Vargas        