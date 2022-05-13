Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5+6
11
>>> 5/36
0.1388888888888889
>>> #El módulo es el resto de una divisón si no se utilizarán decimales, se maneja con el símbolo %, por ejemplo
>>> 10%3
1
>>> 5**3
125
>>> #La división entera te arroja el valor entero de una división sin décimales, por ejemplo
>>> 9//2
4
>>> #las variables en python son definidas por el contenido y no por el contenedorm, es decir, por lo que va después del = , yo puedo decir text=5 a, a pesar de que digo que es texto en realidad python lee la variable como un número entero. Aquí también, se utiliza el _ para conectar el nombre de la variable, por ejemplo, mi_nombre=5, finalmente hay que tener en cuenta que para python todo son objetos. Veremos la función type() que me arroja el tipo de dato de mi variable
>>> nombre=5
>>> type(nombre)
<class 'int'>
>>> #acá python nos dice que la variable previamente introducida es de tipo int es decir entero
>>> nombre=Esteban
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Esteban' is not defined
>>> nombre="Esteban"
>>> type(nombre)
<class 'str'>
>>> nombre=5.2
>>> type(nombre)
<class 'float'>
>>> #vamos a usa la triple comilla, sirve para introducir saltos de texto
>>> mensaje="""esto es un mensaje
... con tres
... saltos de línea"""
>>> print(mensaje)
esto es un mensaje
con tres
saltos de línea
>>> #vamos a ver la función if por lo que se van a comparar variable con esta función utilizando operadores de comparación
>>> Número1=5
>>> Número2=7
>>> if Número1>Número2:
... 	print("El Número 1 asigando es mayor al valor comparado")
... else:
... 	print("El Número 1 asigando es menor al comparado")
... 
El Número 1 asigando es menor al comparado
>>> 
***Repl Killed***

>>> 
>>> 
>>> 