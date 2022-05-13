#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado

Nombre=(input("Introduzca su nombre: "))

Dirección=(input("Introduzca su dirección: "))

Teléfono=(input("Introduzca su número de teléfono: "))

Lista_Datos_Personales=[Nombre, Dirección, Teléfono]

print("Los datos personales son:" + Lista_Datos_Personales[0] + ", " +
	Lista_Datos_Personales[1] + ", " + Lista_Datos_Personales[2])