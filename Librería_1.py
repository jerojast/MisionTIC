#Vamos a crear nuestra propia librería

def funcion_suma (num1: float, num2: float) -> float:
    suma =  num1 + num2
    mensaje = "La suma de los números es: " + str(suma)
    return mensaje

# Vamos a pasar de atan de radianes a grados porque la libreria math maneja atan en radianes

import math

def atan ( x:float ) -> float:
    return math.atan(math.pi / 180 * x)
