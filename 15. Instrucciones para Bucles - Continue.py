for letra in "Python":
	
	if letra=="h":
		#Continue quiere decir que cuando se encuentre con esta condición ignora la siguiente parte del bucle en esta iteración
		continue

	print("Viendo la letra: " + letra)

#Vamos con otro ejemplo, aquí vamos a ignorar el conteo del espacio vacío porque solo queremos contar letras
#Variable

nombre="Pildoras Informáticas"

contador=0

for i in nombre:

	if i==" ":
		continue
#Lo siguiente es lo mismo que poner contador=contador+1
	contador+=1

print(contador)