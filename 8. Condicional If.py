#Defino una función aquí en def

def evaluación(nota):

#Creo una variable llamada "Valoración" 

	valoración="Aprobó"

#Utilizo "if" y su sintáxis es como se presenta a continuación

	if nota<5:

#Aquí se le dice a if que si no cumple la condición, cambie el valor de la variable de "Aprobó" a "Perdió"

		valoración="Perdió"

#Aquí que devuelva lo que arroje la variable

	return valoración

print(evaluación(4))

#Segunda parte del ejercicio; iniciamos poniendo un título al programa

print("Programa de evaluación de notas de alumnos")

#vamos ahora a usar .input que permite ingresar datos en el teclado y hasta no dar Enter, el programa no continua
#definimos una nueva variable; dentro de input puede haber un mensaje

Nota_Alumno=input("introduce la nota del alumno")
def evaluación(nota):
	valoración="Aprobó"
	if nota<5:
		valoración="Perdió"
	return valoración

#Ahora no podemos llamar igual que antes, debemos llamar a Nota_Alumno

print(evaluación(int(Nota_Alumno)))

#Inicialmente arroja error porque .input lee todo lo que introducimos como texto, debemos hacerle entender que es en realidad un valor numérico
#Para hacer lo anterior usamos .int que transforma en un valor entero siempre que sea posible
