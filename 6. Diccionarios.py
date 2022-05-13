#Los diccionarios son como Listas o Tuplas com la diferencia de que incorporan el ítem clave : valor
#y el orden de este tipo de elemento no afecta así como si en las listas y tuplas, su sintaxtis es con {} en las listas es [] la tuplas ()
#vamos a trabajar claves:valor entonces en el ejemplo es país:capital

Mi_Diccionario={"Alemania":"Berlín","Francia":"París","Colombia":"Bogotá", "España":"Madrid"}

#para llamar un elemento de la lista accedemos mediante su clave

print(Mi_Diccionario["Colombia"])

#Para llamar todo el diccionario es solo con el nombre

print(Mi_Diccionario)

#Para agregar un elemento al diccionario se hace así (hay un erro es apropósito para la práctica)

Mi_Diccionario["Italia"]="Lisboa"
print(Mi_Diccionario)

#Ahora vamos a corregir el error (es reemplazar el vlor de la clave)

Mi_Diccionario["Italia"]="Roma"
print(Mi_Diccionario)

#Para eliminar un elemento es con el del

del Mi_Diccionario["Francia"]
print(Mi_Diccionario)

#Ahora vamos a intreoducir listas y tulpas o datos en el diccionario

Tupla_Diccionario=("Lucky","Chucky","Kira")
Mi_Diccionario2={"Mamá":53,"Papá":60,21:"Karen","Esteban":24, "Tupla":Tupla_Diccionario}
print(Mi_Diccionario2)

#.keys me devuelve las claves, .len me dice la extensión, .values me bota los valores
print(Mi_Diccionario2.keys())
print(Mi_Diccionario2.values())
print(len (Mi_Diccionario2))