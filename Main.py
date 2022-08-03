from Interfaz import *

opcion = 0

while opcion != "5":
    opcion = menuprincipal ()
    if opcion == "1":
        opcion = CrearTarea ()
    elif opcion == "2":
        opcion = LeerTareas ()
    elif opcion == "3":
        opcion = UpdateTarea ()
    elif opcion == "4":
        opcion = EliminarTarea ()
    elif opcion == "5":
        break