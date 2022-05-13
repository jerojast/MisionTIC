#La notación f da una característica especial (de función, es la que le dice a python coja la variable) al texto, por otra parte el usar los {} ayuda a que lo que haya adentro el print lo lea con la variable
for i in range(5):
	print(f"valor de la variable {i}")

#podemos usar el Range en intervalos como se ve a continuación y lo que hará será leer desde el 5 al 9
for i in range(5,10):
	print(f"valor de la variable {i}")

#También podemos usar rango y de cuánto en cuánto queremos que cuente la variable entonces el rango sería 5,50 y la tercera coma será de cuánto en cuanto , 3 en este caso cada tres
for i in range(5,50,3):
	print(f"valor de la variable {i}")

#Validaremos un email con range, para ello usamos .len

valido=False

email=input("Introduce tu correo electrónico: ")

for i in range(len(email)):

	if email[i]=="@":

		valido=True

if valido:
	print("email correcto")

else:
	print("Verifique su email")