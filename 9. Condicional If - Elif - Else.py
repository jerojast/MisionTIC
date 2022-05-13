print("Verificación de Acceso")

#Nueva variable

edad_usuario=int(input("Introduce tu edad por favor: "))

#Vamos con If

if edad_usuario<18:
	print("El ingreso no es permitido")

#Ahora meteremos elif, es una unión de else e if y sirve para usar las combinaciones de estos, es decir, poder tener dos condiciones y ejecutar eventualmente un else si nada de lo anterior se cumple

elif edad_usuario>100:
	print("Por favor valide su edad y vuelva a ejecutar el programa")
else:
	print("Bienvenido")

#Se usa el .else (y si no es verdad) de manera que verifique si el .if se cumple. El .if puede ir solo, sin embargo, el .else, nunca puede ir solo, debe acompañarse del if

print("El programa ha finalizado")

#Vamos a hacer un programa ahora que asinge lo cualitativo a una calificación

print("Verificación de Acceso")

#Nueva variable

nota_alumno=int(input("Introduce tu nota, por favor: "))

if nota_alumno<3:
	print("Suspenso")

elif nota_alumno<4:
	print("Suficiente")

elif nota_alumno<5:
	print("Muy bien")

elif nota_alumno>5:
	print("Por favor introduzca una nota dentro del rango válido")

else:
	print("Excelente")