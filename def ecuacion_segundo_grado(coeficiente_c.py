def ecuacion_segundo_grado(coeficiente_cuadratico, coeficiente_lineal,  termino_independiente):

    import math  #importar modulo matematico

    coeficiente_cuadratico =1
    coeficiente_lineal =2
    termino_independiente =3

    cuadrado = (coeficiente_lineal * coeficiente_lineal)
    multiplicacion = (4 * coeficiente_cuadratico * termino_independiente)
    discriminante = cuadrado - multiplicacion

    if (discriminante >= 1):

        solucion_positiva = (-coeficiente_lineal + ((math.sqrt(cuadrado-multiplicacion))/(2 * coeficiente_cuadratico)))

        solucion_negativa = (-coeficiente_lineal - ((math.sqrt(cuadrado-multiplicacion))/(2 * coeficiente_cuadratico)))

        print ("solucion_positiva, solucion_negativa")

    if (discriminante<=1):

        print ("no hay solucion")