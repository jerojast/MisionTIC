#El * le hace saber a pytohn que va a recibir un número x de argumentos y serán en forma de Tupla
def devuelve_ciudades(*ciudades):

	for elemento in ciudades:
		#for subElemento in elemento: omitimos este porque usamos yield from
		yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Bogotá", "Barcelona", "Medallo")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))