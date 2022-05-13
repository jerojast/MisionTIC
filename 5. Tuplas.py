NombreTupla=("Claus","Jorge","Karito","Esteban",29,1,1996,1996)

#La tuplas son mas compactas (más rápidas y menos pesadas) no obstate no permite agregar, eliminar cosas sí permite hacer búsquedas

print(NombreTupla[5])

#Se puede generar listas desde una tupla y tupla desde una lista con list

Lista_de_Tupla=list(NombreTupla)

print(NombreTupla)

#Ahora de lista a Tupla con tuple

NombreLista=["Claus","Jorge","Karito","Esteban",29,1,1996,1996]

Tupla_de_Lista=tuple(NombreLista)

print(Tupla_de_Lista)

#Para contar un elemento con count

print(Tupla_de_Lista.count(1996))

#para conocer la longitud se usa len

print(len(Tupla_de_Lista))

#Se puede desempaquetar una Tupla, es decir asignar los valores de la tupla a unas variables

Tupla_Desempaquetar=("Claus","Jorge","Karito","Esteban",29,1,1996)

Mama, papa, hermana, yo, dia, mes, agno=Tupla_Desempaquetar

print(mes)
print(agno)
print(hermana)