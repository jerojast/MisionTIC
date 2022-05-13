# los generadores sonb similares a las funciones solo que no llevan return si no yield

#el argumento límite me sirve para detener la función y que no se vuelva infinita

def numpares(limite):

	num=1

#Esta lista es la que almacenará los números

	milista=[]

	while num<limite:

		milista.append(num*2)

		num=num+1

	return milista

print(numpares(10))

#Lo anterior era tipo función ahora hagamoslo como generador


def numimpares(limite2):

	num2=1

	while num2<limite2:

		yield num2*1

		num2=num2+1

#Debo crear una variable que alamcene los objetos

devuelveImpares=numimpares(10)

print(next(devuelveImpares))

print("Aquí podría ir más código...")

print(next(devuelveImpares))

print("Aquí podría ir más código...")

print(next(devuelveImpares))