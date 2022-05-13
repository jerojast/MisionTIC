print("Programa de Becas 2022")

#Genero mis variables

distacia_colegio=(int(input("Introduce la distancia a tu escuela en Km: ")))
print(distacia_colegio)

numero_de_hermanos=(int(input("Introduce el número de hermanos: ")))
print(numero_de_hermanos)

ingresos_familia=(int(input("Introduce en pesos el total de los ingresos mensuales de la familia: ")))
print(ingresos_familia)

#Se va a usar and para incluir todos los criterios

if distacia_colegio>20 and numero_de_hermanos>2 and ingresos_familia<=2000000:
	print("El estudiante es beneficiario")

else:
	print("El estudiante no tiene derecho a beca")

#Vamos a darle más peso a alguno de los criterios de selección, para ello cambiamos en operador and por el operador or
#El or es como si dijera, si lo anterior nada es cierto y lo que sigue sí dele prelación a lo que sigue

if distacia_colegio>20 and numero_de_hermanos>2 or ingresos_familia<=2000000:
	print("El estudiante es beneficiario")

else:
	print("El estudiante no tiene derecho a beca")

#Vamos ahora a usar el operador in con un nuevo ejemplo

print("Electivas Ingeniería Ambiental 2022-1")
print("Electivas: Ordenamiento Territorial - Contaminación I - Química Ambiental Aplicada")

Opción=input("Escribe la electiva elegida: ")

#Vamos a ponerlo todo en minúsculas con .lower; hay que tener cuidado que como ahora todo estpa en minpuscula, en la lista todo debe ir en minúscula

electiva=Opción.lower()

#Operador .in si está o no en el listado

if electiva in ("ordenamiento territorial", "contaminación i", "química ambiental aplicada"):
	print("Electiva disponible " + electiva)

else:
	print("La electiva no se encuentra disponible")