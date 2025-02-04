NumeroEmpleados=int(input("Ingrese el numero de empleados: "))
## pedimos cuantos empleados se van a registrar
horacomparada=0
horaguardada=0
totalsueldobruto=0
totaleps=0
totalpension=0
totalsueldoneto=0
personamenorsueldo=""
personamayorsueldo=""
me=0
ma=0

## definimos dos variables para despues en el mayor y menor sueldo
for i in range(1,NumeroEmpleados+1):
    nombre=input("Ingrese el nombre del empleado en orden del que mas horas trabajo a menos horas trabajo: ")
    ## pedimos el nombre del empleado
    horas=int(input("Ingrese el numero de horas trabajadas para el empleado: "))
    ## pedimos las horas que el empleado trabajo
    sueldobruto=horas*20000
    ## valor sueldo bruto
    totalsueldobruto=totalsueldobruto+sueldobruto
    ## total sueldo bruto
    eps=sueldobruto*0.04
    ## valor eps
    pension=sueldobruto*0.04
    ## valor pension
    sueldoNeto=sueldobruto-eps-pension
    ## valor sueldo neto
    totaleps=totaleps+eps
    ## total eps
    totalpension=totalpension+pension
    ## total pension
    totalsueldoneto=totalsueldoneto+sueldoNeto
    ## total sueldo neto
    if horas>horacomparada:
        ## un condicional para saber quien es la persona que mas hizo horas y por ende quien gano mas
        personamayorsueldo=nombre
        horaguardada=horacomparada
        horacomparada=horas
        ma=sueldoNeto
        
        ## si se cumple, la persona actual seria la que mas va ganando y despues se comnparara con la siguiente persona
    elif horas<horacomparada:
        horacomparada=horas
        personamenorsueldo=nombre
        me=sueldoNeto
        ## si no cumplen con la condicion despues se hallara cual es el menor sueldo de estas personas y se comparara despues si hay alguno mas menor
print("El total de salario bruto es: $", totalsueldobruto)
print("El total de pension es: $", totalpension)
print("El total de eps es: $", totaleps)
print("El total del salario neto es: $", totalsueldoneto)
print("El empleado que mas sueldo gano fue: $",personamayorsueldo," con: $",ma)
print("El empleado que menos sueldo gano fue: $",personamenorsueldo," con: $",me)
print("El promedio de los salarios brutos es de: $", (totalsueldobruto/NumeroEmpleados))
print("El promedio de los salarios netos es de: $", (totalsueldoneto/NumeroEmpleados))
## mostramos la informacion pedida del ejercicio

## realizado por: Harley Yefrey Cabrales Vargas