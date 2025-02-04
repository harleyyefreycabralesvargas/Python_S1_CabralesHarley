def editar(numeroe,nombres,nombrenuevo):
    nombres[numeroe]=nombrenuevo
def agregar(nombres1,nombrenuevo1,apellidos1,apellidonuevo1):
    nombres1.append(nombrenuevo1)
    apellidos1.append(apellidonuevo1)
def eliminar(numeroe1,nombres,apellidos):
    del nombres[numeroe1]
    del apellidos[numeroe1]
def lista(nombres,apellidos):
     for i in range (len(nombres)):
          print("Estudiante ",i+1, " " .join(nombres[i]) ," " .join(apellidos[i]))
def apagar(apagar,negro):
    negro=apagar