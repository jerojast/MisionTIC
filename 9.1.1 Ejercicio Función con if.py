#Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos

#Creo la función

num1=(int(input("Introduce el primer número: ")))

num2=(int(input("Introduce el segundo número: ")))


def DevuelveMax (n1, n2):

	if num1<num2:
		print("n2 es mayor que n1")
		return num2
	elif num1>num2:
		print("n1 es mayor que n2")
		return num1
	else:
		print("n1 es igual a n2")

DevuelveMax(num1, num2)

print("Fin del programa")