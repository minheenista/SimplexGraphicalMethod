# Librerías
import numpy as np  # Calculos matemáticos
import matplotlib.pyplot as plt  # para hacer plots graficas
import math  # Matemáticas
from tokenize import tokenize  # Función para separar por tokens posiciones
from io import BytesIO  # Poder leer linea terminal
import customtkinter  # Estilacho GUI <-

inicio = customtkinter.CTk()  # Hacer un mainframe
inicio.geometry('400x400')  # Especificas el tamaño del mainframe
inicio.title("Método Gráfico")


# Calculos
def calculos():
    global datosFuncObj
    global datosRes1
    global datosRes2
    global datosRes3
    global resultadoFinal
    combinacionFinal = 0
    datosFuncObj = []
    datosRes1 = []
    datosRes2 = []
    datosRes3 = []
    resultadoFinal = []
    valorFuncObj = entryFunObjetivo.get()
    valorRes1 = res1.get()
    valorRes2 = res2.get()
    global punto1Inters1
    global punto2Inters1
    global punto1Inters2
    global punto2Inters2
    global punto1Inters3
    global punto2Inters3
    global extremoY
    global extremoX
    global x1FuncObj
    global x2FuncObj
    global optionmenu
    global punto1Res1
    global punto2Res1
    global punto1Res2
    global punto2Res2
    global punto1Res3
    global punto2Res3
    global xs
    global ys
    global stringResCombinacion
    global stringResultado
    global numResFinal
    punto1Res1 = []
    punto2Res1 = []
    punto1Res2 = []
    punto2Res2 = []
    punto1Res3 = []
    punto2Res3 = []
    xs = []
    ys = []
    stringResCombinacion = ""
    stringResultado = ""
    numResFinal = 0

    # Token para la func objetivo
    tokenFuncObj = tokenize(BytesIO(valorFuncObj.encode('utf-8')).readline)
    non_empty = [t for t in tokenFuncObj if t.line != '']
    for tokenFuncObj in non_empty:
        datosFuncObj.append(tokenFuncObj.string)
        # 1.-2 #2.-x1 3.- +/- ...

    # Token de la restriccion 1:
    tokenRes1 = tokenize(BytesIO(valorRes1.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes1 if t.line != '']
    for tokenRes1 in non_empty:
        datosRes1.append(tokenRes1.string)

    # Token de la restriccion 2
    tokenRes2 = tokenize(BytesIO(valorRes2.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes2 if t.line != '']
    for tokenRes2 in non_empty:
        datosRes2.append(tokenRes2.string)

    datosFuncObj = np.array(datosFuncObj)
    datosRes2 = np.array(datosRes2)
    datosRes1 = np.array(datosRes1)

    # DATOS RECIBIDOS DEL DUAL _________________________________________________________________________________________________________________

    # Función objetivo
    x1FO = int(datosFuncObj[2])
    x2FO = int(datosFuncObj[5])
    x3FO = int(datosFuncObj[8])

    # Restriccion 1
    x1R1 = float(datosRes1[0])
    x2R1 = float(datosRes1[3])
    x3R1 = float(datosRes1[6])
    constR1 = float(datosRes1[9])

    # Restriccion 2
    x1R2 = float(datosRes2[0])
    x2R2 = float(datosRes2[3])
    x3R2 = float(datosRes2[6])
    constR2 = float(datosRes2[9])

    # MAXIMIZACIÓN ____________________________________________________________________________________________________________________________

    # x1FuncObj = int(datosFuncObj[2])  # Valor de x1                         //Constante de Restricción 1    temp
    x1FuncObj = constR1
    # x2FuncObj = int(datosFuncObj[5])  # Valor de x2                         //Constante de Restricción 2    temp
    x2FuncObj = constR2

    # RESTRICCIÓN 1
    # temp = float(datosRes1[6])      #=                                      //x1 de Función objetivo        x1FuncObj
    temp = x1FO
    # temp2 = float(datosRes1[3])     #x2                                     //x1 restriccion 2
    temp2 = x1R2
    temp3 = temp / temp2
    punto1Res1.append(0)
    punto1Res1.append(temp3)
    # punto1Res1 = np.array(punto2Res1)
    ys.append(temp3)
    # temp = float(datosRes1[6])      #=                                      //x1 de Función objetivo        x1FuncObj
    temp = x1FO
    # temp2 = float(datosRes1[0])     #x1                                     //x1 restriccion 1
    temp2 = x1R1
    temp3 = temp / temp2
    punto2Res1.append(temp3)
    xs.append(temp3)
    punto2Res1.append(0)

    # RESTRICCIÓN 2

    # temp = float(datosRes2[6])      #=                                      //x2 de Función objetivo
    temp = x2FO
    # temp2 = float(datosRes2[3])     #x2                                     //x2 restriccion 2
    temp2 = x2R2
    temp3 = temp / temp2
    punto1Res2.append(0)
    punto1Res2.append(temp3)
    ys.append(temp3)
    # temp = float(datosRes2[6])      #=                                      //x2 de Función objetivo
    temp = x2FO
    # temp2 = float(datosRes2[0])     #x1                                     //x2 restriccion 1
    temp2 = x2R1
    temp3 = temp / temp2
    punto2Res2.append(temp3)
    xs.append(temp3)
    punto2Res2.append(0)

    # RESTRICCIÓN 3

    # temp = float(datosRes3[6])      #=                                      //x3 de Función objetivo
    temp = x3FO
    # temp2 = float(datosRes3[3])     #x2                                     //x3 restriccion 2
    temp2 = x3R2
    temp3 = temp / temp2
    punto1Res3.append(0)
    punto1Res3.append(temp3)
    ys.append(temp3)
    # temp = float(datosRes3[6])      #=                                      //x3 de Función objetivo
    temp = x3FO
    # temp2 = float(datosRes3[0])     #x2                                     //x3 restriccion 1
    temp2 = x3R1
    temp3 = temp / temp2
    punto2Res3.append(temp3)
    xs.append(temp3)
    punto2Res3.append(0)

    # intersección linea uno con línea dos
    value1 = x1R1
    value2 = x1R2
    value3 = x2R1
    value4 = x2R2
    value5 = x1FO
    value6 = x2FO
    A = np.array([[value1, value2], [value3, value4]])
    B = np.array([value5, value6])
    X = np.linalg.inv(A).dot(B)
    punto1Inters1 = X[0]
    punto2Inters1 = X[1]

    # intersección linea uno con línea tres
    value1 = x1R1
    value2 = x1R2
    value3 = x3R1
    value4 = x3R2
    value5 = x1FO
    value6 = x3FO
    A = np.array([[value1, value2], [value3, value4]])
    B = np.array([value5, value6])
    X = np.linalg.inv(A).dot(B)
    punto1Inters2 = X[0]
    punto2Inters2 = X[1]
    # intersección linea dos con línea tres
    value1 = x2R1
    value2 = x2R2
    value3 = x3R1
    value4 = x3R2
    value5 = x2FO
    value6 = x3FO
    A = np.array([[value1, value2], [value3, value4]])
    B = np.array([value5, value6])
    X = np.linalg.inv(A).dot(B)
    punto1Inters3 = X[0]
    punto2Inters3 = X[1]

    # evaluamos lo que tenga el radioButton, 1 es máximizar y 2 es minimizar
    if optionmenu.get() == "Maximizar":
        extremoY = np.min(ys)
        extremoX = np.min(xs)
    elif optionmenu.get() == "Minimizar":
        extremoY = np.max(ys)
        extremoX = np.max(xs)

    # Ahora calculamos el resultado para minimizar
    tempRes = (punto1Inters1 * x1FuncObj) + (punto2Inters1 * x2FuncObj)
    resultadoFinal.append(tempRes)
    tempRes = (punto1Inters2 * x1FuncObj) + (punto2Inters2 * x2FuncObj)
    resultadoFinal.append(tempRes)
    tempRes = (punto1Inters3 * x1FuncObj) + (punto2Inters3 * x2FuncObj)
    resultadoFinal.append(tempRes)
    # extremos
    tempRes = (0 * x1FuncObj) + (extremoY * x2FuncObj)
    resultadoFinal.append(tempRes)
    tempRes = (extremoX * x1FuncObj) + (0 * x2FuncObj)
    resultadoFinal.append(tempRes)
    # Calcular que restricción tenemos que evitar, siempre se evita la más pequeña
    # first = second = math.inf
    if optionmenu.get() == "Maximizar":  # máximizar
        first = second = 0
        for i in range(0, len(resultadoFinal)):
            if resultadoFinal[i] > first:
                second = first
                first = resultadoFinal[i]
                # first = resultadoFinal[i]
                # combinacionFinal = i
            elif (resultadoFinal[i] > second and resultadoFinal[i] != first):
                second = resultadoFinal[i]
                combinacionFinal = i

        numResFinal = second
    elif optionmenu.get() == "Minimizar":  # minimizar
        first = second = math.inf
        for i in range(0, len(resultadoFinal)):
            if resultadoFinal[i] < first:
                second = first
                first = resultadoFinal[i]
            elif (resultadoFinal[i] < second and resultadoFinal[i] != first):
                second = resultadoFinal[i]
                combinacionFinal = i

        numResFinal = second
    # imprimimos el resultado
    if combinacionFinal == 0:
        stringResCombinacion = "Mejor combinación: \n x1 = " + str(round(punto1Inters1)) + "\n x2 = " + str(round(
            punto2Inters1))
        stringResultado = "En total se generan: " + str(round(numResFinal)) + " unidades."
    elif combinacionFinal == 1:
        stringResCombinacion = "Mejor combinación: \n x1 = " + str(round(punto1Inters2)) + "\n x2 = " + str(
            round(punto2Inters2))
        stringResultado = "En total se generan: " + str(round(numResFinal)) + " unidades."
    elif combinacionFinal == 2:
        stringResCombinacion = "Mejor combinación: \n x1 = " + str(round(punto1Inters3)) + "\n x2 = " + str(
            round(punto2Inters3))
        stringResultado = "En total se generan: " + str(round(numResFinal)) + " unidades."
    elif combinacionFinal == 3:
        stringResCombinacion = "Mejor combinación: \n x1 = 0 \n x2 = " + str(round(extremoY))
        stringResultado = "En total se generan: " + str(round(numResFinal)) + " unidades."

    elif combinacionFinal == 4:
        stringResCombinacion = "Mejor combinación \n x1 = " + str(round(extremoX)) + "\n x2 = 0"
        stringResultado = "En total se generan: " + str(round(numResFinal)) + " unidades."

    resCombEtiqueta = customtkinter.CTkLabel(inicio, text=stringResCombinacion)
    resCombEtiqueta.grid(row=8, column=1)
    resEtiqueta = customtkinter.CTkLabel(inicio, text=stringResultado)
    resEtiqueta.grid(row=9, column=1)


# \n


def grafica():
    plt.plot(punto2Res1, punto1Res1)
    plt.plot(punto2Res2, punto1Res2)
    plt.plot(punto2Res3, punto1Res3)
    plt.plot(punto1Inters1, punto2Inters1, marker="o")
    plt.plot(punto1Inters2, punto2Inters2, marker="o")
    plt.plot(punto1Inters3, punto2Inters3, marker="o")
    plt.plot(0, extremoY, marker="o")
    plt.plot(extremoX, 0, marker="o")
    plt.grid()
    plt.show()


# Ingresar datos
labelRestriccion = customtkinter.CTkLabel(inicio, text="Ingrese la función de la manera z=Ax1+Bx2+Cx3 ", fg_color="transparent")
labelRestriccion.grid(row=0, column=1)
labelFunObjetivo = customtkinter.CTkLabel(inicio, text="Función objetivo: ",
                                          fg_color="transparent")  # label = parrafo (texto)
labelFunObjetivo.grid(row=1, column=0)
entryFunObjetivo = customtkinter.CTkEntry(inicio, corner_radius=6)  # Crear el objeto (widgets)
entryFunObjetivo.grid(row=1, column=1, pady=5)  # Imprimir el objeto - Entry = cajita de texto (entrada)

# Restriccion 1
labelRestriccion = customtkinter.CTkLabel(inicio, text="Ingrese la restricción de la manera Ax1+Bx2+Cx3=D", fg_color="transparent")
labelRestriccion.grid(row=2, column=1)
labelRestriccion = customtkinter.CTkLabel(inicio, text="Restricción 1: ", fg_color="transparent")
labelRestriccion.grid(row=3, column=0)
res1 = customtkinter.CTkEntry(inicio)
res1.grid(row=3, column=1, pady=5)

# Restriccion 2
labelRestriccion = customtkinter.CTkLabel(inicio, text="Restricción 2: ", fg_color="transparent")
labelRestriccion.grid(row=4, column=0)
res2 = customtkinter.CTkEntry(inicio)
res2.grid(row=4, column=1, pady=5)

# optionmenuar max o min
optionmenu = customtkinter.CTkOptionMenu(inicio, values=["Maximizar"])
optionmenu.set("Maximizar")
optionmenu.grid(row=5, column=1, pady=15)

calcularButton = customtkinter.CTkButton(inicio, text="Calcular", command=calculos, fg_color="#8762d1")
calcularButton.grid(row=6, column=1, sticky="w", pady=15)

graficarButton = customtkinter.CTkButton(inicio, text="Graficar", command=grafica, fg_color="#8762d1")
graficarButton.grid(row=7, column=1, sticky="w", pady=15)

inicio.mainloop()  # No se cierre el mainframe