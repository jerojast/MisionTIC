informacion = {}

informacion ["id_cliente"] = int ()
informacion ["nombre"] = str ()
informacion ["edad"] = int ()
informacion ["primer_ingreso"] = bool ()

def cliente (informacion:dict):
    resultado = {}
    
    resultado ["nombre"] = informacion ["nombre"]
    resultado ["edad"] = informacion ["edad"]
            
    if resultado ["edad"] > 18:
        apto = True
        atraccion = "X-Treme"
        valor_ticket = 20000
    elif 15 <= resultado ["edad"] <= 18:
        apto = True
        atraccion = "Carros chocones"
        valor_ticket = 5000
    elif  7 <= resultado ["edad"] < 15:
        apto = True
        atraccion = "Sillas voladoras"
        valor_ticket = 10000
    else:
        apto = False
        atraccion = "N/A"
        valor_ticket = "N/A"

    resultado ["atraccion"] = atraccion
    resultado ["apto"] = apto
    resultado ["primer_ingreso"] = informacion ["primer_ingreso"]

    if resultado ["primer_ingreso"] == True and valor_ticket == 20000:
        totalpago = valor_ticket * 0.95
    elif resultado ["primer_ingreso"] == True and valor_ticket == 5000:
        totalpago = valor_ticket * 0.93
    elif resultado ["primer_ingreso"] == True and valor_ticket == 10000:
        totalpago = valor_ticket * 0.95
    else:
        totalpago = valor_ticket

    resultado ["total_boleta"] = totalpago

    return resultado

