Mi_Lista=["Karen","Claus","Jorge","Esteban","Lucky","Chucky","Kira"]

#Para imprimir todo la lista se usa [:]

print(Mi_Lista[:])

#Para acceder a uno de los elementos de la lista se utiliza en índice del elemento

print(Mi_Lista[1])

#Los índices negativos los cuenta desde el final de la lista

print(Mi_Lista[-4])

#la proción de lista incluye el inicio pero no el final de la porción

print(Mi_Lista[0:3])

#Puedo omitir el 0 y python lo lee desde el primer índice

print(Mi_Lista[:3])

#Puedo omitir el último número lo que le diré es que lea desde el que yo le diga hasta el último

print(Mi_Lista[4:])

#Puedo agregar un elemento a mi lista utilizando .append

Mi_Lista.append("Familia")

print(Mi_Lista[:])

#Si en determinado caso quiero agregar un elemento pero en una posición que yo le indique debo usar .insert

Mi_Lista.insert(4,"Feliz")

print(Mi_Lista)

#Si quiero agregar más de un elemento a mi lista debo utilizar extend

Mi_Lista.extend(["Mascotas","Hogar","Prosperidad"])

print(Mi_Lista)

#Para conocer el índice de un elemento debo utilizar .index

print(Mi_Lista.index("Mascotas"))

#Si el elemento está repetido y pregunto por el índice de dicho elemento, el me arroja el que primero encuentre en la lista

#Si quiero conocer si determinado elemento está en la lista debo utilizar in y me arroja un True o un False

print("Feliz" in Mi_Lista)

#Puedo manejar varios tipos de datos (Números decimales o enteros, textos, booleanos)

Mi_Lista2=["Karen",6.45,"Jorge",5,True,False]
print(Mi_Lista2[0])

#Para eliminar un elemento de la lista se debe utilizar .remove 

Mi_Lista2.remove(6.45)

print(Mi_Lista2[:])

#Para eliminar el último elemento se usa .pop

Mi_Lista2.pop()

print(Mi_Lista2[:])

#Puedo sumar las listas usando +

Mi_Lista3=Mi_Lista+Mi_Lista2

print(Mi_Lista3[:])

#el * va a repetir el número de veces que yo quiera las lista 

print((Mi_Lista3[:])*5)