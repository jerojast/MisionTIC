#Aplicación CRUD que maneje una lista de tareas, manejado en un diccionario de diccionarios
tareas = {

    "t1" : {
        "Descripción" : "Ir a mercar",
        "Estado" : "Pendiente",
        "Tiempo" : 90
    },
    
    "t2" : {
        "Descripción" : "Hacer ejercicio",
        "Estado" : "Pendiente",
        "Tiempo" : 25
    },
    
    "t3" : {
        "Descripción" : "Hacer almuerzo",
        "Estado" : "Pendiente",
        "Tiempo" : 45
    }
}

def create (clave, nuevatarea):
    tareas [clave] = nuevatarea
    return

def readAll ():
    return tareas.items()

def update (clave, tarea):
    tareas [clave] = tarea
    return

def delete (clave):
    return tareas.pop(clave)

def obtenerClaves ():
    return tareas.keys()

print (obtenerClaves())