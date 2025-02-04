def celcius_a_fahrenheit(c):
    result=(c*9/5)+32
    return result
def fahrenheit_a_celcius(d):
    resultt=(d-32)*5/9
    return resultt
i=int(input("Para pasar de celcius a fahrenheit presione 1, para pasar de fahrenheit a celcuis presione 2: "))
if i!=1 and i!=2:
    print("Dato no coincidente, por favor digite un parametro correcto")
elif i==1:
 c=float(input("Dame los grados celcius que quieres pasar a fahrenheit: "))
 print(celcius_a_fahrenheit(c))
else:
 d=float(input("Dame los grados fahrenheit que quires pasar a celcius: "))
 print(fahrenheit_a_celcius(d))