from CRUD import create
from CRUD import readAll
from CRUD import update
from CRUD import delete
from CRUD import obtenerClaves

def menuprincipal():
    print ( "--Aplicación CRUD--")
    print ("1. Crear Tarea")
    print ("2. Consultar Tarea")
    print ("3. Actualizar Tarea")   
    print ("4. Eliminar Tarea")
    print ("5. Salir del programa")
    opcion = input ("Seleccione una opción: ")
    return opcion

def CrearTarea ():

    claves = obtenerClaves ()
    CodigoTarea = input ("Por favor introduzca el código de la nueva tarea: " )
    
    if CodigoTarea in claves:
        print("El código introducido ya existe en la base de datos")
        return
          
    descripcion = input ("Por favor introduzca la descripción de la tarea: ")
    TiempoTarea = int (input ("Introduzca la duración de la tarea en minutos: "))
    TareaNueva = {
        "Descripción" : descripcion,
        "Estado" : "Pendiente",
        "Tiempo" : TiempoTarea
    }
    create (CodigoTarea,TareaNueva)
    print ("Se ha creado exitosamente la tarea.")
    
    return

def LeerTareas ():
    print ("Las tareas guardadas son: ")
    tareas = readAll()
    
    for (clave, tarea) in tareas:
        print ("--------------------------------------------------------")
        
        print ("La tarea tiene código: " + clave)
        descripcion = tarea ["Descripción"]
        print ("La descripción de la tarea es: " + descripcion)
        estado = tarea ["Estado"]
        print ("El estado de la tarea es: " + estado)
        tiempo = str (tarea ["Tiempo"])
        print ("El tiempo de duración de la tarea es de: " + tiempo + " minutos")
        
        print ("--------------------------------------------------------")
    return

def UpdateTarea ():
    
    claves = obtenerClaves()
    CodigoTarea = input ("Por favor introduzca el código de la tarea a actualizar: " )

    if not (CodigoTarea in claves):
        print("El código introducido ya existe en la base de datos")
        return
    
    descripcion = input ("Por favor introduzca la descripción de la tarea a actualizar: ")
    estado = input ("Por favor introduzca el estado de la tarea a actualizar: ")
    TiempoTarea = int (input ("Introduzca la nueva duración de la tarea en minutos: "))
    
    TareaActualizada = {
        "Descripción" : descripcion,
        "Estado" : estado,
        "Tiempo" : TiempoTarea
    }
    update (CodigoTarea, TareaActualizada)
    print ("Se ha actualizado exitosamente la tarea.")
    return

def EliminarTarea ():
    eliminar = input ("Por favor introduzca el código de la tarea a eliminar: ")
    delete (eliminar)
    print("La tarea se eliminó correctamente")
    return