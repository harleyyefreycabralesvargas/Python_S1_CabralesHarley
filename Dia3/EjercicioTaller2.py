def InteresCompuesto(co):
    c=co*((1+(f/x))**x)
    return c

def InteresSimple(sim):
    s=sim*(f)*x
    return s
print("Para calcular interes simple presione 1")
print("Para calcular interes compuesto presione 2")
z=int(input("Cual desea hallar"))
if z==1:
    sim=float(input("Dame el valor del capital "))
    p=float(input("Dame el valor del interes anual en % "))
    a=float(input("Cada cuantos meses se realiza este interes "))
    f=p/100
    x=12/a
    print("Valor interes simple ", InteresSimple(sim))
    print("Valor total ", InteresSimple(sim)+sim)
elif z==2:
    co=float(input("Dame el valor del capital "))
    p=float(input("Dame el valor del interes anual en % "))
    a=float(input("Cada cuantos meses se realiza el interes "))
    f=p/100
    x=12/a
    print("valor interes compuesto ", InteresCompuesto(co)-co)
    print("valor total ", InteresCompuesto(co))