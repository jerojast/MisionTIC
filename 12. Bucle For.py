#Bucle determinado FOR; funciona con declaración y cuerpo del bucle
#El Bucle se va a ejecutar el número de veces de acuerdo con el número de elementos en la lista

for i in ["Pirmavera", "Verano", "Otoño", "Invierno"]:
	print("Hola")

#En este caso ejecuta cuatro veces porque hay cuatro elementos
#La variable asume los valores asignados en la lista, es decir i=Primavera i=Verano y asi...

for i in ["Pirmavera", "Verano", "Otoño", "Invierno"]:
	print(i, end=" ") 

#Con End le digo al print como quiero finalizar el texto

#Si metemos un dato tipo string (Texto) lo imprimirá el número de veces de acuerdo con el número de caractéres que haya en el string

for i in "jerojast.96@gmail.com":
	print("Hola") 

#Vamos a comprobar el e-mail con base en el @

e_mail=False

for i in "jerojast.96@gmail.com":
	if(i=="@"):

		e_mail=True

#Acá se puede reemplazar e_mail==True por e_mail lo que implicitamente indica que la variable e_mail está en True
#Otro dato es que el = Asigna valores y el == compara valores

if e_mail==True:
	print("E-mail correcto")
else:
	print("Verifique el E-mail")

#Vamos ahora a evaluar un e-mail introducido

contador=0
miemail=input("Introduce tu usuario: ")

for i in miemail:
	if(i=="@" or i=="."):

		contador=contador+1

if contador==2:
	print("E-mail correcto")
else:
	print("Verifique el E-mail")

#Veamos ahora .Range le estoy diciendo, cree una lista de 5 elementos [0,1,2,3,4]

for i in range(5):
	print (i)