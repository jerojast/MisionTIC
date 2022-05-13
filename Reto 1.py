
def CDT():

    print("Inicio del programa")
    
        
    print("Por favor introduzca su usuario: ")
    
    usuario = str ( input() )

    print("Por favor introuzca el capital que desea invertir en COP: ")

    capital = int (input())

    print("Por favor introduzca el tiempo en meses que desea dejar su capital invertido: ")

    tiempo = int (input())

    if capital>0:

        if tiempo > 2:

            interesescdt = ((capital*0.03*tiempo)//12)

            valor_total_cdt = interesescdt+capital

            print("Para el usuario " + usuario + " la cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total_cdt))
    
        else:

            valor_perdida = capital*0.02

            valor_total_perdida = capital-valor_perdida

            print("Para el usuario " + usuario + " la cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total_perdida))

    else:

        print("El valor a invertir no puede ser negativo")
    
    print ("Fin del programa")

CDT()

#A partir de acá el código que superó la prueba

def CDT(usuario: str, capital: int, tiempo: int):

    if tiempo>2:
        
        intereses_cdt = ((capital*0.03*tiempo)//12)
        
        valor_total = (capital+intereses_cdt)
        
        respuesta = ("Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total))
        
    else:
        
        valor_perdido = capital*0.02
        
        valor_perdida = capital-valor_perdido
        
        respuesta = ("Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_perdida))

    return (respuesta)

