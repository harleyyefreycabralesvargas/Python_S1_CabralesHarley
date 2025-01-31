##definos a "b" y "c" como el numero mas pequeño y mas grande posible
b=-1
c=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
##hacemos un para en el rango 1 a 11 para que se repita 10 veces
for i in range (1,11):
 ##hacemos que se repita 10 veces la lectura de un numero
 a = int(input("dame los 10 numeros"))
 if a>b:
  b=a
  mayor=b
  ##hacemos un condicional que si se cumple que a>b, b pase a ser a y le asignamos a "mayor" el valor de b  
 elif a<c:
  c=a
  menor=c
   ##hacemos un condicional que si se cumple que a>c, c pase a ser a y le asignamos a "menor" el valor de c
##mostramos cual es el numero menor y mayor entre los 10  
print("el menor es: ",menor)
print("el mayor es: ",mayor)
  
  
  
  

  
