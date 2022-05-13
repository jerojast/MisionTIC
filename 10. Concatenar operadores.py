#Define variables

edad=-7

#Que me omita las que son mayores que 100, vamos a concatenar dos comparativos con 0<variable<100

if 0<edad<100:
	print("Edad correcta")
else:
	print("Verifique su edad")

#Vamos ahora a hacer otro ejemplo

salario_presidente=(int(input("Introduce el salario del presidente: ")))

#Python no permite concatenar enteros con texto, se deben poner en el mismo sentido bien sea con int o comn str

print("Salario presidente: " + str(salario_presidente))

salario_director=(int(input("Introduce el salario del director: ")))
print("Salario director: " + str(salario_director))

salario_jefe_area=(int(input("Introduce el salario del jefe de área: ")))
print("Salario jefe de área: " + str(salario_jefe_area))

salario_administrativo=(int(input("Introduce el salario del administrativo: ")))
print("Salario administrativo: " + str(salario_administrativo))

#Vamos con el condicional

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Salarios correctamente asigandos")
else:
	print("Salarios mal asignados")