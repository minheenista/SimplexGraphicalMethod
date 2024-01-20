import numpy as np
import matplotlib.pyplot as plt

def solve_simplex(graphic_method=True):
    # Ingresar datos
    print("\n \n \n ------------ MÉTODO GRÁFICO - MAXIMIZAR ----------- \n \n")
    n = 2
    print("Ingrese el número de restricciones:")
    m = int(input())

    print("Ingrese los coeficientes de la función objetivo (Z):")
    c = []
    for i in range(n):
        print("Coeficiente para x" + str(i+1) + ":")
        coef = float(input())
        c.append(coef)

    print("Ingrese las restricciones en la forma Ax <= b:")
    A = np.zeros((m, n))
    b = np.zeros(m)
    for i in range(m):
        print("Restricción " + str(i+1) + ":")
        for j in range(n):
            print("Coeficiente para x" + str(j+1) + ":")
            coef = float(input())
            A[i][j] = coef
        print("Valor de constante:")
        b[i] = float(input())

    # Resolver utilizando el método gráfico
    if graphic_method:
        # Encontrar las intersecciones de las restricciones
        vertices = []
        for i in range(m):
            for j in range(i+1, m):
                x = np.linalg.solve([A[i], A[j]], [b[i], b[j]])
                if (x >= 0).all():
                    vertices.append(x)

        # Encontrar la solución óptima en los vértices
        z = np.dot(c, vertices[0])
        opt_vertex = vertices[0]
        for vertex in vertices[1:]:
            z_vertex = np.dot(c, vertex)
            if z_vertex > z:
                z = z_vertex
                opt_vertex = vertex

        # Mostrar resultados
        print("El punto óptimo es:", opt_vertex)
        print("El valor óptimo de la función objetivo (Z) es:", z)
        print("Para maximizar, se deben producir ", round(opt_vertex[0], 2), " de x1 y ", round(opt_vertex[1], 2), " de x2, para obtener los margenes de ganancia de ", round(z, 2))

        # Graficar las restricciones y la solución óptima
        for i in range(m):
            plt.plot([0, b[i]/A[i][1]], [b[i]/A[i][0], 0], label="Restricción " + str(i+1))

        plt.scatter(opt_vertex[1], opt_vertex[0], color='red', label="Punto óptimo")
        plt.xlabel('x2')
        plt.ylabel('x1')
        plt.legend()
        plt.grid(True)
        plt.show()

    else:
        print("La opción seleccionada no es válida.")

# Ejecutar la función para resolver el problema
solve_simplex(graphic_method=True)