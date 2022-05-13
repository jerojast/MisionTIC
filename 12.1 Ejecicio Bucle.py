#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra=input("Introduce tu palabra: ")

for i in range(10):
	print(palabra)

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("¿Cuántos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")

	