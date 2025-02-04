from modulo import *
nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]
apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]
zzz=True
while zzz==True:
    print("Para ver la lista de estudiantes presione 1")
    print("para añadir un estudiante presione 2")
    print("para modoficar un estudiante presione 3")
    print("para eliminar un estudiante presione 4")
    print("para salir presione 5")
    opcion=int(input("cual opcion deseas hacer: "))
    if opcion==1:
      lista(nombres,apellidos)
    if opcion==3:
        a=True
        while a==True:
            c=int(input("Cual estudiante desea modificar: "))
            s=int(input("Si desea modificar nombre presione 1, si desea modificar apellido presione 2: "))
            if s==1:
                k=input("Cual es el nuevo nombre que desea editar: ")
                editar(c-1,nombres,k)
            elif s==2:
                g=input("Cual es el nuevo apellido que desea editar: ")
                editar(c-1,apellidos,g)
            d=int(input("Desea seguir editando 1:si 2:no : "))
            if d==2:
                a=False  
    if opcion==2:
        nombrenuevo=input("cual es el nombre del nuevo estudiante que deseas agregar: ")   
        apellidonuevo=input("cual es el apellido del nuevo estudiante que deseas agregar: ")
        agregar(nombres,nombrenuevo,apellidos,apellidonuevo)
    if opcion==4:
        r=int(input("cual es el estudiante que deseas eliminar: "))    
        eliminar(r-1,nombres,apellidos)
    if opcion==5:
        apagar(opcion,zzz)  
        break