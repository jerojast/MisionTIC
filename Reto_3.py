def AutoPartes (ventas : list):
    diccionario = {}
    for idProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador,fVenta in ventas:
        if diccionario.get(idProducto) == None:
            diccionario [idProducto] = []
        diccionario[idProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador,fVenta))
    return diccionario


def consultaRegistro (ventas, idProducto):
    if idProducto in ventas:
        for dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            print ("Producto consultado : " + str(idProducto) + "  Descripción  " 
            + str(dProducto) + "  #Parte  " + str(pnProducto) + "  Cantidad vendida  " 
            + str(cvProducto) + "  Stock  " + str(sProducto) + "  Comprador " + str(nComprador) 
            + "  Documento  " + str(cComprador) + "  Fecha Venta  " + str(fVenta))
    else:
        print("No hay registro de venta de ese producto")
    return


