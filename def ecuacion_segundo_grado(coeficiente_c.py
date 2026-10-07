def ecuacion_segundo_grado(coeficiente_cuadratico, coeficiente_lineal,  termino_independiente):

    import math  #importar modulo matematico

    cuadrado = (coeficiente_lineal * coeficiente_lineal)
    multiplicacion = (4 * coeficiente_cuadratico * termino_independiente)
    discriminante = (cuadrado - multiplicacion)

    if (discriminante >= 1):

        solucion_positiva = ((-coeficiente_lineal + math.sqrt(discriminante))/(2 * coeficiente_cuadratico))

        solucion_negativa = ((-coeficiente_lineal - math.sqrt(discriminante))/(2 * coeficiente_cuadratico))

        print (int(solucion_positiva), int (solucion_negativa))

    if (discriminante < 0 ):

        print ("no hay solucion")

ecuacion_segundo_grado(1,-5,6)