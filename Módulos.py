#Se va a importar un módulo
#Para ver sus funciones le doy f12 o click derecho definition

from cmath import atan
import math

#Ctrl space abre el autocompletado

tempora1 = math . tau

print (tempora1)

tempora1 = math . atan (512)

print (tempora1)

#Vamos a definir los tipos de los parámeteros y de lo que 
#devuelva mi función suma

def funcion_suma (num1: float, num2: float) -> float:
    return ( num1 + num2 )

#Puedo importar únicamente una sección de la librería
#para reducir el peso del código, ya que import math me trae
#toda la librería

from math import acos
from math import pi
from math import sinh
from math import atan

#Ahora ya no es necesario decir math.FUNCION, porque la llamé
#en específico

tempora1 = pi

print (tempora1)

#vamos a traer la función suma desde la que creamos desde
#Librería_1

from Librería_1 import funcion_suma

tempora1 = funcion_suma (7.5 , 3.4584596)

print (tempora1)

#Vamos a usar la función input

tempora1 = input("Introduzca el número que desea calcular el arcotangente: ")

tempora2 = atan (float (tempora1))

print ("El resultado de la arcotangente del número introducido es: " + str(tempora2))

#Podemos cambiar el nombre de una función de una librería
#La libreria math maneja atan en radianes, pasemoslo a grados desde librería_1

from math import atan as atan_radianes

from Librería_1 import atan as atan_grados

tempora1 = input("Introduzca el número que desea calcular el arcotangente, en radianes: ")

tempora2 = atan_radianes (float (tempora1))

print ("El resultado de la arcotangente del número introducido es: " + str(tempora2))

tempora1 = input("Introduzca el número que desea calcular el arcotangente, en grados: ")

tempora2 = atan_grados (float (tempora1))

print ("El resultado de la arcotangente del número introducido es: " + str(tempora2))

#La función round redondea los décimales, es diferente de //

tempora1 =  round (4.5125*2.53 , 3)

print (str(tempora1))
