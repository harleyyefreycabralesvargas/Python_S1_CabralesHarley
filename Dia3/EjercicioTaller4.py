import string
import random
longitud=int(input("Ingrese la longitud de la cadena "))
pasword=string.ascii_uppercase + string.ascii_lowercase + "!#$%&/()=¿?*+-{}[]" + "0123456789"
print(pasword)
a=string.digits(input("Que elemento deseas eliminar"))
paasword=pasword - a
cadena=""
for _ in range (longitud):
    cadena += random.SystemRandom().choice(paasword)

print(cadena)