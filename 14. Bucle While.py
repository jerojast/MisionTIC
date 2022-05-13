import math

#Variable

i=1

#Sintáxis es while + condición. en este caso es infinito porque no es posible finalizar poruqe no se cumple la condición, de manera que uso i=i+1 para que logre llegar a la condción y finalice
while i<=10:
	print("Ejecución " + str(i))
	i=i+1

print("Terminó la ejecución")

#Vamos a usar un ejemplo con el indeterminado de while

edad=int(input("Introduce la edad: "))

#Puedo poner más operadores en el while

while edad<5 or edad>100:
	print("Has introducido una edad no válida")
	edad=int(input("Introduce la edad: "))

print("La edad registrada es: " + str(edad))
print("Gracias por visitarnos")

#Vamos a ver cómo hacer para que un BUCLE no sea infinito

print("Programa de cálculo de raíz cuadrada")

numero=int(input("Introduce tu número: "))

intentos=0

while numero<0:
	print("No es posible hallar la raíz de un número negativo")

	if intentos==2:
		print("Has superado el número de intentos")
#Break rompe la ejecución del programa
		break;

	numero=int(input("Introduce tu número: "))
	if numero<0:
		intentos=intentos+1

#Math orientado a objetos se debe importarlo

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))