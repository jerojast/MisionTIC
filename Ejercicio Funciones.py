# def Nombre_Funcion (par1, par2, ..., parn):
    #Instrucciones
    #return Lo que requiera devolver de las instrucciones

def funcion_suma (num1, num2):
    totalsuma = num1 + num2
    mensaje = "La suma de los números introducidos es: " + str(totalsuma)
    return mensaje

suma1 = funcion_suma (154645465486464516816541654851621684684616548, 145215487965424155865565)

print(suma1)

suma1 = funcion_suma (14785214785236985214785268524585698525625586482428624521452145284154, 25214569852145985214585214587521587525874521458752585215248585)

print(suma1)

#Vamos a escribir una función que calcule el volumen de un sólido
# 3 parámetros Alto, Ancho, Longitud (Paralelepipedo rectangular)
 
def Volumen_Solido ( alto, ancho, longitud):

    Volumen = alto * ancho * longitud

    Resultado_texto = "El volumen del sólido es: " + str (Volumen)
    
    return Resultado_texto

Intento1 = Volumen_Solido( 7 , 10 , 5 )
print(Intento1)
##############################################
#Hacer un función que retorne una cadena de texto
#Si el número del parámetro es par "El número XXX es par"
#Si el número del parámetro es impar "El número XXX es impar"

def numero_par_impar (a):

    if a%2 == 0:

        mensaje = "El número " + str(a) + " es par."
    
    else:

        mensaje = "El número " + str(a) + " es impar."

    return mensaje

Intento1 = numero_par_impar(52)

print(Intento1)



